# DBody

## Description

Part item class.

## Properties

|Attribute|Description|
|-|-|
|typeID|Item type ID (= 3). DItemType.<br>*#Get the integer value of Entity ItemType*<br>The return value is int`(DItemw::GetItemTypeInt)`|
|key|The internal ID of the item. This is a _unique ID_ within each _typeID_ and __cannot be changed__ by the user.<br>*#Get the internal Key of Entity*<br>The return value is `ID`.|
|id|External ID of the item. Duplicate within each TypeID, but not recommended.<br>Some entity IDs can be changed with the renumbering function.<br>*#Get the external ID of Entity*<br>The return value is `ID (int)`|
|name|Item name.|
|faces|The faces (Array of FaceVector class) included in the item.<br>*#Get Face information set in Part*<br>The return value is a `DFaceW` array.|
|edges|The edges (Array of the EdgeVector class) included in the item.<br>*#Get Edge information set in Part*<br>The return value is a `DEdgeW` array.|
|elems|Element contained in the item (Array of ElemVector class).<br>*#Get the information of the elements set in Part*<br>The return value is a `DElemW` array.|
|nodes|Nodes included in the item (Array of NodeVector class).<br>*#Get the node information set in Part*<br>The return value is a `DNodeW` array.|
|vertex|The vertices included in the item (An array of VertexVector class).<br>*#Get the Vertex information set in Part*<br>The return value is a `DVertexW` array.|
|color|Item color information.|
|transparance|The transparency of the item.|
