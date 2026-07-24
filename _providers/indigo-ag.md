---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: Soil-carbon program that enrolls growers, captures on-farm management practice data, and uses Indigo's MRV engine to quantify and verify soil organic-carbon outcomes that are sold as carbon credits to
  name: Carbon by Indigo
  slug: carbon-program
- description: Scope-3 supply-chain program for consumer goods and biofuel companies. Designs and runs grower programs aligned with the GHG Protocol, collects and verifies field-level data via Indigo's MRV engine, a
  name: Source by Indigo
  slug: source
- description: Indigo's portfolio of microbial seed and foliar treatments, sold to growers and ag retailers. Product line, not an API; included so the apis.yml reflects Indigo's complete commercial surface.
  name: biotrinsic Microbial Treatments
  slug: biotrinsic
- description: On-farm seed-treatment application hardware used to apply biotrinsic products to seed prior to planting. Hardware product, not an API.
  name: CLIPS Seed-Treatment Device
  slug: clips-device
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/indigo-ag-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.indigoag.com/
- group: other
  title: ''
  type: GrowerApp
  url: https://app.indigoag.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/indigo-ag
- group: company
  title: ''
  type: News
  url: https://www.indigoag.com/news
- group: company
  title: ''
  type: Blog
  url: https://www.indigoag.com/blog
- group: operate
  title: ''
  type: Contact
  url: https://www.indigoag.com/contact
created: '2026-05-23'
description: 'Indigo Agriculture is a Boston-based agriculture-technology company combining microbial seed and foliar treatments (biotrinsic) and on-farm seed treatment hardware (CLIPS) with two large supply-chain programs: Carbon by Indigo, a soil-carbon program that pays growers for verified carbon credits using Indigo''s proprietary measurement, reporting, and verification (MRV) stack; and Source by Indigo, a Scope-3 program that connects consumer-goods buyers to sustainably grown crops with greenhouse-gas, water, and low-carbon-biofuel outcome reporting. Indigo does not publish a public developer portal; partner and supply-chain integrations are negotiated directly through their team.'
finops:
- name: Indigo Ag Finops
  service_category: API
  slug: indigo-ag-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/indigo-ag.png
layout: provider
modified: '2026-05-23'
name: Indigo Agriculture
nav: Providers
network: true
overview: 'Indigo Agriculture publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, AgTech, Microbials, Soil Carbon, and MRV.


  Indigo Agriculture''s developer surface includes GitHub presence, product news, engineering blog, and 4 more developer resources.'
plans:
- name: Indigo Ag Plans Pricing
  plan_count: 1
  slug: indigo-ag-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Indigo Ag Rate Limits
  slug: indigo-ag-rate-limits
score:
  band: emerging
  composite: 19.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/indigo-ag/refs/heads/main/screenshots/indigo-ag-2026-06-20T183318.png
security:
- kind: domain-security
  name: Indigo Ag Domain Security
  slug: indigo-ag-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: indigo-ag
tags:
- Agriculture
- AgTech
- Microbials
- Soil Carbon
- MRV
- Scope 3
- Sustainability
website: https://www.indigoag.com/
---
