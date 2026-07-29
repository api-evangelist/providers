---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Wmo Agentic Access
  operation_count: 21
  slug: wmo-agentic-access
  summary_line: 21 operations · 4 acting
api_count: 9
apis:
- description: The WMO World Weather Information Service (WWIS) provides public JSON endpoints delivering official city weather forecasts and climatological data contributed by WMO member national meteorological and
  name: World Weather Information Service API
  slug: world-weather-information-service-api
- description: The OSCAR/Surface REST API provides programmatic access to the WMO Observing Systems Capability Analysis and Review tool for surface-based stations. The public GET endpoints enable search and retrieva
  name: OSCAR/Surface REST API
  slug: oscar-surface-api
- description: The WIS2 Global Broker provides an MQTT(S) publish-subscribe service that re-publishes real-time weather notification messages from all WIS2 Nodes worldwide. Subscribers connect using MQTTS on port 88
  name: WIS2 Global Broker (MQTT)
  slug: wis2-global-broker-mqtt-api
- description: The WMO Hydrological Observing System (WHOS) provides multiple API interfaces for accessing global hydrological station data and time series. Available services include a REST/JSON DAB Observation and
  name: WHOS Hydrological Observing System API
  slug: whos-hydrological-api
- description: The jobs API from World Meteorological Organization — 3 operation(s) for jobs.
  name: World Meteorological Organization jobs API
  slug: wmo-jobs-api
- description: The pywcmp-wis2-wcmp2-ets API from World Meteorological Organization — 2 operation(s) for pywcmp-wis2-wcmp2-ets.
  name: World Meteorological Organization pywcmp-wis2-wcmp2-ets API
  slug: wmo-pywcmp-wis2-wcmp2-ets-api
- description: The pywcmp-wis2-wcmp2-kpi API from World Meteorological Organization — 2 operation(s) for pywcmp-wis2-wcmp2-kpi.
  name: World Meteorological Organization pywcmp-wis2-wcmp2-kpi API
  slug: wmo-pywcmp-wis2-wcmp2-kpi-api
- description: Meteorological Service of Canada Global Discovery Catalogue (GDC)
  name: World Meteorological Organization server API
  slug: wmo-server-api
- description: WIS2 discovery metadata
  name: World Meteorological Organization wis2-discovery-metadata API
  slug: wmo-wis2-discovery-metadata-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wmo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wmo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wmo.int/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/World-Meteorological-Organization
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wmo-im
- group: operate
  title: ''
  type: Community
  url: https://community.wmo.int/
- group: start
  title: ''
  type: Portal
  url: https://wmo.int/activities/type-of-activity/exchange-data
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wis2box.wis.wmo.int/en/latest/
- group: other
  title: ''
  type: SevereWeatherAlerts
  url: https://severeweather.wmo.int/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/WMO
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/world-meteorological-organization-wmo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://worldweather.wmo.int/en/dataguide.html
created: '2024-01-01'
description: The World Meteorological Organization (WMO) is a specialized agency of the United Nations that coordinates global meteorological, climatological, hydrological, and related geophysical sciences. WMO provides public REST APIs for weather data, climate observation metadata, hydrological monitoring, severe weather alerts, and the WIS2 global meteorological information exchange system enabling real-time access to earth system data from member nations worldwide.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wmo.png
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: World Meteorological Organization
nav: Providers
network: true
overview: 'World Meteorological Organization publishes 5 APIs on the [APIs.io](https://apis.io/) network, including jobs API, pywcmp-wis2-wcmp2-ets API, pywcmp-wis2-wcmp2-kpi API, and 2 more. Tagged areas include Weather, Climate, Hydrology, Meteorology, and International Organization.


  The World Meteorological Organization catalog on APIs.io includes 1 JSON-LD context.


  World Meteorological Organization''s developer surface includes developer portal, documentation, and 10 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 15
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 35.8
  delta: -2.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 59.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 27.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wmo/refs/heads/main/screenshots/wmo-2026-06-20T201531.png
security:
- kind: domain-security
  name: Wmo Domain Security
  slug: wmo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wmo
tags:
- Weather
- Climate
- Hydrology
- Meteorology
- International Organization
- United Nations
- Open Data
website: https://wmo.int/
---
