---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Galileo Fs Agentic Access
  operation_count: 19
  slug: galileo-fs-agentic-access
  summary_line: 19 operations · 19 acting · 1 human-in-the-loop
api_count: 17
apis:
- description: 'REST API for managing accounts and cards: account creation, KYC/CIP verification, balance/funding, card issuance (physical, digital, virtual, instant-issue), authorization controls.'
  name: Galileo Program API
  slug: program-api
- description: REST API for program configuration including card products, fee schedules, MCC controls, and program parameters.
  name: Galileo Config API
  slug: config-api
- description: REST API for the dispute lifecycle (chargebacks, representments, network communications).
  name: Galileo Dispute API 3.0
  slug: dispute-api
- description: REST API for credit, lending, BNPL, and secured-credit products including draw, repayment, and balance inquiry.
  name: Galileo Loan API
  slug: loan-api
- description: REST API for ACH, RTP, Bill Pay, and other payments rails.
  name: Galileo Payment Hub API
  slug: payment-hub-api
- description: REST API for risk and fraud screening tools.
  name: Galileo Risk API
  slug: risk-api
- description: Synchronous webhook-style endpoint customers expose for Galileo to call during authorization for approve/decline decisions.
  name: Galileo Auth API (Authorization Controller)
  slug: auth-api
- description: Outbound webhook delivery for transactions, account events, card events, and other lifecycle events.
  name: Galileo Events API
  slug: events-api
- description: REST API to feed third-party transactions into Galileo program ledgers for unified reporting.
  name: Galileo External Transactions API
  slug: external-transactions-api
- description: The Config API from Galileo Financial Technologies — 1 operation(s) for config.
  name: Galileo Financial Technologies Config API
  slug: galileo-fs-config-api
- description: The Dispute API from Galileo Financial Technologies — 3 operation(s) for dispute.
  name: Galileo Financial Technologies Dispute API
  slug: galileo-fs-dispute-api
- description: The Events API from Galileo Financial Technologies — 1 operation(s) for events.
  name: Galileo Financial Technologies Events API
  slug: galileo-fs-events-api
- description: The ExternalTransactions API from Galileo Financial Technologies — 1 operation(s) for externaltransactions.
  name: Galileo Financial Technologies ExternalTransactions API
  slug: galileo-fs-externaltransactions-api
- description: The Loan API from Galileo Financial Technologies — 3 operation(s) for loan.
  name: Galileo Financial Technologies Loan API
  slug: galileo-fs-loan-api
- description: The PaymentHub API from Galileo Financial Technologies — 3 operation(s) for paymenthub.
  name: Galileo Financial Technologies PaymentHub API
  slug: galileo-fs-paymenthub-api
- description: The Program API from Galileo Financial Technologies — 6 operation(s) for program.
  name: Galileo Financial Technologies Program API
  slug: galileo-fs-program-api
- description: The Risk API from Galileo Financial Technologies — 1 operation(s) for risk.
  name: Galileo Financial Technologies Risk API
  slug: galileo-fs-risk-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Galileo Financial Technologies Pro Config API
  slug: open-galileo-fs-config-api
- collection_type: open
  name: Galileo Financial Technologies Pro Config Dispute API
  slug: open-galileo-fs-dispute-api
- collection_type: open
  name: Galileo Financial Technologies Pro Config Events API
  slug: open-galileo-fs-events-api
- collection_type: open
  name: Galileo Financial Technologies Pro Config ExternalTransactions API
  slug: open-galileo-fs-externaltransactions-api
- collection_type: open
  name: Galileo Financial Technologies Pro Config Loan API
  slug: open-galileo-fs-loan-api
- collection_type: open
  name: Galileo Financial Technologies Pro Config PaymentHub API
  slug: open-galileo-fs-paymenthub-api
- collection_type: open
  name: Galileo Financial Technologies Pro Config Program API
  slug: open-galileo-fs-program-api
- collection_type: open
  name: Galileo Financial Technologies Pro Config Risk API
  slug: open-galileo-fs-risk-api
- collection_type: open
  name: Galileo Financial Technologies Pro API
  slug: open-galileo-fs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/galileo-fs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/galileo-fs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/galileo-fs-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/galileo-financial-technologies
- group: company
  title: ''
  type: Website
  url: https://www.galileo-ft.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/galileo-fs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/galileo-fs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/galileo-fs-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.galileo-ft.com/llms.txt
created: '2026-05-08'
description: Galileo Financial Technologies (a SoFi company) is a card-issuing and banking platform powering many fintechs. Provides Program API (accounts, cards), Config API, Dispute API 3.0, Loan API, Payment Hub API, Risk API, Auth API (authorization controller webhook), Events API webhooks, and External Transactions API.
finops:
- name: Galileo Fs Finops
  service_category: FinTech
  slug: galileo-fs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/galileo-fs.png
layout: provider
modified: '2026-05-08'
name: Galileo Financial Technologies
nav: Providers
network: true
overview: 'Galileo Financial Technologies publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Config API, Dispute API, Events API, and 5 more. Tagged areas include FinTech, BaaS, Card Issuing, Banking, and Payments.


  Galileo Financial Technologies'' developer surface includes authentication and 8 more developer resources.'
plans:
- name: Galileo Fs Plans Pricing
  plan_count: 1
  slug: galileo-fs-plans-pricing
random_paper: 101
rate_limits:
- limit_count: 2
  name: Galileo Fs Rate Limits
  slug: galileo-fs-rate-limits
score:
  band: emerging
  composite: 25.5
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 51.9
    developer_ergonomics: 10.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 25.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/galileo-fs/refs/heads/main/screenshots/galileo-fs-2026-06-20T181643.png
security:
- kind: authentication
  name: Galileo Fs Authentication
  slug: galileo-fs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Galileo Fs Domain Security
  slug: galileo-fs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: galileo-fs
tags:
- FinTech
- BaaS
- Card Issuing
- Banking
- Payments
- ACH
website: https://www.galileo-ft.com/
---
