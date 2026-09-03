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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: REST API for third-party sellers and integrators to connect to the KaBuM! marketplace (operated on the Mirakl platform). Covers category hierarchies, product attribute mapping, product and offer impor
  name: KaBuM! Marketplace Seller Integration API
  slug: kabum-marketplace-seller-integration-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.kabum.com.br/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.kabum.com.br/hotsite/documentacao-hubscore/
- group: docs
  title: ''
  type: Documentation
  url: https://www.kabum.com.br/hotsite/documentacao-hubscore/
- group: start
  title: ''
  type: SignUp
  url: https://marketplace-kabum.mirakl.net/login
- group: operate
  title: ''
  type: Support
  url: https://www.kabum.com.br/atendimento
- group: company
  title: ''
  type: Blog
  url: https://www.kabum.com.br/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kabum.com.br/termos-de-uso
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kabum.com.br/privacidade
- group: auth
  title: ''
  type: Authentication
  url: authentication/kabum-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kabum-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/kabum-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kabum-domain-security.yml
created: '2026-07-17'
description: KaBuM! is the largest e-commerce retailer of technology, computer hardware, electronics, and games in Latin America, headquartered in Limeira, Brazil and part of the Magalu (Magazine Luiza) group. Beyond its consumer storefront, KaBuM! operates a third-party seller marketplace on the Mirakl platform and publishes an integration guide for sellers and integrators to connect their ERP/OMS to the marketplace via a REST API — managing product catalog, attribute mapping, offers (price/stock), order retrieval, shipping carriers, document uploads, and tracking/ship confirmation. Authentication is API-key based, write operations are expected to be idempotent, and integrations poll asynchronous import jobs by id. This profile was added to the API Evangelist network from a VC portfolio lead and enriched from KaBuM!'s public integration documentation.
image: https://logo.clearbit.com/kabum.com.br
layout: provider
modified: '2026-07-19'
name: KaBum!
nav: Providers
network: true
overview: 'KaBum! publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Marketplace, and Technology.


  KaBum!''s developer surface includes documentation, signup flow, support, engineering blog, authentication, and 7 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kabum/refs/heads/main/screenshots/kabum-2026-07-25T223359.png
security:
- kind: authentication
  name: Kabum Authentication
  slug: kabum-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kabum Domain Security
  slug: kabum-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kabum
tags:
- Company
- E-Commerce
- Retail
- Marketplace
- Technology
- Electronics
- Games
- Brazil
- Seller Integration
- Mirakl
website: https://www.kabum.com.br/
---
