
// Boost Includes ==============================================================
#include <boost/python.hpp>
#include <boost/cstdint.hpp>

// Includes ====================================================================
#include <matrix.h>
#include <quaternion.h>
#include <rotation.h>
#include <transform.h>
#include <vec3.h>

// Using =======================================================================
using namespace boost::python;

// Module ======================================================================
BOOST_PYTHON_MODULE(libpyTransform2)
{
    class_< EMAN::Vec3<float> >("Vec3f", init<  >())
        .def(init< const EMAN::Vec3<float>& >())
        .def("normalize", &EMAN::Vec3<float>::normalize)
        .def("length", &EMAN::Vec3<float>::length)
        .def("negate", &EMAN::Vec3<float>::negate, return_internal_reference< 1 >())
        .def("get_as_list", &EMAN::Vec3<float>::get_as_list)
    ;

    class_< EMAN::Vec3<int> >("Vec3i", init<  >())
        .def(init< const EMAN::Vec3<int>& >())
        .def("normalize", &EMAN::Vec3<int>::normalize)
        .def("length", &EMAN::Vec3<int>::length)
        .def("negate", &EMAN::Vec3<int>::negate, return_internal_reference< 1 >())
        .def("get_as_list", &EMAN::Vec3<int>::get_as_list)
    ;

    class_< EMAN::Matrix3f >("Matrix3f", init<  >())
        .def(init< float, float, float, float, float, float, float, float, float >())
        .def(init< const std::vector<float,std::allocator<float> >& >())
        .def(init< const EMAN::Matrix3f& >())
        .def("make_identity", &EMAN::Matrix3f::make_identity)
        .def("mult_right", &EMAN::Matrix3f::mult_right, return_internal_reference< 1 >())
        .def("mult_left", &EMAN::Matrix3f::mult_left, return_internal_reference< 1 >())
        .def("set_value", &EMAN::Matrix3f::set_value)
        .def("get_as_list", &EMAN::Matrix3f::get_as_list)
        .def("inverse", &EMAN::Matrix3f::inverse, return_internal_reference< 1 >())
        .def("transpose", &EMAN::Matrix3f::transpose, return_internal_reference< 1 >())
        .def("create_inverse", &EMAN::Matrix3f::create_inverse)
        .def("get_row", &EMAN::Matrix3f::get_row)
        .def("get_col", &EMAN::Matrix3f::get_col)
        .def( self == self )
        .def( self / self )
        .def( self - self )
        .def( self * self )
        .def( self / other< float >() )
        .def( self + self )
        .def( self - other< float >() )
        .def( self * other< float >() )
        .def( other< float >() / self )
        .def( self + other< float >() )
        .def( other< float >() - self )
        .def( other< float >() * self )
        .def( other< float >() + self )
        .def( self != self )
        .def( self += other< float >() )
        .def( self -= other< float >() )
        .def( self *= other< float >() )
        .def( self /= other< float >() )
        .def( self += self )
        .def( self -= self )
        .def( self *= self )
        .def( self /= self )
    ;

    class_< EMAN::Matrix4f >("Matrix4f", init<  >())
        .def(init< const std::vector<float,std::allocator<float> >& >())
        .def(init< const EMAN::Matrix3f& >())
        .def(init< const EMAN::Matrix4f& >())
        .def("mult_right", &EMAN::Matrix4f::mult_right, return_internal_reference< 1 >())
        .def("mult_left", &EMAN::Matrix4f::mult_left, return_internal_reference< 1 >())
        .def("make_identity", &EMAN::Matrix4f::make_identity)
        .def("set_value", &EMAN::Matrix4f::set_value)
        .def("get_as_list", &EMAN::Matrix4f::get_as_list)
        .def("get_matrix3", &EMAN::Matrix4f::get_matrix3)
        .def("inverse", &EMAN::Matrix4f::inverse, return_internal_reference< 1 >())
        .def("transpose", &EMAN::Matrix4f::transpose, return_internal_reference< 1 >())
        .def("create_inverse", &EMAN::Matrix4f::create_inverse)
        .def( self * other< float >() )
        .def( self / other< float >() )
        .def( self == self )
        .def( self != self )
        .def( self + self )
        .def( self - self )
        .def( self * self )
        .def( self / self )
        .def( other< float >() + self )
        .def( self - other< float >() )
        .def( self + other< float >() )
        .def( other< float >() / self )
        .def( other< float >() * self )
        .def( other< float >() - self )
        .def( self += other< float >() )
        .def( self -= other< float >() )
        .def( self *= other< float >() )
        .def( self /= other< float >() )
        .def( self += self )
        .def( self -= self )
        .def( self *= self )
        .def( self /= self )
    ;

    class_< EMAN::Quaternion >("Quaternion", init<  >())
        .def(init< const EMAN::Quaternion& >())
        .def(init< float, float, float, float >())
        .def(init< float, const EMAN::Vec3<float>& >())
        .def(init< const EMAN::Vec3<float>&, float >())
        .def(init< const EMAN::Matrix3f& >())
        .def(init< const EMAN::Matrix4f& >())
        .def("norm", &EMAN::Quaternion::norm)
        .def("conj", &EMAN::Quaternion::conj)
        .def("abs", &EMAN::Quaternion::abs)
        .def("normalize", &EMAN::Quaternion::normalize)
        .def("inverse", &EMAN::Quaternion::inverse, return_internal_reference< 1 >())
        .def("create_inverse", &EMAN::Quaternion::create_inverse)
        .def("rotate", &EMAN::Quaternion::rotate)
        .def("to_angle", &EMAN::Quaternion::to_angle)
        .def("to_axis", &EMAN::Quaternion::to_axis)
        .def("to_matrix3", &EMAN::Quaternion::to_matrix3)
        .def("to_matrix4", &EMAN::Quaternion::to_matrix4)
        .def("real", &EMAN::Quaternion::real)
        .def("unreal", &EMAN::Quaternion::unreal)
        .def("get_as_list", &EMAN::Quaternion::get_as_list)
        .def("interpolate", &EMAN::Quaternion::interpolate)
        .staticmethod("interpolate")
        .def( self - self )
        .def( self * self )
        .def( self * other< float >() )
        .def( other< float >() * self )
        .def( self + self )
        .def( self != self )
        .def( self == self )
        .def( self / self )
        .def( self += self )
        .def( self -= self )
        .def( self *= self )
        .def( self *= other< float >() )
        .def( self /= self )
        .def( self /= other< float >() )
    ;

    scope* EMAN_Rotation_scope = new scope(
    class_< EMAN::Rotation >("Rotation", init<  >())
        .def(init< const EMAN::Rotation& >())
        .def(init< float, float, float, EMAN::Rotation::EulerType >())
        .def(init< float, float, float, float, EMAN::Rotation::EulerType >())
        .def(init< const EMAN::Quaternion& >())
        .def(init< const EMAN::Matrix3f& >())
        .def_readonly("ERR_LIMIT", &EMAN::Rotation::ERR_LIMIT)
        .def("inverse", &EMAN::Rotation::inverse, return_internal_reference< 1 >())
        .def("create_inverse", &EMAN::Rotation::create_inverse)
        .def("diff", &EMAN::Rotation::diff)
        .def("rotate_from_left", &EMAN::Rotation::rotate_from_left, return_internal_reference< 1 >())
        .def("set_sym", &EMAN::Rotation::set_sym)
        .def("get_max_nsym", &EMAN::Rotation::get_max_nsym)
        .def("get_sym", &EMAN::Rotation::get_sym)
        .def("set_angle", (void (EMAN::Rotation::*)(float, float, float, EMAN::Rotation::EulerType) )&EMAN::Rotation::set_angle)
        .def("set_angle", (void (EMAN::Rotation::*)(float, float, float, float, EMAN::Rotation::EulerType) )&EMAN::Rotation::set_angle)
        .def("set_angle", (void (EMAN::Rotation::*)(const EMAN::Matrix3f&) )&EMAN::Rotation::set_angle)
        .def("set_angle", (void (EMAN::Rotation::*)(const EMAN::Quaternion&) )&EMAN::Rotation::set_angle)
        .def("is_valid", &EMAN::Rotation::is_valid)
        .def("rectify", &EMAN::Rotation::rectify)
        .def("eman_alt", &EMAN::Rotation::eman_alt)
        .def("eman_az", &EMAN::Rotation::eman_az)
        .def("eman_phi", &EMAN::Rotation::eman_phi)
        .def("mrc_theta", &EMAN::Rotation::mrc_theta)
        .def("mrc_phi", &EMAN::Rotation::mrc_phi)
        .def("mrc_omega", &EMAN::Rotation::mrc_omega)
        .def("imagic_alpha", &EMAN::Rotation::imagic_alpha)
        .def("imagic_beta", &EMAN::Rotation::imagic_beta)
        .def("imagic_gamma", &EMAN::Rotation::imagic_gamma)
        .def("spider_phi", &EMAN::Rotation::spider_phi)
        .def("spider_theta", &EMAN::Rotation::spider_theta)
        .def("spider_gamma", &EMAN::Rotation::spider_gamma)
        .def("get_spin_axis", (std::vector<float,std::allocator<float> > (EMAN::Rotation::*)() const)&EMAN::Rotation::get_spin_axis)
        .def("get_spin_axis", (void (EMAN::Rotation::*)(float*, float*, float*, float*) const)&EMAN::Rotation::get_spin_axis)
        .def("get_sgi", (std::vector<float,std::allocator<float> > (EMAN::Rotation::*)() const)&EMAN::Rotation::get_sgi)
        .def("get_sgi", (void (EMAN::Rotation::*)(float*, float*, float*, float*) const)&EMAN::Rotation::get_sgi)
        .def("get_quaternion", &EMAN::Rotation::get_quaternion)
        .def("get_matrix3", &EMAN::Rotation::get_matrix3)
        .def("get_matrix4", &EMAN::Rotation::get_matrix4)
        .def("interpolate", &EMAN::Rotation::interpolate)
        .staticmethod("interpolate")
        .def( self / self )
        .def( self == self )
        .def( self != self )
        .def( self * self )
        .def( self *= self )
        .def( self /= self )
    );

    enum_< EMAN::Rotation::EulerType >("EulerType")
        .value("MATRIX", EMAN::Rotation::MATRIX)
        .value("UNKNOWN", EMAN::Rotation::UNKNOWN)
        .value("IMAGIC", EMAN::Rotation::IMAGIC)
        .value("SPIDER", EMAN::Rotation::SPIDER)
        .value("QUATERNION", EMAN::Rotation::QUATERNION)
        .value("SGIROT", EMAN::Rotation::SGIROT)
        .value("MRC", EMAN::Rotation::MRC)
        .value("SPIN", EMAN::Rotation::SPIN)
        .value("EMAN", EMAN::Rotation::EMAN)
    ;

    delete EMAN_Rotation_scope;

    scope* EMAN_Transform_scope = new scope(
    class_< EMAN::Transform >("Transform", init<  >())
        .def(init< const EMAN::Transform& >())
        .def(init< const EMAN::Matrix4f& >())
        .def(init< const EMAN::Vec3<float>& >())
        .def(init< const EMAN::Rotation& >())
        .def(init< const EMAN::Rotation&, const EMAN::Vec3<float>& >())
        .def("set_rotate_instance", (EMAN::Transform& (EMAN::Transform::*)(const EMAN::Rotation&) )&EMAN::Transform::set_rotate_instance, return_internal_reference< 1 >())
        .def("set_rotate_instance", (EMAN::Transform& (EMAN::Transform::*)(const EMAN::Matrix3f&) )&EMAN::Transform::set_rotate_instance, return_internal_reference< 1 >())
        .def("set_translate_instance", &EMAN::Transform::set_translate_instance, return_internal_reference< 1 >())
        .def("set_scale_instance", &EMAN::Transform::set_scale_instance, return_internal_reference< 1 >())
        .def("set_transform_instance", (EMAN::Transform& (EMAN::Transform::*)(const EMAN::Vec3<float>&, const EMAN::Rotation&, const EMAN::Vec3<float>&, const EMAN::Rotation&, const EMAN::Vec3<float>&) )&EMAN::Transform::set_transform_instance, return_internal_reference< 1 >())
        .def("set_transform_instance", (EMAN::Transform& (EMAN::Transform::*)(const EMAN::Vec3<float>&, const EMAN::Rotation&, const EMAN::Vec3<float>&) )&EMAN::Transform::set_transform_instance, return_internal_reference< 1 >())
        .def("set_center", &EMAN::Transform::set_center, return_internal_reference< 1 >())
        .def("set_matrix", &EMAN::Transform::set_matrix, return_internal_reference< 1 >())
        .def("set_post_translate", &EMAN::Transform::set_post_translate, return_internal_reference< 1 >())
        .def("inverse", &EMAN::Transform::inverse, return_internal_reference< 1 >())
        .def("create_inverse", &EMAN::Transform::create_inverse)
        .def("transpose", &EMAN::Transform::transpose, return_internal_reference< 1 >())
        .def("post_concatenate", &EMAN::Transform::post_concatenate, return_internal_reference< 1 >())
        .def("pre_concatenate", &EMAN::Transform::pre_concatenate, return_internal_reference< 1 >())
        .def("translate", &EMAN::Transform::translate, return_internal_reference< 1 >())
        .def("rotate", &EMAN::Transform::rotate, return_internal_reference< 1 >())
        .def("rotate_center", &EMAN::Transform::rotate_center, return_internal_reference< 1 >())
        .def("rotate_scale", &EMAN::Transform::rotate_scale, return_internal_reference< 1 >())
        .def("pre_translate_rotate", &EMAN::Transform::pre_translate_rotate, return_internal_reference< 1 >())
        .def("post_translate_rotate", &EMAN::Transform::post_translate_rotate, return_internal_reference< 1 >())
        .def("scale", &EMAN::Transform::scale, return_internal_reference< 1 >())
        .def("transform", &EMAN::Transform::transform)
        .def("inverse_transform", &EMAN::Transform::inverse_transform)
        .def("get_rotation", &EMAN::Transform::get_rotation)
        .def("get_scale", (float (EMAN::Transform::*)(int) const)&EMAN::Transform::get_scale)
        .def("get_scale", (EMAN::Vec3<float> (EMAN::Transform::*)() const)&EMAN::Transform::get_scale)
        .def("get_center", &EMAN::Transform::get_center)
        .def("get_matrix", &EMAN::Transform::get_matrix)
        .def("get_pre_translate", &EMAN::Transform::get_pre_translate)
        .def("get_post_translate", &EMAN::Transform::get_post_translate)
        .def("get_type", &EMAN::Transform::get_type)
        .def( other< float >() / self )
        .def( other< float >() * self )
        .def( self / other< float >() )
        .def( self - self )
        .def( self * other< float >() )
        .def( self / self )
        .def( self + self )
        .def( self * self )
        .def( self += self )
        .def( self -= self )
        .def( self *= self )
        .def( self *= other< float >() )
        .def( self /= self )
        .def( self /= other< float >() )
    );

    enum_< EMAN::Transform::TransformType >("TransformType")
        .value("SCALE", EMAN::Transform::SCALE)
        .value("UNIFORM_SCALE", EMAN::Transform::UNIFORM_SCALE)
        .value("TRANSFORM", EMAN::Transform::TRANSFORM)
        .value("ROTATION", EMAN::Transform::ROTATION)
        .value("TRANSLATION", EMAN::Transform::TRANSLATION)
        .value("IDENTITY", EMAN::Transform::IDENTITY)
    ;

    delete EMAN_Transform_scope;

}

