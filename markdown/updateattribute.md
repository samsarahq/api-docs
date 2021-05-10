# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;attributeType**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Denotes the data type of the attribute's values. Valid values: `string`, `number`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;attributeValueQuantity**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Defines whether or not this attribute can be used on the same entity many times (with different values). Valid values: `single`, `multi`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;entities**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | Entities that this attribute is applied onto |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;entityId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;externalIds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;numberValues**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number array_ | Number values that are associated with this attribute. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stringValues**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string array_ | String values that are associated with this attribute. |
| **&nbsp;&nbsp;&nbsp;&nbsp;entityType**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Denotes the type of entity, driver or aset. Valid values: `driver`, `asset`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The samsara id of the attribute object. |
| **&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of attribute. |
| **&nbsp;&nbsp;&nbsp;&nbsp;numberValues**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;number array_ | Number values that can be associated with this attribute |
| **&nbsp;&nbsp;&nbsp;&nbsp;stringValues**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string array_ | String values that can be associated with this attribute |
