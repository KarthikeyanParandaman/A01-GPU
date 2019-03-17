'''
Created on 27-Feb-2019

@author: Karthi SP
'''
from google.appengine.ext import ndb
class MyGpu(ndb.Model):
    name = ndb.StringProperty()
    manufacturer = ndb.StringProperty()
    date_issued = ndb.DateProperty()
    geometry_shader = ndb.BooleanProperty(default=False)
    tesselation_shader = ndb.BooleanProperty(default=False)
    shaderInt16 = ndb.BooleanProperty(default=False)
    sparse_binding = ndb.BooleanProperty(default=False)
    texture_compressionETC2 = ndb.BooleanProperty(default=False)
    vertex_pipeline_storesandAtomics = ndb.BooleanProperty(default=False)
