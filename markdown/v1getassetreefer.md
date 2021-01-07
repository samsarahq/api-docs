# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **assetType**<br/>_string_ | Asset type |
| **id**<br/>_integer_ | Asset ID |
| **name**<br/>_string_ | Asset name |
| **reeferStats**<br/>_object_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;alarms**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | Reefer alarms |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alarms**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object array_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alarmCode**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | ID of the alarm |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Description of the alarm |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;operatorAction**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Recommended operator action |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;severity**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Severity of the alarm: 1: OK to run, 2: Check as specified, 3: Take immediate action |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;changedAtMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Timestamp when the alarms were reported, in Unix milliseconds since epoch |
| **&nbsp;&nbsp;&nbsp;&nbsp;engineHours**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | Engine hours of the reefer |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;changedAtMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Timestamp in Unix milliseconds since epoch. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;engineHours**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Engine hours of the reefer. |
| **&nbsp;&nbsp;&nbsp;&nbsp;fuelPercentage**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | Fuel percentage of the reefer |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;changedAtMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Timestamp in Unix milliseconds since epoch. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fuelPercentage**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Fuel percentage of the reefer. |
| **&nbsp;&nbsp;&nbsp;&nbsp;powerStatus**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | Power status of the reefer |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;changedAtMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Timestamp in Unix milliseconds since epoch. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;status**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Power status of the reefer. |
| **&nbsp;&nbsp;&nbsp;&nbsp;returnAirTemp**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | Return air temperature of the reefer |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;changedAtMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Timestamp in Unix milliseconds since epoch. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tempInMilliC**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Return air temperature in millidegree Celsius. |
| **&nbsp;&nbsp;&nbsp;&nbsp;setPoint**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | Set point temperature of the reefer |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;changedAtMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Timestamp in Unix milliseconds since epoch. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tempInMilliC**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Set point temperature in millidegree Celsius. |
