# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;accessoryDevices**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | Accessory devices on gateway |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;model**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Product model name of the device |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The serial number of the accessory device. |
| **&nbsp;&nbsp;&nbsp;&nbsp;asset**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | An object containing information about the asset the gateway is installed on |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;externalIds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | A map of external ids |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The unique Samsara ID of the asset where the gateway is installed. This is automatically generated when the asset is created and cannot be changed. Use this ID on PATCH vehicle, equipment, or trailer endpoints to update the asset |
| **&nbsp;&nbsp;&nbsp;&nbsp;connectionStatus**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | An objecting containing information about the connectivity status of the gateway |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;healthStatus**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The most recent health status of the gateway. Valid values: `Status Not Set`, `Connected`, `Not Installed`, `Power Source Off - Active Vehicle`, `Power Source Off - Inactive Vehicle`, `Weak Cellular Signal`, `Requires Investigation`, `Requires Charge`, `Unsupported Product`, `Low Battery. Replace Device.`, `Low Vehicle Battery`, `Unplugged`, `Low Charging State`, `Vehicle Off`, `Weak GPS Signal`, `Low Gateway Battery`, `Low Gateway Battery (AG24)`, `Low Gateway Battery (AG45)`, `Low Gateway Battery (AG26)`, `Low Gateway Battery (AG46)`, `Low Gateway Battery (AG46-P)`, `Temporarily Offline`, `Prolonged Offline`, `Recently Offline`, `Replacement Required`, `Status Unknown`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lastConnected**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The last time the gateway was connected in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). |
| **&nbsp;&nbsp;&nbsp;&nbsp;dataUsageLast30Days**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | An object containing information about the gateway data usage in mb for the last 30 days. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cellularDataUsageBytes**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Celluar data usage in bytes. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hotspotUsageBytes**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Wifi hotspot data usage in bytes. |
| **&nbsp;&nbsp;&nbsp;&nbsp;model**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The model of the gateway installed on the asset. Valid values: `AG15`, `AG24`, `AG24EU`, `AG26`, `AG26EU`, `AG41`, `AG41EU`, `AG45`, `AG45EU`, `AG46`, `AG46EU`, `AG46P`, `IG15`, `IG21`, `IG41`, `IG61`, `SG1`, `VG32`, `VG33`, `VG34`, `VG34EU`, `VG34FN`, `VG54EU`, `VG54NA`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;serial**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The serial number of the gateway installed on the asset. |
