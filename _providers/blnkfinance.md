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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Managed Cloud REST surface covering OAuth auth, a Proxy API to a Core instance, Data API, Filters API, Alerts API, and the MCP endpoint. Auth via API keys or OAuth.
  name: Blnk Cloud API
  slug: blnk-cloud-api
- description: Rule-based transaction monitoring API (transaction evaluation, instruction management, Git-backed rule sync). Beta.
  name: Blnk Watch API
  slug: blnk-watch-api
- baseURL: http://localhost:5001
  baseurl_source: declared
  description: The Accounts API from Blnk Finance — 2 operation(s) for accounts.
  name: Blnk Finance Accounts API
  phrasing_intents:
  - id: CreateAccount
    intent: Link a bank account to a balance
    question: How do I attach an external bank account to a ledger balance and an identity?
  - id: UpdateAccount
    intent: Change a bank account's details
    question: How do I correct the bank name or account number on an existing account?
  - id: GetAccount
    intent: Look up a bank account record
    question: Where can I see the bank name and account number stored for an account ID?
  phrasing_ops: 3
  slug: blnkfinance-accounts-api
- baseURL: http://localhost:5001
  baseurl_source: declared
  description: The Backup API from Blnk Finance — 2 operation(s) for backup.
  name: Blnk Finance Backup API
  phrasing_intents:
  - id: BackDB
    intent: Back up the ledger database locally
    question: How do I take a backup of the Blnk database on the server itself?
  - id: BackDBToS3
    intent: Back up the ledger database to Amazon S3
    question: Can I push a backup of the ledger database straight to an S3 bucket?
  phrasing_ops: 2
  slug: blnkfinance-backup-api
- baseURL: http://localhost:5001
  baseurl_source: declared
  description: The Balance Monitors API from Blnk Finance — 2 operation(s) for balance monitors.
  name: Blnk Finance Balance Monitors API
  phrasing_intents:
  - id: CreateBalanceMonitor
    intent: Watch a balance and get notified on a condition
    question: How do I get a webhook callback when a balance drops below a threshold?
  - id: UpdateBalanceMonitor
    intent: Change a balance monitor's condition
    question: Can I change the threshold an existing balance monitor alerts on?
  - id: GetBalanceMonitor
    intent: View a balance monitor's settings
    question: What condition is an existing balance monitor watching for?
  phrasing_ops: 3
  slug: blnkfinance-balance-monitors-api
- baseURL: http://localhost:5001
  baseurl_source: declared
  description: The Balances API from Blnk Finance — 2 operation(s) for balances.
  name: Blnk Finance Balances API
  phrasing_intents:
  - id: CreateBalance
    intent: Open a new balance in a ledger
    question: How do I create a wallet balance in a specific currency inside a ledger?
  - id: GetBalance
    intent: Check a balance's current amount
    question: What is the current amount sitting in a given balance?
  phrasing_ops: 2
  slug: blnkfinance-balances-api
- baseURL: http://localhost:5001
  baseurl_source: declared
  description: The Identities API from Blnk Finance — 2 operation(s) for identities.
  name: Blnk Finance Identities API
  phrasing_intents:
  - id: CreateIdentity
    intent: Register a customer or business identity
    question: How do I add a new customer or organization record with an address in Blnk?
  - id: UpdateIdentity
    intent: Update a person's identity details
    question: How do I change the email address or phone number on an existing identity?
  - id: GetIdentity
    intent: Look up an identity's profile
    question: Where do I see the stored name, address and contact details for an identity ID?
  phrasing_ops: 3
  slug: blnkfinance-identities-api
- baseURL: http://localhost:5001
  baseurl_source: declared
  description: The Ledgers API from Blnk Finance — 2 operation(s) for ledgers.
  name: Blnk Finance Ledgers API
  phrasing_intents:
  - id: Createledger
    intent: Create a new ledger
    question: How do I set up a new ledger to group my balances?
  - id: GetLedger
    intent: Look up a ledger
    question: What name and metadata does an existing ledger have?
  phrasing_ops: 2
  slug: blnkfinance-ledgers-api
- baseURL: http://localhost:5001
  baseurl_source: declared
  description: The Refund Transaction API from Blnk Finance — 1 operation(s) for refund transaction.
  name: Blnk Finance Refund Transaction API
  phrasing_intents:
  - id: RefundTransaction
    intent: Refund a recorded transaction
    question: How do I reverse a transaction that was already recorded in the ledger?
  phrasing_ops: 1
  slug: blnkfinance-refund-transaction-api
