---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 52
  human_in_the_loop: 1
  name: Moneyhash Agentic Access
  operation_count: 86
  slug: moneyhash-agentic-access
  summary_line: 86 operations · 52 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://web.moneyhash.io
  baseurl_source: declared
  description: The Accounts API from MoneyHash — 5 operation(s) for accounts.
  name: MoneyHash Accounts API
  slug: moneyhash-accounts-api
- baseURL: https://web.moneyhash.io
  baseurl_source: declared
  description: The Customers API from MoneyHash — 8 operation(s) for customers.
  name: MoneyHash Customers API
  slug: moneyhash-customers-api
- baseURL: https://web.moneyhash.io
  baseurl_source: declared
  description: The Direct API from MoneyHash — 6 operation(s) for direct.
  name: MoneyHash Direct API
  slug: moneyhash-direct-api
- baseURL: https://web.moneyhash.io
  baseurl_source: declared
  description: The External API from MoneyHash — 6 operation(s) for external.
  name: MoneyHash External API
  slug: moneyhash-external-api
- baseURL: https://web.moneyhash.io
  baseurl_source: declared
  description: The Loyalty API from MoneyHash — 4 operation(s) for loyalty.
  name: MoneyHash Loyalty API
  slug: moneyhash-loyalty-api
- baseURL: https://web.moneyhash.io
  baseurl_source: declared
  description: The Payment Links API from MoneyHash — 3 operation(s) for payment links.
  name: MoneyHash Payment Links API
  slug: moneyhash-payment-links-api
- baseURL: https://web.moneyhash.io
  baseurl_source: declared
  description: The Payments API from MoneyHash — 12 operation(s) for payments.
  name: MoneyHash Payments API
  slug: moneyhash-payments-api
- baseURL: https://web.moneyhash.io
  baseurl_source: declared
  description: The Payout API from MoneyHash — 10 operation(s) for payout.
  name: MoneyHash Payout API
  slug: moneyhash-payout-api
- baseURL: https://web.moneyhash.io
  baseurl_source: declared
  description: The Providers API from MoneyHash — 5 operation(s) for providers.
  name: MoneyHash Providers API
  slug: moneyhash-providers-api
- baseURL: https://web.moneyhash.io
  baseurl_source: declared
  description: The Reconciliations API from MoneyHash — 3 operation(s) for reconciliations.
  name: MoneyHash Reconciliations API
  slug: moneyhash-reconciliations-api
- baseURL: https://web.moneyhash.io
  baseurl_source: declared
  description: The Subscriptions API from MoneyHash — 11 operation(s) for subscriptions.
  name: MoneyHash Subscriptions API
  slug: moneyhash-subscriptions-api
- baseURL: https://web.moneyhash.io
  baseurl_source: declared
  description: The Tokens API from MoneyHash — 3 operation(s) for tokens.
  name: MoneyHash Tokens API
  slug: moneyhash-tokens-api
- baseURL: https://web.moneyhash.io
  baseurl_source: declared
  description: The Transactions API from MoneyHash — 1 operation(s) for transactions.
  name: MoneyHash Transactions API
  slug: moneyhash-transactions-api
artifact_total: 22
asyncapis:
- description: ''
  name: Moneyhash Webhooks
  slug: moneyhash-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/moneyhash/agentic-access/moneyhash-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/moneyhash-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/moneyhash/plans/moneyhash-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moneyhash-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/moneyhash/rules/moneyhash-rules.yml
  title: ''
  type: Spectral
  url: rules/moneyhash-rules.yml
- group: design
  href: https://artifacts.apis.io/moneyhash/json-ld/moneyhash-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/moneyhash-context.jsonld
- group: design
  href: https://artifacts.apis.io/moneyhash/vocabulary/moneyhash-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/moneyhash-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/moneyhash/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/moneyhash/asyncapi/moneyhash-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/moneyhash-webhooks.yml
- group: design
  href: https://artifacts.apis.io/moneyhash/data-model/moneyhash-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moneyhash-data-model.yml
- group: start
  href: https://artifacts.apis.io/moneyhash/sandbox/moneyhash-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/moneyhash-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/moneyhash/authentication/moneyhash-authentication.yml
  title: ''
  type: Authentication
  url: authentication/moneyhash-authentication.yml
- group: design
  href: https://artifacts.apis.io/moneyhash/errors/moneyhash-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/moneyhash-problem-types.yml
- group: design
  href: https://artifacts.apis.io/moneyhash/conformance/moneyhash-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moneyhash-conformance.yml
- group: agent
  href: https://artifacts.apis.io/moneyhash/llms/moneyhash-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moneyhash-llms.txt
- group: other
  href: https://artifacts.apis.io/moneyhash/hosts/moneyhash-hosts.yml
  title: ''
  type: Hosts
  url: hosts/moneyhash-hosts.yml
- group: other
  href: https://artifacts.apis.io/moneyhash/vendors/moneyhash-vendors.yml
  title: ''
  type: Vendors
  url: vendors/moneyhash-vendors.yml
- group: build
  href: https://artifacts.apis.io/moneyhash/packages/moneyhash-packages.yml
  title: ''
  type: SDKs
  url: packages/moneyhash-packages.yml
- group: build
  href: https://artifacts.apis.io/moneyhash/packages/moneyhash-packages.yml
  title: ''
  type: Packages
  url: packages/moneyhash-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://moneyhash.io/get-started
- group: company
  title: ''
  type: Blog
  url: https://moneyhash.io/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.moneyhash.io/reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moneyhash.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MoneyHash
- group: auth
  href: https://artifacts.apis.io/moneyhash/security/moneyhash-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moneyhash-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://moneyhash.io/
created: '2026-10-26'
description: MoneyHash is a payment orchestration platform targeting emerging and global markets. It offers an all‑in‑one flexible solution for payment processing, revenue operations, and scaling payment infrastructure across growth stages. The service helps businesses build, optimize, and expand their payment capabilities, providing tools for handling transactions, compliance, and financial operations in a unified platform.
image: https://framerusercontent.com/assets/i3qlo7m4yhseSbNPdoVnVXLwVQ.png
jsonld:
- class_count: 120
  name: Moneyhash Context
  property_count: 420
  slug: moneyhash-context
layout: provider
modified: '2026-10-26'
name: MoneyHash
nav: Providers
network: true
overview: 'MoneyHash publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Customers API, Direct API, and 10 more. Tagged areas include Company, Payments, Fintech, and Orchestration.


  The MoneyHash catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  MoneyHash''s developer surface includes sandbox, authentication, getting-started guide, engineering blog, API reference, documentation, and 18 more developer resources.'
plans:
- name: Moneyhash Plans Pricing
  plan_count: 1
  slug: moneyhash-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: MoneyHash API Rules
  rule_count: 12
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 5
  slug: moneyhash-rules
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 51.8
    catalog_earned_first_party: 8.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 68.6
    developer_ergonomics: 43.5
    discoverability: 55.4
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/moneyhash/moneyhash-2026-11-03T135831.png
security:
- kind: authentication
  name: Moneyhash Authentication
  slug: moneyhash-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Moneyhash Domain Security
  slug: moneyhash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: moneyhash-create-and-pay-payment-intent
  slug: moneyhash-create-and-pay-payment-intent
- name: moneyhash-settlement-file-process
  slug: moneyhash-settlement-file-process
slug: moneyhash
tags:
- Company
- Payments
- Fintech
- Orchestration
website: https://moneyhash.io/
---
