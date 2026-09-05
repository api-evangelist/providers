---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Typo3 Agentic Access
  operation_count: 23
  slug: typo3-agentic-access
  summary_line: 23 operations · 13 acting
api_count: 1
apis:
- description: The TYPO3 Headless extension provides a JSON API for delivering page content, navigation structures, layouts, and media to decoupled frontend applications. Responds with JSON when the Accept header is
  name: TYPO3 Headless JSON Content API
  slug: headless-json-api
- description: The sourcebroker/t3api extension provides an easy-to-configure REST API layer for TYPO3 Extbase models. APIs are configured with PHP annotations on classes, properties, and methods, with partial suppo
  name: TYPO3 REST API Extension (t3api)
  slug: extension-rest-api
- baseURL: https://example.typo3.org
  baseurl_source: declared
  description: The Cache API from TYPO3 — 2 operation(s) for cache.
  name: TYPO3 Cache API
  slug: typo3-cache-api
- baseURL: https://example.typo3.org
  baseurl_source: declared
  description: The Major API from TYPO3 — 9 operation(s) for major.
  name: TYPO3 Major API
  slug: typo3-major-api
- baseURL: https://example.typo3.org
  baseurl_source: declared
  description: The Release API from TYPO3 — 4 operation(s) for release.
  name: TYPO3 Release API
  slug: typo3-release-api
- baseURL: https://example.typo3.org
  baseurl_source: declared
  description: The sitepackage API from TYPO3 — 1 operation(s) for sitepackage.
  name: TYPO3 sitepackage API
  slug: typo3-sitepackage-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: get.typo3.org Cache API
  slug: open-typo3-cache-api
- collection_type: open
  name: get.typo3.org Cache Major API
  slug: open-typo3-major-api
- collection_type: open
  name: get.typo3.org Cache Release API
  slug: open-typo3-release-api
- collection_type: open
  name: get.typo3.org Cache sitepackage API
  slug: open-typo3-sitepackage-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/TYPO3-Headless/headless/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/TYPO3-Headless/headless/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/TYPO3-Headless/headless/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/TYPO3-Headless/headless/blob/master/CONTRIBUTING.rst
- group: commercial
  title: ''
  type: License
  url: https://github.com/TYPO3-Headless/headless/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/typo3-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/typo3-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/typo3-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://typo3.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.typo3.org
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/TYPO3
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/typo3-gmbh
- group: company
  title: ''
  type: Blog
  url: https://typo3.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://typo3.com/typo3-cms/what-is-typo3/open-source/licenses
- group: operate
  title: ''
  type: StatusPage
  url: https://status.typo3.org
- group: other
  title: ''
  type: X
  url: https://twitter.com/typo3
- group: commercial
  title: ''
  type: Plans
  url: plans/typo3-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/typo3-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/typo3-finops.yml
created: '2026-06-13'
description: TYPO3 is an open-source enterprise PHP content management system providing REST APIs via the TYPO3 Headless extension and get.typo3.org release API for managing pages, content elements, media, navigation, and site configuration. The headless JSON content API delivers structured page and content data to decoupled frontend applications such as PWAs and SPAs.
finops:
- name: Typo3 Finops
  service_category: ''
  slug: typo3-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/typo3.png
jsonld:
- class_count: 10
  name: Typo3 Context
  property_count: 4
  slug: typo3-context
layout: provider
modified: '2026-06-13'
name: TYPO3
nav: Providers
network: true
overview: 'TYPO3 publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cache API, Major API, Release API, and 1 more. Tagged areas include CMS, Content Management, Enterprise, PHP, and Headless.


  The TYPO3 catalog on APIs.io includes 1 JSON-LD context.


  TYPO3''s developer surface includes authentication, documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Typo3 Plans Pricing
  plan_count: 3
  slug: typo3-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Typo3 Rate Limits
  slug: typo3-rate-limits
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 48.8
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 65.0
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/typo3/refs/heads/main/screenshots/typo3-2026-06-20T195907.png
security:
- kind: authentication
  name: Typo3 Authentication
  slug: typo3-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Typo3 Domain Security
  slug: typo3-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: typo3
tags:
- CMS
- Content Management
- Enterprise
- PHP
- Headless
- JSON:API
- Open-Source
website: https://typo3.org
---
