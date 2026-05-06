---
aid: electricity-maps
name: Electricity Maps
description: Electricity Maps tracks the carbon intensity and electricity mix of power grids around the world. Their commercial API delivers real-time, historical, and forecasted signals for carbon intensity, power source breakdown, renewable and carbon-free percentages, electricity flows, grid load, and day-ahead pricing across hundreds of geographic zones, enabling data centers, software platforms, and sustainability teams to make emissions-aware decisions.
type: Index
position: Producer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Energy
  - Electricity
  - Carbon Intensity
  - Sustainability
  - Climate
  - Grid Data
created: '2025-05-02'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/electricity-maps/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: electricity-maps:electricity-maps
    name: Electricity Maps API
    description: The Electricity Maps API exposes carbon intensity, electricity mix, renewable and carbon-free percentages, electricity flows, total and net load, and day-ahead pricing for hundreds of zones worldwide. Each signal is available in three temporality variants (latest, past, and forecast) and supports zone, coordinate, and data-center lookups with configurable temporal granularity and emission factor type.
    humanURL: https://app.electricitymaps.com/docs/getting-started
    baseURL: https://api.electricitymap.org
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Energy
      - Carbon Intensity
      - Renewables
      - Grid Data
      - Forecasting
    properties:
      - type: Documentation
        url: https://app.electricitymaps.com/docs/getting-started
      - type: OpenAPI
        url: openapi/electricity-maps-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - name: Electricity Maps Website
    url: https://www.electricitymaps.com
    type: Website
  - name: Electricity Maps Live App
    url: https://app.electricitymaps.com
    type: Application
  - name: Electricity Maps API Pricing
    url: https://www.electricitymaps.com/api-pricing
    type: Pricing
  - name: Electricity Maps Documentation
    url: https://app.electricitymaps.com/docs/getting-started
    type: Documentation
  - name: Electricity Maps Blog
    url: https://www.electricitymaps.com/blog
    type: Blog
  - name: Electricity Maps GitHub
    url: https://github.com/electricitymaps
    type: GitHub
---
