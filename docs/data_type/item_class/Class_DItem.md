# DItem

## Description

Base class for all items in Jupiter.

## Properties

|Attribute|Description|
|-|-|
|isValid|Determine if it can be used. True if available.<br>_#Check if Entity is available_<br> The return value is `True` if available, `False` if not|
|type|The type of item.<br>_#Get ItemType of Entity_<br>The return value is `ItemType`.|
|typeID|The item type ID (The DItemType)<br>_#Get the integer value of Entity ItemType_<br>The return value is an `int`.|
|key|The internal ID of the item. This is a _unique ID_ within each _typeID_ and __cannot be changed__ by the user.<br>_#Get the internal Key of Entity._<br>The return value is `ID (int)`.|
|id|Item external ID.<br>It can be duplicated within each `TypeID`, but it is not recommended.<br>Some entity IDs can be changed with the renumber function.<br>_#Get the external ID of Entity_<br>The return value is ID (int).|
|name|The name of the item.<br>_#Get Entity name or name setting_|
|targets|Another Item that Item holds.<br>_#Acquisition of Entity set in Entity_<br>The return value is an array of DItem.|
|masters|Master/face/edge/node of connection/contact.<br>_#Acquisition of Master Entity set in Entity_<br>The return value is an array of DItem.|
|slaves|It refers to the slave side face/edge/node of connection/contact.<br>_#Acquisition of Slave Entity set in Entity_<br>The return value is an array of DItem.|
|children|Refers to a sub-assembly of an assembly item within the assembly tree.<br>_#Acquisition of child Entity when it is nested on the tree, array of return value DItem_|
|parent|A sub-assembly that is the parent of an item in the assembly tree.<br>_#Acquisition of parent Entity when nested in tree, DItem_|
|info|Entity information for parts and faces.<br>Including the number of meshes.<br>_#Display entity information. Must be a Tree Item or PartItem_|
