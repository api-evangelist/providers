---
aid: air-quality-programmatic-apis
url: https://raw.githubusercontent.com/api-search/air-quality-programmatic-apis/refs/heads/main/apis.yml
apis:
  - aid: air-quality-programmatic-apis:air-quality-programmatic-apis
    name: AQICN Real-Time Air Quality API
    tags:
      - Air Quality
      - AQI
      - PM2.5
      - EPA
      - Environment
      - Public Health
      - Real-Time
      - Open Data
    humanURL: https://aqicn.org/api/
    properties:
      - url: https://aqicn.org/api/
        type: Documentation
      - url: https://aqicn.org/json-api/doc/
        type: APIReference
        title: JSON API Reference
      - url: openapi/air-quality-programmatic-apis-openapi.yml
        type: OpenAPI
        title: Map Tile API
      - url: https://aqicn.org/data-platform/token/
        type: Authentication
        title: API Token Request
    description: Real-time and forecast air quality data from 11,000+ monitoring stations globally. Returns AQI measurements for PM2.5, PM10, NO2, CO, SO2, and ozone pollutants by city, station, geographic coordinates, or IP geolocation. Includes weather data and 3-8 day air quality forecasts.
  - aid: air-quality-programmatic-apis:aqicn-json-api
    name: AQICN JSON Air Quality API
    tags:
      - Air Quality
      - AQI
      - PM2.5
      - JSON
      - Real-Time
      - Forecast
    humanURL: https://aqicn.org/json-api/doc/
    description: JSON API returning real-time AQI station data by city name, station name, geographic coordinates, or IP geolocation. Includes pollutant breakdowns (PM2.5, PM10, NO2, CO, SO2, O3), weather data, and multi-day forecasts.
    properties:
      - url: https://aqicn.org/json-api/doc/
        type: Documentation
      - url: https://aqicn.org/json-api/doc/
        type: APIReference
      - url: openapi/aqicn-json-api-openapi.yaml
        type: OpenAPI
name: Air Quality Programmatic APIs
tags:
  - Air Quality
  - Environment
  - EPA
  - Open Data
  - Public Health
  - IoT
  - Government Data
  - Real-Time Data
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - name: AQICN FAQ
    url: https://aqicn.org/faq/
    type: FAQ
    description: Frequently asked questions about AQICN air quality data and APIs.
  - name: AQICN API Token
    url: https://aqicn.org/data-platform/token/
    type: Authentication
    description: Request an API access token for AQICN programmatic APIs.
  - name: AQICN Map
    url: https://aqicn.org/map/
    type: Portal
    description: World air quality index map powered by the AQICN API.
  - name: AQICN Data Platform
    url: https://aqicn.org/data-platform/
    type: Portal
    description: AQICN data platform for historical downloads and enterprise access.
  - name: AQICN Terms of Use
    url: https://aqicn.org/api/tos/
    type: TermsOfService
    description: Terms of service for AQICN API usage (non-commercial free use).
  - type: Features
    data:
      - name: Real-Time AQI Data
        description: Live air quality index readings from 11,000+ monitoring stations updated continuously.
      - name: Global Coverage
        description: Data from 1,000+ cities worldwide including US EPA, China MEP, Europe EEA, and other monitoring networks.
      - name: Multi-Pollutant Data
        description: Pollutant-specific AQI for PM2.5, PM10, nitrogen dioxide, carbon monoxide, sulfur dioxide, and ozone.
      - name: Air Quality Forecasts
        description: 3-8 day air quality forecasts for major monitoring stations.
      - name: Geolocation Queries
        description: Find nearest stations by latitude/longitude, city name, or IP-based geolocation.
      - name: Map Tile API
        description: Raster map tiles for overlaying real-time AQI data on web maps (Leaflet, Google Maps, etc.).
      - name: Station Search
        description: Search and discover monitoring stations by name or location within a geographic boundary.
      - name: Weather Data
        description: Current weather conditions co-located with air quality measurements.
  - type: UseCases
    data:
      - name: Air Quality Mobile Apps
        description: Build apps that show users real-time air quality for their location with health recommendations.
      - name: Environmental Monitoring Dashboards
        description: Create web dashboards visualizing air quality trends across cities and regions.
      - name: Public Health Research
        description: Access historical and real-time air quality data for epidemiological and public health research.
      - name: Smart City Integration
        description: Integrate air quality data into smart city platforms and IoT systems for environmental management.
      - name: Outdoor Activity Planning
        description: Provide air quality-based recommendations for outdoor activities in fitness and weather apps.
  - type: Integrations
    data:
      - name: Leaflet Maps
        description: Integrate AQI map tiles with Leaflet.js for interactive air quality maps.
      - name: Google Maps
        description: Overlay AQI data on Google Maps using the tile API.
      - name: US EPA AirNow
        description: Data aggregated from US EPA AirNow monitoring network.
      - name: OpenAQ
        description: Complementary open air quality data platform with API access.
  - name: AQICN Spectral Rules
    url: rules/aqicn-spectral-rules.yml
    type: SpectralRules
    description: Spectral rules for AQICN API conventions.
  - name: Air Quality Monitoring Capability
    url: capabilities/air-quality-monitoring.yaml
    type: NaftikoCapability
    description: Naftiko workflow for air quality monitoring.
  - name: AQICN Vocabulary
    url: vocabulary/aqicn-vocabulary.yaml
    type: Vocabulary
    description: Taxonomy for AQICN air quality APIs.
created: '2024-11-07'
modified: '2026-04-19'
position: Consuming
description: Air Quality Programmatic APIs provide real-time and forecast air quality data from 11,000+ monitoring stations in 1,000+ cities worldwide. APIs deliver Air Quality Index (AQI) measurements for PM2.5, PM10, NO2, CO, SO2, and ozone pollutants. Provided by AQICN (World Air Quality Index project) in partnership with the US EPA and global environmental agencies. Data is available via JSON API and map tile API for visualization.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
