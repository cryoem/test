# Helper functions from Pawel Penczek
# Please do not alter this file without permision from the author.

from EMAN2 import *
from math import *
from time import *
from random import *

def getImage(imagename, nx = 0, ny = 1, nz = 1):
    """Read an image from the disk or assign existing object to the output.

    Usage: myimage = readImage("path/to/image")
    or     myimage = readImage(name_of_existing_image)
    """
    if type(imagename) == type(""):
        e = EMData()
        e.read_image(imagename)
    elif not imagename:
        e = EMData()
        if (nx > 0):
            e.set_size(nx, ny, nz)
    else:
        e = imagename
    return e

def dropImage(imagename,destination):
    """Write an image to the disk or assign to an output object.

    Usage:  dropImage(name_of_existing_image,"path/to/image")
    or      dropImage(name_of_existing_image,myimage)
    """
    if type(destination) == type(""):
        imagename.write_image(destination,0,SINGLE_SPIDER)
    else:
        destination = EMData()
        destination = imagename

def info(image):
    """Calculate and print the descriptive statistics of an image.

    Usage: [mean, sigma, xmin, xmax, nx, ny, nz =] info(image object)
           or
           [mean, sigma, xmin, xmax, nx, ny, nz =] info("path/image")

    Purpose: calculate basic statistical characteristics of an image.
    """
    e = getImage(image)
    mean = e.get_attr("mean")
    sigma = e.get_attr("sigma")
    imin = e.get_attr("minimum")
    imax = e.get_attr("maximum")
    nx = e.get_xsize()
    ny = e.get_ysize()
    nz = e.get_zsize()
    if (e.is_complex()):
    	if (e.is_fftodd()):
    		print "Complex odd image: nx = %i, ny = %i, nz = %i" % (nx, ny, nz)
	else:
    		print "Complex even image: nx = %i, ny = %i, nz = %i" % (nx, ny, nz)

    else:
    	print "Real image: nx = %i, ny = %i, nz = %i" % (nx, ny, nz)

    print "avg = %g, std dev = %g, min = %g, max = %g" % (mean, sigma, imin, imax)
    return mean,sigma,imin,imax, nx, ny, nz
    

def printRow(input, ix=0, iz=0):
    """Print the data in slice iz, row ix of an image to standard out.

    Usage: printRow(image, ix, iz)
       or
           printRow("path/to/image", ix, iz)
    """
    image=getImage(input)
    nx = image.get_xsize()
    ny = image.get_ysize()
    nz = image.get_zsize()
    print "(z = %d slice, x = %d row)" % (iz, ix)
    line = []
    for iy in xrange(ny):
        line.append("%12.5g  " % (image.get_value_at(ix,iy,iz)))
        if ((iy + 1) % 5 == 0):
            line.append("\n   ")
    line.append("\n")
    print "".join(line)

def printCol(input, iy=0, iz=0):
    """Print the data in slice iz, column iy of an image to standard out.

       Usage: printCol(image, iy, iz)
          or
              printCol("path/to/image", iy, iz)
    """
    image=getImage(input)
    nx = image.get_xsize()
    ny = image.get_ysize()
    nz = image.get_zsize()
    print "(z = %d slice, y = %d col)" % (iz, iy)
    line = []
    for ix in xrange(ny):
        line.append("%12.5g  " % (image.get_value_at(ix,iy,iz)))
        if ((ix + 1) % 5 == 0):
            line.append("\n   ")
    line.append("\n")
    print "".join(line)

def printSlice(input, iz=0):
    """Print the data in slice iz of an image to standard out.

    Usage: printImage(image, int)
       or
           printImage("path/to/image", int)
    """
    image=getImage(input)
    nx = image.get_xsize()
    ny = image.get_ysize()
    nz = image.get_zsize()
    print "(z = %d slice)" % (iz)
    line = []
    for ix in xrange(nx):
        for iy in xrange(ny):
            line.append("%12.5g  " % (image.get_value_at(ix,iy,iz)))
            if ((iy + 1) % 5 == 0):
                line.append("\n   ")
        line.append("\n")
    print "".join(line)

