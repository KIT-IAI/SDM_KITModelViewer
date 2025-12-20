# KITModelViewer

* [KITModelViewer](https://www.iai.kit.edu/ifc) - Windows® freeware application
* [Plugin SDK](https://github.com/KIT-IAI/SDM_Plugin_SDK) - Software development kit for developing your own plugins 
* [Python API](https://github.com/KIT-IAI/SDM_Plugin_Python) - Open-source plugin for a Python API
* [SDM_Plugin_General](https://github.com/KIT-IAI/SDM_Plugin_General) - Repository with open-source plugins
<br>

The [KITModelViewer](https://www.iai.kit.edu/ifc) is a Windows® freeware application developed at the [Institute for Automation and Applied Informatics](https://www.iai.kit.edu) at KIT ([Karlsruhe Institute of Technology](https://www.kit.edu/)). It is used to visualise and analyze semantic data models from the fields of BIM (Building Information Modelling) and GIS (Geographic Information Systems). The focus is on open, standardised data formats.

On the detail level of buildings, the IFC data model is supported in the SPF (STEP Physical File) and ifcXML file formats from version IFC2X onwards. For the building simulation, gbXML (Green Building XML) is supported, which serves as an exchange file format from BIM to energy simulation systems.

On the detail level of cities and districts, CityGML is supported from version 0.4.0 onwards including the ADE (Application Domain Extension) extension concept.

In addition to the two major data models IFC and CityGML, a whole range of other data formats are supported, either [file-based](#Supported-data-models-and-file-formats) or as a [web service](#Supported-web-services).

<img width="1545" alt="KITModelViewer" src="https://github.com/user-attachments/assets/494ebacb-02d9-426f-9b8c-48ec2d2cbc8f"><br>

Two APIs are available for the KITModelViewer. One is a [Python API](https://github.com/KIT-IAI/SDM_Plugin_Python) for the rapid development of compact scripts to evaluate the imported data or for the development of more complex Python plugins with integration of external modules. The Python Plugin is available as open source and is realized as a plugin based on the C++ plugin SDK.
For more experienced developers with C++ knowledge, a [plugin SDK](https://github.com/KIT-IAI/SDM_Plugin_SDK) is available that provides full access to the internal data structures and functionalities.

An overview of freely available plugins can be found here: [SDM_Plugin_General](https://github.com/KIT-IAI/SDM_Plugin_General)

The sources of the KITModelViewer are not publicly accessible for various reasons, but it is planned to publish individual, selected parts of the source code, especially in relation with the plugin mechanism.
In addition, various use cases for the application of the KITModelViewer with different data formats will be documented in this repo.

## Features
* Standard functionality for displaying, navigating in and interacting with 3D models
* Detailed presentation of attributes, property sets, relations and geometries
* Interactive object lists enable a direct link between the list and the 3D scene<br>
  <img width="500" alt="InteractiveLists" src="https://github.com/user-attachments/assets/f49fda25-f650-414b-8b29-90a94778fe71" />
* Individual colour coding of objects based on attributes and properties<br>(The example shows the ThermalTransmittance property of the IFC common property sets)<br>
  <img width="500" alt="ColorCoding_u-Value" src="https://github.com/user-attachments/assets/fde0d293-5e5a-48a0-b3a3-556f2413f16e" />
* BIM and GIS integration. Merging different models and file formats in one 3D scene<br>(The example shows merged data containing IFC, CityGML and a map service)<br>
  <img width="500" alt="ModelMerge" src="https://github.com/user-attachments/assets/d4471f66-b342-4515-8b87-3a7dfdbb81e3" />
* Georeferencing support for a wide range of spatial reference systems<br>
  <img width="500" alt="CityGML_GeoReference" src="https://github.com/user-attachments/assets/d9cd3e62-8b13-43e2-b3e4-9d13b2db5f2f" />
* openBIM validation based on mvdXML, including the creation and editing of mvdXML definitions<br>
  <img width="500" alt="mvdXML" src="https://github.com/user-attachments/assets/20ea1764-5f90-4973-be52-edc617d41ba9" />
* Building energy simulation using [EnergyPlus™](https://github.com/NREL/EnergyPlus). Support for IDF and epJSON data sets, visualization of building geometry, display of parameters, simulation, and presentation of results.<br>
  <img width="500" alt="EnergyPlus" src="https://github.com/user-attachments/assets/ee549246-5f27-4e4f-9103-55ad83811a8d" />

## Supported data models and file formats
* IFC - Industry Foundation Classes
* gbXML - Green Building XML
* GML - Geography Markup Language
	* CityGML, supporting also the Application Domain Extension (ADE) mechanism (EnergyADE, ...)
	* XPlangGML
	* INSPIRE
 	* NAS
  	* ALKIS-WFS
  	* ...
* LandXML
* EnergyPlus (IDF, epJSON)
* CIM - Common Information Model (IEC 61970]
* Pointcloud data (e57, las, laz, lad, xyz, pts, ...)
* Panorama images (tif, jpg, png, ...)

Other supported formats:
* CityJSON
* Shapefile
* GeoJSON
* GeoPackage
* GPX
* [dotbim](https://github.com/paireks/dotbim)
* ISYBAU
* DXF
* CPIxml
* Various 3D formats using [assimp](https://github.com/assimp/assimp) (FBX, OBJ, glTF, ...) 
* Various image formats (PNG, JPG, TIFF, GeoTIFF, ...)

## Supported web services
* OGC Web Services (WFS, WMS, WMTS, WCS, W3DS, SOS, WPS, ...)
* Web map services (Google, OSM, Bing, ...)
* [LOPoCS](https://github.com/Oslandia/lopocs) - Light OpenSource PointCloud Server
* OpenStreetMap (OSM API, Overpass API)
* [ETHOS.BUILDA](https://ethos-builda.fz-juelich.de/api/v8_20240916/swagger/) - Residential Building TABULA Archetype Dataset Germany
* [GlobalBuildingAtlas](https://github.com/zhu-xlab/GlobalBuildingAtlas) - Base polygon and height of buildings across the globe
* [bSDD](https://search.bsdd.buildingsmart.org/) - buildingSMART Data Dictionary
* ILCD - International Life Cycle Data system

## Application Examples
* [Query IFC georeferencing information](Documentation/IFC_GeoreferenceInfo.md)
* Creation of 3D CityGML buildings based on OSM data
* Setup and usage of a OGC Web Feature Service
* [3D CityGML building generation based on GlobalBuildingAtlas](Documentation/CityGML_GlobalBuildingAtlas.md)
  
## Examples of Python Scripts
* [IFC](Python/IFC)
* [gbXML](Python/gbXML)
* [CityGML](Python/CityGML)

## Dependencies
The KITModelViewer is developed for the Windows® operating system and requires the following software packages from Microsoft:<br>
- [Microsoft Visual Studio C++ Redistributalbe](https://aka.ms/vs/17/release/vc_redist.x64.exe)<br>
- [Microsoft .NET Framework 4.8](https://go.microsoft.com/fwlink/?linkid=2088631)<br>
> [!IMPORTANT]
> Make sure that these packages are installed and the latest version of the redistributables is used.

## How to cite

```bibtex
@software{SDM_KITModelViewer,
	title        = {SDM_KITModelViewer},
	author       = {{Andreas Geiger}},
	url          = {https://github.com/KIT-IAI/SDM_KITModelViewer},
	date         = {2025}
}
```

























































