---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Typo3 Agentic Access
  operation_count: 23
  slug: typo3-agentic-access
  summary_line: 23 operations · 13 acting
api_count: 6
apis:
- description: The TYPO3 Headless extension provides a JSON API for delivering page content, navigation structures, layouts, and media to decoupled frontend applications. Responds with JSON when the Accept header is
  name: TYPO3 Headless JSON Content API
  slug: headless-json-api
- description: The sourcebroker/t3api extension provides an easy-to-configure REST API layer for TYPO3 Extbase models. APIs are configured with PHP annotations on classes, properties, and methods, with partial suppo
  name: TYPO3 REST API Extension (t3api)
  slug: extension-rest-api
- description: The Cache API from TYPO3 — 2 operation(s) for cache.
  name: TYPO3 Cache API
  slug: typo3-cache-api
- description: The Major API from TYPO3 — 9 operation(s) for major.
  name: TYPO3 Major API
  slug: typo3-major-api
- description: The Release API from TYPO3 — 4 operation(s) for release.
  name: TYPO3 Release API
  slug: typo3-release-api
- description: The sitepackage API from TYPO3 — 1 operation(s) for sitepackage.
  name: TYPO3 sitepackage API
  slug: typo3-sitepackage-api
artifact_total: 13
common:
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


  TYPO3''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Typo3 Plans Pricing
  plan_count: 3
  slug: typo3-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 0
  name: Typo3 Rate Limits
  slug: typo3-rate-limits
score:
  band: thin
  composite: 36.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 49.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
- JSON API
- Open Source
website: https://typo3.org
---
