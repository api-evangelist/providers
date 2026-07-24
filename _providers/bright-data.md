---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 27
  human_in_the_loop: 1
  name: Bright Data Agentic Access
  operation_count: 56
  slug: bright-data-agentic-access
  summary_line: 56 operations · 27 acting · 1 human-in-the-loop
api_count: 17
apis:
- description: Real-time SERP data from Google, Bing, Yandex, and DuckDuckGo across 31 languages and 195 countries. Supports organic, news, images, videos, shopping, jobs, hotels, flights, lens, trends, reviews, map
  name: Bright Data SERP API
  slug: serp-api
- description: Bright Data's Model Context Protocol server exposes 60+ web-access tools (search, scrape, structured extraction, browser automation, datasets) to MCP-compatible clients including Claude Desktop, Claud
  name: Bright Data MCP Server
  slug: mcp-server
- description: The Access API from Bright Data — 3 operation(s) for access.
  name: Bright Data Access API
  slug: bright-data-access-api
- description: The Archive API from Bright Data — 4 operation(s) for archive.
  name: Bright Data Archive API
  slug: bright-data-archive-api
- description: The Billing API from Bright Data — 2 operation(s) for billing.
  name: Bright Data Billing API
  slug: bright-data-billing-api
- description: The Datasets API from Bright Data — 2 operation(s) for datasets.
  name: Bright Data Datasets API
  slug: bright-data-datasets-api
- description: The Delivery API from Bright Data — 2 operation(s) for delivery.
  name: Bright Data Delivery API
  slug: bright-data-delivery-api
- description: The IPs API from Bright Data — 2 operation(s) for ips.
  name: Bright Data IPs API
  slug: bright-data-ips-api
- description: The Lookup API from Bright Data — 6 operation(s) for lookup.
  name: Bright Data Lookup API
  slug: bright-data-lookup-api
- description: The Proxies API from Bright Data — 4 operation(s) for proxies.
  name: Bright Data Proxies API
  slug: bright-data-proxies-api
- description: Trigger and monitor asynchronous scraping jobs.
  name: Bright Data Scrape API
  slug: bright-data-scrape-api
- description: Inspect active Scraping Browser sessions.
  name: Bright Data Sessions API
  slug: bright-data-sessions-api
- description: The Shield API from Bright Data — 4 operation(s) for shield.
  name: Bright Data Shield API
  slug: bright-data-shield-api
- description: The Snapshots API from Bright Data — 6 operation(s) for snapshots.
  name: Bright Data Snapshots API
  slug: bright-data-snapshots-api
- description: The Tokens API from Bright Data — 1 operation(s) for tokens.
  name: Bright Data Tokens API
  slug: bright-data-tokens-api
- description: Submit and retrieve unlock requests.
  name: Bright Data Unlock API
  slug: bright-data-unlock-api
- description: The Zones API from Bright Data — 3 operation(s) for zones.
  name: Bright Data Zones API
  slug: bright-data-zones-api
arazzos:
- description: Inspect a marketplace dataset's metadata, read a snapshot, and deliver it to cloud.
  name: Bright Data Marketplace Dataset Snapshot and Deliver
  slug: bright-data-dataset-marketplace-deliver-workflow
- description: Trigger a Deep Lookup, wait for it to finish, and enrich its columns.
  name: Bright Data Deep Lookup Trigger and Enrich Columns
  slug: bright-data-deep-lookup-enrich-workflow
- description: Preview a Deep Lookup query, trigger it, poll until ready, and download results.
  name: Bright Data Deep Lookup Research and Download
  slug: bright-data-deep-lookup-research-workflow
- description: Create a Web Unlocker zone, confirm it, and run a synchronous unlock against it.
  name: Bright Data Provision an Unlocker Zone then Unlock a URL
  slug: bright-data-provision-unlocker-zone-and-scrape-workflow
- description: Create a zone, confirm it, and allocate dedicated IPs to it.
  name: Bright Data Provision a Zone and Allocate IPs
  slug: bright-data-provision-zone-ips-workflow
- description: Create a proxy port in the local Proxy Manager and read it back to confirm it.
  name: Bright Data Proxy Manager Create and Verify a Port
  slug: bright-data-proxy-port-provision-workflow
- description: Submit an asynchronous SERP request and poll for the parsed search results.
  name: Bright Data Submit SERP Request and Retrieve Results
  slug: bright-data-serp-search-workflow
- description: Submit a Web Archive search, poll it until ready, and deliver the corpus to cloud.
  name: Bright Data Web Archive Search and Deliver
  slug: bright-data-web-archive-search-workflow
- description: Trigger a scrape, wait for the snapshot to finish, and deliver it to cloud storage.
  name: Bright Data Scrape and Deliver Snapshot to Cloud Storage
  slug: bright-data-web-scraper-deliver-workflow
