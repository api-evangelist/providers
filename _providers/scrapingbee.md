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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Scrapingbee Agentic Access
  operation_count: 3
  slug: scrapingbee-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 6
apis:
- description: The Google Search API returns structured JSON SERP data covering organic results, knowledge graph, featured snippets, related searches, news, maps, image results, and ads. Supports search_type (web, n
  name: ScrapingBee Google Search API
  slug: google-search-api
- description: The Data Extraction API layers structured-data extraction rules on top of HTML API calls so callers receive parsed JSON instead of raw HTML. Supports CSS selectors, XPath expressions, nested objects a
  name: ScrapingBee Data Extraction API
  slug: data-extraction-api
- description: The AI Web Scraping API leverages LLM-driven extraction to lift content from web pages by expressing what you need in plain English via the ai_query parameter, with no CSS selectors, XPath, or parsing
  name: ScrapingBee AI Web Scraping API
  slug: ai-extraction-api
- description: The Screenshot API captures full-page or viewport screenshots of any URL using headless Chrome, with control over viewport size, full_page rendering, image format, and combination with JavaScript scen
  name: ScrapingBee Screenshot API
  slug: screenshot-api
- description: Structured Google SERP results (web, news, maps, images).
  name: ScrapingBee Google Search API API
  slug: scrapingbee-google-search-api-api
- description: Headless-browser scraping with proxy rotation, screenshots, and AI extraction.
  name: ScrapingBee HTML API API
  slug: scrapingbee-html-api-api
artifact_total: 16
collections:
- collection_type: postman
  name: ScrapingBee Google Search API API
  slug: postman-scrapingbee-google-search-api-api
- collection_type: postman
  name: ScrapingBee Google Search API HTML API API
  slug: postman-scrapingbee-html-api-api
- collection_type: open
  name: ScrapingBee API
  slug: open-scrapingbee
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/scrapingbee/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scrapingbee-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scrapingbee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scrapingbee-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.scrapingbee.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.scrapingbee.com/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.scrapingbee.com/documentation/#quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://www.scrapingbee.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.scrapingbee.com/blog/
- group: start
  title: ''
  type: Signup
  url: https://app.scrapingbee.com/account/register
- group: start
  title: ''
  type: Login
  url: https://app.scrapingbee.com/account/login
- group: operate
  title: ''
  type: Support
  url: https://help.scrapingbee.com
- group: operate
  title: ''
  type: Status
  url: https://status.scrapingbee.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.scrapingbee.com/changelog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.scrapingbee.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scrapingbee.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ScrapingBee
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scrapingbee
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/ScrapingBee/scrapingbee-python
- group: build
  title: ''
  type: NodeSDK
  url: https://github.com/ScrapingBee/scrapingbee-node
- group: build
  title: ''
  type: CLI
  url: https://github.com/ScrapingBee/scrapingbee-cli
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/api-evangelist/scraping/documentation/ygpc6xm/scrapingbee
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/ScrapingBee/mcp-server
- group: commercial
  title: ''
  type: Plans
  url: plans/scrapingbee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scrapingbee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/scrapingbee-finops.yml
created: '2026-03-26'
description: ScrapingBee is a France-based web scraping API that handles headless browsers, proxy rotation, anti-bot defenses, and CAPTCHA solving so developers can extract data from any website with a single API call. The platform exposes a unified HTML scraping endpoint alongside dedicated APIs for Google Search, Amazon, Walmart, YouTube, and ChatGPT, with JavaScript rendering, AI-powered data extraction, screenshots, and an MCP server for agentic workflows.
finops:
- name: Scrapingbee Finops
  service_category: API
  slug: scrapingbee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scrapingbee.png
layout: provider
mcp_servers:
- description: ''
  name: mcp-server
  slug: mcp-server
modified: '2026-05-25'
name: ScrapingBee
nav: Providers
network: true
overview: 'ScrapingBee publishes 2 APIs on the [APIs.io](https://apis.io/) network: Google Search API API and HTML API API. Tagged areas include AI Extraction, Anti-Bot, Data Aggregation, Data Extraction, and Headless Browser.


  ScrapingBee''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, signup flow, support, and 19 more developer resources.'
plans:
- name: Scrapingbee Plans Pricing
  plan_count: 3
  slug: scrapingbee-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Scrapingbee Rate Limits
  slug: scrapingbee-rate-limits
score:
  band: strong
  composite: 57.9
  delta: -2.1
  facets:
    commercial_clarity: 84.2
    contract_quality: 61.9
    developer_ergonomics: 56.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 60.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scrapingbee/refs/heads/main/screenshots/scrapingbee-2026-06-20T193558.png
security:
- kind: authentication
  name: Scrapingbee Authentication
  slug: scrapingbee-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Scrapingbee Domain Security
  slug: scrapingbee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scrapingbee
tags:
- AI Extraction
- Anti-Bot
- Data Aggregation
- Data Extraction
- Headless Browser
- JavaScript Rendering
- Proxy Rotation
- Screenshots
- Search Engine
- Web Scraping
website: https://www.scrapingbee.com
---
