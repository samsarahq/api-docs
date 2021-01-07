# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;completedAtTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Time that PDF generation was completed, in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;documentId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the document. |
| **&nbsp;&nbsp;&nbsp;&nbsp;downloadDocumentPdfUrl**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | S3 pre-signed URL to download PDF file. |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the PDF file generated or being generated for the document |
| **&nbsp;&nbsp;&nbsp;&nbsp;jobStatus**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Describes status of the PDF generation job. |
| **&nbsp;&nbsp;&nbsp;&nbsp;requestedAtTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Time that PDF generation was requested, in RFC 3339 format. |
