# Samsara REST API: Open API and Examples

This repo hosts [Samsara](https://www.samsara.com/)'s [Open API spec](https://swagger.io/specification/v2/) and examples.

Please visit [developers.samsara.com](https://developers.samsara.com/) for in-depth documentation.

## Open API Spec

We use [swagger](https://swagger.io/specification/v2/) (also known as Open API) to document our REST APIs. There are two swagger files in this repo:

- `swagger.json`
- `swagger-preview.json`

Samsara is currently in the process of releasing a new generation of our APIs. You can read more about the new generation [here](https://developers.samsara.com/docs/introducing-our-next-generation-api), but suffice to say that the new generation contains may improvements to the first one.

`swagger.json` is the Open API spec of the first generation of our APIs. You should only use this if you need to reference legacy APIs. You can find the reference documentation [here](https://www.samsara.com/api).

`swagger-preview.json` is the Open API spec containing all our new APIs and any legacy APIs that don't have a new equivalent available yet. We'll be releasing new APIs to this spec on a rolling basis. You can find the reference documentation for this set of APIs [here](https://www.samsara.com/api-preview).

We recommend that primarily utilize `swagger-preview.json` as we are encouraging all users to use the new API endpoints when available. These endpoints are faster and easier to use. `swagger-preview.json` is what we use to generate the examples below.

*Note: You can use old and new API endpoints side-by-side as we continue to bring the new generation up to feature parity. `swagger-preview.json` currently includes both. Read more [here](https://developers.samsara.com/docs/introducing-our-next-generation-api).*

## Examples

The examples we provide come in the form of a [Postman](https://www.getpostman.com/product/api-client) collection. [Postman](https://www.getpostman.com/product/api-client) is an easy to use desktop app that allows you to test REST APIs.

Find out how to get started with this Postman collection at [developers.samsara.com](https://developers.samsara.com/docs/getting-started)
