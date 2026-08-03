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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The Tradogram REST API enables two-way data synchronization between Tradogram and external systems. It provides programmatic access to core procurement modules including purchase orders, requisitions,
  name: Tradogram API
  slug: tradogram-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tradogram-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tradogram.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.tradogram.com/software/integrations
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tradogram
- group: company
  title: ''
  type: Blog
  url: https://www.tradogram.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tradogram.com/pricing
- group: other
  title: ''
  type: X
  url: https://twitter.com/tradogram
- group: commercial
  title: ''
  type: Plans
  url: plans/tradogram-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tradogram-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tradogram-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/tradogram-context.jsonld
created: '2026-06-13'
description: Tradogram is a cloud-based procurement management platform that provides businesses with comprehensive tools to control costs and automate procure-to-pay workflows. The platform enables organizations to manage purchase orders, supplier catalogs, budgets, contracts, and accounts payable through a unified interface. Tradogram exposes a RESTful API at https://api.tradogram.com/v1.0.2 that allows developers to build two-way integrations between Tradogram and external ERP, accounting, or business systems. The API uses API key authentication obtained from the Tradogram dashboard and supports operations across requisitions, purchase orders, sourcing, receiving, invoicing, contracts, and inventory. Tradogram serves small to mid-market teams and enterprises across industries including education, healthcare, and technology seeking structured spend visibility and approval routing without heavyweight ERP complexity.
finops:
- name: Tradogram Finops
  service_category: ''
  slug: tradogram-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tradogram.png
jsonld:
- class_count: 24
  name: Tradogram Context
  property_count: 0
  slug: tradogram-context
layout: provider
modified: '2026-06-13'
name: Tradogram
nav: Providers
network: true
overview: 'Tradogram publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Procurement, Purchase Orders, Supplier Management, Spend Management, and Contracts.


  The Tradogram catalog on APIs.io includes 1 JSON-LD context.


  Tradogram''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Tradogram Plans Pricing
  plan_count: 4
  slug: tradogram-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Tradogram Rate Limits
  slug: tradogram-rate-limits
score:
  band: thin
  composite: 34.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tradogram/refs/heads/main/screenshots/tradogram-2026-06-20T195531.png
security:
- kind: domain-security
  name: Tradogram Domain Security
  slug: tradogram-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tradogram
tags:
- Procurement
- Purchase Orders
- Supplier Management
- Spend Management
- Contracts
- Budgets
- Accounts Payable
- Sourcing
- Inventory
- Procure-to-Pay
website: https://www.tradogram.com
---
