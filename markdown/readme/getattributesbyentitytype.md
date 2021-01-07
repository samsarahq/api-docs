# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object array_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;attributeType**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Denotes the data type of the attribute's values. |
| **&nbsp;&nbsp;&nbsp;&nbsp;attributeValueQuantity**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Defines whether or not this attribute can be used on the same entity many times (with different values). |
| **&nbsp;&nbsp;&nbsp;&nbsp;entityType**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Denotes the type of entity, driver or vehicle. |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The samsara id of the attribute object. |
| **&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of attribute. |
| **&nbsp;&nbsp;&nbsp;&nbsp;numberValues**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;number array_ | Number values that can be associated with this attribute |
| **&nbsp;&nbsp;&nbsp;&nbsp;stringValues**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string array_ | String values that can be associated with this attribute |
| **pagination**<br/>_object_ | Pagination parameters. |
| **&nbsp;&nbsp;&nbsp;&nbsp;endCursor**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Cursor identifier representing the last element in the response. This value should be used in conjunction with a subsequent request's 'after' query parameter. This may be an empty string if there are no more pages left to view. |
| **&nbsp;&nbsp;&nbsp;&nbsp;hasNextPage**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | True if there are more pages of results immediately available after this endCursor. |
