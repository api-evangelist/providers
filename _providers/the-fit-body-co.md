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
  url: security/the-fit-body-co-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/the-fit-body-co-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-fit-body-co-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/the-fit-body-co-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://fitbody.mx
created: '2026-07-17'
description: The Fit Body Co (Fitbody) is a Mexican direct-to-consumer sports nutrition and dietary supplements brand selling isolated and hydrolyzed protein powders, creatine, vitamins, and wellness products, along with digital recipe guides, through a Shopify-based online storefront at fitbody.mx. It is a portfolio company of 500 Global. As an e-commerce retail brand it publishes no public developer API, developer portal, SDK, or API documentation; this API Evangelist profile captures its company identity and domain-security posture rather than an API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-fit-body-co.png
layout: provider
modified: '2026-07-21'
name: The Fit Body Co
nav: Providers
network: true
overview: 'The Fit Body Co is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports Nutrition, Dietary Supplements, E-Commerce, and Health and Wellness.


  The Fit Body Co''s developer surface includes authentication and 4 more developer resources.'
random_paper: 12
scopes:
- name: The Fit Body Co Scopes
  scope_count: 4
  slug: the-fit-body-co-scopes
  summary_line: 4 scopes
score:
  band: emerging
  composite: 11.1
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 36.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: The Fit Body Co Authentication
  slug: the-fit-body-co-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: The Fit Body Co Domain Security
  slug: the-fit-body-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-fit-body-co
tags:
- Company
- Sports Nutrition
- Dietary Supplements
- E-Commerce
- Health and Wellness
- Consumer Products
- Mexico
- Shopify
website: https://fitbody.mx
---
