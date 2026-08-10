---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Cdc Agentic Access
  operation_count: 33
  slug: cdc-agentic-access
  summary_line: 33 operations · 20 acting
api_count: 14
apis:
- description: The CDC WONDER (Wide-ranging Online Data for Epidemiologic Research) API enables automated data queries in XML format over HTTP. Supports access to online databases covering mortality, natality, cance
  name: CDC WONDER API
  slug: cdc-wonder-api
- description: Allows querying of data from the CDC National Environmental Public Health Tracking Network. Returns JSON-formatted responses covering environmental health indicators such as air quality, water quality
  name: CDC Environmental Public Health Tracking Network API
  slug: cdc-environmental-public-health-tracking-network-api
- description: Enables CDC to offer web content to other sites and applications. Provides structured access to CDC health content including articles, health topics, media, and tools in JSON and XML formats for syndi
  name: CDC Content Syndication API
  slug: cdc-content-syndication-api
- description: 'The Public Health Information Network Vocabulary Access and Distribution System (PHIN VADS) is a web-based enterprise vocabulary system for accessing, searching, and distributing vocabularies used in '
  name: PHIN VADS API
  slug: phin-vads-api
- description: The app-notifications API from CDC — 1 operation(s) for app-notifications.
  name: CDC app-notifications API
  slug: cdc-app-notifications-api
- description: The code-systems API from CDC — 1 operation(s) for code-systems.
  name: CDC code-systems API
  slug: cdc-code-systems-api
- description: The conditions API from CDC — 2 operation(s) for conditions.
  name: CDC conditions API
  slug: cdc-conditions-api
- description: The configurations API from CDC — 15 operation(s) for configurations.
  name: CDC configurations API
  slug: cdc-configurations-api
- description: The events API from CDC — 2 operation(s) for events.
  name: CDC events API
  slug: cdc-events-api
- description: The Query API from CDC — 1 operation(s) for query.
  name: CDC Query API
  slug: cdc-query-api
- description: The Query Connector API OpenAPI 3.0 API from CDC — 1 operation(s) for query connector api openapi 3.0.
  name: CDC Query Connector API OpenAPI 3.0 API
  slug: cdc-query-connector-api-openapi-3-0-api
- description: The releases API from CDC — 1 operation(s) for releases.
  name: CDC releases API
  slug: cdc-releases-api
- description: The simulator API from CDC — 3 operation(s) for simulator.
  name: CDC simulator API
  slug: cdc-simulator-api
- description: The user API from CDC — 1 operation(s) for user.
  name: CDC user API
  slug: cdc-user-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cdc-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cdc-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://open.cdc.gov/apis.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/CDCgov
- group: auth
  title: ''
  type: Authentication
  url: https://dev.socrata.com/docs/app-tokens.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cdc.gov/other/policies.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cdc.gov/other/privacy.html
- group: other
  title: ''
  type: Licensing
  url: https://www.cdc.gov/other/policies.html#linking
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/cdc/refs/heads/main/json-ld/apis-jsonld.json
created: '2026-06-13'
description: The US Centers for Disease Control and Prevention (CDC) provides a suite of public APIs for accessing disease surveillance data, vaccination rates, health statistics, environmental public health tracking, and public health datasets. Key offerings include the CDC WONDER API for querying mortality and disease databases, the Open Data API powered by Socrata for thousands of datasets across categories such as flu vaccinations, STDs, injury, and NCHS statistics, the Environmental Public Health Tracking Network API for environmental health data, and the PHIN VADS vocabulary service for public health terminology.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cdc.png
layout: provider
modified: '2026-06-13'
name: CDC
nav: Providers
network: true
overview: 'CDC publishes 10 APIs on the [APIs.io](https://apis.io/) network, including app-notifications API, code-systems API, conditions API, and 7 more. Tagged areas include Public Health, Disease Surveillance, Vaccination, Health Statistics, and Government.


  CDC''s developer surface includes developer portal, GitHub presence, authentication, and 6 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 66
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 34.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 47.8
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 34.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 37.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cdc/refs/heads/main/screenshots/cdc-2026-06-20T174105.png
security:
- kind: domain-security
  name: Cdc Domain Security
  slug: cdc-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: cdc
tags:
- Public Health
- Disease Surveillance
- Vaccination
- Health Statistics
- Government
- Open Data
- Environmental Health
- Mortality
- CDC WONDER
website: https://open.cdc.gov/apis.html
---