- description: Trigger a Web Scraper collector, poll the snapshot until ready, and download the rows.
  name: Bright Data Trigger Web Scraper Job and Download Results
  slug: bright-data-web-scraper-job-workflow
- description: Read snapshot progress, pull the log on errors, and cancel a job that is still running.
  name: Bright Data Monitor a Snapshot and Cancel a Stuck Job
  slug: bright-data-web-scraper-monitor-cancel-workflow
- description: Inspect an existing snapshot, rerun it when it failed, and poll the new snapshot.
  name: Bright Data Rerun a Failed Snapshot and Monitor It
  slug: bright-data-web-scraper-rerun-workflow
- description: Submit an asynchronous Web Unlocker request and poll for the unlocked response.
  name: Bright Data Submit Async Unlock and Retrieve Result
  slug: bright-data-web-unlocker-async-workflow
artifact_total: 83
collections:
- collection_type: postman
  name: Bright Data Account Management API
  slug: postman-bright-data-account-management-api
- collection_type: postman
  name: Bright Data Dataset Marketplace API
  slug: postman-bright-data-dataset-marketplace-api
- collection_type: postman
  name: Bright Data Deep Lookup API
  slug: postman-bright-data-deep-lookup-api
- collection_type: postman
  name: Bright Data Proxy Manager API
  slug: postman-bright-data-proxy-manager-api
- collection_type: postman
  name: Bright Data Scraping Browser API
  slug: postman-bright-data-scraping-browser-api
- collection_type: postman
  name: Bright Data Scraping Shield API
  slug: postman-bright-data-scraping-shield-api
- collection_type: postman
  name: Bright Data SERP API
  slug: postman-bright-data-serp-api
- collection_type: postman
  name: Bright Data Web Archive API
  slug: postman-bright-data-web-archive-api
- collection_type: postman
  name: Bright Data Web Scraper API
  slug: postman-bright-data-web-scraper-api
- collection_type: postman
  name: Bright Data Web Unlocker API
  slug: postman-bright-data-web-unlocker-api
- collection_type: open
  name: Bright Data Account Management API
  slug: open-bright-data-account-management-api
- collection_type: open
  name: Bright Data Dataset Marketplace API
  slug: open-bright-data-dataset-marketplace-api
- collection_type: open
  name: Bright Data Deep Lookup API
  slug: open-bright-data-deep-lookup-api
- collection_type: open
  name: Bright Data Proxy Manager API
  slug: open-bright-data-proxy-manager-api
- collection_type: open
  name: Bright Data Scraping Browser API
  slug: open-bright-data-scraping-browser-api
- collection_type: open
  name: Bright Data Scraping Shield API
  slug: open-bright-data-scraping-shield-api
- collection_type: open
  name: Bright Data SERP API
  slug: open-bright-data-serp-api
- collection_type: open
  name: Bright Data Web Archive API
  slug: open-bright-data-web-archive-api
- collection_type: open
  name: Bright Data Web Scraper API
  slug: open-bright-data-web-scraper-api
- collection_type: open
  name: Bright Data Web Unlocker API
  slug: open-bright-data-web-unlocker-api
- collection_type: open
  name: Bright Data API (Index)
  slug: open-bright-data
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bright-data-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bright-data-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bright-data-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bright-data/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bright-data-dataset-marketplace-deliver-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bright-data-deep-lookup-enrich-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bright-data-deep-lookup-research-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bright-data-provision-unlocker-zone-and-scrape-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bright-data-provision-zone-ips-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bright-data-proxy-port-provision-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bright-data-serp-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bright-data-web-archive-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bright-data-web-scraper-deliver-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bright-data-web-scraper-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bright-data-web-scraper-monitor-cancel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bright-data-web-scraper-rerun-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bright-data-web-unlocker-async-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://brightdata.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.brightdata.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.brightdata.com/quickstart
- group: start
  title: ''
  type: Signup
  url: https://brightdata.com/cp/start
- group: start
  title: ''
  type: Login
  url: https://brightdata.com/cp/zones
- group: commercial
  title: ''
  type: Pricing
  url: https://brightdata.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/bright-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bright-data-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bright-data-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://brightdata.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brightdata.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brightdata.com/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brightdata.com/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://brightdata.com/trust-center
- group: operate
  title: ''
  type: Support
  url: https://brightdata.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bright-data
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/luminati-io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brightdata
- group: build
  title: ''
  type: SDKs
  url: https://github.com/brightdata/sdk-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/brightdata/sdk-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/brightdata/ai-sdk
- group: other
  title: ''
  type: CommandLineInterface
  url: https://github.com/brightdata/cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/brightdata/brightdata-mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/brightdata/openclaw-plugin
