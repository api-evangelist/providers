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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Instapi.co provides an Instagram search and post enrichment API. It allows developers to query Instagram users, hashtags, places, and retrieve posts with AI-parsed text, images, and videos.
  name: Instapi API
  slug: instapi-api
- description: 'instapi-co API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: instapi-co API
  slug: instapi-co-api
artifact_total: 16
common:
- group: commercial
  href: https://artifacts.apis.io/instapi-co/plans/instapi-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/instapi-co-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/instapi-co/rules/instapi-co-rules.yml
  title: ''
  type: Spectral
  url: rules/instapi-co-rules.yml
- group: design
  href: https://artifacts.apis.io/instapi-co/json-ld/instapi-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/instapi-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/instapi-co/vocabulary/instapi-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/instapi-co-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/instapi-co/data-model/instapi-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/instapi-co-data-model.yml
- group: auth
  href: https://artifacts.apis.io/instapi-co/authentication/instapi-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/instapi-co-authentication.yml
- group: design
  href: https://artifacts.apis.io/instapi-co/errors/instapi-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/instapi-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/instapi-co/conformance/instapi-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/instapi-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/instapi-co/llms/instapi-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/instapi-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/instapi-co/mcp/instapi-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/instapi-co-mcp.yml
- group: other
  href: https://artifacts.apis.io/instapi-co/hosts/instapi-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/instapi-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/instapi-co/vendors/instapi-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/instapi-co-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://instapi.co/api/help
- group: start
  title: ''
  type: Login
  url: https://instapi.co/app/login
- group: auth
  href: https://artifacts.apis.io/instapi-co/security/instapi-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/instapi-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://instapi.co/
- group: docs
  title: ''
  type: Documentation
  url: https://instapi.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://instapi.co/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://instapi.co/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://instapi.co/docs
created: '2026-10-30'
description: Instapi.co provides an Instagram search and post enrichment API. It allows developers to query Instagram users, hashtags, places, and retrieve posts with AI-parsed text, images, and videos. The service offers a free tier with 10 credits on signup and charges per request thereafter. Authentication is via Bearer tokens, supporting JWTs prefixed with jwt_instapi_ and API keys prefixed with sk_instapi_. The API is accessible via REST endpoints and a hosted MCP streaming server.
image: https://instapi.co/favicon.png
json_schemas:
- name: GetApiInstagramUsersUsernamePostsResponse
  property_count: 9
  slug: instapi-co-get-api-instagram-users-username-posts-response
- name: GetApiInstagramUsersUsernameResponse
  property_count: 16
  slug: instapi-co-get-api-instagram-users-username-response
- name: GetApiKeysResponse
  property_count: 2
  slug: instapi-co-get-api-keys-response
- name: GetApiStatusResponse
  property_count: 4
  slug: instapi-co-get-api-status-response
- name: PostApiLoginRequest
  property_count: 2
  slug: instapi-co-post-api-login-request
- name: PostApiLoginResponse
  property_count: 3
  slug: instapi-co-post-api-login-response
jsonld:
- class_count: 12
  name: Instapi Co Context
  property_count: 34
  slug: instapi-co-context
layout: provider
mcp_servers:
- description: Remote MCP server at instapi.co requiring an API key.
  name: instapi-co MCP Server
  slug: instapi-co-mcp-yml
modified: '2026-10-30'
name: instapi-co
nav: Providers
network: true
overview: 'instapi-co is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Instagram, Search, Data Enrichment, and Social Media.


  The instapi-co catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  instapi-co''s developer surface includes authentication, support, documentation, API reference, getting-started guide, and 15 more developer resources.'
plans:
- name: Instapi Co Plans Pricing
  plan_count: 2
  slug: instapi-co-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Instapi Co Rate Limits
  slug: instapi-co-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: instapi-co API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: instapi-co-rules
scopes:
- name: Instapi Co Scopes
  scope_count: 0
  slug: instapi-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 60.8
    catalog_earned_first_party: 8.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 27.6
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 33.3
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 34.0
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
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/instapi-co/instapi-co-2026-11-03T133853.png
security:
- kind: authentication
  name: Instapi Co Authentication
  slug: instapi-co-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Instapi Co Domain Security
  slug: instapi-co-domain-security
  summary_line: TLSv1.3
slug: instapi-co
tags:
- Instagram
- Search
- Data Enrichment
- Social Media
website: https://instapi.co/
---
