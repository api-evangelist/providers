---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Fragment's GraphQL Ledger API. Store a double-entry chart-of-accounts schema, create ledgers, post idempotent ledger entries and lines, read aggregated / historical / period / strongly-consistent bala
  name: Fragment Ledger API
  slug: fragment-ledger-api
artifact_total: 6
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fragment.dev/docs
- group: docs
  title: ''
  type: Documentation
  url: https://fragment.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://fragment.dev/api-reference/ledger-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://fragment.dev/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://fragment.dev/blog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fragment-changelog.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fragment-dev
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fragment.dev
- group: start
  title: ''
  type: SignUp
  url: https://fragment.dev/get-access
- group: start
  title: ''
  type: Login
  url: https://dashboard.fragment.dev/login
- group: operate
  title: ''
  type: Support
  url: https://fragment.dev/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fragment.dev/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fragment.dev/legal
- group: auth
  title: ''
  type: Security
  url: https://fragment.dev/security
- group: auth
  title: ''
  type: Compliance
  url: https://fragment.dev/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/fragment-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fragment-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fragment-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/fragment-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fragment-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/fragment-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fragment-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fragment-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/fragment-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fragment-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fragment-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fragment-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fragment-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fragment-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fragment-llms.txt
created: '2026-07-17'
description: Fragment is the ledger API for engineers who move money. It provides a double-entry accounting engine — "the database for money" — that lets developers model any funds flow as declarative, typed schemas and post balanced, immutable ledger entries through a GraphQL API. Fragment generates a typesafe SDK from your chart-of-accounts schema, tracks real-time, historical, period, and strongly-consistent balances across multi-currency and custom-currency accounts, and reconciles internal ledgers against external systems (Stripe, Increase, Unit, banks) via linked and external accounts. Every write mutation is idempotent (per-Ledger idempotency keys), responses are GraphQL union types with typed errors, list queries are cursor-paginated, and the API is deployed across AWS regions. Fragment is used by companies including Bill, Ramp, Pleo, AtoB, Basic Capital, and Nala, and is backed by General Catalyst.
image: https://fragment.dev/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: fragment-mcp.yml
  slug: fragment-mcpyml
modified: '2026-07-19'
name: Fragment
nav: Providers
network: true
overview: 'Fragment publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ledger, Accounting, Payments, and Fintech.


  Fragment''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, signup flow, support, and 24 more developer resources.'
random_paper: 107
score:
  band: developing
  composite: 53.0
  delta: 2.1
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 43.3
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 50.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fragment/refs/heads/main/screenshots/fragment-2026-07-25T215102.png
security:
- kind: authentication
  name: Fragment Authentication
  slug: fragment-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Fragment Domain Security
  slug: fragment-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Fragment Vulnerability Disclosure
  slug: fragment-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Fragment Trust Center
  slug: fragment-trust-center
  summary_line: SOC 2 Type II
slug: fragment
tags:
- Company
- Ledger
- Accounting
- Payments
- Fintech
- Double-Entry
- Money Movement
- GraphQL
- Financial Infrastructure
- Reconciliation
website: https://fragment.dev/docs
---
