---
access_model:
  confidence: high
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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 67.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Cloro Dev Agentic Access
  operation_count: 17
  slug: cloro-dev-agentic-access
  summary_line: 17 operations · 12 acting
api_count: 2
apis:
- description: 'Hosted Model Context Protocol server (Streamable HTTP) wrapping the sync monitor endpoints of api.cloro.dev as nine tools: scrape_chatgpt, scrape_gemini, scrape_copilot, scrape_perplexity, scrape_goog'
  name: cloro MCP server
  slug: cloro-mcp-server
- baseURL: https://api.cloro.dev
  baseurl_source: declared
  description: The Async API from cloro — 5 operation(s) for async.
  name: cloro Async API
  slug: cloro-dev-async-api
- baseURL: https://api.cloro.dev
  baseurl_source: declared
  description: The Countries API from cloro — 1 operation(s) for countries.
  name: cloro Countries API
  slug: cloro-dev-countries-api
- baseURL: https://api.cloro.dev
  baseurl_source: declared
  description: The Credits API from cloro — 1 operation(s) for credits.
  name: cloro Credits API
  slug: cloro-dev-credits-api
- baseURL: https://api.cloro.dev
  baseurl_source: declared
  description: The Monitor API from cloro — 9 operation(s) for monitor.
  name: cloro Monitor API
  slug: cloro-dev-monitor-api
- baseURL: https://api.cloro.dev
  baseurl_source: declared
  description: The States API from cloro — 1 operation(s) for states.
  name: cloro States API
  slug: cloro-dev-states-api
artifact_total: 29
asyncapis:
- description: ''
  name: Cloro Dev Webhooks
  slug: cloro-dev-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/cloro-dev/finops/cloro-dev-finops.yml
  title: ''
  type: FinOps
  url: finops/cloro-dev-finops.yml
- group: build
  href: https://artifacts.apis.io/cloro-dev/integrations/cloro-dev-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/cloro-dev-integration-edges.yml
- group: agent
  href: https://artifacts.apis.io/cloro-dev/agentic-access/cloro-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cloro-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/cloro-dev/rate-limits/cloro-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cloro-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cloro-dev/plans/cloro-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloro-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cloro-dev/rules/cloro-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/cloro-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/cloro-dev/json-ld/cloro-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloro-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloro-dev/vocabulary/cloro-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cloro-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cloro-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cloro-dev/asyncapi/cloro-dev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cloro-dev-webhooks.yml
- group: design
  href: https://artifacts.apis.io/cloro-dev/data-model/cloro-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloro-dev-data-model.yml
- group: operate
  href: https://artifacts.apis.io/cloro-dev/changelog/cloro-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cloro-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/cloro-dev/conventions/cloro-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cloro-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/cloro-dev/conventions/cloro-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloro-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/cloro-dev/security/cloro-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cloro-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cloro-dev/scopes/cloro-dev-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cloro-dev-scopes.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://cloro.dev/docs/guides/versioning
- group: design
  href: https://artifacts.apis.io/cloro-dev/lifecycle/cloro-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cloro-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cloro-dev/errors/cloro-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloro-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cloro-dev/conformance/cloro-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloro-dev-conformance.yml
- group: other
  href: https://artifacts.apis.io/cloro-dev/overlays/cloro-dev-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloro-dev-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/cloro-dev/llms/cloro-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloro-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/cloro-dev/llms/cloro-dev-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloro-dev-docs-llms.txt
- group: other
  href: https://artifacts.apis.io/cloro-dev/a2a/cloro-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cloro-dev-a2a.yml
- group: build
  href: https://artifacts.apis.io/cloro-dev/mcp/cloro-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cloro-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cloro-dev/mcp/cloro-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cloro-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/cloro-dev/well-known/cloro-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cloro-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/cloro-dev/well-known/cloro-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloro-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/cloro-dev/hosts/cloro-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloro-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/cloro-dev/vendors/cloro-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloro-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/cloro-dev/packages/cloro-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/cloro-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/cloro-dev/packages/cloro-dev-packages.yml
  title: ''
  type: Packages
  url: packages/cloro-dev-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://cloro.dev/perplexity/media/
- group: auth
  href: https://artifacts.apis.io/cloro-dev/authentication/cloro-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloro-dev-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cloro-dev/security/cloro-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloro-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cloro-dev/security/cloro-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloro-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloro.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.cloro.dev
- group: docs
  title: ''
  type: Documentation
  url: https://cloro.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cloro.dev/docs/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://cloro.dev/docs/introduction/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://cloro.dev/docs/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://cloro.dev/pricing/
- group: company
  title: ''
  type: Blog
  url: https://cloro.dev/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloro-dev
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.cloro.dev/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloro.dev/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloro.dev/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloro.dev
- group: operate
  title: ''
  type: Support
  url: https://cloro.dev/contact/