- baseURL: http://localhost:5001
  baseurl_source: declared
  description: The Transactions API from Blnk Finance — 2 operation(s) for transactions.
  name: Blnk Finance Transactions API
  phrasing_intents:
  - id: RecordTransaction
    intent: Move money between balances
    question: How do I record a transfer of funds from one balance to another?
  - id: UpdateInflightTransaction
    intent: Commit or void an inflight transaction
    question: How do I commit a transaction that is still on hold as inflight?
  phrasing_ops: 2
  slug: blnkfinance-transactions-api
artifact_total: 35
asyncapis:
- description: ''
  name: Blnkfinance Webhooks
  slug: blnkfinance-webhooks
common:
- group: other
  href: https://artifacts.apis.io/blnkfinance/capabilities/blnkfinance-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/blnkfinance-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.blnkfinance.com/
- group: auth
  href: https://artifacts.apis.io/blnkfinance/security/blnkfinance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blnkfinance-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/blnkfinance/authentication/blnkfinance-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blnkfinance-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.blnkfinance.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blnkfinance.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.blnkfinance.com/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blnkfinance.com/home/install
- group: operate
  title: ''
  type: Support
  url: https://blnkfinance.com/contact/us
- group: company
  title: ''
  type: Blog
  url: https://blnkfinance.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blnkfinance
- group: commercial
  title: ''
  type: Pricing
  url: https://blnkfinance.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.blnkfinance.com/auth/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blnkfinance.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blnkfinance.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blnkfinance.com/
- group: build
  href: https://artifacts.apis.io/blnkfinance/packages/blnkfinance-packages.yml
  title: ''
  type: Packages
  url: packages/blnkfinance-packages.yml
- group: build
  href: https://artifacts.apis.io/blnkfinance/packages/blnkfinance-packages.yml
  title: ''
  type: SDKs
  url: packages/blnkfinance-packages.yml
- group: build
  href: https://artifacts.apis.io/blnkfinance/cli/blnkfinance-cli.yml
  title: ''
  type: CLI
  url: cli/blnkfinance-cli.yml
- group: agent
  href: https://artifacts.apis.io/blnkfinance/well-known/blnkfinance-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blnkfinance-well-known.yml
- group: other
  href: https://artifacts.apis.io/blnkfinance/a2a/blnkfinance-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/blnkfinance-a2a.yml
- group: agent
  href: https://artifacts.apis.io/blnkfinance/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/blnkfinance/llms/blnkfinance-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blnkfinance-llms.txt
- group: other
  href: https://artifacts.apis.io/blnkfinance/overlays/blnkfinance-core-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/blnkfinance-core-overlay.yaml
- group: design
  href: https://artifacts.apis.io/blnkfinance/conformance/blnkfinance-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blnkfinance-conformance.yml
- group: auth
  href: https://artifacts.apis.io/blnkfinance/conformance/blnkfinance-conformance.yml
  title: ''
  type: Compliance
  url: conformance/blnkfinance-conformance.yml
- group: design
  href: https://artifacts.apis.io/blnkfinance/errors/blnkfinance-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/blnkfinance-error-codes.yml
- group: design
  href: https://artifacts.apis.io/blnkfinance/lifecycle/blnkfinance-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/blnkfinance-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/blnkfinance/lifecycle/blnkfinance-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/blnkfinance-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/blnkfinance/scopes/blnkfinance-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/blnkfinance-scopes.yml
- group: auth
  href: https://artifacts.apis.io/blnkfinance/security/blnkfinance-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blnkfinance-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blnkfinance/security/blnkfinance-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/blnkfinance-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blnkfinance/security/blnkfinance-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/blnkfinance-trust-center.yml
- group: start
  href: https://artifacts.apis.io/blnkfinance/sandbox/blnkfinance-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/blnkfinance-sandbox.yml
- group: design
  href: https://artifacts.apis.io/blnkfinance/conventions/blnkfinance-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blnkfinance-conventions.yml
- group: design
  href: https://artifacts.apis.io/blnkfinance/conventions/blnkfinance-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/blnkfinance-conventions.yml
- group: operate
  href: https://artifacts.apis.io/blnkfinance/changelog/blnkfinance-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/blnkfinance-changelog.yml
- group: design
  href: https://artifacts.apis.io/blnkfinance/data-model/blnkfinance-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blnkfinance-data-model.yml
- group: design
  href: https://artifacts.apis.io/blnkfinance/asyncapi/blnkfinance-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/blnkfinance-webhooks.yml
