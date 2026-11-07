---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Glew's data pipeline product page says it connects with any data source, including 170+ pre-built integrations, custom integrations via REST API and data table uploads. Glew publishes no public API re
  name: Glew Data Pipeline REST API
  slug: glew-data-pipeline-rest-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/glew/changelog/glew-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/glew-changelog.yml
- group: build
  href: https://artifacts.apis.io/glew/integrations/glew-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/glew-integration-edges.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.glew.io/guides/getting-started-with-ecommerce-tracking-in-google-analytics
- group: commercial
  href: https://artifacts.apis.io/glew/plans/glew-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/glew-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/glew/hosts/glew-hosts.yml
  title: ''
  type: Hosts
  url: hosts/glew-hosts.yml
- group: other
  href: https://artifacts.apis.io/glew/vendors/glew-vendors.yml
  title: ''
  type: Vendors
  url: vendors/glew-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.glew.io/news
- group: auth
  href: https://artifacts.apis.io/glew/security/glew-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/glew-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.glew.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.glew.io/resources
- group: docs
  title: ''
  type: Guides
  url: https://www.glew.io/guides
- group: operate
  title: ''
  type: Support
  url: https://www.glew.io/faqs
- group: company
  title: ''
  type: Blog
  url: https://www.glew.io/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://www.glew.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.glew.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.glew.io/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.glew.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.glew.io/product-updates
- group: company
  title: ''
  type: About
  url: https://www.glew.io/company/about
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/glew
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/glewanalytics
coverage:
  checked: '2026-10-28'
  detail: Glew's data-pipeline page advertises custom integrations via REST API but links no API reference or base URL; /openapi.json and /swagger.json on www.glew.io return 404, and the app host app.glew.io returns 403 AccessDenied for every spec path.
  evidence:
  - status: 404
    url: https://www.glew.io/openapi.json
  - status: 200
    url: https://www.glew.io/products/data-pipeline
  - status: 403
    url: https://app.glew.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Glew is a commerce data platform for ecommerce and multichannel retail brands, merchants and agencies. Its Commerce Data Cloud combines an automated data pipeline (ELT with data validation), a managed commerce data warehouse and Commerce Intelligence reporting (custom reports powered by Looker, daily snapshot emails) across 170+ integrations including Shopify, BigCommerce, Magento, WooCommerce, Salesforce, Klaviyo and TikTok Shop. No public developer API documentation is linked from its site; integrations are configured inside the app at app.glew.io.
image: https://cdn.prod.website-files.com/65b7d3ad3b22fa986d8601e3/667196351e159a02d5f9083f_Commerce%20Data%20Cloud%20(1).png
layout: provider
modified: '2026-10-28'
name: Glew
nav: Providers
network: true
overview: 'Glew is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Analytics, Data Platform, and Retail.


  Glew''s developer surface includes changelog, getting-started guide, documentation, support, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Glew Plans Pricing
  plan_count: 2
  slug: glew-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Glew Rate Limits
  slug: glew-rate-limits
scopes:
- name: Glew Scopes
  scope_count: 0
  slug: glew-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 58.0
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.1
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/glew/glew-2026-11-03T132840.png
security:
- kind: authentication
  name: Glew Authentication
  slug: glew-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Glew Domain Security
  slug: glew-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: glew
tags:
- Company
- E-Commerce
- Analytics
- Data Platform
- Retail
- Business Intelligence
- ETL
- Data Warehouse
- Reporting
website: https://www.glew.io/
---
