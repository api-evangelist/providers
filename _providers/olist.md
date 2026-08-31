---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://olist.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://olist.com/programa-de-parceiros/parceiros-tech/
- group: start
  title: ''
  type: SignUp
  url: https://parceiros.olist.com/login
- group: operate
  title: ''
  type: Support
  url: https://ajuda.olist.com/
- group: company
  title: ''
  type: Blog
  url: https://olist.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://olist.com/precos/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/olist
- group: agent
  title: ''
  type: WellKnown
  url: well-known/olist-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/olist-domain-security.yml
created: '2026-07-17'
description: Olist is a Brazilian commerce technology company headquartered in Curitiba, Paraná, offering an integrated ecosystem of solutions that automate business management for online sellers. Its products include an ERP for inventory, invoicing and order automation, a multi-marketplace Integration Hub (Mercado Livre, TikTok Shop and others), a POS for physical stores, a digital account with Pix payments, shipping and fulfillment (Envios), and storefront creation. Olist exposes robust partner APIs through its Technology Partner program ("Parceiro Tecnológico"), where approved developers receive test credentials and Swagger documentation to build and homologate integrations reaching 60,000+ merchants. The public API surface is gated behind partner registration; no open developer portal or OpenAPI specification is published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/olist.png
layout: provider
modified: '2026-07-20'
name: Olist
nav: Providers
network: true
overview: 'Olist is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Marketplace, Payments, and Logistics.


  Olist''s developer surface includes signup flow, support, engineering blog, pricing, and 5 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/olist/refs/heads/main/screenshots/olist-2026-08-07T190120.png
security:
- kind: domain-security
  name: Olist Domain Security
  slug: olist-domain-security
  summary_line: TLSv1.3 · DMARC
slug: olist
tags:
- Company
- E-Commerce
- Marketplace
- Payments
- Logistics
- ERP
- Brazil
- Commerce
- Integration
website: https://olist.com
---
