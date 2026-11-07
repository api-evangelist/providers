---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Programmatic API for company search, data retrieval, and intelligence endpoints.
  name: B2BHint API
  slug: b2bhint-api
- description: 'B2BHint API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: B2BHint API
  slug: b2bhint-com-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/b2bhint-com/rate-limits/b2bhint-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/b2bhint-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/b2bhint-com/plans/b2bhint-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/b2bhint-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/b2bhint-com/rules/b2bhint-com-rules.yml
  title: ''
  type: Spectral
  url: rules/b2bhint-com-rules.yml
- group: design
  href: https://artifacts.apis.io/b2bhint-com/json-ld/b2bhint-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/b2bhint-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/b2bhint-com/vocabulary/b2bhint-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/b2bhint-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/b2bhint-com/data-model/b2bhint-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/b2bhint-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/b2bhint-com/conventions/b2bhint-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/b2bhint-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/b2bhint-com/authentication/b2bhint-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/b2bhint-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/b2bhint-com/conformance/b2bhint-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/b2bhint-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/b2bhint-com/llms/b2bhint-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/b2bhint-com-llms.txt
- group: build
  href: https://artifacts.apis.io/b2bhint-com/mcp/b2bhint-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/b2bhint-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/b2bhint-com/mcp/b2bhint-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/b2bhint-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/b2bhint-com/hosts/b2bhint-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/b2bhint-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/b2bhint-com/vendors/b2bhint-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/b2bhint-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/b2bhint-com/security/b2bhint-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/b2bhint-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://b2bhint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://b2bhint.com/en/about
- group: docs
  title: ''
  type: APIReference
  url: https://b2bhint.com/en/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://b2bhint.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://b2bhint.com/en/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://b2bhint.com/en/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://b2bhint.com/en/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://b2bhint.com/en/contact-us
created: '2026-11-02'
description: B2BHint provides company intelligence across 188 jurisdictions, aggregating official government register data to deliver comprehensive profiles including financials, officers, court cases, ownership, and more. The platform offers searchable company data, export capabilities, and an API for programmatic access, with free tier limits and paid plans for higher usage. Data is sourced directly from registers, ensuring accuracy and compliance.
image: https://b2bhint.com/favicon.ico
json_schemas:
- name: GetApiV1CompanyChangesResponse
  property_count: 4
  slug: b2bhint-com-get-api-v1-company-changes-response
- name: GetApiV1UserMeResponse
  property_count: 3
  slug: b2bhint-com-get-api-v1-user-me-response
- name: GetApiV1WatchlistResponse
  property_count: 3
  slug: b2bhint-com-get-api-v1-watchlist-response
- name: GetApiV2SearchCompanyResponse
  property_count: 6
  slug: b2bhint-com-get-api-v2-search-company-response
- name: GetApiWidgetSearchResponse
  property_count: 2
  slug: b2bhint-com-get-api-widget-search-response
- name: PostApiV1WatchlistResponse
  property_count: 12
  slug: b2bhint-com-post-api-v1-watchlist-response
jsonld:
- class_count: 10
  name: B2Bhint Com Context
  property_count: 40
  slug: b2bhint-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at b2bhint.com requiring an API key.
  name: B2BHint MCP Server
  slug: b2bhint-com-mcp-yml
modified: '2026-11-02'
name: B2BHint
nav: Providers
network: true
overview: 'B2BHint is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Company Intelligence, Data, Finance, and Jurisdictions.


  The B2BHint catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  B2BHint''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, and 17 more developer resources.'
plans:
- name: B2Bhint Com Plans Pricing
  plan_count: 5
  slug: b2bhint-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 16
  name: B2Bhint Com Rate Limits
  slug: b2bhint-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: B2BHint API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: b2bhint-com-rules
scopes:
- name: B2Bhint Com Scopes
  scope_count: 0
  slug: b2bhint-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 25.0
    developer_ergonomics: 22.6
    discoverability: 56.7
    operational_transparency: 31.6
  previous_composite: 43.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
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
security:
- kind: authentication
  name: B2Bhint Com Authentication
  slug: b2bhint-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: B2Bhint Com Domain Security
  slug: b2bhint-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: b2bhint-com
tags:
- Company
- Company Intelligence
- Data
- Finance
- Jurisdictions
website: https://b2bhint.com/
---
