---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.8
  scored_at: '2026-09-12'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Cross River Bank Agentic Access
  operation_count: 22
  slug: cross-river-bank-agentic-access
  summary_line: 22 operations · 16 acting
api_count: 8
apis:
- description: 'Proprietary API-driven banking core that underpins all Cross River partner programs. Provides a real-time subledger, KYC / KYB, compliance workflows, accounts, payments, cards, and lending primitives '
  name: Cross River Operating System (COS)
  slug: cos
- description: REST API for opening and managing FDIC-insured deposit accounts (checking, savings, purpose-built program accounts) on behalf of partner-program end users. Includes balances, statements, holds, and ac
  name: Cross River Accounts API
  slug: accounts-api
- description: Unified payments API covering ACH and Same-Day ACH, FedNow and RTP instant payments, domestic and international wires, and book transfers. Includes payment origination, returns, and reporting.
  name: Cross River Payments API
  slug: payments-api
- description: Card issuing and processing API spanning Visa, Mastercard, and regional networks. Supports debit, credit, and prepaid programs, virtual / physical card lifecycle, authorizations, settlement, and merch
  name: Cross River Card Payments API
  slug: card-payments-api
- description: Marketplace-lending and loan-origination API used by fintech lending partners for consumer and SMB loan origination, underwriting, funding, servicing, participation, and securitization.
  name: Cross River Lending / Loan Funding API
  slug: lending-api
- description: Money-movement API supporting stablecoin pay-ins and pay-outs across fiat rails for crypto and Web3 partners, with the bank serving as the regulated on/off-ramp.
  name: Cross River Stablecoin Payments
  slug: stablecoin
- description: Outbound webhook events covering account, payment, card, and lending lifecycle changes. Endpoints and signing secrets are configured per partner program.
  name: Cross River Webhooks
  slug: webhooks
- description: Postman collection of the COS APIs distributed to onboarded partners to accelerate sandbox testing and integration work.
  name: Cross River Postman Collection
  slug: postman
artifact_total: 14
common:
- group: operate
  title: ''
  type: Support
  url: https://www.crossriver.com/support
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.crossriver.com/developers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crossriver.com/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.crossriver.com/get-started/quickstart
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cross-river-bank-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cross-river-bank-authentication.yml
- group: start
  title: ''
  type: Signup
  url: https://www.crossriver.com/contact
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cross-river-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.crossriver.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crossriver.com/
- group: start
  title: ''
  type: PartnerPortal
  url: https://www.crossriver.com/partners
- group: other
  title: ''
  type: COS
  url: https://www.crossriver.com/cos
- group: operate
  title: ''
  type: ContactSales
  url: https://www.crossriver.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cross-river-bank
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.crossriver.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.crossriver.com/insights
created: '2026-05-23'
description: Cross River Bank is an FDIC-insured chartered bank that operates as a sponsor bank and banking-as-a-service (BaaS) provider for fintech companies, embedded-finance platforms, and crypto / stablecoin issuers. The product surface is delivered through the Cross River Operating System (COS) - a proprietary API-driven banking core with real-time subledger generation - and includes accounts, ACH and Same-Day ACH, RTP and FedNow instant payments, wires, card issuing and processing (Visa / Mastercard), merchant acquiring, stablecoin rails, consumer and SMB lending, and capital markets / loan participation services. API access is gated behind a partner onboarding process; documentation and sandbox are at docs.crossriver.com.
finops:
- name: Cross River Bank Finops
  service_category: API
  slug: cross-river-bank-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cross-river-bank.png
layout: provider
modified: '2026-05-23'
name: Cross River Bank
nav: Providers
network: true
overview: 'Cross River Bank publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Banking as a Service, Sponsor Bank, Embedded Finance, and Payments.


  Cross River Bank''s developer surface includes support, getting-started guide, authentication, signup flow, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Cross River Bank Plans Pricing
  plan_count: 1
  slug: cross-river-bank-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Cross River Bank Rate Limits
  slug: cross-river-bank-rate-limits
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 81.5
    operational_transparency: 21.1
  previous_composite: 30.3
  provenance:
    agentic_access: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.0
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/cross-river-bank/refs/heads/main/screenshots/cross-river-bank-2026-06-20T175244.png
security:
- kind: authentication
  name: Cross River Bank Authentication
  slug: cross-river-bank-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cross River Bank Domain Security
  slug: cross-river-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cross-river-bank
tags:
- Banking
- Banking as a Service
- Sponsor Bank
- Embedded Finance
- Payments
- ACH
- RTP
- FedNow
- Cards
- Lending
- Stablecoins
website: https://www.crossriver.com/
---
