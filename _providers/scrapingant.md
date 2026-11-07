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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Scrapingant Agentic Access
  operation_count: 6
  slug: scrapingant-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 2
apis:
- description: ScrapingAnt is a web scraping API service that handles proxy rotation, headless browsers, and CAPTCHA solving for reliable web data extraction.
  name: ScrapingAnt
  slug: scrapingant
- baseURL: https://api.scrapingant.com
  baseurl_source: declared
  description: The ScrapingAnt web scraping endpoint. GET/POST/PUT/PATCH/DELETE /v2/general renders a target URL in headless Chrome behind rotating proxies and returns the page HTML; a non-GET method is proxied thro
  name: ScrapingAnt Scraping API
  slug: scrapingant-scraping-api
- baseURL: https://api.scrapingant.com
  baseurl_source: declared
  description: Account credit metering for ScrapingAnt. GET /v2/usage returns the current plan name, subscription period, total plan credits and remaining credits - the only way to observe budget on an API that publ
  name: ScrapingAnt Usage API
  slug: scrapingant-usage-api
- description: First-party hosted remote MCP server at https://api.scrapingant.com/mcp/ exposing get_web_page_html, get_web_page_markdown and get_web_page_text to MCP clients over streamable HTTP, authenticated with
  name: ScrapingAnt MCP Server
  slug: scrapingant-mcp-server
- baseURL: https://api.scrapingant.com/v2
  baseurl_source: declared
  description: The General API from ScrapingAnt — 1 operation(s) for general.
  name: ScrapingAnt General API
  slug: scrapingant-general-api
artifact_total: 19
collections:
- collection_type: open
  name: ScrapingAnt Scraping API
  slug: open-scrapingant-scraping-api
- collection_type: open
  name: ScrapingAnt
  slug: open-scrapingant
common:
- group: agent
  href: https://artifacts.apis.io/scrapingant/agentic-access/scrapingant-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/scrapingant-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/scrapingant/security/scrapingant-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scrapingant-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/scrapingant/authentication/scrapingant-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scrapingant-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ScrapingAnt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scrapingant
- group: company
  title: ''
  type: Website
  url: https://scrapingant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scrapingant.com/
- group: company
  title: ''
  type: Blog
  url: https://scrapingant.com/blog/rss.xml
- group: build
  href: https://artifacts.apis.io/scrapingant/packages/scrapingant-packages.yml
  title: ''
  type: Packages
  url: packages/scrapingant-packages.yml
- group: build
  href: https://artifacts.apis.io/scrapingant/packages/scrapingant-packages.yml
  title: ''
  type: SDKs
  url: packages/scrapingant-packages.yml
- group: agent
  href: https://artifacts.apis.io/scrapingant/mcp/scrapingant-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/scrapingant-mcp.yml
- group: build
  href: https://artifacts.apis.io/scrapingant/mcp/scrapingant-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/scrapingant-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/scrapingant/llms/scrapingant-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scrapingant-llms.txt
- group: other
  href: https://artifacts.apis.io/scrapingant/overlays/scrapingant-scraping-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scrapingant-scraping-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/scrapingant/conformance/scrapingant-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scrapingant-conformance.yml
- group: design
  href: https://artifacts.apis.io/scrapingant/errors/scrapingant-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scrapingant-problem-types.yml
- group: design
  href: https://artifacts.apis.io/scrapingant/lifecycle/scrapingant-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/scrapingant-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/scrapingant/conventions/scrapingant-conventions.yml
  title: ''
  type: Conventions
  url: conventions/scrapingant-conventions.yml
- group: design
  href: https://artifacts.apis.io/scrapingant/data-model/scrapingant-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scrapingant-data-model.yml
- group: agent
  href: https://artifacts.apis.io/scrapingant/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/scrapingant/plans/scrapingant-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scrapingant-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/scrapingant/rate-limits/scrapingant-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/scrapingant-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/scrapingant/finops/scrapingant-finops.yml
  title: ''
  type: FinOps
  url: finops/scrapingant-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.scrapingant.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.scrapingant.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.scrapingant.com/api-basics
- group: commercial
  title: ''
  type: Pricing
  url: https://scrapingant.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.scrapingant.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.scrapingant.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scrapingant.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scrapingant.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://scrapingant.com/#contact
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ScrapingAnt
created: '2026-03-29'
description: ScrapingAnt is a web-data infrastructure platform operated by DATAANT that puts headless Chrome rendering, a rotating pool of 3M+ residential and datacenter proxies, CAPTCHA avoidance and AI-powered extraction behind a single HTTP API. One request returns a fully JavaScript-rendered page as raw HTML, as LLM-ready Markdown, as an extended JSON envelope carrying cookies, headers, XHRs and iframes, or as structured JSON described in plain English. A hosted, remote MCP server exposes three of those formats as native tools to Claude, Cursor, Windsurf, Cline and VS Code, so an AI agent gets live web access without running a browser locally. Billing is metered in API credits with a permanently free 10,000-credit monthly tier; standalone rotating proxies are sold separately by bandwidth.
finops:
- has_sources: true
  method: derived
  name: Scrapingant Finops
  primary_unit: credits
  service_category: ''
  slug: scrapingant-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scrapingant.png
layout: provider
mcp_servers:
- description: ScrapingAnt operates a first-party hosted MCP server that gives an AI agent live web access through the same headless-Chrome cluster and rotating proxy pool that backs the /v2/general REST endpoint. T
  name: ScrapingAnt MCP Server
  slug: scrapingant-mcp-server
modified: '2026-08-29'
name: ScrapingAnt
nav: Providers
network: true
overview: 'ScrapingAnt publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Scraping API, Usage API, General API, and 2 more. Tagged areas include Data Extraction, Proxies, Web Scraping, Browser Automation, and AI Agents.


  The ScrapingAnt catalog on APIs.io includes 1 Spectral governance ruleset.


  ScrapingAnt''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Scrapingant Plans Pricing
  plan_count: 6
  slug: scrapingant-plans-pricing
- name: Scrapingant Price Estimates
  plan_count: 0
  slug: scrapingant-price-estimates
random_paper: 2
rate_limits:
- limit_count: 7
  name: Scrapingant Rate Limits
  slug: scrapingant-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: ScrapingAnt API Rules
  rule_count: 51
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 3
  slug: scrapingant-rules
score:
  band: developing
  composite: 53.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 72.4
    contract_governance: 18.2
    contract_quality: 50.5
    developer_ergonomics: 63.7
    discoverability: 68.3
    operational_transparency: 34.2
  previous_composite: 52.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 66.7
      total: 3
    mcp: first-party
    skills: derived
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/scrapingant/scrapingant-2026-06-20T193558.png
security:
- kind: authentication
  name: Scrapingant Authentication
  slug: scrapingant-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Scrapingant Domain Security
  slug: scrapingant-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: scrapingant-page-to-markdown-for-llm
  slug: scrapingant-page-to-markdown-for-llm
- name: scrapingant-scrape-a-page
  slug: scrapingant-scrape-a-page
- name: scrapingant-track-credit-budget
  slug: scrapingant-track-credit-budget
slug: scrapingant
tags:
- Data Extraction
- Proxies
- Web Scraping
- Browser Automation
- AI Agents
- MCP
- LLM
- Data Collection
- Web Data
website: https://scrapingant.com/
---
