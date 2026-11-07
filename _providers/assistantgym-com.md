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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public API for Assistant Gym, referenced on the Developers page.
  name: Assistant Gym API
  slug: assistant-gym-api
- description: 'Assistant Gym API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Assistant Gym API
  slug: assistantgym-com-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/assistantgym-com/rules/assistantgym-com-rules.yml
  title: ''
  type: Spectral
  url: rules/assistantgym-com-rules.yml
- group: design
  href: https://artifacts.apis.io/assistantgym-com/json-ld/assistantgym-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/assistantgym-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/assistantgym-com/vocabulary/assistantgym-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/assistantgym-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/assistantgym-com/data-model/assistantgym-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/assistantgym-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/assistantgym-com/conformance/assistantgym-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/assistantgym-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/assistantgym-com/hosts/assistantgym-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assistantgym-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/assistantgym-com/security/assistantgym-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assistantgym-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://assistantgym.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://assistantgym.com/developers.html
- group: start
  title: ''
  type: GettingStarted
  url: https://assistantgym.com/how-it-works.html
- group: operate
  title: ''
  type: Support
  url: https://assistantgym.com/status.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assistantgym.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://assistantgym.com/privacy
coverage:
  checked: '2026-11-02'
  detail: Developers page provides HTML docs but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://assistantgym.com/developers.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Assistant Gym builds a platform to improve AI assistants for better outcomes, lower costs, and fewer mistakes. It offers tools like Decision Audit, Handoff Check, and a suite of bounded utilities to evaluate, train, test, verify, certify, and audit assistants in real work contexts.
image: https://assistantgym.com/assets/ag-v21-friction-20261013/icon.svg
json_schemas:
- name: PostApiV1EvalReportResponse
  property_count: 4
  slug: assistantgym-com-post-api-v1-eval-report-response
- name: PostApiV1ExportRequest
  property_count: 8
  slug: assistantgym-com-post-api-v1-export-request
- name: PostApiV1RunsRequest
  property_count: 2
  slug: assistantgym-com-post-api-v1-runs-request
- name: PostApiV1RunsResponse
  property_count: 3
  slug: assistantgym-com-post-api-v1-runs-response
- name: PostApiV1TeachRequest
  property_count: 2
  slug: assistantgym-com-post-api-v1-teach-request
- name: PostApiV1TurnsRequest
  property_count: 2
  slug: assistantgym-com-post-api-v1-turns-request
jsonld:
- class_count: 11
  name: Assistantgym Com Context
  property_count: 30
  slug: assistantgym-com-context
layout: provider
modified: '2026-11-02'
name: Assistant Gym
nav: Providers
network: true
overview: 'Assistant Gym is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Assistant, Productivity, Automation, and Platform.


  The Assistant Gym catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Assistant Gym''s developer surface includes getting-started guide, support, and 11 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Assistant Gym API Rules
  rule_count: 39
  severity_counts:
    error: 36
    hint: 0
    info: 2
    warn: 1
  slug: assistantgym-com-rules
scopes:
- name: Assistantgym Com Scopes
  scope_count: 0
  slug: assistantgym-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 13.1
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 25.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Assistantgym Com Authentication
  slug: assistantgym-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Assistantgym Com Domain Security
  slug: assistantgym-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: assistantgym-com
tags:
- Artificial Intelligence
- Assistant
- Productivity
- Automation
- Platform
website: https://assistantgym.com/
---
