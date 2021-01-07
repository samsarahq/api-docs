# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **assets**<br/>_object array_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;assetSerialNumber**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Asset serial number |
| **&nbsp;&nbsp;&nbsp;&nbsp;cable**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | The cable connected to the asset |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assetType**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Asset type |
| **&nbsp;&nbsp;&nbsp;&nbsp;engineHours**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Engine hours |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Asset ID |
| **&nbsp;&nbsp;&nbsp;&nbsp;location**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | Current location of an asset |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;latitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | The latitude of the location in degrees. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;location**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The best effort (street,city,state) for the latitude and longitude. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;longitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | The longitude of the location in degrees. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speedMilesPerHour**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | The speed calculated from GPS that the asset was traveling at in miles per hour. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | Time in Unix milliseconds since epoch when the asset was at the location. |
| **&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Asset name |
| **pagination**<br/>_object_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;endCursor**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Cursor identifier representing the last element in the response. This value should be used in conjunction with a subsequent request's 'startingAfter' query parameter. |
| **&nbsp;&nbsp;&nbsp;&nbsp;hasNextPage**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | True if there are more pages of results after this response. |
| **&nbsp;&nbsp;&nbsp;&nbsp;hasPrevPage**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | True if there are more pages of results before this response. |
| **&nbsp;&nbsp;&nbsp;&nbsp;startCursor**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Cursor identifier representing the first element in the response. This value should be used in conjunction with a subsequent request's 'ending_before' query parameter. |
