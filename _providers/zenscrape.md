---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Zenscrape Agentic Access
  operation_count: 2
  slug: zenscrape-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: The Account API from Zenscrape — 1 operation(s) for account.
  name: Zenscrape Account API
  slug: zenscrape-account-api
- description: The Scrape API from Zenscrape — 1 operation(s) for scrape.
  name: Zenscrape Scrape API
  slug: zenscrape-scrape-api
artifact_total: 9
collections:
- collection_type: open
  name: Zenscrape API
  slug: open-zenscrape
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zenscrape-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenscrape-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zenscrape-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zenscrape
- group: company
  title: ''
  type: Website
  url: https://zenscrape.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.zenscrape.com/documentation
- group: commercial
  title: ''
  type: Plans
  url: plans/zenscrape-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zenscrape-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zenscrape-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://zenscrape.com/feed/
created: '2026-06-20'
description: Zenscrape is a web scraping API that returns the rendered HTML of any target URL while handling proxy rotation, headless-browser JavaScript rendering, geotargeting, and Cloudflare protection. A single GET /get request fetches a page through a rotating pool of standard or premium residential proxies, with a /status endpoint for remaining credits and an HTTP proxy-mode interface for existing proxy-based clients.
finops:
- name: Zenscrape Finops
  service_category: Web Scraping and Data Extraction
  slug: zenscrape-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zenscrape.png
layout: provider
modified: '2026-06-20'
name: Zenscrape
nav: Providers
network: true
overview: 'Zenscrape publishes 2 APIs on the [APIs.io](https://apis.io/) network: Account API and Scrape API. Tagged areas include Web Scraping, Proxy, HTML, Data Extraction, and JavaScript Rendering.


  Zenscrape''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Zenscrape Plans Pricing
  plan_count: 5
  slug: zenscrape-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 3
  name: Zenscrape Rate Limits
  slug: zenscrape-rate-limits
score:
  band: thin
  composite: 38.2
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zenscrape/refs/heads/main/screenshots/zenscrape-2026-06-20T201818.png
security:
- kind: authentication
  name: Zenscrape Authentication
  slug: zenscrape-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Zenscrape Domain Security
  slug: zenscrape-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zenscrape
tags:
- Web Scraping
- Proxy
- HTML
- Data Extraction
- JavaScript Rendering
website: https://zenscrape.com/
---