- group: commercial
  href: https://artifacts.apis.io/blnkfinance/plans/blnkfinance-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blnkfinance-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/blnkfinance/rate-limits/blnkfinance-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/blnkfinance-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/blnkfinance/mcp/blnkfinance-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/blnkfinance-mcp.yml
- group: build
  href: https://artifacts.apis.io/blnkfinance/mcp/blnkfinance-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/blnkfinance-tool-crosswalk.yml
- group: operate
  title: ''
  type: Contact
  url: mailto:sales@blnkfinance.com
created: '2026-08-26'
description: Open-source double-entry ledger for financial products (wallets, loans, payouts, escrow, cards). Available as self-hosted Blnk Core (OSS engine) and Blnk Cloud (managed), plus Blnk Watch for transaction monitoring. Exposes REST APIs with a public OpenAPI spec, hosted MCP servers, llms.txt, and installable agent skills.
finops:
- has_sources: true
  method: derived
  name: Blnkfinance Finops
  primary_unit: instance
  service_category: ''
  slug: blnkfinance-finops
  template: false
image: https://blnkfinance.com/_astro/og-default.4FpZOtzr.png
layout: provider
mcp_servers:
- description: 'Open, no-auth Mintlify DOCUMENTATION-SEARCH MCP on a first-party host. Probed live 2026-08-27: initialize + tools/list returned 200, serverInfo "Blnk Finance", protocolVersion 2025-11-25, 3 tools. It '
  name: Blnk Finance MCP Server
  slug: mcp
modified: '2026-08-27'
name: Blnk Finance
nav: Providers
network: true
overview: 'Blnk Finance publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Backup API, Balance Monitors API, and 7 more. Tagged areas include Fintech, Financial Services, Ledger, Double-Entry, and Payments.


  The Blnk Finance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Blnk Finance''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 37 more developer resources.'
plans:
- name: Blnkfinance Plans Pricing
  plan_count: 8
  slug: blnkfinance-plans-pricing
- name: Blnkfinance Price Estimates
  plan_count: 0
  slug: blnkfinance-price-estimates
random_paper: 19
rate_limits:
- limit_count: 2
  name: Blnkfinance Rate Limits
  slug: blnkfinance-rate-limits
scopes:
- name: Blnkfinance Scopes
  scope_count: 24
  slug: blnkfinance-scopes
  summary_line: 24 scopes
score:
  band: exemplar
  composite: 71.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 55.0
    catalog_earned_first_party: 20.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 46.3
    developer_ergonomics: 85.7
    discoverability: 63.3
    operational_transparency: 84.2
  previous_composite: 69.8
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 41.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/blnkfinance/blnkfinance-2026-09-02T144933.png
security:
- kind: authentication
  name: Blnkfinance Authentication
  slug: blnkfinance-authentication
  summary_line: apiKey/http/oauth2 · 0 schemes
- kind: domain-security
  name: Blnkfinance Domain Security
  slug: blnkfinance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Blnkfinance Vulnerability Disclosure
  slug: blnkfinance-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Blnkfinance Trust Center
  slug: blnkfinance-trust-center
  summary_line: ISO/IEC 27001, GDPR, SOC 2, PCI DSS, HIPAA
skill_count: 14
skills:
- name: blnk-core
  slug: blnkfinance-core
- name: blnk-documentation
  slug: blnkfinance-documentation
- name: blnk-fx
  slug: blnkfinance-fx
- name: blnk-implementation
  slug: blnkfinance-implementation
- name: blnk-inflight
  slug: blnkfinance-inflight
- name: blnk-ledger-architecture
  slug: blnkfinance-ledger-architecture
- name: blnk-naming-patterns
  slug: blnkfinance-naming-patterns
- name: blnk-precision
  slug: blnkfinance-precision
- name: blnk-queueing
  slug: blnkfinance-queueing
- name: blnk-sdks
  slug: blnkfinance-sdks
- name: blnk-support
  slug: blnkfinance-support
- name: blnk-transactions
  slug: blnkfinance-transactions
- name: blnk-watch
  slug: blnkfinance-watch
- name: blnk-webhooks
  slug: blnkfinance-webhooks
slug: blnkfinance
tags:
- Fintech
- Financial Services
- Ledger
- Double-Entry
- Payments
- Wallets
- Lending
- Banking Infrastructure
- Open Source
- MCP
- AI Agents
- Developer Tools
- A2A
website: https://www.blnkfinance.com/
---
