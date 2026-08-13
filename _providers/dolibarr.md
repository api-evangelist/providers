---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: REST API for the Dolibarr ERP/CRM platform providing full CRUD operations on business objects including contacts, invoices, products, orders, projects, banking entries, and HR records. Available on an
  name: Dolibarr REST API
  slug: dolibarr-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dolibarr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dolibarr.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.dolibarr.org/developer-documentation.php
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/dolibarr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/association-dolibarr
- group: company
  title: ''
  type: Blog
  url: https://www.dolibarr.org/#lastnews
- group: commercial
  title: ''
  type: Pricing
  url: https://wiki.dolibarr.org/index.php/Cloud_Solutions_for_Dolibarr_ERP_CRM
- group: operate
  title: ''
  type: StatusPage
  url: https://www.dolibarr.org
- group: other
  title: ''
  type: X
  url: https://x.com/dolibarr
- group: commercial
  title: ''
  type: Plans
  url: plans/dolibarr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dolibarr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dolibarr-finops.yml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/dolibarr.jsonld
created: 2026-06-13
description: Dolibarr is an open-source ERP and CRM platform for businesses, freelancers, and foundations. It provides a REST API for managing contacts, invoices, products, orders, projects, banking, HR, and business module integrations. The API uses standard HTTP methods and JSON, with token-based authentication via the DOLAPIKEY header.
finops:
- name: Dolibarr Finops
  service_category: ''
  slug: dolibarr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dolibarr.png
jsonld:
- class_count: 0
  name: Dolibarr Context
  property_count: 0
  slug: dolibarr
layout: provider
modified: 2026-06-13
name: Dolibarr
nav: Providers
network: true
overview: 'Dolibarr publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include ERP, CRM, Open Source, Invoices, and Contacts.


  The Dolibarr catalog on APIs.io includes 1 JSON-LD context.


  Dolibarr''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Dolibarr Plans Pricing
  plan_count: 3
  slug: dolibarr-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Dolibarr Rate Limits
  slug: dolibarr-rate-limits
score:
  band: emerging
  composite: 22.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 8.1
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 22.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 13.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dolibarr/refs/heads/main/screenshots/dolibarr-2026-06-20T180134.png
security:
- kind: domain-security
  name: Dolibarr Domain Security
  slug: dolibarr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dolibarr
tags:
- ERP
- CRM
- Open Source
- Invoices
- Contacts
- Orders
- Products
- Projects
- Banking
- HR
- Business
website: https://www.dolibarr.org
---