- group: company
  title: ''
  type: About
  url: https://cloro.dev/about/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://cloro.dev/llms.txt
- group: build
  title: ''
  type: SDK
  url: https://github.com/cloro-dev/cloro-python
- group: build
  title: ''
  type: SDK
  url: https://github.com/cloro-dev/cloro-node
created: '2026-10-07'
description: 'cloro is one API for Google Search and AI answer engines: a REST surface at api.cloro.dev that submits a prompt to ChatGPT, Gemini, Perplexity, Microsoft Copilot, Google AI Mode, Google Search, Google AI Overview and Google News from a chosen country (and US state) and returns the engine''s answer as structured JSON with parsed text, markdown, cited sources, brand entities, shopping cards and ads. Sync monitor endpoints answer in-line; async tasks and batches of up to 500 run in the background with polling or signed webhooks. Credit-based subscription billing, a free tier of 500 monthly credits, a hosted MCP server at mcp.cloro.dev with OAuth, official Python and TypeScript SDKs, n8n, Zapier and LangChain integrations.'
finops:
- has_sources: true
  method: derived
  name: Cloro Dev Finops
  primary_unit: subscription
  service_category: ''
  slug: cloro-dev-finops
  template: false
image: https://cloro.dev/opengraph.jpg
json_schemas:
- name: AiModeMonitorResponse
  property_count: 2
  slug: cloro-dev-ai-mode-monitor-response
- name: ChatGPTMonitorResponse
  property_count: 2
  slug: cloro-dev-chat-gptmonitor-response
- name: CopilotMonitorResponse
  property_count: 2
  slug: cloro-dev-copilot-monitor-response
- name: GeminiMonitorResponse
  property_count: 2
  slug: cloro-dev-gemini-monitor-response
- name: GoogleMonitorRequest
  property_count: 10
  slug: cloro-dev-google-monitor-request
- name: GoogleMonitorResponse
  property_count: 2
  slug: cloro-dev-google-monitor-response
- name: PerplexityMonitorResponse
  property_count: 2
  slug: cloro-dev-perplexity-monitor-response
jsonld:
- class_count: 61
  name: Cloro Dev Context
  property_count: 135
  slug: cloro-dev-context
layout: provider
mcp_servers:
- description: cloro's hosted Model Context Protocol server. A thin wrapper over api.cloro.dev exposing the sync monitor endpoints as tools; each request forwards the caller's own credential so the API enforces auth
  name: cloro MCP server
  slug: cloro
modified: '2026-10-07'
name: cloro
nav: Providers
network: true
overview: 'cloro publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Async API, Countries API, Credits API, and 3 more. Tagged areas include Company, Search, Artificial Intelligence, Web Scraping, and SERP.


  The cloro catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  cloro''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 47 more developer resources.'
plans:
- name: Cloro Dev Plans Pricing
  plan_count: 11
  slug: cloro-dev-plans-pricing
- name: Cloro Dev Price Estimates
  plan_count: 0
  slug: cloro-dev-price-estimates
random_paper: 19
rate_limits:
- limit_count: 2
  name: Cloro Dev Rate Limits
  slug: cloro-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 111
  extends:
  - spectral:oas
  name: cloro API Rules
  rule_count: 70
  severity_counts:
    error: 65
    hint: 0
    info: 2
    warn: 3
  slug: cloro-dev-rules
scopes:
- name: Cloro Dev Scopes
  scope_count: 3
  slug: cloro-dev-scopes
  summary_line: 3 scopes
score:
  band: strong
  composite: 62.4
  coverage:
    artifact_dirs: 35
    catalog_earned: 85.8
    catalog_earned_first_party: 20.0
    catalog_gap: 29.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.8
  facets:
    access_clarity: 61.8
    contract_governance: 35.6
    contract_quality: 76.9
    developer_ergonomics: 47.0
    discoverability: 75.8
    operational_transparency: 57.9
  previous_composite: 76.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 33.3
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cloro-dev/cloro-dev-2026-10-11T103054.png
security:
- kind: authentication
  name: Cloro Dev Authentication
  slug: cloro-dev-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Cloro Dev Domain Security
  slug: cloro-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cloro Dev Vulnerability Disclosure
  slug: cloro-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: google-serp-and-ai-overview
  slug: cloro-dev-google-serp-and-ai-overview
- name: monitor-ai-answer
  slug: cloro-dev-monitor-ai-answer
- name: track-prompts-async
  slug: cloro-dev-track-prompts-async
slug: cloro-dev
tags:
- Company
- Search
- Artificial Intelligence
- Web Scraping
- SERP
- Generative Engine Optimization
- SEO
- Brand Monitoring
- Market Research
- Data Extraction
- MCP
website: https://cloro.dev
---
