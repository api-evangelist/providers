---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The HTTP API for Scrapy Cloud, Zyte's hosted platform for running Scrapy spiders. Schedule, stop, update and delete jobs; list and count queued work; read job metadata, logs, requests and scraped item
  name: Scrapy Cloud API
  slug: zyte-scrapy-cloud
- baseURL: https://api.zyte.com/v1
  baseurl_source: declared
  description: The Extract API from Zyte — 1 operation(s) for extract.
  name: Zyte Extract API
  slug: zyte-extract-api
- baseURL: https://api.zyte.com/v1
  baseurl_source: declared
  description: The Stats API from Zyte — 2 operation(s) for stats.
  name: Zyte Stats API
  slug: zyte-stats-api
artifact_total: 27
common:
- group: other
  href: https://artifacts.apis.io/zyte/capabilities/zyte-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/zyte-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/zyte/overlays/zyte-zyte-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zyte-zyte-api-overlay.yaml
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
  href: https://artifacts.apis.io/zyte/lifecycle/zyte-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/zyte-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://www.zyte.com/terms-policies/responsible-disclosure-program/
- group: auth
  href: https://artifacts.apis.io/zyte/security/zyte-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zyte-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/zyte/security/zyte-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zyte-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/zyte/security/zyte-trust-center.yml
  title: ''
  type: Compliance
  url: security/zyte-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/zyte/security/zyte-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zyte-domain-security.yml
- group: design
  href: https://artifacts.apis.io/zyte/conformance/zyte-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zyte-conformance.yml
- group: auth
  href: https://artifacts.apis.io/zyte/authentication/zyte-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zyte-authentication.yml
- group: design
  href: https://artifacts.apis.io/zyte/conventions/zyte-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zyte-conventions.yml
- group: design
  href: https://artifacts.apis.io/zyte/errors/zyte-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zyte-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/zyte/rate-limits/zyte-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zyte-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/zyte/plans/zyte-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zyte-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/zyte/finops/zyte-finops.yml
  title: ''
  type: FinOps
  url: finops/zyte-finops.yml
- group: design
  href: https://artifacts.apis.io/zyte/data-model/zyte-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zyte-data-model.yml
- group: operate
  href: https://artifacts.apis.io/zyte/changelog/zyte-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zyte-changelog.yml
- group: start
  title: ''
  type: Console
  url: https://app.zyte.com/
- group: build
  href: https://artifacts.apis.io/zyte/cli/zyte-cli.yml
  title: ''
  type: CLI
  url: cli/zyte-cli.yml
- group: build
  href: https://artifacts.apis.io/zyte/packages/zyte-packages.yml
  title: ''
  type: Packages
  url: packages/zyte-packages.yml
- group: build
  href: https://artifacts.apis.io/zyte/packages/zyte-packages.yml
  title: ''
  type: SDKs
  url: packages/zyte-packages.yml
- group: agent
  href: https://artifacts.apis.io/zyte/skills/_index.yml
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
- has_sources: true
  method: searched
  name: Zyte Finops
  primary_unit: request
  service_category: API
  slug: zyte-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zyte.png
layout: provider
modified: '2026-08-29'
name: Zyte
nav: Providers
network: true
overview: 'Zyte publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Extract API, Stats API, and 1 more. Tagged areas include Crawling, Data Extraction, Web Scraping, Proxies, and Browser Automation.


  The Zyte catalog on APIs.io includes 1 Spectral governance ruleset.


  Zyte''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Zyte Plans Pricing
  plan_count: 5
  slug: zyte-plans-pricing
- name: Zyte Price Estimates
  plan_count: 0
  slug: zyte-price-estimates
random_paper: 4
rate_limits:
- limit_count: 4
  name: Zyte Rate Limits
  slug: zyte-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Zyte API Rules
  rule_count: 49
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 2
  slug: zyte-rules
score:
  band: exemplar
  composite: 68.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.3
  facets:
    access_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 78.6
    discoverability: 73.2
    operational_transparency: 76.3
  previous_composite: 59.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/zyte/zyte-2026-06-20T202012.png
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
skill_count: 15
skills:
- name: scrape-add-page-object
  slug: zyte-scrape-add-page-object
- name: scrape-analyze-page
  slug: zyte-scrape-analyze-page
- name: scrape-codegen-analyze
  slug: zyte-scrape-codegen-analyze
- name: scrape-codegen-generate
  slug: zyte-scrape-codegen-generate
- name: scrape-codegen
  slug: zyte-scrape-codegen
- name: scrape-create-spider
  slug: zyte-scrape-create-spider
- name: scrape-define
  slug: zyte-scrape-define
- name: scrape-ensure-project
  slug: zyte-scrape-ensure-project
- name: scrape-explore-site
  slug: zyte-scrape-explore-site
- name: scrape-review-schema
  slug: zyte-scrape-review-schema
- name: scrape-scrapy-cloud
  slug: zyte-scrape-scrapy-cloud
- name: scrape-spec
  slug: zyte-scrape-spec
- name: scrape-zyte-api-stats
  slug: zyte-scrape-zyte-api-stats
- name: scrape-zyte-login
  slug: zyte-scrape-zyte-login
- name: scrape
  slug: zyte-scrape
slug: zyte
tags:
- Crawling
- Data Extraction
- Web Scraping
- Proxies
- Browser Automation
- Anti-Ban
- SERP
- Agent Skills
- Developer Tools
website: https://www.zyte.com/
---
