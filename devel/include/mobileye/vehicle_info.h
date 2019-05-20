// Generated by gencpp from file mobileye/vehicle_info.msg
// DO NOT EDIT!


#ifndef MOBILEYE_MESSAGE_VEHICLE_INFO_H
#define MOBILEYE_MESSAGE_VEHICLE_INFO_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace mobileye
{
template <class ContainerAllocator>
struct vehicle_info_
{
  typedef vehicle_info_<ContainerAllocator> Type;

  vehicle_info_()
    : Speed(0.0)
    , YawAngle(0.0)
    , PitchAngle(0.0)  {
    }
  vehicle_info_(const ContainerAllocator& _alloc)
    : Speed(0.0)
    , YawAngle(0.0)
    , PitchAngle(0.0)  {
  (void)_alloc;
    }



   typedef float _Speed_type;
  _Speed_type Speed;

   typedef float _YawAngle_type;
  _YawAngle_type YawAngle;

   typedef float _PitchAngle_type;
  _PitchAngle_type PitchAngle;




  typedef boost::shared_ptr< ::mobileye::vehicle_info_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mobileye::vehicle_info_<ContainerAllocator> const> ConstPtr;

}; // struct vehicle_info_

typedef ::mobileye::vehicle_info_<std::allocator<void> > vehicle_info;

typedef boost::shared_ptr< ::mobileye::vehicle_info > vehicle_infoPtr;
typedef boost::shared_ptr< ::mobileye::vehicle_info const> vehicle_infoConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mobileye::vehicle_info_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mobileye::vehicle_info_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace mobileye

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'mobileye': ['/home/silentroar/Desktop/ROS_Intell_Driving/src/mobileye/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::mobileye::vehicle_info_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mobileye::vehicle_info_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mobileye::vehicle_info_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mobileye::vehicle_info_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mobileye::vehicle_info_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mobileye::vehicle_info_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mobileye::vehicle_info_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4ce4cbfa04d5e948da15a941ff921a8a";
  }

  static const char* value(const ::mobileye::vehicle_info_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4ce4cbfa04d5e948ULL;
  static const uint64_t static_value2 = 0xda15a941ff921a8aULL;
};

template<class ContainerAllocator>
struct DataType< ::mobileye::vehicle_info_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mobileye/vehicle_info";
  }

  static const char* value(const ::mobileye::vehicle_info_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mobileye::vehicle_info_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 Speed\n\
float32 YawAngle\n\
float32 PitchAngle\n\
";
  }

  static const char* value(const ::mobileye::vehicle_info_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mobileye::vehicle_info_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.Speed);
      stream.next(m.YawAngle);
      stream.next(m.PitchAngle);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct vehicle_info_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mobileye::vehicle_info_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mobileye::vehicle_info_<ContainerAllocator>& v)
  {
    s << indent << "Speed: ";
    Printer<float>::stream(s, indent + "  ", v.Speed);
    s << indent << "YawAngle: ";
    Printer<float>::stream(s, indent + "  ", v.YawAngle);
    s << indent << "PitchAngle: ";
    Printer<float>::stream(s, indent + "  ", v.PitchAngle);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOBILEYE_MESSAGE_VEHICLE_INFO_H