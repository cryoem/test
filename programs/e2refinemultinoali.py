#!/usr/bin/env python

#
# Author: Steve Ludtke, 1/18/2008 (sludtke@bcm.edu)
# Copyright (c) 2000-2007 Baylor College of Medicine
#
# This software is issued under a joint BSD/GNU license. You may use the
# source code in this file under either license. However, note that the
# complete EMAN2 and SPARX software packages have some GPL dependencies,
# so you are responsible for compliance with the licenses of these packages
# if you opt to use BSD licensing. The warranty disclaimer below holds
# in either instance.
#
# This complete copyright notice must be included in any revised version of the
# source code. Additional authorship citations may be added, but existing
# author citations must be preserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  2111-1307 USA
#
#


from EMAN2 import *
from math import *
from os import system,remove
import sys

def main():
	progname = os.path.basename(sys.argv[0])
	usage = """prog [options] 
	WARNING: THIS PROGRAM IS NOT YET COMPLETE

	"""
	parser = EMArgumentParser(usage=usage,version=EMANVERSION)

	# we grab all relevant options from e2refine.py for consistency
	# and snag a bunch of related code from David
	
	#options associated with e2refine2d.py
	parser.add_argument("--input", default="start.hdf",type=str, help="The name of the file containing the particle data")
	parser.add_argument("--iter", type = int, default=0, help = "The total number of refinement iterations to perform")
	parser.add_argument("--nmodels", type = int, default=0, help = "The number of models to simultaneously reconstruct")	
	parser.add_argument("--check", "-c",default=False, action="store_true",help="Checks the contents of the current directory to verify th command will work - checks for the existence of the necessary starting files and checks their dimensions. Performs no work ")
	parser.add_argument("--verbose", "-v", dest="verbose", action="store", metavar="n", type=int, default=0, help="verbose level [0-9], higner number means higher level of verboseness")
	parser.add_argument("--iterclassav", default=2, type=int, help="Number of iterations when making class-averages")
	
	# options associated with e2project3d.py
	parser.add_argument("--prop", dest = "prop", type = float, help = "The proportional angular separation of projections in degrees")
	parser.add_argument("--sym", dest = "sym", help = "Specify symmetry - choices are: c<n>, d<n>, h<n>, tet, oct, icos")
	parser.add_argument("--projector", dest = "projector", default = "standard",help = "Projector to use")
	parser.add_argument("--numproj", dest = "numproj", type = float,help = "The number of projections to generate - this is opposed to using the prop argument")
	
	# options associated with e2simmx.py
	parser.add_argument("--simcmp",type=str,help="The name of a 'cmp' to be used in comparing the aligned images", default="dot:normalize=1")
	
	## options associated with e2classaverage.py
	#parser.add_argument("--classkeep",type=float,help="The fraction of particles to keep in each class, based on the similarity score generated by the --cmp argument.")
	#parser.add_argument("--classkeepsig", type=float,default=1.0, help="Change the keep (\'--keep\') criterion from fraction-based to sigma-based.")
	#parser.add_argument("--classiter", type=int, help="The number of iterations to perform. Default is 1.", default=3)
	#parser.add_argument("--classalign",type=str,help="If doing more than one iteration, this is the name and parameters of the 'aligner' used to align particles to the previous class average.", default="rotate_translate")
	#parser.add_argument("--classaligncmp",type=str,help="This is the name and parameters of the comparitor used by the fist stage aligner  Default is dot.",default="phase")
	#parser.add_argument("--classralign",type=str,help="The second stage aligner which refines the results of the first alignment in class averaging. Default is None.", default=None)
	#parser.add_argument("--classraligncmp",type=str,help="The comparitor used by the second stage aligner in class averageing. Default is dot:normalize=1.",default="dot:normalize=1")
	#parser.add_argument("--classaverager",type=str,help="The averager used to generate the class averages. Default is \'image\'.",default="image")
	#parser.add_argument("--classcmp",type=str,help="The name and parameters of the comparitor used to generate similarity scores, when class averaging. Default is \'dot:normalize=1\'", default="dot:normalize=1")
	parser.add_argument("--ppid", type=int, help="Set the PID of the parent process, used for cross platform PPID",default=-1)
	
	print "WARNING: This is just a stub for a planned program. It does not yet exist."
		
	global options
	(options, args) = parser.parse_args()
	subverbose=options.verbose-1
	if subverbose<0: subverbose=0
	
	#error = False
	#if check(options,True) == True : 
		#error = True
	#if check_projection_args(options) == True : 
		#error = True
	#if check_simmx_args(options,True) == True :
		#error = True
	#if check_classify_args(options,True) == True :
		#error = True
	#options.cafile = "e2classes.1.img"
	#if check_classaverage_args(options,True) == True :
		#error = True
	#if check_make3d_args(options,True) == True:
		#error = True
	
#	if error:
#		print "Error encountered while, bailing"
#		exit(1)
