# Structural elements

This example shows how elements of the static model (structural domain) can be queried in an IFC dataset.

<u>__Example code:__</u>
```
import ifcdb

document = ifcdb.get_document()

nodeEntities = document.get_entities_by_type("IfcStructuralPointConnection")

nodes = []
    
dictNodes = {}
    
for entity in nodeEntities:

    node = []
    node.append(entity.guid)

    dictNodes.update({entity.oid : entity.guid})
        
    geometry = entity.get_geometry()

    if (geometry.type == "Vertex"):
        node[1:] = geometry.data[1];
  
    attributesDict = entity.get_attributes()

    boundaryConditionDict = attributesDict.get('AppliedCondition')
        
    if boundaryConditionDict != None:
        node.append(boundaryConditionDict.get('TranslationalStiffnessX'))
        node.append(boundaryConditionDict.get('TranslationalStiffnessY'))
        node.append(boundaryConditionDict.get('TranslationalStiffnessZ'))
        
    nodes.append(node)

document.log_message("Nodes: " + str(nodes))

BarEntities = document.get_entities_by_type("IfcStructuralCurveMember")

bars = []

for entity in BarEntities:

    bar = []

    relations = entity.get_relations("IfcRelConnectsStructuralMember")
        
    bar.append(entity.guid)

    for relation in relations:
                
        attributesDict = relation.get_attributes()

        relatedStructuralELement = document.get_entity_by_oid(attributesDict.get('RelatedStructuralConnection'))

        bar.append(relatedStructuralELement.guid)

    relations = entity.get_relations("IfcRelAssociatesMaterial")

    for relation in relations:

        attributesDict = relation.get_attributes()
            
        document.log_message(attributesDict)
            
        attributesDict.get('MaterialProfiles')
        
    bars.append(bar)

document.log_message("Bars: " + str(bars))

point_loads = []

PointLoadEntities = document.get_entities_by_type("IfcStructuralPointAction")
    
for entity in PointLoadEntities:

    load = []
    load.append(entity.guid)
 
    relations = entity.get_relations("IfcRelConnectsStructuralActivity")

    for relation in relations:
        
        attributesDict = relation.get_attributes()
        
        relatingElement = document.get_entity_by_oid(attributesDict.get('RelatingElement'))
            
        load.append(relatingElement.guid)
 
    attributesDict = entity.get_attributes()

    singleForceDict = attributesDict.get('AppliedLoad')

    if singleForceDict != None:
        load.append(singleForceDict.get('ForceX'))
        load.append(singleForceDict.get('ForceY'))
        load.append(singleForceDict.get('ForceZ'))
        
    point_loads.append(load)

document.log_message("PointLoads: " + str(point_loads))
```
