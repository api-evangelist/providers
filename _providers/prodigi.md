---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Prodigi Agentic Access
  operation_count: 10
  slug: prodigi-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 3
apis:
- description: Create, retrieve, list, and act on print orders.
  name: Prodigi Orders API
  slug: prodigi-orders-api
- description: Query the product catalogue by SKU.
  name: Prodigi Products API
  slug: prodigi-products-api
- description: Request pricing and shipping breakdowns before ordering.
  name: Prodigi Quotes API
  slug: prodigi-quotes-api
artifact_total: 10
collections:
- collection_type: open
  name: Prodigi Print API
  slug: open-prodigi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prodigi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prodigi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prodigi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Prodigi-Group
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prodigi
- group: company
  title: ''
  type: Website
  url: https://www.prodigi.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.prodigi.com/print-api/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/prodigi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prodigi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/prodigi-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.prodigi.com/blog/
created: '2026-06-25'
description: Prodigi is a global print-on-demand and dropshipping platform that connects merchants to a worldwide network of print labs. The Prodigi Print API (v4.0) lets developers create and manage print orders, fetch real-time quotes, and query the product catalogue, with print and shipping fulfilled at wholesale prices direct from the manufacturer.
finops:
- name: Prodigi Finops
  service_category: Print and Fulfillment
  slug: prodigi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prodigi.png
layout: provider
modified: '2026-06-25'
name: Prodigi
nav: Providers
network: true
overview: 'Prodigi publishes 3 APIs on the [APIs.io](https://apis.io/) network: Orders API, Products API, and Quotes API. Tagged areas include Print on Demand, Printing, Dropshipping, Fulfillment, and E-commerce.


  Prodigi''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Prodigi Plans Pricing
  plan_count: 2
  slug: prodigi-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Prodigi Rate Limits
  slug: prodigi-rate-limits
score:
  band: thin
  composite: 35.3
  delta: -2.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 57.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 37.4
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
security:
- kind: authentication
  name: Prodigi Authentication
  slug: prodigi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Prodigi Domain Security
  slug: prodigi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: prodigi
tags:
- Print on Demand
- Printing
- Dropshipping
- Fulfillment
- E-commerce
website: https://www.prodigi.com
---
