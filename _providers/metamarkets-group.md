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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: HTTPS event-stream ingestion API for programmatic advertising data. Customers continuously POST newline-delimited, OpenRTB-based JSON event records (gzip-compressed) to a per-customer HTTPS endpoint u
  name: Metamarkets Real-Time Data Ingestion (RDI) API
  slug: metamarkets-real-time-data-ingestion-rdi-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metamarkets-group-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamarkets.com/docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.metamarkets.com/docs/getting-started
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metamarkets-group-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/metamarkets-group-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/metamarkets-group-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metamarkets-group-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/metamarkets-group-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/metamarkets-group-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/metamarkets-group-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/metamarkets-group-well-known.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metamx
created: '2026-07-17'
description: Metamarkets was a real-time analytics platform for programmatic advertising, giving ad exchanges, SSPs, DSPs, and ad networks interactive dashboards over billions of daily bid, impression, click, and spend events. Its Real-time Data Ingestion (RDI) API accepted continuous streams of OpenRTB-based JSON event records over authenticated HTTPS POST, surfacing them in the Metamarkets dashboard within seconds. Founded in 2010 and the birthplace of the Druid analytics database (now Apache Druid), Metamarkets was acquired by Snap Inc. in 2017; its successor products live on as Rill Data. This profile enriches the dcvc portfolio lead from the surviving public documentation at docs.metamarkets.com.
image: https://files.readme.io/7e7ea7f-small-MMX-logo.png
layout: provider
modified: '2026-07-20'
name: Metamarkets Group
nav: Providers
network: true
overview: 'Metamarkets Group publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Analytics, and Programmatic Advertising.


  Metamarkets Group''s developer surface includes documentation, getting-started guide, authentication, sandbox, and 8 more developer resources.'
random_paper: 145
score:
  band: emerging
  composite: 15.3
  delta: -1.7
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 36.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 17.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metamarkets-group/refs/heads/main/screenshots/metamarkets-group-2026-08-07T172649.png
security:
- kind: authentication
  name: Metamarkets Group Authentication
  slug: metamarkets-group-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Metamarkets Group Domain Security
  slug: metamarkets-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metamarkets-group
tags:
- Company
- Advertising
- AdTech
- Analytics
- Programmatic Advertising
- Real-Time Data
- Data Ingestion
- OpenRTB
- Dashboards
---
