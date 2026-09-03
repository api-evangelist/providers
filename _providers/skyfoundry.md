---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: SkySpark is a native Project Haystack server. External applications integrate through the Haystack HTTP REST API, exposing operations such as about, read, hisRead, hisWrite, pointWrite, watchSub, watc
  name: SkySpark REST API (Project Haystack)
  slug: skyspark-rest-api-project-haystack
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://skyfoundry.com
- group: docs
  title: ''
  type: Documentation
  url: https://skyfoundry.com/product
- group: docs
  title: ''
  type: APIReference
  url: https://project-haystack.org/doc/docHaystack/HttpApi
- group: company
  title: ''
  type: Blog
  url: https://skyfoundry.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skyfoundry.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skyfoundry
- group: auth
  title: ''
  type: Authentication
  url: authentication/skyfoundry-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/skyfoundry-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skyfoundry-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/skyfoundry-well-known.yml
created: '2026-07-17'
description: 'SkyFoundry, founded in 2009 and headquartered in Glen Allen, Virginia, develops SkySpark, an analytics and informatics platform that connects, stores, analyzes, and visualizes data from smart devices, automation and control systems, meters, and sensors to "find what matters" in large equipment and facility datasets. SkySpark automatically detects issues, patterns, deviations, faults, and cost-reduction opportunities across intelligent buildings, industrial, agriculture, energy, government, and healthcare facilities, and has been applied to over 15,000 buildings spanning more than a billion square feet. SkySpark is a native Project Haystack server: external applications integrate through the Haystack HTTP REST API (ops such as read, hisRead, hisWrite, pointWrite, watchSub/watchPoll, eval, commit, and nav) with Zinc, JSON, Trio, and CSV data formats, and authenticate using the Haystack SCRAM (SHA-256) handshake with bearer authTokens. The company sells through a network of 140+
  OEM, systems-integrator, and value-added-distributor channel partners rather than a self-service public SaaS.'
image: https://skyfoundry.com/file/17/SkyFoundry-Logo.png
layout: provider
modified: '2026-07-21'
name: SkyFoundry
nav: Providers
network: true
overview: 'SkyFoundry publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Building Analytics, IoT, Energy Management, and Fault Detection.


  SkyFoundry''s developer surface includes documentation, API reference, engineering blog, authentication, and 6 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 14.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 21.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skyfoundry/refs/heads/main/screenshots/skyfoundry-2026-09-02T155802.png
security:
- kind: authentication
  name: Skyfoundry Authentication
  slug: skyfoundry-authentication
  summary_line: scram/http · 5 schemes
- kind: domain-security
  name: Skyfoundry Domain Security
  slug: skyfoundry-domain-security
  summary_line: TLSv1.3 · DMARC
slug: skyfoundry
tags:
- Company
- Building Analytics
- IoT
- Energy Management
- Fault Detection
- Smart Buildings
- Project Haystack
- Time Series
- Analytics
website: https://skyfoundry.com
---
