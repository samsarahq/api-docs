# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **assets**<br/>_object array_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;assetSerialNumber**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Serial number of the host asset |
| **&nbsp;&nbsp;&nbsp;&nbsp;cable**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | The cable connected to the asset |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assetType**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Asset type |
| **&nbsp;&nbsp;&nbsp;&nbsp;engineHours**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Engine hours |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Asset ID |
| **&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Asset name |
| **&nbsp;&nbsp;&nbsp;&nbsp;vehicleId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The ID of the Vehicle associated to the Asset (if present) |
