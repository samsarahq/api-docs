# Swagger

We use [Swagger](http://swagger.io/) to generate the Samsara API documentation and client SDKs -- samsara-python and samsara-js.

This repository holds the for the current Samsara REST API, which must be updated whenever the user-facing API is changed.

## Updating the documentation

1. Update `swagger.json` with your changes.
2. Validate your changes with the [online Swagger editor](http://editor.swagger.io/):
 - Go to http://editor.swagger.io/
 - In the top-left navigation menu, open "File -> Past JSON"
 - Paste the complete file contents of the `swagger.json` file (including your changes)
 - The tool will validate the file contents and give you feedback.
3. Commit your changes. Documentation changes are automatically deployed upon committing.
