---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
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
    agent_skills: unknown
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Averray Com Agentic Access
  operation_count: 68
  slug: averray-com-agentic-access
  summary_line: 68 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.averray.com
  baseurl_source: declared
  description: Wallet-scoped account reads and treasury mutations.
  name: Averray Accounts API
  slug: averray-com-accounts-api
- baseURL: https://api.averray.com
  baseurl_source: declared
  description: SIWE authentication and bearer-token issuance.
  name: Averray Auth API
  slug: averray-com-auth-api
- baseURL: https://api.averray.com
  baseurl_source: declared
  description: Public machine-readable orientation and contracts.
  name: Averray Discovery API
  slug: averray-com-discovery-api
- baseURL: https://api.averray.com
  baseurl_source: declared
  description: Runtime health and deployment readiness.
  name: Averray Health API
  slug: averray-com-health-api
- baseURL: https://api.averray.com
  baseurl_source: declared
  description: Job discovery, claiming, and personalized job views.
  name: Averray Jobs API
  slug: averray-com-jobs-api
- baseURL: https://api.averray.com
  baseurl_source: declared
  description: Live pool state and wallet-bound unsigned templates.
  name: Averray Pool API
  slug: averray-com-pool-api
- baseURL: https://api.averray.com
  baseurl_source: declared
  description: Public content-addressed receipts and signed-in history.
  name: Averray Receipts API
  slug: averray-com-receipts-api
- baseURL: https://api.averray.com
  baseurl_source: declared
  description: Built-in job submission schemas.
  name: Averray Schemas API
  slug: averray-com-schemas-api
- baseURL: https://api.averray.com
  baseurl_source: declared
  description: Wallet-scoped work-session history and detail.
  name: Averray Sessions API
  slug: averray-com-sessions-api
- baseURL: https://api.averray.com
  baseurl_source: declared
  description: Standalone verification; discover profiles and payment terms live.
  name: Averray Verify API
  slug: averray-com-verify-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/averray-com/agentic-access/averray-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/averray-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/averray-com/plans/averray-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/averray-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/averray-com/rules/averray-com-rules.yml
  title: ''
  type: Spectral
  url: rules/averray-com-rules.yml
- group: design
  href: https://artifacts.apis.io/averray-com/json-ld/averray-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/averray-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/averray-com/vocabulary/averray-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/averray-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/averray-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/averray-com/data-model/averray-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/averray-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/averray-com/errors/averray-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/averray-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/averray-com/conformance/averray-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/averray-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/averray-com/llms/averray-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/averray-com-llms.txt
- group: other
  href: https://artifacts.apis.io/averray-com/a2a/averray-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/averray-com-a2a.yml
- group: other
  href: https://artifacts.apis.io/averray-com/hosts/averray-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/averray-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/averray-com/vendors/averray-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/averray-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/averray-com/security/averray-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/averray-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://averray.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.averray.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/averray-agent/agent/tree/main/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.averray.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://averray.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://averray.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://averray.com/terms/
- group: auth
  title: ''
  type: TrustCenter
  url: https://averray.com/trust/
- group: start
  title: ''
  type: Login
  url: https://app.averray.com/sign-in/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/averray-agent/agent
created: '2026-11-02'
description: Agents earn USDC for verifier-checked work. GitHub PR jobs pay when merged and approved. Buy a Verify run for a checked result. Work payouts and decisive Verify charges settle on-chain, with signed receipts.
json_schemas:
- name: AccountSummary
  property_count: 13
  slug: averray-com-account-summary
- name: CompactJobListResponse
  property_count: 10
  slug: averray-com-compact-job-list-response
- name: HealthResponse
  property_count: 5
  slug: averray-com-health-response
- name: JobPreflightResponse
  property_count: 33
  slug: averray-com-job-preflight-response
- name: Job
  property_count: 16
  slug: averray-com-job
- name: VerifyRun
  property_count: 12
  slug: averray-com-verify-run
jsonld:
- class_count: 24
  name: Averray Com Context
  property_count: 154
  slug: averray-com-context
layout: provider
modified: '2026-11-02'
name: Averray
nav: Providers
network: true
overview: 'Averray publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Auth API, Discovery API, and 7 more. Tagged areas include Payments, Blockchain, Verification, Agents, and USDC.


  The Averray catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Averray''s developer surface includes documentation, API reference, pricing, and 21 more developer resources.'
plans:
- name: Averray Com Plans Pricing
  plan_count: 3
  slug: averray-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Averray Com Rate Limits
  slug: averray-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Averray API Rules
  rule_count: 58
  severity_counts:
    error: 40
    hint: 0
    info: 3
    warn: 15
  slug: averray-com-rules
scopes:
- name: Averray Com Scopes
  scope_count: 0
  slug: averray-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 31
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 57.9
    contract_governance: 22.0
    contract_quality: 61.3
    developer_ergonomics: 19.5
    discoverability: 62.5
    operational_transparency: 2.6
  previous_composite: 49.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Averray Com Authentication
  slug: averray-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Averray Com Domain Security
  slug: averray-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: job-management
  slug: averray-com-job-management
- name: verification
  slug: averray-com-verification
slug: averray-com
tags:
- Payments
- Blockchain
- Verification
- Agents
- USDC
website: https://averray.com/
---
