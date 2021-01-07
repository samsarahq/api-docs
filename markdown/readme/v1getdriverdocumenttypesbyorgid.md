# 200 Response Schema
| Property Name | Description |
| :------------ | :---------- |
| ****<br/>_object array_ |  |
| **fieldTypes**<br/>_object array_ | The fields associated with this document type. |
| **&nbsp;&nbsp;&nbsp;&nbsp;label**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | Name of this field type. |
| **&nbsp;&nbsp;&nbsp;&nbsp;multipleChoiceValueTypeMetadata**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | Metadata about the multiple choice field. Only present for value type `ValueType_MultipleChoice` |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multipleChoiceOptionLabels**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;object array_ | Array of the multiple choice option labels for the field |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ |  |
| **&nbsp;&nbsp;&nbsp;&nbsp;numberValueTypeMetadata**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | Metadata about the number field. Only present for value type `ValueType_Number` |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;numDecimalPlaces**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number_ | The number of decimal places allowed for this number field |
| **&nbsp;&nbsp;&nbsp;&nbsp;signatureValueTypeMetadata**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;object_ | Metadata about the signature field. Only present for value type `ValueType_Signature` |
| **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;legalText**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string_ | Legal text displayed alongside signature |
| **&nbsp;&nbsp;&nbsp;&nbsp;valueType**<br/>_&nbsp;&nbsp;&nbsp;&nbsp;string_ | The type of value this field can have.<br/>Valid values: `ValueType_Number`, `ValueType_String`, `ValueType_Photo`, `ValueType_MultipleChoice`, `ValueType_Signature`, `ValueType_DateTime`. |
| **name**<br/>_string_ | Name of the document type. |
| **orgId**<br/>_integer_ | ID for the organization this document belongs to. |
| **uuid**<br/>_string_ | Universally unique identifier for the document type. Can be passed in as the `documentTypeUuid` when creating a document for this document type. |
