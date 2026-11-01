---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://cdn.corenexis.com
  baseurl_source: declared
  description: 'corenexis-com API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: corenexis-com API
  slug: corenexis-com-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/corenexis-com/rate-limits/corenexis-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/corenexis-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/corenexis-com/plans/corenexis-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/corenexis-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/corenexis-com/rules/corenexis-com-rules.yml
  title: ''
  type: Spectral
  url: rules/corenexis-com-rules.yml
- group: design
  href: https://artifacts.apis.io/corenexis-com/json-ld/corenexis-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/corenexis-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/corenexis-com/vocabulary/corenexis-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/corenexis-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/corenexis-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/corenexis-com/data-model/corenexis-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/corenexis-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/corenexis-com/authentication/corenexis-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/corenexis-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/corenexis-com/errors/corenexis-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/corenexis-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/corenexis-com/conformance/corenexis-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/corenexis-com-conformance.yml
- group: build
  href: https://artifacts.apis.io/corenexis-com/mcp/corenexis-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/corenexis-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/corenexis-com/mcp/corenexis-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/corenexis-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/corenexis-com/well-known/corenexis-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/corenexis-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/corenexis-com/hosts/corenexis-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/corenexis-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/corenexis-com/vendors/corenexis-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/corenexis-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://blog.corenexis.com/category/security
- group: auth
  href: https://artifacts.apis.io/corenexis-com/security/corenexis-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/corenexis-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://corenexis.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.corenexis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.corenexis.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.corenexis.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Core-Nexis
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corenexis.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corenexis.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://dash.corenexis.com/auth/login
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.corenexis.com/mcp
  - status: 401
    url: https://cashly.corenexis.com/api/mcp
  - status: 200
    url: https://corenexis.com/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Corenexis builds developer-friendly APIs, a sign‑in service for apps, and Cashly, a smart expense, EMI and debt tracker. The platform offers nine production APIs—including PDF rendering, OCR, image conversion and delivery, email validation, and QR/ barcode generation—accessible via clean REST endpoints with free and paid plans, rate limits, SLA, and dedicated support. Founded in 2022 by Raushan and Shyamini, Corenexis aims to simplify integration for developers and businesses.
image: https://assets.corenexis.com/logo/logo.png
json_schemas:
- name: PostF35At4D5YcjqPdfResponse
  property_count: 4
  slug: corenexis-com-post-f35-at4-d5-ycjq-pdf-response
- name: PostFQlm6VwhvlurPdfResponse
  property_count: 4
  slug: corenexis-com-post-fqlm6-vwhvlur-pdf-response
- name: PostWpJsonCorenexisV1LoginRequest
  property_count: 2
  slug: corenexis-com-post-wp-json-corenexis-v1-login-request
- name: PostWpJsonCorenexisV1PluginsActivateRequest
  property_count: 1
  slug: corenexis-com-post-wp-json-corenexis-v1-plugins-activate-request
- name: PostWpJsonCorenexisV1PostsRequest
  property_count: 7
  slug: corenexis-com-post-wp-json-corenexis-v1-posts-request
- name: PostWpJsonCorenexisV1UsersRequest
  property_count: 9
  slug: corenexis-com-post-wp-json-corenexis-v1-users-request
jsonld:
- class_count: 8
  name: Corenexis Com Context
  property_count: 23
  slug: corenexis-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.corenexis.com requiring an API key.
  name: corenexis-com MCP Server
  slug: corenexis-com-mcp-yml
modified: '2026-10-29'
name: corenexis-com
nav: Providers
network: true
overview: 'corenexis-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, Platform, DeveloperTools, and FinTech.


  The corenexis-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  corenexis-com''s developer surface includes authentication, documentation, engineering blog, signup flow, and 21 more developer resources.'
plans:
- name: Corenexis Com Plans Pricing
  plan_count: 5
  slug: corenexis-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Corenexis Com Rate Limits
  slug: corenexis-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: corenexis-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: corenexis-com-rules
scopes:
- name: Corenexis Com Scopes
  scope_count: 0
  slug: corenexis-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 26.2
    developer_ergonomics: 39.8
    discoverability: 65.0
    operational_transparency: 47.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Corenexis Com Authentication
  slug: corenexis-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Corenexis Com Domain Security
  slug: corenexis-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: markdown-to-pdf
  slug: corenexis-com-markdown-to-pdf
slug: corenexis-com
tags:
- Company
- API
- Platform
- DeveloperTools
- FinTech
- SaaS
website: https://corenexis.com/
---
