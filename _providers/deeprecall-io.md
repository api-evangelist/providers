---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Deeprecall Io Agentic Access
  operation_count: 5
  slug: deeprecall-io-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://api.deeprecall.io
  baseurl_source: declared
  description: System health and status endpoints
  name: DeepRecall Health API
  slug: deeprecall-io-health-api
- baseURL: https://api.deeprecall.io
  baseurl_source: declared
  description: Product recall data endpoints
  name: DeepRecall Recalls API
  slug: deeprecall-io-recalls-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/deeprecall-io/agentic-access/deeprecall-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deeprecall-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/deeprecall-io/rate-limits/deeprecall-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/deeprecall-io-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/deeprecall-io/rules/deeprecall-io-rules.yml
  title: ''
  type: Spectral
  url: rules/deeprecall-io-rules.yml
- group: design
  href: https://artifacts.apis.io/deeprecall-io/json-ld/deeprecall-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deeprecall-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/deeprecall-io/vocabulary/deeprecall-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deeprecall-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/deeprecall-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/deeprecall-io/data-model/deeprecall-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deeprecall-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/deeprecall-io/conventions/deeprecall-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/deeprecall-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/deeprecall-io/authentication/deeprecall-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deeprecall-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/deeprecall-io/errors/deeprecall-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/deeprecall-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/deeprecall-io/conformance/deeprecall-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deeprecall-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/deeprecall-io/llms/deeprecall-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deeprecall-io-llms.txt
- group: other
  href: https://artifacts.apis.io/deeprecall-io/a2a/deeprecall-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/deeprecall-io-a2a.yml
- group: other
  href: https://artifacts.apis.io/deeprecall-io/hosts/deeprecall-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deeprecall-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/deeprecall-io/vendors/deeprecall-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deeprecall-io-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.deeprecall.io/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.deeprecall.io/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deeprecall.io/
- group: auth
  href: https://artifacts.apis.io/deeprecall-io/security/deeprecall-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deeprecall-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deeprecall.io/
created: '2026-11-05'
description: DeepRecall provides AI‑powered regulatory intelligence for marketplace enforcement, delivering over 120,000 alerts across multiple jurisdictions. The platform automates decision‑making with regulator‑grade evidence and complies with DSA, GPSR, and CPSC standards. It helps businesses monitor and respond to compliance risks efficiently.
image: https://deeprecall.io/assets/images/og-image.jpg
json_schemas:
- name: HealthResponse
  property_count: 4
  slug: deeprecall-io-health-response
- name: RecallsFeedResponse
  property_count: 6
  slug: deeprecall-io-recalls-feed-response
- name: RecallsSimilaritySearchRequest
  property_count: 6
  slug: deeprecall-io-recalls-similarity-search-request
- name: RecallsSimilaritySearchResponse
  property_count: 10
  slug: deeprecall-io-recalls-similarity-search-response
jsonld:
- class_count: 12
  name: Deeprecall Io Context
  property_count: 65
  slug: deeprecall-io-context
layout: provider
modified: '2026-11-05'
name: DeepRecall
nav: Providers
network: true
overview: 'DeepRecall publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Health API and Recalls API. Tagged areas include Artificial Intelligence, Regulatory, Marketplace, Compliance, and Intelligence.


  The DeepRecall catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DeepRecall''s developer surface includes authentication, API reference, getting-started guide, documentation, and 16 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 3
  name: Deeprecall Io Rate Limits
  slug: deeprecall-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: DeepRecall API Rules
  rule_count: 55
  severity_counts:
    error: 48
    hint: 0
    info: 6
    warn: 1
  slug: deeprecall-io-rules
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 57.1
    developer_ergonomics: 46.9
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Deeprecall Io Authentication
  slug: deeprecall-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Deeprecall Io Domain Security
  slug: deeprecall-io-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: get-feed
  slug: deeprecall-io-get-feed
slug: deeprecall-io
tags:
- Artificial Intelligence
- Regulatory
- Marketplace
- Compliance
- Intelligence
website: https://deeprecall.io/
---
