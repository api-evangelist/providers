---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 52
  human_in_the_loop: 12
  name: Hyperbrowser Agentic Access
  operation_count: 108
  slug: hyperbrowser-agentic-access
  summary_line: 108 operations · 52 acting · 12 human-in-the-loop
api_count: 12
apis:
- description: 'Manage cloud Chromium browser sessions: create, list, inspect, update, and stop sessions; retrieve recording, video, and downloads URLs; and run manual CAPTCHA evaluation. Sessions expose a WebSocket '
  name: Hyperbrowser Sessions API
  slug: sessions-api
- description: Create, list, fetch, and delete persistent browser profiles that retain cookies, local storage, and authenticated state across sessions.
  name: Hyperbrowser Profiles API
  slug: profiles-api
- description: Single-page and batch scrape jobs returning HTML, Markdown, links, and screenshots with asynchronous status polling.
  name: Hyperbrowser Scrape API
  slug: scrape-api
- description: Recursive crawl jobs across many pages with structured page-by-page results and status polling.
  name: Hyperbrowser Crawl API
  slug: crawl-api
- description: Structured data extraction jobs that pull typed records from one or more pages using prompts and JSON schemas.
  name: Hyperbrowser Extract API
  slug: extract-api
- description: Start, stop, and monitor agentic browser tasks across HyperAgent, Browser-Use, Claude Computer Use, Gemini Computer Use, and OpenAI's CUA. Each task runs inside a stealth Hyperbrowser session with liv
  name: Hyperbrowser Agents API
  slug: agents-api
- description: Upload and list custom Chrome extensions that can be attached to browser sessions for advanced automation, custom UI, or workflow tooling.
  name: Hyperbrowser Extensions API
  slug: extensions-api
- description: 'Stateless web utilities: fetch a single page, run a web search, or start a crawl. Includes `/x402` micropayment-gated variants of fetch and search for permissionless, pay-per-call usage.'
  name: Hyperbrowser Web API
  slug: web-api
- description: The Profile API from Hyperbrowser — 2 operation(s) for profile.
  name: Hyperbrowser Profile API
  slug: hyperbrowser-profile-api
- description: The Session API from Hyperbrowser — 8 operation(s) for session.
  name: Hyperbrowser Session API
  slug: hyperbrowser-session-api
- description: The Task API from Hyperbrowser — 20 operation(s) for task.
  name: Hyperbrowser Task API
  slug: hyperbrowser-task-api
- description: The X402 API from Hyperbrowser — 2 operation(s) for x402.
  name: Hyperbrowser X402 API
  slug: hyperbrowser-x402-api
arazzos:
- description: Start a batch scrape over many URLs, poll status, then fetch all results.
  name: Hyperbrowser Batch Scrape and Retrieve
  slug: hyperbrowser-batch-scrape-and-retrieve-workflow
- description: Start a Browser Use agent task, poll status, then fetch its final result.
  name: Hyperbrowser Browser Use Task Run
  slug: hyperbrowser-browser-use-task-run-workflow
- description: Start a crawl from a seed URL, poll status, then page through the results.
  name: Hyperbrowser Crawl Site and Retrieve
  slug: hyperbrowser-crawl-site-and-retrieve-workflow
- description: Start an extract job with a prompt and schema, poll status, then fetch data.
  name: Hyperbrowser Extract Structured Data
  slug: hyperbrowser-extract-structured-data-workflow
- description: Start a HyperAgent task, poll status, then fetch its final result.
  name: Hyperbrowser HyperAgent Task Run
  slug: hyperbrowser-hyperagent-task-run-workflow
- description: Create a profile, launch a session bound to it, persist changes, then stop.
  name: Hyperbrowser Persistent Profile Session
  slug: hyperbrowser-persistent-profile-session-workflow
- description: Start a scrape job for a single URL, poll its status, then fetch the result.
  name: Hyperbrowser Scrape and Retrieve
  slug: hyperbrowser-scrape-and-retrieve-workflow
