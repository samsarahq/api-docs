# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **days**<br/>_object array_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;activeHours**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;number_ | Hours spent on duty or driving, rounded to two decimal places. |
| **&nbsp;&nbsp;&nbsp;&nbsp;activeMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Milliseconds spent on duty or driving. |
| **&nbsp;&nbsp;&nbsp;&nbsp;certified**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Whether this HOS day chart was certified by the driver. |
| **&nbsp;&nbsp;&nbsp;&nbsp;certifiedAtMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;number_ | Unix epoch time (in ms) of time when this chart was certified. If this chart is uncertified, 0. |
| **&nbsp;&nbsp;&nbsp;&nbsp;distanceMiles**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;number_ | Distance driven in miles, rounded to two decimal places. |
| **&nbsp;&nbsp;&nbsp;&nbsp;endMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | End of the HOS day, specified in milliseconds UNIX time. |
| **&nbsp;&nbsp;&nbsp;&nbsp;shippingDocIds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string array_ | List of customer shipping document IDs associated with the driver for the day. |
| **&nbsp;&nbsp;&nbsp;&nbsp;startMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Start of the HOS day, specified in milliseconds UNIX time. |
| **&nbsp;&nbsp;&nbsp;&nbsp;trailerIds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string array_ | List of trailer ID's associated with the driver for the day. |
| **&nbsp;&nbsp;&nbsp;&nbsp;vehicleIds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | List of vehicle ID's associated with the driver for the day. |
