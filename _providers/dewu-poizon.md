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
  score: 8.5
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dewu-poizon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dewu-poizon-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dewu-poizon-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.poizon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open.poizon.com/doc/list/documentationDetail/15
- group: docs
  title: ''
  type: APIReference
  url: https://open.poizon.com/doc/list/apiDetail/166?openKey=1
- group: company
  title: ''
  type: Website
  url: https://dewu.com
- group: company
  title: ''
  type: Website
  url: https://www.poizon.com/
created: '2026-07-17'
description: Dewu (POIZON) is a leading Chinese online marketplace for sneakers, streetwear, luxury goods, and collectibles, distinguished by its integrated product authentication (legit-check) service that verifies items before they ship to buyers. Operated by Shanghai-based Poizon and backed by Hongshan (formerly Sequoia China), it runs both the domestic Dewu (得物) app and the global POIZON marketplace. For developers it operates the POIZON / Dewu Open Platform (open.poizon.com and open.dewu.com), a partner program that lets sellers, ISVs, and ERP integrators connect to the marketplace over an app-key plus request-signature authenticated API covering product data, pricing, catalog search, delivery modes, and vendor information.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dewu-poizon.png
layout: provider
modified: '2026-07-18'
name: Dewu (POIZON)
nav: Providers
network: true
overview: 'Dewu (POIZON) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, E-Commerce, Marketplace, and Retail.


  Dewu (POIZON)''s developer surface includes authentication, documentation, API reference, and 5 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 8.1
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dewu-poizon/refs/heads/main/screenshots/dewu-poizon-2026-07-25T211934.png
security:
- kind: authentication
  name: Dewu Poizon Authentication
  slug: dewu-poizon-authentication
  summary_line: apiKey/signature · 1 scheme
- kind: domain-security
  name: Dewu Poizon Domain Security
  slug: dewu-poizon-domain-security
  summary_line: TLSv1.2
slug: dewu-poizon
tags:
- Company
- Technology
- E-Commerce
- Marketplace
- Retail
- Sneakers
- Luxury Goods
- Authentication
- China
website: https://dewu.com
---
