---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Ayushrai Site Agentic Access
  operation_count: 9
  slug: ayushrai-site-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- baseURL: https://www.ayushrai.site
  baseurl_source: declared
  description: The Ask API from ayushrai-site — 1 operation(s) for ask.
  name: ayushrai-site Ask API
  slug: ayushrai-site-ask-api
- baseURL: https://www.ayushrai.site
  baseurl_source: declared
  description: The Compare API from ayushrai-site — 1 operation(s) for compare.
  name: ayushrai-site Compare API
  slug: ayushrai-site-compare-api
- baseURL: https://www.ayushrai.site
  baseurl_source: declared
  description: The Mcp API from ayushrai-site — 1 operation(s) for mcp.
  name: ayushrai-site MCP API
  slug: ayushrai-site-mcp-api
- baseURL: https://www.ayushrai.site
  baseurl_source: declared
  description: The Projects API from ayushrai-site — 3 operation(s) for projects.
  name: ayushrai-site Projects API
  slug: ayushrai-site-projects-api
- baseURL: https://www.ayushrai.site
  baseurl_source: declared
  description: The Search API from ayushrai-site — 2 operation(s) for search.
  name: ayushrai-site Search API
  slug: ayushrai-site-search-api
artifact_total: 22
common:
- group: auth
  href: https://artifacts.apis.io/ayushrai-site/well-known/ayushrai-site-developers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ayushrai-site-developers-security.txt
- group: agent
  href: https://artifacts.apis.io/ayushrai-site/agentic-access/ayushrai-site-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ayushrai-site-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/ayushrai-site/rate-limits/ayushrai-site-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ayushrai-site-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/ayushrai-site/rules/ayushrai-site-rules.yml
  title: ''
  type: Spectral
  url: rules/ayushrai-site-rules.yml
- group: design
  href: https://artifacts.apis.io/ayushrai-site/json-ld/ayushrai-site-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ayushrai-site-context.jsonld
- group: design
  href: https://artifacts.apis.io/ayushrai-site/vocabulary/ayushrai-site-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ayushrai-site-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ayushrai-site/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ayushrai-site/data-model/ayushrai-site-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ayushrai-site-data-model.yml
- group: build
  href: https://artifacts.apis.io/ayushrai-site/cli/ayushrai-site-cli.yml
  title: ''
  type: CLI
  url: cli/ayushrai-site-cli.yml
- group: design
  href: https://artifacts.apis.io/ayushrai-site/conventions/ayushrai-site-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ayushrai-site-conventions.yml
- group: operate
  href: https://artifacts.apis.io/ayushrai-site/lifecycle/ayushrai-site-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ayushrai-site-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ayushrai-site/lifecycle/ayushrai-site-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ayushrai-site-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ayushrai-site/errors/ayushrai-site-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ayushrai-site-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ayushrai-site/conformance/ayushrai-site-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ayushrai-site-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ayushrai-site/llms/ayushrai-site-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ayushrai-site-llms.txt
- group: other
  href: https://artifacts.apis.io/ayushrai-site/a2a/ayushrai-site-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ayushrai-site-a2a.yml
- group: agent
  href: https://artifacts.apis.io/ayushrai-site/mcp/ayushrai-site-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ayushrai-site-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ayushrai-site/well-known/ayushrai-site-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ayushrai-site-well-known.yml
- group: other
  href: https://artifacts.apis.io/ayushrai-site/hosts/ayushrai-site-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ayushrai-site-hosts.yml
- group: other
  href: https://artifacts.apis.io/ayushrai-site/vendors/ayushrai-site-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ayushrai-site-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.ayushrai.site/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ayushrai.site/developers
- group: auth
  href: https://artifacts.apis.io/ayushrai-site/security/ayushrai-site-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ayushrai-site-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ayushrai.site/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ayushrai.site/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://www.ayushrai.site/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://www.ayushrai.site/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ayushrai.site/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ayushrai-hub
created: '2026-10-29'
description: Ayush Rai is an AI engineer and product builder who runs a personal website ayushrai.site showcasing his work, research, and open‑source projects. The site provides a free, public, read‑only REST API (OpenAPI 3.1) that mirrors the website content, along with an MCP server for tool discovery. The API is keyless, rate‑limited to 60 requests per minute, and includes endpoints for searching projects, retrieving project details, and accessing markdown content. This profile captures the public‑facing API and documentation of Ayush Rai’s personal site.
image: https://www.ayushrai.site/IMG_0029.jpeg
json_schemas:
- name: AskRequest
  property_count: 3
  slug: ayushrai-site-ask-request
- name: AskResponse
  property_count: 7
  slug: ayushrai-site-ask-response
- name: CompareResponse
  property_count: 2
  slug: ayushrai-site-compare-response
- name: ProjectListResponse
  property_count: 3
  slug: ayushrai-site-project-list-response
- name: SearchResponse
  property_count: 5
  slug: ayushrai-site-search-response
- name: ServerCard
  property_count: 8
  slug: ayushrai-site-server-card
jsonld:
- class_count: 10
  name: Ayushrai Site Context
  property_count: 39
  slug: ayushrai-site-context
layout: provider
mcp_servers:
- description: Remote MCP server at life.ayushrai.site.
  name: ayushrai-site MCP Server
  slug: ayushrai-site-mcp-yml
modified: '2026-10-29'
name: ayushrai-site
nav: Providers
network: true
overview: 'ayushrai-site publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ask API, Compare API, MCP API, and 2 more. Tagged areas include Company, Artificial Intelligence, Engineering, Consulting, and Portfolio.


  The ayushrai-site catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ayushrai-site''s developer surface includes CLI, documentation, API reference, support, and 25 more developer resources.'
plans:
- name: Ayushrai Site Plans Pricing
  plan_count: 0
  slug: ayushrai-site-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Ayushrai Site Rate Limits
  slug: ayushrai-site-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: ayushrai-site API Rules
  rule_count: 56
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 7
  slug: ayushrai-site-rules
scopes:
- name: Ayushrai Site Scopes
  scope_count: 0
  slug: ayushrai-site-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 34
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 5.3
    contract_governance: 35.6
    contract_quality: 59.6
    developer_ergonomics: 29.0
    discoverability: 75.8
    operational_transparency: 42.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ayushrai-site/ayushrai-site-2026-11-03T121456.png
security:
- kind: authentication
  name: Ayushrai Site Authentication
  slug: ayushrai-site-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ayushrai Site Domain Security
  slug: ayushrai-site-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: get-project
  slug: get-project
- name: search-portfolio
  slug: search-portfolio
slug: ayushrai-site
tags:
- Company
- Artificial Intelligence
- Engineering
- Consulting
- Portfolio
website: https://ayushrai.site/
---
