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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pepperfry-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pepperfry.com
created: '2026-07-17'
description: 'Pepperfry is an Indian online marketplace for furniture and home products, founded in 2011 and headquartered in Mumbai. It sells furniture, decor, lamps, kitchen and dining goods, furnishings, and modular home solutions to consumers across India through its website, mobile apps, and a network of physical studio showrooms. It was added to the API Evangelist network as a portfolio company of Norwest Venture Partners. An enrichment pass on 2026-07-20 found no public developer portal, API documentation, OpenAPI/GraphQL specification, SDKs, or /.well-known discovery surface: the consumer site is fully bot-protected (HTTP 403) and there is no evidence of an externally documented API program. The one artifact captured is a live domain-security probe of pepperfry.com.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pepperfry.png
layout: provider
modified: '2026-07-20'
name: Pepperfry
nav: Providers
network: true
overview: Pepperfry is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-commerce, Furniture, Home, and Retail.
random_paper: 5
score:
  band: minimal
  composite: 5.0
  delta: -1.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Pepperfry Domain Security
  slug: pepperfry-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pepperfry
tags:
- Company
- E-commerce
- Furniture
- Home
- Retail
- Marketplace
- India
website: https://pepperfry.com
---
