---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Programmatic access to the design reference database, including site listings and synthesis via /extract-essence.
  name: AllGoodInsp REST API
  slug: allgoodinsp-rest-api
- baseURL: https://api.allgoodinsp.com
  baseurl_source: declared
  description: 'AllGoodInsp API as documented publicly: 18 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AllGoodInsp API
  slug: allgoodinsp-com-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/allgoodinsp-com/rate-limits/allgoodinsp-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/allgoodinsp-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/allgoodinsp-com/plans/allgoodinsp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/allgoodinsp-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/allgoodinsp-com/rules/allgoodinsp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/allgoodinsp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/allgoodinsp-com/json-ld/allgoodinsp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/allgoodinsp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/allgoodinsp-com/vocabulary/allgoodinsp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/allgoodinsp-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/allgoodinsp-com/data-model/allgoodinsp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/allgoodinsp-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/allgoodinsp-com/authentication/allgoodinsp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/allgoodinsp-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/allgoodinsp-com/errors/allgoodinsp-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/allgoodinsp-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/allgoodinsp-com/conformance/allgoodinsp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allgoodinsp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/allgoodinsp-com/llms/allgoodinsp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allgoodinsp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/allgoodinsp-com/well-known/allgoodinsp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allgoodinsp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/allgoodinsp-com/hosts/allgoodinsp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allgoodinsp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/allgoodinsp-com/vendors/allgoodinsp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allgoodinsp-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/allgoodinsp-com/security/allgoodinsp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allgoodinsp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allgoodinsp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://allgoodinsp.com/docs/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://allgoodinsp.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://allgoodinsp.com/docs/mcp
- group: operate
  title: ''
  type: Support
  url: https://allgoodinsp.com/contact
- group: company
  title: ''
  type: Blog
  url: https://allgoodinsp.com/insights
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allgoodinsp.com/privacy
coverage:
  checked: '2026-11-01'
  detail: API documentation provides a base URL but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 200
    url: https://allgoodinsp.com/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AllGoodInsp is a curated collection of design references built for both humans and AI. Every site in the collection is analyzed for its design decisions — typography, layout, color, motion, and information architecture — and stored as structured data that AI tools can query through MCP (Model Context Protocol).
image: https://allgoodinsp.com/favicon.svg
json_schemas:
- name: GetV1SitesResponse
  property_count: 2
  slug: allgoodinsp-com-get-v1-sites-response
- name: PostApiKeysResponse
  property_count: 5
  slug: allgoodinsp-com-post-api-keys-response
- name: PostExtractEssenceRequest
  property_count: 4
  slug: allgoodinsp-com-post-extract-essence-request
- name: PostExtractEssenceResponse
  property_count: 5
  slug: allgoodinsp-com-post-extract-essence-response
- name: PostSubmissionsRequest
  property_count: 3
  slug: allgoodinsp-com-post-submissions-request
- name: PostV1ExtractEssenceResponse
  property_count: 2
  slug: allgoodinsp-com-post-v1-extract-essence-response
jsonld:
- class_count: 19
  name: Allgoodinsp Com Context
  property_count: 29
  slug: allgoodinsp-com-context
layout: provider
modified: '2026-11-01'
name: AllGoodInsp
nav: Providers
network: true
overview: 'AllGoodInsp is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Design, Artificial Intelligence, References, Curated, and MCP.


  The AllGoodInsp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AllGoodInsp''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 15 more developer resources.'
plans:
- name: Allgoodinsp Com Plans Pricing
  plan_count: 3
  slug: allgoodinsp-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 12
  name: Allgoodinsp Com Rate Limits
  slug: allgoodinsp-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: AllGoodInsp API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: allgoodinsp-com-rules
scopes:
- name: Allgoodinsp Com Scopes
  scope_count: 0
  slug: allgoodinsp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 29.8
    discoverability: 66.1
    operational_transparency: 31.6
  previous_composite: 39.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Allgoodinsp Com Authentication
  slug: allgoodinsp-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Allgoodinsp Com Domain Security
  slug: allgoodinsp-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: allgoodinsp-com
tags:
- Design
- Artificial Intelligence
- References
- Curated
- MCP
website: https://allgoodinsp.com/
---
