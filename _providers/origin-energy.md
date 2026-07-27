---
access_model:
  confidence: high
  generated: '2026-07-27'
  label: Gated · CDR accreditation or Origin partner/customer account required
  method: probed
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - cdr-register
  - well-known
  - documentation
  trial: false
  try_now: false
api_count: 7
artifact_total: 0
created: '2026-07-27'
description: 'Origin Energy Limited is Australia''s largest energy retailer, an ASX-listed integrated gas and electricity company headquartered in Sydney that supplies roughly 4.5 million electricity, natural gas, LPG and broadband customer accounts, operates the Eraring Power Station and a large gas-fired and renewable generation portfolio, holds a stake in the Australia Pacific LNG project, and runs the Origin Loop virtual power plant. It sits at the retail end of the National Electricity Market value chain, buying and generating wholesale energy and selling it to households and businesses. Its API posture is defined almost entirely by regulation rather than by a developer strategy: Origin is a designated energy data holder under Australia''s Consumer Data Right and that obligation is genuinely implemented — it appears on the CDR Register with its own public base URI, serves the Consumer Data Standards discovery endpoints anonymously, and presents an mTLS resource endpoint whose TLS certificate
  is issued by the ACCC''s own CDR Certificate Authority — but every byte of actual customer usage, billing and DER data behind that surface is reachable only by an accredited data recipient acting on a consumer''s consent. Alongside the mandate, Origin runs its retail business on Octopus Energy''s Kraken platform (Origin holds an equity stake in Octopus and Kraken Technologies), which exposes a publicly readable partner developer portal with downloadable OpenAPI definitions, a GraphQL API, an external events catalogue and an OpenID Connect authorisation server — none of it self-serve. Origin publishes no open grid, market or system data of its own; the only anonymously retrievable data is its retail plan reference data, and that is served from the Australian Energy Regulator''s Energy Made Easy CDR gateway, not from an Origin host.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/origin-energy.png
layout: provider
modified: '2026-07-27'
name: Origin Energy
nav: Providers
network: true
random_paper: 51
slug: origin-energy
tags:
- Energy
- Australia
- Utilities
- Electricity
- Gas
- Energy Retail
- Consumer Data Right
- Smart Metering
- Solar
- DER
- Demand Response
- Energy Markets
---
