import os
from nabweb import settings
from pathlib import Path

class Resources(object):
  @staticmethod
  def find(type, filename):
    if Path(filename).is_absolute():
      raise ValueError('find_resource expects a relative path, got {path}'.format(path = filename))
    if "/" in type:
      raise ValueError('find_resource expects a directory name for type, got {type}'.format(type = type))
    all_apps = settings.INSTALLED_APPS.copy()
    all_apps.append('nabd')
    basepath = Path(settings.BASE_DIR)
    for app in all_apps:
      path = basepath.joinpath(app, type, filename)
      if path.is_file():
        return path
    return None
