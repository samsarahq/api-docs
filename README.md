# Samsara REST API: Open API and Examples

This repo hosts [Samsara](https://www.samsara.com/)'s [Open API spec](https://swagger.io/specification/v2/) and examples.

Please visit [developers.samsara.com](https://developers.samsara.com/) for in-depth documentation.

## Open API Spec

We use [swagger](https://swagger.io/specification/v2/) (also known as Open API) to document our REST APIs. There are two swagger files in this repo:

- `swagger.json`
- `swagger-legacy.json`

Samsara is currently in the process of releasing a new generation of our APIs. You can read more about the new generation [here](https://developers.samsara.com/docs/introducing-our-next-generation-api), but suffice to say that the new generation contains many improvements to the first one.

`swagger.json` should be your go-to reference for Samsara's Open APIs. It contains the most recently released APIs, as well as any legacy APIs necessary to maintain feature parity. You can find the reference documentation [here](https://www.samsara.com/api).

`swagger-legacy.json` is the Open API spec containing all of our legacy APIs, and should only be used if you need to use a legacy API for an old implementation. You can find the reference documentation for this set of APIs [here](https://www.samsara.com/api-legacy).

## Examples

The examples we provide come in the form of a [Postman](https://www.getpostman.com/product/api-client) collection. [Postman](https://www.getpostman.com/product/api-client) is an easy to use desktop app that allows you to test REST APIs.

Find out how to get started with this Postman collection at [developers.samsara.com](https://developers.samsara.com/docs/getting-started)
