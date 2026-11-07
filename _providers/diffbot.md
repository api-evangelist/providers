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
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Diffbot Agentic Access
  operation_count: 53
  slug: diffbot-agentic-access
  summary_line: 53 operations · 9 acting
api_count: 9
apis:
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: Diffbot Extract API is a powerful tool that allows users to automatically extract multiple types of data from web pages. This API is capable of extracting information such as article text, author deta
  name: Diffbot Extract API
  slug: diffbot-extract-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: Diffbot Crawl API is a powerful tool that automates the process of extracting content and data from websites on a large scale. By using advanced machine learning algorithms, the API can analyze and ex
  name: Diffbot Crawl API
  phrasing_intents:
  - id: create-a-crawl
    intent: Create a crawl that spiders and extracts a site
    question: How do I spider an entire website and extract structured data from every page?
  - id: manage-a-crawl-job
    intent: Pause, restart, delete or check a crawl job
    question: How do I pause a crawl that's already spidering a site?
  - id: retrieve-crawl-job-data
    intent: Download the results of a crawl job
    question: Where do I download the pages a crawl job extracted?
  phrasing_ops: 3
  slug: diffbot-crawl-api
- baseURL: https://nl.diffbot.com
  baseurl_source: declared
  description: Diffbot Natural Language API allows users to extract and analyze textual content from websites. By utilizing advanced natural language processing algorithms, the API can automatically identify and ext
  name: Diffbot Natural Language API
  phrasing_intents: []
  phrasing_ops: 1
  slug: diffbot-natural-language-api
- baseURL: https://kg.diffbot.com/kg/v3
  baseurl_source: declared
  description: The Knowledge Graph itself — a linked graph of over 10 billion entities (organizations, people, articles, places, products, job posts and more) crawled and structured from the public web. It is reache
  name: Diffbot Knowledge Graph API
  phrasing_intents:
  - id: dqlSearch
    intent: Query the Knowledge Graph using DQL
    question: How do I search for companies or people in the Knowledge Graph?
  - id: enhance
    intent: Enrich a person or organization record
    question: Can I enrich a company record from just its name?
  phrasing_ops: 2
  slug: diffbot-knowledge-graph-api
