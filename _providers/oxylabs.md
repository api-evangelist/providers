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
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Oxylabs Agentic Access
  operation_count: 11
  slug: oxylabs-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 15
apis:
- description: Search-engine results page scraping for Google (Search, Ads, Images, Lens, Maps, Suggest, Shopping, Travel, Trends, AI Overviews, AI Mode), Bing (Search, Hotels), Baidu, Yandex, DuckDuckGo, Naver, and
  name: Oxylabs SERP Scraper API
  slug: oxylabs-serp-scraper-api
- description: Pre-built scraping targets for major e-commerce platforms — Amazon (search, product, reviews, questions, best sellers, offer listing, ASIN), Walmart, eBay, Etsy, Target, Best Buy, Wayfair, Kroger, Mac
  name: Oxylabs E-Commerce Scraper API
  slug: oxylabs-ecommerce-scraper-api
- description: AI-driven proxy solution exposed as a single HTTPS endpoint (unblock.oxylabs.io:60000) that handles proxy rotation, browser fingerprinting, JavaScript rendering, CAPTCHA solving, and bot-mitigation by
  name: Oxylabs Web Unblocker
  slug: oxylabs-web-unblocker
- description: Cloud-hosted headless browser service exposed via Chrome DevTools Protocol (CDP) and Selenium / Playwright / Puppeteer. Each remote browser session is geo-targetable, includes premium proxy egress, an
  name: Oxylabs Headless Browser
  slug: oxylabs-headless-browser
- description: 'Rotating residential IP pool (195M+ IPs across 195 countries) for accessing geo-fenced and consumer-protected web content. HTTP/HTTPS/SOCKS5 endpoints with country, city, ASN, state, coordinates, and '
  name: Oxylabs Residential Proxies
  slug: oxylabs-residential-proxies
- description: High-speed shared, dedicated, and self-service datacenter IP proxies for fast public data gathering. Includes a free trial pool of datacenter IPs. Authentication via username/password or IP whitelisti
  name: Oxylabs Datacenter Proxies
  slug: oxylabs-datacenter-proxies
- description: 5G / 4G / 3G / LTE rotating mobile IP proxies sourced from real mobile carriers. Country, city, coordinates, and ASN/carrier targeting. Designed for use cases that require high-trust mobile-network eg
  name: Oxylabs Mobile Proxies
  slug: oxylabs-mobile-proxies
- description: Static residential (ISP) proxies that combine the legitimacy of residential IPs with the speed and stability of datacenter infrastructure. Dedicated and shared options across major geographies, with b
  name: Oxylabs ISP Proxies
  slug: oxylabs-isp-proxies
