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
  scored_at: '2026-09-04'
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
overview: 'Daily Harvest is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Direct to Consumer, E-Commerce, and Food Delivery.


  Daily Harvest''s developer surface includes support, engineering blog, authentication, and 7 more developer resources.'
random_paper: 18
scopes:
- name: Daily Harvest Scopes
  scope_count: 4
  slug: daily-harvest-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/daily-harvest/refs/heads/main/screenshots/daily-harvest-2026-08-07T164023.png
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
- Food and Beverage
- Direct to Consumer
- E-Commerce
- Food Delivery
- Health and Wellness
- Subscription
- Shopify
website: https://daily-harvest.com/
---
