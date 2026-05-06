---
aid: national-weather-service
name: National Weather Service
description: The National Weather Service (NWS) is a government agency within the National Oceanic and Atmospheric Administration (NOAA) that is responsible for providing weather forecasts, warnings, and other meteorological information to the public, government agencies, and private industries.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/national-weather-service/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Federal Government
  - Forecasting
  - Weather
apis:
  - aid: national-weather-service:national-weather-service-api
    name: National Weather Service API
    tags:
      - Forecasting
      - Weather
    humanURL: https://www.weather.gov/documentation/services-web-api
    baseURL: https://api.weather.gov/
    properties:
      - url: https://www.weather.gov/documentation/services-web-api
        type: Documentation
      - url: https://api.weather.gov/openapi.json
        type: OpenAPI
      - url: openapi/national-weather-service-openapi.json
        type: OpenAPI
    description: The National Weather Service API allows developers access to critical forecasts, alerts, and observations, along with other weather data. The API is designed with a cache-friendly approach and based on JSON-LD to promote machine data discovery.
common:
  - type: Website
    url: https://www.weather.gov/
  - type: Portal
    url: https://www.weather.gov/documentation/services-web-api
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
