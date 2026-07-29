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
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/helprnow-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/helprnow-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://giftr.my
- group: start
  title: ''
  type: Login
  url: https://giftr.my/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://giftr.my/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://giftr.my/policies/privacy-policy
created: '2026-07-17'
description: HelprNow (operating as Giftr, by Helpr Asia) is Malaysia's leading online gift marketplace, helping people improve relationships with loved ones through a seamless gifting experience. It delivers flowers, cakes, balloons, chocolates, personalised gifts, hampers and gift cards with same-day and nationwide delivery options. The storefront runs on Shopify (helpr-asia.myshopify.com), so its public technical surface is a consumer commerce site rather than a developer API program; the only machine-discoverable interfaces are Shopify's customer-account OAuth2/OpenID Connect endpoints served under giftr.my/.well-known/. Backed by 500 Global; profiled in the API Evangelist network as a portfolio lead.
image: https://cdn.shopify.com/s/files/1/1428/2106/files/Giftr_Logo_Social_Media_Sharing_-_1200_X_628.jpg?v=1624515691
layout: provider
modified: '2026-07-19'
name: HelprNow
nav: Providers
network: true
overview: HelprNow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gifting, E-commerce, Retail, and Marketplace.
random_paper: 32
score:
  band: emerging
  composite: 13.0
  delta: -0.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Helprnow Domain Security
  slug: helprnow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: helprnow
tags:
- Company
- Gifting
- E-commerce
- Retail
- Marketplace
- Malaysia
- Shopify
- Flowers
website: https://giftr.my
---
