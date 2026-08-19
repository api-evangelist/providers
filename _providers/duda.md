---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Duda Agentic Access
  operation_count: 16
  slug: duda-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 10
apis:
- description: Manage partner and customer accounts
  name: Duda Accounts API
  slug: duda-accounts-api
- description: SSO and access token management
  name: Duda Authentication API
  slug: duda-authentication-api
- description: Manage site blogs and blog posts
  name: Duda Blog API
  slug: duda-blog-api
- description: Manage dynamic data collections
  name: Duda Collections API
  slug: duda-collections-api
- description: Manage eCommerce orders
  name: Duda eCommerce - Orders API
  slug: duda-ecommerce-orders-api
- description: Manage eCommerce products
  name: Duda eCommerce - Products API
  slug: duda-ecommerce-products-api
- description: Create and manage site pages
  name: Duda Pages API
  slug: duda-pages-api
- description: Create, read, update, and delete websites
  name: Duda Sites API
  slug: duda-sites-api
- description: Manage site templates
  name: Duda Templates API
  slug: duda-templates-api
- description: Subscribe to site and account events
  name: Duda Webhooks API
  slug: duda-webhooks-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Duda Partner Accounts API
  slug: open-duda-accounts-api
- collection_type: open
  name: Duda Partner Accounts Authentication API
  slug: open-duda-authentication-api
- collection_type: open
  name: Duda Partner Accounts Blog API
  slug: open-duda-blog-api
- collection_type: open
  name: Duda Partner Accounts Collections API
  slug: open-duda-collections-api
- collection_type: open
  name: Duda Partner Accounts eCommerce - Orders API
  slug: open-duda-ecommerce-orders-api
- collection_type: open
  name: Duda Partner Accounts eCommerce - Products API
  slug: open-duda-ecommerce-products-api
- collection_type: open
  name: Duda Partner Accounts Pages API
  slug: open-duda-pages-api
- collection_type: open
  name: Duda Partner Accounts Sites API
  slug: open-duda-sites-api
- collection_type: open
  name: Duda Partner Accounts Templates API
  slug: open-duda-templates-api
- collection_type: open
  name: Duda Partner Accounts Webhooks API
  slug: open-duda-webhooks-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/DudaDev/partner-api/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/DudaDev/partner-api/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/DudaDev/partner-api/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/duda-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/duda-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/duda-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.duda.co
- group: docs
  title: ''
  type: Documentation
  url: https://developer.duda.co
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/dudadev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/duda
- group: company
  title: ''
  type: Blog
  url: https://blog.duda.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.duda.co/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.duda.co
- group: other
  title: ''
  type: X
  url: https://twitter.com/buildwithduda
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/duda/refs/heads/main/plans/duda-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/duda/refs/heads/main/rate-limits/duda-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/duda/refs/heads/main/finops/duda-finops.yml
created: '2026-06-13'
description: Duda is a professional website builder platform for agencies, SaaS companies, and web professionals. It provides a REST API for creating and managing websites, pages, templates, sections, content, widgets, eCommerce stores, blog posts, dynamic collections, and white-label client portal access. The platform is designed for digital agencies to build and manage websites at scale.
finops:
- name: Duda Finops
  service_category: ''
  slug: duda-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/duda.png
layout: provider
modified: '2026-06-13'
name: Duda
nav: Providers
network: true
overview: 'Duda publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Blog API, and 7 more. Tagged areas include Website Builder, Agencies, White Label, SaaS, and eCommerce.


  Duda''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Duda Plans Pricing
  plan_count: 5
  slug: duda-plans-pricing
random_paper: 116
rate_limits:
- limit_count: 2
  name: Duda Rate Limits
  slug: duda-rate-limits
score:
  band: developing
  composite: 43.4
  delta: -1.5
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 58.5
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/duda/refs/heads/main/screenshots/duda-2026-06-20T180313.png
security:
- kind: authentication
  name: Duda Authentication
  slug: duda-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Duda Domain Security
  slug: duda-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: duda
tags:
- Website Builder
- Agencies
- White Label
- SaaS
- eCommerce
- CMS
website: https://www.duda.co
---
