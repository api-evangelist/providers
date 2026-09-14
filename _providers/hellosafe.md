---
api_count: 2
apis:
- baseURL: https://atlas.hellosafe.com/api/v1/travel
  baseurl_source: declared
  description: Server-to-server conversion postback.
  name: HelloSafe Conversion API
  slug: hellosafe-conversion-api
- baseURL: https://atlas.hellosafe.com/api/v1/travel
  baseurl_source: declared
  description: Turn a chosen offer into a tracked, attributed subscription link.
  name: HelloSafe Links API
  slug: hellosafe-links-api
- baseURL: https://atlas.hellosafe.com/api/v1/travel
  baseurl_source: declared
  description: Price a trip and read the catalogue vocabulary.
  name: HelloSafe Quotes API
  slug: hellosafe-quotes-api
- description: REST API for travel-insurance reference data, quoting, tracked link minting, and signed conversion postbacks. The conversion postback and tracked deep links are live today; quote-and-bind travel endpo
  name: HelloSafe Travel Insurance API
  slug: hellosafe-travel-insurance-api
artifact_total: 4
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/hellosafe-capability-edges.yml
- group: other
  title: ''
  type: APIsJSON
  url: well-known/hellosafe-provider-apis.json
- group: start
  title: ''
  type: Onboarding
  url: well-known/hellosafe-api-onboarding.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hellosafe-llms.txt
- group: company
  title: ''
  type: Website
  url: https://hellosafe.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://atlas.hellosafe.com/platform/api
created: '2026-08-25'
description: HelloSafe distributes travel insurance through APIs, under the Atlas platform at atlas.hellosafe.com. The Travel Insurance API returns multi-insurer pricing, tracked attributed links and a pre-sale coverage assessment, aimed at travel agencies, tour operators, OTAs, booking engines and travel apps. A second surface, the Coach API, sits alongside it. The contract is an OpenAPI 3.1 document of 4 operations and 8 schemas, and requests are HMAC-SIGNED rather than bearing a plain API key — three headers, AtlasKeyId, AtlasTimestamp and AtlasSignature, which is materially stronger than what most providers this size ship.
layout: provider
modified: '2026-08-25'
name: HelloSafe
nav: Providers
network: true
overview: HelloSafe publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Conversion API, Links API, Quotes API, and 1 more. Tagged areas include Travel Insurance, Insurance Distribution, Pricing, and Travel.
random_paper: 2
screenshot: https://raw.githubusercontent.com/api-evangelist/hellosafe/refs/heads/main/screenshots/hellosafe-2026-09-02T145720.png
slug: hellosafe
tags:
- Travel Insurance
- Insurance Distribution
- Pricing
- Travel
website: https://hellosafe.com
---
