# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **crashCount**<br/>_integer_ | Crash event count |
| **driverId**<br/>_integer_ | Driver ID |
| **harshAccelCount**<br/>_integer_ | Harsh acceleration event count |
| **harshBrakingCount**<br/>_integer_ | Harsh braking event count |
| **harshEvents**<br/>_object array_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;harshEventType**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Type of the harsh event |
| **&nbsp;&nbsp;&nbsp;&nbsp;timestampMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Timestamp that the harsh event occurred in Unix milliseconds since epoch |
| **&nbsp;&nbsp;&nbsp;&nbsp;vehicleId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Vehicle associated with the harsh event |
| **harshTurningCount**<br/>_integer_ | Harsh turning event count |
| **safetyScore**<br/>_integer_ | Safety Score |
| **safetyScoreRank**<br/>_string_ | Safety Score Rank |
| **timeOverSpeedLimitMs**<br/>_integer_ | Amount of time driven over the speed limit in milliseconds |
| **totalDistanceDrivenMeters**<br/>_integer_ | Total distance driven in meters |
| **totalHarshEventCount**<br/>_integer_ | Total harsh event count |
| **totalTimeDrivenMs**<br/>_integer_ | Amount of time driven in milliseconds |