- description: Suite of AI-native data acquisition primitives — AI Scraper (turn any URL into structured JSON or markdown from a natural-language schema), AI Crawler (URL-seed crawl + extract), AI Map (LLM-driven si
  name: Oxylabs AI Studio
  slug: oxylabs-ai-studio
- description: Official Model Context Protocol server that exposes Oxylabs Web Scraper API, AI Studio, and proxy capabilities as MCP tools to Claude Code, Claude Desktop, Cursor, and any MCP-compatible AI client. In
  name: Oxylabs MCP Server
  slug: oxylabs-mcp-server
- description: Pre-collected, ready-to-deliver web datasets for e-commerce (Amazon, Google Shopping, Best Buy, Walmart, eBay), job postings (Indeed, Glassdoor, LinkedIn), product reviews, company intelligence, commu
  name: Oxylabs Datasets
  slug: oxylabs-datasets
- description: The Login API from Oxylabs — 1 operation(s) for login.
  name: Oxylabs Login API
  slug: oxylabs-login-api
- description: The Queries API from Oxylabs — 1 operation(s) for queries.
  name: Oxylabs Queries API
  slug: oxylabs-queries-api
- description: The Stats API from Oxylabs — 2 operation(s) for stats.
  name: Oxylabs Stats API
  slug: oxylabs-stats-api
- description: The Users API from Oxylabs — 4 operation(s) for users.
  name: Oxylabs Users API
  slug: oxylabs-users-api
arazzos:
- description: Assemble a dashboard view from available filters, usage statistics, and client statistics.
  name: Oxylabs Account Statistics Dashboard
  slug: oxylabs-account-statistics-dashboard-workflow
- description: Read a sub-user record then delete it from the residential account.
  name: Oxylabs Offboard Sub-user
  slug: oxylabs-offboard-sub-user-workflow
- description: Authenticate, create a residential proxy sub-user, and read back its record.
  name: Oxylabs Provision Sub-user
  slug: oxylabs-provision-sub-user-workflow
- description: Submit an asynchronous Web Scraper API job and branch on the returned job status.
  name: Oxylabs Push-Pull Scrape and Confirm Job
  slug: oxylabs-push-pull-scrape-and-confirm-job-workflow
- description: Run a synchronous Web Scraper API job and confirm the scrape against account usage statistics.
  name: Oxylabs Realtime Scrape and Verify Usage
  slug: oxylabs-realtime-scrape-and-verify-usage-workflow
- description: Exchange basic auth for a bearer token and list the residential proxy sub-users.
  name: Oxylabs Residential Login and List Sub-users
  slug: oxylabs-residential-login-and-list-sub-users-workflow
- description: Run a parsed search scrape, then scrape a discovered result URL with a second realtime job.
  name: Oxylabs Search Then Scrape Result
  slug: oxylabs-search-then-scrape-result-workflow
- description: Log in, list sub-users, and pull per-sub-user target statistics for an audit.
  name: Oxylabs Sub-user Usage Audit
  slug: oxylabs-sub-user-usage-audit-workflow
- description: Find a sub-user by name and patch its traffic limit and status.
  name: Oxylabs Throttle Sub-user Traffic
  slug: oxylabs-throttle-sub-user-traffic-workflow
artifact_total: 66
collections:
- collection_type: postman
  name: Oxylabs Web Intelligence APIs
  slug: postman-oxylabs
- collection_type: open
  name: Oxylabs Web Intelligence APIs
  slug: open-oxylabs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oxylabs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/oxylabs-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oxylabs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oxylabs-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/oxylabs/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oxylabs-account-statistics-dashboard-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oxylabs-offboard-sub-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oxylabs-provision-sub-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oxylabs-push-pull-scrape-and-confirm-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oxylabs-realtime-scrape-and-verify-usage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oxylabs-residential-login-and-list-sub-users-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oxylabs-search-then-scrape-result-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oxylabs-sub-user-usage-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oxylabs-throttle-sub-user-traffic-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://oxylabs.io/
- group: company
  title: ''
  type: Website
  url: https://oxylabs.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.oxylabs.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.oxylabs.io/api-targets
- group: docs
  title: ''
  type: Documentation
  url: https://oxylabs.io/products
- group: docs
  title: ''
  type: Documentation
  url: https://oxylabs.io/integrations
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.oxylabs.io/get-started/quick-start-proxies
- group: start
  title: ''
  type: Signup
  url: https://dashboard.oxylabs.io/en/registration
- group: other
  title: ''
  type: Dashboard
  url: https://dashboard.oxylabs.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://uptime.oxylabs.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.oxylabs.io/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: https://oxylabs.io/developers/release-notes
- group: other
  title: ''
  type: RSS
  url: https://developers.oxylabs.io/rss.xml
- group: agent
  title: ''
  type: LlmsText
  url: https://oxylabs.io/llms.txt
- group: operate
  title: ''
  type: HelpCenter
  url: https://developers.oxylabs.io/help-center
- group: operate
  title: ''
  type: Support
  url: https://oxylabs.io/contact-us
- group: operate
  title: ''
  type: Support
  url: https://developers.oxylabs.io/have-a-question
- group: commercial
  title: ''
  type: Pricing
  url: https://oxylabs.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://oxylabs.io/blog
- group: learn
  title: ''
  type: Training
  url: https://experts.oxylabs.io/lessons
- group: learn
  title: ''
  type: Training
  url: https://oxylabs.io/resources
- group: company
  title: ''
  type: Careers
  url: https://career.oxylabs.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oxylabs.io/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oxylabs.io/legal/terms-of-service
- group: auth
  title: ''
  type: TrustCenter
  url: https://oxylabs.io/legal
- group: docs
  title: ''
  type: Documentation
  url: https://oxylabs.io/sustainability
- group: docs
  title: ''
  type: Documentation
  url: https://oxylabs.io/core-values
- group: company
  title: ''
  type: Press
  url: https://oxylabs.io/press-area
- group: company
  title: ''
  type: AboutUs
  url: https://oxylabs.io/about-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/oxylabs-io
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/oxylabs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oxylabs
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/oxylabs/oxylabs-readme
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/oxylabs/oxylabs-mcp
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/oxylabs/agent-skills
- group: build
  title: ''
  type: SDKs
  url: https://github.com/oxylabs/oxylabs-sdk-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/oxylabs/oxylabs-sdk-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/oxylabs/oxylabs-ai-studio-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/oxylabs/oxylabs-ai-studio-js
- group: build
  title: ''
  type: Plugin
  url: https://github.com/oxylabs/oxylabs-ai-studio-openclaw
- group: build
  title: ''
  type: SDKs
  url: https://github.com/oxylabs/browser-agent-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/oxylabs/ai-crawler-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/oxylabs/ai-map-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/oxylabs/AI-Search-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/oxylabs/ai-scraper-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/oxylabs/OxyMouse
- group: build
  title: ''
  type: SDKs
  url: https://github.com/oxylabs/OxyParser
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/oxylabs/web-unblocker
- group: build
  title: ''
  type: Tools
  url: https://github.com/oxylabs/Oxylabs-Web-Scraper-API-Scheduler
- group: build
  title: ''
  type: Tools
  url: https://github.com/oxylabs/proxy-chrome-extension
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/oxylabs/proxy-integrations
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/oxylabs/product-integrations
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/oxylabs/quick-start-guide
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/oxylabs/web-scraping-tutorials
- group: commercial
  title: ''
  type: Plans
  url: plans/oxylabs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/oxylabs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/oxylabs-finops.yml
created: '2026-03-29'
description: Oxylabs is a Lithuanian (Vilnius-based) web intelligence platform providing premium proxy networks (Residential, Datacenter, Mobile, ISP, Dedicated), web data acquisition APIs (Web Scraper API, SERP Scraper API, E-Commerce Scraper API, Real Estate Scraper API, Web Unblocker, Headless Browser), AI-native scraping tools (AI Studio — AI Scraper, AI Crawler, AI Map, Browser Agent, AI Search), an official MCP server, and ready-to-deliver datasets. The platform serves large-scale public web data extraction for e-commerce intelligence, brand protection, market research, SEO/SERP monitoring, cybersecurity, and AI/LLM training pipelines.
features:
- Web Scraper API with Realtime (sync) and Push-Pull (async) delivery modes
- SERP Scraper API for Google, Bing, Baidu, Yandex, Naver, DuckDuckGo (Search, Ads, Images, Lens, Maps, Suggest, Shopping, Travel, Trends, AI Overviews, AI Mode)
- E-Commerce Scraper API for Amazon, Walmart, eBay, Etsy, Target, Best Buy, AliExpress, 1688, Shein, Lazada, Trip, Trivago, MercadoLivre and more
- Real Estate Scraper API (Redfin, Zillow patterns)
- Web Unblocker — single endpoint that handles proxy rotation, fingerprinting, JS rendering, and CAPTCHA solving automatically
- Headless Browser cloud service with Chrome DevTools Protocol, Playwright, Puppeteer, Selenium support
- AI Studio — AI Scraper, AI Crawler, AI Map, Browser Agent, AI Search
- AI Web Scraper Copilot — code generator that produces Requests / Parsing / API integration code
- Residential Proxies (195M+ IPs across 195 countries) with country / city / ASN / state / coordinates / ZIP-code targeting and sticky sessions
- Dedicated and shared Datacenter Proxies, including free trial datacenter IPs
- Mobile Proxies (5G / 4G / 3G / LTE) with carrier and geo targeting
- ISP Proxies (static residential) — self-service and Dedicated ISP Enterprise tiers
- Datasets — pre-collected e-commerce, job-posting, product-review, company, and community-and-code feeds; custom dataset service on request
- Official Oxylabs MCP server for Claude, Cursor, and other MCP-compatible AI clients
- Official Agent Skills for Oxylabs products
- Sub-user management and statistics via Residential Public API
- Dashboard API for usage, billing, team management
- Geo-targeting at country, state, city, ZIP/postal-code, coordinates, and ASN levels
- Domain locale results-language and e-commerce-localization controls
- JavaScript rendering and custom browser instructions (beta)
- Custom parsing instructions and built-in parsers for major SERP and e-commerce targets
- HTTP context and job-management primitives, callback / webhook delivery for Push-Pull
- HTTP, HTTPS, and SOCKS5 protocols across proxy products
- SOC 2 Type II, ISO/IEC 27001, GDPR, and CCPA compliance
- Oxy Proxy Manager browser extension and proxy manager apps
- Free trial across Web Scraper API, Web Unblocker, Residential, Datacenter, and Mobile proxies
- Pay-as-you-go and committed-use pricing; usage measured by request and by GB of proxy traffic
finops:
- name: Oxylabs Finops
  service_category: API
  slug: oxylabs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oxylabs.png
layout: provider
mcp_servers:
- description: ''
  name: oxylabs-mcp
  slug: oxylabs-mcp
modified: '2026-05-25'
name: Oxylabs
nav: Providers
network: true
overview: 'Oxylabs publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Login API, Queries API, Stats API, and 1 more. Tagged areas include AI Web Scraping, Bot Mitigation Bypass, CAPTCHA Solving, Data Extraction, and Datacenter Proxies.


  Oxylabs'' developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, changelog, support, and 64 more developer resources.'
plans:
- name: Oxylabs Plans Pricing
  plan_count: 3
  slug: oxylabs-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Oxylabs Rate Limits
  slug: oxylabs-rate-limits
score:
  band: strong
  composite: 61.6
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 58.9
    developer_ergonomics: 73.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 61.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oxylabs/refs/heads/main/screenshots/oxylabs-2026-06-20T191301.png
security:
- kind: authentication
  name: Oxylabs Authentication
  slug: oxylabs-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Oxylabs Domain Security
  slug: oxylabs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Oxylabs Trust Center
  slug: oxylabs-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 5
skills:
- name: oxylabs-headless-browser
  slug: oxylabs-headless-browser
- name: oxylabs-proxies
  slug: oxylabs-proxies
- name: oxylabs-video-data
  slug: oxylabs-video-data
- name: oxylabs-web-scraper
  slug: oxylabs-web-scraper
- name: oxylabs-web-unblocker
  slug: oxylabs-web-unblocker
slug: oxylabs
tags:
- AI Web Scraping
- Bot Mitigation Bypass
- CAPTCHA Solving
- Data Extraction
- Datacenter Proxies
- Datasets
- E-Commerce Data
- Headless Browser
- ISP Proxies
- Mobile Proxies
- Proxies
- Residential Proxies
- SERP
- Scraper API
- Scraping
- Web Data
- Web Intelligence
- Web Unblocker
website: https://oxylabs.io/
---
