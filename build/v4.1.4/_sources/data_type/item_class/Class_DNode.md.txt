# DNode

## Description

Node item class.

## Properties

|Attribute|Description|
|-|-|
|typeID|Item type ID (=3)<br>_#Get the integer value of Entity ItemType_<br>The return value is an `int(DItemw::GetItemTypeInt)`|
|key|The internal ID of the item. This is a _unique ID_ within each _typeID_ and __cannot be changed__ by the user.<br>_#Internal Key acquisition of Entity_<br>The return value is `ID (int)`|
|id|The external ID of the item.<br>It can be duplicated within each typeID, but it is not recommended.<br>Some entity IDs can be changed with the renumber function.<br>_#Entity external ID acquisition_<br>The return value is `ID (int)`|
|isFloating|The return value is True for floating nodes.|
|pos|Holds the position coordinates of the node in TVector3d type.|
