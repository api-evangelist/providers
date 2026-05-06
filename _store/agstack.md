---
aid: agstack
url: https://raw.githubusercontent.com/api-evangelist/agstack/refs/heads/main/apis.yml
apis:
  - aid: agstack:openagri-weather-service
    name: OpenAgri Weather Service
    tags:
      - Agriculture
      - Weather
      - Open Source
      - Linux Foundation
    humanURL: https://github.com/agstack/OpenAgri-WeatherService
    properties:
      - url: https://github.com/agstack/OpenAgri-WeatherService
        type: Documentation
      - url: https://github.com/agstack/OpenAgri-WeatherService/blob/main/README.md
        type: GettingStarted
      - url: openapi/agstack-openagri-weather-service-openapi.yml
        type: OpenAPI
      - url: json-schema/agstack-openagri-weather-service-predictionout-schema.json
        type: JSONSchema
      - url: json-schema/agstack-openagri-weather-service-weatherdataout-schema.json
        type: JSONSchema
      - url: json-schema/agstack-openagri-weather-service-thidataout-schema.json
        type: JSONSchema
      - url: json-schema/agstack-openagri-weather-service-sprayforecastresponse-schema.json
        type: JSONSchema
      - url: json-schema/agstack-openagri-weather-service-flightstatusforecastresponse-schema.json
        type: JSONSchema
      - url: json-schema/agstack-openagri-weather-service-geojsonout-schema.json
        type: JSONSchema
      - url: json-schema/agstack-openagri-weather-service-jsonldgraph-schema.json
        type: JSONSchema
      - url: json-schema/agstack-openagri-weather-service-authtoken-schema.json
        type: JSONSchema
      - url: json-schema/agstack-openagri-weather-service-pointout-schema.json
        type: JSONSchema
      - url: json-schema/agstack-openagri-weather-service-validationerror-schema.json
        type: JSONSchema
      - url: json-schema/agstack-openagri-weather-service-httpvalidationerror-schema.json
        type: JSONSchema
      - url: json-schema/agstack-openagri-weather-service-body-token-auth-token-post-schema.json
        type: JSONSchema
      - url: json-structure/agstack-openagri-weather-service-predictionout-structure.json
        type: JSONStructure
      - url: json-structure/agstack-openagri-weather-service-weatherdataout-structure.json
        type: JSONStructure
      - url: json-structure/agstack-openagri-weather-service-thidataout-structure.json
        type: JSONStructure
      - url: json-structure/agstack-openagri-weather-service-sprayforecastresponse-structure.json
        type: JSONStructure
      - url: json-structure/agstack-openagri-weather-service-flightstatusforecastresponse-structure.json
        type: JSONStructure
      - url: json-structure/agstack-openagri-weather-service-geojsonout-structure.json
        type: JSONStructure
      - url: json-structure/agstack-openagri-weather-service-jsonldgraph-structure.json
        type: JSONStructure
      - url: json-structure/agstack-openagri-weather-service-authtoken-structure.json
        type: JSONStructure
      - url: json-structure/agstack-openagri-weather-service-pointout-structure.json
        type: JSONStructure
      - url: json-structure/agstack-openagri-weather-service-validationerror-structure.json
        type: JSONStructure
      - url: json-structure/agstack-openagri-weather-service-httpvalidationerror-structure.json
        type: JSONStructure
      - url: json-structure/agstack-openagri-weather-service-body-token-auth-token-post-structure.json
        type: JSONStructure
      - url: examples/agstack-openagri-weather-service-predictionout-example.json
        type: Example
      - url: examples/agstack-openagri-weather-service-weatherdataout-example.json
        type: Example
      - url: examples/agstack-openagri-weather-service-thidataout-example.json
        type: Example
      - url: examples/agstack-openagri-weather-service-sprayforecastresponse-example.json
        type: Example
      - url: examples/agstack-openagri-weather-service-flightstatusforecastresponse-example.json
        type: Example
      - url: examples/agstack-openagri-weather-service-geojsonout-example.json
        type: Example
      - url: examples/agstack-openagri-weather-service-jsonldgraph-example.json
        type: Example
      - url: examples/agstack-openagri-weather-service-authtoken-example.json
        type: Example
      - url: examples/agstack-openagri-weather-service-pointout-example.json
        type: Example
      - url: examples/agstack-openagri-weather-service-validationerror-example.json
        type: Example
      - url: examples/agstack-openagri-weather-service-httpvalidationerror-example.json
        type: Example
      - url: examples/agstack-openagri-weather-service-body-token-auth-token-post-example.json
        type: Example
    description: FastAPI-based weather service providing 5-day forecasts, current conditions, Temperature-Humidity Index (THI) for livestock heat stress, UAV flight condition forecasts, and spray condition assessments. Supports both JSON and JSON-LD/OCSM output formats for linked data interoperability. Part of the OpenAgri EU Horizon Europe project.
  - aid: agstack:openagri-farm-calendar
    name: OpenAgri Farm Calendar
    tags:
      - Agriculture
      - Farm Management
      - Open Source
      - Linux Foundation
    humanURL: https://github.com/agstack/OpenAgri-FarmCalendar
    properties:
      - url: https://github.com/agstack/OpenAgri-FarmCalendar
        type: Documentation
      - url: https://github.com/agstack/OpenAgri-FarmCalendar/blob/main/README.md
        type: GettingStarted
      - url: openapi/agstack-openagri-farm-calendar-openapi.yml
        type: OpenAPI
    description: Django REST API for digital farm calendar management. Records farmer operations (planting, spraying, harvesting, irrigation), farm observations, parcel properties, and farm assets. Provides data in both JSON and JSON-LD formats conforming to the OpenAgri Common Semantic Model (OCSM). Part of the OpenAgri EU Horizon Europe project.
  - aid: agstack:asset-registry
    name: AgStack Asset Registry
    tags:
      - Agriculture
      - Geospatial
      - Open Source
      - Linux Foundation
    humanURL: https://github.com/agstack/asset-registry
    properties:
      - url: https://github.com/agstack/asset-registry
        type: Documentation
      - url: https://api-ar.agstack.org
        type: APIReference
      - url: openapi/agstack-asset-registry-openapi.yml
        type: OpenAPI
      - url: json-schema/agstack-asset-registry-registerfieldwktrequest-schema.json
        type: JSONSchema
      - url: json-schema/agstack-asset-registry-geojsonfeaturecollection-schema.json
        type: JSONSchema
      - url: json-schema/agstack-asset-registry-bulkpointresult-schema.json
        type: JSONSchema
      - url: json-structure/agstack-asset-registry-registerfieldwktrequest-structure.json
        type: JSONStructure
      - url: json-structure/agstack-asset-registry-geojsonfeaturecollection-structure.json
        type: JSONStructure
      - url: json-structure/agstack-asset-registry-bulkpointresult-structure.json
        type: JSONStructure
      - url: examples/agstack-asset-registry-registerfieldwktrequest-example.json
        type: Example
      - url: examples/agstack-asset-registry-geojsonfeaturecollection-example.json
        type: Example
      - url: examples/agstack-asset-registry-bulkpointresult-example.json
        type: Example
    description: The AgStack Asset Registry provides global field boundary registration and identification. Submit a field polygon (WKT or GeoJSON) and receive a permanent 256-bit (16-character alphanumeric) geo ID. Supports single and bulk registration, field retrieval, centroid calculation, and spatial overlap analysis. Production API available at api-ar.agstack.org.