def printImage(input):
    """Print the data in an image to standard out.

    Usage: printImage(image)
       or
           printImage("path/to/image")
    """
    image=getImage(input)
    nz = image.get_zsize()
    for iz in xrange(nz):
        printSlice(input, iz)


def add_series(file_pattern,i1,i2,average,variance):
    """ Calculate average and variance files for an image series
    
    Usage:  add_series("img****.ext",i1,i2,average,variance)
      i1 - first file in image series
      i2 - last file in image series
      average and variance are output objects, or, if written as "a", are output disk files
      
    """
    fname = Util.parse_spider_fname(file_pattern,[i1]) #f=file_pattern[i1]
    ave = getImage(fname)
    var = ave*ave  #pow(ave,2.0)
    descriptive_statistics(ave)

    # process the remaining files
    for index in range(i1+1,i2+1):
        fname = Util.parse_spider_fname(file_pattern,[index])
        e = getImage(fname)
        ave = ave + e
        var = var + e*e  #pow(e,2.0)
    
    print "sum"
    descriptive_statistics(ave)
    ii=i2-i1+1
    ave = ave/ii
    print "average"
    descriptive_statistics(ave)
    #var = (var - pow(ave,2)/ii)/(ii-1)
    var = (var - ave*ave*ii)/(ii-1)
    print "variance"
    descriptive_statistics(var)

    dropImage(ave,average)
    dropImage(var,variance)


def do_reconstruction(filepattern, start, end, anglelist, symmetry="c1"):
    """Perform a 3-D reconstruction using Pawel's FFT Back Projection algoritm.
       
       Input:
         filepattern -- string such as "foo{****}.ext" that will be
                        used to determine the filenames of the 
                        projections to be read in.
        start        -- initial integer value to put in the field
        end          -- final integer value to put in the field
        anglelist    -- flat list of euler angles (in degrees), with the
                        number of euler angles equal to the number of 
                        projections to be read in.
        symmetry     -- Point group of the target molecule (defaults to "C1")
    
       Return:  3d reconstructed volume image

       Usage:
         
         anglelist = getAngles("myangles.txt") # not yet written
         filepattern = "proj{****}.hrs"
         start = 0
         end = 5087
         vol = do_reconstruction(filepattern, start, end, anglelist, symmetry)
    """
    from math import radians
    npad = 4
    # convert angles to transform (rotation) objects
    nangles = len(anglelist) / 3
    rotations = []
    for i in range(nangles):
        phi = radians(anglelist[3*i])
        theta = radians(anglelist[3*i+1])
        psi = radians(anglelist[3*i+2])
        Ttype = Transform3D.EulerType.SPIDER
        rotations.append(Transform3D(Ttype, phi, theta, psi))
        
    # read first image to determine the size to use
    projname = Util.parse_spider_fname(filepattern,[start]) 
    first = getImage(projname)
    size = first.get_xsize()
    # sanity check -- image must be square
    if first.get_xsize() != first.get_ysize():
        print "Image projections must be square!"
        # FIXME: throw exception instead
        return None
    del first # don't need it any longer
    # reconstructor
    params = {"size":size, "npad":npad, "symmetry":symmetry}
    r = Reconstructors.get("PawelBackProjection", params)
    r.setup()
    for i in range(start, end+1):
        projname = Util.parse_spider_fname(filepattern,[i])
        projection = getImage(projname)
        r.insert_slice(projection, rotations[i])
    v = r.finish()
    return v

def create_write_projections(volume, filepattern, anglelist, radius):
    nangles = len(anglelist) / 3
    for i in range(nangles):
        myangles = anglelist[3*i:3*(i+1)] # just a single slice of phi, theta, psi
        myparams = {"angletype":"SPIDER",
                    "anglelist":myangles,
                    "radius":radius}
        proj = volume.project("Pawel",myparams)
        projname = Util.parse_spider_fname(filepattern, [i])
        proj.write_image(projname, 0, EMUtil.ImageType.IMAGE_SINGLE_SPIDER)

