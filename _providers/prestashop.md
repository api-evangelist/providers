---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: The PrestaShop Webservice API enables third-party applications to access and manage shop data through CRUD operations on 60+ resources including products, categories, orders, customers, carriers, stoc
  name: PrestaShop Webservice API
  slug: prestashop-webservice-api
- description: The PrestaShop Admin API is a modern REST API introduced in PrestaShop 9 based on API Platform framework using CQRS patterns. It supports OAuth 2.0 client credentials authentication and provides acces
  name: PrestaShop Admin API
  slug: prestashop-admin-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prestashop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.prestashop.com/
- group: docs
  title: ''
  type: Documentation
  url: https://devdocs.prestashop-project.org/9/webservice/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/PrestaShop
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prestashop
- group: company
  title: ''
  type: Blog
  url: https://build.prestashop-project.org/
- group: commercial
  title: ''
  type: Pricing
  url: https://prestashop.com/prestashop-offers/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.prestashop.com/
- group: other
  title: ''
  type: X
  url: https://x.com/PrestaShop
- group: commercial
  title: ''
  type: Plans
  url: plans/prestashop-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prestashop-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/prestashop-finops.yml
created: '2026-06-13'
description: PrestaShop is an open-source e-commerce platform with a REST API for managing products, categories, orders, customers, carriers, stock, and tax rules for online stores. The Webservice API provides full CRUD access to 60+ shop resources using HTTP Basic authentication, while the newer Admin API supports OAuth 2.0 client credentials for programmatic store management.
finops:
- name: Prestashop Finops
  service_category: ''
  slug: prestashop-finops
graphqls:
- description: PrestaShop is an open-source e-commerce platform that exposes its data through a REST/Webservice API and a newer Admin API (PrestaShop 9+). There is no native GraphQL endpoint in PrestaShop's official
  name: PrestaShop GraphQL Schema
  slug: prestashop-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prestashop.png
layout: provider
modified: '2026-06-13'
name: PrestaShop
nav: Providers
network: true
overview: 'PrestaShop publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Open Source, Products, Orders, and Customers.


  PrestaShop''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Prestashop Plans Pricing
  plan_count: 3
  slug: prestashop-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Prestashop Rate Limits
  slug: prestashop-rate-limits
score:
  band: thin
  composite: 33.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 48.1
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 33.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prestashop/refs/heads/main/screenshots/prestashop-2026-06-20T192052.png
security:
- kind: domain-security
  name: Prestashop Domain Security
  slug: prestashop-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: prestashop
tags:
- E-Commerce
- Open Source
- Products
- Orders
- Customers
- Inventory
- Catalog
- Carriers
- Stock
- Tax
website: https://www.prestashop.com/
---
