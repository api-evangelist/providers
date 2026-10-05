---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: platform
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.4
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Contextdev Agentic Access
  operation_count: 84
  slug: contextdev-agentic-access
  summary_line: 84 operations · 32 acting
api_count: 1
apis:
- baseURL: https://api.context.dev/v1
  baseurl_source: declared
  description: The Brand Intelligence API from Context.dev — 7 operation(s) for brand intelligence.
  name: Context.dev Brand Intelligence API
  phrasing_intents:
  - id: getBrandRetrieve
    intent: Get a company's brand kit from its domain
    question: Can I get a company's logos, colors and industry just from its website domain?
  - id: postBrandRetrieve
    intent: Look up a brand with one identifier in a request body
    question: Which single endpoint lets me look up a brand by domain, name, email, ticker, transaction or direct URL in a JSON body?
  - id: getBrandRetrieveByName
    intent: Find a brand by its company name
    question: I only know the company name, not its website. Can I still get its logo and colors?
  - id: getBrandRetrieveByEmail
    intent: Identify a company's brand from a work email
    question: Can I figure out which company a signup belongs to from their work email address?
  - id: getBrandRetrieveByTicker
    intent: Get a public company's brand from its stock ticker
    question: Can I get a public company's logo from its stock ticker symbol like AAPL?
  - id: getBrandRetrieveByIsin
    intent: Get a company's brand from its ISIN
    question: Can I look up a company's brand assets from an ISIN securities identifier?
  - id: getBrandTransactionIdentifier
    intent: Identify the merchant behind a card transaction
    question: How do I turn a messy bank transaction description into a recognizable merchant brand?
  - id: getBrandRetrieveSimplified
    intent: Get a lightweight brand summary for a domain
    question: Is there a faster, smaller brand response with just the title, colors, logos and backdrops?
  phrasing_ops: 8
  slug: contextdev-brand-intelligence-api
- baseURL: https://api.context.dev/v1
  baseurl_source: declared
  description: Monitor pages, sitemaps, and extracted website data for exact or semantic changes. Webhook payloads are documented by the MonitorsChangeDetectedWebhookPayload and MonitorsRunCompletedWebhookPayload sc
  name: Context.dev Monitors API
  phrasing_intents:
  - id: createMonitor
    intent: Create a website change monitor
    question: How do I start watching a web page for changes?
  - id: listMonitors
    intent: List and search my website monitors
    question: How do I see all the website monitors set up on my Context.dev account?
  - id: getMonitor
    intent: Get the details of one monitor
    question: Where can I see the full configuration of a single monitor?
  - id: updateMonitor
    intent: Update an existing monitor's settings
    question: Can I pause an existing monitor or rename it without recreating it?
  - id: deleteMonitor
    intent: Delete a monitor
    question: How do I permanently remove a monitor I no longer need?
  - id: listMonitorRuns
    intent: List the run history of one monitor
    question: When did a specific monitor last run, and did it succeed?
  - id: listMonitorChanges
    intent: List changes detected by one monitor
    question: What changes has a particular monitor picked up on its page?
  - id: listAccountRuns
    intent: List monitor runs across my whole account
    question: Is there one feed of runs across every monitor on my account?
  phrasing_ops: 13
  slug: contextdev-monitors-api
- baseURL: https://api.context.dev/v1
  baseurl_source: declared
  description: The Parsing API from Context.dev — 1 operation(s) for parsing.
  name: Context.dev Parsing API
  phrasing_intents:
  - id: postParse
    intent: Convert a file's raw bytes into Markdown
    question: How do I turn a PDF, Word or Excel file into Markdown an LLM can read?
  phrasing_ops: 1
  slug: contextdev-parsing-api
- baseURL: https://api.context.dev/v1
  baseurl_source: declared
  description: The People API from Context.dev — 1 operation(s) for people.
  name: Context.dev People API
  phrasing_intents:
  - id: postPeopleRetrieve
    intent: Look up a person's profile from known identifiers
    question: Can I get a normalized profile of a person from identifiers I already have about them?
  phrasing_ops: 1
  slug: contextdev-people-api
