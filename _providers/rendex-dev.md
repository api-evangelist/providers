---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 62.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Rendex Dev Agentic Access
  operation_count: 21
  slug: rendex-dev-agentic-access
  summary_line: 21 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.rendex.dev
  baseurl_source: declared
  description: Plan, usage, and upgrade information
  name: rendex-dev Account API
  slug: rendex-dev-account-api
- baseURL: https://api.rendex.dev
  baseurl_source: declared
  description: Multi-URL batch capture
  name: rendex-dev Batch API
  slug: rendex-dev-batch-api
- baseURL: https://api.rendex.dev
  baseurl_source: declared
  description: Service health checks
  name: rendex-dev Health API
  slug: rendex-dev-health-api
- baseURL: https://api.rendex.dev
  baseurl_source: declared
  description: Async job and batch status polling
  name: rendex-dev Jobs API
  slug: rendex-dev-jobs-api
- baseURL: https://api.rendex.dev
  baseurl_source: declared
  description: Capture webpage screenshots
  name: rendex-dev Screenshot API
  slug: rendex-dev-screenshot-api
- baseURL: https://api.rendex.dev
  baseurl_source: declared
  description: 'Website change monitoring — create watches, read run history, receive change webhooks. Rendex renders each check in real Chrome, runs a before/after visual (and/or text) diff, and alerts you by email '
  name: rendex-dev Watch API
  slug: rendex-dev-watch-api
artifact_total: 27
asyncapis:
- description: ''
  name: Rendex Dev Webhooks
  slug: rendex-dev-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/rendex-dev/agentic-access/rendex-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rendex-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/rendex-dev/rate-limits/rendex-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rendex-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/rendex-dev/plans/rendex-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rendex-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/rendex-dev/rules/rendex-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/rendex-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/rendex-dev/json-ld/rendex-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rendex-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/rendex-dev/vocabulary/rendex-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rendex-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/rendex-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/rendex-dev/asyncapi/rendex-dev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/rendex-dev-webhooks.yml
- group: design
  href: https://artifacts.apis.io/rendex-dev/data-model/rendex-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rendex-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/rendex-dev/authentication/rendex-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rendex-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/rendex-dev/lifecycle/rendex-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rendex-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/rendex-dev/errors/rendex-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rendex-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rendex-dev/conformance/rendex-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rendex-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rendex-dev/llms/rendex-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rendex-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/rendex-dev/mcp/rendex-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/rendex-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/rendex-dev/mcp/rendex-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rendex-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/rendex-dev/well-known/rendex-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rendex-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/rendex-dev/well-known/rendex-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rendex-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/rendex-dev/hosts/rendex-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rendex-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/rendex-dev/vendors/rendex-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rendex-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/rendex-dev/packages/rendex-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/rendex-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/rendex-dev/packages/rendex-dev-packages.yml
  title: ''
  type: Packages
  url: packages/rendex-dev-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://rendex.dev/status
- group: auth
  title: ''
  type: Security
  url: https://rendex.dev/security
- group: start
  title: ''
  type: Login
  url: https://rendex.dev/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://rendex.dev/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.rendex.dev</span
- group: auth
  href: https://artifacts.apis.io/rendex-dev/security/rendex-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/rendex-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/rendex-dev/security/rendex-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rendex-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rendex.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://rendex.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://rendex.dev/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://rendex.dev/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://rendex.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rendex.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rendex.dev/privacy
- group: company
  title: ''
  type: Blog
  url: https://rendex.dev/blog
created: '2026-10-31'
description: Rendex provides a rendering API that converts HTML, URLs, or Markdown into images, PDFs, and OG graphics. It supports batch processing, geo‑targeted captures, signed webhooks, and integrates with automation platforms like n8n, Make, Zapier, and AI agents via MCP. Free tier offers 100 renders per month, with paid plans scaling to enterprise needs.
image: https://rendex.dev/opengraph-image?8389e348edd4f2d1
json_schemas:
- name: CreateWatchRequest
  property_count: 10
  slug: rendex-dev-create-watch-request
- name: ScreenshotJsonResponse
  property_count: 3
  slug: rendex-dev-screenshot-json-response
- name: ScreenshotRequest
  property_count: 43
  slug: rendex-dev-screenshot-request
- name: UpdateWatchRequest
  property_count: 10
  slug: rendex-dev-update-watch-request
- name: WatchRun
  property_count: 18
  slug: rendex-dev-watch-run
- name: Watch
  property_count: 22
  slug: rendex-dev-watch
jsonld:
- class_count: 19
  name: Rendex Dev Context
  property_count: 107
  slug: rendex-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.rendex.dev requiring OAuth.
  name: rendex-dev MCP Server
  slug: rendex-dev-mcp-yml
modified: '2026-10-31'
name: rendex-dev
nav: Providers
network: true
overview: 'rendex-dev publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Batch API, Health API, and 3 more. Tagged areas include Rendering, Screenshot, PDF, API, and Automation.


  The rendex-dev catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  rendex-dev''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, pricing, engineering blog, and 30 more developer resources.'
plans:
- name: Rendex Dev Plans Pricing
  plan_count: 5
  slug: rendex-dev-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Rendex Dev Rate Limits
  slug: rendex-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: rendex-dev API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 1
  slug: rendex-dev-rules
scopes:
- name: Rendex Dev Scopes
  scope_count: 0
  slug: rendex-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 75.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 99.3
    catalog_earned_first_party: 0.0
    catalog_gap: 15.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 69.0
    developer_ergonomics: 66.0
    discoverability: 65.0
    operational_transparency: 78.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Rendex Dev Authentication
  slug: rendex-dev-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Rendex Dev Domain Security
  slug: rendex-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rendex Dev Vulnerability Disclosure
  slug: rendex-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: rendex-account
  slug: rendex-dev-account
- name: rendex-extract
  slug: rendex-dev-extract
- name: rendex-render-link
  slug: rendex-dev-render-link
- name: rendex-screenshot
  slug: rendex-dev-screenshot
slug: rendex-dev
tags:
- Rendering
- Screenshot
- PDF
- API
- Automation
website: https://rendex.dev/
---
