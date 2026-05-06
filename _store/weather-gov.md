---
aid: weather-gov
url: https://raw.githubusercontent.com/api-evangelist/weather-gov/refs/heads/main/apis.yml
apis:
  - name: Weather.gov API Web Service
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.weather.gov/documentation/services-web-api
    baseURL: https://api.weather.gov
    properties:
      - url: openapi/openapi.yml
        name: Weather.gov OpenAPI
        type: OpenAPI
      - url: https://www.weather.gov/documentation/services-web-api
        type: Documentation
      - url: https://api.weather.gov/openapi.json
        type: APIReference
    description: The National Weather Service API provides access to real-time weather data including forecasts, alerts, observations, radar, aviation weather, and zone information for the United States. The API is free, open, and requires only a User-Agent header for identification.
    aid: weather-gov:weather-gov-api-web-service
    tags:
      - Weather
      - Forecasting
      - Alerts
      - Observations
      - Radar
      - United States
      - Government
name: Weather.gov
tags:
  - Weather
  - Government
  - United States
  - Forecasting
  - Alerts
  - Open Data
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/api-web-service.png
common:
  - url: https://www.weather.gov/documentation/services-web-api
    type: Documentation
  - url: https://github.com/weather-gov/api
    type: GitHubRepository
  - url: https://api.weather.gov/openapi.json
    type: APIReference
  - url: https://www.weather.gov
    type: Portal
  - url: https://www.weather.gov/contact
    type: Contact
  - url: https://api.weather.gov/glossary
    type: Glossary
  - type: Features
    data:
      - name: Free and Open
        description: No API key required (only a User-Agent header); completely free for any use.
      - name: Forecast Gridpoints
        description: 12-hour and hourly forecasts for 2.5km grid cells across the US.
      - name: Real-Time Alerts
        description: Live weather alerts and warnings including active counts by area, zone, and region.
      - name: Observation Data
        description: Latest and historical observations from thousands of weather stations across the US.
      - name: Radar Data
        description: Radar station metadata, alarms, queues, and wind profiler data.
      - name: Aviation Weather
        description: SIGMETs, AIRMETs, Center Weather Advisories, and Terminal Aerodrome Forecasts for pilots.
      - name: GeoJSON Responses
        description: All responses return GeoJSON or JSON-LD by default, suitable for mapping and linked data.
      - name: Multiple Output Formats
        description: Supports GeoJSON, JSON-LD, DWML, OXML, CAP, and ATOM formats.
  - type: UseCases
    data:
      - name: Emergency Management
        description: Monitor active weather alerts and warnings for emergency response and public safety decisions.
      - name: Application Development
        description: Integrate NWS weather data into mobile apps, websites, and IoT devices.
      - name: Aviation Planning
        description: Access SIGMETs, AIRMETs, and TAFs for flight planning and aviation safety.
      - name: Agricultural Monitoring
        description: Use zone forecasts and observation data for crop management and agricultural planning.
      - name: Research and Education
        description: Access historical observation data and forecast products for climate research and educational purposes.
  - type: SpectralRules
    url: rules/weather-gov-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/weather-monitoring.yaml
    title: Weather Monitoring Capability
  - type: Vocabulary
    url: vocabulary/weather-gov-vocabulary.yml
created: '2024-07-02T00:00:00.000Z'
modified: '2026-05-03'
description: Weather.gov is the official website of the National Weather Service (NWS), operated by NOAA within the US Department of Commerce. The NWS provides weather, hydrologic, and climate forecasts and warnings for the United States, its territories, adjacent waters, and ocean areas. The Weather.gov API provides free, open access to forecasts, alerts, observations, radar data, aviation weather, and geographic zone information across all 50 states and territories.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
type: Index
position: Consumer
access: 3rd-Party
---
