---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Scrapfly Agentic Access
  operation_count: 3
  slug: scrapfly-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 7
apis:
- description: 'Capture screenshots of web pages with full-page or element-specific capture using CSS selectors. Supports JavaScript rendering, viewport configuration, and screenshot of dynamic content. The base URL '
  name: Scrapfly Screenshot API
  slug: screenshot-api
- description: AI-powered structured data extraction from HTML content. Supports template-based extraction, LLM prompt-driven extraction, and auto-extraction using predefined models for common content types.
  name: Scrapfly Extraction API
  slug: extraction-api
- description: Web crawling API (currently in early access) that enables crawling entire websites with advanced configuration for depth control and content filtering. Outputs in WARC format for comprehensive web arc
  name: Scrapfly Crawler API
  slug: crawler-api
- description: Headless browser automation API (currently in beta) compatible with Playwright, Puppeteer, and Selenium frameworks. Enables complex browser interactions, JavaScript execution, and file download captur
  name: Scrapfly Cloud Browser API
  slug: cloud-browser-api
- description: Official SDKs for Python, TypeScript, Go, Rust, and Scrapy with full feature coverage across every language including scrape, screenshot, extract, and crawl capabilities.
  name: Scrapfly SDKs
  slug: sdks
- description: The Scraping API from Scrapfly — 1 operation(s) for scraping.
  name: Scrapfly Scraping API
  slug: scrapfly-scraping-api
- description: The Screenshots API from Scrapfly — 1 operation(s) for screenshots.
  name: Scrapfly Screenshots API
  slug: scrapfly-screenshots-api
artifact_total: 24
collections:
- collection_type: open
  name: Scrapfly Scrape API
  slug: open-scrapfly-scrape
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/scrapfly-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scrapfly-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/scrapfly-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scrapfly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scrapfly-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scrapfly
- group: agent
  title: ''
  type: LlmsText
  url: https://scrapfly.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://scrapfly.io/blog/rss/
created: '2025-02-08'
description: 'Scrapfly is a web scraping API platform that enables effortless collection of web data with battle-tested APIs that scale. It provides capabilities for scraping web pages, capturing screenshots, and extracting structured data with AI assistance to handle anti-bot measures and JavaScript rendering. One API key unlocks five APIs: Web Scraping (anti-bot unblocker), Cloud Browser (CDP), Screenshot, Extraction, and Crawler. Scrapfly operates globally with proxies across 190+ countries.'
examples:
- key_count: 2
  name: Scrapfly Scrape Url Example
  slug: scrapfly-scrape-url-example
finops:
- name: Scrapfly Finops
  service_category: Web Scraping / Data Extraction
  slug: scrapfly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: Scrapfly Scrape Response
  property_count: 2
  slug: scrapfly-scrape-response
- name: ScrapeRequest
  property_count: 19
  slug: scrapfly-scraperequest
- name: ScrapeResponse
  property_count: 2
  slug: scrapfly-scraperesponse
json_structures:
- name: Scrapfly Scrape Request Structure
  property_count: 0
  slug: scrapfly-scrape-request-structure
- name: Scrapfly Structure
  property_count: 0
  slug: scrapfly-structure
jsonld:
- class_count: 0
  name: Scrapfly Context
  property_count: 15
  slug: scrapfly-context
layout: provider
modified: '2026-05-19'
name: Scrapfly
nav: Providers
network: true
overview: 'Scrapfly publishes 2 APIs on the [APIs.io](https://apis.io/) network: Scraping API and Screenshots API. Tagged areas include AI, Data Extraction, Screenshots, Web Scraping, and Proxies.


  The Scrapfly catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Scrapfly''s developer surface includes authentication, engineering blog, and 6 more developer resources.'
plans:
- name: Scrapfly Plans Pricing
  plan_count: 6
  slug: scrapfly-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 7
  name: Scrapfly Rate Limits
  slug: scrapfly-rate-limits
rules:
- name: Scrapfly API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: scrapfly-jsonschema-spectral-rules
- name: Scrapfly API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: scrapfly-rules
score:
  band: developing
  composite: 47.7
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 72.1
    developer_ergonomics: 13.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scrapfly/refs/heads/main/screenshots/scrapfly-2026-06-20T193556.png
security:
- kind: authentication
  name: Scrapfly Authentication
  slug: scrapfly-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Scrapfly Domain Security
  slug: scrapfly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Scrapfly Trust Center
  slug: scrapfly-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: scrapfly
tags:
- AI
- Data Extraction
- Screenshots
- Web Scraping
- Proxies
- Browser Automation
---
