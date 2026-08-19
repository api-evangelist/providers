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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Brightdata Agentic Access
  operation_count: 8
  slug: brightdata-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 5
apis:
- description: Scraping Browser session metadata (CDP itself is over WebSocket).
  name: Bright Data Browser API API
  slug: brightdata-browser-api-api
- description: Search-engine results via zone-based requests.
  name: Bright Data SERP API
  slug: brightdata-serp-api
- description: Trigger dataset collections and retrieve snapshots.
  name: Bright Data Web Scraper API
  slug: brightdata-web-scraper-api
- description: Single-page unlocking via zone-based requests.
  name: Bright Data Web Unlocker API
  slug: brightdata-web-unlocker-api
- description: Account and proxy zone management.
  name: Bright Data Zones API
  slug: brightdata-zones-api
artifact_total: 20
asyncapis:
- description: 'AsyncAPI 2.6 description of Bright Data''s **Scraping Browser / Browser API** WebSocket surface. Bright Data DOES publish a public WebSocket API. The Scraping Browser is a cloud headless-browser fleet '
  name: Bright Data Scraping Browser (Browser API) - CDP over WebSocket
  slug: brightdata-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bright Data Platform Browser API API
  slug: open-brightdata-browser-api-api
- collection_type: open
  name: Bright Data Platform Browser API SERP API
  slug: open-brightdata-serp-api
- collection_type: open
  name: Bright Data Platform Browser API Web Scraper API
  slug: open-brightdata-web-scraper-api
- collection_type: open
  name: Bright Data Platform Browser API Web Unlocker API
  slug: open-brightdata-web-unlocker-api
- collection_type: open
  name: Bright Data Platform Browser API Zones API
  slug: open-brightdata-zones-api
- collection_type: open
  name: Bright Data Platform API
  slug: open-brightdata
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brightdata-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brightdata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brightdata-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brightdata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bright-data
- group: company
  title: ''
  type: Website
  url: https://brightdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.brightdata.com
- group: commercial
  title: ''
  type: Plans
  url: plans/brightdata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brightdata-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/brightdata-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://brightdata.com/blog
created: '2026-07-12'
description: Bright Data is a web data platform providing a global proxy network (residential, datacenter, ISP, mobile), pre-built Web Scraper APIs for 100+ sites, a SERP API, the Web Unlocker, ready-made Datasets, and a Scraping Browser (Browser API) that exposes a real Chrome DevTools Protocol endpoint over WebSocket for Puppeteer, Playwright, and Selenium automation.
finops:
- name: Brightdata Finops
  service_category: Web Data and Scraping
  slug: brightdata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brightdata.png
layout: provider
modified: '2026-07-12'
name: Bright Data
nav: Providers
network: true
overview: 'Bright Data publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Browser API API, SERP API, Web Scraper API, and 2 more. Tagged areas include Web Data, Web Scraping, Web Intelligence, Proxy, and Data Extraction.


  The Bright Data catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Bright Data''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Brightdata Plans Pricing
  plan_count: 4
  slug: brightdata-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Brightdata Rate Limits
  slug: brightdata-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Bright Data API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: brightdata-asyncapi-spectral-rules
score:
  band: developing
  composite: 42.5
  delta: -5.1
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 65.3
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 34.2
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/brightdata/refs/heads/main/screenshots/brightdata-2026-07-25T203834.png
security:
- kind: authentication
  name: Brightdata Authentication
  slug: brightdata-authentication
  summary_line: http/userPassword · 2 schemes
- kind: domain-security
  name: Brightdata Domain Security
  slug: brightdata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brightdata
tags:
- Web Data
- Web Scraping
- Web Intelligence
- Proxy
- Data Extraction
- SERP
- Web Unlocker
- Datasets
- Data Collection
- Browser Automation
website: https://brightdata.com/
---
