---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Model Context Protocol (MCP) tools for Claude News, providing search and recent news operations.
  name: Claude News MCP
  slug: claude-news-mcp
- description: 'Claude News API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Claude News API
  slug: claudenews-online-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/claudenews-online/rules/claudenews-online-rules.yml
  title: ''
  type: Spectral
  url: rules/claudenews-online-rules.yml
- group: design
  href: https://artifacts.apis.io/claudenews-online/json-ld/claudenews-online-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/claudenews-online-context.jsonld
- group: design
  href: https://artifacts.apis.io/claudenews-online/vocabulary/claudenews-online-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/claudenews-online-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/claudenews-online/data-model/claudenews-online-data-model.yml
  title: ''
  type: DataModel
  url: data-model/claudenews-online-data-model.yml
- group: operate
  href: https://artifacts.apis.io/claudenews-online/lifecycle/claudenews-online-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/claudenews-online-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/claudenews-online/lifecycle/claudenews-online-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/claudenews-online-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/claudenews-online/conformance/claudenews-online-conformance.yml
  title: ''
  type: Conformance
  url: conformance/claudenews-online-conformance.yml
- group: agent
  href: https://artifacts.apis.io/claudenews-online/llms/claudenews-online-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claudenews-online-llms.txt
- group: other
  href: https://artifacts.apis.io/claudenews-online/hosts/claudenews-online-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claudenews-online-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://claudenews.online/en/newsroom
- group: docs
  title: ''
  type: Documentation
  url: https://claudenews.online/guides
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/anthropics/claude-code/releases/tag/v2.1.318
- group: start
  title: ''
  type: GettingStarted
  url: https://claudenews.online/en/guides/comment-utiliser-claude
- group: auth
  href: https://artifacts.apis.io/claudenews-online/security/claudenews-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claudenews-online-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claudenews.online/
created: '2026-11-03'
description: Claude News aggregates real‑time news about Claude and Anthropic, pulling from official Anthropic releases, status updates, press, Hacker News, Reddit and GitHub. It curates and summarizes content, providing a signal without the noise. The service is operated by Héra SASU and launched in June 2026, offering timely AI model updates, security alerts, and community insights.
image: https://claudenews.online/opengraph-image?d64b7c393845860f
json_schemas:
- name: GetV1ModelsModelidResponse
  property_count: 1
  slug: claudenews-online-get-v1-models-modelid-response
- name: GetV1ModelsResponse
  property_count: 1
  slug: claudenews-online-get-v1-models-response
jsonld:
- class_count: 2
  name: Claudenews Online Context
  property_count: 1
  slug: claudenews-online-context
layout: provider
modified: '2026-11-03'
name: Claude News
nav: Providers
network: true
overview: 'Claude News is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include News, Artificial Intelligence, Anthropic, Real-Time, and Aggregator.


  The Claude News catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Claude News'' developer surface includes documentation, changelog, getting-started guide, and 12 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: Claude News API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: claudenews-online-rules
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 10.7
    discoverability: 58.0
    operational_transparency: 15.8
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
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Claudenews Online Domain Security
  slug: claudenews-online-domain-security
  summary_line: TLSv1.3 · HSTS
slug: claudenews-online
tags:
- News
- Artificial Intelligence
- Anthropic
- Real-Time
- Aggregator
website: https://claudenews.online/
---
