---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Repsly Agentic Access
  operation_count: 24
  slug: repsly-agentic-access
  summary_line: 24 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Export and import clients and client notes.
  name: Repsly Clients API
  slug: repsly-clients-api
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Export completed forms and retail audits.
  name: Repsly Forms API
  slug: repsly-forms-api
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Bulk import surface and import job status.
  name: Repsly Import API
  slug: repsly-import-api
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Export photos captured in the field.
  name: Repsly Photos API
  slug: repsly-photos-api
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Export and import pricelists and pricelist items.
  name: Repsly Pricelists API
  slug: repsly-pricelists-api
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Export and import products, product lists, packages, and document types.
  name: Repsly Products API
  slug: repsly-products-api
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Export purchase orders and update sales document status.
  name: Repsly Purchase Orders API
  slug: repsly-purchase-orders-api
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Export representatives, users, and daily working time.
  name: Repsly Representatives API
  slug: repsly-representatives-api
- baseURL: https://api.repsly.com/v3
  baseurl_source: declared
  description: Export visits, visit schedules, and realizations; import schedules.
  name: Repsly Visits API
  slug: repsly-visits-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Repsly Web Clients API
  slug: open-repsly-clients-api
- collection_type: open
  name: Repsly Web Clients Forms API
  slug: open-repsly-forms-api
- collection_type: open
  name: Repsly Web Clients Import API
  slug: open-repsly-import-api
- collection_type: open
  name: Repsly Web Clients Photos API
  slug: open-repsly-photos-api
- collection_type: open
  name: Repsly Web Clients Pricelists API
  slug: open-repsly-pricelists-api
- collection_type: open
  name: Repsly Web Clients Products API
  slug: open-repsly-products-api
- collection_type: open
  name: Repsly Web Clients Purchase Orders API
  slug: open-repsly-purchase-orders-api
- collection_type: open
  name: Repsly Web Clients Representatives API
  slug: open-repsly-representatives-api
- collection_type: open
  name: Repsly Web Clients Visits API
  slug: open-repsly-visits-api
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
random_paper: 20
rate_limits:
- limit_count: 3
  name: Repsly Rate Limits
  slug: repsly-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/repsly/refs/heads/main/screenshots/repsly-2026-09-02T153511.png
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
