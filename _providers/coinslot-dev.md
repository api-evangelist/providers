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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Coinslot API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Coinslot API
  slug: coinslot-dev-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/coinslot-dev/rules/coinslot-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/coinslot-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/coinslot-dev/json-ld/coinslot-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coinslot-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/coinslot-dev/vocabulary/coinslot-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coinslot-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/coinslot-dev/data-model/coinslot-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coinslot-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/coinslot-dev/conformance/coinslot-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coinslot-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coinslot-dev/llms/coinslot-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinslot-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/coinslot-dev/hosts/coinslot-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinslot-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/coinslot-dev/vendors/coinslot-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinslot-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/coinslot-dev/security/coinslot-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinslot-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coinslot.dev/
created: '2026-11-04'
description: Coinslot provides micro‑APIs that AI agents can pay for autonomously via x402 (USDC). No signup is required – insert a coin and get a result. The platform offers 12 micro‑APIs, each callable by AI or humans with credits, built and operated by an AI. It aims to be the vending machine for machines, exposing simple, pay‑per‑call endpoints for tasks like currency conversion, weather, and more.
json_schemas:
- name: GetApiDiffResponse
  property_count: 2
  slug: coinslot-dev-get-api-diff-response
- name: PostApiCheckoutRequest
  property_count: 1
  slug: coinslot-dev-post-api-checkout-request
- name: PostApiDiffRequest
  property_count: 2
  slug: coinslot-dev-post-api-diff-request
- name: PostApiQrRequest
  property_count: 1
  slug: coinslot-dev-post-api-qr-request
jsonld:
- class_count: 4
  name: Coinslot Dev Context
  property_count: 6
  slug: coinslot-dev-context
layout: provider
modified: '2026-11-04'
name: Coinslot
nav: Providers
network: true
overview: 'Coinslot is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Micro-API, Payments, Automation, and Machine Learning.


  The Coinslot catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Coinslot API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: coinslot-dev-rules
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coinslot Dev Domain Security
  slug: coinslot-dev-domain-security
  summary_line: TLSv1.3
slug: coinslot-dev
tags:
- Artificial Intelligence
- Micro-API
- Payments
- Automation
- Machine Learning
website: https://coinslot.dev/
---
