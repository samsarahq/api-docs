# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;attributes**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | List of attributes associated with the entity |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Id of the attribute |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the attribute |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;numberValues**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number array_ | List of number values associated with the attribute |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stringValues**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string array_ | List of string values associated with the attribute. |
| **&nbsp;&nbsp;&nbsp;&nbsp;enabledForMobile**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Indicates if the trailer is visible on the Samsara mobile apps. |
| **&nbsp;&nbsp;&nbsp;&nbsp;externalIds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | A map of external ids |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The unique Samsara ID of the Trailer. This is automatically generated when the Trailer object is created. It cannot be changed. |
| **&nbsp;&nbsp;&nbsp;&nbsp;installedGateway**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | A minified gateway object. This field will be omitted if the trailer does not have a gateway installed. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;model**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The model of the gateway installed on the asset. Valid values: `none`, `AG45`, `AG41`, `AG46EU`, `IG41`, `VG34`, `IG15`, `EM22`, `PM7`, `VG54NA`, `OEMP`, `ACCCRGO`, `EM01`, `Baxter`, `IGMAO`, `EKM`, `DM1`, `VG54EU`, `IG11`, `CM12`, `AG41EU`, `IM32`, `AG46P`, `EM12`, `EM21`, `CM31`, `AG46`, `IG61`, `OEMV`, `Trailer`, `IM31`, `VG33`, `AG24`, `HM21`, `EM23`, `VG34EU`, `AG26EU`, `IG20`, `HM11`, `NVR10`, `VG34FN`, `IG21`, `IGMAI`, `AG15`, `OEM`, `AG26`, `SG1`, `VS25C`, `PM20`, `ACCBDH`, `AG24EU`, `CMVR`, `ACCHMI10`, `OEMR`, `VG32`, `PM10`, `VS2C`, `EM02`, `EM11`, `IM33`, `ACCDM11`, `CM52`, `CM11`, `GW22`, `VS25`, `CM22`, `CM32`, `PM8`, `WM11`, `AG45EU`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The serial number of the gateway installed on the asset. |
| **&nbsp;&nbsp;&nbsp;&nbsp;licensePlate**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The license plate of the Trailer. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time. |
| **&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The human-readable name of the Trailer. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time. |
| **&nbsp;&nbsp;&nbsp;&nbsp;notes**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | These are generic notes about the Trailer. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time. |
| **&nbsp;&nbsp;&nbsp;&nbsp;tags**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | The list of [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting) associated with the Trailer. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the tag |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the tag. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parentTagId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | If this tag is part a hierarchical tag tree, this is the ID of the parent tag, otherwise this will be omitted. |
| **&nbsp;&nbsp;&nbsp;&nbsp;trailerSerialNumber**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The serial number of the trailer. |
