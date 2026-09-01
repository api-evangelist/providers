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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Cheerio implements a subset of core jQuery designed for the server. It parses markup into a traversable, manipulable DOM-like data structure and exposes a familiar jQuery-style API for selecting eleme
  name: Cheerio
  slug: cheerio
artifact_total: 37
common:
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
modified: '2026-04-23'
name: Cheerio
nav: Providers
network: true
overview: 'Cheerio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Extraction, DOM, HTML, HTML Parsing, and jQuery.


  The Cheerio catalog on APIs.io includes 1 JSON-LD context.


  Cheerio''s developer surface includes documentation, API reference, tooling, and 8 more developer resources.'
plans:
- name: Cheerio Plans Pricing
  plan_count: 3
  slug: cheerio-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Cheerio Rate Limits
  slug: cheerio-rate-limits
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 7
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cheerio/refs/heads/main/screenshots/cheerio-2026-06-20T174246.png
security:
- kind: domain-security
  name: Cheerio Domain Security
  slug: cheerio-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
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
