---
api_count: 5
artifact_total: 0
created: '2026-07-27'
description: 'Voltus is a United States virtual power plant (VPP) operator and distributed energy resource (DER) technology platform, headquartered in San Francisco, California, that aggregates commercial, industrial, residential and transportation loads and batteries into wholesale electricity markets across all of North America''s organized markets (AESO, CAISO, ERCOT, IESO, ISO-NE, MISO, NYISO, PJM, SPP). It sits in the demand-response and flexibility layer of the energy value chain: it is not a utility and not a metering data holder, so no Green Button, Consumer Data Right or smart-meter data mandate applies to it — mandate regime is honestly none. Its API posture is unusually good for the sector and unusually split. Voltus runs a genuine public developer portal at api.voltus.co/docs (Docusaurus, no login) with concepts, tutorials, an OpenAPI-generated reference and a changelog, plus a fully anonymous sandbox at sandbox.voltus.co that answers real HTTP requests with the documented public
  key "X-Voltus-API-Key: secret" — a developer can call it before signing anything. Production, however, is partner-only: api.voltus.co/2022-04-15 returns 401 Permission denied to the sandbox key, and real access requires a commercial partnership plus a signed Letter of Authorization per site. Site telemetry and dispatch control are exposed to partners over that account-scoped REST API and over OpenADR 2.0a Simple HTTP PULL with mutual TLS; Voltus publishes no open grid or market data of its own, so consumer/site energy data is available under contract while market data is closed. No downloadable OpenAPI or Swagger document is served — /openapi.json, /swagger.json and /openapi3.yaml all 404.'
image: https://api.voltus.co/img/voltus.png
layout: provider
modified: '2026-07-27'
name: Voltus
nav: Providers
network: true
random_paper: 5
slug: voltus
tags:
- Energy
- United States
- Electricity
- Demand Response
- Virtual Power Plant
- DER
- Grid
- Energy Markets
- Flexibility
- Energy Storage
- OpenADR
- Telemetry
---
