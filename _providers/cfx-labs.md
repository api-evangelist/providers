---
agent_readiness:
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Cfx Labs Agentic Access
  operation_count: 53
  slug: cfx-labs-agentic-access
  summary_line: 53 operations · 28 acting
api_count: 4
apis:
- baseURL: https://api.cfx.to
  baseurl_source: declared
  description: The Cash API from CFX Labs — 8 operation(s) for cash.
  name: CFX Labs Cash API
  slug: cfx-labs-cash-api
- baseURL: https://api.cfx.to
  baseurl_source: declared
  description: Retrieve and manage deposits into the CFX network.
  name: CFX Labs Deposit API
  slug: cfx-labs-deposit-api
- baseURL: https://api.cfx.to
  baseurl_source: declared
  description: Memos that route inbound deposits to a ledger account.
  name: CFX Labs Deposit Memos API
  slug: cfx-labs-deposit-memos-api
- baseURL: https://api.cfx.to
  baseurl_source: declared
  description: Create, fund, claim, reject, and cancel escrow transfers across their lifecycle.
  name: CFX Labs Escrow Transfers API
  slug: cfx-labs-escrow-transfers-api
- baseURL: https://api.cfx.to
  baseurl_source: declared
  description: Register, retrieve, update, and verify identities.
  name: CFX Labs Identity API
  slug: cfx-labs-identity-api
- baseURL: https://api.cfx.to
  baseurl_source: declared
  description: Upload and manage KYC documents for an identity.
  name: CFX Labs Identity Documents API
  slug: cfx-labs-identity-documents-api
- baseURL: https://api.cfx.to
  baseurl_source: declared
  description: MoveUSD-denominated accounts owned by an identity.
  name: CFX Labs Ledger Accounts API
  slug: cfx-labs-ledger-accounts-api
- baseURL: https://api.cfx.to
  baseurl_source: declared
  description: Bank accounts and wallets an identity can send to or receive from.
  name: CFX Labs Payment Instruments API
  slug: cfx-labs-payment-instruments-api
- baseURL: https://api.cfx.to
  baseurl_source: declared
  description: Products available to an identity and their activation status.
  name: CFX Labs Products API
  slug: cfx-labs-products-api
- baseURL: https://api.cfx.to
  baseurl_source: declared
  description: Request-for-payment flow that precedes an escrow transfer (create, accept, reject, cancel).
  name: CFX Labs Transfer Requests API
  slug: cfx-labs-transfer-requests-api
- baseURL: https://api.cfx.to
  baseurl_source: declared
  description: US bank ACH pull deposits.
  name: CFX Labs US Bank ACH API
  slug: cfx-labs-us-bank-ach-api
artifact_total: 16
asyncapis:
- description: ''
  name: Cfx Labs Webhooks
  slug: cfx-labs-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/cfx-labs/agentic-access/cfx-labs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cfx-labs-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cfx-labs/rules/cfx-labs-rules.yml
  title: ''
  type: Spectral
  url: rules/cfx-labs-rules.yml
- group: design
  href: https://artifacts.apis.io/cfx-labs/vocabulary/cfx-labs-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cfx-labs-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cfx-labs/asyncapi/cfx-labs-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cfx-labs-webhooks.yml
- group: design
  href: https://artifacts.apis.io/cfx-labs/conventions/cfx-labs-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cfx-labs-conventions.yml
- group: design
  href: https://artifacts.apis.io/cfx-labs/conventions/cfx-labs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cfx-labs-conventions.yml
- group: design
  href: https://artifacts.apis.io/cfx-labs/errors/cfx-labs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cfx-labs-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cfx-labs/conformance/cfx-labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cfx-labs-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cfx-labs/llms/cfx-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cfx-labs-llms.txt
- group: agent
  href: https://artifacts.apis.io/cfx-labs/well-known/cfx-labs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cfx-labs-well-known.yml
- group: other
  href: https://artifacts.apis.io/cfx-labs/hosts/cfx-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cfx-labs-hosts.yml
- group: other
  href: https://artifacts.apis.io/cfx-labs/vendors/cfx-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cfx-labs-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cfx.to
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cfx.to/reference
- group: auth
  href: https://artifacts.apis.io/cfx-labs/authentication/cfx-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cfx-labs-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cfx-labs/security/cfx-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cfx-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cfx.to/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cfx.to/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cfx.to/developers
- group: other
  title: ''
  type: Company
  url: https://cfx.to/company
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cfx.to/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cfx.to/legal/privacy-policy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://docs.cfx.to/mcp
  - status: 403
    url: https://api.cfx.to/mcp
  - status: 200
    url: https://cfx.to/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: partner-login
  state: gated
created: '2026-10-07'
description: CFX Labs provides programmable U.S. banking APIs for global platforms, offering ACH, wire, RTP, cash deposits, virtual accounts, and on‑chain settlement. The fintech‑focused service aggregates deposits across 3,000+ FDIC‑insured banks, tokenizes balances 1:1, and delivers compliance, KYC, and risk controls via a single integration. Backed by multiple venture firms, CFX serves marketplaces, neobanks, card programs, exchanges, and lenders, handling over $1 B in payment volume in 2025 across 67 countries.
image: https://cfx.to/opengraph-image?02d7fabe23a86c5f
layout: provider
modified: '2026-10-07'
name: CFX Labs
nav: Providers
network: true
overview: 'CFX Labs publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cash API, Deposit API, Deposit Memos API, and 8 more. Tagged areas include Fintech, Banking, Payments, Programmable, and Company.


  The CFX Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  CFX Labs'' developer surface includes API reference, authentication, documentation, and 19 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: CFX Labs API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 3
    warn: 1
  slug: cfx-labs-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 60.0
    developer_ergonomics: 38.1
    discoverability: 71.4
    operational_transparency: 7.9
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 23.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cfx Labs Authentication
  slug: cfx-labs-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cfx Labs Domain Security
  slug: cfx-labs-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: cfx-labs
tags:
- Fintech
- Banking
- Payments
- Programmable
- Company
website: https://cfx.to/
---
