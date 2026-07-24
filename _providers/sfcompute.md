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
- acting_count: 7
  human_in_the_loop: 0
  name: Sfcompute Agentic Access
  operation_count: 25
  slug: sfcompute-agentic-access
  summary_line: 25 operations · 7 acting
api_count: 7
apis:
- description: The Account API from SF Compute — 4 operation(s) for account.
  name: SF Compute Account API
  slug: sfcompute-account-api
- description: The Balance API from SF Compute — 2 operation(s) for balance.
  name: SF Compute Balance API
  slug: sfcompute-balance-api
- description: The Clusters API from SF Compute — 5 operation(s) for clusters.
  name: SF Compute Clusters API
  slug: sfcompute-clusters-api
- description: The Contracts API from SF Compute — 2 operation(s) for contracts.
  name: SF Compute Contracts API
  slug: sfcompute-contracts-api
- description: The Nodes API from SF Compute — 3 operation(s) for nodes.
  name: SF Compute Nodes API
  slug: sfcompute-nodes-api
- description: The Orders API from SF Compute — 3 operation(s) for orders.
  name: SF Compute Orders API
  slug: sfcompute-orders-api
- description: The Prices API from SF Compute — 1 operation(s) for prices.
  name: SF Compute Prices API
  slug: sfcompute-prices-api
artifact_total: 14
collections:
- collection_type: open
  name: SF Compute API
  slug: open-sfcompute
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sfcompute-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sfcompute-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sfcompute-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sfcompute
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sfcompute
- group: company
  title: ''
  type: Website
  url: https://sfcompute.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sfcompute.com
- group: commercial
  title: ''
  type: Plans
  url: plans/sfcompute-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sfcompute-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sfcompute-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://sfcompute.com/blog
created: '2026-06-21'
description: SF Compute (San Francisco Compute Company) runs a spot-priced market for very large scale GPU clusters. The api.sfcompute.com REST API lets buyers and sellers place market orders for blocks of H100 GPU-hours, manage tradable cluster contracts, query live market prices, check balances, and provision managed Kubernetes clusters, nodes, and VMs - all driven by the `sf` CLI and language SDKs.
finops:
- name: Sfcompute Finops
  service_category: Compute
  slug: sfcompute-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sfcompute.png
layout: provider
modified: '2026-06-21'
name: SF Compute
nav: Providers
network: true
overview: 'SF Compute publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Balance API, Clusters API, and 4 more. Tagged areas include GPU, Compute, Marketplace, H100, and Spot Pricing.


  SF Compute''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Sfcompute Plans Pricing
  plan_count: 3
  slug: sfcompute-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Sfcompute Rate Limits
  slug: sfcompute-rate-limits
score:
  band: thin
  composite: 36.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.3
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Sfcompute Authentication
  slug: sfcompute-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sfcompute Domain Security
  slug: sfcompute-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sfcompute
tags:
- GPU
- Compute
- Marketplace
- H100
- Spot Pricing
website: https://sfcompute.com
---
