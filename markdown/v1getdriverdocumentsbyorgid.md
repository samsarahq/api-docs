# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **driverDocuments**<br/>_object array_ | List of documents. |
| **&nbsp;&nbsp;&nbsp;&nbsp;conditionalFieldSections**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;array_ | An array of objects that describe a set of fields conditionally shown by a multiple choice value. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;conditionalFieldIndexFirst**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | Start index of the conditional fields set |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;conditionalFieldIndexLast**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | End index of the conditional fields set |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;triggeringFieldIndex**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | Index of the multiple choice field that triggers the conditional fields |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;triggeringFieldValue**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Multiple choice value that triggers the conditional fields |
| **&nbsp;&nbsp;&nbsp;&nbsp;dispatchJobId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | ID of the Samsara dispatch job for which the document is submitted. |
| **&nbsp;&nbsp;&nbsp;&nbsp;documentType**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the document type. |
| **&nbsp;&nbsp;&nbsp;&nbsp;driverCreatedAtMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The time in Unix epoch milliseconds that the document was created in the driver app. |
| **&nbsp;&nbsp;&nbsp;&nbsp;driverId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | ID of the driver for whom the document is submitted. |
| **&nbsp;&nbsp;&nbsp;&nbsp;fields**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;array_ | An array of field objects associated with a document. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;barcodeValue**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object array_ | The value of a barcode scanning field. Only present for barcode scanning fields |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;barcodeType**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The barcode type that was scanned |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;barcodeValue**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The captured barcode value |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dateTimeValue**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | The value of a date time field. Only present for date time fields. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dateTimeMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | Date time value in milliseconds. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The name of a field. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multipleChoiceValue**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object array_ | The value of a multiple choice field. Only present for multiple choice fields. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;selected**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Boolean representing if the choice has been selected. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Description of the choice. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;numberValue**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | The value of a number field. Only present for number fields. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;photoValue**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object array_ | The value of a photo or document scanning field. Only present for photo or document scanning fields. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Url of the photo. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uuid**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Uuid of the photo. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;signatureValue**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | The value of a signature field. Only present for signature fields. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the signee for a signature field |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;signedAtMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | Date time value in milliseconds of the time a signature was captured. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Url of a signature field's PNG signature image. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uuid**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Uuid of a signature field |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stringValue**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The value of a string field. Only present for string fields. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;valueType**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The value type of a field. |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the document. |
| **&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Custom name of the document. If no custom name is given to the document, the admin dashboard and driver app will display the template name as the default document name. |
| **&nbsp;&nbsp;&nbsp;&nbsp;notes**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Notes submitted with this document. |
| **&nbsp;&nbsp;&nbsp;&nbsp;orgId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Organization ID that the document belongs to. |
| **&nbsp;&nbsp;&nbsp;&nbsp;serverCreatedAtMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The time in Unix epoch milliseconds that the document was received by the server. |
| **&nbsp;&nbsp;&nbsp;&nbsp;serverUpdatedAtMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The time in Unix epoch milliseconds that the document was updated on the server. |
| **&nbsp;&nbsp;&nbsp;&nbsp;state**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The condition of the document created for the driver. Can be either `Required` or `Submitted`. If no value is specified, `state` defaults to `Required`. `Required` documents are pre-populated documents for the Driver to fill out in the Driver App and have not yet been submitted. `Submitted` documents have been submitted by the driver in the Driver App. `Archived` documents have been archived by the admin in the cloud dashboard. |
| **&nbsp;&nbsp;&nbsp;&nbsp;vehicleId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | ID of the vehicle the driver was signed into when the document was submitted. Will be `null` if the document `state` is `Required`. |
