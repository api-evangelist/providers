---
aid: u-s-geological-survey
url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/apis.yml
apis:
  - aid: u-s-geological-survey:earthquake-api
    name: Earthquake Notifications, Feeds, and Web Services
    tags:
      - Earthquakes
      - Seismic
      - Geoscience
    humanURL: https://earthquake.usgs.gov/earthquakes/feed/
    baseURL: https://earthquake.usgs.gov/fdsnws/event/1
    properties:
      - url: https://earthquake.usgs.gov/fdsnws/event/1/
        type: Documentation
      - url: https://earthquake.usgs.gov/earthquakes/feed/
        type: GettingStarted
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/openapi/usgs-earthquake-api-openapi.yaml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/json-schema/usgs-earthquake-api-earthquake-properties-schema.json
        type: JSONSchema
        title: Earthquake Properties Schema
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/json-ld/usgs-earthquake-api-context.jsonld
        type: JSON-LD
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/examples/usgs-earthquake-api-earthquake-properties-example.json
        type: Example
        title: Earthquake Properties Example
    description: The USGS Earthquake Hazards Program provides real-time notifications and historical earthquake data through the FDSN Event Web Service. Search the ANSS ComCat earthquake catalog by geography, time, magnitude, and depth. Responses available in GeoJSON, CSV, KML, and QuakeML formats.
  - aid: u-s-geological-survey:water-data-api
    name: USGS Water Data APIs
    tags:
      - Water
      - Hydrology
      - Streamflow
      - Groundwater
    humanURL: https://api.waterdata.usgs.gov/
    baseURL: https://api.waterdata.usgs.gov/ogcapi/v0
    properties:
      - url: https://api.waterdata.usgs.gov/docs/
        type: Documentation
      - url: https://api.waterdata.usgs.gov/signup/
        type: Authentication
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/openapi/usgs-water-data-api-openapi.yaml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/json-schema/usgs-water-data-api-monitoring-location-properties-schema.json
        type: JSONSchema
        title: Monitoring Location Schema
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/json-schema/usgs-water-data-api-time-series-properties-schema.json
        type: JSONSchema
        title: Time Series Properties Schema
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/json-ld/usgs-water-data-api-context.jsonld
        type: JSON-LD
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/examples/usgs-water-data-api-monitoring-location-properties-example.json
        type: Example
        title: Monitoring Location Example
    description: The USGS Water Data OGC APIs provide standardized access to USGS water monitoring data including continuous streamflow, daily values, groundwater levels, discrete water quality measurements, and monitoring location metadata. Implements OGC API Features standard with spatial and temporal filtering support.
  - aid: u-s-geological-survey:asset-identifier-service-ais
    name: Asset Identifier Service (AIS)
    tags:
      - Identifiers
      - Research Data
    humanURL: https://www.usgs.gov/tools/asset-identifier-service-ais
    properties:
      - url: https://www.usgs.gov/tools/asset-identifier-service-ais
        type: Documentation
    description: The USGS Asset Identifier Service (AIS) allows USGS personnel to reserve, register, publish, and manage USGS persistent identifiers to make research more Findable, Accessible, Interoperable, and Reusable (FAIR).
  - aid: u-s-geological-survey:seismic-design-web-service
    name: Seismic Design Web Service
    tags:
      - Seismic
      - Engineering
    humanURL: https://earthquake.usgs.gov/ws/designmaps/
    properties:
      - url: https://earthquake.usgs.gov/ws/designmaps/
        type: Documentation
    description: Web services produced by the U.S. Geological Survey for calculating parameter values from various seismic design reference documents for engineering and construction purposes.
  - aid: u-s-geological-survey:sciencebase
    name: ScienceBase
    tags:
      - Research Data
      - Data Repository
    humanURL: https://www.usgs.gov/tools/sciencebase
    properties:
      - url: https://www.usgs.gov/tools/sciencebase
        type: Documentation
      - url: https://www.usgs.gov/sciencebase-instructions-and-documentation/api-and-web-services
        type: Documentation
        title: ScienceBase API Documentation
    description: ScienceBase is a USGS Trusted Digital Repository that provides permission-controlled and public access to scientific data products through a REST API supporting upload, documentation, and sharing of research data.
  - aid: u-s-geological-survey:streamstats-web-services
    name: StreamStats Web Services
    tags:
      - Hydrology
      - Streamflow
      - Statistics
    humanURL: https://www.usgs.gov/tools/streamstats-web-services
    properties:
      - url: https://www.usgs.gov/tools/streamstats-web-services
        type: Documentation
    description: The StreamStats Web Services provide HTTP-accessible hydrological analysis services for delineating drainage areas, estimating peak flows, and computing basin characteristics for water resources planning.
  - aid: u-s-geological-survey:usgs-water-services
    name: USGS Water Services (Legacy)
    tags:
      - Water
      - Hydrology
      - Legacy
    humanURL: https://www.usgs.gov/tools/usgs-water-services
    properties:
      - url: https://nwis.waterservices.usgs.gov/
        type: Documentation
    description: The original USGS NWIS water services API providing streamflow, groundwater, water quality, and site information via REST protocol in XML and other media types. High availability and fault-tolerant design.
