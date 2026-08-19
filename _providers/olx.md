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
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.1
  scored_at: '2026-08-19'
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
  name: olx-mcp.yml
  slug: olx-mcpyml
modified: '2026-07-20'
name: OLX
nav: Providers
network: true
overview: 'OLX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Marketplace, Classifieds, and Ecommerce.


  OLX''s developer surface includes documentation, API reference, authentication, and 10 more developer resources.'
random_paper: 41
score:
  band: emerging
  composite: 17.0
  delta: -0.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 17.5
  provenance:
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
- Ecommerce
- Automotive
- Real Estate
- Partner API
website: https://www.olx.com/
---
