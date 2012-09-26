#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lintao

class HelperReadOnly(object):
  def __init__(self, val):
    self.val = val

  def __get__(self, obj, objtype):
    return self.val

  def __set__(self, obj, val):
    raise AttributeError("can't modify attribute")

class AbsFileSystem(object):
  fs_name = HelperReadOnly("AbsFileSystem")
  seq = HelperReadOnly("/")

  def list_dir(self, path):
    raise NotImplementedError

  def is_dir(self, path):
    raise NotImplementedError


import os
import os.path
class UnixLikeFileSystem(AbsFileSystem):
  fs_name = HelperReadOnly("UnixLikeFileSystem")
  seq = HelperReadOnly("/")

  def list_dir(self, path):
    for entry in os.listdir(path):
      if self.is_dir( os.path.join(path, entry) ):
        entry += self.seq
      yield entry
  def is_dir(self, path):
    return os.path.isdir(path)
  pass

if __name__ == "__main__":
  ulfs = UnixLikeFileSystem()
  print "FS", ulfs.fs_name
  print "SEQ", ulfs.seq

  print list(ulfs.list_dir("/"))