common:
  - url: https://agstack.org/
    type: Portal
  - url: https://agstack.org/projects/
    type: Documentation
  - url: https://github.com/agstack
    type: GitHubOrganization
  - url: https://agstack.org/about/
    type: About
  - url: https://lfaidata.foundation/
    type: About
    title: Linux Foundation AI and Data
  - url: json-ld/agstack-context.jsonld
    type: JSON-LD
  - url: rules/agstack-spectral-rules.yml
    type: SpectralRules
  - url: vocabulary/agstack-vocabulary.yaml
    type: Vocabulary
  - url: capabilities/shared/agstack-openagri-weather-service-api.yaml
    type: NaftikoCapability
  - url: capabilities/shared/agstack-asset-registry-api.yaml
    type: NaftikoCapability
  - url: capabilities/precision-agriculture.yaml
    type: NaftikoCapability
  - type: Features
    data:
      - name: Field Boundary Registry
        description: Global registry for agricultural field boundaries — submit WKT or GeoJSON geometry, receive a permanent unique 16-character geo ID
      - name: Agricultural Weather Intelligence
        description: 5-day weather forecasts, current conditions, and agricultural indicators including THI, spray conditions, and UAV flight suitability
      - name: Digital Farm Calendar
        description: Record and manage farm operations (planting, irrigation, spraying, harvesting) with linked data (JSON-LD/OCSM) output
      - name: Linked Data Support
        description: All APIs support JSON-LD output conforming to the OpenAgri Common Semantic Model (OCSM) for semantic interoperability
      - name: EUDR Compliance Support
        description: Tools for EU Deforestation Regulation compliance — field boundary registration and supply chain traceability via INATrace
      - name: Irrigation Management
        description: Evapotranspiration (ETo) calculations and soil moisture analysis for data-driven irrigation decisions
      - name: Open Source Infrastructure
        description: All tools are Apache-2.0 licensed, Docker-ready, and deployable on any cloud or on-premises infrastructure
  - type: UseCases
    data:
      - name: Farmer Field Registration
        description: Farmers and agri-cooperatives register field boundaries in the global asset registry to enable data-driven farm management
      - name: Crop Protection Planning
        description: Check spray conditions and UAV flight forecasts before applying pesticides or fertilizers to minimize drift and maximize efficacy
      - name: Livestock Heat Stress Monitoring
        description: Monitor Temperature-Humidity Index to detect and prevent heat stress events in dairy and beef cattle herds
      - name: EUDR Supply Chain Compliance
        description: Register plot geolocations and trace agricultural commodities through the supply chain to demonstrate zero-deforestation compliance
      - name: Precision Irrigation
        description: Use evapotranspiration data and soil moisture analysis to schedule irrigation and optimize water usage
      - name: Interoperable Agtech Integration
        description: Share agricultural data between platforms using JSON-LD/OCSM linked data format for semantic interoperability
  - type: Integrations
    data:
      - name: OpenWeatherMap
        description: Weather data source for current conditions and forecasts used by the OpenAgri Weather Service
      - name: OpenAgri
        description: EU Horizon Europe project (Grant No. 101134083) that funds and drives the OpenAgri microservices ecosystem
      - name: OCSM
        description: OpenAgri Common Semantic Model — linked data vocabulary for agricultural interoperability used across all OpenAgri APIs
      - name: INATrace
        description: Open-source blockchain-based track and trace system for agricultural supply chains
      - name: TerraTrac
        description: TechnoServe Labs mobile and web application for EUDR compliance field data collection integrated with the asset registry
name: AgStack Foundation
tags:
  - Agriculture
  - Linux Foundation
  - Open Source
  - Geospatial
  - Precision Agriculture
  - Linked Data
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-16'
modified: '2026-04-19'
position: Consumer
description: AgStack Foundation is a Linux Foundation project providing open-source digital infrastructure for the agriculture sector. Key projects include the Asset Registry (global field boundary registration with unique geo IDs), the OpenAgri Weather Service (agricultural weather forecasts, THI, spray conditions, UAV flight forecasts), and the OpenAgri Farm Calendar (farm operation recording with JSON-LD/OCSM linked data support). AgStack tools support EUDR compliance, precision agriculture, and interoperability across the agtech ecosystem through the OpenAgri Common Semantic Model.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
