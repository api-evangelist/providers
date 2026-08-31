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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
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
artifact_total: 12
common:
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


  Cross River Bank''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
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
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cross-river-bank/refs/heads/main/screenshots/cross-river-bank-2026-06-20T175244.png
security:
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
- Stablecoin
website: https://www.crossriver.com/
---
