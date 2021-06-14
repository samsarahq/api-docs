# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object array_ | List of trailer objects. |
| **&nbsp;&nbsp;&nbsp;&nbsp;enabledForMobile**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Indicates if the trailer is visible on the Samsara mobile apps. |
| **&nbsp;&nbsp;&nbsp;&nbsp;externalIds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | A map of external ids |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The unique Samsara ID of the Trailer. This is automatically generated when the Trailer object is created. It cannot be changed. |
| **&nbsp;&nbsp;&nbsp;&nbsp;installedGateway**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | A minified gateway object. This field will be omitted if the trailer does not have a gateway installed. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;model**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The model of the gateway installed on the asset. Valid values: `AG15`, `AG24`, `AG24EU`, `AG26`, `AG26EU`, `AG41`, `AG41EU`, `AG45`, `AG45EU`, `AG46`, `AG46EU`, `AG46P`, `IG15`, `IG21`, `IG41`, `IG61`, `SG1`, `VG32`, `VG33`, `VG34`, `VG34EU`, `VG34FN`, `VG54EU`, `VG54NA`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The serial number of the gateway installed on the asset. |
| **&nbsp;&nbsp;&nbsp;&nbsp;licensePlate**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The license plate of the Trailer. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time. |
| **&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The human-readable name of the Trailer. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time. |
| **&nbsp;&nbsp;&nbsp;&nbsp;notes**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | These are generic notes about the Trailer. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time. |
| **&nbsp;&nbsp;&nbsp;&nbsp;tags**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | The list of [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting) associated with the Trailer. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the tag |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the tag. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parentTagId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | If this tag is part a hierarchical tag tree, this is the ID of the parent tag, otherwise this will be omitted. |
| **&nbsp;&nbsp;&nbsp;&nbsp;trailerSerialNumber**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The serial number of the trailer. |
| **pagination**<br/>_object_ | Pagination parameters. |
| **&nbsp;&nbsp;&nbsp;&nbsp;endCursor**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Cursor identifier representing the last element in the response. This value should be used in conjunction with a subsequent request's 'after' query parameter. This may be an empty string if there are no more pages left to view. |
| **&nbsp;&nbsp;&nbsp;&nbsp;hasNextPage**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | True if there are more pages of results immediately available after this endCursor. |
