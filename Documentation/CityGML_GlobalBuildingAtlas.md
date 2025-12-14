# 3D CityGML building generation based on GlobalBuildingAtlas
[GlobalBuildingAtlas](https://github.com/zhu-xlab/GlobalBuildingAtlas) provides 2D building outlines worldwide and allows access via standardized OGC WebFeatureService. This article describes how to set up the web service in KITModelViewer and how to retrieve data. It also shows how to use the [GlobalBuildingAtlas BuldingCreator](https://github.com/KIT-IAI/SDM_Plugin_GlobalBuildingAtlas-BuildingCreator) plugin to create 3D buildings in CityGML format from this data.
## Setup the WebService

Go to the <kbd>Web Service Toolbar</kbd>, use the context menu <kbd>Add New Web Service</kbd> and fill the dialog.<br>
Url: ```http://tubvsig-so2sat-vm1.srv.mwn.de/geoserver/ows?```<br><br>
<img width="471" height="463" alt="grafik" src="https://github.com/user-attachments/assets/d405b425-2f47-447c-9129-7bb1bc8f24b5" />

## Request data from WebService
To request building data, you first need to define an bounding box. The easiest way to do this is to use a map query dialog by using the entry <kbd>New Map</kbd> in the main menu below File. Then use the <kbd>Web Service Toolbar</kbd> to create a query with <kbd>Get Specific Feature</kbd>. Use the <kbd>Bounding Box</kbd> button in the Filteroptions to apply the bounding box of the current scene. The new filter is added in the list below. Activate the filter and submit the request by pressing <kbd>OK</kbd>

## Use plugin for 3D building creation

First, you need to make sure that the plugin is already installed. To do this, check under <kbd>Plugins</kbd> to see if the entry <kbd>GlobalBuildingAtlas BuildingCreator</kbd> exists. If not, download the plugin from the GitHub repo [GlobalBuildingAtlas BuildingCreator]() and install it using the menu item <kbd>Install Plugin</kbd>.
Then, all you have to do is start the plugin via the corresponding menu item. If the download was successful, the 3D CityGML buildings will be created and displayed in the current scene.
