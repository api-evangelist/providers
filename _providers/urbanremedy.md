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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 13.5
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: Platform-provided WooCommerce Store API on urbanremedy.com, discovered live at /wp-json/wc/store/v1. Public, unauthenticated read access to the product catalog (verified 200 with product JSON); cart a
  name: Urban Remedy WooCommerce Store API
  slug: urban-remedy-woocommerce-store-api
- description: 'WordPress core REST API on urbanremedy.com, discovered live at /wp-json/wp/v2. Public JSON read access to Journal posts and site pages (verified 200). The /wp-json/ index self-describes 35 namespaces '
  name: Urban Remedy WordPress REST API
  slug: urban-remedy-wordpress-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://urbanremedy.com
- group: company
  title: ''
  type: Blog
  url: https://urbanremedy.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://urbanremedy.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://urbanremedy.com/my-account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://urbanremedy.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://urbanremedy.com/privacy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/urbanremedy-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/urbanremedy-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/urbanremedy-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/urbanremedy-domain-security.yml
created: '2026-07-17'
description: Urban Remedy is a certified B Corp organic food company founded by Neka Pasquale on the belief that food is healing. It makes fresh, organic, plant-based, ready-to-eat meals, cold pressed juices, juice cleanses, and snacks with fresh, locally sourced ingredients, delivered nationwide and sold through its own retail stores and kiosks. The company runs on WordPress + WooCommerce, exposing a live public storefront REST surface at /wp-json/ alongside its e-commerce site.
image: https://urbanremedy.com/wp-content/uploads/cropped-UR-favicon-192x192.png
layout: provider
modified: '2026-07-21'
name: Urban Remedy
nav: Providers
network: true
overview: 'Urban Remedy publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Organic, Plant-Based, and Juice.


  Urban Remedy''s developer surface includes engineering blog, support, signup flow, authentication, and 6 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 19.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Urbanremedy Authentication
  slug: urbanremedy-authentication
  summary_line: none/apiKey · 2 schemes
- kind: domain-security
  name: Urbanremedy Domain Security
  slug: urbanremedy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: urbanremedy
tags:
- Company
- Food
- Organic
- Plant-Based
- Juice
- Wellness
- eCommerce
- Retail
website: https://urbanremedy.com
---
