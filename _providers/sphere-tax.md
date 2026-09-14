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
- acting_count: 3
  human_in_the_loop: 0
  name: Sphere Tax Agentic Access
  operation_count: 4
  slug: sphere-tax-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- baseURL: https://server.getsphere.com
  baseurl_source: declared
  description: The Tax Calculation API from Sphere — 1 operation(s) for tax calculation.
  name: Sphere Tax Calculation API
  slug: sphere-tax-tax-calculation-api
- baseURL: https://server.getsphere.com
  baseurl_source: declared
  description: The Transactions Export API from Sphere — 3 operation(s) for transactions export.
  name: Sphere Transactions Export API
  slug: sphere-tax-transactions-export-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sphere Tax Tax Calculation API
  slug: open-sphere-tax-tax-calculation-api
- collection_type: open
  name: Sphere Tax Tax Calculation Transactions Export API
  slug: open-sphere-tax-transactions-export-api
- collection_type: open
  name: Sphere Tax API
  slug: open-sphere-tax
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sphere-tax-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sphere-tax-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sphere-tax-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getsphere
- group: company
  title: ''
  type: Website
  url: https://www.getsphere.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getsphere.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/sphere-tax-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sphere-tax-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sphere-tax-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.getsphere.com/blog
created: '2026-06-21'
description: Sphere is a developer-first global indirect tax compliance platform that automates sales tax, VAT, and GST across nexus monitoring, registration, real-time calculation, and filing/remittance. Its REST API lets billing and checkout flows call the Sphere tax engine to calculate tax on transactions and export transaction data, authenticated with an X-API-KEY header.
finops:
- name: Sphere Tax Finops
  service_category: Tax and Compliance
  slug: sphere-tax-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sphere-tax.png
layout: provider
modified: '2026-06-21'
name: Sphere
nav: Providers
network: true
overview: 'Sphere publishes 2 APIs on the [APIs.io](https://apis.io/) network: Tax Calculation API and Transactions Export API. Tagged areas include Tax, Sales Tax, VAT, GST, and Compliance.


  Sphere''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Sphere Tax Plans Pricing
  plan_count: 2
  slug: sphere-tax-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Sphere Tax Rate Limits
  slug: sphere-tax-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/sphere-tax/refs/heads/main/screenshots/sphere-tax-2026-09-02T160620.png
security:
- kind: authentication
  name: Sphere Tax Authentication
  slug: sphere-tax-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sphere Tax Domain Security
  slug: sphere-tax-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sphere-tax
tags:
- Tax
- Sales Tax
- VAT
- GST
- Compliance
- Fintech
website: https://www.getsphere.com/
---
