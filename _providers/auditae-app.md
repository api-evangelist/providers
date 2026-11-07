---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Auditae App Agentic Access
  operation_count: 21
  slug: auditae-app-agentic-access
  summary_line: 21 operations · 12 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://auditae.app
  baseurl_source: declared
  description: Balance, prices and top-ups.
  name: AuditAE Billing API
  slug: auditae-app-billing-api
- baseURL: https://auditae.app
  baseurl_source: declared
  description: Run prompts on answer engines and read the results.
  name: AuditAE Citations API
  slug: auditae-app-citations-api
- baseURL: https://auditae.app
  baseurl_source: declared
  description: JSON-LD generation, validation and Wikidata lookups.
  name: AuditAE Schema API
  slug: auditae-app-schema-api
- baseURL: https://auditae.app
  baseurl_source: declared
  description: Page checks and site crawls.
  name: AuditAE Technical API
  slug: auditae-app-technical-api
artifact_total: 20
common:
- group: auth
  href: https://artifacts.apis.io/auditae-app/well-known/auditae-app-wordpress-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/auditae-app-wordpress-security.txt
- group: agent
  href: https://artifacts.apis.io/auditae-app/agentic-access/auditae-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/auditae-app-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/auditae-app/rate-limits/auditae-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/auditae-app-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/auditae-app/plans/auditae-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/auditae-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/auditae-app/rules/auditae-app-rules.yml
  title: ''
  type: Spectral
  url: rules/auditae-app-rules.yml
- group: design
  href: https://artifacts.apis.io/auditae-app/json-ld/auditae-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/auditae-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/auditae-app/vocabulary/auditae-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/auditae-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/auditae-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/auditae-app/data-model/auditae-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/auditae-app-data-model.yml
- group: auth
  href: https://artifacts.apis.io/auditae-app/authentication/auditae-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/auditae-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/auditae-app/errors/auditae-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/auditae-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/auditae-app/conformance/auditae-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/auditae-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/auditae-app/llms/auditae-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auditae-app-llms.txt
- group: build
  href: https://artifacts.apis.io/auditae-app/mcp/auditae-app-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/auditae-app-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/auditae-app/mcp/auditae-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/auditae-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/auditae-app/well-known/auditae-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/auditae-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/auditae-app/hosts/auditae-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auditae-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/auditae-app/vendors/auditae-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auditae-app-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://auditae.app/sign-up?redirect_url=%2Fdashboard%2Foverview%3Fsrc%3Dheader&src=header
- group: start
  title: ''
  type: GettingStarted
  url: https://auditae.app/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/auditae-app/security/auditae-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auditae-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auditae.app/
- group: docs
  title: ''
  type: Documentation
  url: https://auditae.app/docs
- group: docs
  title: ''
  type: APIReference
  url: https://auditae.app/api
- group: commercial
  title: ''
  type: Pricing
  url: https://auditae.app/pricing
- group: company
  title: ''
  type: Blog
  url: https://auditae.app/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://auditae.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auditae.app/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://auditae.app/openapi.json
  - status: 401
    url: https://auditae.app/api/mcp
  - status: 401
    url: https://auditae.app/api/graphql
  - status: 200
    url: https://auditae.app/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: AuditAE provides AI visibility tracking software that monitors whether large language model responses such as ChatGPT, Perplexity, Gemini, and Google AI Overviews cite your brand when users ask questions related to your product category. The platform offers automated checks, highlights gaps, and suggests precise edits to improve AI search citation, with pricing starting at $5 free and per‑check costs as low as 5–12¢.
image: https://auditae.app/opengraph-image?2b4c3c69e9f271c7
json_schemas:
- name: CrawlCheckDetail
  property_count: 14
  slug: auditae-app-crawl-check-detail
- name: CrawlCheck
  property_count: 15
  slug: auditae-app-crawl-check
- name: CrawlComparison
  property_count: 15
  slug: auditae-app-crawl-comparison
- name: CrawlResult
  property_count: 36
  slug: auditae-app-crawl-result
- name: CrawlSettings
  property_count: 13
  slug: auditae-app-crawl-settings
- name: DiscoveredEntity
  property_count: 14
  slug: auditae-app-discovered-entity
jsonld:
- class_count: 38
  name: Auditae App Context
  property_count: 236
  slug: auditae-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at auditae.app.
  name: AuditAE MCP Server
  slug: auditae-app-mcp-yml
modified: '2026-11-02'
name: AuditAE
nav: Providers
network: true
overview: 'AuditAE publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Citations API, Schema API, and 1 more. Tagged areas include Artificial Intelligence, SEO, Marketing, Software-as-a-Service, and Visibility.


  The AuditAE catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AuditAE''s developer surface includes authentication, signup flow, getting-started guide, documentation, API reference, pricing, engineering blog, and 21 more developer resources.'
plans:
- name: Auditae App Plans Pricing
  plan_count: 1
  slug: auditae-app-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Auditae App Rate Limits
  slug: auditae-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: AuditAE API Rules
  rule_count: 63
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 7
  slug: auditae-app-rules
scopes:
- name: Auditae App Scopes
  scope_count: 0
  slug: auditae-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 68.4
    developer_ergonomics: 33.8
    discoverability: 65.0
    operational_transparency: 42.1
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
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
  name: Auditae App Authentication
  slug: auditae-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Auditae App Domain Security
  slug: auditae-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: check-citation
  slug: check-citation
slug: auditae-app
tags:
- Artificial Intelligence
- SEO
- Marketing
- Software-as-a-Service
- Visibility
website: https://auditae.app/
---
