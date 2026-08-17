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
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.honest.com/
- group: company
  title: ''
  type: Blog
  url: https://www.honest.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.honest.com/pages/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.honest.com/pages/terms-of-service
- group: start
  title: ''
  type: Login
  url: https://www.honest.com/account/login
- group: agent
  title: ''
  type: WellKnown
  url: well-known/the-honest-company-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-honest-company-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/the-honest-company-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-honest-company-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-honest-company-domain-security.yml
created: '2026-07-17'
description: The Honest Company is a consumer-goods brand selling baby, personal-care, beauty, and household products through its direct-to-consumer storefront at honest.com and through major retailers. It was surfaced in the API Evangelist network as a portfolio company of iconiq-capital, ivp, and lightspeed-venture-partners. The honest.com storefront runs on Shopify and does not publish a first-party developer API; the only machine-readable API surface discoverable on the domain is Shopify's Customer Account API (OIDC/OAuth2) advertised via the store's /.well-known/ discovery documents. This profile captures that authentication surface, the domain security posture, and the storefront's public web properties.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-honest-company.png
layout: provider
modified: '2026-07-21'
name: The Honest Company
nav: Providers
network: true
overview: 'The Honest Company is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Consumer Goods, Ecommerce, and Retail.


  The Honest Company''s developer surface includes engineering blog, authentication, and 8 more developer resources.'
random_paper: 39
scopes:
- name: The Honest Company Scopes
  scope_count: 4
  slug: the-honest-company-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 15.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 50.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 15.9
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: The Honest Company Authentication
  slug: the-honest-company-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: The Honest Company Domain Security
  slug: the-honest-company-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-honest-company
tags:
- Company
- Consumer
- Consumer Goods
- Ecommerce
- Retail
- Baby
- Personal Care
- Shopify
website: https://www.honest.com/
---