def do_alignment(exptpattern, start, end, refpattern, alipattern, anglelist):
    newangles = []
    for i in range(start, end+1):
        exptname = Util.parse_spider_fname(exptpattern, [i])
        aliname  = Util.parse_spider_fname(alipattern, [i])
        exptimage = getImage(exptname)
        nangles = len(anglelist) / 3
        for ref in range(nangles):
            refname = Util.parse_spider_fname(refpattern, [ref])
            refimage = getImage(refname)
            #  do something real here
        # this next bit is utter rubbish just so the code "works"
        aliimage = exptimage 
        aliimage.write_image(aliname, 0, EMUtil.ImageType.IMAGE_SINGLE_SPIDER)
        newangles.append(1.0)
        newangles.append(2.0)
        newangles.append(3.0)
    return newangles

# shortcuts to Fourier product functions
# Correlation functions
def ccf(e, f):
    o = correlation(e,f,fp_flag.CIRCULANT)
    return o

def ccfn(e, f):
    o = correlation(e,f,fp_flag.CIRCULANT_NORMALIZED)
    return o

def ccfp(e, f):
    o = correlation(e,f,fp_flag.PADDED)
    return o

def ccfnp(e, f):
    o = correlation(e,f,fp_flag.PADDED_NORMALIZED)
    return o

def ccfpl(e, f):
    o = correlation(e,f,fp_flag.PADDED_LAG)
    return o

def ccfnpl(e, f):
    o = correlation(e,f,fp_flag.PADDED_NORMALIZED_LAG)
    return o
    
# Convolution functions
def cnv(e, f):
    o = convolution(e,f,fp_flag.CIRCULANT)
    return o

def cnvn(e, f):
    o = convolution(e,f,fp_flag.CIRCULANT_NORMALIZED)
    return o

def cnvp(e, f):
    o = convolution(e,f,fp_flag.PADDED)
    return o

def cnvnp(e, f):
    o = convolution(e,f,fp_flag.PADDED_NORMALIZED)
    return o

def cnvpl(e, f):
    o = convolution(e,f,fp_flag.PADDED_LAG)
    return o

def cnvnpl(e, f):
    o = convolution(e,f,fp_flag.PADDED_NORMALIZED_LAG)
    return o
    
# Autocorrelation functions
def acf(e, f):
    o = autocorrelation(e,f,fp_flag.CIRCULANT)
    return o

def acfn(e, f):
    o = autocorrelation(e,f,fp_flag.CIRCULANT_NORMALIZED)
    return o

def acfp(e, f):
    o = autocorrelation(e,f,fp_flag.PADDED)
    return o

def acfnp(e, f):
    o = autocorrelation(e,f,fp_flag.PADDED_NORMALIZED)
    return o

def acfpl(e, f):
    o = autocorrelation(e,f,fp_flag.PADDED_LAG)
    return o

def acfnpl(e, f):
    o = autocorrelation(e,f,fp_flag.PADDED_NORMALIZED_LAG)
    return o
   
    
# Selfcorrelation functions
def scf(e, f):
    o = self_correlation(e,f,fp_flag.CIRCULANT)
    return o

def scfn(e, f):
    o = self_correlation(e,f,fp_flag.CIRCULANT_NORMALIZED)
    return o

def scfp(e, f):
    o = self_correlation(e,f,fp_flag.PADDED)
    return o

def scfnp(e, f):
    o = self_correlation(e,f,fp_flag.PADDED_NORMALIZED)
    return o

def scfpl(e, f):
    o = self_correlation(e,f,fp_flag.PADDED_LAG)
    return o

def scfnpl(e, f):
    o = self_correlation(e,f,fp_flag.PADDED_NORMALIZED_LAG)
    return o
    
