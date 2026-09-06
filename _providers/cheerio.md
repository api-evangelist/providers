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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
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
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Cheerio implements a subset of core jQuery designed for the server. It parses markup into a traversable, manipulable DOM-like data structure and exposes a familiar jQuery-style API for selecting eleme
  name: Cheerio
  slug: cheerio
artifact_total: 38
common:
- group: build
  title: ''
  type: Packages
  url: packages/cheerio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cheerio-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cheerio-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/cheerio-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cheerio-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cheerio-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cheerio-changelog.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cheerio-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cheerio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cheerio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cheerio-finops.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://cheerio.js.org/docs/intro
- group: company
  title: ''
  type: Blog
  url: https://cheerio.js.org/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://cheerio.js.org/blog/rss.xml
- group: operate
  title: ''
  type: Support
  url: https://github.com/cheeriojs/cheerio/discussions
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/cheeriojs/cheerio/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/cheeriojs/cheerio/blob/main/SECURITY.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cheerio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cheerio.js.org/
- group: docs
  title: ''
  type: Documentation
  url: https://cheerio.js.org/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://cheerio.js.org/docs/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cheeriojs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cheeriojs/cheerio
- group: build
  title: ''
  type: NPMPackage
  url: https://www.npmjs.com/package/cheerio
- group: commercial
  title: ''
  type: License
  url: https://github.com/cheeriojs/cheerio/blob/main/LICENSE
- group: operate
  title: ''
  type: Issues
  url: https://github.com/cheeriojs/cheerio/issues
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cheerio-context.jsonld
- group: build
  title: ''
  type: Tools
  url: ''
created: '2026-03-29'
description: Cheerio is a fast, flexible, and elegant Node.js library for parsing and manipulating HTML and XML using a jQuery-compatible API. It is widely used for server-side web scraping, HTML transformation, data extraction, and static site generation. Cheerio is MIT licensed and distributed as the cheerio npm package, maintained under the cheeriojs GitHub organization.
features:
- name: jQuery-Compatible API
- name: Server-Side HTML Parsing
- name: XML Parsing
- name: DOM Traversal
- name: DOM Manipulation
- name: CSS Selector Engine
- name: parse5 Integration
- name: htmlparser2 Integration
- name: Streaming Parser
- name: TypeScript Types
- name: Browser-Compatible Builds
finops:
- name: Cheerio Finops
  service_category: API
  slug: cheerio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cheerio.png
integrations:
- name: Node.js
- name: npm
- name: TypeScript
- name: Bun
- name: Deno
- name: Puppeteer
- name: Playwright
- name: Axios
- name: node-fetch
- name: Got
jsonld:
- class_count: 0
  name: Cheerio Context
  property_count: 3
  slug: cheerio-context
layout: provider
modified: '2026-09-05'
name: Cheerio
nav: Providers
network: true
overview: 'Cheerio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Extraction, DOM, HTML, HTML Parsing, and jQuery.


  The Cheerio catalog on APIs.io includes 1 JSON-LD context.


  Cheerio''s developer surface includes changelog, getting-started guide, engineering blog, support, documentation, API reference, tooling, and 20 more developer resources.'
plans:
- name: Cheerio Plans Pricing
  plan_count: 0
  slug: cheerio-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Cheerio Rate Limits
  slug: cheerio-rate-limits
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 21.7
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cheerio/refs/heads/main/screenshots/cheerio-2026-06-20T174246.png
security:
- kind: domain-security
  name: Cheerio Domain Security
  slug: cheerio-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cheerio Vulnerability Disclosure
  slug: cheerio-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cheerio
tags:
- Data Extraction
- DOM
- HTML
- HTML Parsing
- jQuery
- MIT License
- Node.js
- npm
- Open-Source
- Parser
- Scraping
- Server-Side
- Web Scraping
- XML
use_cases:
- name: Web Scraping
- name: Server-Side HTML Manipulation
- name: Static Site Generation
- name: Data Extraction Pipelines
- name: HTML Email Templating
- name: SEO Auditing Tools
- name: Content Migration
- name: Test HTML Assertions
- name: RSS and Atom Feed Generation
- name: HTML Sanitization Tooling
website: https://cheerio.js.org/
---
