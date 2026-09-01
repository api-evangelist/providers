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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Sfcompute Agentic Access
  operation_count: 25
  slug: sfcompute-agentic-access
  summary_line: 25 operations · 7 acting
api_count: 1
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
- description: The Images API from SF Compute — 5 operation(s) for images.
  name: SF Compute Images API
  slug: sfcompute-images-api
- description: The Money API from SF Compute — 4 operation(s) for money.
  name: SF Compute Money API
  slug: sfcompute-money-api
- description: The VMs API from SF Compute — 5 operation(s) for vms.
  name: SF Compute V Ms API
  slug: sfcompute-vms-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SF Compute API
  slug: open-sf-compute
- collection_type: open
  name: SF Compute Account API
  slug: open-sfcompute-account-api
- collection_type: open
  name: SF Compute Account Balance API
  slug: open-sfcompute-balance-api
- collection_type: open
  name: SF Compute Account Clusters API
  slug: open-sfcompute-clusters-api
- collection_type: open
  name: SF Compute Account Contracts API
  slug: open-sfcompute-contracts-api
- collection_type: open
  name: SF Compute Account Images API
  slug: open-sfcompute-images-api
- collection_type: open
  name: SF Compute Account Money API
  slug: open-sfcompute-money-api
- collection_type: open
  name: SF Compute Account Nodes API
  slug: open-sfcompute-nodes-api
- collection_type: open
  name: SF Compute Account Orders API
  slug: open-sfcompute-orders-api
- collection_type: open
  name: SF Compute Account Prices API
  slug: open-sfcompute-prices-api
- collection_type: open
  name: SF Compute Account VMs API
  slug: open-sfcompute-vms-api
- collection_type: open
  name: SF Compute API
  slug: open-sfcompute
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/sfcompute-capability-edges.yml
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
- group: other
  title: ''
  type: Developer
  url: https://docs.sfcompute.com
- group: start
  title: ''
  type: Signup
  url: https://sfcompute.com/signup
- group: start
  title: ''
  type: Login
  url: https://sfcompute.com/signin
- group: commercial
  title: ''
  type: Pricing
  url: https://sfcompute.com/prices
- group: operate
  title: ''
  type: ChangeLog
  url: https://sfcompute.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://sfcompute.com/contact
- group: build
  title: ''
  type: CLI
  url: https://github.com/sfcompute/cli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sfcompute/nodes-go
- group: other
  title: ''
  type: GPUs
  url: ''
- group: other
  title: ''
  type: Customers
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.sfcompute.com/llms.txt
created: '2026-06-21'
description: SF Compute (San Francisco Compute Company) runs a spot-priced market for very large scale GPU clusters. The api.sfcompute.com REST API lets buyers and sellers place market orders for blocks of H100 GPU-hours, manage tradable cluster contracts, query live market prices, check balances, and provision managed Kubernetes clusters, nodes, and VMs - all driven by the `sf` CLI and language SDKs.
features:
- description: Per-node hourly pricing fluctuates with supply and demand, with no long-term contracts.
  name: Market-Based GPU Pricing
- description: Reserve any number of H100 or H200 nodes for custom durations and start times.
  name: Flexible Node Reservations
- description: Slurm-scheduled clusters available on request for larger training jobs.
  name: Managed Slurm Clusters
- description: Direct bare-metal access for advanced workloads on request.
  name: Bare Metal Clusters
- description: Automatic refunds for failed nodes with hardware-level monitoring.
  name: Hardware Failure Refunds
- description: Cancel or resell unused capacity without penalty.
  name: Cancel Anytime
finops:
- name: Sfcompute Finops
  service_category: Compute
  slug: sfcompute-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sfcompute.png
layout: provider
modified: '2026-08-08'
name: SF Compute
nav: Providers
network: true
overview: 'SF Compute publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Account API, Balance API, Clusters API, and 7 more. Tagged areas include GPU, Compute, Marketplace, H100, and Spot Pricing.


  SF Compute''s developer surface includes authentication, documentation, engineering blog, signup flow, pricing, changelog, support, and 14 more developer resources.'
plans:
- name: Sfcompute Plans Pricing
  plan_count: 3
  slug: sfcompute-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Sfcompute Rate Limits
  slug: sfcompute-rate-limits
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 12
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 56.6
    commercial_clarity: 56.6
    contract_governance: 0.0
    contract_quality: 48.8
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 50.0
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sfcompute/refs/heads/main/screenshots/sfcompute-2026-06-20T193742.png
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
