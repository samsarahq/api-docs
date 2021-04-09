# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object array_ | List of responses for each data output from the original request. |
| **&nbsp;&nbsp;&nbsp;&nbsp;errorMessage**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | If the request failed, this displays the error message. |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The data output ID. |
| **&nbsp;&nbsp;&nbsp;&nbsp;statusCode**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The status code of the request. 200 indicates the request succeeded for this data output. 500 indicates an internal server error. |
