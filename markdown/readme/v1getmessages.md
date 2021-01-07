# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_array_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;driverId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | ID of the driver for whom the message is sent to or sent by. |
| **&nbsp;&nbsp;&nbsp;&nbsp;isRead**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | True if the message was read by the recipient. |
| **&nbsp;&nbsp;&nbsp;&nbsp;sender**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of user that is sending the message. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Type of user that is sending the message. It will be either dispatch or driver. |
| **&nbsp;&nbsp;&nbsp;&nbsp;sentAtMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The time in Unix epoch milliseconds that the message is sent to the recipient. |
| **&nbsp;&nbsp;&nbsp;&nbsp;text**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The text sent in the message. |
