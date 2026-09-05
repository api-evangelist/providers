---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: 'Disburse money programmatically to any Indonesian bank account or e-wallet. Create single and bulk disbursements, inquire bank accounts, list bank codes, and receive callbacks on disbursement status. '
  name: Flip Money Transfer (Disbursement) API
  slug: flip-money-transfer-disbursement-api
- description: Accept online payments from customers via bank transfer, virtual accounts, e-wallets, cards, QRIS, and retail outlets. Create payment links / bills, configure payment methods and expiry, and receive p
  name: Flip Accept Payment API
  slug: flip-accept-payment-api
- description: Send cross-border international transfers, including bulk international transfers, with recipient inquiry, request-for-information (RFI) handling, and transfer status callbacks.
  name: Flip International Transfer API
  slug: flip-international-transfer-api
artifact_total: 6
asyncapis:
- description: ''
  name: Flip Webhooks
  slug: flip-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flip.id/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.flip.id/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flip.id/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.flip.id/
- group: company
  title: ''
  type: Blog
  url: https://docs.flip.id/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://flip.id/business/pricing
- group: start
  title: ''
  type: SignUp
  url: https://business.flip.id/
- group: start
  title: ''
  type: Login
  url: https://business.flip.id/
- group: operate
  title: ''
  type: Support
  url: https://help.flip.id/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.flip.id/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flip.id/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flip.id/syarat-ketentuan
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flip-id
- group: other
  title: ''
  type: Business
  url: https://flip.id/business
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.flip.id/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/flip-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flip-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flip-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/flip-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/flip-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/flip-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flip-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/flip-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/flip-packages.yml
created: '2026-07-17'
description: Flip (PT Fliptech Lentera Inspirasi Pertiwi) is an Indonesian financial technology company offering low-cost interbank money transfers, bill payments, and cross-border remittance to consumers, and a "Flip for Business" (bigflip) suite of payment APIs to companies. The Flip for Business API lets businesses disburse money to any Indonesian bank or e-wallet (Money Transfer / Disbursement API), accept online payments via bank transfer, virtual accounts, e-wallets, cards, and retail outlets (Accept Payment API), and send international transfers (International Transfer API). The API is HTTP Basic authenticated with a secret key, supports IP whitelisting, idempotency keys, and signed callbacks/webhooks, and ships a sandbox environment plus WooCommerce and Magento 2 payment plugins. Flip is backed by Insight Partners, Lightspeed Venture Partners, and Y Combinator.
image: https://flip.id/images/logo-big-flip.png
layout: provider
modified: '2026-07-19'
name: Flip
nav: Providers
network: true
overview: 'Flip publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Payment Gateway, Money Transfer, and Disbursement.


  The Flip catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Flip''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, changelog, and 18 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 64.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 40.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flip/refs/heads/main/screenshots/flip-2026-07-25T214801.png
security:
- kind: authentication
  name: Flip Authentication
  slug: flip-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Flip Domain Security
  slug: flip-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: flip
tags:
- Company
- Payments
- Payment Gateway
- Money Transfer
- Disbursement
- Remittance
- Fintech
- Indonesia
- International Transfer
- Banking
website: https://flip.id/
---
