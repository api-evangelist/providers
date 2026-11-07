---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Browserless Agentic Access
  operation_count: 81
  slug: browserless-agentic-access
  summary_line: 81 operations · 46 acting
api_count: 2
apis:
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: The Browser REST APIs API from Browserless — 41 operation(s) for browser rest apis.
  name: Browserless Browser REST APIs API
  slug: browserless-browser-rest-apis-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: The Management REST APIs API from Browserless — 13 operation(s) for management rest apis.
  name: Browserless Management REST APIs API
  slug: browserless-management-rest-apis-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: Run autonomous browser agents. `POST /agent/run` starts an asynchronous run and returns an id to poll via `GET /agent/run/:id`; `POST /agent/run/:id/continue` sends it a follow-up task (not enabled in
  name: Browserless Agent API
  slug: browserless-agent-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: Run BrowserQL (BQL) queries over REST, or connect over WebSocket for a persistent BQL session. `/chromium/bql` runs standard BQL; `/stealth/bql` adds fingerprint randomization for bot-detection-sensit
  name: Browserless BQL Execution API
  slug: browserless-bql-execution-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: Inspect running sessions, terminate browsers, and retrieve server metadata. `/active` lists current sessions, `/kill/:id` terminates one, and `/meta` returns server configuration.
  name: Browserless Browser Management API
  slug: browserless-browser-management-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: 'Low-level WebSocket connections for CDP tooling: the hosted-agent CLI chat (`/chromium/cli`), reconnecting to an existing stealth session, attaching to an already-running Chromium process, and the und'
  name: Browserless CDP & DevTools Connections API
  slug: browserless-cdp-devtools-connections-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: The `/chrome/*` endpoints use the licensed Google Chrome binary, which includes proprietary codec and DRM support. Use these when a site requires Chrome-specific features, video codecs (Twitch, YouTub
  name: Browserless Chrome (licensed build) API
  slug: browserless-chrome-licensed-build-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: Launch, monitor, and cancel multi-page crawl jobs. `POST /crawl` starts a crawl, `GET /crawl/:id` polls for progress, and `DELETE /crawl/:id` cancels it.
  name: Browserless Crawling API
  slug: browserless-crawling-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: Run custom JavaScript in a browser context and retrieve the resulting files. Use `/function` to execute a Puppeteer or Playwright script server-side, and `/download` to capture binary assets triggered
  name: Browserless Functions & Downloads API
  slug: browserless-functions-downloads-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: Connect external services to browser sessions. Currently supports 1Password for injecting stored credentials into a session without exposing secrets in your code.
  name: Browserless Integrations API
  slug: browserless-integrations-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: 'Site-specific browser-automation skills: tuned recipes an agent should follow for a given domain instead of planning its own steps.'
  name: Browserless Platform / Skills API
  slug: browserless-platform-skills-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: Create and manage persistent browser profiles that preserve cookies, localStorage, and IndexedDB across sessions. Capture a logged-in state once with `Browserless.saveProfile`, then rehydrate it on an
  name: Browserless Profiles API
  slug: browserless-profiles-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: Discover available proxy locations and configure residential or datacenter routing for your sessions. > Residential proxies are only available on Enterprise and Cloud plans. Add these parameters to yo
  name: Browserless Proxy API
  slug: browserless-proxy-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: Load pages and extract HTML, text, or structured data. `/chromium/content` returns raw HTML. `/chromium/scrape` runs `querySelectorAll` against the rendered DOM and returns matched elements. `/smart-s
  name: Browserless Scraping & Content API
  slug: browserless-scraping-content-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: 'Capture full-page or element screenshots and generate PDFs from web pages. The root `/screenshot` and `/pdf` routes work for most cases. Use browser-specific variants like `/edge/screenshot` when you '
  name: Browserless Screenshots & PDFs API
  slug: browserless-screenshots-pdfs-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: 'Create persistent browser sessions, reconnect to running browsers, and query CDP metadata. `/session` spins up a session that outlives a single WebSocket connection. `/reconnect/:id` reattaches to it '
  name: Browserless Sessions & Connections API
  slug: browserless-sessions-connections-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: Bypass bot detection and anti-scraping measures. `/unblock` handles aggressive anti-bot challenges end-to-end. The stealth toggle (`/stealth`, `/chromium/stealth`, `/chrome/stealth`) randomizes browse
  name: Browserless Unblock & Stealth API
  slug: browserless-unblock-stealth-api
- baseURL: https://production-sfo.browserless.io
  baseurl_source: declared
  description: Connect Puppeteer, Playwright, or raw DevTools Protocol clients over WebSocket. Launch a browser with `wss://` and get back a CDP session for full programmatic control.
  name: Browserless WebSocket APIs API
  slug: browserless-websocket-apis-api
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
artifact_total: 52
collections:
- collection_type: postman
  name: Browserless
  slug: postman-browserless
- collection_type: open
  name: Browserless Browser REST APIs API
  slug: open-browserless-browser-rest-apis-api
- collection_type: open
  name: Browserless Browser REST APIs Browser WebSocket APIs API
  slug: open-browserless-browser-websocket-apis-api
- collection_type: open
  name: Browserless Browser REST APIs Management REST APIs API
  slug: open-browserless-management-rest-apis-api
- collection_type: open
  name: Browserless
  slug: open-browserless
common:
- group: other
  href: https://artifacts.apis.io/browserless/capabilities/browserless-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/browserless-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/browserless/plans/browserless-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/browserless-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/browserless/rate-limits/browserless-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/browserless-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/browserless/finops/browserless-finops.yml
  title: ''
  type: FinOps
  url: finops/browserless-finops.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/browserless/browserless/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/browserless/browserless/releases
- group: agent
  href: https://artifacts.apis.io/browserless/agentic-access/browserless-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/browserless-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/browserless/security/browserless-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/browserless-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/browserless/security/browserless-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/browserless-domain-security.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/browserless/overview
- group: design
  href: https://artifacts.apis.io/browserless/arazzo/browserless-content-to-pdf-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/browserless-content-to-pdf-workflow.yml
- group: design
  href: https://artifacts.apis.io/browserless/arazzo/browserless-full-page-archive-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/browserless-full-page-archive-workflow.yml
- group: design
  href: https://artifacts.apis.io/browserless/arazzo/browserless-function-download-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/browserless-function-download-workflow.yml
- group: design
  href: https://artifacts.apis.io/browserless/arazzo/browserless-function-then-screenshot-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/browserless-function-then-screenshot-workflow.yml
- group: design
  href: https://artifacts.apis.io/browserless/arazzo/browserless-performance-audit-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/browserless-performance-audit-workflow.yml
- group: design
  href: https://artifacts.apis.io/browserless/arazzo/browserless-scrape-then-screenshot-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/browserless-scrape-then-screenshot-workflow.yml
- group: design
  href: https://artifacts.apis.io/browserless/arazzo/browserless-site-capture-bundle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/browserless-site-capture-bundle-workflow.yml
- group: design
  href: https://artifacts.apis.io/browserless/arazzo/browserless-unblock-then-render-workflow.yml
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
- has_sources: true
  method: derived
  name: Browserless Finops
  primary_unit: units
  service_category: ''
  slug: browserless-finops
  template: false
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
mcp_servers:
- description: ''
  name: Browserless MCP Server
  slug: mcp
modified: '2026-05-25'
name: Browserless
nav: Providers
network: true
overview: 'Browserless publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Browser REST APIs API, Management REST APIs API, Agent API, and 15 more. Tagged areas include Browser Automation, Browser Infrastructure, AI Agents, Web Scraping, and BrowserQL.


  The Browserless catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Browserless'' developer surface includes documentation, API reference, engineering blog, pricing, changelog, signup flow, and 26 more developer resources.'
plans:
- name: Browserless Plans Pricing
  plan_count: 5
  slug: browserless-plans-pricing
- name: Browserless Price Estimates
  plan_count: 0
  slug: browserless-price-estimates
random_paper: 11
rate_limits:
- limit_count: 10
  name: Browserless Rate Limits
  slug: browserless-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Browserless — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: browserless-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Browserless API Rules
  rule_count: 10
  severity_counts:
    error: 0
    hint: 0
    info: 4
    warn: 6
  slug: browserless-rules
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 74.4
    catalog_earned_first_party: 12.0
    catalog_gap: 40.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.9
  facets:
    access_clarity: 85.5
    contract_governance: 27.3
    contract_quality: 55.5
    developer_ergonomics: 36.9
    discoverability: 75.0
    operational_transparency: 34.2
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 81.8
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/browserless/browserless-2026-06-20T173726.png
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
- Browser Automation
- Browser Infrastructure
- AI Agents
- Web Scraping
- BrowserQL
- Puppeteer
- Playwright
- Selenium
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
- Chrome DevTools Protocol
website: https://www.browserless.io
---
