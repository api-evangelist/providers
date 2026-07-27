---
access_model:
  confidence: high
  generated: '2026-07-27'
  label: Free · Anonymous, no registration, no documentation
  method: manual
  onboarding: self-serve
  pricing: free
  public: true
  source:
  - documentation
  - probes
  trial: false
  try_now: true
api_count: 4
artifact_total: 0
created: '2026-07-27'
description: 'Manitoba Hydro is the provincial Crown corporation that generates, transmits, and distributes electricity and distributes natural gas across Manitoba, Canada — "Manitoba''s publicly owned electricity and natural gas supplier" in its own words, serving 632,117 electric customers and 300,789 natural gas customers, and trading electricity into wholesale markets across the Midwestern U.S. and Canada. It is a vertically integrated monopoly in a province with no retail competition, no independent system operator of its own, and no consumer energy data mandate: Ontario''s Green Button regulation (O. Reg. 633/21) binds Ontario distributors only, Australia''s Consumer Data Right does not reach Canada, and the Green Button Alliance states plainly that it has "no information about Green Button deployments in Manitoba." Manitoba Hydro also has no advanced metering infrastructure — its 2006-2009 smart meter pilot was not continued — so there is no interval consumption data for a consumer
  API to serve in the first place. The API posture is therefore the inverse of a mandated utility: consumer data is entirely closed, reachable only by the customer through a login at account.hydro.mb.ca, while grid and system data is genuinely open and anonymous. Manitoba Hydro runs a public ArcGIS Online organization whose current and planned power outage layers are queryable without a key over both the Esri ArcGIS REST API and OGC WFS 2.0.0, refreshed every five minutes; an on-domain ArcGIS Server REST directory at maps.hydro.mb.ca; and a live KISTERS hydrological monitoring application whose station and time-series JSON at hydro.mb.ca is served anonymously and was observed carrying same-day readings. None of it is documented as an API. There is no developer portal, no API keys, no OpenAPI, and no terms of use for data reuse — the open surface exists as a by-product of public map publishing rather than as an API program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-27'
name: Manitoba Hydro
nav: Providers
network: true
random_paper: 10
slug: manitoba-hydro
tags:
- Energy
- Canada
- Utilities
- Electricity
- Gas
- Hydroelectric
- Grid
- Outage Data
- Open Data
- Crown Corporation
---
