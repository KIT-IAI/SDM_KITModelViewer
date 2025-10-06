# Querying IFC georeferencing information

Supported types of IFC georeferencing:
- IfcMapConversion / IfcRigidOperation
- ePset_MapConversion / ePset_RigidOperation
- Latitude/longitude of the IfcSite
- Georeferencing via the WorldCoordinateSystem (WCS) of the IfcGeometricRepresentationContext
- Global coordinates in the local placement of a component
- Global coordinates within the coordinates of the geometry of a component

If a model contains multiple types of georeferences, the distance between them is calculated.
If an address is also available for IfcSite or IfcBuilding, the distance between the georeference and the address is also calculated.

<img width="854" height="1011" alt="IFC_GeoreferenceInfo" src="https://github.com/user-attachments/assets/edf538b2-598f-4705-8f49-89061ec6648c" />
