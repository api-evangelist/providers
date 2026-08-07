---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Aquabyte Agentic Access
  operation_count: 19
  slug: aquabyte-agentic-access
  summary_line: 19 operations · 1 acting
api_count: 1
apis:
- description: Read-only REST API over Aquabyte's aquaculture monitoring data. Version v3.1 exposes site and pen inventory plus historical and latest time-series for biomass (including harvest reports), sea-lice cou
  name: Aquabyte Public API
  slug: aquabyte-public-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.aquabyte.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api.aquabyte.ai/v3/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.aquabyte.ai/v3/docs
- group: start
  title: ''
  type: Login
  url: https://app.aquabyte.ai/login
- group: operate
  title: ''
  type: Support
  url: https://www.aquabyte.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aquabyte.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aquabyte.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aquabyte-new
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aquabyte
- group: auth
  title: ''
  type: Authentication
  url: authentication/aquabyte-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aquabyte-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aquabyte-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aquabyte-domain-security.yml
created: '2026-08-06'
description: Aquabyte AS is a Norwegian-American aquaculture technology company, founded in 2017 with offices in Bergen (Laksevåg), Norway, San Francisco and Chile, that applies computer vision and machine learning to salmon and trout farming. Underwater cameras (Hydra 360, Hammerhead, Atlas) stream imagery into a cloud platform that produces biomass and weight estimation, sea-lice counting, welfare scoring, swim-speed and breathing-index behaviour metrics, environmental readings and feeding decision support, from smolt through harvest. Customers reach that data either through the Aquabyte customer portal at app.aquabyte.ai or through the Aquabyte Public API — a documented, API-key-authenticated REST service at api.aquabyte.ai/v3 whose OpenAPI 3.1 definition is served publicly at api.aquabyte.ai/openapi.json and rendered with ReDoc at /v3/docs.
image: https://www.aquabyte.ai/en/icon-illyi6.png
layout: provider
modified: '2026-08-06'
name: Aquabyte
nav: Providers
network: true
overview: 'Aquabyte publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Aquaculture, Fish Farming, Computer Vision, Machine Learning, and Biomass Estimation.


  Aquabyte''s developer surface includes documentation, API reference, support, authentication, and 9 more developer resources.'
random_paper: 69
rate_limits:
- limit_count: 1
  name: Aquabyte Rate Limits
  slug: aquabyte-rate-limits
score:
  band: thin
  composite: 38.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 45.0
    developer_ergonomics: 30.4
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 26.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Aquabyte Authentication
  slug: aquabyte-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aquabyte Domain Security
  slug: aquabyte-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aquabyte
tags:
- Aquaculture
- Fish Farming
- Computer Vision
- Machine Learning
- Biomass Estimation
- Sea Lice
- Fish Welfare
- Environmental Monitoring
- Agriculture Technology
- Norway
- Salmon
- Data
website: https://www.aquabyte.ai/
---
