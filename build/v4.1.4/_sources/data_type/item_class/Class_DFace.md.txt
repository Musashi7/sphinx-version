# DFace

## Description

Face item class.

## Properties

|Attribute|Description|
|-|-|
|typeID|Item type ID (=6). The DItemType.<br>_#Get the integer value of Entity ItemType._<br>The return value is int(DItemw::GetItemTypeInt).|
|key|The internal ID of the item. This is a _unique ID_ within each _typeID_ and __cannot be changed__ by the user.<br>_#Get the internal Key of Entity._<br>The return value is ID (int).|
|id|The external ID of the item.<br>It can be duplicated within each typeID, but it is not recommended.<br>Some entity IDs can be changed with the renumber function.<br>_#Get the external ID of Entity._<br>The return value is ID (int).|
|edges|_#Get Edge information set for Face._<br>The return value is a DEdgeW array.|
|elems|Nodes (array of ElemVector class) included in the item.<br>_#Get the element information set in Face._<br>Get the element information set in Face.|
|nodes|Nodes included in the item (Array of NodeVector class).<br>_#Get the node information set for Face._<br>The return value is a DNodeW array.
|color|Item color information.|