- group: build
  title: ''
  type: Tools
  url: https://github.com/brightdata/brightdata-cursor-plugin
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/brightdata/bright-data-quickstart-templates
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/luminati-io/sbr-examples
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.brightdata.com/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.brightdata.com/api-reference
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/brightdata
created: '2026-03-26'
description: Bright Data is an Israeli web data platform and operator of the world's largest legitimate residential proxy network (400M+ IPs across 195 countries). The platform combines proxy infrastructure (residential, ISP, datacenter, mobile) with higher-level web-access APIs — Web Unlocker, SERP API, Web Scraper API, Scraping Browser, Deep Lookup, and Web Archive — plus a 350-dataset marketplace and an MCP server that exposes 60+ web-access tools to AI agents. Serves 20,000+ customers across eCommerce, finance, real estate, ad-tech, and AI/ML, and is a primary supplier of training and grounding data for foundation-model providers.
features:
- Web Unlocker API — 98%+ success rate single-endpoint unblocking with proxy, JS rendering, CAPTCHA solving, and anti-bot evasion
- SERP API — real-time Google/Bing/Yandex/DuckDuckGo across 31 languages and 195 countries with organic, news, images, video, shopping, jobs, hotels, flights, lens, trends, and AI Overview result types
- Web Scraper API — 660+ pre-built dataset endpoints plus custom collectors with snapshot-based async delivery
- Scraping Browser — managed remote Chromium browsers compatible with Puppeteer, Playwright, and Selenium
- Deep Lookup API — natural-language entity research over 1,000+ sources with 95%+ accuracy
- Web Archive API — petabyte-scale historical web search over 250+ domains
- Dataset Marketplace — 350+ ready-to-use datasets across eCommerce, social, real estate, travel, and business verticals
- Proxy Networks — 400M+ residential IPs, 1.3M+ ISP IPs, datacenter and 7M+ mobile IPs across 195 countries
- Geo-targeting at country, state, city, ZIP, and ASN granularity with sticky and rotating sessions
- Account Management API — programmatic zone, IP, balance, bandwidth, and billing management
- Proxy Manager API — local self-hosted REST control plane (port 22999) for routing, banning, and refreshing
- Scraping Shield API — domain classification API for compliance and trust-and-safety workflows
- MCP Server with 60+ tools, hosted (5,000 free requests/month), self-hosted, or remote
- Direct delivery to Amazon S3, Azure Blob Storage, Google Cloud Storage, Snowflake, and webhooks
- JSON, NDJSON, CSV, XLSX, and Parquet output formats
- Official Python SDK, JavaScript SDK, AI SDK, and CLI
- Pay-only-for-success pricing across Web Unlocker, SERP, and Web Scraper APIs
- 99.99% uptime, 99.95% success rate
- SOC 2 Type II, ISO 27001, GDPR, and CCPA compliant
- Open MCP integrations with Claude Desktop, Claude Code, ChatGPT, Cursor, LangChain, LangGraph, LlamaIndex, CrewAI, n8n, Google ADK, NVIDIA NeMo, Cloudflare Agents, Snowflake Cortex, and Vapi
finops:
- name: Bright Data Finops
  service_category: WebData
  slug: bright-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bright-data.png
json_schemas:
- name: Bright Data Proxy Port
  property_count: 14
  slug: bright-data-proxy-port
- name: Bright Data Snapshot
  property_count: 13
  slug: bright-data-snapshot
- name: Bright Data Zone
  property_count: 12
  slug: bright-data-zone
jsonld:
- class_count: 36
  name: Bright Data Context
  property_count: 1
  slug: bright-data-context
layout: provider
modified: '2026-05-25'
name: Bright Data
nav: Providers
network: true
overview: 'Bright Data publishes 16 APIs on the [APIs.io](https://apis.io/) network, including SERP API, Access API, Archive API, and 13 more. Tagged areas include Web Data, Web Scraping, Proxy, Residential Proxy, and Datacenter Proxy.


  The Bright Data catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Bright Data''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 40 more developer resources.'
plans:
- name: Bright Data Plans Pricing
  plan_count: 17
  slug: bright-data-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 8
  name: Bright Data Rate Limits
  slug: bright-data-rate-limits
rules:
- name: Bright Data API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bright-data-jsonschema-spectral-rules
- name: Bright Data API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 5
  slug: bright-data-rules
score:
  band: strong
  composite: 68.5
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 58.4
    developer_ergonomics: 65.2
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 68.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bright-data/refs/heads/main/screenshots/bright-data-2026-06-20T173659.png
security:
- kind: authentication
  name: Bright Data Authentication
  slug: bright-data-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bright Data Domain Security
  slug: bright-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bright-data
tags:
- Web Data
- Web Scraping
- Proxy
- Residential Proxy
- Datacenter Proxy
- ISP Proxy
- Mobile Proxy
- SERP
- Web Unlocker
- Scraping Browser
- Dataset Marketplace
- MCP
- AI Agents
website: https://brightdata.com
---
