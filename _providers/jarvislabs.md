---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Jarvislabs Agentic Access
  operation_count: 13
  slug: jarvislabs-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.jarvislabs.ai/v1
  baseurl_source: declared
  description: Account balance and status.
  name: JarvisLabs Account API
  slug: jarvislabs-account-api
- baseURL: https://api.jarvislabs.ai/v1
  baseurl_source: declared
  description: Persistent storage volumes.
  name: JarvisLabs Filesystems API
  slug: jarvislabs-filesystems-api
- baseURL: https://api.jarvislabs.ai/v1
  baseurl_source: declared
  description: GPU type discovery, availability, and pricing.
  name: JarvisLabs GPU Types API
  slug: jarvislabs-gpu-types-api
- baseURL: https://api.jarvislabs.ai/v1
  baseurl_source: declared
  description: GPU and CPU instance lifecycle.
  name: JarvisLabs Instances API
  slug: jarvislabs-instances-api
- baseURL: https://api.jarvislabs.ai/v1
  baseurl_source: declared
  description: Framework templates available for provisioning.
  name: JarvisLabs Templates API
  slug: jarvislabs-templates-api
artifact_total: 18
collections:
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
- group: company
  title: ''
  type: Blog
  url: https://jarvislabs.ai/updates
- group: commercial
  title: ''
  type: Pricing
  url: https://jarvislabs.ai/pricing
- group: other
  href: https://artifacts.apis.io/jarvislabs/capabilities/jarvislabs-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/jarvislabs-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/jarvislabs/agentic-access/jarvislabs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/jarvislabs-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/jarvislabs/security/jarvislabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jarvislabs-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/jarvislabs/authentication/jarvislabs-authentication.yml
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
  href: https://artifacts.apis.io/jarvislabs/plans/jarvislabs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jarvislabs-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/jarvislabs/rate-limits/jarvislabs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jarvislabs-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/jarvislabs/finops/jarvislabs-finops.yml
  title: ''
  type: FinOps
  url: finops/jarvislabs-finops.yml
created: '2026-06-21'
description: JarvisLabs.ai is a GPU cloud for AI development that lets you launch on-demand GPU and CPU instances (H100, H200, A100, RTX Pro 6000, A6000, A5000, L4, A30) from the terminal. Its Python SDK (jarvislabs / legacy jlclient) and jl CLI wrap an API for the full instance lifecycle - create, pause, resume, and destroy - plus GPU type discovery, framework templates, persistent filesystems, and managed runs for training and inference workloads, billed per minute of compute.
finops:
- has_sources: true
  method: generated
  name: Jarvislabs Finops
  primary_unit: ''
  service_category: Compute and GPU Cloud
  slug: jarvislabs-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jarvislabs.png
layout: provider
modified: '2026-10-06'
name: JarvisLabs
nav: Providers
network: true
overview: 'JarvisLabs publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Filesystems API, GPU Types API, and 2 more. Tagged areas include Artificial Intelligence, GPU, Cloud, Infrastructure, and Compute.


  The JarvisLabs catalog on APIs.io includes 1 Spectral governance ruleset.


  JarvisLabs'' developer surface includes engineering blog, pricing, authentication, documentation, and 9 more developer resources.'
plans:
- name: Jarvislabs Plans Pricing
  plan_count: 15
  slug: jarvislabs-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Jarvislabs Rate Limits
  slug: jarvislabs-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: JarvisLabs API Rules
  rule_count: 60
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 1
  slug: jarvislabs-rules
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 54.0
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/jarvislabs/jarvislabs-2026-07-25T223101.png
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
- Artificial Intelligence
- GPU
- Cloud
- Infrastructure
- Compute
website: https://jarvislabs.ai
---
