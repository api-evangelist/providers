---
api_count: 2
artifact_total: 0
created: '2026-07-27'
description: Western Power is the Western Australian state-owned statutory corporation that owns and operates the electricity transmission and distribution network — the poles, wires, substations and streetlights — across the South West Interconnected System (SWIS), from Kalbarri in the north to Albany in the south and east to Kalgoorlie, across more than 103,000 km of powerlines, 825,788 poles and towers, 276,000 streetlights and 154 transmission substations. It is a regulated network distributor (DNO/DSO), not a retailer and not a generator; Synergy is the SWIS retailer for residential and small-business customers and AEMO operates the WA Wholesale Electricity Market. Its API posture is honestly minimal — there is no developer portal, no published API program and no OpenAPI anywhere on westernpower.com.au (developer./api./docs./data. subdomains all fail to resolve; /developers, /api, /docs, /openapi.json all return 404). Consumer energy data is real but not programmatic — a third party
  must register a business with Western Power and collect verifiable customer consent, after which up to two years of interval and accumulated metering data is delivered by email or a web portal, never an API. Australia's Consumer Data Right, the mandate that forced identical banking APIs and was then transplanted into energy, does not reach this organisation at all — CDR energy covers National Electricity Market retailers, and Western Australia sits outside the NEM while distributors were never designated data holders in any state. The one genuinely machine-readable surface is an undocumented Esri ArcGIS Online feature service behind the public outage tracker, which answers anonymous queries with live unplanned and planned outage polygons. Its 36 network asset and capacity datasets are published through the WA Government DataWA/SLIP portals as "open data subject to registering for access" under Western Power's own data licence — WFS, WMS and ArcGIS REST endpoints that return HTTP 401 to
  an anonymous caller.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-27'
name: Western Power
nav: Providers
network: true
random_paper: 18
slug: western-power
tags:
- Energy
- Australia
- Utilities
- Electricity
- Grid
- Network Distribution
- Smart Metering
- Open Data
- GIS
- Outages
---
