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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read-only JSON API of aicomputeradar.dev providing model signals, GPU rental prices and hardware-fit verdicts.
  name: AI Compute Radar API
  slug: ai-compute-radar-api
- baseURL: https://aicomputeradar.dev/api/v1
  baseurl_source: declared
  description: Read-only JSON API of aicomputeradar.dev. Every response carries provenance (meta.source, meta.collectedAt). Data compilation is licensed CC BY 4.0 — attribute 'AI Compute Radar (https://aicomputerada
  name: AI Compute Radar API V1 API
  slug: ai-compute-radar-api-v1-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/aicomputeradar-dev/rules/aicomputeradar-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/aicomputeradar-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/aicomputeradar-dev/json-ld/aicomputeradar-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aicomputeradar-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/aicomputeradar-dev/vocabulary/aicomputeradar-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aicomputeradar-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aicomputeradar-dev/data-model/aicomputeradar-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aicomputeradar-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/aicomputeradar-dev/errors/aicomputeradar-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aicomputeradar-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aicomputeradar-dev/conformance/aicomputeradar-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aicomputeradar-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aicomputeradar-dev/llms/aicomputeradar-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aicomputeradar-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/aicomputeradar-dev/hosts/aicomputeradar-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aicomputeradar-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/aicomputeradar-dev/vendors/aicomputeradar-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aicomputeradar-dev-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aicomputeradar.dev/legal/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://aicomputeradar.dev/developers
- group: auth
  href: https://artifacts.apis.io/aicomputeradar-dev/security/aicomputeradar-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aicomputeradar-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aicomputeradar.dev/
created: '2026-11-01'
description: AI Compute Radar provides a web platform that ranks and matches open AI models to your GPU capabilities. It aggregates model metadata, compute requirements, and pricing from public sources, presenting them in an easy-to-use interface for developers and researchers to select suitable models for their hardware.
image: https://aicomputeradar.dev/opengraph-image?16d7484b21669be5
json_schemas:
- name: FitResponse
  property_count: 4
  slug: aicomputeradar-dev-fit-response
- name: Hardware
  property_count: 9
  slug: aicomputeradar-dev-hardware
- name: HistoryPoint
  property_count: 11
  slug: aicomputeradar-dev-history-point
- name: Model
  property_count: 11
  slug: aicomputeradar-dev-model
- name: Pick
  property_count: 12
  slug: aicomputeradar-dev-pick
- name: PriceBand
  property_count: 16
  slug: aicomputeradar-dev-price-band
jsonld:
- class_count: 11
  name: Aicomputeradar Dev Context
  property_count: 79
  slug: aicomputeradar-dev-context
layout: provider
modified: '2026-11-01'
name: AI Compute Radar
nav: Providers
network: true
overview: 'AI Compute Radar publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API V1 API, and 1 more. Tagged areas include Artificial Intelligence, Compute, Radar, Models, and GPU.


  The AI Compute Radar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI Compute Radar''s developer surface includes API reference and 12 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AI Compute Radar API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: aicomputeradar-dev-rules
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 51.0
    developer_ergonomics: 3.6
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 25.3
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aicomputeradar Dev Domain Security
  slug: aicomputeradar-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aicomputeradar-dev
tags:
- Artificial Intelligence
- Compute
- Radar
- Models
- GPU
website: https://aicomputeradar.dev/
---
