# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from mobileye/mobileye_Obstacle.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class mobileye_Obstacle(genpy.Message):
  _md5sum = "daa4d2ee849152973a6c14f07fc64bd5"
  _type = "mobileye/mobileye_Obstacle"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint8 ID
float32 PosX
float32 PosY
uint8 Blinker
uint8 CutState
float32 VrelX
uint8 MType
uint8 Status
uint8 Brake
uint8 Valid
float32 Length
float32 Width
uint8 Age
uint8 ObsLane
uint8 CIPV
float32 AngleRate
float32 ScaleChange
float32 AccelX
float32 Angle
uint8 Replaced
"""
  __slots__ = ['ID','PosX','PosY','Blinker','CutState','VrelX','MType','Status','Brake','Valid','Length','Width','Age','ObsLane','CIPV','AngleRate','ScaleChange','AccelX','Angle','Replaced']
  _slot_types = ['uint8','float32','float32','uint8','uint8','float32','uint8','uint8','uint8','uint8','float32','float32','uint8','uint8','uint8','float32','float32','float32','float32','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ID,PosX,PosY,Blinker,CutState,VrelX,MType,Status,Brake,Valid,Length,Width,Age,ObsLane,CIPV,AngleRate,ScaleChange,AccelX,Angle,Replaced

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(mobileye_Obstacle, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.ID is None:
        self.ID = 0
      if self.PosX is None:
        self.PosX = 0.
      if self.PosY is None:
        self.PosY = 0.
      if self.Blinker is None:
        self.Blinker = 0
      if self.CutState is None:
        self.CutState = 0
      if self.VrelX is None:
        self.VrelX = 0.
      if self.MType is None:
        self.MType = 0
      if self.Status is None:
        self.Status = 0
      if self.Brake is None:
        self.Brake = 0
      if self.Valid is None:
        self.Valid = 0
      if self.Length is None:
        self.Length = 0.
      if self.Width is None:
        self.Width = 0.
      if self.Age is None:
        self.Age = 0
      if self.ObsLane is None:
        self.ObsLane = 0
      if self.CIPV is None:
        self.CIPV = 0
      if self.AngleRate is None:
        self.AngleRate = 0.
      if self.ScaleChange is None:
        self.ScaleChange = 0.
      if self.AccelX is None:
        self.AccelX = 0.
      if self.Angle is None:
        self.Angle = 0.
      if self.Replaced is None:
        self.Replaced = 0
    else:
      self.ID = 0
      self.PosX = 0.
      self.PosY = 0.
      self.Blinker = 0
      self.CutState = 0
      self.VrelX = 0.
      self.MType = 0
      self.Status = 0
      self.Brake = 0
      self.Valid = 0
      self.Length = 0.
      self.Width = 0.
      self.Age = 0
      self.ObsLane = 0
      self.CIPV = 0
      self.AngleRate = 0.
      self.ScaleChange = 0.
      self.AccelX = 0.
      self.Angle = 0.
      self.Replaced = 0

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
      buff.write(_struct_B2f2Bf4B2f3B4fB.pack(_x.ID, _x.PosX, _x.PosY, _x.Blinker, _x.CutState, _x.VrelX, _x.MType, _x.Status, _x.Brake, _x.Valid, _x.Length, _x.Width, _x.Age, _x.ObsLane, _x.CIPV, _x.AngleRate, _x.ScaleChange, _x.AccelX, _x.Angle, _x.Replaced))
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
      end += 47
      (_x.ID, _x.PosX, _x.PosY, _x.Blinker, _x.CutState, _x.VrelX, _x.MType, _x.Status, _x.Brake, _x.Valid, _x.Length, _x.Width, _x.Age, _x.ObsLane, _x.CIPV, _x.AngleRate, _x.ScaleChange, _x.AccelX, _x.Angle, _x.Replaced,) = _struct_B2f2Bf4B2f3B4fB.unpack(str[start:end])
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
      buff.write(_struct_B2f2Bf4B2f3B4fB.pack(_x.ID, _x.PosX, _x.PosY, _x.Blinker, _x.CutState, _x.VrelX, _x.MType, _x.Status, _x.Brake, _x.Valid, _x.Length, _x.Width, _x.Age, _x.ObsLane, _x.CIPV, _x.AngleRate, _x.ScaleChange, _x.AccelX, _x.Angle, _x.Replaced))
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
      end += 47
      (_x.ID, _x.PosX, _x.PosY, _x.Blinker, _x.CutState, _x.VrelX, _x.MType, _x.Status, _x.Brake, _x.Valid, _x.Length, _x.Width, _x.Age, _x.ObsLane, _x.CIPV, _x.AngleRate, _x.ScaleChange, _x.AccelX, _x.Angle, _x.Replaced,) = _struct_B2f2Bf4B2f3B4fB.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B2f2Bf4B2f3B4fB = struct.Struct("<B2f2Bf4B2f3B4fB")
