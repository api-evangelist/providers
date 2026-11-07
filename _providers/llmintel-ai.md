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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Llmintel Ai Agentic Access
  operation_count: 6
  slug: llmintel-ai-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 1
apis:
- baseURL: https://llmintel.ai
  baseurl_source: declared
  description: Side-by-side comparison of models across cost, performance, and lifecycle.
  name: llmintel-ai Compare API
  slug: llmintel-ai-compare-api
- baseURL: https://llmintel.ai
  baseurl_source: declared
  description: Lifecycle change events for incremental polling.
  name: llmintel-ai Events API
  slug: llmintel-ai-events-api
- baseURL: https://llmintel.ai
  baseurl_source: declared
  description: Tracked models and their current canonical lifecycle state.
  name: llmintel-ai Models API
  slug: llmintel-ai-models-api
- baseURL: https://llmintel.ai
  baseurl_source: declared
  description: Public freshness / SLA transparency signal.
  name: llmintel-ai Status API
  slug: llmintel-ai-status-api
- baseURL: https://llmintel.ai
  baseurl_source: declared
  description: Ingest runtime model usage for cost analysis and model discovery.
  name: llmintel-ai Telemetry API
  slug: llmintel-ai-telemetry-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/llmintel-ai/agentic-access/llmintel-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/llmintel-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/llmintel-ai/rules/llmintel-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/llmintel-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/llmintel-ai/json-ld/llmintel-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/llmintel-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/llmintel-ai/vocabulary/llmintel-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/llmintel-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/llmintel-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/llmintel-ai/data-model/llmintel-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/llmintel-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/llmintel-ai/changelog/llmintel-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/llmintel-ai-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://llmintel.ai/security
- group: auth
  href: https://artifacts.apis.io/llmintel-ai/security/llmintel-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/llmintel-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/llmintel-ai/authentication/llmintel-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/llmintel-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/llmintel-ai/errors/llmintel-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/llmintel-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/llmintel-ai/conformance/llmintel-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/llmintel-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/llmintel-ai/well-known/llmintel-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/llmintel-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/llmintel-ai/hosts/llmintel-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/llmintel-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/llmintel-ai/vendors/llmintel-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/llmintel-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/llmintel-ai/packages/llmintel-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/llmintel-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/llmintel-ai/packages/llmintel-ai-packages.yml
  title: ''
  type: Packages
  url: packages/llmintel-ai-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://llmintel.ai/changelog
- group: auth
  href: https://artifacts.apis.io/llmintel-ai/security/llmintel-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/llmintel-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/llmintel-ai/security/llmintel-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/llmintel-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/llmintel-ai/security/llmintel-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/llmintel-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://llmintel.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://llmintel.ai/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://llmintel.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://llmintel.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://llmintel.ai/demo
- group: operate
  title: ''
  type: Support
  url: https://llmintel.ai/dashboard
- group: commercial
  title: ''
  type: Pricing
  url: https://llmintel.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://llmintel.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://llmintel.ai/privacy
created: '2026-10-30'
description: LLMIntel provides runtime telemetry for large language model (LLM) cost, usage, and optimization. It meters every model call across OpenAI, Anthropic, Azure, AWS Bedrock, and Google, showing real spend by app, environment, and key. It flags cheaper on‑par alternatives and warns before model deprecation. Free under $300/mo of tracked spend, with paid plans scaling with usage.
image: https://llmintel.ai/opengraph-image?a0ab1b6b7a9530c6
json_schemas:
- name: Comparison
  property_count: 3
  slug: llmintel-ai-comparison
- name: Event
  property_count: 6
  slug: llmintel-ai-event
- name: ModelDetail
  property_count: 16
  slug: llmintel-ai-model-detail
- name: Model
  property_count: 12
  slug: llmintel-ai-model
- name: Status
  property_count: 6
  slug: llmintel-ai-status
- name: TelemetryRequest
  property_count: 1
  slug: llmintel-ai-telemetry-request
jsonld:
- class_count: 8
  name: Llmintel Ai Context
  property_count: 42
  slug: llmintel-ai-context
layout: provider
modified: '2026-10-30'
name: llmintel-ai
nav: Providers
network: true
overview: 'llmintel-ai publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Compare API, Events API, Models API, and 2 more. Tagged areas include Artificial Intelligence, Cost, Observability, Telemetry, and Generative AI.


  The llmintel-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  llmintel-ai''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, pricing, and 23 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: llmintel-ai API Rules
  rule_count: 19
  severity_counts:
    error: 16
    hint: 0
    info: 2
    warn: 1
  slug: llmintel-ai-rules
scopes:
- name: Llmintel Ai Scopes
  scope_count: 0
  slug: llmintel-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 27.6
    contract_governance: 22.0
    contract_quality: 65.6
    developer_ergonomics: 46.9
    discoverability: 66.1
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 35.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/llmintel-ai/llmintel-ai-2026-11-03T134957.png
security:
- kind: authentication
  name: Llmintel Ai Authentication
  slug: llmintel-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Llmintel Ai Domain Security
  slug: llmintel-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Llmintel Ai Vulnerability Disclosure
  slug: llmintel-ai-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Llmintel Ai Trust Center
  slug: llmintel-ai-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
skill_count: 6
skills:
- name: compare-models
  slug: compare-models
- name: get-model
  slug: get-model
- name: get-status
  slug: get-status
- name: ingest-telemetry
  slug: ingest-telemetry
- name: list-events
  slug: list-events
- name: list-models
  slug: list-models
slug: llmintel-ai
tags:
- Artificial Intelligence
- Cost
- Observability
- Telemetry
- Generative AI
website: https://llmintel.ai/
---
