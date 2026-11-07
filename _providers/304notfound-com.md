---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: 304Notfound Com Agentic Access
  operation_count: 16
  slug: 304notfound-com-agentic-access
  summary_line: 16 operations · 9 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Answer API from 304NotModified — 1 operation(s) for answer.
  name: 304NotModified Answer API
  slug: 304notfound-com-answer-api
- description: The Ask API from 304NotModified — 1 operation(s) for ask.
  name: 304NotModified Ask API
  slug: 304notfound-com-ask-api
- description: The Calculs sur vos données API from 304NotModified — 3 operation(s) for calculs sur vos données.
  name: 304NotModified Calculs sur vos données API
  slug: 304notfound-com-calculs-sur-vos-donn-es-api
- description: The Comment API from 304NotModified — 1 operation(s) for comment.
  name: 304NotModified Comment API
  slug: 304notfound-com-comment-api
- description: The Domains API from 304NotModified — 1 operation(s) for domains.
  name: 304NotModified Domains API
  slug: 304notfound-com-domains-api
- description: The Feedback API from 304NotModified — 1 operation(s) for feedback.
  name: 304NotModified Feedback API
  slug: 304notfound-com-feedback-api
- description: The Health API from 304NotModified — 1 operation(s) for health.
  name: 304NotModified Health API
  slug: 304notfound-com-health-api
- description: The Keys API from 304NotModified — 1 operation(s) for keys.
  name: 304NotModified Keys API
  slug: 304notfound-com-keys-api
- description: The Llms.txt API from 304NotModified — 1 operation(s) for llms.txt.
  name: 304NotModified Llms.txt API
  slug: 304notfound-com-llms-txt-api
- description: The Services API from 304NotModified — 5 operation(s) for services.
  name: 304NotModified Services API
  slug: 304notfound-com-services-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/304notfound-com/agentic-access/304notfound-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/304notfound-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/304notfound-com/rules/304notfound-com-rules.yml
  title: ''
  type: Spectral
  url: rules/304notfound-com-rules.yml
- group: design
  href: https://artifacts.apis.io/304notfound-com/json-ld/304notfound-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/304notfound-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/304notfound-com/vocabulary/304notfound-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/304notfound-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/304notfound-com/data-model/304notfound-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/304notfound-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/304notfound-com/errors/304notfound-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/304notfound-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/304notfound-com/conformance/304notfound-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/304notfound-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/304notfound-com/llms/304notfound-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/304notfound-com-llms.txt
- group: other
  href: https://artifacts.apis.io/304notfound-com/hosts/304notfound-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/304notfound-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/304notfound-com/security/304notfound-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/304notfound-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://304notfound.com/
- group: docs
  title: ''
  type: Documentation
  url: https://304notfound.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://304notfound.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://304notfound.com/llms.txt
created: '2026-10-31'
description: 304NotModified provides AI‑agent‑focused factual answer services, delivering verified, sourced and timestamped responses across French regulatory domains such as electronic invoicing, vocational training, taxes, finance and law. The platform offers on‑demand services including content creation by AUTARK, and exposes a public HTTP API (Swagger UI) with endpoints for answering questions, retrieving domain coverage, and managing free API keys. All responses are cached and sourced from official references, enabling agents to obtain reliable data without personal data collection.
json_schemas:
- name: AnswerRequest
  property_count: 3
  slug: 304notfound-com-answer-request
- name: CommentRequest
  property_count: 4
  slug: 304notfound-com-comment-request
- name: IchimokuIn
  property_count: 8
  slug: 304notfound-com-ichimoku-in
- name: PositionIn
  property_count: 14
  slug: 304notfound-com-position-in
- name: RegimeIn
  property_count: 5
  slug: 304notfound-com-regime-in
- name: SelfServiceKeyRequest
  property_count: 3
  slug: 304notfound-com-self-service-key-request
jsonld:
- class_count: 12
  name: 304Notfound Com Context
  property_count: 50
  slug: 304notfound-com-context
layout: provider
modified: '2026-10-31'
name: 304NotModified
nav: Providers
network: true
overview: '304NotModified publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Answer API, Ask API, Calculs sur vos données API, and 7 more. Tagged areas include Artificial Intelligence, Knowledge Base, French, and Fact Checking.


  The 304NotModified catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  304NotModified''s developer surface includes documentation, API reference, getting-started guide, and 11 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 0
  name: 304Notfound Com Rate Limits
  slug: 304notfound-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: 304NotModified API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: 304notfound-com-rules
scopes:
- name: 304Notfound Com Scopes
  scope_count: 0
  slug: 304notfound-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 49.2
    developer_ergonomics: 14.3
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 26.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 304Notfound Com Authentication
  slug: 304notfound-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 304Notfound Com Domain Security
  slug: 304notfound-com-domain-security
  summary_line: TLSv1.3
slug: 304notfound-com
tags:
- Artificial Intelligence
- Knowledge Base
- French
- Fact Checking
website: https://304notfound.com/
---
