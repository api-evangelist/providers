---
access_model:
  confidence: high
  label: Public
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://webscraping.ai/#pricing
  - https://webscraping.ai/dashboard/api-request-builder
  - https://webscraping.ai/docs
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 63.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Webscraping Ai Agentic Access
  operation_count: 7
  slug: webscraping-ai-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: Hosted remote Model Context Protocol server exposing the same seven capabilities as tools to AI assistants. Streamable HTTP transport, OAuth 2.1 login with PKCE and dynamic client registration, no API
  name: WebScraping.AI MCP Server
  slug: webscrapingai-mcp-server
- baseURL: https://api.webscraping.ai
  baseurl_source: declared
  description: Information about your account API credits quota
  name: WebScraping.AI Account API
  slug: webscraping-ai-account-api
- baseURL: https://api.webscraping.ai
  baseurl_source: declared
  description: Analyze web pages using LLMs
  name: WebScraping.AI AI API
  slug: webscraping-ai-ai-api
- baseURL: https://api.webscraping.ai
  baseurl_source: declared
  description: Get full HTML content of pages using proxies and Chromium JS rendering
  name: WebScraping.AI HTML API
  slug: webscraping-ai-html-api
- baseURL: https://api.webscraping.ai
  baseurl_source: declared
  description: Get HTML content of selected page areas (like price, search results, page title, etc.)
  name: WebScraping.AI Selected HTML API
  slug: webscraping-ai-selected-html-api
- baseURL: https://api.webscraping.ai
  baseurl_source: declared
  description: Get visible text of pages using proxies and Chromium JS rendering
  name: WebScraping.AI Text API
  slug: webscraping-ai-text-api
artifact_total: 21
collections:
- collection_type: open
  name: WebScraping.AI Account API
  slug: open-webscraping-ai-account-api
- collection_type: open
  name: WebScraping. AI API
  slug: open-webscraping-ai-ai-api
- collection_type: open
  name: WebScraping.AI HTML API
  slug: open-webscraping-ai-html-api
- collection_type: open
  name: WebScraping.AI Selected HTML API
  slug: open-webscraping-ai-selected-html-api
- collection_type: open
  name: WebScraping.AI Text API
  slug: open-webscraping-ai-text-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/webscraping-ai/webscraping-ai-mcp-server/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/webscraping-ai/webscraping-ai-mcp-server/releases
- group: docs
  href: https://artifacts.apis.io/webscraping-ai/openapi/_original/webscraping-ai-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/webscraping-ai-openapi.yml
- group: other
  href: https://artifacts.apis.io/webscraping-ai/overlays/webscraping-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/webscraping-ai-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/webscraping-ai/agentic-access/webscraping-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/webscraping-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/webscraping-ai/authentication/webscraping-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/webscraping-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/webscraping-ai/security/webscraping-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/webscraping-ai-domain-security.yml
- group: design
  href: https://artifacts.apis.io/webscraping-ai/conventions/webscraping-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/webscraping-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/webscraping-ai/conventions/webscraping-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/webscraping-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/webscraping-ai/errors/webscraping-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/webscraping-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/webscraping-ai/lifecycle/webscraping-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/webscraping-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/webscraping-ai/conformance/webscraping-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/webscraping-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/webscraping-ai/data-model/webscraping-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/webscraping-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/webscraping-ai/rate-limits/webscraping-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/webscraping-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/webscraping-ai/plans/webscraping-ai-plans.yml
  title: ''
  type: Plans
  url: plans/webscraping-ai-plans.yml
- group: build
  href: https://artifacts.apis.io/webscraping-ai/packages/webscraping-ai-packages.yml
  title: ''
  type: Packages
  url: packages/webscraping-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/webscraping-ai/packages/webscraping-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/webscraping-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/webscraping-ai/cli/webscraping-ai-cli.yml
  title: ''
  type: CLI
  url: cli/webscraping-ai-cli.yml
- group: start
  href: https://artifacts.apis.io/webscraping-ai/sandbox/webscraping-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/webscraping-ai-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/webscraping-ai/mcp/webscraping-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/webscraping-ai-mcp.yml