- baseURL: https://api.context.dev/v1
  baseurl_source: declared
  description: The Utility API from Context.dev — 3 operation(s) for utility.
  name: Context.dev Utility API
  phrasing_intents:
  - id: postBrandPrefetch
    intent: Warm up brand data for a domain ahead of time
    question: Can I make brand lookups for a domain faster by prefetching them before I need them?
  - id: postBrandPrefetchByEmail
    intent: Warm up brand data from a signup's email
    question: Can I prefetch a company's brand data from a new user's work email at signup?
  - id: postUtilityPrefetch
    intent: Queue a prefetch by type and identifier
    question: Is there a general utility prefetch that takes a type and a domain-or-email identifier?
  phrasing_ops: 3
  slug: contextdev-utility-api
- baseURL: https://api.context.dev/v1
  baseurl_source: declared
  description: The Web Extraction API from Context.dev — 9 operation(s) for web extraction.
  name: Context.dev Web Extraction API
  phrasing_intents:
  - id: postWebExtract
    intent: Extract structured data from a site using a schema
    question: Can I crawl a website and get back data shaped to my own JSON Schema?
  - id: getWebCompetitors
    intent: Find a company's direct competitors
    question: Who are the direct competitors of a company, based on its website?
  - id: getWebStyleguide
    intent: Extract a website's design system
    question: Can I pull a site's full design system — colors, typography, spacing, shadows and components?
  - id: getWebFonts
    intent: Find which fonts a website uses
    question: What font families does a website use, and how often is each one used?
  - id: getWebNaics
    intent: Classify a brand into NAICS industry codes
    question: What NAICS industry code fits a company, given its domain or name?
  - id: getWebSic
    intent: Classify a brand into SIC industry codes
    question: Which SIC code does a company fall under, from its domain or name?
  - id: postBrandAiQuery
    intent: Ask AI to pull specific data points from a brand's site
    question: Can AI read a company's website and answer specific data points I list, like pricing or HQ address?
  - id: postBrandAiProduct
    intent: Extract product details from one product page
    question: Given a single URL, can it tell me whether it's a product page and pull the product info?
  phrasing_ops: 9
  slug: contextdev-web-extraction-api
- baseURL: https://api.context.dev/v1
  baseurl_source: declared
  description: The Web Scraping API from Context.dev — 7 operation(s) for web scraping.
  name: Context.dev Web Scraping API
  phrasing_intents:
  - id: getWebScrapeHtml
    intent: Scrape a page's raw HTML
    question: Can I get the raw HTML of a web page, rendered in a browser?
  - id: getWebScrapeMarkdown
    intent: Scrape a single page into Markdown
    question: How do I turn one web page into clean Markdown for an LLM?
  - id: getWebScrapeImages
    intent: Collect all images on a web page
    question: Can I list every image on a page, including SVGs, CSS backgrounds and video posters?
  - id: getWebScrapeSitemap
    intent: List every page URL on a website
    question: How can I get a list of all the page URLs on a website from its sitemap?
  - id: postWebCrawl
    intent: Crawl a site and scrape many pages to Markdown
    question: Can I crawl a whole docs site from one starting URL and get every page back as Markdown?
  - id: postWebSearch
    intent: Search the web and optionally scrape results
    question: Can I run a web search and get each result scraped into Markdown in one call?
  - id: getWebScreenshot
    intent: Capture a screenshot of a website
    question: Can I take a full-page screenshot of a website?
  phrasing_ops: 7
  slug: contextdev-web-scraping-api
artifact_total: 24
asyncapis:
- description: ''
  name: Contextdev Webhooks
  slug: contextdev-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Context Brand Intelligence API
  slug: open-contextdev-brand-intelligence-api
- collection_type: open
  name: Context Brand Intelligence Monitors API
  slug: open-contextdev-monitors-api
- collection_type: open
  name: Context Brand Intelligence Parsing API
  slug: open-contextdev-parsing-api
- collection_type: open
  name: Context Brand Intelligence People API
  slug: open-contextdev-people-api
- collection_type: open
  name: Context Brand Intelligence Utility API
  slug: open-contextdev-utility-api
- collection_type: open
  name: Context Brand Intelligence Web Extraction API
  slug: open-contextdev-web-extraction-api
