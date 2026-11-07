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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Drillerdb Com Agentic Access
  operation_count: 20
  slug: drillerdb-com-agentic-access
  summary_line: 20 operations · 1 acting
api_count: 1
apis:
- baseURL: https://drillerdb.com
  baseurl_source: declared
  description: Industry conference calendars
  name: DrillerDB Conferences API
  slug: drillerdb-com-conferences-api
- baseURL: https://drillerdb.com
  baseurl_source: declared
  description: app.drillerdb.com/api/v1 contacts (X-API-Key)
  name: DrillerDB Contacts API
  slug: drillerdb-com-contacts-api
- baseURL: https://drillerdb.com
  baseurl_source: declared
  description: app.drillerdb.com/api/v1 documentation (X-API-Key)
  name: DrillerDB Documentation API
  slug: drillerdb-com-documentation-api
- baseURL: https://drillerdb.com
  baseurl_source: declared
  description: Find-a-Driller directory and state license records
  name: DrillerDB Driller directory API
  slug: drillerdb-com-driller-directory-api
- baseURL: https://drillerdb.com
  baseurl_source: declared
  description: Model Context Protocol server for DrillerDB Enterprise (enterprise.drillerdb.com)
  name: DrillerDB Enterprise MCP API
  slug: drillerdb-com-enterprise-mcp-api
- baseURL: https://drillerdb.com
  baseurl_source: declared
  description: app.drillerdb.com/api/v1 equipment (X-API-Key)
  name: DrillerDB Equipment API
  slug: drillerdb-com-equipment-api
- baseURL: https://drillerdb.com
  baseurl_source: declared
  description: ZIP code resolution used by the directory
  name: DrillerDB Geocoding API
  slug: drillerdb-com-geocoding-api
- baseURL: https://drillerdb.com
  baseurl_source: declared
  description: app.drillerdb.com/api/v1 inventory (X-API-Key)
  name: DrillerDB Inventory API
  slug: drillerdb-com-inventory-api
- baseURL: https://drillerdb.com
  baseurl_source: declared
  description: app.drillerdb.com/api/v1 invoices (X-API-Key)
  name: DrillerDB Invoices API
  slug: drillerdb-com-invoices-api
- baseURL: https://drillerdb.com
  baseurl_source: declared
  description: Published platform counts
  name: DrillerDB Platform API
  slug: drillerdb-com-platform-api
- baseURL: https://drillerdb.com
  baseurl_source: declared
  description: app.drillerdb.com/api/v1 projects (X-API-Key)
  name: DrillerDB Projects API
  slug: drillerdb-com-projects-api
- baseURL: https://drillerdb.com
  baseurl_source: declared
  description: Depth and water-table statistics from the public well dataset
  name: DrillerDB Well data API
  slug: drillerdb-com-well-data-api
- baseURL: https://drillerdb.com
  baseurl_source: declared
  description: app.drillerdb.com/api/v1 work orders (X-API-Key)
  name: DrillerDB Work Orders API
  slug: drillerdb-com-work-orders-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/drillerdb-com/agentic-access/drillerdb-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/drillerdb-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/drillerdb-com/rate-limits/drillerdb-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/drillerdb-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/drillerdb-com/plans/drillerdb-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/drillerdb-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/drillerdb-com/rules/drillerdb-com-rules.yml
  title: ''
  type: Spectral
  url: rules/drillerdb-com-rules.yml
- group: design
  href: https://artifacts.apis.io/drillerdb-com/json-ld/drillerdb-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/drillerdb-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/drillerdb-com/vocabulary/drillerdb-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/drillerdb-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/drillerdb-com/data-model/drillerdb-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/drillerdb-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/drillerdb-com/lifecycle/drillerdb-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/drillerdb-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/drillerdb-com/lifecycle/drillerdb-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/drillerdb-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/drillerdb-com/errors/drillerdb-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/drillerdb-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/drillerdb-com/conformance/drillerdb-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/drillerdb-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/drillerdb-com/llms/drillerdb-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/drillerdb-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/drillerdb-com/well-known/drillerdb-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/drillerdb-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/drillerdb-com/hosts/drillerdb-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/drillerdb-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drillerdb.com/terms
- group: operate
  title: ''
  type: Support
  url: https://drillerdb.com/support
- group: start
  title: ''
  type: SignUp
  url: https://drillerdb.com/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drillerdb.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://drillerdb.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://drillerdb.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://drillerdb.com/docs
- group: company
  title: ''
  type: Blog
  url: https://drillerdb.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://drillerdb.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://console.drillerdb.com/developers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DrillerDB
- group: auth
  href: https://artifacts.apis.io/drillerdb-com/scopes/drillerdb-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/drillerdb-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/drillerdb-com/authentication/drillerdb-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/drillerdb-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/drillerdb-com/security/drillerdb-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drillerdb-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drillerdb.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://drillerdb.com/openapi.json
  - status: null
    url: https://enterprise.drillerdb.com/openapi.json
  - status: 401
    url: https://console.drillerdb.com/api/mcp
  - status: 401
    url: https://enterprise.drillerdb.com/api/mcp
  - status: 200
    url: https://drillerdb.com/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: Water well drilling and pump service software offering quotes, scheduling, well logs, state well reports, job maps, and invoicing. DrillerDB provides a professional plan for drillers to manage projects, track data, and streamline operations. Book a free demo to explore features and improve drilling efficiency.
image: https://drillerdb.com/drillerdb-images/drillingRigOverlay2.jpg
json_schemas:
- name: DrillerLicenseLookupResponse
  property_count: 3
  slug: drillerdb-com-driller-license-lookup-response
- name: JsonRpcRequest
  property_count: 4
  slug: drillerdb-com-json-rpc-request
- name: JsonRpcResponse
  property_count: 4
  slug: drillerdb-com-json-rpc-response
- name: PlatformStats
  property_count: 4
  slug: drillerdb-com-platform-stats
- name: WellDepthInsufficientData
  property_count: 4
  slug: drillerdb-com-well-depth-insufficient-data
- name: WellDepthResult
  property_count: 18
  slug: drillerdb-com-well-depth-result
jsonld:
- class_count: 44
  name: Drillerdb Com Context
  property_count: 146
  slug: drillerdb-com-context
layout: provider
modified: '2026-11-05'
name: DrillerDB
nav: Providers
network: true
overview: 'DrillerDB publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Conferences API, Contacts API, Documentation API, and 10 more. Tagged areas include Water Well, DrillingSoftware, PumpService, Project Management, and Software-as-a-Service.


  The DrillerDB catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DrillerDB''s developer surface includes support, signup flow, pricing, documentation, engineering blog, getting-started guide, API reference, and 22 more developer resources.'
plans:
- name: Drillerdb Com Plans Pricing
  plan_count: 4
  slug: drillerdb-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Drillerdb Com Rate Limits
  slug: drillerdb-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 113
  extends:
  - spectral:oas
  name: DrillerDB API Rules
  rule_count: 72
  severity_counts:
    error: 65
    hint: 0
    info: 1
    warn: 6
  slug: drillerdb-com-rules
scopes:
- name: Drillerdb Com Scopes
  scope_count: 1
  slug: drillerdb-com-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 59.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 65.9
    developer_ergonomics: 47.6
    discoverability: 67.9
    operational_transparency: 44.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Drillerdb Com Authentication
  slug: drillerdb-com-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Drillerdb Com Domain Security
  slug: drillerdb-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: drillerdb-com
tags:
- Water Well
- DrillingSoftware
- PumpService
- Project Management
- Software-as-a-Service
website: https://drillerdb.com/
---
