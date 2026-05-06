---
aid: xweather
name: Xweather
description: Xweather, a Vaisala company, provides weather data APIs delivering science-backed, hyper-local weather intelligence for operational applications. The Xweather Weather API exposes current conditions, forecasts, severe weather alerts, lightning data, air quality, observations, wildfire information, tropical cyclone tracks, and maritime weather through a single REST API. Authentication uses a client_id and client_secret passed as query parameters or HTTP headers.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consumer
url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/apis.yml
tags:
  - Air Quality
  - Company
  - Data
  - Forecasts
  - Lightning
  - Maritime
  - Observations
  - Severe Weather
  - Weather
created: '2024-11-08'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: xweather:xweather
    name: Xweather Weather API
    description: The Xweather Weather API provides real-time and historical weather data including current conditions, forecasts, severe weather alerts, lightning data, air quality, maritime weather, wildfire data, and tropical cyclone information. Backed by Vaisala, Xweather delivers science-backed hyper-local weather intelligence through a RESTful interface authenticated with client ID and client secret.
    humanURL: https://www.xweather.com/docs/weather-api
    baseURL: https://data.api.xweather.com
    tags:
      - Air Quality
      - Alerts
      - Data
      - Forecasts
      - Lightning
      - Maritime
      - Observations
      - Severe Weather
      - Weather
    properties:
      - type: Documentation
        url: https://www.xweather.com/docs/weather-api
      - type: GettingStarted
        url: https://www.xweather.com/docs/weather-api/getting-started/authentication
      - type: APIReference
        url: https://www.xweather.com/docs/weather-api/endpoints
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/openapi/xweather-weather-api-openapi.yml
common:
  - type: Website
    url: https://xweather.com
  - type: Documentation
    url: https://www.xweather.com/docs/weather-api
  - type: APIReference
    url: https://www.xweather.com/docs/weather-api/endpoints
  - type: Authentication
    url: https://www.xweather.com/docs/weather-api/getting-started/authentication
  - type: SignUp
    url: https://www.xweather.com/
  - type: Pricing
    url: https://www.xweather.com/weather-api
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/openapi/xweather-weather-api-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/json-schema/xweather-location-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/json-schema/xweather-conditions-observation-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/json-schema/xweather-forecast-period-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/json-schema/xweather-alert-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/json-schema/xweather-lightning-strike-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/json-schema/xweather-air-quality-observation-schema.json
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/json-structure/xweather-weather-api-structure.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/json-ld/xweather-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/vocabulary/xweather-vocabulary.yml
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/rules/xweather-rules.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/capabilities/operational-weather-monitoring.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/capabilities/lightning-safety.yaml
  - type: Example
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/examples/xweather-get-conditions-example.json
  - type: Example
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/examples/xweather-get-forecasts-example.json
  - type: Example
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/examples/xweather-get-alerts-example.json
  - type: Example
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/examples/xweather-get-lightning-example.json
  - type: Example
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/examples/xweather-get-air-quality-example.json
  - type: Example
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/examples/xweather-list-tropical-cyclones-example.json
  - type: Example
    url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/examples/xweather-get-maritime-example.json
  - type: Features
    data:
      - name: Real-Time Conditions
        description: Current surface weather observations for any location worldwide.
      - name: Hourly and Daily Forecasts
        description: Forecast records out to 15 days with hourly and daily granularity.
      - name: Severe Weather Alerts
        description: Government-issued alerts, watches, and warnings with severity, urgency, and certainty.
      - name: Global Lightning Network
        description: Cloud-to-ground and in-cloud lightning strike data from Vaisala's global detection network.
      - name: Lightning Threat Nowcast
        description: Probabilistic short-term lightning threat used to drive stop-work and all-clear automation.
      - name: Air Quality
        description: AQI values, primary pollutant, and detailed pollutant breakdowns for monitoring and reporting.
      - name: Maritime Weather
        description: Marine weather including waves, swell, sea-surface temperature, and sea state.
      - name: Wildfire Data
        description: Active wildfire incident records and perimeters for situational awareness.
      - name: Tropical Cyclones
        description: Active tropical cyclone tracks, intensity, and forecast cones.
  - type: UseCases
    data:
      - name: Construction Lightning Safety
        description: Automatically pause and resume outdoor construction work using lightning threat nowcasts.
      - name: Aviation Ground Operations
        description: Drive ramp closures and re-openings around lightning, severe weather, and visibility thresholds.
      - name: Outdoor Sports and Events
        description: Manage stadium and event evacuations and re-entries based on lightning and severe weather.
      - name: Energy and Utilities
        description: Plan grid operations, crew dispatch, and storm restoration around forecasts and alerts.
      - name: Logistics and Routing
        description: Optimize routing and dispatch decisions using maritime, road weather, and severe weather feeds.
      - name: Insurance and Risk
        description: Use historical and real-time storm and lightning data for claims and underwriting.
      - name: Environmental Reporting
        description: Aggregate AQI and pollutant feeds for ESG and regulatory reporting.
  - type: Integrations
    data:
      - name: AerisWeather Mapping
        description: Tile and overlay services for visualizing Xweather data on web and mobile maps.
      - name: Vaisala Lightning Network
        description: Underlying global lightning detection infrastructure feeding the Xweather lightning APIs.
      - name: Common Alerting Protocol
        description: Severe-weather alert payloads align with CAP severity, urgency, and certainty fields.
      - name: METAR
        description: Surface observations are derived from the international METAR observation standard.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
