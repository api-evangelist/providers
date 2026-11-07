---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: true
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Aveiro API provides endpoints for site management, audience newsletters, social media, and publishing.
  name: Aveiro API
  slug: aveiro-api
- baseURL: https://www.aveiro.app
  baseurl_source: declared
  description: 'Aveiro API as documented publicly: 45 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Aveiro API
  slug: aveiro-app-api
artifact_total: 16
common:
- group: commercial
  href: https://artifacts.apis.io/aveiro-app/plans/aveiro-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aveiro-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aveiro-app/rules/aveiro-app-rules.yml
  title: ''
  type: Spectral
  url: rules/aveiro-app-rules.yml
- group: design
  href: https://artifacts.apis.io/aveiro-app/json-ld/aveiro-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aveiro-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/aveiro-app/vocabulary/aveiro-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aveiro-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aveiro-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aveiro-app/data-model/aveiro-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aveiro-app-data-model.yml
- group: auth
  href: https://artifacts.apis.io/aveiro-app/authentication/aveiro-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aveiro-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aveiro-app/scopes/aveiro-app-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aveiro-app-scopes.yml
- group: design
  href: https://artifacts.apis.io/aveiro-app/errors/aveiro-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aveiro-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aveiro-app/conformance/aveiro-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aveiro-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aveiro-app/llms/aveiro-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aveiro-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/aveiro-app/mcp/aveiro-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aveiro-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aveiro-app/well-known/aveiro-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aveiro-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/aveiro-app/hosts/aveiro-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aveiro-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/aveiro-app/vendors/aveiro-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aveiro-app-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/once-ui-system
- group: start
  title: ''
  type: GettingStarted
  url: https://help.aveiro.app/getting-started/what-is-aveiro
- group: auth
  href: https://artifacts.apis.io/aveiro-app/security/aveiro-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aveiro-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aveiro.app/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aveiro.app/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.aveiro.app/developers
- group: docs
  title: ''
  type: APIReference
  url: https://api.aveiro.app
- group: company
  title: ''
  type: Blog
  url: https://blog.aveiro.app
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aveiro.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.aveiro.app/auth
- group: start
  title: ''
  type: Login
  url: https://www.aveiro.app/auth?login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aveiro.app/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aveiro.app/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@aveiro.app
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.aveiro.app
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract found despite public documentation.
  evidence:
  - status: 200
    url: https://api.aveiro.app/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Aveiro is a no‑code publishing platform that lets users create, style, and publish content across web, email, and social channels from a single workspace. It offers AI‑assisted editing, template marketplaces, newsletter and social publishing, product and merch sales, and analytics. Built on the Once UI design system, Aveiro integrates a suite of tools for content creation, distribution, and monetization, targeting creators and businesses seeking fast, design‑first publishing without code.
image: https://www.aveiro.app/trademarks/wordmark-dark.svg
json_schemas:
- name: GetApiV1SitesSiteidResponse
  property_count: 5
  slug: aveiro-app-get-api-v1-sites-siteid-response
- name: PostApiV1SitesSiteidMediaImportUrlResponse
  property_count: 3
  slug: aveiro-app-post-api-v1-sites-siteid-media-import-url-response
- name: PostApiV1SitesSiteidMediaScreenshotRequest
  property_count: 11
  slug: aveiro-app-post-api-v1-sites-siteid-media-screenshot-request
- name: PostApiV1SitesSiteidMediaScreenshotResponse
  property_count: 10
  slug: aveiro-app-post-api-v1-sites-siteid-media-screenshot-response
- name: PostApiV1SitesSiteidMediaUploadResponse
  property_count: 6
  slug: aveiro-app-post-api-v1-sites-siteid-media-upload-response
- name: PostApiV1SocialPostsRequest
  property_count: 7
  slug: aveiro-app-post-api-v1-social-posts-request
jsonld:
- class_count: 25
  name: Aveiro App Context
  property_count: 71
  slug: aveiro-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.aveiro.app requiring OAuth.
  name: Aveiro MCP Server
  slug: aveiro-app-mcp-yml
modified: '2026-11-02'
name: Aveiro
nav: Providers
network: true
overview: 'Aveiro is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, No-Code, Publishing, Templates, and Artificial Intelligence.


  The Aveiro catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aveiro''s developer surface includes authentication, getting-started guide, documentation, API reference, engineering blog, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Aveiro App Plans Pricing
  plan_count: 4
  slug: aveiro-app-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Aveiro App Rate Limits
  slug: aveiro-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Aveiro API Rules
  rule_count: 45
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 2
  slug: aveiro-app-rules
scopes:
- name: Aveiro App Scopes
  scope_count: 12
  slug: aveiro-app-scopes
  summary_line: 12 scopes
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 41.0
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 46.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
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
  name: Aveiro App Authentication
  slug: aveiro-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aveiro App Domain Security
  slug: aveiro-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aveiro-app
tags:
- Company
- No-Code
- Publishing
- Templates
- Artificial Intelligence
website: https://www.aveiro.app/
---
