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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Shadeform Agentic Access
  operation_count: 23
  slug: shadeform-agentic-access
  summary_line: 23 operations · 12 acting
api_count: 1
apis:
- baseURL: https://api.shadeform.ai/v1
  baseurl_source: declared
  description: Query standardized instance types, availability, and pricing.
  name: Shadeform Instance Types API
  slug: shadeform-instance-types-api
- baseURL: https://api.shadeform.ai/v1
  baseurl_source: declared
  description: Launch and manage GPU instances across clouds.
  name: Shadeform Instances API
  slug: shadeform-instances-api
- baseURL: https://api.shadeform.ai/v1
  baseurl_source: declared
  description: Manage SSH public keys for instance access.
  name: Shadeform SSH Keys API
  slug: shadeform-ssh-keys-api
- baseURL: https://api.shadeform.ai/v1
  baseurl_source: declared
  description: Save and reuse launch templates.
  name: Shadeform Templates API
  slug: shadeform-templates-api
- baseURL: https://api.shadeform.ai/v1
  baseurl_source: declared
  description: Manage persistent storage volumes.
  name: Shadeform Volumes API
  slug: shadeform-volumes-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shadeform Instance Types API
  slug: open-shadeform-instance-types-api
- collection_type: open
  name: Shadeform Instance Types Instances API
  slug: open-shadeform-instances-api
- collection_type: open
  name: Shadeform Instance Types SSH Keys API
  slug: open-shadeform-ssh-keys-api
- collection_type: open
  name: Shadeform Instance Types Templates API
  slug: open-shadeform-templates-api
- collection_type: open
  name: Shadeform Instance Types Volumes API
  slug: open-shadeform-volumes-api
- collection_type: open
  name: Shadeform API
  slug: open-shadeform
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/shadeform-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shadeform-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shadeform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shadeform-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shadeform
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shadeformai
- group: company
  title: ''
  type: Website
  url: https://www.shadeform.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shadeform.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/shadeform-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shadeform-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shadeform-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://shadeform.com/resources/articles
created: '2026-06-21'
description: Shadeform is a GPU cloud marketplace that exposes a single REST API for deploying and managing GPU compute across many underlying clouds. One interface lets you compare real-time availability and per-GPU-hour pricing, then launch, inspect, restart, and delete instances, attach volumes and SSH keys, and reuse saved launch templates across providers such as Lambda, Nebius, Crusoe, and Hyperstack.
finops:
- name: Shadeform Finops
  service_category: Compute
  slug: shadeform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shadeform.png
layout: provider
modified: '2026-06-21'
name: Shadeform
nav: Providers
network: true
overview: 'Shadeform publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Instance Types API, Instances API, SSH Keys API, and 2 more. Tagged areas include GPU, Cloud, Marketplace, Compute, and Infrastructure.


  Shadeform''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Shadeform Plans Pricing
  plan_count: 2
  slug: shadeform-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Shadeform Rate Limits
  slug: shadeform-rate-limits
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 57.8
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shadeform/refs/heads/main/screenshots/shadeform-2026-09-02T155055.png
security:
- kind: authentication
  name: Shadeform Authentication
  slug: shadeform-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Shadeform Domain Security
  slug: shadeform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shadeform
tags:
- GPU
- Cloud
- Marketplace
- Compute
- Infrastructure
- Artificial Intelligence
website: https://www.shadeform.ai
---
