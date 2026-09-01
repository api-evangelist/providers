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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: OAuth2 partner API for OLX Poland (olx.pl) that lets integrators manage classified adverts (list, create, update), read category attributes, and read delivery settings. Bearer-token authenticated; OLX
  name: OLX Poland Partner API
  slug: olx-poland-partner-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.olx.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.olx.pl/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.olx.pl/api/doc
- group: docs
  title: ''
  type: APIReference
  url: https://developer.olx.pl/api/doc
- group: auth
  title: ''
  type: Authentication
  url: authentication/olx-authentication.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/olx-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/olx-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/olx-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.olx.com.br/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/olx-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/olx-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/olx-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/olx-llms.txt
created: '2026-07-17'
description: OLX is a global online classifieds and marketplace operator, part of OLX Group (owned by Prosus / Naspers), running consumer buy-and-sell marketplaces across 30+ countries under 20+ brands including OLX Poland (olx.pl), OLX Brazil (olx.com.br), OLX Portugal, OLX Bulgaria and OLX Romania, spanning general classifieds, motors/autos, and real estate. OLX Poland publishes a public Partner API (OAuth2) that lets integrators and sellers manage adverts, categories/attributes, and delivery settings programmatically. Surfaced as a portfolio company of Bessemer Venture Partners and General Catalyst and enriched into the API Evangelist network.
image: https://www.olx.pl/app/static/media/olx-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: OLX MCP Server
  slug: olx-mcp-server
modified: '2026-07-20'
name: OLX
nav: Providers
network: true
overview: 'OLX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Marketplace, Classifieds, and E-Commerce.


  OLX''s developer surface includes documentation, API reference, authentication, and 10 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 15.9
  provenance:
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/olx/refs/heads/main/screenshots/olx-2026-08-07T190129.png
security:
- kind: authentication
  name: Olx Authentication
  slug: olx-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Olx Domain Security
  slug: olx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Olx Vulnerability Disclosure
  slug: olx-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: olx
tags:
- Company
- Consumer
- Marketplace
- Classifieds
- E-Commerce
- Automotive
- Real-Estate
- Partner API
website: https://www.olx.com/
---
