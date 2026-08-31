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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'The comma connect API is a JWT-authenticated REST API for comma / openpilot users and devices. It exposes the authenticated user profile and device list, per-device operations (info, location, stats, '
  name: comma connect API
  slug: comma-connect-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commaai-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.comma.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.comma.ai
- group: docs
  title: ''
  type: APIReference
  url: https://api.comma.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://comma.ai/setup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/commaai
- group: company
  title: ''
  type: Blog
  url: https://blog.comma.ai
- group: operate
  title: ''
  type: Support
  url: https://comma.ai/support
- group: commercial
  title: ''
  type: Pricing
  url: https://comma.ai/shop
- group: commercial
  title: ''
  type: TermsOfService
  url: https://comma.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://comma.ai/terms
- group: start
  title: ''
  type: Login
  url: https://connect.comma.ai
- group: company
  title: ''
  type: Website
  url: https://comma.ai
- group: auth
  title: ''
  type: Authentication
  url: authentication/commaai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/commaai-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/commaai-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/commaai-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/commaai-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/commaai-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/commaai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/commaai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/commaai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/commaai-packages.yml
created: '2026-07-17'
description: Comma.ai builds openpilot, an open-source driver-assistance / robotics operating system that runs on comma hardware (comma 3X, comma four) and upgrades adaptive cruise control and lane centering on 300+ supported cars. Alongside the open-source stack, comma operates the comma connect cloud platform and a documented JWT-authenticated REST API (api.commadotai.com) that exposes device management, driving routes and segments, video and log access, real-time device communication via athena, comma prime billing, and turn-by-turn navigation. Backed by a16z, comma also publishes large open driving datasets (comma2k19, commaVQ) and the opendbc "Python API for your car." This profile catalogs comma's public developer surface for the API Evangelist network.
image: https://github.com/commaai.png
layout: provider
mcp_servers:
- description: ''
  name: comma connect (candidate)
  slug: comma-connect-candidate
modified: '2026-07-18'
name: Comma.ai
nav: Providers
network: true
overview: 'Comma.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Self-Driving, Robotics, and Artificial Intelligence.


  Comma.ai''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, authentication, and 16 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 31.0
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/commaai/refs/heads/main/screenshots/commaai-2026-07-25T210118.png
security:
- kind: authentication
  name: Commaai Authentication
  slug: commaai-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Commaai Domain Security
  slug: commaai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: commaai
tags:
- Company
- Automotive
- Self-Driving
- Robotics
- Artificial Intelligence
- Machine-Learning
- Open-Source
- Connected Vehicles
- Telematics
- Developer API
website: https://comma.ai
---
