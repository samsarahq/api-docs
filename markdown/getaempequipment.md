# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **fleet**<br/>_object_ | Contains equipment fields. |
| **&nbsp;&nbsp;&nbsp;&nbsp;EquipmentID**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The unique Samsara ID of the equipment. This is automatically generated when the Equipment object is created. It cannot be changed. |
| **&nbsp;&nbsp;&nbsp;&nbsp;ExternalIds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | A map of external ids |
| **&nbsp;&nbsp;&nbsp;&nbsp;Hour**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;number_ | Total number of equipment operating hours. |
| **&nbsp;&nbsp;&nbsp;&nbsp;Latitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;number_ | Location latitude. |
| **&nbsp;&nbsp;&nbsp;&nbsp;Longitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;number_ | Location longitude. |
| **&nbsp;&nbsp;&nbsp;&nbsp;Odometer**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;number_ | Odometer value reported by equipment. |
| **&nbsp;&nbsp;&nbsp;&nbsp;OdometerUnits**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Unit of measurement for distance. |
| **&nbsp;&nbsp;&nbsp;&nbsp;PIN**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The PIN number of the equipment. |
| **&nbsp;&nbsp;&nbsp;&nbsp;Percent**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;number_ | Percent of DEF remaining in tank. |
| **&nbsp;&nbsp;&nbsp;&nbsp;Running**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Boolean value for whether engine is running or not. |
| **&nbsp;&nbsp;&nbsp;&nbsp;SerialNumber**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The serial number of the equipment. |
| **&nbsp;&nbsp;&nbsp;&nbsp;UnitInstallDateTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Telematics unit install date in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). |
| **&nbsp;&nbsp;&nbsp;&nbsp;dateTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Date time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). |
