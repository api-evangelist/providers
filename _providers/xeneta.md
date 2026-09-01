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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-01'
api_count: 1
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
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: xeneta-api-30 Air API
  slug: open-xeneta-air-api
- collection_type: open
  name: xeneta-api-30 Air Ocean API
  slug: open-xeneta-ocean-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/xeneta-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/xeneta-api-30-overlay.yaml
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
- description: 'Xeneta operates no official MCP server: the official MCP registry (registry.modelcontextprotocol.io) returns zero results for "xeneta", npm has no Xeneta MCP package, and the developer docs (help.xene'
  name: Xeneta MCP Server
  slug: xeneta-mcp-server
modified: '2026-07-21'
name: Xeneta
nav: Providers
network: true
overview: 'Xeneta publishes 2 APIs on the [APIs.io](https://apis.io/) network: Air API and Ocean API. Tagged areas include Freight, Shipping, Logistics, Ocean Freight, and Air Freight.


  Xeneta''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 22 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 54.4
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 22.4
  previous_composite: 44.7
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/screenshots/xeneta-2026-08-17T083005.png
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
