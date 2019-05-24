# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from kalman/radar_mobileye_data.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class radar_mobileye_data(genpy.Message):
  _md5sum = "338d6de14083d2c26fc3a506ceca7563"
  _type = "kalman/radar_mobileye_data"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint32 timestamp
uint8 ID
float32 radar_DistX
float32 radar_DistY
float32 radar_VrelX
float32 radar_VrelY
float32 radar_ArelX
float32 radar_ArelY
float32 mobileye_DistX
float32 mobileye_DistY
float32 mobileye_VrelX
float32 mobileye_ArelX
float32 fusion_DistX
float32 fusion_DistY
float32 fusion_VrelX
float32 fusion_VrelY
float32 fusion_ArelX
float32 fusion_ArelY
float32 fusion_Length
float32 fusion_Width
float32 mobileye_Width
float32 mobileye_Length
uint8 fusion_flag
"""
  __slots__ = ['timestamp','ID','radar_DistX','radar_DistY','radar_VrelX','radar_VrelY','radar_ArelX','radar_ArelY','mobileye_DistX','mobileye_DistY','mobileye_VrelX','mobileye_ArelX','fusion_DistX','fusion_DistY','fusion_VrelX','fusion_VrelY','fusion_ArelX','fusion_ArelY','fusion_Length','fusion_Width','mobileye_Width','mobileye_Length','fusion_flag']
  _slot_types = ['uint32','uint8','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       timestamp,ID,radar_DistX,radar_DistY,radar_VrelX,radar_VrelY,radar_ArelX,radar_ArelY,mobileye_DistX,mobileye_DistY,mobileye_VrelX,mobileye_ArelX,fusion_DistX,fusion_DistY,fusion_VrelX,fusion_VrelY,fusion_ArelX,fusion_ArelY,fusion_Length,fusion_Width,mobileye_Width,mobileye_Length,fusion_flag

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(radar_mobileye_data, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.timestamp is None:
        self.timestamp = 0
      if self.ID is None:
        self.ID = 0
      if self.radar_DistX is None:
        self.radar_DistX = 0.
      if self.radar_DistY is None:
        self.radar_DistY = 0.
      if self.radar_VrelX is None:
        self.radar_VrelX = 0.
      if self.radar_VrelY is None:
        self.radar_VrelY = 0.
      if self.radar_ArelX is None:
        self.radar_ArelX = 0.
      if self.radar_ArelY is None:
        self.radar_ArelY = 0.
      if self.mobileye_DistX is None:
        self.mobileye_DistX = 0.
      if self.mobileye_DistY is None:
        self.mobileye_DistY = 0.
      if self.mobileye_VrelX is None:
        self.mobileye_VrelX = 0.
      if self.mobileye_ArelX is None:
        self.mobileye_ArelX = 0.
      if self.fusion_DistX is None:
        self.fusion_DistX = 0.
      if self.fusion_DistY is None:
        self.fusion_DistY = 0.
      if self.fusion_VrelX is None:
        self.fusion_VrelX = 0.
      if self.fusion_VrelY is None:
        self.fusion_VrelY = 0.
      if self.fusion_ArelX is None:
        self.fusion_ArelX = 0.
      if self.fusion_ArelY is None:
        self.fusion_ArelY = 0.
      if self.fusion_Length is None:
        self.fusion_Length = 0.
      if self.fusion_Width is None:
        self.fusion_Width = 0.
      if self.mobileye_Width is None:
        self.mobileye_Width = 0.
      if self.mobileye_Length is None:
        self.mobileye_Length = 0.
      if self.fusion_flag is None:
        self.fusion_flag = 0
    else:
      self.timestamp = 0
      self.ID = 0
      self.radar_DistX = 0.
      self.radar_DistY = 0.
      self.radar_VrelX = 0.
      self.radar_VrelY = 0.
      self.radar_ArelX = 0.
      self.radar_ArelY = 0.
      self.mobileye_DistX = 0.
      self.mobileye_DistY = 0.
      self.mobileye_VrelX = 0.
      self.mobileye_ArelX = 0.
      self.fusion_DistX = 0.
      self.fusion_DistY = 0.
      self.fusion_VrelX = 0.
      self.fusion_VrelY = 0.
      self.fusion_ArelX = 0.
      self.fusion_ArelY = 0.
      self.fusion_Length = 0.
      self.fusion_Width = 0.
      self.mobileye_Width = 0.
      self.mobileye_Length = 0.
      self.fusion_flag = 0

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
      buff.write(_struct_IB20fB.pack(_x.timestamp, _x.ID, _x.radar_DistX, _x.radar_DistY, _x.radar_VrelX, _x.radar_VrelY, _x.radar_ArelX, _x.radar_ArelY, _x.mobileye_DistX, _x.mobileye_DistY, _x.mobileye_VrelX, _x.mobileye_ArelX, _x.fusion_DistX, _x.fusion_DistY, _x.fusion_VrelX, _x.fusion_VrelY, _x.fusion_ArelX, _x.fusion_ArelY, _x.fusion_Length, _x.fusion_Width, _x.mobileye_Width, _x.mobileye_Length, _x.fusion_flag))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 86
      (_x.timestamp, _x.ID, _x.radar_DistX, _x.radar_DistY, _x.radar_VrelX, _x.radar_VrelY, _x.radar_ArelX, _x.radar_ArelY, _x.mobileye_DistX, _x.mobileye_DistY, _x.mobileye_VrelX, _x.mobileye_ArelX, _x.fusion_DistX, _x.fusion_DistY, _x.fusion_VrelX, _x.fusion_VrelY, _x.fusion_ArelX, _x.fusion_ArelY, _x.fusion_Length, _x.fusion_Width, _x.mobileye_Width, _x.mobileye_Length, _x.fusion_flag,) = _struct_IB20fB.unpack(str[start:end])
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
      buff.write(_struct_IB20fB.pack(_x.timestamp, _x.ID, _x.radar_DistX, _x.radar_DistY, _x.radar_VrelX, _x.radar_VrelY, _x.radar_ArelX, _x.radar_ArelY, _x.mobileye_DistX, _x.mobileye_DistY, _x.mobileye_VrelX, _x.mobileye_ArelX, _x.fusion_DistX, _x.fusion_DistY, _x.fusion_VrelX, _x.fusion_VrelY, _x.fusion_ArelX, _x.fusion_ArelY, _x.fusion_Length, _x.fusion_Width, _x.mobileye_Width, _x.mobileye_Length, _x.fusion_flag))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 86
      (_x.timestamp, _x.ID, _x.radar_DistX, _x.radar_DistY, _x.radar_VrelX, _x.radar_VrelY, _x.radar_ArelX, _x.radar_ArelY, _x.mobileye_DistX, _x.mobileye_DistY, _x.mobileye_VrelX, _x.mobileye_ArelX, _x.fusion_DistX, _x.fusion_DistY, _x.fusion_VrelX, _x.fusion_VrelY, _x.fusion_ArelX, _x.fusion_ArelY, _x.fusion_Length, _x.fusion_Width, _x.mobileye_Width, _x.mobileye_Length, _x.fusion_flag,) = _struct_IB20fB.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_IB20fB = struct.Struct("<IB20fB")
