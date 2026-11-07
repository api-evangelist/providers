---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Decide Fyi Agentic Access
  operation_count: 28
  slug: decide-fyi-agentic-access
  summary_line: 28 operations · 10 acting
api_count: 1
apis:
- baseURL: https://www.decide.fyi
  baseurl_source: declared
  description: Record target-system neutral receipts proving whether the action authorized by a Decision Record was executed, skipped, failed, blocked, or reverted.
  name: decide-fyi Action Execution API
  slug: decide-fyi-action-execution-api
- baseURL: https://www.decide.fyi
  baseurl_source: declared
  description: Explainable outcome-based anomaly reports scoped to the caller API key.
  name: decide-fyi Anomalies API
  slug: decide-fyi-anomalies-api
- baseURL: https://www.decide.fyi
  baseurl_source: declared
  description: Caller-scoped cryptographic audit trails with rolling Merkle roots and retained-link verification.
  name: decide-fyi Audit Chain API
  slug: decide-fyi-audit-chain-api
- baseURL: https://www.decide.fyi
  baseurl_source: declared
  description: Opt-in anonymized cross-customer benchmarks with minimum privacy thresholds.
  name: decide-fyi Benchmarks API
  slug: decide-fyi-benchmarks-api
- baseURL: https://www.decide.fyi
  baseurl_source: declared
  description: Predictive decision confidence from caller-scoped Outcome Records.
  name: decide-fyi Confidence API
  slug: decide-fyi-confidence-api
- baseURL: https://www.decide.fyi
  baseurl_source: declared
  description: Simulation-only what-if analysis for stored Decision Records.
  name: decide-fyi Counterfactuals API
  slug: decide-fyi-counterfactuals-api
- baseURL: https://www.decide.fyi
  baseurl_source: declared
  description: Record CRM write-back and inbound sync receipts linked to Decision Records.
  name: decide-fyi CRM Sync API
  slug: decide-fyi-crm-sync-api
- baseURL: https://www.decide.fyi
  baseurl_source: declared
  description: Portable Decision Packet v1 exports that bundle a Decision Record with execution, outcome, intelligence, and audit-chain proof material.
  name: decide-fyi Decision Packets API
  slug: decide-fyi-decision-packets-api
- baseURL: https://www.decide.fyi
  baseurl_source: declared
  description: Core decide, replay, diff, verification, readiness, and registry endpoints.
  name: decide-fyi Decision Protocol API
  slug: decide-fyi-decision-protocol-api
- baseURL: https://www.decide.fyi
  baseurl_source: declared
  description: Outcome-based policy effectiveness scoring scoped to the caller API key.
  name: decide-fyi Effectiveness API
  slug: decide-fyi-effectiveness-api
- baseURL: https://www.decide.fyi
  baseurl_source: declared
  description: Report and read what happened after a Decision Record authorized or routed an action.
  name: decide-fyi Outcome Tracking API
  slug: decide-fyi-outcome-tracking-api
- baseURL: https://www.decide.fyi
  baseurl_source: declared
  description: First-party Decision API pattern templates for common state-changing integrations.
  name: decide-fyi Policy Patterns API
  slug: decide-fyi-policy-patterns-api
- baseURL: https://www.decide.fyi
  baseurl_source: declared
  description: Receipt key and policy bundle registries.
  name: decide-fyi Registries API
  slug: decide-fyi-registries-api
- baseURL: https://www.decide.fyi
  baseurl_source: declared
  description: Hosted and exported Decision Record verification.
  name: decide-fyi Verification API
  slug: decide-fyi-verification-api
artifact_total: 29
common:
- group: agent
  href: https://artifacts.apis.io/decide-fyi/agentic-access/decide-fyi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/decide-fyi-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/decide-fyi/plans/decide-fyi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/decide-fyi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/decide-fyi/rules/decide-fyi-rules.yml
  title: ''
  type: Spectral
  url: rules/decide-fyi-rules.yml
- group: design
  href: https://artifacts.apis.io/decide-fyi/json-ld/decide-fyi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/decide-fyi-context.jsonld
- group: design
  href: https://artifacts.apis.io/decide-fyi/vocabulary/decide-fyi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/decide-fyi-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/decide-fyi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/decide-fyi/data-model/decide-fyi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/decide-fyi-data-model.yml
- group: design
  href: https://artifacts.apis.io/decide-fyi/conventions/decide-fyi-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/decide-fyi-conventions.yml
- group: design
  href: https://artifacts.apis.io/decide-fyi/conventions/decide-fyi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/decide-fyi-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.decide.fyi/resources/trust
