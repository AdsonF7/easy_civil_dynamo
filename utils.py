import sys
import clr
import inspect
# Add Assemblies for AutoCAD and Civil3D
clr.AddReference('AcMgd')
clr.AddReference('AcCoreMgd')
clr.AddReference('AcDbMgd')
clr.AddReference('AecBaseMgd')
clr.AddReference('AecPropDataMgd')
clr.AddReference('AeccDbMgd')
clr.AddReference('ProtoGeometry')
# Import references from AutoCAD
from Autodesk.AutoCAD.Runtime import *
from Autodesk.AutoCAD.ApplicationServices import *
from Autodesk.AutoCAD.EditorInput import *
from Autodesk.AutoCAD.DatabaseServices import *
from Autodesk.AutoCAD.Geometry import *

# Import references from Civil3D
from Autodesk.Civil.ApplicationServices import *
from Autodesk.Civil.DatabaseServices import *

from Autodesk.DesignScript.Geometry import Vector
from Autodesk.DesignScript.Geometry import Cuboid
from Autodesk.DesignScript.Geometry import Plane
from Autodesk.DesignScript.Geometry import Point
# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN

adoc = Application.DocumentManager.MdiActiveDocument
editor = adoc.Editor
offset = 0.1
def PointToVector(point):
	return Vector.ByCoordinates(point.X, point.Y, point.Z)
outs = []
with adoc.LockDocument():
	with adoc.Database as db:
		with db.TransactionManager.StartTransaction() as t:
			list_coords = IN[0][0]
			for i in list_coords:
				x_axis = i.XAxis
				y_axis = i.YAxis
				geometry = Cuboid.ByLengths(10, 10, 10)
				
				geometry = geometry.Rotate(Plane.ByOriginNormal(Point.ByCoordinates(0, 0, 0), Vector.ByCoordinates(0, 0, 1)), 20)
				geometry = geometry.Translate(PointToVector(i.Origin))
				outs.append(geometry)
				#OUT = inspect.getdoc(geometry.Rotate)
OUT = outs
# Assign your output to the OUT variable.


