---
api_count: 2
artifact_total: 0
created: '2026-07-27'
description: 'Electricity North West — rebranded SP Electricity North West in August 2025 after Iberdrola acquired it and folded it in alongside SP Energy Networks — is the regulated electricity distribution network operator for the North West of England, running roughly 13,000 km of overhead line and more than 44,000 km of underground cable from Cumbria to Manchester. It is a poles-and-wires business in the regulated middle of the United Kingdom value chain: it owns the meter point and the network, it earns a regulated revenue under Ofgem''s RIIO-ED2 price control, and it never bills the household — the supplier does. Its API posture is a clean split and worth stating plainly. On the MARKET-DATA side it is genuinely API-native for a network operator: it runs an Opendatasoft-hosted open data portal at electricitynorthwest.opendatasoft.com carrying 146 datasets — embedded capacity register, DFES scenarios, LV headroom and peak demand, network capacity heatmaps, GSP connection queue, GIS conductor
  and substation layers — served through the documented Opendatasoft Explore REST API v2.1 (and legacy v2.0) with a real OpenAPI 3.0.3 contract, a DCAT-AP catalogue export, and an in-portal API console. 96 of those datasets are CC BY 4.0 and 8 are Open Government Licence v3.0, but 41 sit under a bespoke "SP ENW Shared Licence" rather than an open one. On the CONSUMER-DATA side there is nothing: the United Kingdom has no consumer energy data-portability right equivalent to Australia''s Consumer Data Right, Great Britain''s smart-meter mandate produced infrastructure (the licensed Smart DCC) rather than a data right, Green Button has no UK footprint, and Electricity North West publishes no customer usage or billing API of any kind. The obligation that actually binds it is Ofgem''s Data Best Practice Guidance under the RIIO-ED2 digitalisation licence condition — an open-data duty, not a consumer data right — and the portal is a real, verifiable implementation of it. Note that the corporate
  site www.enwl.co.uk sits behind a Cloudflare managed challenge and returns HTTP 403 to every non-browser client, so no part of the main website is machine-readable.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-27'
name: Electricity North West
nav: Providers
network: true
random_paper: 37
slug: electricity-north-west
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Grid
- Distribution Network
- Open Data
- DER
- Renewables
- Energy Markets
- Smart Metering
---