- description: The Diffbot Crawl/Bulk Job API is a powerful tool that allows users to automatically extract and organize large amounts of web data. It enables users to create custom scraping jobs that can gather inf
  name: Diffbot Crawl/Bulk Job API
  slug: diffbot-crawlbulk-job-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: The Account API from Diffbot — 1 operation(s) for account.
  name: Diffbot Account API
  phrasing_intents:
  - id: account
    intent: View account plan, usage and child tokens
    question: What plan is my Diffbot account on and how many API calls have I used?
  phrasing_ops: 1
  slug: diffbot-account-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: The Analyze API from Diffbot — 1 operation(s) for analyze.
  name: Diffbot Analyze API
  phrasing_intents:
  - id: extract-analyze
    intent: Classify a page and extract its data by type
    question: How do I extract data from a web page when I don't know if it's an article, product or something else?
  phrasing_ops: 1
  slug: diffbot-analyze-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: The Article API from Diffbot — 1 operation(s) for article.
  name: Diffbot Article API
  phrasing_intents:
  - id: article
    intent: Extract clean text and data from an article
    question: How do I pull the clean text out of a news article or blog post?
  phrasing_ops: 1
  slug: diffbot-article-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: The Bulk API from Diffbot — 2 operation(s) for bulk.
  name: Diffbot Bulk API
  phrasing_intents:
  - id: create-a-bulk-job
    intent: Start a bulk extract job over a list of URLs
    question: Can I extract thousands of URLs asynchronously instead of one call at a time?
  - id: pause-delete-or-restart-a-bulk-job
    intent: Pause, restart, delete or check a bulk extract job
    question: How do I pause a bulk extraction job that is still running?
  - id: retrieve-bulk-job-data
    intent: Download the results of a bulk extract job
    question: How do I download the extracted output of a finished bulk job?
  phrasing_ops: 3
  slug: diffbot-bulk-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: Enhance multiple records asynchronously
  name: Diffbot Bulk Enhance API
  phrasing_intents:
  - id: submitBulkjob
    intent: Submit a bulk enhance job for many records
    question: How do I enrich a large batch of people or company records at once?
  - id: bulkjobStatusForToken
    intent: List all bulk enhance jobs on my token
    question: Which bulk enhance jobs have I submitted and what state are they in?
  - id: bulkjobStatus
    intent: Check the status of one bulk enhance job
    question: Is my bulk enhance job finished yet?
  - id: bulkjobResultGet
    intent: Download bulk enhance results via query string
    question: How do I download the enriched records from a completed bulk enhance job?
  - id: bulkjobResultPost
    intent: Download bulk enhance results with a POST body
    question: Can I send export options in a request body when downloading bulk enhance results?
  - id: coverageReportGet
    intent: Download a bulk enhance coverage report
    question: How do I see how many records in my bulk enhance job had coverage for each field?
  - id: deleteBulkjob
    intent: Delete a bulk enhance job
    question: Can I permanently remove an old bulk enhance job?
  - id: singleResult
    intent: Get one record's result from a bulk enhance job
    question: Can I fetch just one enriched record out of a bulk enhance job by its position?
  phrasing_ops: 9
  slug: diffbot-bulk-enhance-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: Enhance both a person and the employer data
  name: Diffbot Combine API
  phrasing_intents:
  - id: combine
    intent: Enrich a person plus their current employer
    question: How do I get both a person's profile and their current company's data in one call?
  phrasing_ops: 1
  slug: diffbot-combine-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: The Custom API from Diffbot — 2 operation(s) for custom.
  name: Diffbot Custom API
  phrasing_intents:
  - id: customget
    intent: Extract a page with one of my Custom APIs
    question: How do I run a page through the custom extraction rules I built?
  - id: retrieve-a-custom-api
    intent: List my Custom APIs and their rules
    question: Which Custom APIs and rules are defined on my token?
  - id: create-a-custom-api
    intent: Create or update a Custom API ruleset
    question: How do I define custom extraction rules for pages matching a URL pattern?
  - id: delete-a-custom-api
    intent: Delete a Custom API ruleset
    question: Can I remove a custom extraction ruleset I no longer use?
  phrasing_ops: 4
  slug: diffbot-custom-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: The Discussion API from Diffbot — 1 operation(s) for discussion.
  name: Diffbot Discussion API
  phrasing_intents:
  - id: discussion
    intent: Extract comment and review threads from a page
    question: How do I extract all the comments or reviews from a forum thread?
  phrasing_ops: 1
  slug: diffbot-discussion-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: DQL Search
  name: Diffbot DQL Search API
  phrasing_intents:
  - id: dqlGet
    intent: Search the Knowledge Graph with a DQL query
    question: How do I search the Knowledge Graph for organizations matching certain criteria?
  - id: dqlPost
    intent: Search the Knowledge Graph with DQL in a POST body
    question: Can I send a long DQL query in a request body instead of the URL?
  - id: reportFind
    intent: Get a coverage report for a DQL query
    question: How complete is the data for the entities my DQL query returns?
  - id: reportGet
    intent: Download a coverage report by its ID
    question: Can I re-download a Knowledge Graph coverage report I generated earlier?
  phrasing_ops: 4
  slug: diffbot-dql-search-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: Enhance single records synchronously
  name: Diffbot Enhance API
  phrasing_intents:
  - id: enhance
    intent: Enrich a person or company from partial data
    question: How do I enrich a company record when I only have its name or website?
  - id: enhancePost
    intent: Enrich a person or company via a POST body
    question: Can I send enrichment inputs in a JSON body instead of query parameters?
  - id: combine
    intent: Enrich a person and return their employer too
    question: Can one lookup return both the person and data about their current employer?
  phrasing_ops: 3
  slug: diffbot-enhance-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: The Event API from Diffbot — 1 operation(s) for event.
  name: Diffbot Event API
  phrasing_intents:
  - id: event
    intent: Extract dates, venue and details from an event page
    question: How do I pull the date, location and description out of an event listing page?
  phrasing_ops: 1
  slug: diffbot-event-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: The Image API from Diffbot — 1 operation(s) for image.
  name: Diffbot Image API
  phrasing_intents:
  - id: image
    intent: Identify a page's primary images and their metadata
    question: How do I find the main image on a web page along with its metadata?
  phrasing_ops: 1
  slug: diffbot-image-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: The Job API from Diffbot — 1 operation(s) for job.
  name: Diffbot Job API
  phrasing_intents:
  - id: job
    intent: Extract structured data from a job posting
    question: How do I turn a job posting page into structured fields?
  phrasing_ops: 1
  slug: diffbot-job-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: The List API from Diffbot — 1 operation(s) for list.
  name: Diffbot List API
  phrasing_intents:
  - id: list
    intent: Structure the items on a list-like page
    question: How do I extract every item from a product listing or search results page?
  phrasing_ops: 1
  slug: diffbot-list-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: The Product API from Diffbot — 1 operation(s) for product.
  name: Diffbot Product API
  phrasing_intents:
  - id: product
    intent: Extract price, specs and images from a product page
    question: How do I extract the price and specs from an e-commerce product page?
  phrasing_ops: 1
  slug: diffbot-product-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: The Video API from Diffbot — 1 operation(s) for video.
  name: Diffbot Video API
  phrasing_intents:
  - id: video
    intent: Extract metadata and embed code from a video page
    question: How do I get a video's metadata, thumbnail and embed code from its page?
  phrasing_ops: 1
  slug: diffbot-video-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: The Web Search API from Diffbot — 1 operation(s) for web search.
  name: Diffbot Web Search API
  phrasing_intents:
  - id: get_
    intent: Search the web index with a query string
    question: How do I search Diffbot's web index from a simple GET request?
  - id: post_
    intent: Search the web index with a JSON body
    question: Can I send a web search query with operators like date filters in a request body?
  phrasing_ops: 2
  slug: diffbot-web-search-api
