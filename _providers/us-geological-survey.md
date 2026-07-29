---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Us Geological Survey Agentic Access
  operation_count: 13
  slug: us-geological-survey-agentic-access
  summary_line: 13 operations
api_count: 12
apis:
- description: The USGS ScienceBase Catalog API provides access to USGS scientific data management infrastructure, enabling upload, documentation, sharing, and dynamic data services for USGS research datasets and sc
  name: USGS ScienceBase Catalog API
  slug: sciencebase-api
- description: The USGS Geomagnetism Web Service provides programmatic access to geomagnetic data collected by USGS magnetic observatories across the United States and territories, supporting navigation, space weath
  name: USGS Geomagnetism Web Service
  slug: geomagnetism-api
- description: The USGS Seismic Design Data Web Services provide parameter values from seismic design reference documents for building and infrastructure design, supporting compliance with ASCE 7 and other engineeri
  name: USGS Seismic Design Data Web Services
  slug: seismic-design-api
- description: The USGS National Map services provide geospatial data and elevation products via OGC web services, REST APIs, and download services covering topographic data, imagery, hydrography, boundaries, transp
  name: USGS National Map Services
  slug: national-map-api
- description: OGC API collection discovery
  name: US Geological Survey Collections API
  slug: us-geological-survey-collections-api
- description: Real-time and historical continuous sensor measurements
  name: US Geological Survey Continuous Values API
  slug: us-geological-survey-continuous-values-api
- description: Daily summary water data
  name: US Geological Survey Daily Values API
  slug: us-geological-survey-daily-values-api
- description: Earthquake catalog query and count operations
  name: US Geological Survey Earthquakes API
  slug: us-geological-survey-earthquakes-api
- description: Physically measured values from site visits
  name: US Geological Survey Field Measurements API
  slug: us-geological-survey-field-measurements-api
- description: API metadata and discovery operations
  name: US Geological Survey Metadata API
  slug: us-geological-survey-metadata-api
- description: Geographic and metadata for USGS monitoring stations
  name: US Geological Survey Monitoring Locations API
  slug: us-geological-survey-monitoring-locations-api
- description: Metadata about time series observations
  name: US Geological Survey Time Series Metadata API
  slug: us-geological-survey-time-series-metadata-api
artifact_total: 26
collections:
- collection_type: open
  name: USGS Earthquake Catalog API
  slug: open-usgs-earthquake-catalog
- collection_type: open
  name: USGS Water Data OGC API
  slug: open-usgs-water-data
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/us-geological-survey-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-geological-survey-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/us-geological-survey-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usgs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usgs
created: '2024-12-03'
description: The US Geological Survey is a scientific agency of the United States government that conducts research on the natural resources, natural hazards, and environmental health of the United States. The USGS is responsible for monitoring and assessing the country's water, energy, mineral, and biological resources, as well as investigating geological hazards such as earthquakes, volcanoes, landslides, and floods. USGS provides a broad portfolio of public REST APIs covering earthquake data, water resources, geomagnetism, mapping, seismic design, and scientific data catalogs - all available without cost as US Government works.
examples:
- key_count: 3
  name: Usgs Earthquake Query Example
  slug: usgs-earthquake-query-example
finops:
- name: Us Geological Survey Finops
  service_category: Government Open Data
  slug: us-geological-survey-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-geological-survey.png
json_schemas:
- name: USGS Earthquake Feature
  property_count: 4
  slug: usgs-earthquake-feature
json_structures:
- name: Usgs Earthquake Feature Structure
  property_count: 0
  slug: usgs-earthquake-feature-structure
jsonld:
- class_count: 22
  name: Us Geological Survey Context
  property_count: 6
  slug: us-geological-survey-context
layout: provider
modified: '2026-05-19'
name: US Geological Survey
nav: Providers
network: true
overview: 'US Geological Survey publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Continuous Values API, Daily Values API, and 5 more. Tagged areas include Federal Government, Earth Science, Earthquakes, Water Data, and Geospatial.


  The US Geological Survey catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  US Geological Survey''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Us Geological Survey Plans Pricing
  plan_count: 1
  slug: us-geological-survey-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Us Geological Survey Rate Limits
  slug: us-geological-survey-rate-limits
rules:
- name: US Geological Survey API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: us-geological-survey-jsonschema-spectral-rules
- name: US Geological Survey API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 4
    warn: 4
  slug: usgs-earthquake-api-rules
score:
  band: thin
  composite: 40.0
  delta: -3.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.6
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-geological-survey/refs/heads/main/screenshots/us-geological-survey-2026-06-20T200630.png
security:
- kind: authentication
  name: Us Geological Survey Authentication
  slug: us-geological-survey-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Us Geological Survey Domain Security
  slug: us-geological-survey-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: us-geological-survey
tags:
- Federal Government
- Earth Science
- Earthquakes
- Water Data
- Geospatial
- Hazards
- Environment
---
