# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object array_ | A list of DVIRs. |
| **&nbsp;&nbsp;&nbsp;&nbsp;authorSignature**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;signedAtTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The time when the DVIR was signed. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Whether the DVIR was submitted by a `driver` or `mechanic`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;endTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Time when driver signed and completed this DVIR. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Unique Samsara ID for the DVIR. |
| **&nbsp;&nbsp;&nbsp;&nbsp;licensePlate**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The license plate of this vehicle. |
| **&nbsp;&nbsp;&nbsp;&nbsp;location**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Optional string if your jurisdiction requires a location of the DVIR. |
| **&nbsp;&nbsp;&nbsp;&nbsp;mechanicNotes**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The mechanics notes on the DVIR. |
| **&nbsp;&nbsp;&nbsp;&nbsp;odometerMeters**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The odometer reading in meters. |
| **&nbsp;&nbsp;&nbsp;&nbsp;safetyStatus**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The condition of vehicle on which DVIR was done. |
| **&nbsp;&nbsp;&nbsp;&nbsp;secondSignature**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;signedAtTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The time when the DVIR was signed. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Whether the DVIR was submitted by a `driver` or `mechanic`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;startTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Time when driver began filling out this DVIR. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;thirdSignature**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;signedAtTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The time when the DVIR was signed. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Whether the DVIR was submitted by a `driver` or `mechanic`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;trailer**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the trailer. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the trailer. |
| **&nbsp;&nbsp;&nbsp;&nbsp;trailerDefects**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;array_ | Defects registered for the trailer which was part of the DVIR. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Comment on the defect. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;createdAtTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Time when the defect was created. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;defectType**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The type of DVIR defect. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the defect. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isResolved**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Signifies if this defect is resolved. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mechanicNotes**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The mechanics notes on the defect. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mechanicNotesUpdatedAtTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Time when mechanic notes were last updated. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;resolvedAtTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Time when this defect was resolved. Will not be returned if the defect is unresolved. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;resolvedBy**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | The person who resolved this defect.  Will not be returned if the defect is unresolved. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the entity that resolved this defect. If the defect was resolved by a driver, this will be a Samsara Driver ID. If the defect was resolved by a mechanic, this will be the Samsara Dashboard User ID of the mechanic. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the person who resolved this defect. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Indicates whether this defect was resolved by a `driver` or a `mechanic`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;trailerName**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The name of the trailer the DVIR was submitted for.  Only included for tractor+trailer DVIRs. |
| **&nbsp;&nbsp;&nbsp;&nbsp;type**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Inspection type of the DVIR. |
| **&nbsp;&nbsp;&nbsp;&nbsp;vehicle**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the vehicle. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the vehicle. |
| **&nbsp;&nbsp;&nbsp;&nbsp;vehicleDefects**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;array_ | Defects registered for the vehicle which was part of the DVIR. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Comment on the defect. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;createdAtTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Time when the defect was created. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;defectType**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The type of DVIR defect. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the defect. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isResolved**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Signifies if this defect is resolved. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mechanicNotes**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The mechanics notes on the defect. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mechanicNotesUpdatedAtTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Time when mechanic notes were last updated. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;resolvedAtTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Time when this defect was resolved. Will not be returned if the defect is unresolved. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;resolvedBy**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | The person who resolved this defect.  Will not be returned if the defect is unresolved. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the entity that resolved this defect. If the defect was resolved by a driver, this will be a Samsara Driver ID. If the defect was resolved by a mechanic, this will be the Samsara Dashboard User ID of the mechanic. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the person who resolved this defect. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Indicates whether this defect was resolved by a `driver` or a `mechanic`. |
| **pagination**<br/>_object_ | Pagination parameters. |
| **&nbsp;&nbsp;&nbsp;&nbsp;endCursor**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Cursor identifier representing the last element in the response. This value should be used in conjunction with a subsequent request's 'after' query parameter. This may be an empty string if there are no more pages left to view. |
| **&nbsp;&nbsp;&nbsp;&nbsp;hasNextPage**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | True if there are more pages of results immediately available after this endCursor. |