- collection_type: open
  name: Context Brand Intelligence Web Scraping API
  slug: open-contextdev-web-scraping-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.context.dev/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/skills/contextdev-scrape-in-batches.md
  title: ''
  type: AgentSkill
  url: skills/contextdev-scrape-in-batches.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/overlays/contextdev-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/contextdev-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/agentic-access/contextdev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/contextdev-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/security/contextdev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contextdev-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/authentication/contextdev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/contextdev-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/scopes/contextdev-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/contextdev-scopes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/packages/contextdev-packages.yml
  title: ''
  type: Packages
  url: packages/contextdev-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/packages/contextdev-packages.yml
  title: ''
  type: SDKs
  url: packages/contextdev-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/cli/contextdev-cli.yml
  title: ''
  type: CLI
  url: cli/contextdev-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/mcp/contextdev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/contextdev-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/llms/contextdev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contextdev-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/well-known/contextdev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contextdev-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/conventions/contextdev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/contextdev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/errors/contextdev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/contextdev-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/data-model/contextdev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/contextdev-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/conformance/contextdev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contextdev-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/lifecycle/contextdev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/contextdev-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.context.dev
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/asyncapi/contextdev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/contextdev-webhooks.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/changelog/contextdev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/contextdev-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.context.dev/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.context.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.context.dev/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.context.dev
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.context.dev/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.context.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/context-dot-dev
- group: operate
  title: ''
  type: Support
  url: mailto:support@context.dev
- group: commercial
  title: ''
  type: Pricing
  url: https://www.context.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.context.dev/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.context.dev/privacy
- group: other
  title: ''
  type: X
  url: https://x.com/getcontextdev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/contextdev/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/conventions/contextdev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/contextdev-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/rate-limits/contextdev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/contextdev-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/plans/contextdev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contextdev-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/a2a/contextdev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/contextdev-a2a.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/mcp/contextdev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/contextdev-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/security/contextdev-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/contextdev-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/security/contextdev-trust-center.yml
  title: ''
  type: Compliance
  url: security/contextdev-trust-center.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/overlays/contextdev-batch-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/contextdev-batch-api-overlay.yaml
- group: start
  title: ''
  type: Login
  url: https://www.context.dev/login
created: '2026-07-17'
description: Context.dev is the unified web-context API for software and AI agents — one API that turns any domain or URL into structured, typed JSON. It covers brand intelligence (logos, colors, fonts, socials, address, industry codes, stock ticker / ISIN and transaction-descriptor resolution), web scraping and crawling to clean Markdown or HTML, screenshots, sitemap discovery, web search, structured data extraction against a JSON Schema, product extraction, document parsing to Markdown, NAICS / SIC classification, and website change monitoring with signed webhooks. Typed first-party SDKs ship for TypeScript, Python, Ruby, Go, and PHP, alongside a CLI, a hosted MCP server, and a published Agent Skill. Founded in 2025 by Yahia Bakour and backed by Y Combinator (S26).
image: https://www.context.dev/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.context.dev over HTTP; 2 tools listed.
  name: Context.dev MCP Server
  slug: context
modified: '2026-08-14'
name: Context.dev
nav: Providers
network: true
overview: 'Context.dev publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Brand Intelligence API, Monitors API, Parsing API, and 4 more. Tagged areas include Web Scraping, Brand Intelligence, Data Enrichment, AI Agents, and Web Data.


  The Context.dev catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Context.dev''s developer surface includes authentication, CLI, changelog, documentation, API reference, getting-started guide, engineering blog, and 37 more developer resources.'
plans:
- name: Contextdev Plans Pricing
  plan_count: 5
  slug: contextdev-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 8
  name: Contextdev Rate Limits
  slug: contextdev-rate-limits
scopes:
- name: Contextdev Scopes
  scope_count: 2
  slug: contextdev-scopes
  summary_line: 2 scopes
score:
  band: exemplar
  composite: 67.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 58.7
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 65.8
  previous_composite: 67.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/screenshots/contextdev-2026-07-25T210330.png
security:
- kind: authentication
  name: Contextdev Authentication
  slug: contextdev-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Contextdev Domain Security
  slug: contextdev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Contextdev Trust Center
  slug: contextdev-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2
slug: contextdev
tags:
- Web Scraping
- Brand Intelligence
- Data Enrichment
- AI Agents
- Web Data
- Classification
- Website Monitoring
- Company Data
- Developer Tools
- A2A
website: https://www.context.dev/
---
