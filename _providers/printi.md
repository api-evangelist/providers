---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: Modeled catalog surface for browsing Printi's printable product lines (business cards, flyers, stationery, labels, packaging, promotional items) and their configurable options - format, paper stock, f
  name: Printi Products Catalog API
  slug: printi-products-catalog-api
- description: 'Modeled quoting surface that returns a price for a chosen product configuration - product, format, paper, finish, quantity, and delivery - mirroring the storefront''s dynamic configurator (for example '
  name: Printi Quotes and Pricing API
  slug: printi-quotes-pricing-api
- description: 'Modeled order surface for submitting an accepted quote as a print order, attaching artwork, and tracking production and delivery status. Inferred from the retired Printi developer portal and Printi''s '
  name: Printi Orders API
  slug: printi-orders-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/printi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/printi-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/printi
- group: company
  title: ''
  type: Website
  url: https://www.printi.com.br
- group: other
  title: ''
  type: Reseller
  url: https://www.printi.com.br/comprar-com-vendedor
created: '2026-07-11'
description: Printi is a Brazilian online commercial print marketplace founded in 2012 and based in Barueri / Sao Paulo, offering business cards, flyers, stationery, labels and stickers, packaging, brochures and folders, and promotional items through an online configurator that prices each job dynamically by format, paper, finish, and quantity. Printi is a Cimpress brand - Vistaprint took a minority stake in 2014 and Cimpress acquired a majority stake in 2020 - and sits in the same Cimpress portfolio as Vistaprint. Printi formerly published a public developer portal at developer.printi.com.br ("Printi API", hosted on ReadMe with a Run in Postman button) covering catalog, quoting, and order operations, but that portal is no longer resolvable and appears decommissioned. There is no live, documented, self-serve public API today; programmatic and reseller integration is now partner-gated, channeled through Cimpress's mass-customization / developer platform and Printi's "Comprar com Vendedor"
  reseller channel. The APIs below are modeled from the historical portal and observable storefront behavior - they are NOT sourced from a currently published public specification (see review.yml, endpointsModeled).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/printi.png
layout: provider
modified: '2026-07-11'
name: Printi
nav: Providers
network: true
overview: Printi publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Printing, Print on Demand, Commercial Print, Marketplace, and E-Commerce.
random_paper: 11
score:
  band: minimal
  composite: 6.5
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Printi Domain Security
  slug: printi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Printi Vulnerability Disclosure
  slug: printi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: printi
tags:
- Printing
- Print on Demand
- Commercial Print
- Marketplace
- E-Commerce
- Brazil
- Cimpress
- Partner Gated
website: https://www.printi.com.br
---
