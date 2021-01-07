# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **visionRuns**<br/>_object array_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;deviceId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;endedAtMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;programId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;reportMetadata**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | The response includes 4 additional fields that are now deprecated |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;itemsPerMinute**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | Returns average scanned items per minute. Should be used instead of scanRate. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;noReadCount**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Returns no read count for the run. Should be used instead of noReadScansCount |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rejectCount**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Returns reject count for the run. Should be used instead of failedScansCount |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;successCount**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Returns success count for the run. Should be used instead of successfulScansCount |
| **&nbsp;&nbsp;&nbsp;&nbsp;startedAtMs**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ |  |
