---
aid: agromonitoring
url: https://raw.githubusercontent.com/api-evangelist/agromonitoring/refs/heads/main/apis.yml
apis:
  - aid: agromonitoring:agromonitoring
    name: Agromonitoring
    tags:
      - Agriculture
      - Satellite Imagery
      - Vegetation Indices
      - Weather
      - Precision Agriculture
    humanURL: https://agromonitoring.com/
    properties:
      - url: https://agromonitoring.com/
        type: Documentation
      - url: https://agromonitoring.com/api/
        type: APIReference
      - url: https://agromonitoring.com/api/agro/#auth
        type: Authentication
      - url: https://agromonitoring.com/subscriptions
        type: Pricing
      - url: openapi/agromonitoring-openapi.yml
        type: OpenAPI
      - url: json-schema/agromonitoring-polygon-schema.json
        type: JSONSchema
      - url: json-schema/agromonitoring-geojson-schema.json
        type: JSONSchema
      - url: json-schema/agromonitoring-satelliteimage-schema.json
        type: JSONSchema
      - url: json-schema/agromonitoring-ndvirecord-schema.json
        type: JSONSchema
      - url: json-schema/agromonitoring-vegetationstats-schema.json
        type: JSONSchema
      - url: json-schema/agromonitoring-weatherdata-schema.json
        type: JSONSchema
      - url: json-schema/agromonitoring-temperaturerange-schema.json
        type: JSONSchema
      - url: json-schema/agromonitoring-soildata-schema.json
        type: JSONSchema
      - url: json-schema/agromonitoring-uvindexdata-schema.json
        type: JSONSchema
      - url: json-schema/agromonitoring-polygoncreaterequest-schema.json
        type: JSONSchema
      - url: json-schema/agromonitoring-errorresponse-schema.json
        type: JSONSchema
      - url: json-structure/agromonitoring-polygon-structure.json
        type: JSONStructure
      - url: json-structure/agromonitoring-geojson-structure.json
        type: JSONStructure
      - url: json-structure/agromonitoring-satelliteimage-structure.json
        type: JSONStructure
      - url: json-structure/agromonitoring-ndvirecord-structure.json
        type: JSONStructure
      - url: json-structure/agromonitoring-vegetationstats-structure.json
        type: JSONStructure
      - url: json-structure/agromonitoring-weatherdata-structure.json
        type: JSONStructure
      - url: json-structure/agromonitoring-temperaturerange-structure.json
        type: JSONStructure
      - url: json-structure/agromonitoring-soildata-structure.json
        type: JSONStructure
      - url: json-structure/agromonitoring-uvindexdata-structure.json
        type: JSONStructure
      - url: json-structure/agromonitoring-polygoncreaterequest-structure.json
        type: JSONStructure
      - url: json-structure/agromonitoring-errorresponse-structure.json
        type: JSONStructure
      - url: examples/agromonitoring-polygon-example.json
        type: Example
      - url: examples/agromonitoring-geojson-example.json
        type: Example
      - url: examples/agromonitoring-satelliteimage-example.json
        type: Example
      - url: examples/agromonitoring-ndvirecord-example.json
        type: Example
      - url: examples/agromonitoring-vegetationstats-example.json
        type: Example
      - url: examples/agromonitoring-weatherdata-example.json
        type: Example
      - url: examples/agromonitoring-temperaturerange-example.json
        type: Example
      - url: examples/agromonitoring-soildata-example.json
        type: Example
      - url: examples/agromonitoring-uvindexdata-example.json
        type: Example
      - url: examples/agromonitoring-polygoncreaterequest-example.json
        type: Example
      - url: examples/agromonitoring-errorresponse-example.json
        type: Example
    description: The Agromonitoring Agro API provides satellite imagery, vegetation index time series (NDVI, EVI, DSWI, LSWI), weather data, soil conditions, and UV index for registered agricultural field polygons. Enables precision agriculture workflows including crop health monitoring, irrigation decision support, and yield optimization.
common:
  - url: https://agromonitoring.com/
    type: Portal
  - url: https://agromonitoring.com/api/
    type: Documentation
  - url: https://agromonitoring.com/api/agro/#auth
    type: GettingStarted
  - url: https://agromonitoring.com/subscriptions
    type: Pricing
  - url: https://agromonitoring.com/faq/
    type: FAQ
  - url: https://agromonitoring.com/terms/
    type: TermsOfService
  - url: https://agromonitoring.com/privacy/
    type: PrivacyPolicy
  - url: json-ld/agromonitoring-context.jsonld
    type: JSON-LD
  - url: rules/agromonitoring-spectral-rules.yml
    type: SpectralRules
  - url: vocabulary/agromonitoring-vocabulary.yaml
    type: Vocabulary
  - url: capabilities/shared/agromonitoring-api.yaml
    type: NaftikoCapability
  - url: capabilities/crop-monitoring.yaml
    type: NaftikoCapability
  - type: Features
    data:
      - name: Field Polygon Management
        description: Register, retrieve, and delete georeferenced agricultural field polygons using GeoJSON geometry
      - name: Satellite Imagery Search
        description: Search Sentinel-2 and Landsat satellite archives for cloud-free imagery over registered fields
      - name: Vegetation Index Time Series
        description: Access NDVI, EVI, EVI2, NRI, DSWI, and LSWI historical time series to track crop health and stress
      - name: Current Weather Data
        description: Real-time weather conditions including temperature, humidity, wind speed, pressure, and cloud cover
      - name: Weather Forecasting
        description: Multi-day weather forecasts to support irrigation scheduling and field operation planning
      - name: Soil Monitoring
        description: Soil temperature at surface and 10cm depth plus volumetric soil moisture content
      - name: UV Index Data
        description: Solar UV radiation index to assess sun exposure and radiation stress on crops
  - type: UseCases
    data:
      - name: Crop Health Monitoring
        description: Track vegetation index trends over the growing season to identify stress, disease, or nutrient deficiencies early
      - name: Irrigation Management
        description: Combine soil moisture, weather forecast, and NDVI data to optimize irrigation scheduling and reduce water usage
      - name: Yield Prediction
        description: Use satellite-derived vegetation indices across the growing season to build yield prediction models
      - name: Field Boundary Mapping
        description: Register precise field polygon boundaries for targeted data retrieval and zonal analysis
      - name: Precision Agriculture
        description: Apply variable-rate inputs using spatial variability data from satellite imagery and vegetation indices
      - name: Climate Risk Assessment
        description: Monitor weather extremes, drought, and soil conditions to assess climate-related agricultural risks
  - type: Integrations
    data:
      - name: OpenWeatherMap
        description: Agromonitoring uses OpenWeatherMap weather infrastructure for current and forecast data
      - name: Sentinel-2
        description: European Space Agency Sentinel-2 satellite data is a primary imagery source
      - name: Landsat
        description: NASA/USGS Landsat imagery is available as an additional satellite data source
name: Agromonitoring
tags:
  - Agriculture
  - Satellite Imagery
  - Vegetation Indices
  - Weather
  - Precision Agriculture
  - Remote Sensing
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-06'
modified: '2026-04-19'
position: Consumer
description: Agromonitoring is a technology company specializing in satellite-based agricultural monitoring. Using Sentinel-2 and Landsat imagery combined with weather and soil data, Agromonitoring provides vegetation index time series (NDVI, EVI, DSWI, LSWI), current weather, multi-day forecasts, and soil conditions for registered field polygons. The platform enables precision agriculture workflows including crop health assessment, irrigation optimization, yield prediction, and climate risk monitoring.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
