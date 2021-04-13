# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object array_ | Activated gateways |
| **&nbsp;&nbsp;&nbsp;&nbsp;asset**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | An objecting containing information about the asset the gateway is installed on |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;externalIds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | A map of external ids |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The unique Samsara ID of the asset where the gateway is installed. This is automatically generated when the asset is created and cannot be changed. Use this ID on PATCH vehicle, equipment, or trailer endpoints to update the asset |
| **&nbsp;&nbsp;&nbsp;&nbsp;model**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The model of the gateway installed on the asset. Valid values: `none`, `AG45`, `AG41`, `AG46EU`, `IG41`, `VG34`, `IG15`, `EM22`, `PM7`, `VG54NA`, `OEMP`, `ACCCRGO`, `EM01`, `Baxter`, `IGMAO`, `EKM`, `DM1`, `VG54EU`, `IG11`, `CM12`, `AG41EU`, `IM32`, `AG46P`, `EM12`, `EM21`, `CM31`, `AG46`, `IG61`, `OEMV`, `Trailer`, `IM31`, `VG33`, `AG24`, `HM21`, `EM23`, `VG34EU`, `AG26EU`, `IG20`, `HM11`, `NVR10`, `VG34FN`, `IG21`, `IGMAI`, `AG15`, `OEM`, `AG26`, `SG1`, `VS25C`, `PM20`, `ACCBDH`, `AG24EU`, `CMVR`, `ACCHMI10`, `OEMR`, `VG32`, `PM10`, `VS2C`, `EM02`, `EM11`, `IM33`, `ACCDM11`, `CM52`, `CM11`, `GW22`, `VS25`, `CM22`, `CM32`, `PM8`, `WM11`, `AG45EU`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;serial**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The serial number of the gateway installed on the asset. |
| **pagination**<br/>_object_ | Pagination parameters. |
| **&nbsp;&nbsp;&nbsp;&nbsp;endCursor**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Cursor identifier representing the last element in the response. This value should be used in conjunction with a subsequent request's 'after' query parameter. This may be an empty string if there are no more pages left to view. |
| **&nbsp;&nbsp;&nbsp;&nbsp;hasNextPage**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | True if there are more pages of results immediately available after this endCursor. |
