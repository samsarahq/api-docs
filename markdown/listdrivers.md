# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object array_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;attributes**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | [beta] A minified attribute |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The samsara id of the attribute object. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of attribute. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;numberValues**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number array_ | Number values that are associated with this attribute. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stringValues**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string array_ | String values that are associated with this attribute. |
| **&nbsp;&nbsp;&nbsp;&nbsp;carrierSettings**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | Carrier for a given driver. If the driver's carrier differs from the general organization's carrier settings, the override value is used. Updating this value only updates the override setting for this driver. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;carrierName**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Carrier for a given driver. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dotNumber**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Carrier US DOT Number. If this differs from the general organization's settings, the override value is used. Updating this value only updates the override setting for this driver. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mainOfficeAddress**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Main office address for a given driver. If this differs from the general organization's settings, the override value is used.  |
| **&nbsp;&nbsp;&nbsp;&nbsp;createdAtTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The date and time this driver was created in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;currentIdCardCode**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The ID Card Code on the back of the physical card assigned to the driver.  Contact Samsara if you would like to enable this feature. |
| **&nbsp;&nbsp;&nbsp;&nbsp;driverActivationStatus**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | A value indicating whether the driver is active or deactivated. Valid values: `active`, `deactivated`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;eldAdverseWeatherExemptionEnabled**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Flag indicating this driver may use Adverse Weather exemptions in ELD logs. |
| **&nbsp;&nbsp;&nbsp;&nbsp;eldBigDayExemptionEnabled**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Flag indicating this driver may use Big Day exemption in ELD logs. |
| **&nbsp;&nbsp;&nbsp;&nbsp;eldDayStartHour**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate noon-to-noon driving hours. |
| **&nbsp;&nbsp;&nbsp;&nbsp;eldExempt**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Flag indicating this driver is exempt from the Electronic Logging Mandate. |
| **&nbsp;&nbsp;&nbsp;&nbsp;eldExemptReason**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt). |
| **&nbsp;&nbsp;&nbsp;&nbsp;eldPcEnabled**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Flag indicating this driver may select the Personal Conveyance duty status in ELD logs. |
| **&nbsp;&nbsp;&nbsp;&nbsp;eldSettings**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | The driver's ELD settings. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rulesets**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array_ | The driver's ELD rulesets and overrides. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;break**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The rest break required setting of the ELD ruleset applied to this driver. Valid values: `Property (off-duty/sleeper)`, `Explosives/HazMat (on-duty)`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cycle**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The cycle of the ELD ruleset applied to this driver. Valid values: `USA 60 hour / 7 day`, `USA 70 hour / 8 day`, `AK 80 hour / 8 day`, `AK 70 hour / 7 day`, `CA 80 hour / 8 day`, `CA 112 hour / 8 day`, `FL 80 hour / 8 day`, `FL 70 hour / 7 day`, `NE 80 hour / 8 day`, `NE 70 hour / 7 day`, `NC 80 hour / 8 day`, `NC 70 hour / 7 day`, `OK 70 hour / 8 day`, `OK 60 hour / 7 day`, `OR 80 hour / 8 day`, `OR 70 hour / 7 day`, `SC 80 hour / 8 day`, `SC 70 hour / 7 day`, `TX 70 hour / 7 day`, `WI 80 hour / 8 day`, `WI 70 hour / 7 day`, `Canada South Cycle 1 (70 hour / 7 day)`, `Canada South Cycle 2 (120 hour / 14 day)`, `Canada North Cycle 1 (80 hour / 7 day)`, `Canada North Cycle 2 (120 hour / 14 day)`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;jurisdiction**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The jurisdiction of the ELD ruleset applied to this driver. These are specified by either `CS` or `CN` for Canada South and Canada North, respectively, or the ISO 3166-2 postal code for the supported state or territory. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;restart**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The restart of the ELD ruleset applied to this driver. Valid values: `34-hour Restart`, `24-hour Restart`, `36-hour Restart`, `72-hour Restart`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shift**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | The shift of the ELD ruleset applied to this driver. Valid values: `US Interstate Property`, `US Interstate Passenger`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;eldYmEnabled**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Flag indicating this driver may select the Yard Move duty status in ELD logs. |
| **&nbsp;&nbsp;&nbsp;&nbsp;externalIds**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object. |
| **&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Samsara ID for the driver. |
| **&nbsp;&nbsp;&nbsp;&nbsp;isDeactivated**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | [DEPRECATED] A boolean indicating whether or not the driver is deactivated. Use `driverActivationStatus` instead. |
| **&nbsp;&nbsp;&nbsp;&nbsp;licenseNumber**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Driver's state issued license number. The combination of this number and `licenseState` must be unique. |
| **&nbsp;&nbsp;&nbsp;&nbsp;licenseState**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Abbreviation of US state, Canadian province, or US territory that issued driver's license. |
| **&nbsp;&nbsp;&nbsp;&nbsp;locale**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Locale override (uncommon). These are specified by ISO 3166-2 country codes for supported locales. Valid values: `us`, `at`, `be`, `ca`, `gb`, `fr`, `de`, `ie`, `it`, `lu`, `mx`, `nl`, `es`, `ch`, `pr`. |
| **&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Driver's name. |
| **&nbsp;&nbsp;&nbsp;&nbsp;notes**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Notes about the driver. |
| **&nbsp;&nbsp;&nbsp;&nbsp;phone**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Phone number of the driver. |
| **&nbsp;&nbsp;&nbsp;&nbsp;staticAssignedVehicle**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | Vehicle assigned to the driver for static vehicle assignments. (uncommon). |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the vehicle. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the vehicle. |
| **&nbsp;&nbsp;&nbsp;&nbsp;tachographCardNumber**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Driver's assigned tachograph card number (Europe specific) |
| **&nbsp;&nbsp;&nbsp;&nbsp;tags**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;array_ | The tags this driver belongs to. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the tag. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the tag. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parentTagId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | If this tag is part a hierarchical tag tree, this is the ID of the parent tag, otherwise this will be omitted. |
| **&nbsp;&nbsp;&nbsp;&nbsp;timezone**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs. Driver timezones use [IANA timezone database](https://www.iana.org/time-zones) keys (e.g. `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find a mapping of common timezone formats to IANA timezone keys [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html). |
| **&nbsp;&nbsp;&nbsp;&nbsp;updatedAtTime**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The date and time this driver was last updated in RFC 3339 format. |
| **&nbsp;&nbsp;&nbsp;&nbsp;username**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Driver's login username into the driver app. The username may not contain spaces or the '@' symbol. The username must be unique. |
| **&nbsp;&nbsp;&nbsp;&nbsp;vehicleGroupTag**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | Tag which determines which vehicles a driver will see when selecting vehicles. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | ID of the tag. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of the tag. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parentTagId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | If this tag is part a hierarchical tag tree, this is the ID of the parent tag, otherwise this will be omitted. |
| **pagination**<br/>_object_ | Pagination parameters. |
| **&nbsp;&nbsp;&nbsp;&nbsp;endCursor**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Cursor identifier representing the last element in the response. This value should be used in conjunction with a subsequent request's 'after' query parameter. This may be an empty string if there are no more pages left to view. |
| **&nbsp;&nbsp;&nbsp;&nbsp;hasNextPage**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | True if there are more pages of results immediately available after this endCursor. |
