---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Column Agentic Access
  operation_count: 44
  slug: column-agentic-access
  summary_line: 44 operations · 21 acting
api_count: 1
apis:
- baseURL: https://api.column.com
  baseurl_source: declared
  description: Originate and receive ACH transfers with returns and reversal handling.
  name: Column ACH Transfers API
  slug: column-ach-transfers-api
- baseURL: https://api.column.com
  baseurl_source: declared
  description: Send domestic wires with drawdowns and return-request workflows.
  name: Column Wire Transfers API
  slug: column-wire-transfers-api
- baseURL: https://api.column.com
  baseurl_source: declared
  description: Cross-border wires with FX quoting and amendments.
  name: Column International Wires API
  slug: column-international-wires-api
- baseURL: https://api.column.com
  baseurl_source: declared
  description: Instant RTP/FedNow transfers and Request for Payment (RFP).
  name: Column Realtime Transfers API
  slug: column-realtime-transfers-api
- baseURL: https://api.column.com
  baseurl_source: declared
  description: Internal ledger movements between Column accounts.
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
- baseURL: https://api.column.com
  baseurl_source: declared
  description: HMAC-SHA256 signed event callbacks for ACH, wire, international wire (SWIFT), realtime (RTP/FedNow), book transfers, checks, bank accounts, identity verification, loans, and reporting.
  name: Column Webhooks
  slug: column-webhooks
- baseURL: https://api.column.com
  baseurl_source: declared
  description: The Account Numbers API from Column — 2 operation(s) for account numbers.
  name: Column Account Numbers API
  slug: column-account-numbers-api
- baseURL: https://api.column.com
  baseurl_source: declared
  description: The ACH Transfers API from Column — 4 operation(s) for ach transfers.
  name: Column ACH Transfers API
  slug: column-ach-transfers-api
- baseURL: https://api.column.com
  baseurl_source: declared
  description: The Bank Accounts API from Column — 2 operation(s) for bank accounts.
  name: Column Bank Accounts API
  slug: column-bank-accounts-api
- baseURL: https://api.column.com
  baseurl_source: declared
  description: The Book Transfers API from Column — 2 operation(s) for book transfers.
  name: Column Book Transfers API
  slug: column-book-transfers-api
- baseURL: https://api.column.com
  baseurl_source: declared
  description: The Check Transfers API from Column — 3 operation(s) for check transfers.
  name: Column Check Transfers API
  slug: column-check-transfers-api
- baseURL: https://api.column.com
  baseurl_source: declared
  description: The Counterparties API from Column — 2 operation(s) for counterparties.
  name: Column Counterparties API
  slug: column-counterparties-api
- baseURL: https://api.column.com
  baseurl_source: declared
  description: The Entities API from Column — 4 operation(s) for entities.
  name: Column Entities API
  slug: column-entities-api
- baseURL: https://api.column.com
  baseurl_source: declared
  description: The Events API from Column — 2 operation(s) for events.
  name: Column Events API
  slug: column-events-api
- baseURL: https://api.column.com
  baseurl_source: declared
  description: The International Wires API from Column — 2 operation(s) for international wires.
  name: Column International Wires API
  slug: column-international-wires-api
- baseURL: https://api.column.com
  baseurl_source: declared
  description: The Realtime Transfers API from Column — 2 operation(s) for realtime transfers.
  name: Column Realtime Transfers API
  slug: column-realtime-transfers-api
- baseURL: https://api.column.com
  baseurl_source: declared
  description: The Webhooks API from Column — 2 operation(s) for webhooks.
  name: Column Webhooks API
  slug: column-webhooks-api
- baseURL: https://api.column.com
  baseurl_source: declared
  description: The Wire Transfers API from Column — 2 operation(s) for wire transfers.
  name: Column Wire Transfers API
  slug: column-wire-transfers-api
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Column Account Numbers API
  slug: open-column-account-numbers-api
- collection_type: open
  name: Column Account Numbers ACH Transfers API
  slug: open-column-ach-transfers-api
- collection_type: open
  name: Column Webhooks
  slug: open-column-asyncapi
- collection_type: open
  name: Column Account Numbers Bank Accounts API
  slug: open-column-bank-accounts-api
- collection_type: open
  name: Column Account Numbers Book Transfers API
  slug: open-column-book-transfers-api
- collection_type: open
  name: Column Account Numbers Check Transfers API
  slug: open-column-check-transfers-api
- collection_type: open
  name: Column Account Numbers Counterparties API
  slug: open-column-counterparties-api
- collection_type: open
  name: Column Account Numbers Entities API
  slug: open-column-entities-api
- collection_type: open
  name: Column Account Numbers Events API
  slug: open-column-events-api
- collection_type: open
  name: Column Account Numbers International Wires API
  slug: open-column-international-wires-api
- collection_type: open
  name: Column Account Numbers Realtime Transfers API
  slug: open-column-realtime-transfers-api
- collection_type: open
  name: Column Account Numbers Webhooks API
  slug: open-column-webhooks-api
- collection_type: open
  name: Column Account Numbers Wire Transfers API
  slug: open-column-wire-transfers-api
- collection_type: open
  name: Column API
  slug: open-column
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/column-capability-edges.yml
- group: design
  title: ''
  type: Webhooks
  url: https://docs.column.com/api/webhooks/
- group: start
  title: ''
  type: Sandbox
  url: https://docs.column.com/guides/sandbox-and-testing
- group: docs
  title: ''
  type: APIReference
  url: https://docs.column.com/api/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.column.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://column.com/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.column.com/guides/getting-started
- group: start
  title: ''
  type: Login
  url: https://dashboard.column.com/login
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
overview: 'Column publishes 18 APIs on the [APIs.io](https://apis.io/) network, including ACH Transfers API, Wire Transfers API, International Wires API, and 15 more. Tagged areas include Fintech, Banking, Backend-as-a-Service, ACH, and Wires.


  Column''s developer surface includes sandbox, API reference, changelog, getting-started guide, authentication, engineering blog, and 12 more developer resources.'
plans:
- name: Column Plans Pricing
  plan_count: 1
  slug: column-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Column Rate Limits
  slug: column-rate-limits
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 19.7
    commercial_clarity: 19.7
    contract_governance: 0.0
    contract_quality: 58.4
    developer_ergonomics: 50.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Backend-as-a-Service
- ACH
- Wires
website: https://column.com/
---