- group: auth
  href: https://artifacts.apis.io/decide-fyi/authentication/decide-fyi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/decide-fyi-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.decide.fyi/resources/status
- group: design
  href: https://artifacts.apis.io/decide-fyi/lifecycle/decide-fyi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/decide-fyi-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/decide-fyi/errors/decide-fyi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/decide-fyi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/decide-fyi/conformance/decide-fyi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/decide-fyi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/decide-fyi/llms/decide-fyi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/decide-fyi-llms.txt
- group: other
  href: https://artifacts.apis.io/decide-fyi/a2a/decide-fyi-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/decide-fyi-a2a.yml
- group: agent
  href: https://artifacts.apis.io/decide-fyi/mcp/decide-fyi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/decide-fyi-mcp.yml
- group: agent
  href: https://artifacts.apis.io/decide-fyi/well-known/decide-fyi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/decide-fyi-well-known.yml
- group: other
  href: https://artifacts.apis.io/decide-fyi/hosts/decide-fyi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/decide-fyi-hosts.yml
- group: other
  href: https://artifacts.apis.io/decide-fyi/vendors/decide-fyi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/decide-fyi-vendors.yml
- group: build
  href: https://artifacts.apis.io/decide-fyi/packages/decide-fyi-packages.yml
  title: ''
  type: Packages
  url: packages/decide-fyi-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.decide.fyi/resources/security
- group: build
  title: ''
  type: SDKs
  url: https://www.decide.fyi/sdk
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.decide.fyi/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.decide.fyi/resources/changelog
- group: auth
  href: https://artifacts.apis.io/decide-fyi/security/decide-fyi-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/decide-fyi-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/decide-fyi/security/decide-fyi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decide-fyi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://decide.fyi/
- group: docs
  title: ''
  type: Documentation
  url: https://www.decide.fyi/resources/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.decide.fyi/resources/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.decide.fyi/resources/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.decide.fyi/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.decide.fyi/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.decide.fyi/privacy
created: '2026-10-29'
description: Decide provides a Decision API and a prepaid runtime that enables developers to evaluate business rules before actions are taken. The platform offers versioned rulebooks, schema validation, conformance indexes, and replayable decision records. Pricing includes a $10 per 1,000 decisions prepaid plan and additional enterprise options. Comprehensive documentation, quickstart guides, and API reference are hosted at https://www.decide.fyi/resources/docs. The service enforces rate limits of 20 requests per minute per API key and supports idempotent decision calls.
image: https://www.decide.fyi/assets/social/20261014a-1fe80b709e396e2a/home.png
json_schemas:
- name: DecisionBenchmark
  property_count: 13
  slug: decide-fyi-decision-benchmark
- name: DecisionExecution
  property_count: 37
  slug: decide-fyi-decision-execution
- name: DecisionOutcome
  property_count: 30
  slug: decide-fyi-decision-outcome
- name: DecisionRecord
  property_count: 47
  slug: decide-fyi-decision-record
- name: PolicyAnomalyReport
  property_count: 20
  slug: decide-fyi-policy-anomaly-report
- name: PolicyEffectiveness
  property_count: 21
  slug: decide-fyi-policy-effectiveness
jsonld:
- class_count: 56
  name: Decide Fyi Context
  property_count: 316
  slug: decide-fyi-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.decide.fyi.
  name: decide-fyi MCP Server
  slug: decide-fyi-mcp-yml
modified: '2026-10-29'
name: decide-fyi
nav: Providers
network: true
overview: 'decide-fyi publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Action Execution API, Anomalies API, Audit Chain API, and 11 more. Tagged areas include Decision API, Rule Engine, Software-as-a-Service, Automation, and Runtime.


  The decide-fyi catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  decide-fyi''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, pricing, and 29 more developer resources.'
plans:
- name: Decide Fyi Plans Pricing
  plan_count: 4
  slug: decide-fyi-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Decide Fyi Rate Limits
  slug: decide-fyi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: decide-fyi API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: decide-fyi-rules
score:
  band: developing
  composite: 51.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.5
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 61.9
    developer_ergonomics: 39.9
    discoverability: 75.0
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 62.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/decide-fyi/decide-fyi-2026-11-03T130401.png
security:
- kind: authentication
  name: Decide Fyi Authentication
  slug: decide-fyi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Decide Fyi Domain Security
  slug: decide-fyi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Decide Fyi Trust Center
  slug: decide-fyi-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: decide-fyi
tags:
- Decision API
- Rule Engine
- Software-as-a-Service
- Automation
- Runtime
website: https://decide.fyi/
---
