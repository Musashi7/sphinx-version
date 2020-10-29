# DGroup

## Description

Group class.

## Properties

|Attribute|Description|
|-|-|
|typeID|Item type ID (=79).<br>_#Get the integer value of Entity ItemType._<br>The return value is `int(DItemw::GetItemTypeInt)`|
|key|The internal ID of the item. This is a _unique ID_ within each _typeID_ and __cannot be changed__ by the user.<br>_#Get the internal Key of Entity._<br>The return value is `ID (int)`|
|id|The external ID of the item.<br>It can be duplicated within each typeID, but it is not recommended.<br>Some entity IDs can be changed with the renumber function.<br>_#Get the external ID of Entity._<br>The return value is `ID (int)`.|
|name|The name of the item.|
|targets|Holds the contents of the group.<br>An array of DItem classes.|
