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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: Hosted payment session API for accepting one-off payments from Wave wallet users. Create a checkout session, redirect the customer to the returned wave_launch_url, then receive a checkout.session.comp
  name: Wave Checkout API
  slug: wave-checkout-api
- description: Programmatic disbursement API for sending money from a business wallet to individual Wave wallets, identified by E.164 mobile number. Supports single payouts, payout batches (submit many at once and p
  name: Wave Payout API
  slug: wave-payout-api
- description: Read-side API for inspecting a business wallet's current balance and enumerating its transactions for accounting and reconciliation. GET /v1/balance returns the live wallet balance (optionally aggrega
  name: Wave Balance & Reconciliation API
  slug: wave-balance-reconciliation-api
- description: Sub-merchant management API for aggregators, payment service providers, and platforms that accept Wave payments on behalf of many downstream businesses. Full CRUD over aggregated merchant records — li
  name: Wave Aggregated Merchants API
  slug: wave-aggregated-merchants-api
- description: Outbound event delivery channel for asynchronously notifying merchant systems when state changes on the Wave platform. Events include checkout.session.completed, checkout.session.payment_failed, b2b.p
  name: Wave Webhooks
  slug: wave-webhooks
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wave-mobile-money-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wave-mobile-money-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wave.com
- group: start
  title: ''
  type: Portal
  url: https://www.wave.com/en/
- group: start
  title: ''
  type: Portal
  url: https://business.wave.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wave.com/business
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wave.com/checkout
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wave.com/payout
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wave.com/balance-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wave.com/aggregated-merchants
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wave.com/webhook
- group: company
  title: ''
  type: About
  url: https://www.wave.com/en/about/
- group: company
  title: ''
  type: Careers
  url: https://www.wave.com/en/careers/
- group: company
  title: ''
  type: Blog
  url: https://www.wave.com/en/blog/
- group: company
  title: ''
  type: Blog
  url: https://wave.engineering/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wave.com/en/terms_and_conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wave.com/en/privacy/
- group: auth
  title: ''
  type: Security
  url: https://www.wave.com/en/security/responsible_disclosure
- group: operate
  title: ''
  type: Support
  url: https://www.wave.com/en/complaints-policy/
- group: other
  title: ''
  type: Product
  url: https://www.wave.com/en/wdf/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wave.com/en/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.wave.com/business
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.wave.com/business
- group: company
  title: ''
  type: CrunchBase
  url: https://www.crunchbase.com/organization/wave-mobile-money
- group: other
  title: ''
  type: YCombinator
  url: https://www.ycombinator.com/companies/wave
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Wave_Mobile_Money
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wavemobilemoney/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/WaveSenegal
created: '2026-05-24'
description: Wave is a Dakar, Senegal-headquartered mobile money company on a mission to "make Africa the first cashless continent." Founded by Drew Durbin and Lincoln Quirk (who previously built the Sendwave remittance service) and publicly launched in Senegal in 2018, Wave provides a smartphone- and agent-based wallet that lets users deposit and withdraw cash for free and send money domestically for a flat 1% fee — roughly 70% cheaper than the telco-led mobile money incumbents in the region. Wave operates today in Senegal, Côte d'Ivoire, Uganda, Mali, Burkina Faso, and The Gambia, working through a dense network of human agents alongside the Wave app and a separate Wave Business portal for merchants and enterprises. In September 2021, Wave raised a USD 200M Series A led by Sequoia Heritage, Founders Fund, Stripe, and Ribbit at a USD 1.7B valuation — the largest Series A ever raised on the African continent at the time. For developers, Wave exposes a tier-1 B2B platform via api.wave.com,
  documented at docs.wave.com, with Checkout (hosted payment sessions), Payout (single and batch disbursements, reversals, recipient verification), Balance & Reconciliation (wallet balance, transactions, refunds), Aggregated Merchants (sub-merchant management for aggregators and PSPs), and Webhooks with HMAC-SHA256 signing for asynchronous event delivery. API keys are scoped per-API, support IP allowlisting and optional request signing, and the platform enforces idempotency on POST mutations.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wave-mobile-money.png
layout: provider
modified: '2026-05-24'
name: Wave Mobile Money
nav: Providers
network: true
overview: 'Wave Mobile Money publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Mobile Money, Payments, Fintech, Financial Inclusion, and Africa.


  Wave Mobile Money''s developer surface includes developer portal, documentation, engineering blog, support, pricing, authentication, and 22 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 23.9
  delta: -0.9
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 24.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 40.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wave-mobile-money/refs/heads/main/screenshots/wave-mobile-money-2026-06-20T201254.png
security:
- kind: domain-security
  name: Wave Mobile Money Domain Security
  slug: wave-mobile-money-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wave Mobile Money Vulnerability Disclosure
  slug: wave-mobile-money-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wave-mobile-money
tags:
- Mobile Money
- Payments
- Fintech
- Financial Inclusion
- Africa
- West Africa
- Senegal
- Cote d'Ivoire
- Uganda
- Mali
- Burkina Faso
- Wallets
- Disbursements
- Checkout
- Payouts
- Money Transfer
website: https://www.wave.com
---
