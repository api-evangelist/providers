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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: HTTPS event-ingestion API for streaming batches of newline-delimited JSON, OpenRTB 2.5-based ad-tech event records (e.g. MmxAuctionSummary) to the Metamarkets platform for near-real-time dashboarding.
  name: Metamarkets Real-Time Data Ingestion (RDI) API
  slug: metamarkets-real-time-data-ingestion-rdi-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metamarkets-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamarkets.com/docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.metamarkets.com/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metamx
- group: operate
  title: ''
  type: Support
  url: mailto:support@metamarkets.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metamarkets-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/metamarkets-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/metamarkets-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/metamarkets-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metamarkets-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/metamarkets-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/metamarkets-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/metamarkets-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/metamarkets-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/metamarkets-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/metamarkets-components.yml
created: '2026-07-17'
description: Metamarkets built a real-time analytics platform for the programmatic advertising industry, giving ad exchanges, DSPs, SSPs, and publishers an interactive dashboard over billions of daily bid, impression, and spend events. Its Real-Time Data Ingestion (RDI) platform ingests well-formatted, standards-based ad-tech event data (adhering to OpenRTB 2.5, IAB guidelines, and ISO date/country/language/currency standards) over an authenticated HTTPS streaming endpoint and surfaces it in the Metamarkets dashboard within seconds for querying and analysis. Metamarkets was acquired by Snap Inc. in 2017; the primary metamarkets.com site is now defunct, but the legacy developer documentation for the RDI platform remains live at docs.metamarkets.com. Surfaced as a portfolio company of Anthemis and profiled in the API Evangelist network.
image: https://files.readme.io/7e7ea7f-small-MMX-logo.png
layout: provider
modified: '2026-07-20'
name: Metamarkets
nav: Providers
network: true
overview: 'Metamarkets publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Analytics, and Real Time.


  Metamarkets'' developer surface includes documentation, getting-started guide, support, CLI, authentication, sandbox, and 10 more developer resources.'
random_paper: 48
rate_limits:
- limit_count: 0
  name: Metamarkets Rate Limits
  slug: metamarkets-rate-limits
score:
  band: emerging
  composite: 21.7
  delta: 0.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 20.8
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Metamarkets Authentication
  slug: metamarkets-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Metamarkets Domain Security
  slug: metamarkets-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metamarkets
tags:
- Company
- Advertising
- AdTech
- Analytics
- Real Time
- Data Ingestion
- Programmatic Advertising
- OpenRTB
- Business Intelligence
---
