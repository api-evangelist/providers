---
aid: solcast
name: Solcast
description: Solcast is a solar and renewable energy data company, acquired by DNV in 2023, that provides high-resolution, satellite-derived solar irradiance, PV power, weather forecasting, and historical climate data via a developer API. Its data covers live, forecast, historical, and typical meteorological year (TMY) datasets for rooftop PV, advanced PV, grid aggregations, and soiling models globally.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Solar
  - Energy
  - Forecasting
  - Irradiance
  - Weather
  - Renewable Energy
  - PV Power
created: '2025-05-02'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/solcast/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: solcast:solcast
    name: Solcast API
    description: The Solcast API provides live, forecast, historical, and typical meteorological year (TMY) solar irradiance, PV power, and weather data derived from a global fleet of weather satellites. It supports rooftop PV power, advanced PV power (for registered sites), grid aggregation data, and soiling loss models (Kimber and HSU). Authentication uses an API key. Data is available in JSON and CSV formats with 5- to 60-minute granularity anywhere on the planet.
    humanURL: https://docs.solcast.com.au/
    baseURL: https://api.solcast.com.au
    tags:
      - Solar
      - Forecasting
      - Irradiance
      - PV Power
      - Weather
      - Renewable Energy
      - Grid Aggregation
      - Historical Data
      - TMY
      - Soiling
    properties:
      - type: Documentation
        url: https://docs.solcast.com.au/
      - type: Getting Started
        url: https://docs.solcast.com.au/docs/getting-started
      - type: Authentication
        url: https://docs.solcast.com.au/docs/api-authentication
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/solcast/refs/heads/main/openapi/solcast-openapi.yml
      - type: SDKs
        url: https://solcast.com/sdk
      - type: PythonSDK
        url: https://github.com/Solcast/solcast-api-python-sdk
      - type: CSharpSDK
        url: https://github.com/Solcast/solcast-api-csharp-sdk
      - type: JuliaSDK
        url: https://github.com/Solcast/Solcast.jl
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/solcast/refs/heads/main/rules/solcast-rules.yml
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/solcast/refs/heads/main/capabilities/solar-forecasting.yaml
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/solcast/refs/heads/main/capabilities/solar-resource-assessment.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/solcast/refs/heads/main/json-schema/solcast-radiation-and-weather-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/solcast/refs/heads/main/json-schema/solcast-pv-power-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/solcast/refs/heads/main/json-schema/solcast-pv-power-site-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/solcast/refs/heads/main/json-structure/solcast-radiation-and-weather-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/solcast/refs/heads/main/json-structure/solcast-pv-power-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/solcast/refs/heads/main/json-structure/solcast-pv-power-site-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/solcast/refs/heads/main/json-ld/solcast-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/solcast/refs/heads/main/vocabulary/solcast-vocabulary.yml
    contact:
      - FN: Solcast Support
        url: https://solcast.com/contact
    features:
      - name: Live Radiation and Weather Data
        description: Real-time satellite-derived solar irradiance and weather, updated every 5 minutes, covering the last 7 days.
      - name: Forecast Radiation and Weather
        description: Solar irradiance and weather forecasts up to 14 days ahead with 5- to 60-minute granularity.
      - name: Rooftop PV Power (Live, Forecast, Historic, TMY)
        description: Estimated PV power output for rooftop solar sites by latitude/longitude without pre-registration.
      - name: Advanced PV Power (Live, Forecast, Historic)
        description: High-specification PV power data for registered PV power sites using Solcast's advanced PV model.
      - name: Historical Data
        description: Historical solar radiation and weather data available from 2007-01-01 up to 7 days before present.
      - name: Typical Meteorological Year (TMY)
        description: Long-run average solar and weather profiles calculated from 2007 to 2023 data.
      - name: Grid Aggregation (Live and Forecast)
        description: Live and forecast aggregation data for grid collections and sub-aggregations, up to 7 days.
      - name: Soiling Models
        description: Hourly soiling loss estimates using the Kimber and HSU models, available for live, forecast, and historic data.
      - name: PV Power Site Management
        description: CRUD management of registered PV power sites for use with the advanced PV power model.
    useCases:
      - name: Solar Farm Performance Monitoring
        description: Operators monitor live and forecast irradiance alongside actual PV output to detect underperformance.
      - name: Energy Market Bidding
        description: Traders use 14-day forecasts to place optimal bids in electricity markets.
      - name: Grid Management
        description: Grid operators aggregate real-time and forecast PV generation across portfolios using the aggregation API.
      - name: Solar Resource Assessment
        description: Project developers use historical and TMY data for bankable resource assessment in project financing.
      - name: Soiling Analysis
        description: Asset managers model panel soiling losses to schedule cleaning and improve yield.
      - name: Renewable Energy Integration
        description: Utilities integrate solar forecasts to balance supply and demand and optimise dispatch decisions.
    integrations:
      - name: Python
        url: https://github.com/Solcast/solcast-api-python-sdk
      - name: C# / .NET
        url: https://github.com/Solcast/solcast-api-csharp-sdk
      - name: Julia
        url: https://github.com/Solcast/Solcast.jl
      - name: pvlib
        url: https://pvlib-python.readthedocs.io/
      - name: Pandas
        url: https://github.com/Solcast/howto-pandas
      - name: GeoServer
        url: https://github.com/Solcast/geoserver
common:
  - type: Portal
    url: https://solcast.com/
  - type: Documentation
    url: https://docs.solcast.com.au/
  - type: SDKs
    url: https://solcast.com/sdk
  - type: Sign Up
    url: https://toolkit.solcast.com.au/register
  - type: Pricing
    url: https://solcast.com/pricing/irradiance-weather
  - type: Change Log
    url: https://solcast.com/changelog
  - type: Website
    url: https://solcast.com
  - type: GitHub
    url: https://github.com/Solcast
  - type: API Toolkit
    url: https://toolkit.solcast.com.au/
  - type: Terms of Service
    url: https://solcast.com/terms-of-service
  - type: Privacy Policy
    url: https://solcast.com/privacy-policy
  - type: Contact
    url: https://solcast.com/contact
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
