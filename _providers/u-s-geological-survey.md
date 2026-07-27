---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: U S Geological Survey Agentic Access
  operation_count: 11
  slug: u-s-geological-survey-agentic-access
  summary_line: 11 operations
api_count: 11
apis:
- description: The USGS Asset Identifier Service (AIS) allows USGS personnel to reserve, register, publish, and manage USGS persistent identifiers to make research more Findable, Accessible, Interoperable, and Reusa
  name: Asset Identifier Service (AIS)
  slug: asset-identifier-service-ais
- description: Web services produced by the U.S. Geological Survey for calculating parameter values from various seismic design reference documents for engineering and construction purposes.
  name: Seismic Design Web Service
  slug: seismic-design-web-service
- description: ScienceBase is a USGS Trusted Digital Repository that provides permission-controlled and public access to scientific data products through a REST API supporting upload, documentation, and sharing of r
  name: ScienceBase
  slug: sciencebase
- description: The StreamStats Web Services provide HTTP-accessible hydrological analysis services for delineating drainage areas, estimating peak flows, and computing basin characteristics for water resources plann
  name: StreamStats Web Services
  slug: streamstats-web-services
- description: The original USGS NWIS water services API providing streamflow, groundwater, water quality, and site information via REST protocol in XML and other media types. High availability and fault-tolerant de
  name: USGS Water Services (Legacy)
  slug: usgs-water-services
- description: Discover available catalogs, contributors, and supported parameter values.
  name: U.S. Geological Survey Catalog API
  slug: u-s-geological-survey-catalog-api
- description: OGC API collections listing and metadata.
  name: U.S. Geological Survey Collections API
  slug: u-s-geological-survey-collections-api
- description: Query and retrieve earthquake event data from the USGS earthquake catalog.
  name: U.S. Geological Survey Earthquakes API
  slug: u-s-geological-survey-earthquakes-api
- description: USGS stream gages, groundwater wells, and other water monitoring stations.
  name: U.S. Geological Survey Monitoring Locations API
  slug: u-s-geological-survey-monitoring-locations-api
- description: Reference code tables including agency codes, datum types, and aquifer data.
  name: U.S. Geological Survey Reference Data API
  slug: u-s-geological-survey-reference-data-api
- description: Continuous and daily value water data from USGS monitoring locations.
  name: U.S. Geological Survey Time Series Data API
  slug: u-s-geological-survey-time-series-data-api
artifact_total: 92
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/u-s-geological-survey-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/u-s-geological-survey-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/u-s-geological-survey-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/u-s-geological-survey-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usgs
- group: company
  title: ''
  type: Website
  url: https://www.usgs.gov/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usgs
- group: docs
  title: ''
  type: Documentation
  url: https://www.usgs.gov/products/web-tools/apis
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/rules/usgs-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/vocabulary/u-s-geological-survey-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://www.usgs.gov/news/news-releases/all-news-releases
created: '2024-11-14'
description: The U.S. Geological Survey (USGS) is a scientific agency of the U.S. government that conducts research and provides data on the natural resources and hazards of the United States. The USGS is known for its work in mapping and monitoring earthquakes, volcanoes, and landslides to help mitigate risks and protect communities. USGS also studies water resources including streamflow, groundwater, and water quality through a nationwide network of monitoring stations. Their public APIs provide programmatic access to real-time earthquake data, water monitoring observations, seismic design parameters, and geospatial data products.
examples:
- key_count: 2
  name: Usgs Earthquake Api Count Response Example
  slug: usgs-earthquake-api-count-response-example
- key_count: 4
  name: Usgs Earthquake Api Earthquake Feature Collection Example
  slug: usgs-earthquake-api-earthquake-feature-collection-example
- key_count: 4
  name: Usgs Earthquake Api Earthquake Feature Example
  slug: usgs-earthquake-api-earthquake-feature-example
- key_count: 2
  name: Usgs Earthquake Api Earthquake Geometry Example
  slug: usgs-earthquake-api-earthquake-geometry-example
- key_count: 8
  name: Usgs Earthquake Api Earthquake Metadata Example
  slug: usgs-earthquake-api-earthquake-metadata-example
- key_count: 22
  name: Usgs Earthquake Api Earthquake Properties Example
  slug: usgs-earthquake-api-earthquake-properties-example
- key_count: 4
  name: Usgs Water Data Api Collection Example
  slug: usgs-water-data-api-collection-example
- key_count: 1
  name: Usgs Water Data Api Collections List Example
  slug: usgs-water-data-api-collections-list-example
- key_count: 2
  name: Usgs Water Data Api Error Response Example
  slug: usgs-water-data-api-error-response-example
- key_count: 4
  name: Usgs Water Data Api Feature Collection Example
  slug: usgs-water-data-api-feature-collection-example
- key_count: 3
  name: Usgs Water Data Api Landing Page Example
  slug: usgs-water-data-api-landing-page-example
