# CityGML roof analysis (RoofKIT project)

RoofKIT, developed as part of the ‘Solar Decathlon Europe 21/22’, is an energy concept for CO₂-neutral extensions on existing urban flat roofs with roof-integrated PVT collectors, heat pumps, electricity and heat storage systems and an intelligent energy management system. The aim is to achieve a high degree of solar self-generation, grid-friendliness and the creation of living space. As such extensions have an impact on the electricity grid, their effect is being investigated experimentally under real conditions in the KIT Energy Laboratory's real laboratory - including user behaviour and grid connection - in order to develop solutions for energy management at building and grid level.
 
As not every building is suitable for an extension, building models are analysed in the neutral CityGML standard to identify suitable existing buildings. The aim is to quantify residential buildings with flat roofs and sufficient roof area for a RoofKIT extension. The Python script developed for this purpose identifies precisely these residential buildings with flat roofs and writes their gml:id, building height and roof area to a .csv file for further processing.

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
