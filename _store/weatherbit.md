---
aid: weatherbit
url: https://raw.githubusercontent.com/api-evangelist/weatherbit/refs/heads/main/apis.yml
apis:
  - aid: weatherbit:weatherbit-current-weather-api
    name: Weatherbit Current Weather API
    tags:
      - Weather
      - Current Conditions
      - Observations
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.weatherbit.io/v2.0
    humanURL: https://www.weatherbit.io/api/weather-current
    properties:
      - url: https://www.weatherbit.io/api/weather-current
        type: Documentation
      - url: openapi/weatherbit-current-weather-openapi-original.yml
        type: OpenAPI
    description: Returns current weather conditions from Weatherbit's global network of sub-hourly reporting weather stations and atmospheric meso-analyses. Supports lookup by lat/lon, city name, city ID, postal code, or station ID.
  - aid: weatherbit:weatherbit-severe-weather-alerts-api
    name: Weatherbit Severe Weather Alerts API
    tags:
      - Weather
      - Alerts
      - Emergency
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.weatherbit.io/v2.0
    humanURL: https://www.weatherbit.io/api/alerts
    properties:
      - url: https://www.weatherbit.io/api/alerts
        type: Documentation
    description: Returns severe weather alerts issued by local meteorological agencies. Covers the USA (NOAA), EU nations and UK (Meteoalarm), Canada (Environment Canada), and China (China Meteorological Administration).
  - aid: weatherbit:weatherbit-weather-forecast-api
    name: Weatherbit Weather Forecast API
    tags:
      - Weather
      - Forecasting
      - Daily
      - Hourly
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.weatherbit.io/v2.0
    humanURL: https://www.weatherbit.io/api/weather-forecast-api
    properties:
      - url: https://www.weatherbit.io/api/weather-forecast-api
        type: Documentation
    description: Provides accurate weather forecasts using high-resolution global and regional weather models. Includes 16-day daily, 240-hour hourly, and 60-minute precipitation nowcasts.
  - aid: weatherbit:weatherbit-historical-weather-api
    name: Weatherbit Historical Weather API
    tags:
      - Weather
      - Historical
      - Climate
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.weatherbit.io/v2.0
    humanURL: https://www.weatherbit.io/api/historical-weather-api
    properties:
      - url: https://www.weatherbit.io/api/historical-weather-api
        type: Documentation
    description: High-resolution historical weather data backed by over 120,000 weather stations and gridded datasets. Includes daily, hourly, and sub-hourly observations, climate normals, and gap-free data.
  - aid: weatherbit:weatherbit-ag-weather-api
    name: Weatherbit Ag-Weather API
    tags:
      - Weather
      - Agriculture
      - Evapotranspiration
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.weatherbit.io/v2.0
    humanURL: https://www.weatherbit.io/api/agweather-api
    properties:
      - url: https://www.weatherbit.io/api/agweather-api
        type: Documentation
    description: Agricultural weather data using the GLDAS re-analysis with global coverage at 0.25-degree resolution. Includes evapotranspiration, soil moisture, and crop-specific weather parameters.
  - aid: weatherbit:weatherbit-air-quality-api
    name: Weatherbit Air Quality API
    tags:
      - Air Quality
      - AQI
      - Environment
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.weatherbit.io/v2.0
    humanURL: https://www.weatherbit.io/api/air-quality-api
    properties:
      - url: https://www.weatherbit.io/api/air-quality-api
        type: Documentation
    description: High-quality air quality data derived from global and regional air quality models. Tracks six major pollutants (PM2.5, PM10, O3, NO2, SO2, CO) plus pollen levels and mold. Includes current and 72-hour forecast data.
name: Weatherbit
tags:
  - Weather
  - Forecasting
  - Historical Data
  - Air Quality
  - Alerts
  - Agricultural Weather
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: https://www.weatherbit.io/pricing
    type: Plans
  - url: https://www.weatherbit.io/features
    type: Features
  - url: https://help.weatherbit.io/faq/
    type: FAQ
  - url: https://status.weatherbit.io/
    type: StatusPage
  - url: https://blog.weatherbit.io/
    type: Blog
  - url: https://help.weatherbit.io/
    type: KnowledgeCenter
  - url: https://www.weatherbit.io/account/create
    type: SignUp
  - url: https://www.weatherbit.io/account/login
    type: Login
  - url: https://www.weatherbit.io/terms
    type: TermsOfService
  - url: https://www.weatherbit.io/privacy
    type: PrivacyPolicy
  - url: https://www.weatherbit.io/contact
    type: Contact
  - url: https://github.com/weatherbit/weatherbit-python
    type: GitHubRepository
  - url: https://pypi.org/project/pyweatherbit/
    type: SDK
    title: Python SDK
  - type: SpectralRules
    url: rules/weatherbit-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/weather-intelligence.yaml
    title: Weather Intelligence Capability
  - type: Vocabulary
    url: vocabulary/weatherbit-vocabulary.yml
  - type: Features
    data:
      - name: Current Weather
        description: Live observations updated every 5-30 minutes from global weather station network.
      - name: 16-Day Daily Forecasts
        description: High-accuracy daily forecasts for up to 16 days ahead using state-of-the-art weather models.
      - name: 240-Hour Hourly Forecasts
        description: Detailed hourly forecasts for up to 10 days (240 hours) ahead.
      - name: Severe Weather Alerts
        description: Real-time severe weather alerts from official agencies in the US, EU, Canada, and China.
      - name: Historical Weather Data
        description: Gap-free historical weather data going back decades using ML and statistical backfilling.
      - name: Air Quality Monitoring
        description: Current and forecast air quality data tracking PM2.5, PM10, O3, NO2, SO2, CO, and pollen levels.
      - name: Agricultural Weather
        description: Specialized agricultural weather data including evapotranspiration, soil moisture, and growing degree days.
      - name: Energy Forecasts
        description: Energy sector weather forecasts including heating and cooling degree days.
      - name: Climate Normals
        description: 1991-2020 climate normals at 9km resolution for historical comparison.
      - name: Multiple Lookup Methods
        description: Access data by lat/lon, city name, city ID, station ID, ICAO code, or postal code.
  - type: UseCases
    data:
      - name: Mobile Weather Apps
        description: Power consumer weather applications with accurate forecasts and real-time conditions.
      - name: Agricultural Planning
        description: Optimize crop management with specialized agricultural weather forecasts and historical data.
      - name: Energy Management
        description: Use degree-day forecasts for energy demand prediction and grid management.
      - name: Emergency Management
        description: Monitor severe weather alerts for disaster preparedness and emergency response.
      - name: Insurance and Risk
        description: Access historical and forecast weather data for risk assessment and claims processing.
      - name: Logistics and Transportation
        description: Optimize routing and operations based on weather forecasts and real-time conditions.
  - type: Integrations
    data:
      - name: Python
        description: Official Python SDK available on PyPI (pyweatherbit)
      - name: REST API
        description: RESTful JSON API compatible with any programming language
created: 2023/11/20
modified: '2026-05-03'
description: Weatherbit is a leading provider of weather data and forecasting services. They specialize in delivering accurate and up-to-date weather information to businesses and individuals around the world. Services include real-time current weather, 16-day daily and 240-hour hourly forecasts, historical weather data, severe alerts, air quality monitoring, agricultural weather, energy forecasts, and climate normals. Data is available globally via lat/lon, city name, postal code, and station ID.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
type: Index
position: Consumer
access: 3rd-Party
---
