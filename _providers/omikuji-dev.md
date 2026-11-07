---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: MCP (Machine-Readable API) endpoint requiring OAuth authentication, returning 401 when accessed anonymously.
  name: MCP API
  slug: mcp-api
- baseURL: https://tools.omikuji.dev
  baseurl_source: declared
  description: 'omikuji-dev API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: omikuji-dev API
  slug: omikuji-dev-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/omikuji-dev/rules/omikuji-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/omikuji-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/omikuji-dev/json-ld/omikuji-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/omikuji-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/omikuji-dev/vocabulary/omikuji-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/omikuji-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/omikuji-dev/data-model/omikuji-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/omikuji-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/omikuji-dev/conformance/omikuji-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/omikuji-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/omikuji-dev/llms/omikuji-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/omikuji-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/omikuji-dev/mcp/omikuji-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/omikuji-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/omikuji-dev/hosts/omikuji-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/omikuji-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/omikuji-dev/vendors/omikuji-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/omikuji-dev-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.hatenablog.com/
- group: auth
  href: https://artifacts.apis.io/omikuji-dev/security/omikuji-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/omikuji-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://omikuji.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://omikuji.dev/about/
- group: operate
  title: ''
  type: Support
  url: https://omikuji.dev/contact/
- group: company
  title: ''
  type: Blog
  url: https://omikuji-dev.hatenablog.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/omikuji
- group: commercial
  title: ''
  type: TermsOfService
  url: https://omikuji.dev/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://omikuji.dev/privacy/
coverage:
  checked: '2026-10-29'
  detail: MCP endpoint https://omikuji.dev/mcp returns 401 Unauthorized, indicating authentication is required.
  evidence:
  - status: 401
    url: https://omikuji.dev/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: omikuji.dev is a Japanese personal blog and tool hub that shares gadget reviews, home‑server projects, parenting and daily life notes. It also offers a collection of free browser‑only tools such as emoji, kaomoji, color palettes, holiday calendars, vehicle‑plate lookup, and many more, all open to the public.
image: https://omikuji.dev/og-default.jpg
json_schemas:
- name: GetCdnCgiTraceResponse
  property_count: 1
  slug: omikuji-dev-get-cdn-cgi-trace-response
- name: GetRestNetworkconfResponse
  property_count: 3
  slug: omikuji-dev-get-rest-networkconf-response
- name: PostApiMcpAuthCallbackRequest
  property_count: 3
  slug: omikuji-dev-post-api-mcp-auth-callback-request
- name: PostMcpResponse
  property_count: 3
  slug: omikuji-dev-post-mcp-response
jsonld:
- class_count: 4
  name: Omikuji Dev Context
  property_count: 10
  slug: omikuji-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at omikuji.dev.
  name: omikuji-dev MCP Server
  slug: omikuji-dev-mcp-yml
modified: '2026-10-29'
name: omikuji-dev
nav: Providers
network: true
overview: 'omikuji-dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blog, Tools, Gadgets, and Personal Development.


  The omikuji-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  omikuji-dev''s developer surface includes documentation, getting-started guide, support, engineering blog, and 14 more developer resources.'
plans:
- name: Omikuji Dev Plans Pricing
  plan_count: 0
  slug: omikuji-dev-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Omikuji Dev Rate Limits
  slug: omikuji-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: omikuji-dev API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: omikuji-dev-rules
scopes:
- name: Omikuji Dev Scopes
  scope_count: 0
  slug: omikuji-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 14.3
    discoverability: 75.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 27.9
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
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/omikuji-dev/omikuji-dev-2026-11-03T140533.png
security:
- kind: authentication
  name: Omikuji Dev Authentication
  slug: omikuji-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Omikuji Dev Domain Security
  slug: omikuji-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: omikuji-dev
tags:
- Company
- Blog
- Tools
- Gadgets
- Personal Development
website: https://omikuji.dev/
---
