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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 31.7
  scored_at: '2026-07-23'
api_count: 9
apis:
- description: The Bill API from Seel — 3 operation(s) for bill.
  name: Seel Bill API
  slug: seel-bill-api
- description: The Claim API from Seel — 2 operation(s) for claim.
  name: Seel Claim API
  slug: seel-claim-api
- description: The Contract API from Seel — 2 operation(s) for contract.
  name: Seel Contract API
  slug: seel-contract-api
- description: The Event API from Seel — 1 operation(s) for event.
  name: Seel Event API
  slug: seel-event-api
- description: The Fulfillment API from Seel — 3 operation(s) for fulfillment.
  name: Seel Fulfillment API
  slug: seel-fulfillment-api
- description: The Merchant API from Seel — 2 operation(s) for merchant.
  name: Seel Merchant API
  slug: seel-merchant-api
- description: The Order API from Seel — 4 operation(s) for order.
  name: Seel Order API
  slug: seel-order-api
- description: The Product API from Seel — 4 operation(s) for product.
  name: Seel Product API
  slug: seel-product-api
- description: The Quote API from Seel — 2 operation(s) for quote.
  name: Seel Quote API
  slug: seel-quote-api
artifact_total: 12
asyncapis:
- description: Seel delivers webhook notifications to a merchant-configured HTTPS endpoint when protection contract and claim lifecycle events occur. Each notification is a Notification object with id, created_ts, t
  name: Seel Webhooks
  slug: seel-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://seel.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.seel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.seel.com/docs/welcome-to-seel
- group: docs
  title: ''
  type: APIReference
  url: https://developer.seel.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.seel.com/docs/wfp-getting-started
- group: company
  title: ''
  type: Blog
  url: https://seel.com/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://kover2618.zendesk.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.seel.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.seel.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seel-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/seel-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seel-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Seel is a post-purchase protection and e-commerce insurance platform that helps online merchants offer Worry-Free Purchase coverage, Extended Warranty, and return, fulfillment, and price-drop protection to their shoppers. Its API lets merchants request protection Quotes for a cart, bind coverage to Orders (creating Contracts), manage Products, Fulfillments, Claims, and Bills, and emit Events, with contract and claim lifecycle changes delivered via webhooks. Seel serves 5,000+ merchants and has protected 24M+ orders. Backed by Lightspeed Venture Partners and Techstars.
image: https://seel.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: Seel
nav: Providers
network: true
overview: 'Seel publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Bill API, Claim API, Contract API, and 6 more. Tagged areas include Company, E-commerce, Insurance, Post-Purchase, and Returns.


  The Seel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Seel''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 9 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 38.7
  delta: -1.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 65.5
    developer_ergonomics: 47.8
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 40.2
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 30.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Seel Authentication
  slug: seel-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Seel Domain Security
  slug: seel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: seel
tags:
- Company
- E-commerce
- Insurance
- Post-Purchase
- Returns
- Extended Warranty
- Fraud
- Payments
website: https://seel.com/
---