artifact_total: 47
asyncapis:
- description: ''
  name: Diffbot Webhooks
  slug: diffbot-webhooks
collections:
- collection_type: open
  name: Diffbot Crawl API
  slug: open-diffbot-crawl-api
- collection_type: open
  name: Diffbot Crawl Extract API
  slug: open-diffbot-extract-api
- collection_type: open
  name: Diffbot Crawl Knowledge Graph API
  slug: open-diffbot-knowledge-graph-api
- collection_type: open
  name: Diffbot Crawl Natural Language API
  slug: open-diffbot-natural-language-api
- collection_type: open
  name: Diffbot API
  slug: open-diffbot
common:
- group: other
  href: https://artifacts.apis.io/diffbot/capabilities/diffbot-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/diffbot-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/diffbot/overlays/diffbot-bulk-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/diffbot-bulk-overlay.yaml
- group: other
  href: https://artifacts.apis.io/diffbot/overlays/diffbot-dql-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/diffbot-dql-overlay.yaml
- group: other
  href: https://artifacts.apis.io/diffbot/overlays/diffbot-enhance-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/diffbot-enhance-overlay.yaml
- group: other
  href: https://artifacts.apis.io/diffbot/overlays/diffbot-web-search-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/diffbot-web-search-overlay.yaml
- group: other
  href: https://artifacts.apis.io/diffbot/overlays/diffbot-account-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/diffbot-account-overlay.yaml
- group: docs
  href: https://artifacts.apis.io/diffbot/openapi/_original/diffbot-extract-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/diffbot-extract-openapi.json
- group: build
  href: https://artifacts.apis.io/diffbot/packages/diffbot-packages.yml
  title: ''
  type: Packages
  url: packages/diffbot-packages.yml
- group: build
  href: https://artifacts.apis.io/diffbot/packages/diffbot-packages.yml
  title: ''
  type: SDKs
  url: packages/diffbot-packages.yml
- group: agent
  href: https://artifacts.apis.io/diffbot/mcp/diffbot-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/diffbot-mcp.yml
- group: build
  href: https://artifacts.apis.io/diffbot/mcp/diffbot-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/diffbot-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/diffbot/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/diffbot/conventions/diffbot-conventions.yml
  title: ''
  type: Conventions
  url: conventions/diffbot-conventions.yml
- group: design
  href: https://artifacts.apis.io/diffbot/errors/diffbot-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/diffbot-error-codes.yml
- group: design
  href: https://artifacts.apis.io/diffbot/lifecycle/diffbot-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/diffbot-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.diffbot.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://www.diffbot.com/docs/dql/migrating-from-legacy-api
- group: operate
  href: https://artifacts.apis.io/diffbot/changelog/diffbot-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/diffbot-changelog.yml
- group: build
  href: https://artifacts.apis.io/diffbot/cli/diffbot-cli.yml
  title: ''
  type: CLI
  url: cli/diffbot-cli.yml
- group: start
  href: https://artifacts.apis.io/diffbot/sandbox/diffbot-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/diffbot-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://www.diffbot.com/products/extract/testdrive
- group: design
  href: https://artifacts.apis.io/diffbot/conformance/diffbot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/diffbot-conformance.yml
- group: auth
  href: https://artifacts.apis.io/diffbot/conformance/diffbot-conformance.yml
  title: ''
  type: Compliance
  url: conformance/diffbot-conformance.yml
- group: design
  href: https://artifacts.apis.io/diffbot/data-model/diffbot-data-model.yml
  title: ''
  type: DataModel
  url: data-model/diffbot-data-model.yml
- group: design
  href: https://artifacts.apis.io/diffbot/asyncapi/diffbot-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/diffbot-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/diffbot/rate-limits/diffbot-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/diffbot-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/diffbot/plans/diffbot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/diffbot-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/diffbot/finops/diffbot-finops.yml
  title: ''
  type: FinOps
  url: finops/diffbot-finops.yml
- group: other
  href: https://artifacts.apis.io/diffbot/overlays/diffbot-extract-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/diffbot-extract-overlay.yaml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/diffbotai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.diffbot.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.diffbot.com/docs/interfaces/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.diffbot.com/docs/products-overview
- group: auth
  title: ''
  type: Authentication
  url: https://www.diffbot.com/docs/authentication
