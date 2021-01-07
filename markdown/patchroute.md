# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **driver**<br/>_object_ | A minified driver object |
| **&nbsp;&nbsp;&nbsp;&nbsp;externalIds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | A map of external ids |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the driver |
| **&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the driver |
| **externalIds**<br/>_object_ | A map of external ids |
| **id**<br/>_string_ | ID of the route |
| **name**<br/>_string_ | Route name |
| **notes**<br/>_string_ | Notes for the route |
| **scheduledRouteEndTime**<br/>_string_ |  |
| **scheduledRouteStartTime**<br/>_string_ |  |
| **settings**<br/>_object_ | An optional dictionary, only necessary to override the defaults for route start and end conditions. |
| **&nbsp;&nbsp;&nbsp;&nbsp;routeCompletionCondition**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Defaults to 'arriveLastStop' which ends the route upon arriving at the final stop. The condition 'departLastStop' <br/>ends the route upon departing the last stop. If 'arriveLastStop' is set, then the departure time of the final stop should not be set. |
| **&nbsp;&nbsp;&nbsp;&nbsp;routeStartingCondition**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Defaults to 'departFirstStop' which starts the route upon departing the first stop in the route.<br/> The condition 'arriveFirstStop' starts the route upon arriving at the first stop in the route. If 'departFirstStop' is set,<br/>the arrival time of the first stop should not be set. |
| **stops**<br/>_object array_ | List of stops along the route |
| **&nbsp;&nbsp;&nbsp;&nbsp;address**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | A minified Address object |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;externalIds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | A map of external ids |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Id of the address |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the address |
| **&nbsp;&nbsp;&nbsp;&nbsp;externalIds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | A map of external ids |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Id of the stop |
| **&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the stop |
| **&nbsp;&nbsp;&nbsp;&nbsp;notes**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Notes for the stop |
| **&nbsp;&nbsp;&nbsp;&nbsp;scheduledArrivalTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;scheduledDepartureTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;singleUseLocation**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | This field is used to indicate stops along the route for which an address has not been persisted. This field is mutually exclusive with addressId. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Address of the stop. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;latitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | The latitude of the location |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;longitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | The longitude of the location |
| **vehicle**<br/>_object_ | A minified vehicle object |
| **&nbsp;&nbsp;&nbsp;&nbsp;externalIds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | A map of external ids |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the vehicle |
| **&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the vehicle |
