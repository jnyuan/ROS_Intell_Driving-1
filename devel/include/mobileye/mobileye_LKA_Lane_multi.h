// Generated by gencpp from file mobileye/mobileye_LKA_Lane_multi.msg
// DO NOT EDIT!


#ifndef MOBILEYE_MESSAGE_MOBILEYE_LKA_LANE_MULTI_H
#define MOBILEYE_MESSAGE_MOBILEYE_LKA_LANE_MULTI_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <mobileye/mobileye_LKA_Lane.h>
#include <mobileye/mobileye_LKA_Lane.h>
#include <mobileye/mobileye_LKA_Lane.h>
#include <mobileye/mobileye_LKA_Lane.h>

namespace mobileye
{
template <class ContainerAllocator>
struct mobileye_LKA_Lane_multi_
{
  typedef mobileye_LKA_Lane_multi_<ContainerAllocator> Type;

  mobileye_LKA_Lane_multi_()
    : Left()
    , Right()
    , Next_Left()
    , Next_Right()  {
    }
  mobileye_LKA_Lane_multi_(const ContainerAllocator& _alloc)
    : Left(_alloc)
    , Right(_alloc)
    , Next_Left(_alloc)
    , Next_Right(_alloc)  {
  (void)_alloc;
    }



   typedef  ::mobileye::mobileye_LKA_Lane_<ContainerAllocator>  _Left_type;
  _Left_type Left;

   typedef  ::mobileye::mobileye_LKA_Lane_<ContainerAllocator>  _Right_type;
  _Right_type Right;

   typedef  ::mobileye::mobileye_LKA_Lane_<ContainerAllocator>  _Next_Left_type;
  _Next_Left_type Next_Left;

   typedef  ::mobileye::mobileye_LKA_Lane_<ContainerAllocator>  _Next_Right_type;
  _Next_Right_type Next_Right;




  typedef boost::shared_ptr< ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator> const> ConstPtr;

}; // struct mobileye_LKA_Lane_multi_

typedef ::mobileye::mobileye_LKA_Lane_multi_<std::allocator<void> > mobileye_LKA_Lane_multi;

typedef boost::shared_ptr< ::mobileye::mobileye_LKA_Lane_multi > mobileye_LKA_Lane_multiPtr;
typedef boost::shared_ptr< ::mobileye::mobileye_LKA_Lane_multi const> mobileye_LKA_Lane_multiConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c48a8b814bcf2e7a5ec962b23742a691";
  }

  static const char* value(const ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc48a8b814bcf2e7aULL;
  static const uint64_t static_value2 = 0x5ec962b23742a691ULL;
};

template<class ContainerAllocator>
struct DataType< ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mobileye/mobileye_LKA_Lane_multi";
  }

  static const char* value(const ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mobileye_LKA_Lane Left\n\
mobileye_LKA_Lane Right\n\
mobileye_LKA_Lane Next_Left\n\
mobileye_LKA_Lane Next_Right\n\
\n\
================================================================================\n\
MSG: mobileye/mobileye_LKA_Lane\n\
uint8 MType\n\
uint8 Quality\n\
uint8 Model_degree\n\
float32 Position\n\
float32 Curvature\n\
float32 Heading\n\
float32 Curvature_deriv\n\
float32 Width\n\
float32 View_range\n\
";
  }

  static const char* value(const ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.Left);
      stream.next(m.Right);
      stream.next(m.Next_Left);
      stream.next(m.Next_Right);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct mobileye_LKA_Lane_multi_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mobileye::mobileye_LKA_Lane_multi_<ContainerAllocator>& v)
  {
    s << indent << "Left: ";
    s << std::endl;
    Printer< ::mobileye::mobileye_LKA_Lane_<ContainerAllocator> >::stream(s, indent + "  ", v.Left);
    s << indent << "Right: ";
    s << std::endl;
    Printer< ::mobileye::mobileye_LKA_Lane_<ContainerAllocator> >::stream(s, indent + "  ", v.Right);
    s << indent << "Next_Left: ";
    s << std::endl;
    Printer< ::mobileye::mobileye_LKA_Lane_<ContainerAllocator> >::stream(s, indent + "  ", v.Next_Left);
    s << indent << "Next_Right: ";
    s << std::endl;
    Printer< ::mobileye::mobileye_LKA_Lane_<ContainerAllocator> >::stream(s, indent + "  ", v.Next_Right);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOBILEYE_MESSAGE_MOBILEYE_LKA_LANE_MULTI_H