- description: Create a cloud browser session, inspect it, and stop it cleanly.
  name: Hyperbrowser Session Lifecycle
  slug: hyperbrowser-session-lifecycle-workflow
- description: Create a recorded browser session, stop it, then poll for the recording URL.
  name: Hyperbrowser Session Recording Retrieval
  slug: hyperbrowser-session-recording-retrieval-workflow
- description: Start a Web API crawl job, poll status, then page through the results.
  name: Hyperbrowser Web Crawl and Retrieve
  slug: hyperbrowser-web-crawl-and-retrieve-workflow
- description: Search the web, confirm results, then fetch the top result page as markdown.
  name: Hyperbrowser Web Search then Fetch
  slug: hyperbrowser-web-search-then-fetch-workflow
artifact_total: 60
collections:
- collection_type: postman
  name: Hyperbrowser Agents API
  slug: postman-hyperbrowser-agents-api
- collection_type: postman
  name: Hyperbrowser Crawl API
  slug: postman-hyperbrowser-crawl-api
- collection_type: postman
  name: Hyperbrowser Extensions API
  slug: postman-hyperbrowser-extensions-api
- collection_type: postman
  name: Hyperbrowser Extract API
  slug: postman-hyperbrowser-extract-api
- collection_type: postman
  name: Hyperbrowser Profiles API
  slug: postman-hyperbrowser-profiles-api
- collection_type: postman
  name: Hyperbrowser Scrape API
  slug: postman-hyperbrowser-scrape-api
- collection_type: postman
  name: Hyperbrowser Sessions API
  slug: postman-hyperbrowser-sessions-api
- collection_type: postman
  name: Hyperbrowser Web API
  slug: postman-hyperbrowser-web-api
- collection_type: open
  name: Hyperbrowser Agents API
  slug: open-hyperbrowser-agents-api
- collection_type: open
  name: Hyperbrowser Crawl API
  slug: open-hyperbrowser-crawl-api
- collection_type: open
  name: Hyperbrowser Extensions API
  slug: open-hyperbrowser-extensions-api
- collection_type: open
  name: Hyperbrowser Extract API
  slug: open-hyperbrowser-extract-api
- collection_type: open
  name: Hyperbrowser Profiles API
  slug: open-hyperbrowser-profiles-api
- collection_type: open
  name: Hyperbrowser Scrape API
  slug: open-hyperbrowser-scrape-api
- collection_type: open
  name: Hyperbrowser Sessions API
  slug: open-hyperbrowser-sessions-api
- collection_type: open
  name: Hyperbrowser Web API
  slug: open-hyperbrowser-web-api
- collection_type: open
  name: Hyperbrowser API
  slug: open-hyperbrowser
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hyperbrowser-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyperbrowser-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hyperbrowser-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/hyperbrowser/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbrowser-batch-scrape-and-retrieve-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbrowser-browser-use-task-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbrowser-crawl-site-and-retrieve-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbrowser-extract-structured-data-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbrowser-hyperagent-task-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbrowser-persistent-profile-session-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbrowser-scrape-and-retrieve-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbrowser-session-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbrowser-session-recording-retrieval-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbrowser-web-crawl-and-retrieve-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbrowser-web-search-then-fetch-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://hyperbrowser.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hyperbrowser.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hyperbrowser.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hyperbrowser.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://hyperbrowser.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hyperbrowserai
- group: commercial
  title: ''
  type: Pricing
  url: https://hyperbrowser.ai/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.hyperbrowser.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hyperbrowser.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hyperbrowser.ai/privacy
- group: agent
  title: ''
  type: LlmsText
  url: https://hyperbrowser.ai/llms.txt
- group: build
  title: ''
  type: SDKs
  url: https://github.com/hyperbrowserai/python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/hyperbrowserai/node-sdk
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/hyperbrowser/
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@hyperbrowser/sdk
- group: build
  title: ''
  type: Tools
  url: https://github.com/hyperbrowserai/mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/hyperbrowserai/HyperAgent
