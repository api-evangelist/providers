---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-09-04'
api_count: 3
apis:
- baseURL: https://api.zyte.com/v1
  baseurl_source: declared
  description: 'A single POST /extract operation that retrieves any public URL through Zyte''s automatic ban-avoidance network and returns any combination of raw HTTP body, browser-rendered HTML, screenshots, network '
  name: Zyte API
  slug: zyte
- baseURL: https://zyte-api-stats.zyte.com
  baseurl_source: declared
  description: Read recorded Zyte API usage — request volume, cost, response times and status codes — filtered and grouped by domain, API key label, response code, requested feature, extraction type and customer-sup
  name: Zyte API Stats API
  slug: zyte-stats-api
- description: The HTTP API for Scrapy Cloud, Zyte's hosted platform for running Scrapy spiders. Schedule, stop, update and delete jobs; list and count queued work; read job metadata, logs, requests and scraped item
  name: Scrapy Cloud API
  slug: zyte-scrapy-cloud
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.zyte.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zyte.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zyte.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zyte.com/zyte-api/usage/reference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zyte.com/zyte-api/get-started.html
- group: operate
  title: ''
  type: Support
  url: https://support.zyte.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.zyte.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.zyte.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zytedata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zytedata
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zyte.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.zyte.com/account/signup/zyteapi
- group: start
  title: ''
  type: Login
  url: https://app.zyte.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zyte.com/terms-policies/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zyte.com/terms-policies/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zyte.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zyte-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://www.zyte.com/terms-policies/responsible-disclosure-program/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zyte-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zyte-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/zyte-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zyte-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zyte-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zyte-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zyte-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zyte-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zyte-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zyte-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zyte-finops.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zyte-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zyte-changelog.yml
- group: start
  title: ''
  type: Console
  url: https://app.zyte.com/
- group: build
  title: ''
  type: CLI
  url: cli/zyte-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/zyte-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zyte-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.zyte.com/llms.txt
created: '2026-03-29'
description: 'Zyte (formerly Scrapinghub, the company behind the Scrapy framework) is a web data extraction platform. Its flagship Zyte API is a single POST endpoint that fetches any URL through an automatic anti-ban network, optionally rendering it in a browser, running interaction actions, capturing network traffic and screenshots, and returning AI-extracted structured data for products, articles, job postings, forum threads and search results. Alongside it Zyte runs Scrapy Cloud, a hosted platform for deploying and scheduling Scrapy spiders, a Stats API for usage and spend reporting, and the sunsetting Smart Proxy Manager. Zyte''s agent strategy is Agent Skills rather than MCP: it publishes an official 15-skill "Agentic Web Data" plugin for Claude Code, Codex CLI and GitHub Copilot CLI.'
finops:
- name: Zyte Finops
  service_category: API
  slug: zyte-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zyte.png
layout: provider
modified: '2026-08-29'
name: Zyte
nav: Providers
network: true
overview: 'Zyte publishes 2 APIs on the [APIs.io](https://apis.io/) network, including API Stats API, and 1 more. Tagged areas include Crawling, Data Extraction, Scraping, Web Scraping, and Proxies.


  Zyte''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Zyte Plans Pricing
  plan_count: 5
  slug: zyte-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Zyte Rate Limits
  slug: zyte-rate-limits
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 67.0
    catalog_earned_first_party: 24.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 4.5
    contract_quality: 50.3
    developer_ergonomics: 76.2
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 65.8
  previous_composite: 57.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zyte/refs/heads/main/screenshots/zyte-2026-06-20T202012.png
security:
- kind: authentication
  name: Zyte Authentication
  slug: zyte-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zyte Domain Security
  slug: zyte-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Zyte Vulnerability Disclosure
  slug: zyte-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Zyte Trust Center
  slug: zyte-trust-center
  summary_line: ISO 27001
slug: zyte
tags:
- Crawling
- Data Extraction
- Scraping
- Web Scraping
- Proxies
- Browser Automation
- Anti-Ban
- SERP
- Agent Skills
- Developer Tools
website: https://www.zyte.com/
---
