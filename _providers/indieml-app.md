---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Indieml App Agentic Access
  operation_count: 4
  slug: indieml-app-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- description: The Keys API from indieml-app — 1 operation(s) for keys.
  name: indieml-app Keys API
  slug: indieml-app-keys-api
- description: The Score API from indieml-app — 3 operation(s) for score.
  name: indieml-app Score API
  slug: indieml-app-score-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/indieml-app/agentic-access/indieml-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/indieml-app-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/indieml-app/plans/indieml-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/indieml-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/indieml-app/rules/indieml-app-rules.yml
  title: ''
  type: Spectral
  url: rules/indieml-app-rules.yml
- group: design
  href: https://artifacts.apis.io/indieml-app/json-ld/indieml-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/indieml-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/indieml-app/vocabulary/indieml-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/indieml-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/indieml-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/indieml-app/data-model/indieml-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/indieml-app-data-model.yml
- group: auth
  href: https://artifacts.apis.io/indieml-app/authentication/indieml-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/indieml-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/indieml-app/errors/indieml-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/indieml-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/indieml-app/conformance/indieml-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/indieml-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/indieml-app/llms/indieml-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/indieml-app-llms.txt
- group: other
  href: https://artifacts.apis.io/indieml-app/hosts/indieml-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/indieml-app-hosts.yml
- group: build
  href: https://artifacts.apis.io/indieml-app/packages/indieml-app-packages.yml
  title: ''
  type: SDKs
  url: packages/indieml-app-packages.yml
- group: build
  href: https://artifacts.apis.io/indieml-app/packages/indieml-app-packages.yml
  title: ''
  type: Packages
  url: packages/indieml-app-packages.yml
- group: auth
  href: https://artifacts.apis.io/indieml-app/security/indieml-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/indieml-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://indieml.app/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://indieml.app/docs
- group: docs
  title: ''
  type: Documentation
  url: https://indieml.app/docs
- group: docs
  title: ''
  type: APIReference
  url: https://indieml.app/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://indieml.app/#pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ezchx/indieml
created: '2026-10-30'
description: IndieML provides the Substance API, a high‑speed, transformer‑based service that evaluates digital text for substance, depth, and clarity in under 25 ms. Designed for high‑volume pipelines, it filters content without semantic bias, offering free and paid plans, SDKs for Python and Node.js, and integrations with LangChain, Salesforce, and Zendesk. The API runs on an asynchronous FastAPI backend with INT8‑quantized ONNX models, ensuring low latency and privacy by never storing user text.
image: https://indieml.app/images/final-logo.svg
json_schemas:
- name: KeyRequest
  property_count: 1
  slug: indieml-app-key-request
- name: ScoreBatchRequest
  property_count: 1
  slug: indieml-app-score-batch-request
- name: ScoreBatchResponse
  property_count: 1
  slug: indieml-app-score-batch-response
- name: ScoreRequest
  property_count: 1
  slug: indieml-app-score-request
- name: ScoreResponse
  property_count: 1
  slug: indieml-app-score-response
jsonld:
- class_count: 8
  name: Indieml App Context
  property_count: 13
  slug: indieml-app-context
layout: provider
modified: '2026-10-30'
name: indieml-app
nav: Providers
network: true
overview: 'indieml-app publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Keys API and Score API. Tagged areas include AI, NLP, Text-Analysis, Machine-Learning, and API.


  The indieml-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  indieml-app''s developer surface includes authentication, documentation, API reference, pricing, and 17 more developer resources.'
plans:
- name: Indieml App Plans Pricing
  plan_count: 4
  slug: indieml-app-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Indieml App Rate Limits
  slug: indieml-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: indieml-app API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: indieml-app-rules
scopes:
- name: Indieml App Scopes
  scope_count: 0
  slug: indieml-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 83.5
    catalog_earned_first_party: 0.0
    catalog_gap: 31.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 38.9
    contract_governance: 79.1
    contract_quality: 54.0
    developer_ergonomics: 51.7
    discoverability: 57.1
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Indieml App Authentication
  slug: indieml-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Indieml App Domain Security
  slug: indieml-app-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: score-text
  slug: score-text
slug: indieml-app
tags:
- AI
- NLP
- Text-Analysis
- Machine-Learning
- API
website: https://indieml.app/
---
