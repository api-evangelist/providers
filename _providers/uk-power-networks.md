---
api_count: 2
artifact_total: 0
created: '2026-07-27'
description: 'UK Power Networks is the distribution network operator for London, the South East and the East of England, running three electricity distribution licence areas — London Power Networks (LPN), South Eastern Power Networks (SPN) and Eastern Power Networks (EPN) — and the Distribution System Operator function that sits on top of them. It is a poles-and-wires business: it owns the substations, cables and overhead lines, holds the network capacity and connection queue, and handles more than 70,000 connection enquiries a year, but it does not sell electricity and has no retail customer relationship to expose. Its API posture is the exact inverse of the usual utility story. Britain never legislated a consumer energy data right — there is no CDR equivalent, no Green Button obligation, and the one thing the UK did mandate was infrastructure (the Smart DCC carrying smart-meter traffic under the Smart Energy Code), which produces no public API. What did produce an API was Ofgem''s Data
  Best Practice and digitalisation obligation on network licensees, and UK Power Networks has actually implemented it: a live Opendatasoft-hosted Open Data Portal serving 136 datasets over a documented, versioned REST API with a real OpenAPI 3.0.3 contract published at its own domain, a DCAT-AP catalogue export, and an official open-source Python client (ukpyn) on PyPI. So the split is unusually sharp and unusually positive on one side: market and network data is genuinely open and genuinely queryable — live faults, carbon intensity, embedded capacity register, substation and feeder-level smart meter aggregates, LTDS tables, flexibility dispatches, curtailment events — while consumer data is not merely closed but absent, because as a DNO it holds no billable customer account to hand over. The gate is free and self-serve rather than open: the catalogue and 36 of 136 datasets answer anonymously, but the other 99 return HTTP 403 until you register a free account and mint an API key.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-27'
name: UK Power Networks
nav: Providers
network: true
random_paper: 64
slug: uk-power-networks
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Grid
- Distribution Network
- Open Data
- Smart Metering
- DER
- EV Charging
- Carbon
- Energy Markets
---