name: U.S. Geological Survey
tags:
  - Federal Government
  - Geological
  - Earth Science
  - Natural Resources
  - Earthquake
  - Water
  - Hydrology
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - type: Website
    url: https://www.usgs.gov/
  - type: GitHubOrganization
    url: https://github.com/usgs
  - type: Documentation
    url: https://www.usgs.gov/products/web-tools/apis
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/rules/usgs-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/vocabulary/u-s-geological-survey-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/capabilities/geoscience-data-access.yaml
    title: Geoscience Data Access
  - type: Features
    data:
      - name: Earthquake Catalog Query
        description: Search the USGS ANSS ComCat earthquake catalog by geography, time, magnitude, depth, and event type with 20,000 event limit per query.
      - name: Real-Time Earthquake Data
        description: Access near real-time earthquake data updated within minutes of events occurring anywhere in the world.
      - name: Water Monitoring Locations
        description: Query USGS stream gages, groundwater wells, and other water quality monitoring stations by state, watershed, or geographic area.
      - name: Water Data Time Series
        description: Retrieve continuous and daily water data including streamflow, stage, temperature, and water quality parameters.
      - name: OGC API Compliance
        description: USGS Water Data APIs implement OGC API Features standard supporting CQL2 filtering, spatial queries, and standardized output formats.
      - name: GeoJSON Output
        description: All spatial data returned in GeoJSON format compatible with mapping libraries and geospatial analysis tools.
  - type: UseCases
    data:
      - name: Earthquake Hazard Monitoring
        description: Emergency managers and scientists monitor real-time earthquake activity for hazard assessment and emergency response planning.
      - name: Flood Forecasting
        description: Hydrologists use USGS streamflow data for flood prediction, water supply forecasting, and reservoir management.
      - name: Groundwater Management
        description: Water managers track groundwater level trends for sustainable aquifer management and drought assessment.
      - name: Environmental Research
        description: Researchers use USGS geological and water data for environmental impact assessments and climate change studies.
      - name: Engineering Design
        description: Civil engineers use USGS water data and seismic design services for infrastructure planning and construction.
  - type: Integrations
    data:
      - name: USGS GitHub Organization
        description: Open-source tools including libcomcat, rcomcat, and other clients for accessing USGS earthquake and water data.
      - name: USGS Water Data for the Nation
        description: The flagship USGS water data portal at waterdata.usgs.gov providing maps and tools built on the NWIS water services API.
      - name: National Water Information System (NWIS)
        description: Legacy USGS water data system providing the underlying data for Water Data APIs with millions of site records.
      - name: FDSN Standards
        description: USGS earthquake API implements FDSN (International Federation of Digital Seismograph Networks) web service specifications.
created: '2024-11-14'
modified: '2026-05-03'
position: Consuming
description: The U.S. Geological Survey (USGS) is a scientific agency of the U.S. government that conducts research and provides data on the natural resources and hazards of the United States. The USGS is known for its work in mapping and monitoring earthquakes, volcanoes, and landslides to help mitigate risks and protect communities. USGS also studies water resources including streamflow, groundwater, and water quality through a nationwide network of monitoring stations. Their public APIs provide programmatic access to real-time earthquake data, water monitoring observations, seismic design parameters, and geospatial data products.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
