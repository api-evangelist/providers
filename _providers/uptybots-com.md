---
access_model:
  confidence: medium
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API for accessing monitors, stats, notifications, account info, and API keys.
  name: UptyBots API
  slug: uptybots-api
- description: 'uptybots-com API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: uptybots-com API
  slug: uptybots-com-api
artifact_total: 16
common:
- group: commercial
  href: https://artifacts.apis.io/uptybots-com/plans/uptybots-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/uptybots-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/uptybots-com/rules/uptybots-com-rules.yml
  title: ''
  type: Spectral
  url: rules/uptybots-com-rules.yml
- group: design
  href: https://artifacts.apis.io/uptybots-com/json-ld/uptybots-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/uptybots-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/uptybots-com/vocabulary/uptybots-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/uptybots-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/uptybots-com/data-model/uptybots-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/uptybots-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/uptybots-com/conventions/uptybots-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/uptybots-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/uptybots-com/authentication/uptybots-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/uptybots-com-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://uptybots.com/system/status
- group: design
  href: https://artifacts.apis.io/uptybots-com/lifecycle/uptybots-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/uptybots-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/uptybots-com/errors/uptybots-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/uptybots-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/uptybots-com/conformance/uptybots-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/uptybots-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/uptybots-com/mcp/uptybots-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/uptybots-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/uptybots-com/well-known/uptybots-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/uptybots-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/uptybots-com/hosts/uptybots-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/uptybots-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/uptybots-com/vendors/uptybots-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/uptybots-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/uptybots-com/packages/uptybots-com-packages.yml
  title: ''
  type: SDKs
  url: packages/uptybots-com-packages.yml
- group: build
  href: https://artifacts.apis.io/uptybots-com/packages/uptybots-com-packages.yml
  title: ''
  type: Packages
  url: packages/uptybots-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uptybots.com/page/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uptybots.com/page/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://uptybots.com/blog/uptime-monitoring-for-agencies-a-practical-setup-for-50-client-sites
- group: auth
  href: https://artifacts.apis.io/uptybots-com/security/uptybots-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uptybots-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uptybots.com/
- group: docs
  title: ''
  type: Documentation
  url: https://uptybots.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://uptybots.com/docs/api
- group: company
  title: ''
  type: Blog
  url: https://uptybots.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uptybots
- group: commercial
  title: ''
  type: Pricing
  url: https://uptybots.com/pricing
- group: start
  title: ''
  type: Login
  url: https://uptybots.com/login
- group: start
  title: ''
  type: SignUp
  url: https://uptybots.com/register
coverage:
  checked: '2026-10-31'
  detail: The API reference is public HTML but no OpenAPI/AsyncAPI/GraphQL spec is published.
  evidence:
  - status: 200
    url: https://uptybots.com/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 'Uptime monitoring built for AI-first developers. Monitor websites, APIs, SSL, domains & ports; connect Claude, Cursor or any AI assistant via MCP. Start free. Uptime monitoring platform built for AI-first developers: websites, APIs, SSL certificates, domains, and servers, with native MCP access for AI assistants.'
image: https://uptybots.com/img/logo.png
json_schemas:
- name: GetApiTargetIncidentsResponse
  property_count: 1
  slug: uptybots-com-get-api-target-incidents-response
- name: GetApiTargetStatsDailiesResponse
  property_count: 1
  slug: uptybots-com-get-api-target-stats-dailies-response
- name: GetApiTargetStatsHourliesResponse
  property_count: 5
  slug: uptybots-com-get-api-target-stats-hourlies-response
- name: GetApiTargetsIdResponse
  property_count: 4
  slug: uptybots-com-get-api-targets-id-response
- name: PostApiTargetsTypePortRequest
  property_count: 2
  slug: uptybots-com-post-api-targets-type-port-request
- name: PostApiUserApiKeysResponse
  property_count: 5
  slug: uptybots-com-post-api-user-api-keys-response
jsonld:
- class_count: 15
  name: Uptybots Com Context
  property_count: 9
  slug: uptybots-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.uptybots.com.
  name: uptybots-com MCP Server
  slug: uptybots-com-mcp-yml
modified: '2026-10-31'
name: uptybots-com
nav: Providers
network: true
overview: 'uptybots-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Monitoring, Uptime, Artificial Intelligence, and MCP.


  The uptybots-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  uptybots-com''s developer surface includes authentication, getting-started guide, documentation, API reference, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Uptybots Com Plans Pricing
  plan_count: 4
  slug: uptybots-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Uptybots Com Rate Limits
  slug: uptybots-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: uptybots-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: uptybots-com-rules
scopes:
- name: Uptybots Com Scopes
  scope_count: 0
  slug: uptybots-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 22.7
    developer_ergonomics: 34.5
    discoverability: 56.7
    operational_transparency: 10.5
  previous_composite: 44.5
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
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Uptybots Com Authentication
  slug: uptybots-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Uptybots Com Domain Security
  slug: uptybots-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uptybots-com
tags:
- Company
- Monitoring
- Uptime
- Artificial Intelligence
- MCP
website: https://uptybots.com/
---
