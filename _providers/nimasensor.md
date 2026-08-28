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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nimasensor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nimanow.com
- group: company
  title: ''
  type: Blog
  url: https://nimanow.com/blogs/blog
- group: operate
  title: ''
  type: Support
  url: https://nimanow.com/pages/faqs
- group: start
  title: ''
  type: Login
  url: https://nimanow.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nimanow.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nimanow.com/policies/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nimasensor-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nimasensor-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/nimasensor-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nimasensor-scopes.yml
created: '2026-07-17'
description: NIMA (originally 6SensorLabs, founded by MIT alumni Shireen Yates and Scott Sundvor) makes a portable, consumer-use gluten detection sensor for people living with celiac disease and gluten sensitivity. A pea-sized food sample is loaded into a single-use capsule, inserted into the handheld NIMA Sensor, and returns a clear result in about three minutes, detecting gluten down to 10 ppm. The product relaunched in 2025-2026 with investment from RA Capital Management, pairing a next-generation sensor with newly engineered test capsules and the NIMA Now app. NIMA is a consumer hardware and e-commerce company (storefront hosted on Shopify), not a developer-API provider - it exposes no first-party public developer API. It is tracked in the API Evangelist network as a portfolio company of Uncork Capital.
image: https://nimanow.com/cdn/shop/files/BMC00138-Edit-Edit_6c2e82b0-d6ef-401f-87c0-d8e28987afae.jpg
layout: provider
modified: '2026-07-20'
name: NimaSensor
nav: Providers
network: true
overview: 'NimaSensor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Consumer Hardware, Food Safety, and Gluten.


  NimaSensor''s developer surface includes engineering blog, support, authentication, and 8 more developer resources.'
random_paper: 16
scopes:
- name: Nimasensor Scopes
  scope_count: 4
  slug: nimasensor-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 20.3
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 46.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nimasensor/refs/heads/main/screenshots/nimasensor-2026-08-07T185314.png
security:
- kind: authentication
  name: Nimasensor Authentication
  slug: nimasensor-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Nimasensor Domain Security
  slug: nimasensor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nimasensor
tags:
- Company
- Health
- Consumer Hardware
- Food Safety
- Gluten
- Celiac
- E-Commerce
- IoT
website: https://nimanow.com
---
