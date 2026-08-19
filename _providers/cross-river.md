---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Cross River Agentic Access
  operation_count: 22
  slug: cross-river-agentic-access
  summary_line: 22 operations · 16 acting
api_count: 7
apis:
- description: Deposit accounts and subledgers (COS Core module, /core/v1/dda).
  name: Cross River Accounts API
  slug: cross-river-accounts-api
- description: ACH origination and receipt (COS Payments, /ach).
  name: Cross River ACH API
  slug: cross-river-ach-api
- description: Debit card issuing and management (COS Card Management, /cardmanagement).
  name: Cross River Cards API
  slug: cross-river-cards-api
- description: Customer records, KYC, and onboarding (COS Core module, /core/v1/cm).
  name: Cross River Customer Management API
  slug: cross-river-customer-management-api
- description: RTP, FedNow, and CRNow instant payments (COS Payments, /rtp).
  name: Cross River Instant Payments API
  slug: cross-river-instant-payments-api
- description: Loan origination and servicing (separate lending host).
  name: Cross River Lending API
  slug: cross-river-lending-api
- description: Domestic wire transfers and drawdowns (COS Payments, /wires).
  name: Cross River Wires API
  slug: cross-river-wires-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cross River Operating System (COS) Accounts API
  slug: open-cross-river-accounts-api
- collection_type: open
  name: Cross River Operating System (COS) Accounts ACH API
  slug: open-cross-river-ach-api
- collection_type: open
  name: Cross River Operating System (COS) Accounts Cards API
  slug: open-cross-river-cards-api
- collection_type: open
  name: Cross River Operating System (COS) Accounts Customer Management API
  slug: open-cross-river-customer-management-api
- collection_type: open
  name: Cross River Operating System (COS) Accounts Instant Payments API
  slug: open-cross-river-instant-payments-api
- collection_type: open
  name: Cross River Operating System (COS) Accounts Lending API
  slug: open-cross-river-lending-api
- collection_type: open
  name: Cross River Operating System (COS) Accounts Wires API
  slug: open-cross-river-wires-api
- collection_type: open
  name: Cross River Operating System (COS) API
  slug: open-cross-river
common:
- group: company
  title: ''
  type: Blog
  url: https://www.crossriver.com/insights
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
  url: agentic-access/cross-river-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cross-river-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cross-river-authentication.yml
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
  type: Signup
  url: https://www.crossriver.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cross-river-bank
- group: commercial
  title: ''
  type: Plans
  url: plans/cross-river-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cross-river-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cross-river-finops.yml
created: '2026-07-12'
description: Cross River is a regulated bank (FDIC member, Fort Lee, NJ) that delivers embedded finance and Banking-as-a-Service (BaaS) through its Cross River Operating System (COS) - a collection of REST APIs for deposit accounts, ACH, wires, instant payments (RTP, FedNow, CRNow), card issuing and processing, lending, and KYC/customer onboarding. Access is partner/enterprise-gated - programs are onboarded through Cross River sales and a relationship manager, and OAuth2 client credentials are provisioned for sandbox and then production. Endpoints are grounded in the public developer documentation at docs.crossriver.com; request/response schemas are modeled where the live sandbox is credential-gated.
finops:
- name: Cross River Finops
  service_category: Financial Services and Embedded Finance
  slug: cross-river-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cross-river.png
layout: provider
modified: '2026-07-12'
name: Cross River
nav: Providers
network: true
overview: 'Cross River publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, ACH API, Cards API, and 4 more. Tagged areas include Embedded Finance, Banking as a Service, BaaS, Payments, and ACH.


  Cross River''s developer surface includes engineering blog, support, getting-started guide, authentication, documentation, signup flow, and 9 more developer resources.'
plans:
- name: Cross River Plans Pricing
  plan_count: 2
  slug: cross-river-plans-pricing
random_paper: 108
rate_limits:
- limit_count: 5
  name: Cross River Rate Limits
  slug: cross-river-rate-limits
score:
  band: developing
  composite: 45.3
  delta: 2.1
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 54.5
    developer_ergonomics: 50.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cross-river/refs/heads/main/screenshots/cross-river-2026-07-25T210751.png
security:
- kind: authentication
  name: Cross River Authentication
  slug: cross-river-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cross River Domain Security
  slug: cross-river-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cross-river
tags:
- Embedded Finance
- Banking as a Service
- BaaS
- Payments
- ACH
- Wire
- Push-to-Card
- Lending
- Accounts
- Cards
- Fintech
- RTP
- FedNow
website: https://www.crossriver.com/
---
