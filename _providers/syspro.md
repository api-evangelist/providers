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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: SYSPRO OData provides RESTful access to SYSPRO data across all functional modules including inventory, production, purchasing, sales, and financials. It uses basic authentication over HTTPS and suppor
  name: SYSPRO OData API
  slug: syspro-odata-api
- description: SYSPRO e.net Solutions provides a framework for building custom business applications that integrate with SYSPRO using business objects. Business objects are specialized modules with predefined functi
  name: SYSPRO e.net Solutions API
  slug: syspro-enet-solutions-api
- description: The SYSPRO Open Reporting API enables external applications to programmatically call SYSPRO to run and distribute documents. It creates a business object wrapper around standard SYSPRO print programs,
  name: SYSPRO Open Reporting API
  slug: syspro-open-reporting-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/syspro-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/syspro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.syspro.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.syspro.com/documentation/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/topics/syspro
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/syspro
- group: company
  title: ''
  type: Blog
  url: https://www.syspro.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.syspro.com/contact-us/
- group: operate
  title: ''
  type: StatusPage
  url: https://trust.syspro.com/cloud-services/
- group: other
  title: ''
  type: X
  url: https://twitter.com/SYSPRO
- group: commercial
  title: ''
  type: Plans
  url: plans/syspro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/syspro-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/syspro-finops.yml
created: '2026-06-13'
description: SYSPRO is a manufacturing and distribution ERP platform providing a REST API and integration framework for managing production orders, inventory, purchasing, sales, financial accounting, and supply chain operations. The platform supports integration via e.net Solutions business objects, OData RESTful endpoints, and WCF services, enabling ISVs and custom application developers to extend and connect with the SYSPRO ecosystem.
finops:
- name: Syspro Finops
  service_category: ''
  slug: syspro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/syspro.png
layout: provider
modified: '2026-06-13'
name: SYSPRO
nav: Providers
network: true
overview: 'SYSPRO publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ERP, Manufacturing, Distribution, Inventory, and Production Orders.


  SYSPRO''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Syspro Plans Pricing
  plan_count: 3
  slug: syspro-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Syspro Rate Limits
  slug: syspro-rate-limits
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 67.0
    catalog_earned_first_party: 0.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 30.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/syspro/refs/heads/main/screenshots/syspro-2026-06-20T194838.png
security:
- kind: domain-security
  name: Syspro Domain Security
  slug: syspro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Syspro Trust Center
  slug: syspro-trust-center
  summary_line: ISO 27001, GDPR
slug: syspro
tags:
- ERP
- Manufacturing
- Distribution
- Inventory
- Production Orders
- Purchasing
- Sales
- Financial Accounting
- Supply Chain
website: https://www.syspro.com
---
