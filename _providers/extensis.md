---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Extensis Agentic Access
  operation_count: 4
  slug: extensis-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 3
apis:
- description: The Assets API from Extensis — 2 operation(s) for assets.
  name: Extensis Assets API
  slug: extensis-assets-api
- description: The Catalogs API from Extensis — 1 operation(s) for catalogs.
  name: Extensis Catalogs API
  slug: extensis-catalogs-api
- description: The Search API from Extensis — 1 operation(s) for search.
  name: Extensis Search API
  slug: extensis-search-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/extensis-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/extensis-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/extensis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/extensis-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.extensis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.extensis.com/support/developers
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/wags
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/extensis/
- group: company
  title: ''
  type: Blog
  url: https://www.extensis.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.extensis.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.extensis.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/extensis
- group: company
  title: ''
  type: Newsroom
  url: https://www.extensis.com/newsroom
- group: operate
  title: ''
  type: Support
  url: https://www.extensis.com/help-and-support
- group: commercial
  title: ''
  type: Plans
  url: plans/extensis-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/extensis-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/extensis-finops.yml
created: 2026-06-13
description: Digital asset and font management platform with a REST API for organizing and distributing creative assets, managing font licenses, and integrating with design workflows
examples:
- key_count: 4
  name: Get Asset Response
  slug: get-asset-response
- key_count: 1
  name: List Catalogs Response
  slug: list-catalogs-response
- key_count: 4
  name: Search Assets Request
  slug: search-assets-request
- key_count: 1
  name: Search Assets Response
  slug: search-assets-response
finops:
- name: Extensis Finops
  service_category: ''
  slug: extensis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/extensis.png
json_schemas:
- name: Asset
  property_count: 4
  slug: asset
- name: Catalog
  property_count: 2
  slug: catalog
- name: ErrorResponse
  property_count: 3
  slug: error-response
jsonld:
- class_count: 9
  name: Extensis Context
  property_count: 9
  slug: extensis-context
layout: provider
modified: 2026-06-13
name: Extensis
nav: Providers
network: true
overview: 'Extensis publishes 3 APIs on the [APIs.io](https://apis.io/) network: Assets API, Catalogs API, and Search API. Tagged areas include Digital Asset Management, Font Management, Creative Assets, Font Licensing, and Design Workflows.


  The Extensis catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Extensis'' developer surface includes authentication, documentation, engineering blog, pricing, support, and 12 more developer resources.'
plans:
- name: Extensis Plans Pricing
  plan_count: 3
  slug: extensis-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Extensis Rate Limits
  slug: extensis-rate-limits
rules:
- name: Extensis API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: extensis-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.9
  delta: -3.7
  facets:
    commercial_clarity: 57.9
    contract_quality: 63.6
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 52.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/extensis/refs/heads/main/screenshots/extensis-2026-06-20T180946.png
security:
- kind: authentication
  name: Extensis Authentication
  slug: extensis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Extensis Domain Security
  slug: extensis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Extensis Trust Center
  slug: extensis-trust-center
  summary_line: SOC 2, ISO 27001
slug: extensis
tags:
- Digital Asset Management
- Font Management
- Creative Assets
- Font Licensing
- Design Workflows
- DAM
website: https://www.extensis.com/
---
