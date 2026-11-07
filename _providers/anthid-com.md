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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 22
  human_in_the_loop: 22
  name: Anthid Com Agentic Access
  operation_count: 32
  slug: anthid-com-agentic-access
  summary_line: 32 operations · 22 acting · 22 human-in-the-loop
api_count: 8
apis:
- description: Trading infrastructure API providing controls, accounts, ledger, organizations, intents, billing, instruments, connections.
  name: Anthid API
  slug: anthid-api
- baseURL: https://api.anthid.com
  baseurl_source: declared
  description: Account-level manual control configuration
  name: anthid-com Account Manual Controls API
  slug: anthid-com-account-manual-controls-api
- baseURL: https://api.anthid.com
  baseurl_source: declared
  description: Account-level risk-limit control configuration
  name: anthid-com Account Risk Controls API
  slug: anthid-com-account-risk-controls-api
- baseURL: https://api.anthid.com
  baseurl_source: declared
  description: Account-level time-window control configuration
  name: anthid-com Account Time Controls API
  slug: anthid-com-account-time-controls-api
- baseURL: https://api.anthid.com
  baseurl_source: declared
  description: Effective control-state evaluation
  name: anthid-com Control Evaluation API
  slug: anthid-com-control-evaluation-api
- baseURL: https://api.anthid.com
  baseurl_source: declared
  description: Read manual, risk, and time controls grouped by symbol
  name: anthid-com Effective Controls API
  slug: anthid-com-effective-controls-api
- baseURL: https://api.anthid.com
  baseurl_source: declared
  description: Organization-level control configuration
  name: anthid-com Organization Controls API
  slug: anthid-com-organization-controls-api
- baseURL: https://api.anthid.com
  baseurl_source: declared
  description: Symbol-level manual control configuration
  name: anthid-com Symbol Manual Controls API
  slug: anthid-com-symbol-manual-controls-api
- baseURL: https://api.anthid.com
  baseurl_source: declared
  description: Symbol-level risk-limit control configuration
  name: anthid-com Symbol Risk Controls API
  slug: anthid-com-symbol-risk-controls-api
- baseURL: https://api.anthid.com
  baseurl_source: declared
  description: Symbol-level time-window control configuration
  name: anthid-com Symbol Time Controls API
  slug: anthid-com-symbol-time-controls-api
artifact_total: 36
common:
- group: agent
  href: https://artifacts.apis.io/anthid-com/agentic-access/anthid-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anthid-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/anthid-com/rules/anthid-com-rules.yml
  title: ''
  type: Spectral
  url: rules/anthid-com-rules.yml
- group: design
  href: https://artifacts.apis.io/anthid-com/json-ld/anthid-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anthid-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/anthid-com/vocabulary/anthid-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anthid-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/anthid-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/anthid-com/data-model/anthid-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anthid-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/anthid-com/errors/anthid-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anthid-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/anthid-com/conformance/anthid-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anthid-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anthid-com/llms/anthid-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anthid-com-llms.txt
- group: other
  href: https://artifacts.apis.io/anthid-com/a2a/anthid-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/anthid-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/anthid-com/well-known/anthid-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anthid-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/anthid-com/hosts/anthid-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anthid-com-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.anthid.com/pages/intro/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.anthid.com/
- group: auth
  href: https://artifacts.apis.io/anthid-com/authentication/anthid-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anthid-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/anthid-com/security/anthid-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anthid-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anthid.com/
created: '2026-11-01'
description: 'anthid-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: AccountControl
  property_count: 7
  slug: anthid-com-account-control
- name: AccountRiskControl
  property_count: 9
  slug: anthid-com-account-risk-control
- name: AccountTimeControl
  property_count: 8
  slug: anthid-com-account-time-control
- name: DeletedResponse
  property_count: 4
  slug: anthid-com-deleted-response
- name: EvaluateRequest
  property_count: 5
  slug: anthid-com-evaluate-request
- name: EvaluateResult
  property_count: 2
  slug: anthid-com-evaluate-result
- name: ListControlChangesResponse
  property_count: 2
  slug: anthid-com-list-control-changes-response
- name: ListEffectiveSymbolControlsResponse
  property_count: 2
  slug: anthid-com-list-effective-symbol-controls-response
- name: OrganizationControl
  property_count: 6
  slug: anthid-com-organization-control
- name: PatchControlRequest
  property_count: 3
  slug: anthid-com-patch-control-request
- name: PatchRiskControlRequest
  property_count: 5
  slug: anthid-com-patch-risk-control-request
- name: PatchTimeControlRequest
  property_count: 4
  slug: anthid-com-patch-time-control-request
- name: SymbolControl
  property_count: 8
  slug: anthid-com-symbol-control
- name: SymbolRiskControl
  property_count: 10
  slug: anthid-com-symbol-risk-control
- name: SymbolTimeControl
  property_count: 9
  slug: anthid-com-symbol-time-control
- name: UpsertControlRequest
  property_count: 2
  slug: anthid-com-upsert-control-request
- name: UpsertRiskControlRequest
  property_count: 4
  slug: anthid-com-upsert-risk-control-request
- name: UpsertTimeControlRequest
  property_count: 3
  slug: anthid-com-upsert-time-control-request
jsonld:
- class_count: 57
  name: Anthid Com Context
  property_count: 77
  slug: anthid-com-context
layout: provider
modified: '2026-11-01'
name: anthid-com
nav: Providers
network: true
overview: 'anthid-com publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Manual Controls API, Account Risk Controls API, Account Time Controls API, and 7 more. Tagged areas include Company.


  The anthid-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  anthid-com''s developer surface includes getting-started guide, API reference, authentication, and 14 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 0
  name: Anthid Com Rate Limits
  slug: anthid-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 111
  extends:
  - spectral:oas
  name: anthid-com API Rules
  rule_count: 70
  severity_counts:
    error: 57
    hint: 0
    info: 3
    warn: 10
  slug: anthid-com-rules
scopes:
- name: Anthid Com Scopes
  scope_count: 0
  slug: anthid-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 63.8
    developer_ergonomics: 27.9
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 31.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anthid Com Authentication
  slug: anthid-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Anthid Com Domain Security
  slug: anthid-com-domain-security
  summary_line: DNSSEC · DMARC
skill_count: 1
skills:
- name: account-control
  slug: anthid-com-account-control
slug: anthid-com
tags:
- Company
website: https://anthid.com/
---
