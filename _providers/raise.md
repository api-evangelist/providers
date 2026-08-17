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
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'The Raise Commerce API (business/v2) — browse gift card brands and categories, purchase fixed- and variable-load gift cards, retrieve and act on individual cards (balance check, mark redeemed, update '
  name: Raise Commerce API
  slug: raise-commerce-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/raise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.raise.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.raise.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.raise.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.raise.com/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.raise.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@raise.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.raise.com/business/privacy-policy/
- group: build
  title: ''
  type: Packages
  url: packages/raise-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/raise-llms.txt
created: '2026-07-17'
description: Raise is a digital gift card marketplace and commerce platform. Raise for Business exposes the Raise Commerce API — a REST/JSON API that lets partners programmatically browse a catalog of retailer gift card brands, purchase fixed- and variable-load gift cards, check and manage card balances, and reconcile transactions and commissions across 180+ currencies and many countries. Authentication is OAuth 2.0 bearer tokens (server-to-server client credentials, plus app/web auth with SR25519/RSA key pairs, SMS, or TOTP). The API uses a JSON:API-style data envelope, page-based pagination, request metadata, and client_order_id idempotency. Prior investors include Accel, PayPal, and NEA.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/raise.png
layout: provider
mcp_servers:
- description: ''
  name: raise-mcp.yml
  slug: raise-mcpyml
modified: '2026-07-20'
name: Raise
nav: Providers
network: true
overview: 'Raise publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Gift Cards, Commerce, and Payments.


  Raise''s developer surface includes documentation, API reference, getting-started guide, support, and 6 more developer resources.'
random_paper: 85
score:
  band: emerging
  composite: 17.5
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 39.1
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 17.5
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Raise Authentication
  slug: raise-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Raise Domain Security
  slug: raise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: raise
tags:
- Company
- Consumer
- Gift Cards
- Commerce
- Payments
- Rewards
- Marketplace
- API
website: http://www.raise.com
---
