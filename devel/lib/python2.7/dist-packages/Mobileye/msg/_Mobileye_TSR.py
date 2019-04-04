# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from Mobileye/Mobileye_TSR.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Mobileye_TSR(genpy.Message):
  _md5sum = "c6519f710ac25fe67cd32cf09bf9fb46"
  _type = "Mobileye/Mobileye_TSR"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint8 MType
uint8 SupType
float32 PosX
float32 PosY
float32 PosZ
uint8 FilterType
"""
  __slots__ = ['MType','SupType','PosX','PosY','PosZ','FilterType']
  _slot_types = ['uint8','uint8','float32','float32','float32','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       MType,SupType,PosX,PosY,PosZ,FilterType

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Mobileye_TSR, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.MType is None:
        self.MType = 0
      if self.SupType is None:
        self.SupType = 0
      if self.PosX is None:
        self.PosX = 0.
      if self.PosY is None:
        self.PosY = 0.
      if self.PosZ is None:
        self.PosZ = 0.
      if self.FilterType is None:
        self.FilterType = 0
    else:
      self.MType = 0
      self.SupType = 0
      self.PosX = 0.
      self.PosY = 0.
      self.PosZ = 0.
      self.FilterType = 0

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
      buff.write(_struct_2B3fB.pack(_x.MType, _x.SupType, _x.PosX, _x.PosY, _x.PosZ, _x.FilterType))
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
      end += 15
      (_x.MType, _x.SupType, _x.PosX, _x.PosY, _x.PosZ, _x.FilterType,) = _struct_2B3fB.unpack(str[start:end])
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
      buff.write(_struct_2B3fB.pack(_x.MType, _x.SupType, _x.PosX, _x.PosY, _x.PosZ, _x.FilterType))
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
      end += 15
      (_x.MType, _x.SupType, _x.PosX, _x.PosY, _x.PosZ, _x.FilterType,) = _struct_2B3fB.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2B3fB = struct.Struct("<2B3fB")
