---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-02'
api_count: 2
apis:
- baseURL: https://openapi.thordata.com/api/locations
  baseurl_source: declared
  description: Geo-targeting reference data - the countries, states, cities and ASNs available for each proxy product. Read this before setting a country, state or city on any collection call or in a proxy username,
  name: Thordata Locations API
  slug: thordata-locations-api
- baseURL: https://get-ip.thordata.net
  baseurl_source: declared
  description: Pull a batch of proxy endpoints as host:port pairs for the residential or unlimited product, filtered by country, state, city, protocol and session time, returned as plain text or JSON. Used to hand a
  name: Thordata Proxy IP Extract API
  slug: thordata-proxy-ip-extract-api
- baseURL: https://scraperapi.thordata.com
  baseurl_source: declared
  description: Balances and usage statistics
  name: Thordata Account API
  slug: thordata-account-api
- baseURL: https://scraperapi.thordata.com
  baseurl_source: declared
  description: Purchased proxy inventory
  name: Thordata Proxy API
  slug: thordata-proxy-api
- baseURL: https://scraperapi.thordata.com
  baseurl_source: declared
  description: Proxy sub-user lifecycle and per-user usage
  name: Thordata Proxy Users API
  slug: thordata-proxy-users-api
- baseURL: https://scraperapi.thordata.com
  baseurl_source: declared
  description: Real-time search engine results
  name: Thordata SERP API
  slug: thordata-serp-api-api
- baseURL: https://scraperapi.thordata.com
  baseurl_source: declared
  description: Task lifecycle for the Web Scraper API
  name: Thordata Tasks API
  slug: thordata-tasks-api
- baseURL: https://scraperapi.thordata.com
  baseurl_source: declared
  description: Fetch any URL through Thordata's unblocking layer
  name: Thordata Universal Scraping API
  slug: thordata-universal-scraping-api-api
- baseURL: https://scraperapi.thordata.com
  baseurl_source: declared
  description: Pre-built site scrapers launched as asynchronous tasks
  name: Thordata Web Scraper API
  slug: thordata-web-scraper-api-api
- baseURL: https://scraperapi.thordata.com
  baseurl_source: declared
  description: IP whitelisting for password-free proxy authentication
  name: Thordata Whitelist API
  slug: thordata-whitelist-api
artifact_total: 22
asyncapis:
- description: ''
  name: Thordata Web Scraper Webhooks
  slug: thordata-web-scraper-webhooks
collections:
- collection_type: open
  name: Thordata Locations API
  slug: open-thordata-locations-api
- collection_type: open
  name: Thordata Proxy IP Extract API
  slug: open-thordata-proxy-extract-api
- collection_type: open
  name: Thordata Public API
  slug: open-thordata-public-api
- collection_type: open
  name: Thordata Scraper API
  slug: open-thordata-scraper-api
- collection_type: open
  name: Thordata Universal Scraping API / Web Unlocker
  slug: open-thordata-universal-api
- collection_type: open
  name: Thordata Web Scraper API - Tasks
  slug: open-thordata-web-scraper-tasks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/thordata-scraper-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/thordata-serp-search.md
- group: other
  title: ''
  type: Overlay
  url: overlays/thordata-universal-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/thordata-scrape-page.md
- group: other
  title: ''
  type: Overlay
  url: overlays/thordata-web-scraper-tasks-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/thordata-run-scraper-task.md
- group: other
  title: ''
  type: Overlay
  url: overlays/thordata-public-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/thordata-manage-proxy-users.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.thordata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.thordata.com/doc/overview
- group: docs
  title: ''
  type: APIReference
  url: https://thordata.github.io/thordata-sdk-spec/
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.thordata.com/doc/scraping/serp-api/quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://www.thordata.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.thordata.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Thordata
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thordata.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.thordata.com/register
- group: start
  title: ''
  type: Login
  url: https://dashboard.thordata.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thordata.com/service-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thordata.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.thordata.com/security-vulnerabilities-reward-program
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/thordata-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thordata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thordata-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thordata-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/thordata-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thordata-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/thordata-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thordata-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/thordata-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thordata-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/thordata-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/thordata-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/thordata-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/thordata-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/thordata-web-scraper-webhooks.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/thordata-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMSTxt
  url: llms/thordata-llms.txt
- group: agent
  title: ''
  type: LLMSTxt
  url: https://doc.thordata.com/doc/llms.txt
created: '2026-07-23'
description: 'Web data collection infrastructure combining a global proxy network with four HTTP collection APIs. The proxy side spans residential, ISP, datacenter, mobile and high-bandwidth pools reached through a gateway with per-product ports, geo-targeting encoded in the username, and either Basic auth or IP whitelisting. The API side is a SERP API across Google, Bing, Yandex and DuckDuckGo; a Universal Scraping API and Web Unlocker for JavaScript-rendered and blocked pages; a Web Scraper API of pre-built extractors for Amazon, LinkedIn, TikTok, Zillow, Crunchbase and sixteen more sites, run as asynchronous tasks with cron scheduling and webhook callbacks; and a remote Scraping Browser driven over the Chrome DevTools Protocol from Puppeteer, Playwright or Selenium. A public management API covers account balances, proxy inventory, proxy sub-user provisioning with traffic caps, IP whitelisting and geo-targeting reference data. Thordata maintains a canonical cross-language SDK specification
  on GitHub that drives official Python, JavaScript, Go and Java clients, publishes an OpenAPI generated from it, ships an official LangChain tool pack and a Firecrawl-compatible layer, and serves a full markdown documentation index at llms.txt. Billing is prepaid and unusual in one respect that matters to automated consumers: only a 200 response is charged, so failed and empty collections cost nothing.'
image: https://www.thordata.com/logo.png
layout: provider
modified: '2026-08-11'
name: Thordata
nav: Providers
network: true
overview: 'Thordata publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Locations API, Proxy IP Extract API, Account API, and 7 more. Tagged areas include Proxy network, Web Scraping, Data Extraction, SERP, and Search data.


  The Thordata catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Thordata''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Thordata Plans Pricing
  plan_count: 0
  slug: thordata-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Thordata Rate Limits
  slug: thordata-rate-limits
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 21.0
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 37.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thordata/refs/heads/main/screenshots/thordata-2026-08-17T082346.png
security:
- kind: authentication
  name: Thordata Authentication
  slug: thordata-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Thordata Domain Security
  slug: thordata-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Thordata Vulnerability Disclosure
  slug: thordata-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: thordata
tags:
- Proxy network
- Web Scraping
- Data Extraction
- SERP
- Search data
- Web unblocking
- Residential Proxies
- Mobile Proxies
- ISP Proxies
- Datacenter Proxies
- Scraping Browser
- Data-for-AI
- RAG data pipelines
- Web Data
website: https://dashboard.thordata.com/
---
