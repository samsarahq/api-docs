# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object array_ | A list of user roles |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The unique ID for the role. |
| **&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The name of the role. |
| **pagination**<br/>_object_ | Pagination parameters. |
| **&nbsp;&nbsp;&nbsp;&nbsp;endCursor**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Cursor identifier representing the last element in the response. This value should be used in conjunction with a subsequent request's 'after' query parameter. This may be an empty string if there are no more pages left to view. |
| **&nbsp;&nbsp;&nbsp;&nbsp;hasNextPage**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | True if there are more pages of results immediately available after this endCursor. |
