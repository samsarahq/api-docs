# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object array_ | List of trailers and their stats |
| **&nbsp;&nbsp;&nbsp;&nbsp;carrierReeferState**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of engine state points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The overall state of the multizone carrier reefer. |
| **&nbsp;&nbsp;&nbsp;&nbsp;gps**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of GPS points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;headingDegrees**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Heading of the trailer in degrees. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;latitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | GPS latitude represented in degrees. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;longitude**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | GPS longitude represented in degrees. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reverseGeo**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Reverse geocoded information |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;formattedLocation**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Formatted address of the reverse geocoding data. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speedMilesPerHour**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | GPS speed of the trailer in miles per hour. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;gpsOdometerMeters**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of odometer points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Number of meters the trailer has traveled according to the GPS calculations and the manually specified odometer reading. |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the trailer. |
| **&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the vehicle. |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferAlarms**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of reefer alarm points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alarms**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object array_ | The alarms reported by the reefer. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alarmCode**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The ID of the alarm. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The description of the alarm. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;operatorAction**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The recommended operator action. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;severity**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The severity of the alarm. `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferAmbientAirTemperatureMilliC**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of ambient air temperature points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The ambient air temperature reading of the reefer in millidegree Celsius. |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferFuelPercent**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of fuel percent points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The fuel level in percentage points (e.g. `99`, `50`, etc). |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferObdEngineSeconds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of engine second points |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The number of seconds the reefer has been on according to the onboard diagnostics. |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferReturnAirTemperatureMilliCZone1**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of return air temperature points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The return air temperature reading in millidegree Celsius. |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferReturnAirTemperatureMilliCZone2**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of return air temperature points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The return air temperature reading in millidegree Celsius. |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferReturnAirTemperatureMilliCZone3**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of return air temperature points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The return air temperature reading in millidegree Celsius. |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferRunMode**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of run mode points |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The operational mode of the reefer. |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferSetPointTemperatureMilliCZone1**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of set point temperature points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The set point temperature reading in millidegree Celsius. |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferSetPointTemperatureMilliCZone2**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of set point temperature points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The set point temperature reading in millidegree Celsius. |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferSetPointTemperatureMilliCZone3**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of set point temperature points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The set point temperature reading in millidegree Celsius. |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferStateZone1**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of engine state points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The state zone 1 of the reefer. |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferStateZone2**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of engine state points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The state zone 2 of the reefer. |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferStateZone3**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of engine state points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The state zone 3 of the reefer. |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferSupplyAirTemperatureMilliCZone1**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of supply air temperature points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The supply or discharge air temperature reading in millidegree Celsius. |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferSupplyAirTemperatureMilliCZone2**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of supply air temperature points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The supply or discharge air temperature reading in millidegree Celsius. |
| **&nbsp;&nbsp;&nbsp;&nbsp;reeferSupplyAirTemperatureMilliCZone3**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | A list of supply air temperature points. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decorations**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object_ | Decorated values for the primary trailer stat datapoints. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | UTC timestamp in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The supply or discharge air temperature reading in millidegree Celsius. |
| **pagination**<br/>_object_ | Pagination parameters. |
| **&nbsp;&nbsp;&nbsp;&nbsp;endCursor**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Cursor identifier representing the last element in the response. This value should be used in conjunction with a subsequent request's 'after' query parameter. This may be an empty string if there are no more pages left to view. |
| **&nbsp;&nbsp;&nbsp;&nbsp;hasNextPage**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | True if there are more pages of results immediately available after this endCursor. |