# FFT functions
def fft(e):
    """Out-of-place fft / ift
       No padding performed, and fft-extension along x removed after ift.
    """
    if (e.is_complex()):
        # inverse fft
        f = e.copy()
        f.do_ift_inplace()
        f.postift_depad_corner_inplace()
        return f
    else:
        # forward fft
        return norm_pad_ft(e, False, False, 1)

def fftip(e):
    """In-place fft / ift
       No padding performed, and fft-extension along x removed after ift.
    """
    if (e.is_complex()):
        # inverse fft
        e.do_ift_inplace()
        e.postift_depad_corner_inplace()
    else:
        # forward fft
        e.do_fft_inplace()

# Fourier filters
def filt_tophatl(e, freq):
    params = {"FilterType" : Processor.fourier_filter_types.TOP_HAT_LOW_PASS,
              "Cutoff_frequency" : freq}
    return Processor.EMFourierFilter(e, params)
    
def filt_tophath(e, freq):
    params = {"FilterType" : Processor.fourier_filter_types.TOP_HAT_HIGH_PASS,
              "Cutoff_frequency" : freq}
    return Processor.EMFourierFilter(e, params)
    
def filt_tophatb(e, freql, freqh):
    params = {"FilterType" : Processor.fourier_filter_types.TOP_HAT_BAND_PASS,
              "Low_cutoff_frequency" : freql, "High_cutoff_frequency" : freqh}
    return Processor.EMFourierFilter(e, params)
    
def filt_tophato(e, freql, freqh, value):
    params = {"FilterType" : Processor.fourier_filter_types.TOP_HOMOMORPHIC,
              "Low_cutoff_frequency" : freql, "High_cutoff_frequency" : freqh, "Value_at_zero_frequency" : value}
    return Processor.EMFourierFilter(e, params)

    

def filt_gaussl(e, sigma):
    params = {"FilterType" : Processor.fourier_filter_types.GAUSS_LOW_PASS,
              "Sigma" : sigma}
    return Processor.EMFourierFilter(e, params)
    
def filt_gaussh(e, sigma):
    params = {"FilterType" : Processor.fourier_filter_types.GAUSS_HIGH_PASS,
              "Sigma" : freq}
    return Processor.EMFourierFilter(e, sigma)
    
def filt_gaussb(e, sigma, center):
    params = {"FilterType" : Processor.fourier_filter_types.GAUSS_BAND_PASS,
              "Sigma" : sigma, "Center" : center}
    return Processor.EMFourierFilter(e, params)
    
def filt_gausso(e, sigma, value):
    params = {"FilterType" : Processor.fourier_filter_types.GAUSS_HOMOMORPHIC,
              "Sigma" : sigma, "Value_at_zero_frequency" : value}
    return Processor.EMFourierFilter(e, params)



def filt_btwl(e, freql, freqh):
    params = {"FilterType" : Processor.fourier_filter_types.BUTTERWORTH_LOW_PASS,
              "Low_cutoff_frequency" : freql, "High_cutoff_frequency" : freqh}
    return Processor.EMFourierFilter(e, params)
    
def filt_btwh(e, freql, freqh):
    params = {"FilterType" : Processor.fourier_filter_types.BUTTERWORTH_HIGH_PASS,
              "Low_cutoff_frequency" : freql, "High_cutoff_frequency" : freqh}
    return Processor.EMFourierFilter(e, params)
    
def filt_btwh(e, freql, freqh, value):
    params = {"FilterType" : Processor.fourier_filter_types.BUTTERWORTH_HOMOMORPHIC,
              "Low_cutoff_frequency" : freql, "High_cutoff_frequency" : freqh,
	      "Value_at_zero_frequency" : value}
    return Processor.EMFourierFilter(e, params)
   
    

def filt_tanl(e, freq, fall_off):
    params = {"FilterType" : Processor.fourier_filter_types.TANH_LOW_PASS,
              "Cutoff_frequency" : freq, "Fall_off": fall_off}
    return Processor.EMFourierFilter(e, params)
    
