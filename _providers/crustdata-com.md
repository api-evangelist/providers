---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - rate-limits
  - security
  trial: true
  try_now: false
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
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Real-time B2B data API for AI agents providing firmographic data.
  name: Crustdata API
  slug: crustdata-api
- baseURL: https://api.crustdata.com
  baseurl_source: declared
  description: 'Crustdata API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Crustdata API
  slug: crustdata-com-api
artifact_total: 14
common:
- group: operate
  href: https://artifacts.apis.io/crustdata-com/rate-limits/crustdata-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crustdata-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/crustdata-com/plans/crustdata-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crustdata-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/crustdata-com/rules/crustdata-com-rules.yml
  title: ''
  type: Spectral
  url: rules/crustdata-com-rules.yml
- group: design
  href: https://artifacts.apis.io/crustdata-com/json-ld/crustdata-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crustdata-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/crustdata-com/vocabulary/crustdata-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crustdata-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/crustdata-com/data-model/crustdata-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crustdata-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/crustdata-com/cli/crustdata-com-cli.yml
  title: ''
  type: CLI
  url: cli/crustdata-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/crustdata-com/changelog/crustdata-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/crustdata-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/crustdata-com/conventions/crustdata-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/crustdata-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/crustdata-com/conformance/crustdata-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crustdata-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crustdata-com/llms/crustdata-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crustdata-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/crustdata-com/mcp/crustdata-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crustdata-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/crustdata-com/well-known/crustdata-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crustdata-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/crustdata-com/hosts/crustdata-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crustdata-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/crustdata-com/vendors/crustdata-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crustdata-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://crustdata.com/webhook
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crustdata.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crustdata.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://crustdata.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.crustdata.com/auth/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.crustdata.com/openapi-specs/2025-11-01/changelog
- group: company
  title: ''
  type: Blog
  url: https://crustdata.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crustdata.com/
- group: auth
  href: https://artifacts.apis.io/crustdata-com/security/crustdata-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crustdata-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crustdata.com/
coverage:
  checked: '2026-11-04'
  detail: API documentation is served as a JavaScript-rendered site with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.crustdata.com/openapi-specs/2025-11-01/introduction
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Crustdata provides a real-time B2B data API for AI agents, offering access to over 1 billion people and 60 million companies. The service powers sales, recruiting, and investment workflows with comprehensive firmographic data and growth metrics, enabling developers to integrate up-to-date company information into their applications.
image: https://framerusercontent.com/assets/X026uPKyVz8OZVtmkHAs7wKq0.png
json_schemas:
- name: GetAccountUsageErrorsResponse
  property_count: 4
  slug: crustdata-com-get-account-usage-errors-response
- name: PostCompanySearchRequest
  property_count: 4
  slug: crustdata-com-post-company-search-request
- name: PostJobSearchRequest
  property_count: 3
  slug: crustdata-com-post-job-search-request
- name: PostSocialPostSearchRequest
  property_count: 5
  slug: crustdata-com-post-social-post-search-request
- name: PostWebSearchLiveRequest
  property_count: 8
  slug: crustdata-com-post-web-search-live-request
- name: PostWebSearchLiveResponse
  property_count: 7
  slug: crustdata-com-post-web-search-live-response
jsonld:
- class_count: 12
  name: Crustdata Com Context
  property_count: 28
  slug: crustdata-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.crustdata.com requiring OAuth.
  name: Crustdata MCP Server
  slug: crustdata-com-mcp-yml
modified: '2026-11-04'
name: Crustdata
nav: Providers
network: true
overview: 'Crustdata is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include B2B, Data, Artificial Intelligence, Real-Time, and Company.


  The Crustdata catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Crustdata''s developer surface includes CLI, changelog, pricing, engineering blog, documentation, and 20 more developer resources.'
plans:
- name: Crustdata Com Plans Pricing
  plan_count: 2
  slug: crustdata-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Crustdata Com Rate Limits
  slug: crustdata-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Crustdata API Rules
  rule_count: 48
  severity_counts:
    error: 45
    hint: 0
    info: 2
    warn: 1
  slug: crustdata-com-rules
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 73.8
    catalog_earned_first_party: 16.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 19.0
    discoverability: 56.7
    operational_transparency: 44.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crustdata Com Domain Security
  slug: crustdata-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crustdata-com
tags:
- B2B
- Data
- Artificial Intelligence
- Real-Time
- Company
website: https://crustdata.com/
---
