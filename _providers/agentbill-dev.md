---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: AgentBill provides a pricing and usage API for model calls, documented at the developer portal.
  name: AgentBill API
  slug: agentbill-api
- description: 'AgentBill API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AgentBill API
  slug: agentbill-dev-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/agentbill-dev/plans/agentbill-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentbill-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentbill-dev/rules/agentbill-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/agentbill-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/agentbill-dev/json-ld/agentbill-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentbill-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentbill-dev/vocabulary/agentbill-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentbill-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentbill-dev/data-model/agentbill-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentbill-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentbill-dev/conventions/agentbill-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agentbill-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentbill-dev/conventions/agentbill-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentbill-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/agentbill-dev/authentication/agentbill-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentbill-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentbill-dev/conformance/agentbill-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentbill-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentbill-dev/llms/agentbill-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentbill-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/agentbill-dev/well-known/agentbill-dev-clawhub-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentbill-dev-clawhub-security.txt
- group: agent
  href: https://artifacts.apis.io/agentbill-dev/well-known/agentbill-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentbill-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentbill-dev/hosts/agentbill-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentbill-dev-hosts.yml
- group: build
  href: https://artifacts.apis.io/agentbill-dev/packages/agentbill-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/agentbill-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/agentbill-dev/packages/agentbill-dev-packages.yml
  title: ''
  type: Packages
  url: packages/agentbill-dev-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentbill.dev/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://agentbill.dev/status
- group: auth
  title: ''
  type: Security
  url: https://agentbill.dev/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentbill.dev/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://agentbill.dev/pricing
- group: start
  title: ''
  type: Login
  url: https://agentbill.dev/login
- group: other
  title: ''
  type: Leadership
  url: https://agentbill.dev/app/upgrade/team
- group: docs
  title: ''
  type: Documentation
  url: https://agentbill.dev/docs
- group: company
  title: ''
  type: Blog
  url: https://agentbill.dev/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://agentbill.dev/docs/first-run
- group: auth
  href: https://artifacts.apis.io/agentbill-dev/security/agentbill-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentbill-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentbill.dev/
coverage:
  checked: '2026-11-01'
  detail: Documentation is HTML only; no OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL files were found.
  evidence:
  - status: 200
    url: https://agentbill.dev/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 'agentbill-dev is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://agentbill.dev/og.png?v=0c66b0f9fa14
json_schemas:
- name: GetTasksTaskrefResponse
  property_count: 7
  slug: agentbill-dev-get-tasks-taskref-response
- name: PostEventsRequest
  property_count: 9
  slug: agentbill-dev-post-events-request
- name: PostPreflightRequest
  property_count: 5
  slug: agentbill-dev-post-preflight-request
- name: PostPreflightResponse
  property_count: 7
  slug: agentbill-dev-post-preflight-response
- name: PutBudgetRequest
  property_count: 2
  slug: agentbill-dev-put-budget-request
- name: PutBudgetResponse
  property_count: 7
  slug: agentbill-dev-put-budget-response
jsonld:
- class_count: 12
  name: Agentbill Dev Context
  property_count: 43
  slug: agentbill-dev-context
layout: provider
modified: '2026-10-31'
name: AgentBill
nav: Providers
network: true
overview: 'AgentBill is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The AgentBill catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentBill''s developer surface includes authentication, pricing, documentation, engineering blog, getting-started guide, and 22 more developer resources.'
plans:
- name: Agentbill Dev Plans Pricing
  plan_count: 4
  slug: agentbill-dev-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: AgentBill API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: agentbill-dev-rules
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 59.8
    catalog_earned_first_party: 12.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 24.7
    developer_ergonomics: 31.0
    discoverability: 40.2
    operational_transparency: 13.2
  previous_composite: 43.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentbill Dev Authentication
  slug: agentbill-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentbill Dev Domain Security
  slug: agentbill-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentbill-dev
tags:
- Company
website: https://agentbill.dev/
---