def filt_tanh(e, freq, fall_off):
    params = {"FilterType" : Processor.fourier_filter_types.TANH_HIGH_PASS,
              "Cutoff_frequency" : freq, "Fall_off": fall_off}
    return Processor.EMFourierFilter(e, params)
    
def filt_tanb(e, freql, low_fall_off, freqh, high_fall_off):
    params = {"FilterType" : Processor.fourier_filter_types.TANH_BAND_PASS,
              "Low_cutoff_frequency" : freql, "Low_fall_off": low_fall_off,
	      "High_cutoff_frequency" : freqh, "High_fall_off": high_fall_off}
    return Processor.EMFourierFilter(e, params)
    
def filt_tano(e, freq, fall_off, value):
    params = {"FilterType" : Processor.fourier_filter_types.TANH_HOMOMORPHIC,
              "Cutoff_frequency" : freq, "Fall_off": fall_off,
	      "Value_at_zero_frequency" : value}
    return Processor.EMFourierFilter(e, params)
    

def parse_spider_fname(mystr, *fieldvals):
    """
    Parse a Spider filename string and insert parameters.

    Example input: "foo{***}/img{****}.mrc"
    This string has two fields that should be replaced by integers,
    and the number of '*'s determines how "wide" that field should be.
    So, if the parameters to be inserted are 10 and 3, then the resulting
    filename should be "foo010/img0003.mrc".

    Note: If the image is a stack file, the last character in the string
    must be a '@' (except for possible extraneous whitespace, which is
    ignored).  This stack symbol will be stripped in the output filename.

    Example:

       In [1]: mystr = "foo{***}/img{****}.mrc
       In [2]: parse_spider_fname(mystr, 10, 3)
       Out[2]: 'foo010/img0003.mrc'

    @param mystr Spider filename string to be parsed
    @param fieldvals Integer values to be placed into the fields

    @return Parsed filename
    """
    # helper functions and classes
    def rm_stack_char(mystr):
        "Helper function to remove a stack character if it exists"
        stackloc = mystr.find("@")
        if stackloc != -1: 
            # there's an '@' somewhere
            if len(mystr) - 1 == stackloc:
                # It's at the end of the string
                return mystr[:-1]
            else:
                # '@' not at the end, so it's an error
                raise ValueError, "Invalid format: misplaced '@'."
        else:
            # no '@' at all
            return mystr
    class Fieldloc:
        "Helper class to store description of a field"
        def __init__(self, begin, end):
            self.begin = begin
            self.end = end
        def count(self):
            "Size of the field (including braces)"
            return self.end - self.begin + 1
    def find_fields(mystr):
        "Helper function to identify and validate fields in a string"
        fields = []
        loc = 0
        while True:
            begin = mystr.find('{', loc)
            if begin == -1: break
            end = mystr.find('}', begin)
            field = Fieldloc(begin, end)
            # check validity
            asterisks = mystr[begin+1:end]
            if asterisks.strip("*") != "":
                raise ValueError, "Malformed {*...*} field: %s" % \
                    mystr[begin:end+1]
            fields.append(Fieldloc(begin, end))
            loc = end
        return fields
    # remove leading whitespace
    mystr.strip()
    # remove stack character (if it exists)
    mystr = rm_stack_char(mystr)
    # locate fields to replace
    fields = find_fields(mystr)
    if len(fields) != len(fieldvals):
        # wrong number of fields?
        raise ValueError, "Number of field values provided differs from" \
                          "the number of {*...*} fields."
    newstrfrags = []
    loc = 0
    for i, field in enumerate(fields):
        # text before the field
        newstrfrags.append(mystr[loc:field.begin])
        # replace the field with the field value
        fieldsize = field.count() - 2
        fielddesc = "%0" + str(fieldsize) + "d"
        newstrfrags.append(fielddesc % fieldvals[i])
        loc = field.end + 1
    newstrfrags.append(mystr[loc:])
    return "".join(newstrfrags)