- key_count: 4
  name: Usgs Water Data Api Link Example
  slug: usgs-water-data-api-link-example
- key_count: 4
  name: Usgs Water Data Api Monitoring Location Collection Example
  slug: usgs-water-data-api-monitoring-location-collection-example
- key_count: 3
  name: Usgs Water Data Api Monitoring Location Feature Example
  slug: usgs-water-data-api-monitoring-location-feature-example
- key_count: 9
  name: Usgs Water Data Api Monitoring Location Properties Example
  slug: usgs-water-data-api-monitoring-location-properties-example
- key_count: 4
  name: Usgs Water Data Api Time Series Collection Example
  slug: usgs-water-data-api-time-series-collection-example
- key_count: 2
  name: Usgs Water Data Api Time Series Feature Example
  slug: usgs-water-data-api-time-series-feature-example
- key_count: 7
  name: Usgs Water Data Api Time Series Properties Example
  slug: usgs-water-data-api-time-series-properties-example
features:
- description: Search the USGS ANSS ComCat earthquake catalog by geography, time, magnitude, depth, and event type with 20,000 event limit per query.
  name: Earthquake Catalog Query
- description: Access near real-time earthquake data updated within minutes of events occurring anywhere in the world.
  name: Real-Time Earthquake Data
- description: Query USGS stream gages, groundwater wells, and other water quality monitoring stations by state, watershed, or geographic area.
  name: Water Monitoring Locations
- description: Retrieve continuous and daily water data including streamflow, stage, temperature, and water quality parameters.
  name: Water Data Time Series
- description: USGS Water Data APIs implement OGC API Features standard supporting CQL2 filtering, spatial queries, and standardized output formats.
  name: OGC API Compliance
- description: All spatial data returned in GeoJSON format compatible with mapping libraries and geospatial analysis tools.
  name: GeoJSON Output
finops:
- name: U S Geological Survey Finops
  service_category: Public Open Data
  slug: u-s-geological-survey-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/u-s-geological-survey.png
integrations:
- description: Open-source tools including libcomcat, rcomcat, and other clients for accessing USGS earthquake and water data.
  name: USGS GitHub Organization
- description: The flagship USGS water data portal at waterdata.usgs.gov providing maps and tools built on the NWIS water services API.
  name: USGS Water Data for the Nation
- description: Legacy USGS water data system providing the underlying data for Water Data APIs with millions of site records.
  name: National Water Information System (NWIS)
- description: USGS earthquake API implements FDSN (International Federation of Digital Seismograph Networks) web service specifications.
  name: FDSN Standards
json_schemas:
- name: CountResponse
  property_count: 2
  slug: usgs-earthquake-api-count-response
- name: EarthquakeFeatureCollection
  property_count: 4
  slug: usgs-earthquake-api-earthquake-feature-collection
- name: EarthquakeFeature
  property_count: 4
  slug: usgs-earthquake-api-earthquake-feature
- name: EarthquakeGeometry
  property_count: 2
  slug: usgs-earthquake-api-earthquake-geometry
- name: EarthquakeMetadata
  property_count: 8
  slug: usgs-earthquake-api-earthquake-metadata
- name: EarthquakeProperties
  property_count: 22
  slug: usgs-earthquake-api-earthquake-properties
- name: Collection
  property_count: 4
  slug: usgs-water-data-api-collection
- name: CollectionsList
  property_count: 1
  slug: usgs-water-data-api-collections-list
- name: ErrorResponse
  property_count: 2
  slug: usgs-water-data-api-error-response
- name: FeatureCollection
  property_count: 4
  slug: usgs-water-data-api-feature-collection
- name: LandingPage
  property_count: 3
  slug: usgs-water-data-api-landing-page
- name: Link
  property_count: 4
  slug: usgs-water-data-api-link
- name: MonitoringLocationCollection
  property_count: 4
  slug: usgs-water-data-api-monitoring-location-collection
- name: MonitoringLocationFeature
  property_count: 3
  slug: usgs-water-data-api-monitoring-location-feature
- name: MonitoringLocationProperties
  property_count: 9
  slug: usgs-water-data-api-monitoring-location-properties
- name: TimeSeriesCollection
  property_count: 4
  slug: usgs-water-data-api-time-series-collection
- name: TimeSeriesFeature
  property_count: 2
  slug: usgs-water-data-api-time-series-feature
- name: TimeSeriesProperties
  property_count: 7
  slug: usgs-water-data-api-time-series-properties
json_structures:
- name: Usgs Earthquake Api Count Response Structure
  property_count: 2
  slug: usgs-earthquake-api-count-response-structure
- name: Usgs Earthquake Api Earthquake Feature Collection Structure
  property_count: 4
  slug: usgs-earthquake-api-earthquake-feature-collection-structure
