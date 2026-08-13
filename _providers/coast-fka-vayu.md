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
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Coast's v2 REST API for programmatically managing fuel/fleet cards, corporate cards, spend controls, transactions, and expense data. Documented via a Redocly reference and a Kong developer portal; acc
  name: Coast API v2
  slug: coast-api-v2
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coast-fka-vayu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coastpay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.coastpay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coastpay.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.coastpay.com/openapi/v2/coast-api
- group: commercial
  title: ''
  type: Pricing
  url: https://coastpay.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://portal.coastpay.com/auth
- group: start
  title: ''
  type: Login
  url: https://portal.coastpay.com/auth
- group: operate
  title: ''
  type: Support
  url: https://coastpay.com/customer-service/
- group: operate
  title: ''
  type: HelpCenter
  url: https://coastpay.com/faqs/
- group: company
  title: ''
  type: Blog
  url: https://coastpay.com/resources/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coastpay.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coastpay.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coastpay.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coast-fka-vayu-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/coast-fka-vayu-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/coast-fka-vayu-packages.yml
- group: design
  title: ''
  type: Components
  url: components/coast-fka-vayu-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/coast-fka-vayu-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coast-fka-vayu-llms.txt
created: '2026-07-17'
description: Coast (formerly VayU) is a US financial-technology company that consolidates fuel cards, fleet and field cards, corporate cards, expense management, and bill pay onto a single platform for fleet-based and field-service businesses across HVAC, construction, transportation, and landscaping. Coast pairs Visa card issuing with spend controls, fraud prevention, rewards, and real-time reporting, and integrates with telematics (Samsara, Geotab, Verizon Connect), fleet management (Fleetio, Whip Around), and accounting (QuickBooks, NetSuite, Sage Intacct) systems. Coast exposes a v2 REST API and an embedded-widget SDK through a Kong-hosted developer portal. Backed by ICONIQ Growth, Accel, Insight Partners, and Bessemer Venture Partners.
image: https://coastpay.com/og.png
layout: provider
modified: '2026-07-18'
name: Coast (FKA VayU)
nav: Providers
network: true
overview: 'Coast (FKA VayU) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fleet Cards, Fuel Cards, and Corporate Cards.


  Coast (FKA VayU)''s developer surface includes documentation, API reference, pricing, signup flow, support, engineering blog, and 14 more developer resources.'
random_paper: 67
score:
  band: emerging
  composite: 26.3
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 37.0
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 26.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coast-fka-vayu/refs/heads/main/screenshots/coast-fka-vayu-2026-07-25T205832.png
security:
- kind: domain-security
  name: Coast Fka Vayu Domain Security
  slug: coast-fka-vayu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coast-fka-vayu
tags:
- Company
- Payments
- Fleet Cards
- Fuel Cards
- Corporate Cards
- Expense Management
- Fintech
- Bill Pay
website: https://coastpay.com/
---
