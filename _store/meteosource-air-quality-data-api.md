---
aid: meteosource-air-quality-data-api
name: MeteoSource Air Quality Data API
description: MeteoSource provides an Air Quality API delivering hour-by-hour pollution data for any location on Earth, with forecasts up to 5 days ahead. The API also offers weather forecast data from multiple meteorological models.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/meteosource-air-quality-data-api/refs/heads/main/apis.yml
tags:
  - Air Quality
  - Environmental Data
  - Forecasting
  - Weather
created: '2024-11-07'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: meteosource-air-quality-data-api:meteosource-air-quality-data-api
    name: MeteoSource Air Quality Data API
    tags:
      - Air Quality
      - Weather
    humanURL: https://www.meteosource.com/air-quality-api
    baseURL: https://www.meteosource.com/api/v1
    properties:
      - url: https://www.meteosource.com/air-quality-api
        type: Documentation
      - url: openapi/meteosource-air-quality-data-api-openapi.yml
        type: OpenAPI
    description: Access air quality data through the MeteoSource API for any location on Earth, providing hour-by-hour pollution forecasts up to 5 days.
common:
  - type: Portal
    url: https://www.meteosource.com/
  - type: Pricing
    url: https://www.meteosource.com/pricing
  - type: Sign Up
    url: https://www.meteosource.com/client/register
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
