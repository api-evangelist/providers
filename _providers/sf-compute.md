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
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Sf Compute Agentic Access
  operation_count: 32
  slug: sf-compute-agentic-access
  summary_line: 32 operations · 14 acting
api_count: 7
apis:
- description: The SF Compute Orders API is the REST control plane for placing, listing, and managing orders that reserve GPU node-hours on H100 and H200 clusters. Orders specify node count, duration, and start time
  name: SF Compute Orders API
  slug: orders-api
- description: The Account API from San Francisco Compute Company — 4 operation(s) for account.
  name: San Francisco Compute Company Account API
  slug: sf-compute-account-api
- description: The Images API from San Francisco Compute Company — 5 operation(s) for images.
  name: San Francisco Compute Company Images API
  slug: sf-compute-images-api
- description: The Money API from San Francisco Compute Company — 4 operation(s) for money.
  name: San Francisco Compute Company Money API
  slug: sf-compute-money-api
- description: The Nodes API from San Francisco Compute Company — 6 operation(s) for nodes.
  name: San Francisco Compute Company Nodes API
  slug: sf-compute-nodes-api
- description: The Orders API from San Francisco Compute Company — 2 operation(s) for orders.
  name: San Francisco Compute Company Orders API
  slug: sf-compute-orders-api
- description: The VMs API from San Francisco Compute Company — 5 operation(s) for vms.
  name: San Francisco Compute Company VMs API
  slug: sf-compute-vms-api
artifact_total: 20
collections:
- collection_type: open
  name: SF Compute API
  slug: open-sf-compute
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sf-compute-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sf-compute-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sf-compute-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://sfcompute.com
- group: other
  title: ''
  type: Developer
  url: https://docs.sfcompute.com
- group: docs
  title: ''
  type: Documentation
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
- group: company
  title: ''
  type: Blog
  url: https://sfcompute.com/blog
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
  type: GitHubOrganization
  url: https://github.com/sfcompute
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sf-compute
- group: build
  title: ''
  type: CLI
  url: https://github.com/sfcompute/cli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sfcompute/nodes-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sfcompute/nodes-typescript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sfcompute/sfc-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sfcompute/sfc-sdk-typescript
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
created: '2026-05-23'
description: San Francisco Compute Company (SF Compute) operates a market for buying short-duration time on H100 and H200 GPU clusters with no long-term contracts. Customers reserve VM nodes for any quantity, duration, and start time through the sf CLI and the sfcompute.com Orders API, with managed Slurm and bare-metal clusters available by request.
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
- name: Sf Compute Finops
  service_category: API
  slug: sf-compute-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sf-compute.png
layout: provider
modified: '2026-05-23'
name: San Francisco Compute Company
nav: Providers
network: true
overview: 'San Francisco Compute Company publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Images API, Money API, and 3 more. Tagged areas include AI, Cloud, Clusters, Compute, and GPU.


  San Francisco Compute Company''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, changelog, support, and 13 more developer resources.'
plans:
- name: Sf Compute Plans Pricing
  plan_count: 1
  slug: sf-compute-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 2
  name: Sf Compute Rate Limits
  slug: sf-compute-rate-limits
score:
  band: developing
  composite: 46.5
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 54.3
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sf-compute/refs/heads/main/screenshots/sf-compute-2026-06-20T193742.png
security:
- kind: authentication
  name: Sf Compute Authentication
  slug: sf-compute-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sf Compute Domain Security
  slug: sf-compute-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sf-compute
tags:
- AI
- Cloud
- Clusters
- Compute
- GPU
- Machine Learning
- Marketplace
- Training
website: https://sfcompute.com
---
