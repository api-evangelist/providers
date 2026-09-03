---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: 'The AVEVA CONNECT cloud platform REST APIs provide access to industrial data services including account management, identity management, data ingress pipelines, data views, and time-series retrieval. '
  name: AVEVA CONNECT REST API
  slug: aveva-connect-rest-api
- description: The AVEVA PI System REST API (PI Web API) provides RESTful HTTP access to time- series sensor data, asset metadata, and event frames stored in PI Server. Supports GET, POST, PUT, PATCH, and DELETE ope
  name: AVEVA PI System REST API
  slug: aveva-pi-system-rest-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/aveva-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aveva-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aveva-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aveva.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aveva.com/
- group: company
  title: ''
  type: Blog
  url: https://www.aveva.com/en/perspectives/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aveva
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@AVEVASoftware
- group: company
  title: ''
  type: About
  url: https://www.aveva.com/en/about/
- group: operate
  title: ''
  type: Support
  url: https://www.aveva.com/en/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aveva.com/en/contact/
- group: company
  title: ''
  type: Newsroom
  url: https://www.aveva.com/en/perspectives/news/
created: '2026-06-05'
description: AVEVA is an industrial software company (a subsidiary of Schneider Electric) providing engineering, operations, and data management software for energy, utilities, marine, and manufacturing industries. AVEVA's product portfolio includes System Platform (unified SCADA/MES/IIoT), Plant SCADA, MES, Edge, PI System (industrial data infrastructure), and CONNECT cloud services, all of which expose REST APIs for industrial data integration, asset management, and operational analytics.
graphqls:
- description: 'AVEVA provides engineering and industrial software including PI System, SCADA, and MES solutions. Their API covers process data historian (PI), asset framework, event frames, analytics, manufacturing '
  name: AVEVA GraphQL API
  slug: aveva-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aveva.png
jsonld:
- class_count: 3
  name: Aveva Context
  property_count: 25
  slug: aveva-context
layout: provider
modified: '2026-06-05'
name: AVEVA
nav: Providers
network: true
overview: 'AVEVA publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include SCADA, MES, Industrial Automation, Manufacturing, and Industrial IoT.


  The AVEVA catalog on APIs.io includes 1 JSON-LD context.


  AVEVA''s developer surface includes documentation, engineering blog, YouTube channel, support, pricing, and 7 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 6
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 45.7
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 28.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 29.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aveva/refs/heads/main/screenshots/aveva-2026-06-20T172722.png
security:
- kind: domain-security
  name: Aveva Domain Security
  slug: aveva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aveva Vulnerability Disclosure
  slug: aveva-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Aveva Trust Center
  slug: aveva-trust-center
  summary_line: trust center published
slug: aveva
tags:
- SCADA
- MES
- Industrial Automation
- Manufacturing
- Industrial IoT
- IIoT
- Industrial Data
- Energy
website: https://www.aveva.com
---
