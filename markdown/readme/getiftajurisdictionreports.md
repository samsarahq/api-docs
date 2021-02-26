# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| **data**<br/>_object_ | Dictionary containing summarized jurisdiction report data. |
| **&nbsp;&nbsp;&nbsp;&nbsp;jurisdictionReports**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object array_ | List of summarized jurisdiction reports. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;jurisdiction**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Jurisdiction code. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;taxPaidLiters**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | Liters purchased for all qualified vehicles. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;taxableMeters**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | Distance in meters traveled on public roads in an IFTA jurisdiction. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;totalMeters**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | Total meters driven in this jurisdiction, taxable and non-taxable. |
| **&nbsp;&nbsp;&nbsp;&nbsp;month**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The specified month duration for this IFTA report. |
| **&nbsp;&nbsp;&nbsp;&nbsp;quarter**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The specified quarter duration for this IFTA report. |
| **&nbsp;&nbsp;&nbsp;&nbsp;troubleshooting**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | IFTA report troubleshooting information. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;noPurchasesFound**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boolean_ | Whether or not fuel purchases were found for this report. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unassignedFuelTypePurchases**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The number of fuel purchases without a fuel type assigned. Fuel purchases are used to calculate tax paid gallons. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unassignedFuelTypeVehicles**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The number of vehicles without a fuel type assigned. Vehicles without an assigned fuel type may affect total mileage. |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unassignedVehiclePurchases**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer_ | Purchases without an assigned fuel type may affect tax-paid gallons and fleet mpg. |
| **&nbsp;&nbsp;&nbsp;&nbsp;year**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;integer_ | The specified year for this IFTA report. |
