# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| ****<br/>_object array_ | A list of historical asset locations. |
| **latitude**<br/>_number_ | The latitude of the location in degrees. |
| **location**<br/>_string_ | The best effort (street,city,state) for the latitude and longitude. |
| **longitude**<br/>_number_ | The longitude of the location in degrees. |
| **speedMilesPerHour**<br/>_number_ | The speed calculated from GPS that the asset was traveling at in miles per hour. |
| **time**<br/>_number_ | Time in Unix milliseconds since epoch when the asset was at the location. |
