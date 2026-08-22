---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Zenrows Agentic Access
  operation_count: 2
  slug: zenrows-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 6
apis:
- description: Cloud headless browser exposed over WebSocket at wss://browser.zenrows.com?apikey=KEY, compatible with Playwright, Puppeteer, and the underlying Chrome DevTools Protocol. Each session runs on the ZenR
  name: ZenRows Scraping Browser
  slug: scraping-browser
- description: 'HTTP and SOCKS5 residential proxy network with 55M+ IPs across 190+ countries, username/password authentication, country and world-region targeting (e.g. country-es for Spain), and sticky-session TTL '
  name: ZenRows Residential Proxies
  slug: residential-proxies
- description: Vertical, structured-data scraper endpoints for major commerce and real-estate sites, sharing the api.zenrows.com authentication and credit model. Covers Amazon (ASIN lookup, discovery), Google (searc
  name: ZenRows Scraper APIs
  slug: scraper-apis
- description: Official ZenRows Model Context Protocol server that exposes the scraping platform to AI assistants. Available as a remote hosted server at https://mcp.zenrows.com/mcp with OAuth bearer authentication,
  name: ZenRows MCP Server
  slug: mcp
- description: First-party SDKs that wrap the Universal Scraper API and Residential Proxies with automatic retries, exponential backoff, concurrency helpers, and ergonomic clients. Official SDKs ship for Python (pip
  name: ZenRows SDKs
  slug: sdks
- description: Scrape any URL with anti-bot bypass and optional rendering.
  name: ZenRows Universal Scraper API
  slug: zenrows-universal-scraper-api
artifact_total: 22
collections:
- collection_type: postman
  name: ZenRows Universal Scraper API
  slug: postman-zenrows-universal-scraper-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ZenRows Universal Scraper API
  slug: open-zenrows-universal-scraper-api
- collection_type: open
  name: ZenRows Universal Scraper API
  slug: open-zenrows-universal-scraper
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/ZenRows/zenrows-mcp/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zenrows/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zenrows-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenrows-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zenrows-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.zenrows.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zenrows.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ZenRows
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zenrows.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.zenrows.com/register
- group: start
  title: ''
  type: Login
  url: https://app.zenrows.com/
- group: company
  title: ''
  type: Blog
  url: https://www.zenrows.com/blog
- group: other
  title: ''
  type: KnowledgeBase
  url: https://www.zenrows.com/knowledgehub
- group: operate
  title: ''
  type: Status
  url: https://status.zenrows.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://eu.intercom.news/zenrows
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.zenrows.com/api-error-codes
- group: commercial
  title: ''
  type: Legal
  url: https://www.zenrows.com/legal
- group: other
  title: ''
  type: ForbiddenSites
  url: https://docs.zenrows.com/forbidden-sites
- group: learn
  title: ''
  type: Academy
  url: https://docs.zenrows.com/zenrows-academy/introduction
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.zenrows.com/llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zenrows
- group: company
  title: ''
  type: XTwitter
  url: https://twitter.com/ZenRows
- group: commercial
  title: ''
  type: PlansAndPricing
  url: https://raw.githubusercontent.com/api-evangelist/zenrows/refs/heads/main/plans/zenrows-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/zenrows/refs/heads/main/rate-limits/zenrows-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/zenrows/refs/heads/main/finops/zenrows-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/zenrows/refs/heads/main/vocabulary/zenrows-vocabulary.yml
created: '2026-05-25'
description: 'ZenRows is a Spanish web scraping platform headquartered in Madrid that lets developers collect public web data at scale without managing proxies, browsers, or CAPTCHAs. A single API key unlocks four products against a shared 55M+ residential IP pool across 190+ countries: the Universal Scraper API (HTTP scrape with JS rendering, anti-bot bypass, screenshots, CSS/AI extraction, and PDF/markdown output), the Scraping Browser (cloud Playwright/Puppeteer/CDP browser over WebSocket), Residential Proxies (HTTP/SOCKS5 with sticky sessions and country targeting), and a set of vertical Scraper APIs for Amazon, Google, Walmart, Zillow, and Idealista. ZenRows also ships first-party Python, Node.js, and Go SDKs, a Scrapy middleware, deep integrations across Playwright, Puppeteer, Selenium, Scrapy, LangChain, LlamaIndex, OpenAI Agents SDK, Zapier, n8n, Make, Pipedream, Node-RED, MuleSoft, Clay, and an official MCP server (hosted at https://mcp.zenrows.com/mcp and as @zenrows/mcp on npm)
  exposing scrape and 30+ browser automation tools to AI agents.'
examples:
- key_count: 2
  name: Zenrows Scrape Url Example
  slug: zenrows-scrape-url-example
finops:
- name: Zenrows Finops
  service_category: Web Scraping / Data Extraction
  slug: zenrows-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zenrows.png
json_schemas:
- name: ZenRows Universal Scraper API Response
  property_count: 12
  slug: zenrows-scrape-response
json_structures:
- name: Zenrows Scrape Request Structure
  property_count: 24
  slug: zenrows-scrape-request-structure
jsonld:
- class_count: 0
  name: Zenrows Context
  property_count: 19
  slug: zenrows-context
layout: provider
modified: '2026-05-25'
name: ZenRows
nav: Providers
network: true
overview: 'ZenRows publishes 1 API on the [APIs.io](https://apis.io/) network: Universal Scraper API. Tagged areas include Web Scraping, Data Extraction, Anti-Bot, Proxies, and Residential Proxies.


  The ZenRows catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  ZenRows'' developer surface includes authentication, documentation, pricing, signup flow, engineering blog, status page, changelog, and 19 more developer resources.'
plans:
- name: Zenrows Plans Pricing
  plan_count: 8
  slug: zenrows-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 12
  name: Zenrows Rate Limits
  slug: zenrows-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: ZenRows API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: zenrows-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: ZenRows API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: zenrows-rules
score:
  band: developing
  composite: 50.3
  delta: -7.2
  facets:
    access_clarity: 56.6
    commercial_clarity: 56.6
    contract_governance: 25.0
    contract_quality: 65.0
    developer_ergonomics: 28.6
    discoverability: 72.2
    governance: 25.0
    operational_transparency: 52.6
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/zenrows/refs/heads/main/screenshots/zenrows-2026-06-20T201820.png
security:
- kind: authentication
  name: Zenrows Authentication
  slug: zenrows-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Zenrows Domain Security
  slug: zenrows-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: zenrows
tags:
- Web Scraping
- Data Extraction
- Anti-Bot
- Proxies
- Residential Proxies
- Browser Automation
- Screenshots
- CAPTCHA
- AI
- MCP
- Spain
website: https://www.zenrows.com/
---
