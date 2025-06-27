# CityGML roof analysis (RoofKIT project)

[RoofKIT](https://roofkit.de/), developed as part of the ‘Solar Decathlon Europe 21/22’, is an energy concept for CO₂-neutral extensions on existing urban flat roofs with roof-integrated PVT collectors, heat pumps, electricity and heat storage systems and an intelligent energy management system. The aim is to achieve a high degree of solar self-generation, grid-friendliness and the creation of living space. As such extensions have an impact on the electricity grid, their effect is being investigated experimentally under real conditions in the KIT Energy Laboratory's real laboratory - including user behaviour and grid connection - in order to develop solutions for energy management at building and grid level.
 
As not every building is suitable for an extension, building models are analysed in the neutral CityGML standard to identify suitable existing buildings. The aim is to quantify residential buildings with flat roofs and sufficient roof area for a RoofKIT extension. The Python script developed for this purpose identifies precisely these residential buildings with flat roofs and writes their gml:id, building height and roof area to a .csv file for further processing.

##Main Document Control
The code begins by establishing a connection to the document and initializing message logging. This setup ensures proper access to all document entities and enables tracking of the process through message outputs.
First Entity Loop The initial loop iterates through all entities in the document using the get_entities method. This loop's purpose is to examine every entity available in the document to identify potential building structures.
First Conditional Check (Building Type) Within the first loop, a conditional statement checks if the current entity is of type "building". This check serves as a filter to ensure only building-type entities are processed further, preventing unnecessary processing of non-building entities.
Children Collection After identifying a building, the code retrieves all children elements associated with that building using the get_children method. This collection step is crucial for accessing the hierarchical structure of building components that need to be analyzed.
Second Loop (Children Processing) A second loop processes each child element obtained from the building structure. The purpose of this loop is to examine each component of the building individually, allowing for detailed analysis of specific building elements.
Second Conditional Check (Roof Surface) Within the children loop, another conditional statement identifies if the current child element is a roof surface. This specific check enables the code to focus on roof-related calculations and data collection.
Data Processing Section Following the roof surface identification, the code processes quantities and properties related to both the building and its roof surface. This section's purpose is to extract and calculate relevant measurements and characteristics needed for analysis.
File Handling Conditional A conditional statement checks for the existence of an output file. This check determines whether to create a new file or append to an existing one, ensuring proper data storage management.
Data Writing Loop The final loop processes the collected quantities and writes them to the output file. Its purpose is to organize and store the processed data in a structured format while maintaining data integrity.
Property Validation Conditional A series of nested conditions verify the presence and validity of required properties. These checks ensure data quality by confirming that all necessary information is available and properly formatted before processing.
Value Processing Conditionals Multiple conditional statements handle the conversion and validation of numerical values. Their purpose is to ensure accurate data transformation and prevent processing errors from invalid or missing data.
Error Handling Sections Throughout the code, various error-handling blocks manage potential issues during data processing. These sections ensure the code continues to function even when encountering unexpected data or processing problems, while maintaining a record of any issues.
Success/Failure Tracking The code maintains counters for successful and failed operations throughout the process. This tracking system provides accountability and helps identify potential issues in the data processing workflow.
Data Storage The data is stored in a .csv file with a header as defined at the top in the code. The file will be in the same location as the .gml file from where it was locally loaded into CityGML.




<u>Example code:</u>
```
import ifcdb
import re
import csv
import os


def get_roof_surface():
    document = ifcdb.get_document()

    document.log_message("Code initialized")

    # Initialize counters for success and failure
    success_count = 0
    failure_count = 0

    # Define the file path and header
    file_path = "output.csv"
    header = ["BuildingHeight [m]", "Surface Area [m2]", "gml:id"]

    # exchange these two loops for selected or all entities
    # for Roof in document.get_selected_entities():
    for Roof in document.get_entities():


        if Roof.type == f"bldg:Building":

            roofProperties = Roof.get_properties()

            allChildren = Roof.get_children()

            for child in allChildren:

                if child.type == f"bldg:RoofSurface":
                    dictQuantities = child.calc_quantities()
                    gml_id = roofProperties.get("gml:id", "Unknown")
                    # document.log_message(dictQuantities)

                    # Check if the file already exists
                    file_exists = os.path.isfile(file_path)

                    # Open the CSV file in append mode or write mode
                    with open(file_path, mode='a' if file_exists else 'w', newline='') as file:
                        writer = csv.writer(file)

                        # Write the header if the file does not exist
                        if not file_exists:
                            writer.writerow(header)

                        # Loop through dictQuantities
                        for element in dictQuantities:

                            # Check if both keys are present
                            if 'SurfaceArea' in dictQuantities and "bldg:measuredHeight" in roofProperties:
                                document.log_message("Both SurfaceArea and measuredHeight found.")

                                try:
                                    # Extract the values
                                    roofSurface = dictQuantities['SurfaceArea']
                                    buildingHeight = roofProperties["bldg:measuredHeight"]

                                    document.log_message(f"SurfaceArea: {roofSurface}")
                                    document.log_message(f"BuildingHeight: {buildingHeight}")

                                    # Check if they are not None
                                    if roofSurface is None and buildingHeight is None:
                                        document.log_message("One of the values is None.")
                                        failure_count += 1
                                        continue

                                    try:
                                        # Convert to float and round
                                        float_roofSurface = round(float(roofSurface), 2)
                                    except ValueError:
                                        document.log_message(f"Failed to convert SurfaceArea '{roofSurface}' to float.")
                                        failure_count += 1
                                        continue

                                    # Extract the numerical value from buildingHeight string
                                    value_buildingHeight = re.search(r'-?\d+\.\d+|-?\d+', buildingHeight)

                                    if value_buildingHeight:
                                        try:
                                            float_buildingHeight = float(value_buildingHeight.group())
                                        except ValueError:
                                            document.log_message(
                                                f"Failed to convert BuildingHeight '{value_buildingHeight.group()}' to float.")
                                            failure_count += 1
                                            continue

                                        document.log_message(f"SurfaceArea: {float_roofSurface}")
                                        document.log_message(f"BuildingHeight: {float_buildingHeight}")

                                        # Write to CSV
                                        data_row = [float_buildingHeight, float_roofSurface, gml_id]
                                        writer.writerow(data_row)
                                        document.log_message(f"Data written to file")
                                        success_count += 1

                                        break
                                    else:
                                        document.log_message("No valid number found in buildingHeight.")
                                        failure_count += 1
                                except KeyError as e:
                                    document.log_message(f"KeyError: {e} not found.")
                                    failure_count += 1
                                except Exception as e:
                                    document.log_message(f"Unexpected error: {e}")
                                    failure_count += 1
                            else:
                                document.log_message("Required keys not found.")
                                failure_count += 1

    # Log the summary
    document.log_message(f"Write Summary: {success_count} successful, {failure_count} failed.")
    document.log_message("Code executed")

```
