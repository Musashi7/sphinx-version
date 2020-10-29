# DElem

## Description

Element item class.

## Properties

|Attribute|Description|
|-|-|
|typeID|Item type ID (=11). The DItemType.<br>*#Get the integer value of Entity ItemType*<br>The return value is int.(DItemw::GetItemTypeInt)|
|key|The internal ID of the item. This is a `unique ID` within each `typeID` and ``cannot be changed`` by the user.<br>*#Get the internal Key of Entity*<br>The return value is ID (int).|
|id|The external ID of the item.<br>It can be duplicated within each TypeID, but it is not recommended.<br>Some entity IDs can be changed with the renumber function.<br>*#Get the external ID of Entity*<br>The return value is ID (int).|
|type|The name of the item.<br>*#Get the Type of Element*<br>The return value is ELEM`TYPE.|
|kind|The type of element (ElemKind type).<br>*#Get the type of Element*<br>The return value is ELEM`KIND.|
|nodes|Nodes included in the item (Array of NodeVector class).<br>*#Get the node information set in Element*<br>The return value is a DNodeW array.|
|color|Item color information.<br>`Color setting of Element.`|
