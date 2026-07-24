---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Column Agentic Access
  operation_count: 44
  slug: column-agentic-access
  summary_line: 44 operations · 21 acting
api_count: 21
apis:
- description: Originate and receive ACH transfers with returns and reversal handling.
  name: Column ACH Transfers API
  slug: column-ach-transfers-api
- description: Send domestic wires with drawdowns and return-request workflows.
  name: Column Wire Transfers API
  slug: column-wire-transfers-api
- description: Cross-border wires with FX quoting and amendments.
  name: Column International Wires API
  slug: column-international-wires-api
- description: Instant RTP/FedNow transfers and Request for Payment (RFP).
  name: Column Realtime Transfers API
  slug: column-realtime-transfers-api
- description: Internal ledger movements between Column accounts.
  name: Column Book Transfers API
  slug: column-book-transfers-api
- description: Issue, print, mail and deposit physical checks.
  name: Column Check Services API
  slug: column-check-services-api
- description: Loan disbursements, payments, sales and reporting.
  name: Column Lending API
  slug: column-lending-api
- description: Person and business entity onboarding plus bank accounts and account numbers.
  name: Column Entities & Accounts API
  slug: column-entities-accounts-api
- description: HMAC-SHA256 signed event callbacks for ACH, wire, international wire (SWIFT), realtime (RTP/FedNow), book transfers, checks, bank accounts, identity verification, loans, and reporting.
  name: Column Webhooks
  slug: column-webhooks
- description: The Account Numbers API from Column — 2 operation(s) for account numbers.
  name: Column Account Numbers API
  slug: column-account-numbers-api
- description: The ACH Transfers API from Column — 4 operation(s) for ach transfers.
  name: Column ACH Transfers API
  slug: column-ach-transfers-api
- description: The Bank Accounts API from Column — 2 operation(s) for bank accounts.
  name: Column Bank Accounts API
  slug: column-bank-accounts-api
- description: The Book Transfers API from Column — 2 operation(s) for book transfers.
  name: Column Book Transfers API
  slug: column-book-transfers-api
- description: The Check Transfers API from Column — 3 operation(s) for check transfers.
  name: Column Check Transfers API
  slug: column-check-transfers-api
- description: The Counterparties API from Column — 2 operation(s) for counterparties.
  name: Column Counterparties API
  slug: column-counterparties-api
- description: The Entities API from Column — 4 operation(s) for entities.
  name: Column Entities API
  slug: column-entities-api
- description: The Events API from Column — 2 operation(s) for events.
  name: Column Events API
  slug: column-events-api
- description: The International Wires API from Column — 2 operation(s) for international wires.
  name: Column International Wires API
  slug: column-international-wires-api
- description: The Realtime Transfers API from Column — 2 operation(s) for realtime transfers.
  name: Column Realtime Transfers API
  slug: column-realtime-transfers-api
- description: The Webhooks API from Column — 2 operation(s) for webhooks.
  name: Column Webhooks API
  slug: column-webhooks-api
- description: The Wire Transfers API from Column — 2 operation(s) for wire transfers.
  name: Column Wire Transfers API
  slug: column-wire-transfers-api
artifact_total: 29
collections:
- collection_type: open
  name: Column Webhooks
  slug: open-column-asyncapi
- collection_type: open
  name: Column API
  slug: open-column
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/column-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/column-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/column-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/column-bank
- group: company
  title: ''
  type: Website
  url: https://column.com/
- group: company
  title: ''
  type: Blog
  url: https://column.com/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/column-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/column-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/column-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://column.com/llms.txt
created: '2026-05-08'
description: Column is a chartered nationally-regulated bank purpose-built for developer APIs. Offers ACH, wires, FedNow, checks, BIN sponsorship, and bank-direct ledgering.
finops:
- name: Column Finops
  service_category: Fintech
  slug: column-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/column.png
layout: provider
modified: '2026-05-30'
name: Column
nav: Providers
network: true
overview: 'Column publishes 18 APIs on the [APIs.io](https://apis.io/) network, including ACH Transfers API, Wire Transfers API, International Wires API, and 15 more. Tagged areas include Fintech, Banking, BaaS, ACH, and Wires.


  Column''s developer surface includes authentication, engineering blog, and 8 more developer resources.'
plans:
- name: Column Plans Pricing
  plan_count: 1
  slug: column-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 1
  name: Column Rate Limits
  slug: column-rate-limits
score:
  band: thin
  composite: 30.8
  delta: -0.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 59.8
    developer_ergonomics: 13.0
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 31.6
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Column Authentication
  slug: column-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Column Domain Security
  slug: column-domain-security
  summary_line: TLSv1.3 · DMARC
slug: column
tags:
- Fintech
- Banking
- BaaS
- ACH
- Wires
website: https://column.com/
---
