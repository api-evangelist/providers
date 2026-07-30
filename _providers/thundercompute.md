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
- acting_count: 9
  human_in_the_loop: 0
  name: Thundercompute Agentic Access
  operation_count: 16
  slug: thundercompute-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 8
apis:
- description: The tnr command-line interface is the primary developer surface for Thunder Compute, wrapping the REST API to log in, create, connect to, snapshot, and delete GPU instances and transfer files. Authent
  name: Thunder Compute CLI (tnr)
  slug: thundercompute-cli
- description: The Instances API from Thunder Compute — 6 operation(s) for instances.
  name: Thunder Compute Instances API
  slug: thundercompute-instances-api
- description: The Pricing API from Thunder Compute — 1 operation(s) for pricing.
  name: Thunder Compute Pricing API
  slug: thundercompute-pricing-api
- description: The Snapshots API from Thunder Compute — 3 operation(s) for snapshots.
  name: Thunder Compute Snapshots API
  slug: thundercompute-snapshots-api
- description: The Specs API from Thunder Compute — 1 operation(s) for specs.
  name: Thunder Compute Specs API
  slug: thundercompute-specs-api
- description: The SSH Keys API from Thunder Compute — 3 operation(s) for ssh keys.
  name: Thunder Compute SSH Keys API
  slug: thundercompute-ssh-keys-api
- description: The Templates API from Thunder Compute — 1 operation(s) for templates.
  name: Thunder Compute Templates API
  slug: thundercompute-templates-api
- description: The Tokens API from Thunder Compute — 1 operation(s) for tokens.
  name: Thunder Compute Tokens API
  slug: thundercompute-tokens-api
artifact_total: 15
collections:
- collection_type: open
  name: Thunder Compute API
  slug: open-thundercompute
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thundercompute-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thundercompute-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thundercompute-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Thunder-Compute
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thunder-compute
- group: company
  title: ''
  type: Website
  url: https://www.thundercompute.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.thundercompute.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/thundercompute-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thundercompute-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/thundercompute-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.thundercompute.com/blog
created: '2026-06-21'
description: Thunder Compute is a low-cost GPU cloud offering on-demand virtual GPU instances (T4, A6000, A100 80GB, L40, H100 PCIe) billed per minute. Developers provision and manage instances primarily through the tnr CLI, with a documented REST API at https://api.thundercompute.com:8443/v1 for creating, listing, modifying, and deleting instances, managing snapshots and SSH keys, and reading pricing/specs. A Terraform provider wraps the same API.
finops:
- name: Thundercompute Finops
  service_category: Compute
  slug: thundercompute-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thundercompute.png
layout: provider
modified: '2026-06-21'
name: Thunder Compute
nav: Providers
network: true
overview: 'Thunder Compute publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Instances API, Pricing API, Snapshots API, and 4 more. Tagged areas include GPU, Cloud, Infrastructure, AI, and Compute.


  Thunder Compute''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Thundercompute Plans Pricing
  plan_count: 3
  slug: thundercompute-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 3
  name: Thundercompute Rate Limits
  slug: thundercompute-rate-limits
score:
  band: thin
  composite: 36.3
  delta: -3.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 47.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Thundercompute Authentication
  slug: thundercompute-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Thundercompute Domain Security
  slug: thundercompute-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thundercompute
tags:
- GPU
- Cloud
- Infrastructure
- AI
- Compute
website: https://www.thundercompute.com
---
