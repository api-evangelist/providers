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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
  score: 0.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Boku Direct is Boku's payment gateway API for accepting local payment methods — mobile wallets, account-to-account transfers, and direct carrier billing — with support for one-off charges, subscriptio
  name: Boku Direct - Payment Gateway API
  slug: boku-direct-payment-gateway-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boku-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/boku-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.boku.com/boku-bug-bounty-program
- group: company
  title: ''
  type: Website
  url: https://www.boku.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.boku.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.boku.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.boku.com/json/index.html
- group: company
  title: ''
  type: Blog
  url: https://www.boku.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.boku.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boku.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boku.com/payments-privacy-notice
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/boku-llms.txt
created: '2026-07-17'
description: Boku is a global mobile payments network that connects digital merchants to more than 200 local payment methods — mobile wallets, real-time account-to-account bank transfers, and direct carrier billing — across 70+ countries, reaching over 7 billion payment accounts. Through its Boku Direct payment gateway API, merchants such as Epic Games, Google, Meta, Microsoft, Netflix, Sony, Spotify, and Tencent accept local payments, run subscriptions, and settle globally. Boku processes over $9 billion in payments annually and is publicly traded on the London Stock Exchange (LON:BOKU).
image: https://developer.boku.com/json/static/images/boku-logo.png
layout: provider
modified: '2026-07-18'
name: Boku
nav: Providers
network: true
overview: 'Boku publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Mobile Payments, Carrier Billing, and Digital Wallet.


  Boku''s developer surface includes documentation, API reference, engineering blog, support, and 8 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 16.8
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boku/refs/heads/main/screenshots/boku-2026-07-25T203528.png
security:
- kind: domain-security
  name: Boku Domain Security
  slug: boku-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Boku Vulnerability Disclosure
  slug: boku-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: boku
tags:
- Company
- Payments
- Mobile Payments
- Carrier Billing
- Digital Wallet
- Local Payment Methods
- Subscription
- Fintech
website: https://www.boku.com
---
