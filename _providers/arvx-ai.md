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
  band: agent-ready
  dimensions:
    agent_card: false
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
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Arvx Ai Agentic Access
  operation_count: 2
  slug: arvx-ai-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.arvx.ai
  baseurl_source: declared
  description: The Readings API from ARVX — 1 operation(s) for readings.
  name: ARVX Readings API
  slug: arvx-ai-readings-api
- baseURL: https://api.arvx.ai
  baseurl_source: declared
  description: The Records API from ARVX — 1 operation(s) for records.
  name: ARVX Records API
  slug: arvx-ai-records-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/arvx-ai/agentic-access/arvx-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/arvx-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/arvx-ai/plans/arvx-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/arvx-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/arvx-ai/rules/arvx-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/arvx-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/arvx-ai/json-ld/arvx-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arvx-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/arvx-ai/vocabulary/arvx-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arvx-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/arvx-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/arvx-ai/data-model/arvx-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arvx-ai-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://developer.arvx.ai/terms
- group: auth
  href: https://artifacts.apis.io/arvx-ai/authentication/arvx-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arvx-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/arvx-ai/errors/arvx-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arvx-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/arvx-ai/conformance/arvx-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arvx-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arvx-ai/llms/arvx-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arvx-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/arvx-ai/well-known/arvx-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arvx-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/arvx-ai/well-known/arvx-ai-developer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arvx-ai-developer-security.txt
- group: agent
  href: https://artifacts.apis.io/arvx-ai/well-known/arvx-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arvx-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/arvx-ai/hosts/arvx-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arvx-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/arvx-ai/vendors/arvx-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arvx-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.arvx.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://arvx.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.arvx.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.arvx.ai/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.arvx.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.arvx.ai/
- group: auth
  href: https://artifacts.apis.io/arvx-ai/security/arvx-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arvx-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arvx-ai/security/arvx-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arvx-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arvx.ai/
created: '2026-11-01'
description: 'arvx-ai is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: ReadingRequest
  property_count: 4
  slug: arvx-ai-reading-request
- name: Reading
  property_count: 9
  slug: arvx-ai-reading
jsonld:
- class_count: 9
  name: Arvx Ai Context
  property_count: 28
  slug: arvx-ai-context
layout: provider
modified: '2026-11-01'
name: ARVX
nav: Providers
network: true
overview: 'ARVX publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Readings API and Records API. Tagged areas include Company.


  The ARVX catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ARVX''s developer surface includes authentication, support, pricing, getting-started guide, API reference, and 21 more developer resources.'
plans:
- name: Arvx Ai Plans Pricing
  plan_count: 1
  slug: arvx-ai-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Arvx Ai Rate Limits
  slug: arvx-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: ARVX API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: arvx-ai-rules
scopes:
- name: Arvx Ai Scopes
  scope_count: 0
  slug: arvx-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 32
    catalog_earned: 58.8
    catalog_earned_first_party: 8.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 66.0
    developer_ergonomics: 30.2
    discoverability: 44.6
    operational_transparency: 5.3
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arvx Ai Authentication
  slug: arvx-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Arvx Ai Domain Security
  slug: arvx-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Arvx Ai Vulnerability Disclosure
  slug: arvx-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: record-summary
  slug: arvx-ai-record-summary
- name: two-person-fit
  slug: arvx-ai-two-person-fit
slug: arvx-ai
tags:
- Company
website: https://arvx.ai/
---
