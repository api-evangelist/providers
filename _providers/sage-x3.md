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
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-01'
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
  title: ''
  type: VulnerabilityDisclosure
  url: security/sage-x3-vulnerability-disclosure.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/sage-x3-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sage-x3-rate-limits.yml
- group: commercial
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
overview: 'Sage X3 publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ERP, Enterprise Resource Planning, Manufacturing, Distribution, and Supply Chain.


  The Sage X3 catalog on APIs.io includes 1 JSON-LD context.


  Sage X3''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Sage X3 Plans Pricing
  plan_count: 2
  slug: sage-x3-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Sage X3 Rate Limits
  slug: sage-x3-rate-limits
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 41.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 48.9
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 35.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
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
- Enterprise Resource Planning
- Manufacturing
- Distribution
- Supply Chain
- Financials
- Accounting
- Inventory
- Mid-Market
- Enterprise
website: https://www.sage.com/en-us/products/sage-x3/
---