- group: start
  title: ''
  type: SignUp
  url: https://app.diffbot.com/get-started
- group: start
  title: ''
  type: Login
  url: https://app.diffbot.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@diffbot.com
- group: company
  title: ''
  type: Careers
  url: https://www.diffbot.com/company/careers
- group: agent
  href: https://artifacts.apis.io/diffbot/agentic-access/diffbot-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/diffbot-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/diffbot/security/diffbot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diffbot-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/diffbot/authentication/diffbot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/diffbot-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/diffbot
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/diffbot
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.diffbot.com/changelog
- group: company
  title: ''
  type: Website
  url: https://www.diffbot.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.diffbot.com/pricing/
- group: other
  title: ''
  type: Customers
  url: https://www.diffbot.com/customer-stories/
- group: docs
  title: ''
  type: Documentation
  url: https://www.diffbot.com/docs/
- group: company
  title: ''
  type: News
  url: https://www.diffbot.com/company/news/
- group: company
  title: ''
  type: Blog
  url: https://blog.diffbot.com/
- group: other
  title: ''
  type: Glossary
  url: https://blog.diffbot.com/knowledge-graph-glossary/
- group: learn
  title: ''
  type: Webinars
  url: https://blog.diffbot.com/webinars/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.diffbot.com/company/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.diffbot.com/company/privacy/
- group: other
  title: ''
  type: DataLicensing
  url: https://www.diffbot.com/docs/account-billing/gdpr
- group: agent
  href: https://artifacts.apis.io/diffbot/llms/diffbot-llms.txt
  title: ''
  type: LlmsText
  url: llms/diffbot-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.diffbot.com/llms.txt
created: '2024-11-13'
description: Diffbot is a company that provides AI-powered web scraping and data extraction services. Their technology allows businesses to automatically extract and organize data from any website, turning unstructured web content into structured data that can be easily analyzed and used for various purposes. Diffbot's solution is used by companies across industries to gather competitive intelligence, monitor market trends, track online mentions, and more.
finops:
- has_sources: true
  method: derived
  name: Diffbot Finops
  primary_unit: credits
  service_category: ''
  slug: diffbot-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/diffbot.png
layout: provider
mcp_servers:
- description: 'Diffbot''s first-party MCP server. Exposes the Extract, Web Search, Knowledge Graph (Enhance / DQL), Crawl and Natural Language surfaces as seven agent tools. Diffbot operates a hosted remote endpoint '
  name: Diffbot MCP Server
  slug: diffbot-mcp-server
modified: '2026-09-06'
name: Diffbot
nav: Providers
network: true
overview: 'Diffbot publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Extract API, Crawl API, Natural Language API, and 19 more. Tagged areas include Extraction, Harvesting, Web Scraping, Web, and Knowledge Graph.


  The Diffbot catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Diffbot''s developer surface includes changelog, CLI, sandbox, developer console, API reference, getting-started guide, authentication, and 50 more developer resources.'
plans:
- name: Diffbot Plans Pricing
  plan_count: 4
  slug: diffbot-plans-pricing
- name: Diffbot Price Estimates
  plan_count: 0
  slug: diffbot-price-estimates
random_paper: 14
rate_limits:
- limit_count: 12
  name: Diffbot Rate Limits
  slug: diffbot-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Diffbot API Rules
  rule_count: 52
  severity_counts:
    error: 34
    hint: 0
    info: 3
    warn: 15
  slug: diffbot-rules
score:
  band: exemplar
  composite: 77.8
  coverage:
    artifact_dirs: 32
    catalog_earned: 71.5
    catalog_earned_first_party: 24.0
    catalog_gap: 43.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 61.3
    developer_ergonomics: 90.5
    discoverability: 81.7
    operational_transparency: 81.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 77.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 52.4
      total: 21
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/diffbot/diffbot-2026-06-20T180012.png
security:
- kind: authentication
  name: Diffbot Authentication
  slug: diffbot-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Diffbot Domain Security
  slug: diffbot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 10
skills:
- name: diffbot-crawl
  slug: diffbot-crawl
- name: diffbot-deals
  slug: diffbot-deals
- name: diffbot-dql
  slug: diffbot-dql
- name: diffbot-entities
  slug: diffbot-entities
- name: diffbot-extract
  slug: diffbot-extract
- name: diffbot-news
  slug: diffbot-news
- name: diffbot-organizations
  slug: diffbot-organizations
- name: diffbot-people
  slug: diffbot-people
- name: diffbot-places
  slug: diffbot-places
- name: diffbot-web-search
  slug: diffbot-web-search
slug: diffbot
tags:
- Extraction
- Harvesting
- Web Scraping
- Web
- Knowledge Graph
- Crawling
- Web Search
- Natural-Language
- Entity Resolution
- Artificial Intelligence
- Data Extraction
website: https://www.diffbot.com/
---
