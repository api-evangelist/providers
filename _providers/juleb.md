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
api_count: 1
apis:
- description: Juleb's REST API for the health/retail/distribution platform, documented at docs.juleb.com. Documented resource surface spans inventory (batch, picking, product, product-template), point of sale (conf
  name: Juleb API
  slug: juleb-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/juleb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://juleb.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.juleb.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.juleb.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/juleb-lifecycle.yml
- group: company
  title: ''
  type: Blog
  url: https://juleb.com/blog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/juleb-llms.txt
created: '2026-07-17'
description: Juleb is a Saudi Arabia-based pharma-tech and retail software company providing an integrated cloud platform for the health, retail, and distribution sectors. Its suite spans accounting and financial management, inventory and warehouse management, sales force automation (SFA), point of sale (POS), Rx e-prescription, e-commerce, and DSCSA regulatory compliance. Juleb connects to Saudi compliance systems (ZATCA/Fatoora, RSD, GS1, Wasfaty), e-commerce channels (Salla, Shopify, HungerStation), payment providers (Geidea, Alhamrani), and ERPs (Microsoft Dynamics). Founded by Yousuf Jamjoom and backed by 500 Global, Juleb exposes a REST API (documented at docs.juleb.com) covering inventory, point of sale, prescriptions, and partner/company resources.
image: https://juleb.com/icons/icon-512x512.png
layout: provider
modified: '2026-07-19'
name: Juleb
nav: Providers
network: true
overview: 'Juleb publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Retail, Distribution, and Pharmacy.


  Juleb''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
random_paper: 68
score:
  band: minimal
  composite: 11.2
  delta: -2.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 13.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/juleb/refs/heads/main/screenshots/juleb-2026-07-25T223303.png
security:
- kind: domain-security
  name: Juleb Domain Security
  slug: juleb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: juleb
tags:
- Company
- Health
- Retail
- Distribution
- Pharmacy
- Point of Sale
- Inventory
- E-Prescription
- ERP
- Saudi Arabia
- Compliance
website: https://juleb.com
---
