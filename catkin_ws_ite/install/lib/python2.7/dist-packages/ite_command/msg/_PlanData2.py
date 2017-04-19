# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ite_command/PlanData2.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class PlanData2(genpy.Message):
  _md5sum = "10929a349c15b7d172c404c6c7b2ff74"
  _type = "ite_command/PlanData2"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """std_msgs/Header header # Contains plan number and planning start time
string planner_type
float64 duration       # How long to plan (sec)

bool scarab            # True if planning for scarab
bool quad              # True if planning for quad

bool scarab_action     # True if generated action for scarab
bool quad_action       # True if generated action for quad

geometry_msgs/PoseArray[] scarab_trajs
geometry_msgs/PoseArray[] quad_trajs

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/PoseArray
# An array of poses with a header for global reference.

Header header

Pose[] poses

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['header','planner_type','duration','scarab','quad','scarab_action','quad_action','scarab_trajs','quad_trajs']
  _slot_types = ['std_msgs/Header','string','float64','bool','bool','bool','bool','geometry_msgs/PoseArray[]','geometry_msgs/PoseArray[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,planner_type,duration,scarab,quad,scarab_action,quad_action,scarab_trajs,quad_trajs

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PlanData2, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.planner_type is None:
        self.planner_type = ''
      if self.duration is None:
        self.duration = 0.
      if self.scarab is None:
        self.scarab = False
      if self.quad is None:
        self.quad = False
      if self.scarab_action is None:
        self.scarab_action = False
      if self.quad_action is None:
        self.quad_action = False
      if self.scarab_trajs is None:
        self.scarab_trajs = []
      if self.quad_trajs is None:
        self.quad_trajs = []
    else:
      self.header = std_msgs.msg.Header()
      self.planner_type = ''
      self.duration = 0.
      self.scarab = False
      self.quad = False
      self.scarab_action = False
      self.quad_action = False
      self.scarab_trajs = []
      self.quad_trajs = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.planner_type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_d4B.pack(_x.duration, _x.scarab, _x.quad, _x.scarab_action, _x.quad_action))
      length = len(self.scarab_trajs)
      buff.write(_struct_I.pack(length))
      for val1 in self.scarab_trajs:
        _v1 = val1.header
        buff.write(_struct_I.pack(_v1.seq))
        _v2 = _v1.stamp
        _x = _v2
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v1.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.poses)
        buff.write(_struct_I.pack(length))
        for val2 in val1.poses:
          _v3 = val2.position
          _x = _v3
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v4 = val2.orientation
          _x = _v4
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.quad_trajs)
      buff.write(_struct_I.pack(length))
      for val1 in self.quad_trajs:
        _v5 = val1.header
        buff.write(_struct_I.pack(_v5.seq))
        _v6 = _v5.stamp
        _x = _v6
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v5.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.poses)
        buff.write(_struct_I.pack(length))
        for val2 in val1.poses:
          _v7 = val2.position
          _x = _v7
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v8 = val2.orientation
          _x = _v8
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.scarab_trajs is None:
        self.scarab_trajs = None
      if self.quad_trajs is None:
        self.quad_trajs = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.planner_type = str[start:end].decode('utf-8')
      else:
        self.planner_type = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.duration, _x.scarab, _x.quad, _x.scarab_action, _x.quad_action,) = _struct_d4B.unpack(str[start:end])
      self.scarab = bool(self.scarab)
      self.quad = bool(self.quad)
      self.scarab_action = bool(self.scarab_action)
      self.quad_action = bool(self.quad_action)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.scarab_trajs = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.PoseArray()
        _v9 = val1.header
        start = end
        end += 4
        (_v9.seq,) = _struct_I.unpack(str[start:end])
        _v10 = _v9.stamp
        _x = _v10
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v9.frame_id = str[start:end].decode('utf-8')
        else:
          _v9.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.poses = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Pose()
          _v11 = val2.position
          _x = _v11
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v12 = val2.orientation
          _x = _v12
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          val1.poses.append(val2)
        self.scarab_trajs.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.quad_trajs = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.PoseArray()
        _v13 = val1.header
        start = end
        end += 4
        (_v13.seq,) = _struct_I.unpack(str[start:end])
        _v14 = _v13.stamp
        _x = _v14
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v13.frame_id = str[start:end].decode('utf-8')
        else:
          _v13.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.poses = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Pose()
          _v15 = val2.position
          _x = _v15
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v16 = val2.orientation
          _x = _v16
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          val1.poses.append(val2)
        self.quad_trajs.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.planner_type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_d4B.pack(_x.duration, _x.scarab, _x.quad, _x.scarab_action, _x.quad_action))
      length = len(self.scarab_trajs)
      buff.write(_struct_I.pack(length))
      for val1 in self.scarab_trajs:
        _v17 = val1.header
        buff.write(_struct_I.pack(_v17.seq))
        _v18 = _v17.stamp
        _x = _v18
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v17.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.poses)
        buff.write(_struct_I.pack(length))
        for val2 in val1.poses:
          _v19 = val2.position
          _x = _v19
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v20 = val2.orientation
          _x = _v20
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.quad_trajs)
      buff.write(_struct_I.pack(length))
      for val1 in self.quad_trajs:
        _v21 = val1.header
        buff.write(_struct_I.pack(_v21.seq))
        _v22 = _v21.stamp
        _x = _v22
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v21.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.poses)
        buff.write(_struct_I.pack(length))
        for val2 in val1.poses:
          _v23 = val2.position
          _x = _v23
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v24 = val2.orientation
          _x = _v24
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.scarab_trajs is None:
        self.scarab_trajs = None
      if self.quad_trajs is None:
        self.quad_trajs = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.planner_type = str[start:end].decode('utf-8')
      else:
        self.planner_type = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.duration, _x.scarab, _x.quad, _x.scarab_action, _x.quad_action,) = _struct_d4B.unpack(str[start:end])
      self.scarab = bool(self.scarab)
      self.quad = bool(self.quad)
      self.scarab_action = bool(self.scarab_action)
      self.quad_action = bool(self.quad_action)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.scarab_trajs = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.PoseArray()
        _v25 = val1.header
        start = end
        end += 4
        (_v25.seq,) = _struct_I.unpack(str[start:end])
        _v26 = _v25.stamp
        _x = _v26
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v25.frame_id = str[start:end].decode('utf-8')
        else:
          _v25.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.poses = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Pose()
          _v27 = val2.position
          _x = _v27
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v28 = val2.orientation
          _x = _v28
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          val1.poses.append(val2)
        self.scarab_trajs.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.quad_trajs = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.PoseArray()
        _v29 = val1.header
        start = end
        end += 4
        (_v29.seq,) = _struct_I.unpack(str[start:end])
        _v30 = _v29.stamp
        _x = _v30
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v29.frame_id = str[start:end].decode('utf-8')
        else:
          _v29.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.poses = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Pose()
          _v31 = val2.position
          _x = _v31
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v32 = val2.orientation
          _x = _v32
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          val1.poses.append(val2)
        self.quad_trajs.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_d4B = struct.Struct("<d4B")
_struct_3I = struct.Struct("<3I")
_struct_4d = struct.Struct("<4d")
_struct_2I = struct.Struct("<2I")
_struct_3d = struct.Struct("<3d")