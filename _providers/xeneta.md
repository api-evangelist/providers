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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-08-03'
api_count: 3
apis:
- description: Airline reports API (Selfie) serving rates, chargeable weight, load factor, and capacity reports as CSV files in ZIP archives. Airlines use a branded host (https://{airline}.useselfie.com/api/selfie/v
  name: Xeneta Airline Data API
  slug: xeneta-airline-data-api
- description: The Air API from Xeneta — 1 operation(s) for air.
  name: Xeneta Air API
  slug: xeneta-air-api
- description: The Ocean API from Xeneta — 13 operation(s) for ocean.
  name: Xeneta Ocean API
  slug: xeneta-ocean-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xeneta-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xeneta-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.xeneta.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.xeneta.com/reference
- group: docs
  title: ''
  type: Documentation
  url: https://help.xeneta.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://help.xeneta.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.xeneta.com/reference/api
- group: operate
  title: ''
  type: Support
  url: https://help.xeneta.com/
- group: company
  title: ''
  type: Blog
  url: https://www.xeneta.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xeneta
- group: start
  title: ''
  type: Login
  url: https://app.xeneta.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xeneta.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xeneta.com/xeneta-privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.xeneta.com/xeneta-data-security
- group: auth
  title: ''
  type: TrustCenter
  url: security/xeneta-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/xeneta-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/xeneta-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/xeneta-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xeneta-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/xeneta-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/xeneta-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/xeneta-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://help.xeneta.com/reference/versioning
- group: design
  title: ''
  type: Conventions
  url: conventions/xeneta-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/xeneta-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/xeneta-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Xeneta is an ocean and air freight rate benchmarking and market analytics platform headquartered in Oslo, Norway. It crowdsources contracted freight rates from shippers and forwarders into the world's largest rate database, and its REST API (v3.0) exposes ocean and air market rates, your own contracted prices, carrier spread, estimated rates, capacity, carbon emissions, and schedule reliability data, plus a separate airline reports API for airlines, shippers, and freight forwarders.
image: https://files.readme.io/f8b1664-xeneta-favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: xeneta-mcp.yml
  slug: xeneta-mcpyml
modified: '2026-07-21'
name: Xeneta
nav: Providers
network: true
overview: 'Xeneta publishes 2 APIs on the [APIs.io](https://apis.io/) network: Air API and Ocean API. Tagged areas include Freight, Shipping, Logistics, Ocean Freight, and Air Freight.


  Xeneta''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 20 more developer resources.'
random_paper: 75
score:
  band: developing
  composite: 51.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 62.0
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 28.9
  previous_composite: 51.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 50.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Xeneta Authentication
  slug: xeneta-authentication
  summary_line: apiKey/sessionCookie · 2 schemes
- kind: domain-security
  name: Xeneta Domain Security
  slug: xeneta-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Xeneta Trust Center
  slug: xeneta-trust-center
  summary_line: ISO 27001:2022
slug: xeneta
tags:
- Freight
- Shipping
- Logistics
- Ocean Freight
- Air Freight
- Benchmarking
- Market Data
- Supply Chain
- Rates
- Emissions
website: https://www.xeneta.com/
---
