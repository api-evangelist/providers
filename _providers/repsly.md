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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Repsly Agentic Access
  operation_count: 24
  slug: repsly-agentic-access
  summary_line: 24 operations · 6 acting
api_count: 9
apis:
- description: Export and import clients and client notes.
  name: Repsly Clients API
  slug: repsly-clients-api
- description: Export completed forms and retail audits.
  name: Repsly Forms API
  slug: repsly-forms-api
- description: Bulk import surface and import job status.
  name: Repsly Import API
  slug: repsly-import-api
- description: Export photos captured in the field.
  name: Repsly Photos API
  slug: repsly-photos-api
- description: Export and import pricelists and pricelist items.
  name: Repsly Pricelists API
  slug: repsly-pricelists-api
- description: Export and import products, product lists, packages, and document types.
  name: Repsly Products API
  slug: repsly-products-api
- description: Export purchase orders and update sales document status.
  name: Repsly Purchase Orders API
  slug: repsly-purchase-orders-api
- description: Export representatives, users, and daily working time.
  name: Repsly Representatives API
  slug: repsly-representatives-api
- description: Export visits, visit schedules, and realizations; import schedules.
  name: Repsly Visits API
  slug: repsly-visits-api
artifact_total: 17
collections:
- collection_type: open
  name: Repsly Web API (v3)
  slug: open-repsly
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/repsly-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/repsly-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/repsly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/repsly-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/repsly
- group: company
  title: ''
  type: Website
  url: https://www.repsly.com
- group: docs
  title: ''
  type: Documentation
  url: https://repsly-dev.readme.io/reference/getting-started-1
- group: commercial
  title: ''
  type: Plans
  url: plans/repsly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/repsly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/repsly-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.repsly.com/blog
created: '2026-07-04'
description: Repsly is a retail execution and field sales platform for CPG brands and field teams - covering in-store activity, merchandising, retail audits, order taking, and territory management. The Repsly Web API (v3) is a REST interface at https://api.repsly.com/v3 designed for ERP/CRM integration - it moves clients and products into Repsly (import) and pulls clients, visits, retail audits, forms, photos, purchase orders, pricelists, representatives, and schedules back out (export). Requests use HTTP Basic authentication over SSL, exchange JSON or XML, and paginate export results in batches of up to 50 records using timestamp or last-ID cursors until the response MetaCollectionResult TotalCount reaches zero.
finops:
- name: Repsly Finops
  service_category: Retail Execution and Field Sales Software
  slug: repsly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/repsly.png
layout: provider
modified: '2026-07-04'
name: Repsly
nav: Providers
network: true
overview: 'Repsly publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Clients API, Forms API, Import API, and 6 more. Tagged areas include Retail Execution, Field Sales, Merchandising, CPG, and Retail Audits.


  Repsly''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Repsly Plans Pricing
  plan_count: 2
  slug: repsly-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Repsly Rate Limits
  slug: repsly-rate-limits
score:
  band: thin
  composite: 37.2
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 58.4
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Repsly Authentication
  slug: repsly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Repsly Domain Security
  slug: repsly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Repsly Trust Center
  slug: repsly-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: repsly
tags:
- Retail Execution
- Field Sales
- Merchandising
- CPG
- Retail Audits
- Sales Force Automation
website: https://www.repsly.com
---
