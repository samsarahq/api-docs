# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **id**<br/>_integer_ | ID of the trailer |
| **name**<br/>_string_ | Assignment trailer name (given when creating trailer via the trailer portal) |
| **trailerAssignments**<br/>_object array_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;driverId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The ID of the driver associated with this trailer. |
| **&nbsp;&nbsp;&nbsp;&nbsp;endMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The time at which the driver ended the assignment. If the assignment is current, this value will be omitted. |
| **&nbsp;&nbsp;&nbsp;&nbsp;startMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The time at which the driver started the assignment |