- group: build
  href: https://artifacts.apis.io/webscraping-ai/mcp/webscraping-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/webscraping-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/webscraping-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/webscraping-ai/well-known/webscraping-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/webscraping-ai-well-known.yml
- group: agent
  href: https://artifacts.apis.io/webscraping-ai/llms/webscraping-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/webscraping-ai-llms.txt
- group: company
  title: ''
  type: Website
  url: https://webscraping.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://webscraping.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://webscraping.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://webscraping.ai/docs#parameters
- group: start
  title: ''
  type: GettingStarted
  url: https://webscraping.ai/docs#quick-start
- group: start
  title: ''
  type: Console
  url: https://webscraping.ai/dashboard/api-request-builder
- group: commercial
  title: ''
  type: Pricing
  url: https://webscraping.ai/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://webscraping.ai/auth/sign_up
- group: start
  title: ''
  type: Login
  url: https://webscraping.ai/auth/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://webscraping.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://webscraping.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/webscraping-ai
- group: operate
  title: ''
  type: Support
  url: mailto:support@webscraping.ai
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://webscraping.ai/blog
- group: docs
  title: ''
  type: OpenAPI
  url: https://webscraping.ai/openapi.yml
created: '2026-05-28'
description: WebScraping.AI is a web scraping API that returns the rendered HTML, visible text, CSS-selected fragments, or LLM-extracted structured data of any URL, so callers do not have to operate their own scraping infrastructure. The service handles headless Chromium JavaScript rendering, rotating datacenter, residential and stealth proxies, CAPTCHA solving and geotargeting. Seven read-only GET operations on api.webscraping.ai are documented in a published OpenAPI 3.1.0 specification, authenticated with an api_key query parameter, metered in credits and bounded by a per-plan ceiling on concurrent requests. The same capabilities are reachable as a hosted OAuth-protected MCP server for AI assistants, an HTTP proxy front-end for existing scraping tools, an official CLI that ships an installable agent skill, and first-party SDKs for Python, JavaScript, PHP, Ruby, Go, Java and .NET.
finops:
- has_sources: true
  method: derived
  name: Webscraping Ai Finops
  primary_unit: credit
  service_category: ''
  slug: webscraping-ai-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/webscraping-ai.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.webscraping.ai; 7 tools listed.
  name: WebScraping.AI MCP Server
  slug: webscraping-ai-mcp-yml
modified: '2026-08-09'
name: WebScraping.AI
nav: Providers
network: true
overview: 'WebScraping.AI publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, AI API, HTML API, and 3 more. Tagged areas include Web Scraping, Data Extraction, Proxies, Artificial Intelligence, and Browser Automation.


  The WebScraping.AI catalog on APIs.io includes 1 Spectral governance ruleset.


  WebScraping.AI''s developer surface includes authentication, CLI, sandbox, documentation, API reference, getting-started guide, developer console, and 33 more developer resources.'
plans:
- name: Webscraping Ai Plans
  plan_count: 5
  slug: webscraping-ai-plans
- name: Webscraping Ai Price Estimates
  plan_count: 0
  slug: webscraping-ai-price-estimates
random_paper: 4
rate_limits:
- limit_count: 4
  name: Webscraping Ai Rate Limits
  slug: webscraping-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: WebScraping.AI API Rules
  rule_count: 62
  severity_counts:
    error: 59
    hint: 0
    info: 2
    warn: 1
  slug: webscraping-ai-rules
score:
  band: strong
  composite: 62.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 85.7
    discoverability: 75.0
    operational_transparency: 50.0
  previous_composite: 62.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/webscraping-ai/webscraping-ai-2026-06-20T201335.png
security:
- kind: authentication
  name: Webscraping Ai Authentication
  slug: webscraping-ai-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Webscraping Ai Domain Security
  slug: webscraping-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: webscraping-ai
  slug: webscraping-ai-cli-skill
slug: webscraping-ai
tags:
- Web Scraping
- Data Extraction
- Proxies
- Artificial Intelligence
- Browser Automation
- MCP
- Development
- Public APIs
- HTML
- LLM Tools
- Structured Data
- CAPTCHA
website: https://webscraping.ai/
---
