# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **downloadForwardVideoUrl**<br/>_string_ | URL for downloading the forward facing video |
| **downloadInwardVideoUrl**<br/>_string_ | URL for downloading the inward facing video |
| **downloadTrackedInwardVideoUrl**<br/>_string_ | URL for downloading the tracked inward facing video |
| **harshEventType**<br/>_string_ | Type of the harsh event. One of: [Crash, Harsh Acceleration, Harsh Braking, Harsh Turn, ROP Engine, ROP Brake, YC Engine, YC Brake, Harsh Event] |
| **incidentReportUrl**<br/>_string_ | URL of the associated incident report page |
| **isDistracted**<br/>_boolean_ | Whether the driver was deemed distracted during this harsh event |
| **location**<br/>_object_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;address**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Address of location where the harsh event occurred |
| **&nbsp;&nbsp;&nbsp;&nbsp;latitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;number_ | Latitude of location where the harsh event occurred |
| **&nbsp;&nbsp;&nbsp;&nbsp;longitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;number_ | Longitude of location where the harsh event occurred |
