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
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Scraper Api Agentic Access
  operation_count: 4
  slug: scraper-api-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: ScraperAPI is a web scraping API that manages proxies, browsers, and CAPTCHAs to extract HTML from any web page with a simple API call.
  name: ScraperAPI
  slug: scraper-api
- baseURL: https://api.scraperapi.com
  baseurl_source: spec
  description: The Structured API from ScraperAPI — 2 operation(s) for structured.
  name: ScraperAPI Structured API
  slug: scraper-api-structured-api
- baseURL: https://api.scraperapi.com
  baseurl_source: spec
  description: The Sync API from ScraperAPI — 1 operation(s) for sync.
  name: ScraperAPI Sync API
  slug: scraper-api-sync-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Scraper Structured API
  slug: open-scraper-api-structured-api
- collection_type: open
  name: Scraper Structured Sync API
  slug: open-scraper-api-sync-api
- collection_type: open
  name: ScraperAPI
  slug: open-scraper-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scraper-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scraper-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scraper-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scraperapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scraperapi
- group: company
  title: ''
  type: Website
  url: https://www.scraperapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scraperapi.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://scraperapi.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.scraperapi.com/feed/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-03-29'
description: ScraperAPI is a web scraping API that manages proxies, browsers, and CAPTCHAs to extract HTML from any web page with a simple API call.
finops:
- name: Scraper Api Finops
  service_category: API
  slug: scraper-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scraper-api.png
layout: provider
modified: '2026-08-08'
name: ScraperAPI
nav: Providers
network: true
overview: 'ScraperAPI publishes 2 APIs on the [APIs.io](https://apis.io/) network: Structured API and Sync API. Tagged areas include Data Extraction, Proxies, and Scraping.


  ScraperAPI''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Scraper Api Plans Pricing
  plan_count: 3
  slug: scraper-api-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Scraper Api Rate Limits
  slug: scraper-api-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/scraper-api/refs/heads/main/screenshots/scraper-api-2026-06-20T193553.png
security:
- kind: authentication
  name: Scraper Api Authentication
  slug: scraper-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Scraper Api Domain Security
  slug: scraper-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: scraper-api
tags:
- Data Extraction
- Proxies
- Scraping
website: https://www.scraperapi.com/
---
