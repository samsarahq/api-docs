# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| ****<br/>_object array_ |  |
| **actual_end_ms**<br/>_integer_ | The time in Unix epoch milliseconds that the route actually ended. |
| **actual_start_ms**<br/>_integer_ | The time in Unix epoch milliseconds that the route actually started. |
| **complete_last_stop_on_arrival**<br/>_boolean_ | When set to true (default), this causes the Route to complete on arrival at the final stop. When set to false, the last stop will capture arrival and departure separately as with other stops. |
| **dispatch_jobs**<br/>_object array_ | The dispatch jobs associated with this route. |
| **&nbsp;&nbsp;&nbsp;&nbsp;arrived_at_ms**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The time at which the driver arrived at the job destination. |
| **&nbsp;&nbsp;&nbsp;&nbsp;completed_at_ms**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The time at which the job was marked complete (e.g. started driving to the next destination). |
| **&nbsp;&nbsp;&nbsp;&nbsp;destination_address**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The address of the job destination, as it would be recognized if provided to maps.google.com. Optional if a valid destination address ID is provided. |
| **&nbsp;&nbsp;&nbsp;&nbsp;destination_address_id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | ID of the job destination associated with an address book entry. Optional if valid values are provided for destination address and latitude/longitude. If a valid destination address ID is provided, address/latitude/longitude will be used from the address book entry. Name of the address book entry will only be used if the destination name is not provided. |
| **&nbsp;&nbsp;&nbsp;&nbsp;destination_lat**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;number_ | Latitude of the destination in decimal degrees. Optional if a valid destination address ID is provided. |
| **&nbsp;&nbsp;&nbsp;&nbsp;destination_lng**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;number_ | Longitude of the destination in decimal degrees. Optional if a valid destination address ID is provided. |
| **&nbsp;&nbsp;&nbsp;&nbsp;destination_name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The name of the job destination. If provided, it will take precedence over the name of the address book entry. |
| **&nbsp;&nbsp;&nbsp;&nbsp;dispatch_route_id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | ID of the route that this job belongs to. |
| **&nbsp;&nbsp;&nbsp;&nbsp;documents**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | Document submissions associated with this job. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;driverId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | ID of driver that submitted the document. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of document. This can be used to query for the document's info via the /v1/fleet/drivers/{driver_id}/documents/{document_id} endpoint |
| **&nbsp;&nbsp;&nbsp;&nbsp;driver_id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | ID of the driver assigned to the dispatch job. |
| **&nbsp;&nbsp;&nbsp;&nbsp;en_route_at_ms**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The time at which the assigned driver started fulfilling the job (e.g. started driving to the destination). |
| **&nbsp;&nbsp;&nbsp;&nbsp;external_ids**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object. |
| **&nbsp;&nbsp;&nbsp;&nbsp;fleet_viewer_url**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Fleet viewer url of the dispatch job. |
| **&nbsp;&nbsp;&nbsp;&nbsp;group_id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Deprecated. |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | ID of the Samsara dispatch job. |
| **&nbsp;&nbsp;&nbsp;&nbsp;job_state**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The state of the dispatch job. |
| **&nbsp;&nbsp;&nbsp;&nbsp;notes**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Notes regarding the details of this job, maximum of 2000 characters; newline characters ('\n')can be used for formatting. |
| **&nbsp;&nbsp;&nbsp;&nbsp;scheduled_arrival_time_ms**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The time at which the assigned driver is scheduled to arrive at the job destination. |
| **&nbsp;&nbsp;&nbsp;&nbsp;scheduled_departure_time_ms**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The time at which the assigned driver is scheduled to depart from the job destination. |
| **&nbsp;&nbsp;&nbsp;&nbsp;skipped_at_ms**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The time at which the job was marked skipped. |
| **&nbsp;&nbsp;&nbsp;&nbsp;vehicle_id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | ID of the vehicle used for the dispatch job. |
| **driver_id**<br/>_integer_ | ID of the driver assigned to the dispatch route. Note that driver_id and vehicle_id are mutually exclusive. If neither is specified, then the route is unassigned. |
| **externalIds**<br/>_object_ | The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object. |
| **group_id**<br/>_integer_ | Deprecated. |
| **id**<br/>_integer_ | ID of the Samsara dispatch route. |
| **name**<br/>_string_ | Descriptive name of this route. |
| **notes**<br/>_string_ | Notes regarding the details of this route; maximum of 2000 characters; newline characters ('\n')can be used for formatting. |
| **odometer_end_meters**<br/>_integer_ | Odometer reading at the end of the route. Will not be returned if Route is not completed or if Odometer information is not available for the relevant vehicle. |
| **odometer_start_meters**<br/>_integer_ | Odometer reading at the start of the route. Will not be returned if Route has not started or if Odometer information is not available for the relevant vehicle. |
| **scheduled_end_ms**<br/>_integer_ | The time in Unix epoch milliseconds that the last job in the route is scheduled to end. |
| **scheduled_meters**<br/>_integer_ | The distance expected to be traveled for this route in meters. |
| **scheduled_start_ms**<br/>_integer_ | The time in Unix epoch milliseconds that the route is scheduled to start. |
| **start_location_address**<br/>_string_ | The address of the route's starting location, as it would be recognized if provided to maps.google.com. Optional if a valid start location address ID is provided. |
| **start_location_address_id**<br/>_integer_ | ID of the start location associated with an address book entry. Optional if valid values are provided for start location address and latitude/longitude. If a valid start location address ID is provided, address/latitude/longitude will be used from the address book entry. Name of the address book entry will only be used if the start location name is not provided. |
| **start_location_lat**<br/>_number_ | Latitude of the start location in decimal degrees. Optional if a valid start location address ID is provided. |
| **start_location_lng**<br/>_number_ | Longitude of the start location in decimal degrees. Optional if a valid start location address ID is provided. |
| **start_location_name**<br/>_string_ | The name of the route's starting location. If provided, it will take precedence over the name of the address book entry. |
| **trailer_id**<br/>_integer_ | ID of the trailer assigned to the dispatch route. Note that trailers can only be assigned to routes that have a Vehicle or Driver assigned to them. |
| **vehicle_id**<br/>_integer_ | ID of the vehicle assigned to the dispatch route. Note that vehicle_id and driver_id are mutually exclusive. If neither is specified, then the route is unassigned. |