- name: Usgs Earthquake Api Earthquake Feature Structure
  property_count: 4
  slug: usgs-earthquake-api-earthquake-feature-structure
- name: Usgs Earthquake Api Earthquake Geometry Structure
  property_count: 2
  slug: usgs-earthquake-api-earthquake-geometry-structure
- name: Usgs Earthquake Api Earthquake Metadata Structure
  property_count: 8
  slug: usgs-earthquake-api-earthquake-metadata-structure
- name: Usgs Earthquake Api Earthquake Properties Structure
  property_count: 22
  slug: usgs-earthquake-api-earthquake-properties-structure
- name: Usgs Water Data Api Collection Structure
  property_count: 4
  slug: usgs-water-data-api-collection-structure
- name: Usgs Water Data Api Collections List Structure
  property_count: 1
  slug: usgs-water-data-api-collections-list-structure
- name: Usgs Water Data Api Error Response Structure
  property_count: 2
  slug: usgs-water-data-api-error-response-structure
- name: Usgs Water Data Api Feature Collection Structure
  property_count: 4
  slug: usgs-water-data-api-feature-collection-structure
- name: Usgs Water Data Api Landing Page Structure
  property_count: 3
  slug: usgs-water-data-api-landing-page-structure
- name: Usgs Water Data Api Link Structure
  property_count: 4
  slug: usgs-water-data-api-link-structure
- name: Usgs Water Data Api Monitoring Location Collection Structure
  property_count: 4
  slug: usgs-water-data-api-monitoring-location-collection-structure
- name: Usgs Water Data Api Monitoring Location Feature Structure
  property_count: 3
  slug: usgs-water-data-api-monitoring-location-feature-structure
- name: Usgs Water Data Api Monitoring Location Properties Structure
  property_count: 9
  slug: usgs-water-data-api-monitoring-location-properties-structure
- name: Usgs Water Data Api Time Series Collection Structure
  property_count: 4
  slug: usgs-water-data-api-time-series-collection-structure
- name: Usgs Water Data Api Time Series Feature Structure
  property_count: 2
  slug: usgs-water-data-api-time-series-feature-structure
- name: Usgs Water Data Api Time Series Properties Structure
  property_count: 7
  slug: usgs-water-data-api-time-series-properties-structure
jsonld:
- class_count: 6
  name: Usgs Earthquake Api Context
  property_count: 35
  slug: usgs-earthquake-api-context
- class_count: 12
  name: Usgs Water Data Api Context
  property_count: 30
  slug: usgs-water-data-api-context
layout: provider
modified: '2026-05-19'
name: U.S. Geological Survey
nav: Providers
network: true
overview: 'U.S. Geological Survey publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Collections API, Earthquakes API, and 3 more. Tagged areas include Federal Government, Geological, Earth Science, Natural Resources, and Earthquake.


  The U.S. Geological Survey catalog on APIs.io includes 2 JSON-LD contexts and 3 Spectral governance rulesets.


  U.S. Geological Survey''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: U S Geological Survey Plans Pricing
  plan_count: 1
  slug: u-s-geological-survey-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 2
  name: U S Geological Survey Rate Limits
  slug: u-s-geological-survey-rate-limits
rules:
- name: U.S. Geological Survey API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: u-s-geological-survey-jsonschema-spectral-rules
- name: U.S. Geological Survey API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: u-s-geological-survey-spectral-rules
- name: U.S. Geological Survey API Rules
  rule_count: 33
  severity_counts:
    error: 9
    hint: 0
    info: 10
    warn: 14
  slug: usgs-spectral-rules
score:
  band: developing
  composite: 51.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 73.2
    developer_ergonomics: 21.7
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 26.3
  previous_composite: 51.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/u-s-geological-survey/refs/heads/main/screenshots/u-s-geological-survey-2026-06-20T195914.png
security:
- kind: authentication
  name: U S Geological Survey Authentication
  slug: u-s-geological-survey-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: U S Geological Survey Domain Security
  slug: u-s-geological-survey-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: U S Geological Survey Vulnerability Disclosure
  slug: u-s-geological-survey-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: u-s-geological-survey
tags:
- Federal Government
- Geological
- Earth Science
- Natural Resources
- Earthquake
- Water
- Hydrology
use_cases:
- description: Emergency managers and scientists monitor real-time earthquake activity for hazard assessment and emergency response planning.
  name: Earthquake Hazard Monitoring
- description: Hydrologists use USGS streamflow data for flood prediction, water supply forecasting, and reservoir management.
  name: Flood Forecasting
- description: Water managers track groundwater level trends for sustainable aquifer management and drought assessment.
  name: Groundwater Management
- description: Researchers use USGS geological and water data for environmental impact assessments and climate change studies.
  name: Environmental Research
- description: Civil engineers use USGS water data and seismic design services for infrastructure planning and construction.
  name: Engineering Design
website: https://www.usgs.gov/
---
