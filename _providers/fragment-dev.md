---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-01'
api_count: 6
apis:
- description: Single GraphQL endpoint for defining a ledger Schema, creating Ledgers, posting balanced double-entry Ledger Entries, and reading balances and lines. All write mutations are idempotent via an idempote
  name: Fragment Ledger GraphQL API
  slug: fragment-ledger-graphql-api
- description: Define and version the ledger Schema - the chart of accounts, account types (asset, liability, income, expense), currency modes, and the ledger entry types your product posts. Stored with the storeSch
  name: Fragment Schema API
  slug: fragment-schema-api
- description: Create and query Ledgers from a stored Schema. A Ledger is an isolated database for tracking money for a use case, tenant, or environment, created with createLedger and read with the ledger query.
  name: Fragment Ledgers API
  slug: fragment-ledgers-api
- description: Post immutable, balanced double-entry Ledger Entries made of debit and credit lines against accounts. Uses addLedgerEntry with an idempotency key (ik), reverseLedgerEntry to correct posted entries, an
  name: Fragment Ledger Entries API
  slug: fragment-ledger-entries-api
- description: Read real-time balances and the underlying lines. Query overall ledger balances (getLedgerBalances), per-account balances (getLedgerAccountBalances), and the debit/credit lines behind an account (getL
  name: Fragment Balances API
  slug: fragment-balances-api
- description: Match ledger activity against external money movement. reconcileTx reconciles a transaction idempotently by transaction ID, while syncCustomAccounts and syncCustomTxs ingest external accounts and tran
  name: Fragment Reconciliation API
  slug: fragment-reconciliation-api
artifact_total: 12
collections:
- collection_type: open
  name: Fragment Ledger GraphQL API
  slug: open-fragment-dev
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fragment-dev-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fragment-dev
- group: company
  title: ''
  type: Website
  url: https://fragment.dev
- group: docs
  title: ''
  type: Documentation
  url: https://fragment.dev/docs
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.fragment.dev
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fragment.dev
- group: operate
  title: ''
  type: ChangeLog
  url: https://fragment.dev/changelog
- group: commercial
  title: ''
  type: Plans
  url: plans/fragment-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fragment-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fragment-dev-finops.yml
created: '2026-07-01'
description: Fragment is a ledger API for engineering teams. It provides a real-time, double-entry ledger to track money movement, model balances, and reconcile against external systems (banks, processors, PSPs). The product is GraphQL-first - developers define a Schema (chart of accounts and entry types), create Ledgers, post immutable Ledger Entries composed of balanced debit/credit lines, and read balances and lines back through a single GraphQL endpoint. Every write mutation is idempotent.
finops:
- name: Fragment Dev Finops
  service_category: Financial Infrastructure
  slug: fragment-dev-finops
graphqls:
- description: Fragment (fragment.dev) is a ledger API for engineering teams. It provides a
  name: Fragment Ledger GraphQL API
  slug: fragment-dev-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fragment-dev.png
layout: provider
modified: '2026-07-01'
name: Fragment
nav: Providers
network: true
overview: 'Fragment publishes 1 API on the [APIs.io](https://apis.io/) network: Ledger GraphQL API. Tagged areas include Ledger, Double-Entry, Accounting, Fintech, and Payments.


  Fragment''s developer surface includes documentation, signup flow, changelog, and 7 more developer resources.'
plans:
- name: Fragment Dev Plans Pricing
  plan_count: 3
  slug: fragment-dev-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Fragment Dev Rate Limits
  slug: fragment-dev-rate-limits
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 52.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 32.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fragment-dev/refs/heads/main/screenshots/fragment-dev-2026-07-25T215118.png
security:
- kind: domain-security
  name: Fragment Dev Domain Security
  slug: fragment-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: fragment-dev
tags:
- Ledger
- Double-Entry
- Accounting
- Fintech
- Payments
- Reconciliation
- GraphQL
- Balances
website: https://fragment.dev
---
