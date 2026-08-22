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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Jarvislabs Agentic Access
  operation_count: 13
  slug: jarvislabs-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 5
apis:
- description: Account balance and status.
  name: JarvisLabs Account API
  slug: jarvislabs-account-api
- description: Persistent storage volumes.
  name: JarvisLabs Filesystems API
  slug: jarvislabs-filesystems-api
- description: GPU type discovery, availability, and pricing.
  name: JarvisLabs GPU Types API
  slug: jarvislabs-gpu-types-api
- description: GPU and CPU instance lifecycle.
  name: JarvisLabs Instances API
  slug: jarvislabs-instances-api
- description: Framework templates available for provisioning.
  name: JarvisLabs Templates API
  slug: jarvislabs-templates-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: JarvisLabs Account API
  slug: open-jarvislabs-account-api
- collection_type: open
  name: JarvisLabs Account Filesystems API
  slug: open-jarvislabs-filesystems-api
- collection_type: open
  name: JarvisLabs Account GPU Types API
  slug: open-jarvislabs-gpu-types-api
- collection_type: open
  name: JarvisLabs Account Instances API
  slug: open-jarvislabs-instances-api
- collection_type: open
  name: JarvisLabs Account Templates API
  slug: open-jarvislabs-templates-api
- collection_type: open
  name: JarvisLabs API
  slug: open-jarvislabs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jarvislabs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jarvislabs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jarvislabs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jarvislabsai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jarvislabs-ai
- group: company
  title: ''
  type: Website
  url: https://jarvislabs.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jarvislabs.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/jarvislabs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jarvislabs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/jarvislabs-finops.yml
created: '2026-06-21'
description: JarvisLabs.ai is a GPU cloud for AI development that lets you launch on-demand GPU and CPU instances (H100, H200, A100, RTX Pro 6000, A6000, A5000, L4, A30) from the terminal. Its Python SDK (jarvislabs / legacy jlclient) and jl CLI wrap an API for the full instance lifecycle - create, pause, resume, and destroy - plus GPU type discovery, framework templates, persistent filesystems, and managed runs for training and inference workloads, billed per minute of compute.
finops:
- name: Jarvislabs Finops
  service_category: Compute and GPU Cloud
  slug: jarvislabs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jarvislabs.png
layout: provider
modified: '2026-06-21'
name: JarvisLabs
nav: Providers
network: true
overview: 'JarvisLabs publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Filesystems API, GPU Types API, and 2 more. Tagged areas include AI, GPU, Cloud, Infrastructure, and Compute.


  JarvisLabs'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Jarvislabs Plans Pricing
  plan_count: 3
  slug: jarvislabs-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Jarvislabs Rate Limits
  slug: jarvislabs-rate-limits
score:
  band: developing
  composite: 39.4
  delta: 0.1
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 61.3
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jarvislabs/refs/heads/main/screenshots/jarvislabs-2026-07-25T223101.png
security:
- kind: authentication
  name: Jarvislabs Authentication
  slug: jarvislabs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Jarvislabs Domain Security
  slug: jarvislabs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jarvislabs
tags:
- AI
- GPU
- Cloud
- Infrastructure
- Compute
website: https://jarvislabs.ai
---
