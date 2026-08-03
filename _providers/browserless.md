---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Browserless Agentic Access
  operation_count: 76
  slug: browserless-agentic-access
  summary_line: 76 operations · 43 acting
api_count: 3
apis:
- description: The Browser REST APIs API from Browserless — 41 operation(s) for browser rest apis.
  name: Browserless Browser REST APIs API
  slug: browserless-browser-rest-apis-api
- description: The Browser WebSocket APIs API from Browserless — 23 operation(s) for browser websocket apis.
  name: Browserless Browser WebSocket APIs API
  slug: browserless-browser-websocket-apis-api
- description: The Management REST APIs API from Browserless — 13 operation(s) for management rest apis.
  name: Browserless Management REST APIs API
  slug: browserless-management-rest-apis-api
arazzos:
- description: Render a URL's HTML, then feed that exact HTML into the PDF engine to produce a self-contained PDF.
  name: Browserless Content To PDF
  slug: browserless-content-to-pdf-workflow
- description: Unblock a protected URL, then branch into structured scraping or a content+PDF archive depending on whether unblocked HTML was returned.
  name: Browserless Full Page Archive
  slug: browserless-full-page-archive-workflow
- description: Use the function API to drive a page that triggers a file download, then retrieve the downloaded artifacts via the download API.
  name: Browserless Function Then Download
  slug: browserless-function-download-workflow
- description: Run custom JavaScript against a page via the function API, then capture a screenshot to confirm the resulting state.
  name: Browserless Function Then Screenshot
  slug: browserless-function-then-screenshot-workflow
- description: Run a Lighthouse-style performance audit on a URL, then capture a screenshot of the audited page.
  name: Browserless Performance Audit
  slug: browserless-performance-audit-workflow
- description: Extract structured elements from a page, then capture a screenshot of the same page as visual evidence.
  name: Browserless Scrape Then Screenshot
  slug: browserless-scrape-then-screenshot-workflow
- description: Render a single URL three ways — HTML content, PNG screenshot, and PDF — in one pass.
  name: Browserless Site Capture Bundle
  slug: browserless-site-capture-bundle-workflow
- description: Bypass bot detection on a protected URL, then re-render its HTML content and a PDF using the unblocked content.
  name: Browserless Unblock Then Render
  slug: browserless-unblock-then-render-workflow
artifact_total: 33
collections:
- collection_type: postman
  name: Browserless
  slug: postman-browserless
- collection_type: open
  name: Browserless
  slug: open-browserless
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/browserless-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/browserless-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/browserless-domain-security.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/browserless/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/browserless-content-to-pdf-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/browserless-full-page-archive-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/browserless-function-download-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/browserless-function-then-screenshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/browserless-performance-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/browserless-scrape-then-screenshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/browserless-site-capture-bundle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/browserless-unblock-then-render-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.browserless.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.browserless.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.browserless.io/open-api
- group: company
  title: ''
  type: Blog
  url: https://www.browserless.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/browserless
- group: commercial
  title: ''
  type: Pricing
  url: https://www.browserless.io/pricing
- group: other
  title: ''
  type: Enterprise
  url: https://www.browserless.io/enterprise
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.browserless.io/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.browserless.io
- group: start
  title: ''
  type: Signup
  url: https://account.browserless.io/signup
- group: start
  title: ''
  type: Login
  url: https://account.browserless.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.browserless.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.browserless.io/privacy
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.browserless.io/llms.txt
created: '2026-05-25'
description: Browserless is a cloud browser-automation platform that runs managed Chromium, Chrome, Edge, Firefox, and WebKit browsers for Puppeteer, Playwright, and Selenium clients, plus a GraphQL-based stealth automation layer (BrowserQL) and a family of REST APIs for screenshots, PDFs, content scraping, function execution, performance audits, smart scraping, search, mapping, and full-site crawling. A built-in MCP server exposes browser tooling to Claude, Cursor, VS Code, and other agentic clients. The company also maintains a popular open-source Docker image of the same name (13k+ GitHub stars), residential proxies, CAPTCHA solving, session profiles, recordings, and hybrid live-URL workflows. Target customers are AI startups, agent developers, web scrapers, RPA teams, QA / monitoring teams, and enterprises running production browser automation at scale, with free, prototyping, starter, scale, and enterprise plans (including self-hosted licensing).
examples:
- key_count: 2
  name: Browserless Browserql Example
  slug: browserless-browserql-example
- key_count: 2
  name: Browserless Pdf Example
  slug: browserless-pdf-example
- key_count: 2
  name: Browserless Scrape Example
  slug: browserless-scrape-example
- key_count: 2
  name: Browserless Screenshot Example
  slug: browserless-screenshot-example
- key_count: 2
  name: Browserless Session Example
  slug: browserless-session-example
finops:
- name: Browserless Finops
  service_category: API
  slug: browserless-finops
graphqls:
- description: ''
  name: Browserless GraphQL API
  slug: browserless-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/browserless.png
json_schemas:
- name: Browserless Profile
  property_count: 0
  slug: browserless-profile
- name: Browserless Screenshot Request
  property_count: 10
  slug: browserless-screenshot
- name: Browserless Session
  property_count: 0
  slug: browserless-session
json_structures:
- name: Browserless Profile Structure
  property_count: 8
  slug: browserless-profile-structure
- name: Browserless Session Structure
  property_count: 11
  slug: browserless-session-structure
jsonld:
- class_count: 0
  name: Browserless Context
  property_count: 4
  slug: browserless-context
layout: provider
modified: '2026-05-25'
name: Browserless
nav: Providers
network: true
overview: 'Browserless publishes 3 APIs on the [APIs.io](https://apis.io/) network: Browser REST APIs API, Browser WebSocket APIs API, and Management REST APIs API. Tagged areas include Headless Browser, Browser Infrastructure, Web Automation, AI Agents, and Web Scraping.


  The Browserless catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Browserless'' developer surface includes documentation, API reference, engineering blog, pricing, changelog, signup flow, and 20 more developer resources.'
plans:
- name: Browserless Plans Pricing
  plan_count: 5
  slug: browserless-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 10
  name: Browserless Rate Limits
  slug: browserless-rate-limits
rules:
- name: Browserless API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: browserless-jsonschema-spectral-rules
- name: Browserless API Rules
  rule_count: 10
  severity_counts:
    error: 0
    hint: 0
    info: 4
    warn: 6
  slug: browserless-rules
score:
  band: strong
  composite: 58.7
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 50.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 58.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/browserless/refs/heads/main/screenshots/browserless-2026-06-20T173726.png
security:
- kind: domain-security
  name: Browserless Domain Security
  slug: browserless-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Browserless Trust Center
  slug: browserless-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: browserless
tags:
- Headless Browser
- Browser Infrastructure
- Web Automation
- AI Agents
- Web Scraping
- BrowserQL
- Puppeteer
- Playwright
- Selenium
- CDP
- Stealth
- CAPTCHA Solving
- Residential Proxy
- PDF Generation
- Screenshots
- Smart Scrape
- Crawl
- Search
- MCP
- Session Recording
- Hybrid Automation
website: https://www.browserless.io
---
