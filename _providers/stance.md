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
- group: company
  title: ''
  type: Website
  url: https://stance.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stance.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stance.com/policies/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://stance.com/pages/contact-us
- group: company
  title: ''
  type: Blog
  url: https://stance.com/blogs/news
- group: start
  title: ''
  type: Login
  url: https://stance.com/account/login
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stance-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stance-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/stance-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stance-domain-security.yml
created: '2026-07-17'
description: Stance is a direct-to-consumer apparel brand best known for expressive, performance-oriented socks, plus underwear and related apparel sold under the "Feel good, do good" tagline. The company operates a Shopify-hosted online storefront at stance.com with licensed collaborations (MLB, NBA, Disney, and others). Stance publishes no developer product API; its only public machine-facing surface is the Shopify Customer Account API (OpenID Connect / OAuth 2.0) exposed for customer sign-in at account.stance.com. It was surfaced in the API Evangelist network as a portfolio company of Bond Capital and Shasta Ventures and enriched from live probes of its public well-known discovery documents and storefront pages.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stance.png
layout: provider
modified: '2026-07-21'
name: Stance
nav: Providers
network: true
overview: 'Stance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Apparel, Retail, E-commerce, and Socks.


  Stance''s developer surface includes support, engineering blog, authentication, and 7 more developer resources.'
random_paper: 22
scopes:
- name: Stance Scopes
  scope_count: 4
  slug: stance-scopes
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
  name: Stance Authentication
  slug: stance-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Stance Domain Security
  slug: stance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stance
tags:
- Company
- Apparel
- Retail
- E-commerce
- Socks
- Direct-to-Consumer
- Shopify
website: https://stance.com
---
