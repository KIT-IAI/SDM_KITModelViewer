# KITModelViewer

The KITModelViewer is a freeware application developed at the Institute for Automation and Applied Informatics at KIT (Karlsruhe Institute of Technology). It is used to visualise and analyze semantic data models from the fields of BIM (Building Information Modelling) and GIS (Geographic Information Systems). The focus is on open, standardised data formats.

On the detail level of buildings, the IFC data model is supported in the SPF (STEP Physical File) and ifcXML file formats from version IFC2X onwards. For the building simulation, gbXML (Green Building XML) is supported, which serves as an exchange file format from BIM to energy simulation systems.

On the detail level of cities and districts, CityGML is supported from version 0.4.0 onwards including the ADE (Application Domain Extension) extension concept.

In addition to the two major data models IFC and CityGML, a whole range of other data formats are supported ([see also](#Supported-data-models-and-file-formats)).

<img width="1545" alt="KITModelViewer" src="https://github.com/user-attachments/assets/494ebacb-02d9-426f-9b8c-48ec2d2cbc8f"><br>

Two APIs are available for the KITModelViewer. One is a [Python API](https://github.com/KIT-IAI/SDM_Plugin_Python) for the rapid development of compact scripts to evaluate the imported data or for the development of more complex Python plugins with integration of external modules. The Python Plugin is available as open source and is realized as a plugin based on the C++ plugin SDK.
For more experienced developers with C++ knowledge, a [plugin SDK](https://github.com/KIT-IAI/SDM_Plugin_SDK) is available that provides full access to the internal data structures and functionalities.

An overview of freely available plugins can be found here: [SDM_Plugin_General](https://github.com/KIT-IAI/SDM_Plugin_General)

The sources of the KITModelViewer are not publicly accessible for various reasons, but it is planned to publish individual, selected parts of the source code, especially in relation with the plugin mechanism.
In addition, various use cases for the application of the KITModelViewer with different data formats will be documented in this repo.

## Supported data models and file formats
* IFC - Industry Foundation Classes
* gbXML - Green Building XML
* GML - Geography Markup Language (CityGML, EnergyADE, NAS, ALKIS-WFS, ...)
* LandXML
* EnergyPlus (IDF, EPjson)
* CIM - Common Information Model
* Pointcloud data (e57, las, laz, lad, xyz, pts, ...)
* Panorama Images (tif, jpg, png, ...)

## Application Examples
* Creation of 3D CityGML buildings based on OSM data
* Setup und usage of a OGC Web Feature Service
  
## Examples of Python Scripts
* [CityGML](Python/CityGML)

## How to cite

```bibtex
@software{SDM_KITModelViewer,
	title        = {SDM_KITModelViewer},
	author       = {{Andreas Geiger}},
	url          = {https://github.com/KIT-IAI/SDM_KITModelViewer},
	date         = {2025}
}
```
