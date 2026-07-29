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
    asyncapi_events: false
    auth_clarity: true
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
  score: 12.6
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/daily-harvest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://daily-harvest.com/
- group: operate
  title: ''
  type: Support
  url: https://daily-harvest.com/blogs/faq
- group: company
  title: ''
  type: Blog
  url: https://daily-harvest.com/blogs/all
- group: commercial
  title: ''
  type: TermsOfService
  url: https://daily-harvest.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://daily-harvest.com/policies/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://account.daily-harvest.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/daily-harvest-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/daily-harvest-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/daily-harvest-scopes.yml
created: '2026-07-17'
description: Daily Harvest is a direct-to-consumer health food delivery company. It sells organic, ready-to-prepare frozen foods — smoothies, oat bowls, elixirs, protein, and boosters — that customers order on daily-harvest.com (a Shopify storefront) and receive shipped frozen to their door, with no subscription required. Daily Harvest is a portfolio company of Lightspeed Venture Partners. It publishes no first-party developer API; its only public programmatic surface is the Shopify Customer Account API OIDC/OAuth2 authorization layer exposed at account.daily-harvest.com.
image: https://daily-harvest.com/cdn/shop/files/DH_logo.jpg?v=1760391224
layout: provider
modified: '2026-07-18'
name: Daily Harvest
nav: Providers
network: true
overview: 'Daily Harvest is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food & Beverage, Direct-to-Consumer, E-commerce, and Food Delivery.


  Daily Harvest''s developer surface includes support, engineering blog, authentication, and 7 more developer resources.'
random_paper: 32
scopes:
- name: Daily Harvest Scopes
  scope_count: 4
  slug: daily-harvest-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 16.4
  delta: -0.7
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Daily Harvest Authentication
  slug: daily-harvest-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Daily Harvest Domain Security
  slug: daily-harvest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: daily-harvest
tags:
- Company
- Food & Beverage
- Direct-to-Consumer
- E-commerce
- Food Delivery
- Health & Wellness
- Subscription
- Shopify
website: https://daily-harvest.com/
---
