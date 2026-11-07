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
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for accessing flight data, pricing estimates, and aircraft information. Documentation is at the developer portal but no machine‑readable spec was found.
  name: Altivo Jets API
  slug: altivo-jets-api
- description: 'Altivo Jets API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Altivo Jets API
  slug: altivojets-com-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/altivojets-com/rules/altivojets-com-rules.yml
  title: ''
  type: Spectral
  url: rules/altivojets-com-rules.yml
- group: design
  href: https://artifacts.apis.io/altivojets-com/json-ld/altivojets-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/altivojets-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/altivojets-com/vocabulary/altivojets-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/altivojets-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/altivojets-com/data-model/altivojets-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/altivojets-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/altivojets-com/conformance/altivojets-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/altivojets-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/altivojets-com/llms/altivojets-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/altivojets-com-llms.txt
- group: other
  href: https://artifacts.apis.io/altivojets-com/hosts/altivojets-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/altivojets-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/altivojets-com/vendors/altivojets-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/altivojets-com-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://altivojets.com/ar-ae/pricing-and-fees/
- group: auth
  href: https://artifacts.apis.io/altivojets-com/security/altivojets-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altivojets-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://altivojets.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://altivojets.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://altivojets.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://altivojets.com/developers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://altivojets.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://altivojets.com/privacy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://altivojets.com/developers/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or MCP spec was discoverable on api.altivojets.com or altivojets.com.
  evidence:
  - status: 0
    url: https://api.altivojets.com/openapi.json
  - status: 404
    url: https://altivojets.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Altivo Jets is a private jet and helicopter charter broker operating in 12 countries. It offers licensed operators, instant quotes, and a free public MCP server for AI assistants to access live empty‑leg data, pricing estimates, and aircraft information. The company provides a multilingual web portal, detailed guides on charter flights, and a developer portal for API access.
image: https://altivojets.com/images/wm/jet-runway.jpg
json_schemas:
- name: GetApiV1EstimateResponse
  property_count: 6
  slug: altivojets-com-get-api-v1-estimate-response
- name: GetApiV1LegsResponse
  property_count: 1
  slug: altivojets-com-get-api-v1-legs-response
- name: GetMcpResponse
  property_count: 1
  slug: altivojets-com-get-mcp-response
- name: PostApiV1QuotesRequest
  property_count: 10
  slug: altivojets-com-post-api-v1-quotes-request
- name: PostApiV1QuotesResponse
  property_count: 2
  slug: altivojets-com-post-api-v1-quotes-response
jsonld:
- class_count: 5
  name: Altivojets Com Context
  property_count: 20
  slug: altivojets-com-context
layout: provider
modified: '2026-11-01'
name: Altivo Jets
nav: Providers
network: true
overview: 'Altivo Jets is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Aviation, Charter, Private-Jet, and Helicopter.


  The Altivo Jets catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Altivo Jets'' developer surface includes pricing, documentation, API reference, and 14 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Altivo Jets API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: altivojets-com-rules
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 13.1
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 26.3
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Altivojets Com Domain Security
  slug: altivojets-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: altivojets-com
tags:
- Aviation
- Charter
- Private-Jet
- Helicopter
website: https://altivojets.com/
---
