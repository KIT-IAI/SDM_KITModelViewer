# CityGML building enrichment

3D building models in the CityGML data format are freely available as open data in Germany and various other countries. However, this data does not usually contain information like year of construction, building type or building usage type. This information is typically contained in the cadastral data. 
As an application example, individual buildings from the 3D city model of the city of Vienna will be considered for a thermal analysis. The cadastral data for Vienna is also freely available as an XML Format and can be converted into the geoJSON format. The CityGML city model and the GeoJSON dataset can be imported and processed in the KITModelViewer. A small Python script is used to enrich the CityGML buildings and executed with the Python plugin. In the CityGML buildings, the gml:name attribute is identical to the ‘ACD’ attribute from the building information in the cadastral data.  
In the following Python script, a dictionary with the cadastral data is created in a first loop. The ACD identifier is used as the key and the entity with the building attributes as the value. In a second loop, the CityGML buildings are iterated over and the building information from the cadastral data is searched by using the building name in the dictionary. The year of construction is then searched within this building information and the bldg:yearOfConstruction attribute is created in the CityGML building and the corresponding value is assigned. 
Alternatively, a spatial search would also be possible here. The cadastral data contains one point geometry per building. This point coordinate can be used to check within which building it is located and the attributes searched for can be assigned accordingly.

<u>__Example code:__</u>
```
import ifcdb

def enrich_citygml_properties():

    document = ifcdb.get_document()

    geojsonDict = {} 

    for geojson_entity in document.get_entities_by_type("GeoJSON Data"):

        tBuildingName = geojson_entity.get_string_attribute("ACD")

        geojsonDict[tBuildingName] = geojson_entity

    for building in document.get_entities_by_type("bldg:Building"):

        document.log_message(f"Building processed {building.name}")

        geojson_entity = geojsonDict.get(building.name)

        if geojson_entity != None:

            tBaujahr = geojson_entity.get_string_attribute("BAUJAHR")

            try:
                    
                iBaujahr = int(tBaujahr)
                    
                if iBaujahr > 0:

                    building.add_date_attribute("bldg:yearOfConstruction", iBaujahr, 0, 0)

                    document.log_message(f"Name: {building.name}: yearOfConstruction {iBaujahr} assigned")

            except:

                document.log_message(f"Conversion failed {tBaujahr}")
```
