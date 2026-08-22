---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Crawlbase Agentic Access
  operation_count: 11
  slug: crawlbase-agentic-access
  summary_line: 11 operations · 4 acting
api_count: 5
apis:
- description: Fetch any URL through the rotating proxy network, optionally rendered.
  name: Crawlbase Crawling API API
  slug: crawlbase-crawling-api-api
- description: Publicly visible email discovery for a domain (legacy).
  name: Crawlbase Leads API API
  slug: crawlbase-leads-api-api
- description: Ready-made structured-data extractors for supported sites (legacy).
  name: Crawlbase Scraper API API
  slug: crawlbase-scraper-api-api
- description: Rendered page screenshots in headless Chrome (legacy).
  name: Crawlbase Screenshots API API
  slug: crawlbase-screenshots-api-api
- description: Retrieve, list, and delete previously stored crawls.
  name: Crawlbase Storage API API
  slug: crawlbase-storage-api-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Crawlbase Crawling API API
  slug: open-crawlbase-crawling-api-api
- collection_type: open
  name: Crawlbase Crawling API Leads API API
  slug: open-crawlbase-leads-api-api
- collection_type: open
  name: Crawlbase Crawling API Scraper API API
  slug: open-crawlbase-scraper-api-api
- collection_type: open
  name: Crawlbase Crawling API Screenshots API API
  slug: open-crawlbase-screenshots-api-api
- collection_type: open
  name: Crawlbase Crawling API Storage API API
  slug: open-crawlbase-storage-api-api
- collection_type: open
  name: Crawlbase API
  slug: open-crawlbase
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crawlbase-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crawlbase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crawlbase-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crawlbase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crawlbase
- group: company
  title: ''
  type: Website
  url: https://crawlbase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://crawlbase.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/crawlbase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crawlbase-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/crawlbase-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://crawlbase.com/blog
created: '2026-07-12'
description: Crawlbase (formerly ProxyCrawl) is a web crawling and scraping platform that fetches any web page through a large rotating proxy network with optional headless-Chrome JavaScript rendering, returning raw HTML, Markdown, screenshots, or structured JSON. A single token-authenticated REST host (api.crawlbase.com) exposes the Crawling API, a Scraper API of ready-made site extractors, Cloud Storage for crawled pages, a Screenshots API, and a Leads API for domain email discovery.
finops:
- name: Crawlbase Finops
  service_category: Web Data and Scraping
  slug: crawlbase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crawlbase.png
layout: provider
modified: '2026-07-12'
name: Crawlbase
nav: Providers
network: true
overview: 'Crawlbase publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Crawling API API, Leads API API, Scraper API API, and 2 more. Tagged areas include Web Scraping, Web Crawling, Web Intelligence, Data Extraction, and Proxy.


  Crawlbase''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Crawlbase Plans Pricing
  plan_count: 10
  slug: crawlbase-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Crawlbase Rate Limits
  slug: crawlbase-rate-limits
score:
  band: thin
  composite: 38.3
  delta: -0.9
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.2
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crawlbase/refs/heads/main/screenshots/crawlbase-2026-07-25T210650.png
security:
- kind: authentication
  name: Crawlbase Authentication
  slug: crawlbase-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Crawlbase Domain Security
  slug: crawlbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crawlbase
tags:
- Web Scraping
- Web Crawling
- Web Intelligence
- Data Extraction
- Proxy
- Scraper API
- Data Collection
- SERP
- Web Data
website: https://crawlbase.com/
---
