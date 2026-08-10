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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Public OAuth2 / OpenID Connect authorization server (Ory-style) backing the Refectory (Dejbox) consumer and B2B applications. Advertises a standards-compliant OpenID discovery document with authorizat
  name: Refectory Identity (OAuth2 / OpenID Connect)
  slug: refectory-identity-oauth2-openid-connect
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dejbox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.refectory.fr/
- group: operate
  title: ''
  type: Support
  url: mailto:hello@refectory.fr
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dejbox-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dejbox-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dejbox-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dejbox-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dejbox-conformance.yml
created: '2026-07-17'
description: Dejbox is a French corporate-catering company founded in Lille in 2015 by Adrien Verhack and Vincent Dupied, acquired by the Carrefour Group in January 2020 and since rebranded as Refectory (refectory.fr). It delivers prepared, seasonal meals to employees of companies located in the peripheral zones of major French cities via a digital canteen (click-and-collect precommande before 10:30) and connected self-service fridges, controlling 100% of its value chain through its own Manufactures and a national network of 23 logistics hubs. Originally surfaced as a Partech portfolio company, it operates in Bordeaux, Grenoble, Lille, Lyon, Nantes, Paris and other French cities. Its consumer platform runs on a public OAuth2/OIDC identity server (customers.refectory.fr) and an API gateway (gateway.refectory.fr).
image: https://www.refectory.fr/_nuxt/icons/512x512.0114ee25.png
layout: provider
modified: '2026-07-18'
name: Dejbox (Refectory)
nav: Providers
network: true
overview: 'Dejbox (Refectory) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food & Agritech, Corporate Catering, Food Delivery, and B2B.


  Dejbox (Refectory)''s developer surface includes support, authentication, and 6 more developer resources.'
random_paper: 56
scopes:
- name: Dejbox Scopes
  scope_count: 3
  slug: dejbox-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: minimal
  composite: 12.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 12.1
  provenance:
    conformance: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dejbox/refs/heads/main/screenshots/dejbox-2026-07-25T211637.png
security:
- kind: authentication
  name: Dejbox Authentication
  slug: dejbox-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Dejbox Domain Security
  slug: dejbox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dejbox
tags:
- Company
- Food & Agritech
- Corporate Catering
- Food Delivery
- B2B
- France
- Meal Delivery
- OAuth2
- OpenID Connect
website: https://www.refectory.fr/
---
