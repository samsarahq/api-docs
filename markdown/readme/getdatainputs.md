# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object array_ | An array of data input objects. Each object contains the data input's name, ID, and other metadata. |
| **&nbsp;&nbsp;&nbsp;&nbsp;assetId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Unique identifier for the data input's asset. |
| **&nbsp;&nbsp;&nbsp;&nbsp;dataGroup**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Data group for this data input. |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Unique identifier for the data input. |
| **&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of this data input. |
| **&nbsp;&nbsp;&nbsp;&nbsp;units**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Units of data for this data input. |
| **pagination**<br/>_object_ | Pagination parameters. |
| **&nbsp;&nbsp;&nbsp;&nbsp;endCursor**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Cursor identifier representing the last element in the response. This value should be used in conjunction with a subsequent request's 'after' query parameter. This may be an empty string if there are no more pages left to view. |
| **&nbsp;&nbsp;&nbsp;&nbsp;hasNextPage**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | True if there are more pages of results immediately available after this endCursor. |