- group: build
  title: ''
  type: Tools
  url: https://github.com/hyperbrowserai/n8n-node
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/hyperbrowserai/examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/hyperbrowserai/hyperbrowser-app-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/hyperbrowserai/cua-as-a-tool
- group: commercial
  title: ''
  type: Plans
  url: plans/hyperbrowser-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hyperbrowser-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hyperbrowser-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/hyperbrowser-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hyperbrowser-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/hyperbrowser-rules.yml
created: '2026-05-23'
description: Hyperbrowser provides cloud browser infrastructure tailored for AI agents, bundling managed Chromium sessions with web scraping, crawling, and data-extraction APIs. The platform ships the open-source HyperAgent framework and first-class integrations for Browser-Use, Claude Computer Use, Gemini Computer Use, and OpenAI's CUA, so teams can deploy general-purpose web agents quickly. Customers include AI startups, data teams, and enterprises that need stealthy, multi-region browsers with CAPTCHA solving, proxies, and session profiles. Python and Node SDKs cover sessions, scrape/crawl/extract jobs, agent task management, and an MCP server lets any Model Context Protocol client (Claude Desktop, Cursor, Windsurf, etc.) drive Hyperbrowser tools. Pricing is usage-based via the hyperbrowser.ai pricing page.
examples:
- key_count: 3
  name: Hyperbrowser Claude Computer Use Example
  slug: hyperbrowser-claude-computer-use-example
- key_count: 3
  name: Hyperbrowser Create Session Example
  slug: hyperbrowser-create-session-example
- key_count: 3
  name: Hyperbrowser Extract Example
  slug: hyperbrowser-extract-example
- key_count: 3
  name: Hyperbrowser Scrape Example
  slug: hyperbrowser-scrape-example
- key_count: 3
  name: Hyperbrowser Web Search Example
  slug: hyperbrowser-web-search-example
finops:
- name: Hyperbrowser Finops
  service_category: API
  slug: hyperbrowser-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyperbrowser.png
json_schemas:
- name: Hyperbrowser Agent Task
  property_count: 5
  slug: hyperbrowser-agent-task
- name: Hyperbrowser Crawl Job
  property_count: 1
  slug: hyperbrowser-crawl-job
- name: Hyperbrowser Extract Job
  property_count: 4
  slug: hyperbrowser-extract-job
- name: Hyperbrowser Scrape Job
  property_count: 4
  slug: hyperbrowser-scrape-job
- name: Hyperbrowser Session
  property_count: 0
  slug: hyperbrowser-session
json_structures:
- name: Hyperbrowser Session Structure
  property_count: 0
  slug: hyperbrowser-session-structure
jsonld:
- class_count: 0
  name: Hyperbrowser Context
  property_count: 10
  slug: hyperbrowser-context
layout: provider
modified: '2026-05-25'
name: Hyperbrowser
nav: Providers
network: true
overview: 'Hyperbrowser publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Sessions API, Profiles API, Scrape API, and 9 more. Tagged areas include Headless Browser, Browser Infrastructure, Web Scraping, Web Crawling, and Data Extraction.


  The Hyperbrowser catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Hyperbrowser''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 35 more developer resources.'
plans:
- name: Hyperbrowser Plans Pricing
  plan_count: 1
  slug: hyperbrowser-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Hyperbrowser Rate Limits
  slug: hyperbrowser-rate-limits
rules:
- name: Hyperbrowser API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: hyperbrowser-jsonschema-spectral-rules
- name: Hyperbrowser API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: hyperbrowser-rules
score:
  band: strong
  composite: 62.7
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 65.6
    developer_ergonomics: 58.7
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 62.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyperbrowser/refs/heads/main/screenshots/hyperbrowser-2026-06-20T183036.png
security:
- kind: authentication
  name: Hyperbrowser Authentication
  slug: hyperbrowser-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hyperbrowser Domain Security
  slug: hyperbrowser-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hyperbrowser
tags:
- Headless Browser
- Browser Infrastructure
- Web Scraping
- Web Crawling
- Data Extraction
- AI Agents
- Browser Automation
- Computer Use
- Stealth
- Proxies
- CAPTCHA Solving
- MCP
- HyperAgent
- X402
website: https://hyperbrowser.ai
---
