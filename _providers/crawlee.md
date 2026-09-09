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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.1
  scored_at: '2026-09-08'
api_count: 2
apis:
- description: The Crawlee JavaScript SDK is a Node.js/TypeScript library for building reliable web scrapers and crawlers. It provides a family of crawler classes - BasicCrawler, HttpCrawler, CheerioCrawler, JSDOMCr
  name: Crawlee JavaScript SDK
  slug: crawlee-javascript-sdk
- description: The Crawlee Python SDK is a Python library for building reliable web scrapers and crawlers. It offers BasicCrawler, HttpCrawler, BeautifulSoupCrawler, ParselCrawler, PlaywrightCrawler, and Adaptive cr
  name: Crawlee Python SDK
  slug: crawlee-python-sdk
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apify/crawlee/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apify/crawlee/blob/master/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crawlee-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apify
- group: company
  title: ''
  type: Website
  url: https://crawlee.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://crawlee.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apify
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apify/crawlee
- group: company
  title: ''
  type: Blog
  url: https://crawlee.dev/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/apify/crawlee/releases
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/jyEM2PRvMU
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/jyEM2PRvMU
- group: commercial
  title: ''
  type: License
  url: https://github.com/apify/crawlee/blob/master/LICENSE.md
- group: other
  title: ''
  type: Apify
  url: https://apify.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://crawlee.dev/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crawlee-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/crawlee-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/crawlee-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/crawlee-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/crawlee-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crawlee-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/crawlee-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crawlee-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crawlee-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2025-02-08'
description: Crawlee is an open-source web scraping and crawling library maintained by Apify, providing a unified set of crawler classes, request queues, datasets, and key-value stores for building reliable scrapers. It is available for both JavaScript/TypeScript (Node.js) and Python, offering HTTP, Cheerio, JSDOM, LinkeDOM, Puppeteer, Playwright, and Stagehand crawler implementations along with proxy and session management utilities for production-grade scraping.
finops:
- name: Crawlee Finops
  service_category: Open Source Library
  slug: crawlee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crawlee.png
layout: provider
modified: '2026-09-07'
name: Crawlee
nav: Providers
network: true
overview: 'Crawlee publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Apache 2.0, Apify, Browser Automation, Crawlers, and Harvesting.


  Crawlee''s developer surface includes documentation, engineering blog, changelog, CLI, and 21 more developer resources.'
plans:
- name: Crawlee Plans Pricing
  plan_count: 0
  slug: crawlee-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Crawlee Rate Limits
  slug: crawlee-rate-limits
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 26.7
  provenance:
    conformance: first-party
    mcp: derived
    skills: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/crawlee/refs/heads/main/screenshots/crawlee-2026-06-20T175215.png
security:
- kind: domain-security
  name: Crawlee Domain Security
  slug: crawlee-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: crawlee
tags:
- Apache 2.0
- Apify
- Browser Automation
- Crawlers
- Harvesting
- JavaScript
- Node.js
- Open-Source
- Playwright
- Puppeteer
- Python
- Scraping
- Web
website: https://crawlee.dev/
---
