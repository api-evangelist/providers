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
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.apione.store/v1
  baseurl_source: declared
  description: 'apione-store API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: apione-store API
  slug: apione-store-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/apione-store/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/apione-store/rate-limits/apione-store-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apione-store-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/apione-store/plans/apione-store-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apione-store-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apione-store/rules/apione-store-rules.yml
  title: ''
  type: Spectral
  url: rules/apione-store-rules.yml
- group: design
  href: https://artifacts.apis.io/apione-store/json-ld/apione-store-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apione-store-context.jsonld
- group: design
  href: https://artifacts.apis.io/apione-store/vocabulary/apione-store-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apione-store-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/apione-store/data-model/apione-store-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apione-store-data-model.yml
- group: auth
  href: https://artifacts.apis.io/apione-store/authentication/apione-store-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apione-store-authentication.yml
- group: design
  href: https://artifacts.apis.io/apione-store/errors/apione-store-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apione-store-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apione-store/conformance/apione-store-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apione-store-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apione-store/llms/apione-store-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apione-store-llms.txt
- group: build
  href: https://artifacts.apis.io/apione-store/mcp/apione-store-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/apione-store-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/apione-store/mcp/apione-store-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apione-store-mcp.yml
- group: agent
  href: https://artifacts.apis.io/apione-store/well-known/apione-store-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apione-store-well-known.yml
- group: other
  href: https://artifacts.apis.io/apione-store/hosts/apione-store-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apione-store-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apione.store/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apione.store/privacy
- group: company
  title: ''
  type: Blog
  url: https://apione.store/blog
- group: auth
  href: https://artifacts.apis.io/apione-store/security/apione-store-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apione-store-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apione.store/
- group: docs
  title: ''
  type: Documentation
  url: https://apione.store/docs
- group: docs
  title: ''
  type: APIReference
  url: https://apione.store/docs#api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apione.store/docs#quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://apione.store/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://apione.store/sign-in?redirect_url=%2Fdashboard
created: '2026-10-30'
description: ApiOne provides a B2B data enrichment API focused on GCC and MENA companies, offering company, people, email finding and verification endpoints. The service returns structured JSON with cited sources, includes free credits, tiered pricing, and supports MCP for AI agents. It enables developers to integrate comprehensive company intelligence, growth signals, and technology stack detection into applications with a single API key.
image: https://apione.store/favicon.svg
json_schemas:
- name: PostApiV1EmailsFindRequest
  property_count: 3
  slug: apione-store-post-api-v1-emails-find-request
- name: PostApiV1WatchRequest
  property_count: 6
  slug: apione-store-post-api-v1-watch-request
- name: PostV1CompanyResponse
  property_count: 9
  slug: apione-store-post-v1-company-response
- name: PostV1EmailFindResponse
  property_count: 1
  slug: apione-store-post-v1-email-find-response
- name: PostV1EmailVerifyResponse
  property_count: 7
  slug: apione-store-post-v1-email-verify-response
- name: PostV1PeopleResponse
  property_count: 8
  slug: apione-store-post-v1-people-response
jsonld:
- class_count: 20
  name: Apione Store Context
  property_count: 39
  slug: apione-store-context
layout: provider
mcp_servers:
- description: Remote MCP server at apione.store requiring an API key.
  name: apione-store MCP Server
  slug: apione-store-mcp-yml
modified: '2026-10-30'
name: apione-store
nav: Providers
network: true
overview: 'apione-store is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include B2B, Data Enrichment, Data, GCC, and MENA.


  The apione-store catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  apione-store''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, pricing, signup flow, and 18 more developer resources.'
plans:
- name: Apione Store Plans Pricing
  plan_count: 4
  slug: apione-store-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Apione Store Rate Limits
  slug: apione-store-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: apione-store API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: apione-store-rules
scopes:
- name: Apione Store Scopes
  scope_count: 0
  slug: apione-store-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 86.0
    catalog_earned_first_party: 24.0
    catalog_gap: 29.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.2
  facets:
    access_clarity: 53.9
    contract_governance: 19.7
    contract_quality: 24.8
    developer_ergonomics: 33.8
    discoverability: 65.0
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 47.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/apione-store/apione-store-2026-11-03T120953.png
security:
- kind: authentication
  name: Apione Store Authentication
  slug: apione-store-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apione Store Domain Security
  slug: apione-store-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: apione-store-mcp-tools
  slug: apione-store-mcp-tools
slug: apione-store
tags:
- B2B
- Data Enrichment
- Data
- GCC
- MENA
website: https://apione.store/
---
