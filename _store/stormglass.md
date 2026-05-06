---
aid: stormglass
name: Stormglass
description: Stormglass provides a global marine and weather API delivering high-resolution forecasts, historical data, and environmental measurements for any coordinate on Earth. The platform aggregates data from multiple authoritative sources including NOAA, ECMWF, DWD, and others to provide weather point forecasts, marine data, tidal information, solar and astronomical data, biological oceanographic data, and elevation/bathymetry data. Used widely for maritime navigation, renewable energy forecasting, outdoor activity planning, and environmental monitoring applications.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Astronomy
  - Bio
  - Climate
  - Elevation
  - Forecasting
  - Marine
  - Ocean
  - Solar
  - Tides
  - Weather
  - Wind
created: '2025-05-02'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/stormglass/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: stormglass:stormglass-api
    name: Stormglass API
    description: The Stormglass API provides global weather, marine, tidal, astronomical, solar, biological, and elevation data for any coordinate on Earth. It aggregates data from multiple meteorological and oceanographic sources into a single REST API. All endpoints return JSON and use API key authentication via the Authorization header.
    humanURL: https://stormglass.io/
    baseURL: https://api.stormglass.io/v2
    tags:
      - Astronomy
      - Bio
      - Elevation
      - Forecasting
      - Marine
      - Solar
      - Tides
      - Weather
    properties:
      - type: Documentation
        url: https://docs.stormglass.io/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/stormglass/refs/heads/main/openapi/stormglass-openapi.yml
      - type: Pricing
        url: https://stormglass.io/pricing
      - type: Sign Up
        url: https://stormglass.io/register
      - type: Website
        url: https://stormglass.io/
      - type: Blog
        url: https://stormglass.io/blog
      - type: TermsOfService
        url: https://stormglass.io/terms-and-conditions/
      - type: PrivacyPolicy
        url: https://stormglass.io/privacy-policy/
common:
  - type: Portal
    url: https://stormglass.io/
  - type: Documentation
    url: https://docs.stormglass.io/
  - type: Sign Up
    url: https://stormglass.io/register
  - type: Pricing
    url: https://stormglass.io/pricing
  - type: Website
    url: https://stormglass.io/
  - type: Blog
    url: https://stormglass.io/blog
  - type: TermsOfService
    url: https://stormglass.io/terms-and-conditions/
  - type: PrivacyPolicy
    url: https://stormglass.io/privacy-policy/
  - type: GitHubOrg
    url: https://github.com/stormglass
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
