---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-09-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Diffbot Agentic Access
  operation_count: 14
  slug: diffbot-agentic-access
  summary_line: 14 operations · 1 acting
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
  slug: diffbot-crawl-api
- baseURL: https://api.diffbot.com/v3
  baseurl_source: declared
  description: Diffbot Bulk Extract API is a tool that allows users to extract data at scale from a variety of sources, including websites, documents, and social media platforms. This API utilizes machine learning a
  name: Diffbot Bulk Extract API
  slug: diffbot-bulk-extract-api
- baseURL: https://kg.diffbot.com
  baseurl_source: declared
  description: The Diffbot DQL API is a powerful tool that allows users to query and retrieve data from the web in a structured format. By using a simple query language, users can access a wealth of information from
  name: Diffbot DQL API
  slug: diffbot-dql-api
- baseURL: https://kg.diffbot.com
  baseurl_source: declared
  description: Diffbot Enhance API enhances data by providing additional context and insights. By analyzing text and images, the API can identify and extract key information, such as entities, topics, and sentiment,
  name: Diffbot Enhance API
  slug: diffbot-enhance-api
- baseURL: https://nl.diffbot.com
  baseurl_source: declared
  description: Diffbot Natural Language API allows users to extract and analyze textual content from websites. By utilizing advanced natural language processing algorithms, the API can automatically identify and ext
  name: Diffbot Natural Language API
  slug: diffbot-natural-language-api
- baseURL: https://llm.diffbot.com/api/v1/web_search
  baseurl_source: declared
  description: Search Diffbot's own web index — the largest independently crawled index outside Google and Bing, over 150TB. Candidates are retrieved and reranked by a cross-encoder trained to favour factual relevan
  name: Diffbot Web Search API
  slug: diffbot-web-search-api
- baseURL: https://api.diffbot.com/v4
  baseurl_source: declared
  description: 'Retrieve account details, plan, token metadata and usage activity for a Diffbot token. The only introspection surface Diffbot publishes: because the APIs return no rate-limit or quota response headers'
  name: Diffbot Account API
  slug: diffbot-account-api
- baseURL: https://kg.diffbot.com/kg/v3
  baseurl_source: declared
  description: The Knowledge Graph itself — a linked graph of over 10 billion entities (organizations, people, articles, places, products, job posts and more) crawled and structured from the public web. It is reache
  name: Diffbot Knowledge Graph API
  slug: diffbot-knowledge-graph-api
- description: The Diffbot Crawl/Bulk Job API is a powerful tool that allows users to automatically extract and organize large amounts of web data. It enables users to create custom scraping jobs that can gather inf
  name: Diffbot Crawl/Bulk Job API
  slug: diffbot-crawlbulk-job-api
artifact_total: 24
asyncapis:
- description: ''
  name: Diffbot Webhooks
  slug: diffbot-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/diffbot-extract-openapi.json
- group: build
  title: ''
  type: Packages
  url: packages/diffbot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/diffbot-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/diffbot-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/diffbot-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/diffbot-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/diffbot-error-codes.yml
- group: design
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
  title: ''
  type: ChangeLog
  url: changelog/diffbot-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/diffbot-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/diffbot-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://www.diffbot.com/products/extract/testdrive
- group: design
  title: ''
  type: Conformance
  url: conformance/diffbot-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/diffbot-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/diffbot-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/diffbot-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/diffbot-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/diffbot-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/diffbot-finops.yml
- group: other
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
  title: ''
  type: AgenticAccess
  url: agentic-access/diffbot-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/diffbot-domain-security.yml
- group: auth
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
- name: Diffbot Finops
  service_category: API
  slug: diffbot-finops
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
overview: 'Diffbot publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Extract API, Crawl API, Bulk Extract API, and 6 more. Tagged areas include Extraction, Harvesting, Scraping, Web, and Knowledge Graph.


  The Diffbot catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Diffbot''s developer surface includes changelog, CLI, sandbox, developer console, API reference, getting-started guide, authentication, and 44 more developer resources.'
plans:
- name: Diffbot Plans Pricing
  plan_count: 4
  slug: diffbot-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 12
  name: Diffbot Rate Limits
  slug: diffbot-rate-limits
score:
  band: exemplar
  composite: 73.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 67.0
    catalog_earned_first_party: 24.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.3
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 58.7
    developer_ergonomics: 90.5
    discoverability: 81.5
    operational_transparency: 81.6
  previous_composite: 71.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/diffbot/refs/heads/main/screenshots/diffbot-2026-06-20T180012.png
security:
- kind: authentication
  name: Diffbot Authentication
  slug: diffbot-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Diffbot Domain Security
  slug: diffbot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: diffbot
tags:
- Extraction
- Harvesting
- Scraping
- Web
- Knowledge Graph
- Crawling
- Web Search
- Natural Language
- Entity Resolution
- AI
website: https://www.diffbot.com/
---
