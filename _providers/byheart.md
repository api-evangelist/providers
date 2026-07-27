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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 25.0
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.byheart.com
- group: start
  title: ''
  type: SignUp
  url: https://byheart.com/account/login
- group: start
  title: ''
  type: Login
  url: https://byheart.com/account/login
- group: operate
  title: ''
  type: Support
  url: https://byheart.com/pages/byheart-faqs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://byheart.com/pages/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://byheart.com/pages/terms-and-conditions
- group: agent
  title: ''
  type: WellKnown
  url: well-known/byheart-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/byheart-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/byheart-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/byheart-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/byheart-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/byheart-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/byheart-domain-security.yml
created: '2026-07-17'
description: ByHeart is a US infant-nutrition company founded in 2016 that makes Whole Nutrition Infant Formula, marketed on the promise of better science, better ingredients, and better quality. It sells direct-to-consumer through a Shopify storefront at byheart.com as well as through retail. The company ran its own clinical program and built its own manufacturing. In November 2025 ByHeart recalled all batches after Clostridium botulinum contamination linked to infant-botulism cases and paused production pending FDA clearance to resume. ByHeart is a portfolio company of D1 Capital. It publishes no first-party developer API; its only machine-discoverable surface is the Shopify Customer Account API (OpenID Connect / OAuth 2.0) advertised under its domain.
image: https://www.byheart.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: byheart-mcp.yml
  slug: byheart-mcpyml
modified: '2026-07-18'
name: ByHeart
nav: Providers
network: true
overview: 'ByHeart is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Infant Nutrition, Baby Formula, and Direct-to-Consumer.


  ByHeart''s developer surface includes signup flow, support, authentication, and 10 more developer resources.'
random_paper: 3
scopes:
- name: Byheart Scopes
  scope_count: 4
  slug: byheart-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 27.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 27.0
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 76.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Byheart Authentication
  slug: byheart-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Byheart Domain Security
  slug: byheart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: byheart
tags:
- Company
- Consumer
- Infant Nutrition
- Baby Formula
- Direct-to-Consumer
- Ecommerce
- Health
- Shopify
website: https://www.byheart.com
---
