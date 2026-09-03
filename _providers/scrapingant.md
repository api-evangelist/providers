---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.5
  scored_at: '2026-09-02'
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
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ScrapingAnt Scraping API
  slug: open-scrapingant-scraping-api
- collection_type: open
  name: ScrapingAnt
  slug: open-scrapingant
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scrapingant-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scrapingant-domain-security.yml
- group: auth
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
  title: ''
  type: Packages
  url: packages/scrapingant-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/scrapingant-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/scrapingant-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/scrapingant-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scrapingant-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/scrapingant-scraping-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/scrapingant-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/scrapingant-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/scrapingant-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/scrapingant-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/scrapingant-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/scrapingant-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scrapingant-rate-limits.yml
- group: commercial
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
- name: Scrapingant Finops
  service_category: API
  slug: scrapingant-finops
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
overview: 'ScrapingAnt publishes 2 APIs on the [APIs.io](https://apis.io/) network: Scraping API and Usage API. Tagged areas include Data Extraction, Proxies, Scraping, Web Scraping, and Headless Browsers.


  ScrapingAnt''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Scrapingant Plans Pricing
  plan_count: 6
  slug: scrapingant-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 7
  name: Scrapingant Rate Limits
  slug: scrapingant-rate-limits
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 21
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.8
  facets:
    access_clarity: 72.4
    commercial_clarity: 72.4
    contract_governance: 4.5
    contract_quality: 57.1
    developer_ergonomics: 63.7
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scrapingant/refs/heads/main/screenshots/scrapingant-2026-06-20T193558.png
security:
- kind: authentication
  name: Scrapingant Authentication
  slug: scrapingant-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Scrapingant Domain Security
  slug: scrapingant-domain-security
  summary_line: TLSv1.3 · DMARC
slug: scrapingant
tags:
- Data Extraction
- Proxies
- Scraping
- Web Scraping
- Headless Browsers
- AI Agents
- MCP
- LLM
- Data Collection
- Web Data
website: https://scrapingant.com/
---
