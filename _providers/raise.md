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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The Raise Commerce API (business/v2) — browse gift card brands and categories, purchase fixed- and variable-load gift cards, retrieve and act on individual cards (balance check, mark redeemed, update '
  name: Raise Commerce API
  slug: raise-commerce-api
artifact_total: 3
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
modified: '2026-07-20'
name: Raise
nav: Providers
network: true
overview: 'Raise publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Gift Cards, Commerce, and Payments.


  Raise''s developer surface includes documentation, API reference, getting-started guide, support, and 6 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 17.7
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/raise/refs/heads/main/screenshots/raise-2026-09-02T152823.png
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
website: http://www.raise.com
---
