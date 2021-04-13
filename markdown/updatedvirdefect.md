# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;comment**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Comment on the defect. |
| **&nbsp;&nbsp;&nbsp;&nbsp;createdAtTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Time when the defect was created. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;defectType**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The type of DVIR defect. |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the defect. |
| **&nbsp;&nbsp;&nbsp;&nbsp;isResolved**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Signifies if this defect is resolved. |
| **&nbsp;&nbsp;&nbsp;&nbsp;mechanicNotes**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The mechanics notes on the defect. |
| **&nbsp;&nbsp;&nbsp;&nbsp;mechanicNotesUpdatedAtTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Time when mechanic notes were last updated. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;resolvedAtTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Time when this defect was resolved. Will not be returned if the defect is unresolved. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;resolvedBy**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | The person who resolved this defect.  Will not be returned if the defect is unresolved. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the entity that resolved this defect. If the defect was resolved by a driver, this will be a Samsara Driver ID. If the defect was resolved by a mechanic, this will be the Samsara Dashboard User ID of the mechanic. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the person who resolved this defect. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Indicates whether this defect was resolved by a `driver` or a `mechanic`. Valid values: `driver`, `mechanic`. |
