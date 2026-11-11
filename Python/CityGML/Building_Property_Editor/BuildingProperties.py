import ifcdb
import re

class BuildingProperty:

    def __init__(self, property_name, control, unit_control=None):
        self.property_name = property_name
        self.control = control
        self.unit_control = unit_control
        self.change_state = False

    def mark_changed(self):
        self.change_state = True

    def reset_changed(self):
        self.change_state = False

    def get_value(self):
        return self.control.GetValue()

    def set_value(self, value):

        if self.unit_control is not None:
            value, unit = self.split_value_unit(value)

            if unit:
                self.unit_control.SetLabel(unit)

        self.control.ChangeValue("" if value is None else str(value))
        self.reset_changed()

    def split_value_unit(self, value):
        if value is None:
            return "", ""

        match = re.match(r"^\s*(.*?)\s*(?:\[([^\]]+)\])?\s*$", str(value))

        if match:
            return match.group(1).strip(), (match.group(2) or "").strip()

        return str(value).strip(), ""

class BuildingProperties:

    def __init__(self, dialog):

        self.properties = {
            "gml:id": BuildingProperty("gml:id", dialog.m_gmlId),
            "bldg:function": BuildingProperty("bldg:function", dialog.m_buildingFunction),
            "bldg:yearOfConstruction": BuildingProperty("bldg:yearOfConstruction", dialog.m_yearOfConstruction),
            "bldg:roofType": BuildingProperty("bldg:roofType", dialog.m_roofType),
            "bldg:measuredHeight": BuildingProperty("bldg:measuredHeight", dialog.m_buildingHeight, dialog.m_buildingHeightUnit),
            "bldg:storeysAboveGround": BuildingProperty("bldg:storeysAboveGround", dialog.m_storeysAboveGround),
            "bldg:storeyHeightsAboveGround": BuildingProperty("bldg:storeyHeightsAboveGround", dialog.m_storeyHeightsAboveGround),
            "bldg:storeysBelowGround": BuildingProperty("bldg:storeysBelowGround", dialog.m_storeysBelowGround),
            "bldg:storeyHeightsBelowGround": BuildingProperty("bldg:storeyHeightsBelowGround", dialog.m_storeyHeightsBelowGround),
        }

    def mark_changed(self, property_name):
        prop = self.properties.get(property_name)

        if prop is not None:
            prop.mark_changed()

    def is_string_attribute(self, attribute_name):
        return attribute_name in ["gml:id", "bldg:function", "bldg:roofType", "bldg:storeyHeightsAboveGround", "bldg:storeyHeightsBelowGround"]

    def is_integer_attribute(self, attribute_name):
        return attribute_name in ["bldg:yearOfConstruction", "bldg:storeysAboveGround", "bldg:storeysBelowGround"]

    def is_double_attribute(self, attribute_name):
        return attribute_name in ["bldg:measuredHeight"]

    def fill(self, building):

        values = building.get_properties() or {}

        for key, prop in self.properties.items():
            prop.set_value(values.get(key))

    def store(self, building):

        for key, prop in self.properties.items():

            if not prop.change_state:
                continue

            value = prop.get_value()

            if value == "":
                continue

            if self.is_string_attribute(key):

                setter = building.set_string_attribute
                adder = building.add_string_attribute

            elif self.is_integer_attribute(key):

                try:
                    value = int(value)
                except ValueError:
                    return False

                setter = building.set_integer_attribute
                adder = building.add_integer_attribute

            elif self.is_double_attribute(key):

                try:
                    value = float(value)
                except ValueError:
                    return False

                setter = building.set_double_attribute
                adder = building.add_double_attribute

            else:
                continue

            if values.get(key) is not None:
                setter(key, value)
            else:
                adder(key, value)

            prop.reset_changed()

        return True