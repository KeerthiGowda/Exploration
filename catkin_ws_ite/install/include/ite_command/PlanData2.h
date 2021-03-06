// Generated by gencpp from file ite_command/PlanData2.msg
// DO NOT EDIT!


#ifndef ITE_COMMAND_MESSAGE_PLANDATA2_H
#define ITE_COMMAND_MESSAGE_PLANDATA2_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <geometry_msgs/PoseArray.h>
#include <geometry_msgs/PoseArray.h>

namespace ite_command
{
template <class ContainerAllocator>
struct PlanData2_
{
  typedef PlanData2_<ContainerAllocator> Type;

  PlanData2_()
    : header()
    , planner_type()
    , duration(0.0)
    , scarab(false)
    , quad(false)
    , scarab_action(false)
    , quad_action(false)
    , scarab_trajs()
    , quad_trajs()  {
    }
  PlanData2_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , planner_type(_alloc)
    , duration(0.0)
    , scarab(false)
    , quad(false)
    , scarab_action(false)
    , quad_action(false)
    , scarab_trajs(_alloc)
    , quad_trajs(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _planner_type_type;
  _planner_type_type planner_type;

   typedef double _duration_type;
  _duration_type duration;

   typedef uint8_t _scarab_type;
  _scarab_type scarab;

   typedef uint8_t _quad_type;
  _quad_type quad;

   typedef uint8_t _scarab_action_type;
  _scarab_action_type scarab_action;

   typedef uint8_t _quad_action_type;
  _quad_action_type quad_action;

   typedef std::vector< ::geometry_msgs::PoseArray_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::geometry_msgs::PoseArray_<ContainerAllocator> >::other >  _scarab_trajs_type;
  _scarab_trajs_type scarab_trajs;

   typedef std::vector< ::geometry_msgs::PoseArray_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::geometry_msgs::PoseArray_<ContainerAllocator> >::other >  _quad_trajs_type;
  _quad_trajs_type quad_trajs;




  typedef boost::shared_ptr< ::ite_command::PlanData2_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ite_command::PlanData2_<ContainerAllocator> const> ConstPtr;

}; // struct PlanData2_

typedef ::ite_command::PlanData2_<std::allocator<void> > PlanData2;

typedef boost::shared_ptr< ::ite_command::PlanData2 > PlanData2Ptr;
typedef boost::shared_ptr< ::ite_command::PlanData2 const> PlanData2ConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ite_command::PlanData2_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ite_command::PlanData2_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ite_command

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'ite_trajopt': ['/home/aravind/catkin_ws_ite/src/ite_core/ite_trajopt/msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'ite_command': ['/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ite_command::PlanData2_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ite_command::PlanData2_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ite_command::PlanData2_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ite_command::PlanData2_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ite_command::PlanData2_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ite_command::PlanData2_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ite_command::PlanData2_<ContainerAllocator> >
{
  static const char* value()
  {
    return "10929a349c15b7d172c404c6c7b2ff74";
  }

  static const char* value(const ::ite_command::PlanData2_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x10929a349c15b7d1ULL;
  static const uint64_t static_value2 = 0x72c404c6c7b2ff74ULL;
};

template<class ContainerAllocator>
struct DataType< ::ite_command::PlanData2_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ite_command/PlanData2";
  }

  static const char* value(const ::ite_command::PlanData2_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ite_command::PlanData2_<ContainerAllocator> >
{
  static const char* value()
  {
    return "std_msgs/Header header # Contains plan number and planning start time\n\
string planner_type\n\
float64 duration       # How long to plan (sec)\n\
\n\
bool scarab            # True if planning for scarab\n\
bool quad              # True if planning for quad\n\
\n\
bool scarab_action     # True if generated action for scarab\n\
bool quad_action       # True if generated action for quad\n\
\n\
geometry_msgs/PoseArray[] scarab_trajs\n\
geometry_msgs/PoseArray[] quad_trajs\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: geometry_msgs/PoseArray\n\
# An array of poses with a header for global reference.\n\
\n\
Header header\n\
\n\
Pose[] poses\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of postion and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
";
  }

  static const char* value(const ::ite_command::PlanData2_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ite_command::PlanData2_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.planner_type);
      stream.next(m.duration);
      stream.next(m.scarab);
      stream.next(m.quad);
      stream.next(m.scarab_action);
      stream.next(m.quad_action);
      stream.next(m.scarab_trajs);
      stream.next(m.quad_trajs);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PlanData2_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ite_command::PlanData2_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ite_command::PlanData2_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "planner_type: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.planner_type);
    s << indent << "duration: ";
    Printer<double>::stream(s, indent + "  ", v.duration);
    s << indent << "scarab: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.scarab);
    s << indent << "quad: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.quad);
    s << indent << "scarab_action: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.scarab_action);
    s << indent << "quad_action: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.quad_action);
    s << indent << "scarab_trajs[]" << std::endl;
    for (size_t i = 0; i < v.scarab_trajs.size(); ++i)
    {
      s << indent << "  scarab_trajs[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::geometry_msgs::PoseArray_<ContainerAllocator> >::stream(s, indent + "    ", v.scarab_trajs[i]);
    }
    s << indent << "quad_trajs[]" << std::endl;
    for (size_t i = 0; i < v.quad_trajs.size(); ++i)
    {
      s << indent << "  quad_trajs[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::geometry_msgs::PoseArray_<ContainerAllocator> >::stream(s, indent + "    ", v.quad_trajs[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // ITE_COMMAND_MESSAGE_PLANDATA2_H
