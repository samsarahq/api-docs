# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **trips**<br/>_object array_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;assetIds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer array_ | List of associated asset IDs |
| **&nbsp;&nbsp;&nbsp;&nbsp;codriverIds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer array_ | List of codriver IDs |
| **&nbsp;&nbsp;&nbsp;&nbsp;distanceMeters**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Length of the trip in meters. This value is calculated from the GPS data collected by the Samsara Vehicle Gateway. |
| **&nbsp;&nbsp;&nbsp;&nbsp;driverId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | ID of the driver. |
| **&nbsp;&nbsp;&nbsp;&nbsp;endAddress**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | Text representation of nearest identifiable location to the end (latitude, longitude) coordinates. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The formatted address |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | The ID of the address |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The name of the address |
| **&nbsp;&nbsp;&nbsp;&nbsp;endCoordinates**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | End (latitude, longitude) in decimal degrees. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;latitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;longitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;endLocation**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Geocoded street address of start (latitude, longitude) coordinates. |
| **&nbsp;&nbsp;&nbsp;&nbsp;endMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | End of the trip in UNIX milliseconds. Ongoing trips are indicated by an endMs value of 9223372036854775807. |
| **&nbsp;&nbsp;&nbsp;&nbsp;endOdometer**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Odometer reading (in meters) at the end of the trip. This is read from the vehicle's on-board diagnostics. If Samsara cannot read the vehicle's odometer values from on-board diagnostics, this value will be 0. |
| **&nbsp;&nbsp;&nbsp;&nbsp;fuelConsumedMl**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Amount in milliliters of fuel consumed on this trip. |
| **&nbsp;&nbsp;&nbsp;&nbsp;startAddress**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | Text representation of nearest identifiable location to the start (latitude, longitude) coordinates. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The formatted address |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | The ID of the address |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The name of the address |
| **&nbsp;&nbsp;&nbsp;&nbsp;startCoordinates**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | Start (latitude, longitude) in decimal degrees. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;latitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;longitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;startLocation**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Geocoded street address of start (latitude, longitude) coordinates. |
| **&nbsp;&nbsp;&nbsp;&nbsp;startMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Beginning of the trip in UNIX milliseconds. |
| **&nbsp;&nbsp;&nbsp;&nbsp;startOdometer**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Odometer reading (in meters) at the beginning of the trip. This is read from the vehicle's on-board diagnostics. If Samsara cannot read the vehicle's odometer values from on-board diagnostics, this value will be 0. |
| **&nbsp;&nbsp;&nbsp;&nbsp;tollMeters**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Length in meters trip spent on toll roads. |
