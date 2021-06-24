# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object array_ | List of Job Objects |
| **&nbsp;&nbsp;&nbsp;&nbsp;address**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | jobLocation object |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Address of a location |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;latitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | Latitude of a location |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;longitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | Longitude of a location |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of a location |
| **&nbsp;&nbsp;&nbsp;&nbsp;createdAt**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | When the job was created |
| **&nbsp;&nbsp;&nbsp;&nbsp;customerName**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Customer name for job |
| **&nbsp;&nbsp;&nbsp;&nbsp;endDate**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | End date of job in RFC 3339 format |
| **&nbsp;&nbsp;&nbsp;&nbsp;fleetDevices**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | fleet devices in this job (cannot have both industrial assets and fleet devices in the same job) |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Id of the device |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the device |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Job id |
| **&nbsp;&nbsp;&nbsp;&nbsp;industrialAssets**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | Industrial Assets in this job (cannot have both industrial assets and fleet devices in the same job) |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Id of the device |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the industrial asset |
| **&nbsp;&nbsp;&nbsp;&nbsp;modifiedAt**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | When the job was last modified |
| **&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Job name |
| **&nbsp;&nbsp;&nbsp;&nbsp;notes**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Notes for the upcoming job |
| **&nbsp;&nbsp;&nbsp;&nbsp;startDate**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Start date of job in RFC 3339 format |
| **&nbsp;&nbsp;&nbsp;&nbsp;status**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The current job status Valid values: `active`, `scheduled`, `completed`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;uuid**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Samsara uuid |
| **id**<br/>_string_ | The job id of the failed request |
| **pagination**<br/>_object_ | Pagination parameters. |
| **&nbsp;&nbsp;&nbsp;&nbsp;endCursor**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Cursor identifier representing the last element in the response. This value should be used in conjunction with a subsequent request's 'after' query parameter. This may be an empty string if there are no more pages left to view. |
| **&nbsp;&nbsp;&nbsp;&nbsp;hasNextPage**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | True if there are more pages of results immediately available after this endCursor. |
| **uuid**<br/>_string_ | The uuid of the failed request |
