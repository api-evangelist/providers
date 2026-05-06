---
aid: energy-charts-api
name: Energy Charts API
description: The Energy-Charts API, provided by Fraunhofer ISE, delivers European energy data including electricity production by source, day-ahead spot market prices, cross-border electricity trading and physical flows, grid frequency, installed capacity, and renewable energy share forecasts. It covers more than 40 European countries and bidding zones, supports ISO 8601, daily, and UNIX timestamp formats, and is largely licensed under CC BY 4.0.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Energy
  - Electricity
  - Renewables
  - Grid
  - Europe
  - Power
  - Pricing
  - Forecasts
created: '2025-05-02'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/energy-charts-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: energy-charts-api:energy-charts-api
    name: Energy Charts API
    description: Public REST API from Fraunhofer ISE delivering European electricity production, prices, cross-border flows, grid frequency, installed capacity, and renewable share data across 40+ countries and bidding zones with multiple timestamp formats.
    humanURL: https://api.energy-charts.info/
    baseURL: https://api.energy-charts.info
    tags:
      - Energy
      - Electricity
      - Renewables
      - Grid
      - Power
      - Pricing
    properties:
      - type: Documentation
        url: https://api.energy-charts.info/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/energy-charts-api/refs/heads/main/openapi/energy-charts-api-openapi.yml
common:
  - type: Website
    url: https://www.energy-charts.info/
  - type: Provider
    url: https://www.ise.fraunhofer.de/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
