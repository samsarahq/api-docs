# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object array_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;behaviorLabels**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;array_ | The most up-to-date behavior labels associated with the safety event. These labels can be updated by the Safety Report Admin. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The label associated with the safety event. This list often changes, so it is recommended that clients gracefully handle any types not enumerated in this list. Valid values: `genericTailgating`, `genericDistraction`, `defensiveDriving`, `rollingStop`, `nearCollison`, `speeding`, `obstructedCamera`, `didNotYield`, `noSeatbelt`, `mobileUsage`, `drowsy`, `laneDeparture`, `followingDistanceSevere`, `followingDistanceModerate`, `lateResponse`, `acceleration`, `braking`, `harshTurn`, `crash`, `rolloverProtection`, `yawControl`, `ranRedLight`, `forwardCollisionWarning`, `eatingDrinking`, `smoking`, `followingDistance`, `edgeDistractedDriving`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The source of the label associated with the safety event. Valid values: `automated`, `userGenerated`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;coachingState**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The current coaching status of the event. Valid values: `needsReview`, `coached`, `dismissed`, `reviewed`, `archived`, `manualReview`, `needsCoaching`, `autoDismissed`, `needsRecognition`, `recognized`, `invalid`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;downloadForwardVideoUrl**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | URL to download the forward video. |
| **&nbsp;&nbsp;&nbsp;&nbsp;downloadInwardVideoUrl**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | URL to download the inward video. |
| **&nbsp;&nbsp;&nbsp;&nbsp;downloadTrackedInwardVideoUrl**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | URL to download the tracked inward video. |
| **&nbsp;&nbsp;&nbsp;&nbsp;driver**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | A minified driver object. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the driver. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the driver. |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The unique Samsara ID of the safety event. |
| **&nbsp;&nbsp;&nbsp;&nbsp;location**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | Location object |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;latitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | GPS latitude represented in degrees |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;longitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | GPS longitude represented in degrees |
| **&nbsp;&nbsp;&nbsp;&nbsp;maxAccelerationGForce**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;number_ | The maximum acceleration value as a multiplier on the force of gravity (g). |
| **&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The time the safety event occurred in RFC 3339 milliseconds format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;vehicle**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | A minified vehicle object. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the vehicle. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the vehicle. |
| **pagination**<br/>_object_ | Pagination parameters. |
| **&nbsp;&nbsp;&nbsp;&nbsp;endCursor**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Cursor identifier representing the last element in the response. This value should be used in conjunction with a subsequent request's 'after' query parameter. This may be an empty string if there are no more pages left to view. |
| **&nbsp;&nbsp;&nbsp;&nbsp;hasNextPage**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | True if there are more pages of results immediately available after this endCursor. |
