# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object_ | The configuration settings for the Samsara Driver App. Can be set or updated through the Samsara Settings page or the API at any time. |
| **&nbsp;&nbsp;&nbsp;&nbsp;driverFleetId**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Login user name for the fleet driver app |
| **&nbsp;&nbsp;&nbsp;&nbsp;gamification**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Driver gamification feature. Enabling this will turn on the feature for all drivers using the mobile app. Drivers can be configured into peer groups within the Drivers Page. Unconfigured drivers will be grouped on an organization level. |
| **&nbsp;&nbsp;&nbsp;&nbsp;gamificationConfig**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | Gamification configuration for the Driver App. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;anonymizeDriverNames**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Hide the names of other drivers when viewing the driver leaderboard in the mobile app. |
| **&nbsp;&nbsp;&nbsp;&nbsp;orgVehicleSearch**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Allow drivers to search for vehicles outside of their selection tag when connected to the internet. |
| **&nbsp;&nbsp;&nbsp;&nbsp;trailerSelection**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Allow drivers to see and select trailers in the Samsara Driver app.  |
| **&nbsp;&nbsp;&nbsp;&nbsp;trailerSelectionConfig**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | Trailer selection setting configuration for the Driver App. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;driverTrailerCreationEnabled**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Allow drivers to create new trailers in the Samsara Driver app. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maxNumOfTrailersSelected**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Trailer selection limit. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;orgTrailerSearch**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Allow drivers to search for trailers outside of their selection tag when connected to the internet |
