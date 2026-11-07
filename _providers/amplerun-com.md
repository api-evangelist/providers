---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 54
  human_in_the_loop: 5
  name: Amplerun Com Agentic Access
  operation_count: 104
  slug: amplerun-com-agentic-access
  summary_line: 104 operations · 54 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://amplerun-api.spiry.org
  baseurl_source: declared
  description: Profile, sessions, API keys and third-party tokens for the caller.
  name: AmpleRun Account API
  slug: amplerun-com-account-api
- baseURL: https://amplerun-api.spiry.org
  baseurl_source: declared
  description: Operator console. Admin session with TOTP only; API keys are rejected.
  name: AmpleRun Admin API
  slug: amplerun-com-admin-api
- baseURL: https://amplerun-api.spiry.org
  baseurl_source: declared
  description: An AI agent registers its own account with a wallet signature (EIP-4361). No email, no person in the loop.
  name: AmpleRun Agents API
  slug: amplerun-com-agents-api
- baseURL: https://amplerun-api.spiry.org
  baseurl_source: declared
  description: Balances, ledger entries, receipts, funding intents and withdrawals.
  name: AmpleRun Billing API
  slug: amplerun-com-billing-api
- baseURL: https://amplerun-api.spiry.org
  baseurl_source: declared
  description: Public templates and GPU offers. No credential needed.
  name: AmpleRun Catalog API
  slug: amplerun-com-catalog-api
- baseURL: https://amplerun-api.spiry.org
  baseurl_source: declared
  description: Liveness, readiness and public status. No credential needed.
  name: AmpleRun Health API
  slug: amplerun-com-health-api
- baseURL: https://amplerun-api.spiry.org
  baseurl_source: declared
  description: Machines, offers, telemetry, earnings and payouts for hosts. Host scope.
  name: AmpleRun Hosts API
  slug: amplerun-com-hosts-api
- baseURL: https://amplerun-api.spiry.org
  baseurl_source: declared
  description: Quote, reserve, inspect and stop rentals (a job is one rental). Renter scope.
  name: AmpleRun Jobs API
  slug: amplerun-com-jobs-api
- baseURL: https://amplerun-api.spiry.org
  baseurl_source: declared
  description: Support tickets.
  name: AmpleRun Support API
  slug: amplerun-com-support-api
- baseURL: https://amplerun-api.spiry.org
  baseurl_source: declared
  description: SIWE wallet bindings on Base and the payout destination.
  name: AmpleRun Wallets API
  slug: amplerun-com-wallets-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/amplerun-com/agentic-access/amplerun-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amplerun-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/amplerun-com/rate-limits/amplerun-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amplerun-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/amplerun-com/rules/amplerun-com-rules.yml
  title: ''
  type: Spectral
  url: rules/amplerun-com-rules.yml
- group: design
  href: https://artifacts.apis.io/amplerun-com/json-ld/amplerun-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amplerun-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/amplerun-com/vocabulary/amplerun-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amplerun-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/amplerun-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/amplerun-com/data-model/amplerun-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amplerun-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/amplerun-com/conventions/amplerun-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/amplerun-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/amplerun-com/conventions/amplerun-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/amplerun-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/amplerun-com/authentication/amplerun-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amplerun-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/amplerun-com/lifecycle/amplerun-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/amplerun-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/amplerun-com/errors/amplerun-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amplerun-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/amplerun-com/conformance/amplerun-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amplerun-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/amplerun-com/llms/amplerun-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amplerun-com-llms.txt
- group: other
  href: https://artifacts.apis.io/amplerun-com/a2a/amplerun-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/amplerun-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/amplerun-com/mcp/amplerun-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/amplerun-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/amplerun-com/well-known/amplerun-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amplerun-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/amplerun-com/hosts/amplerun-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amplerun-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/amplerun-com/vendors/amplerun-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amplerun-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/amplerun-com/packages/amplerun-com-packages.yml
  title: ''
  type: SDKs
  url: packages/amplerun-com-packages.yml
- group: build
  href: https://artifacts.apis.io/amplerun-com/packages/amplerun-com-packages.yml
  title: ''
  type: Packages
  url: packages/amplerun-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amplerun.com/terms
- group: operate
  title: ''
  type: Support
  url: https://amplerun.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://amplerun.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amplerun.com/privacy
- group: auth
  href: https://artifacts.apis.io/amplerun-com/security/amplerun-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amplerun-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amplerun.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.amplerun.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.amplerun.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://amplerun.com/pricing
- group: start
  title: ''
  type: Login
  url: https://amplerun.com/sign-in
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.amplerun.com/start/renter/
created: '2026-11-01'
description: AmpleRun is a GPU marketplace founded in 2026 by Spiry Research that enables users to deploy AI models, render videos, and run any compute workload on a single click. Users can also earn by hosting their own GPU resources, with a 10% platform fee included in the price. The platform supports NVIDIA CUDA, AMD, and Apple silicon GPUs, offering a searchable catalog where hosts set their own pricing. AmpleRun provides a developer‑friendly experience with documentation, pricing details, and a sign‑in portal for both renters and hosts.
image: https://amplerun.com/brand/amplerun-symbol.svg
json_schemas:
- name: DepositAddress
  property_count: 9
  slug: amplerun-com-deposit-address
- name: Job
  property_count: 16
  slug: amplerun-com-job
- name: OfferSummary
  property_count: 46
  slug: amplerun-com-offer-summary
- name: Quote
  property_count: 21
  slug: amplerun-com-quote
- name: TelemetrySample
  property_count: 2
  slug: amplerun-com-telemetry-sample
- name: Template
  property_count: 21
  slug: amplerun-com-template
jsonld:
- class_count: 26
  name: Amplerun Com Context
  property_count: 166
  slug: amplerun-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at amplerun.com.
  name: AmpleRun MCP Server
  slug: amplerun-com-mcp-yml
modified: '2026-11-01'
name: AmpleRun
nav: Providers
network: true
overview: 'AmpleRun publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Admin API, Agents API, and 7 more. Tagged areas include GPU, Marketplace, Artificial Intelligence, Cloud, and Compute.


  The AmpleRun catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AmpleRun''s developer surface includes authentication, support, documentation, API reference, pricing, getting-started guide, and 26 more developer resources.'
plans:
- name: Amplerun Com Plans Pricing
  plan_count: 0
  slug: amplerun-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Amplerun Com Rate Limits
  slug: amplerun-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AmpleRun API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: amplerun-com-rules
scopes:
- name: Amplerun Com Scopes
  scope_count: 0
  slug: amplerun-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.8
    catalog_earned_first_party: 0.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 57.9
    developer_ergonomics: 42.1
    discoverability: 65.0
    operational_transparency: 13.2
  previous_composite: 49.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Amplerun Com Authentication
  slug: amplerun-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Amplerun Com Domain Security
  slug: amplerun-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: ticket-management
  slug: amplerun-com-ticket-management
slug: amplerun-com
tags:
- GPU
- Marketplace
- Artificial Intelligence
- Cloud
- Compute
website: https://amplerun.com/
---
