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
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: BuyAPI provides an MCP endpoint for tool discovery and integration.
  name: BuyAPI MCP
  slug: buyapi-mcp
- description: 'BuyAPI API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: BuyAPI API
  slug: buyapi-ai-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/buyapi-ai/rules/buyapi-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/buyapi-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/buyapi-ai/json-ld/buyapi-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buyapi-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/buyapi-ai/vocabulary/buyapi-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buyapi-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/buyapi-ai/data-model/buyapi-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buyapi-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/buyapi-ai/conformance/buyapi-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buyapi-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/buyapi-ai/hosts/buyapi-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buyapi-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/buyapi-ai/vendors/buyapi-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buyapi-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buyapi.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buyapi.ai/privacy
- group: auth
  href: https://artifacts.apis.io/buyapi-ai/security/buyapi-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buyapi-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buyapi.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://buyapi.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://buyapi.ai/docs#getting-started
- group: operate
  title: ''
  type: Support
  url: https://buyapi.ai/contact
created: '2026-11-03'
description: BuyAPI, operated by Fang Labs LLC, provides an open-source MCP server and a platform that helps builders and coding agents choose APIs and infrastructure. It offers current pricing, tradeoffs, evidence, and tools for comparing vendors, with a focus on vendor intelligence and developer assistance.
image: https://buyapi.ai/opengraph-image?d98fdb63cc66bff3
json_schemas:
- name: GetApiEvidenceResponse
  property_count: 1
  slug: buyapi-ai-get-api-evidence-response
- name: GetApiStacksSimilarResponse
  property_count: 1
  slug: buyapi-ai-get-api-stacks-similar-response
- name: GetApiVendorsResponse
  property_count: 1
  slug: buyapi-ai-get-api-vendors-response
- name: GetApiVendorsSearchResponse
  property_count: 2
  slug: buyapi-ai-get-api-vendors-search-response
- name: PostApiRecommendRequest
  property_count: 4
  slug: buyapi-ai-post-api-recommend-request
- name: PostApiRecommendResponse
  property_count: 8
  slug: buyapi-ai-post-api-recommend-response
jsonld:
- class_count: 6
  name: Buyapi Ai Context
  property_count: 16
  slug: buyapi-ai-context
layout: provider
modified: '2026-11-03'
name: BuyAPI
nav: Providers
network: true
overview: 'BuyAPI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Tools, MCP, VendorIntelligence, and Platform.


  The BuyAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BuyAPI''s developer surface includes documentation, getting-started guide, support, and 11 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: BuyAPI API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: buyapi-ai-rules
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 13.1
    discoverability: 48.2
    operational_transparency: 0.0
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buyapi Ai Domain Security
  slug: buyapi-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: buyapi-ai
tags:
- Developer Tools
- MCP
- VendorIntelligence
- Platform
website: https://buyapi.ai/
---
