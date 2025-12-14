# 3D CityGML building generation based on GlobalBuildingAtlas
[GlobalBuildingAtlas](https://github.com/zhu-xlab/GlobalBuildingAtlas) provides 2D building outlines worldwide and allows access via standardized OGC WebFeatureService. This article describes how to set up the web service in KITModelViewer and how to retrieve data. It also shows how to use the [GlobalBuildingAtlas BuldingCreator](https://github.com/KIT-IAI/SDM_Plugin_GlobalBuildingAtlas-BuildingCreator) plugin to create 3D buildings in CityGML format from this data.
## Setup the WebService

Go to the <kbd>Web Service toolbar</kbd>, use the context menu an <kbd>Add New Web Service</kbd> and fill the dialog with the url: ```http://tubvsig-so2sat-vm1.srv.mwn.de/geoserver/ows?```

<img width="474" height="465" alt="grafik" src="https://github.com/user-attachments/assets/4cf5957a-a15e-4dd7-8832-001e65693163" />
<img width="471" height="463" alt="grafik" src="https://github.com/user-attachments/assets/d405b425-2f47-447c-9129-7bb1bc8f24b5" />


## Request data from WebService

## Use plugin for 3D building creation

