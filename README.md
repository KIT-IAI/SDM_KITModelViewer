# KITModelViewer

The KITModelViewer is free software developed at the Institute for Automation and Applied Computer Science at KIT (Karlsruhe Institute of Technology). It is used to visualise semantic data models from the fields of BIM (Building Information Modelling) and GIS (Geographic Information Systems). The focus here is on open, standardised data formats.

On the detail level of buildings, the IFC data model is supported in the SPF (STEP Physical File) and ifcXML file formats from version IFC2X onwards. For the building simulation, gbXML (Green Building XML) is supported, which serves as an exchange file format from BIM to energy simulation systems.

On the detail level of cities and districts, CityGML is supported from version 0.4.0 onwards including the ADE (Application Domain Extension) extension concept.

The sources of the KITModelViewer are not publicly accessible for various reasons, but it is planned to publish individual, selected parts of the source code, especially in relation with the plugin mechanism. Various use cases for the application of the KITModelViewer are also documented here step by step.

## Application Examples
* Creation of 3D CityGML buildings from OSM data
* Setup und usage of a OGC web service
  
## Examples of Python Scripts
* [CityGML](CityGML)

## How to cite

```bibtex
@software{SDM_KITModelViewer,
	title        = {SDM_KITModelViewer},
	author       = {{Andreas Geiger}},
	url          = {https://github.com/KIT-IAI/SDM_KITModelViewer},
	date         = {2025}
}
```
