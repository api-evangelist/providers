---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-09-25'
api_count: 3
apis:
- description: RESTful web service interface for Sage X3 business objects. Supports standard HTTP methods (GET, POST, PUT, DELETE) for managing entities such as customers, suppliers, sales orders, purchase orders, i
  name: Sage X3 REST Web Services
  slug: sage-x3-rest-web-services
- description: GraphQL interface for querying and mutating Sage X3 data. Provides a flexible, strongly-typed schema for accessing business objects with support for filtering, pagination, and selective field retrieva
  name: Sage X3 GraphQL API
  slug: sage-x3-graphql-api
- description: Import/export and data integration API for Sage X3 enabling bulk data operations, batch task submissions, and asynchronous processing for high-volume data exchange scenarios such as inventory updates,
  name: Sage X3 Data Integration API
  slug: sage-x3-data-integration-api
artifact_total: 10
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sage-x3/refs/heads/main/security/sage-x3-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sage-x3-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sage-x3/refs/heads/main/security/sage-x3-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sage-x3-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sage.com/en-us/products/sage-x3/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sage.com/x3
- group: docs
  title: ''
  type: Documentation
  url: https://online-help.sagex3.com/erp/12/en-us/Content/V7DEV/api-guide_api-reference-guide.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Sage-ERP-X3
- group: company
  title: ''
  type: Blog
  url: https://communityhub.sage.com/us/sage_x3/b
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sage.com/en-us/products/sage-x3/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sage.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/products/sagesoftware-sage-x3
- group: other
  title: ''
  type: X
  url: https://twitter.com/sageerp
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sage-x3/refs/heads/main/plans/sage-x3-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sage-x3-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sage-x3/refs/heads/main/rate-limits/sage-x3-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sage-x3-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sage-x3/refs/heads/main/finops/sage-x3-finops.yml
  title: ''
  type: FinOps
  url: finops/sage-x3-finops.yml
created: '2026-06-13'
description: Sage X3 is an enterprise ERP platform offering REST and GraphQL APIs for managing manufacturing, distribution, financials, and supply chain operations in mid-market and enterprise organizations. It provides web service interfaces for business object integration including sales orders, purchase orders, inventory, accounting, and production management across cloud and on-premise deployments.
finops:
- name: Sage X3 Finops
  service_category: ''
  slug: sage-x3-finops
graphqls:
- description: 'Sage X3 exposes a GraphQL interface through its **Xtrem** middleware layer, which sits between client applications and the X3 ERP engine. The GraphQL endpoint enables flexible, strongly-typed queries '
  name: Sage X3 GraphQL API
  slug: sage-x3-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sage-x3.png
jsonld:
- class_count: 15
  name: Sage X3 Context
  property_count: 24
  slug: sage-x3-context
layout: provider
modified: '2026-06-13'
name: Sage X3
nav: Providers
network: true
overview: 'Sage X3 publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ERP, Manufacturing, Distribution, Supply Chain, and Finance.


  The Sage X3 catalog on APIs.io includes 1 JSON-LD context.


  Sage X3''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Sage X3 Plans Pricing
  plan_count: 2
  slug: sage-x3-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Sage X3 Rate Limits
  slug: sage-x3-rate-limits
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 72.0
    catalog_earned_first_party: 0.0
    catalog_gap: 43.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 37.4
    contract_governance: 0.0
    contract_quality: 46.8
    developer_ergonomics: 11.9
    discoverability: 71.4
    operational_transparency: 41.6
  previous_composite: 35.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/sage-x3/refs/heads/main/screenshots/sage-x3-2026-06-20T193329.png
security:
- kind: domain-security
  name: Sage X3 Domain Security
  slug: sage-x3-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sage X3 Vulnerability Disclosure
  slug: sage-x3-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sage-x3
tags:
- ERP
- Manufacturing
- Distribution
- Supply Chain
- Finance
- Accounting
- Inventory
- Mid-Market
- Enterprise
website: https://www.sage.com/en-us/products/sage-x3/
---
