# Querying IFC georeferencing information

This dialog provides an overview of the possible georeferencing options in an IFC models.

Supported types of IFC georeferencing:
- IfcMapConversion / IfcRigidOperation
- Property sets ePset_MapConversion / ePset_RigidOperation
- Geographic coordinates (Latitude / Longitude) of the IfcSite
- Georeferencing via the WorldCoordinateSystem (WCS) of the IfcGeometricRepresentationContext
- Global coordinates in the local placement of a component
- Global coordinates within the coordinates of the geometry of a component

Supported georeferencing variants are attempted to be resolved using a geocoding query; the determined address is displayed in the lower part of the dialog. If several variants are included, the distances between all of them are calculated and displayed. In addition, addresses contained in IfcSite or IfcBuilding are also taken into account and their distances to the georeferencing are calculated.

<img width="854" height="1011" alt="IFC_GeoreferenceInfo" src="https://github.com/user-attachments/assets/edf538b2-598f-4705-8f49-89061ec6648c" />
