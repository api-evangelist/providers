---
aid: dtn
url: https://raw.githubusercontent.com/api-evangelist/dtn/refs/heads/main/apis.yml
apis:
- aid: dtn:dtn-weather-conditions-api
  name: DTN Weather Conditions API
  tags:
  - Agriculture
  - Climate
  - Forecast
  - REST
  - Weather
  image: https://raw.githubusercontent.com/api-evangelist/dtn/refs/heads/main/image.png
  humanURL: https://devportal.dtn.com/catalog/Weather/dtn-weather-conditions-api/documentation
  baseURL: https://weather.api.dtn.com/conditions
  properties:
  - url: https://devportal.dtn.com/catalog/Weather/dtn-weather-conditions-api/documentation
    type: Documentation
  - url: https://devportal.dtn.com/catalog/Weather/dtn-weather-conditions-api/documentation
    type: Reference
  - url: https://devportal.dtn.com/
    type: Portal
  - url: https://raw.githubusercontent.com/api-evangelist/dtn/refs/heads/main/openapi/dtn-weather-conditions-openapi.yml
    type: OpenAPI
  description: DTN Weather Conditions API delivers worldwide forecast, current condition, and historical weather data. The API leverages cloud technology and global forecast models to provide validated, continuously calibrated weather data. Supports geospatial queries, time-based filtering, and multi-station requests across over 70,000 weather stations worldwide. OpenAPI/Swagger spec, Postman collections, and release notes available via the developer portal.
- aid: dtn:dtn-point-observation-api
  name: DTN Point Observation API
  tags:
  - Agriculture
  - Historical Data
  - Observations
  - Weather
  image: https://raw.githubusercontent.com/api-evangelist/dtn/refs/heads/main/image.png
  humanURL: https://api.weather.mg/api-detail-pages/observation-parameter.html
  baseURL: https://point-observation.weather.mg
  properties:
  - url: https://api.weather.mg/api-detail-pages/observation-parameter.html
    type: Documentation
  - url: https://api.weather.mg/
    type: Portal
  description: DTN Point Observation API delivers high-quality weather observation data from weather stations and locations worldwide. Supports near real-time and up to 30 years of historical weather observations. Authentication uses OAuth2 with Client ID and Client Secret. Access tokens obtained via POST to auth.weather.mg/oauth/token, valid for approximately 1 hour, delivered as Bearer tokens.
- aid: dtn:dtn-point-forecast-api
  name: DTN Point Forecast API
  tags:
  - Agriculture
  - Aviation
  - Forecast
  - Weather
  image: https://raw.githubusercontent.com/api-evangelist/dtn/refs/heads/main/image.png
  humanURL: https://api.weather.mg/api-detail-pages/forecast-parameter.html
  baseURL: https://point-forecast.weather.mg
  properties:
  - url: https://api.weather.mg/api-detail-pages/forecast-parameter.html
    type: Documentation
  - url: https://api.weather.mg/
    type: Portal
  description: DTN Point Forecast API delivers high-quality weather forecasts for specified locations. Provides hourly and daily forecast data for agriculture, aviation, shipping, and utilities use cases. Uses the same OAuth2 authentication as the Point Observation API.
- aid: dtn:dtn-radar-precipitation-forecast-api
  name: DTN Radar Precipitation Forecast API
  tags:
  - Precipitation
  - Radar
  - Short-Term Forecast
  - Weather
  image: https://raw.githubusercontent.com/api-evangelist/dtn/refs/heads/main/image.png
  humanURL: https://api.weather.mg/
  baseURL: https://precipitation-forecast.weather.mg
  properties:
  - url: https://api.weather.mg/
    type: Documentation
  description: DTN Radar Precipitation Forecast API provides short-term precipitation forecasts derived from radar data. Supports agricultural, utility, and renewable energy operational planning. Uses OAuth2 authentication with Client ID and Client Secret credentials.
- aid: dtn:dtn-commodity-data-api
  name: DTN Commodity & Market Data API
  tags:
  - Agriculture
  - Commodity Prices
  - Grain
  - Livestock
  - Market Data
  image: https://raw.githubusercontent.com/api-evangelist/dtn/refs/heads/main/image.png
  humanURL: https://www.dtn.com/resources/api-data-integrations/
  baseURL: https://api.dtn.com
  properties:
  - url: https://www.dtn.com/resources/api-data-integrations/
    type: Documentation
  description: DTN provides real-time and historical commodity price data, grain and livestock prices, planting condition indices, and market analysis APIs for precision agriculture and commodity trading workflows.
name: Dtn
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The operation intelligence you can rely on to make confident desicions. Empower your business with the best data resource possible.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

