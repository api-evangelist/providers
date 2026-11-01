---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'REST API for the Hosted·ai neocloud platform, split into an Admin Panel API (GPUaaS infrastructure: GPU pools, nodes, GPU/NPU hardware discovery, high availability, floating IPs, regions) and a User P'
  name: Hosted·ai Platform API
  slug: hostedai-platform-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Blog
  url: https://www.hosted.ai/blog
- group: company
  title: ''
  type: Website
  url: https://hosted.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.hosted.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hosted.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hosted.ai/admin-panel/gpuaas/gpuaas-infrastructure-api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hosted.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hosted.ai/hostedai-privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.hosted.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hosted-ai
- group: auth
  href: https://artifacts.apis.io/hosted-ai/authentication/hosted-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hosted-ai-authentication.yml
- group: operate
  href: https://artifacts.apis.io/hosted-ai/changelog/hosted-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hosted-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/hosted-ai/lifecycle/hosted-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hosted-ai-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/hosted-ai/lifecycle/hosted-ai-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/hosted-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hosted-ai/conventions/hosted-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hosted-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/hosted-ai/errors/hosted-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hosted-ai-problem-types.yml
- group: build
  href: https://artifacts.apis.io/hosted-ai/packages/hosted-ai-packages.yml
  title: ''
  type: Packages
  url: packages/hosted-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/hosted-ai/security/hosted-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hosted-ai-domain-security.yml
- group: design
  href: https://artifacts.apis.io/hosted-ai/conformance/hosted-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hosted-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hosted-ai/mcp/hosted-ai-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/hosted-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/hosted-ai/llms/hosted-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hosted-ai-llms.txt
- group: design
  href: https://artifacts.apis.io/hosted-ai/data-model/hosted-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hosted-ai-data-model.yml
- group: agent
  href: https://artifacts.apis.io/hosted-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Hosted·ai is a San Jose, California software company (founded 2024, public launch early 2025) providing a turnkey neocloud / GPU-as-a-Service (GPUaaS) platform that lets service providers, telcos and hosts turn NVIDIA GPU fleets into high-margin, multi-tenant AI cloud infrastructure. The platform delivers software-defined GPU orchestration (multi-tenant pooling, adaptive scheduling, GPU overcommit 2x-10x), monetization and neocloud operations (billing, metering, user management, white-label self-service panels), and a GPU Mesh wholesale capacity network. It exposes a full REST API across an Admin Panel API (GPUaaS infrastructure: pools, nodes, GPU/NPU discovery, high availability, floating IPs) and a User Panel API, documented at docs.hosted.ai and Swagger-generated, with bearer API-token authentication, IP allowlisting, and prebuilt integrations for WHMCS, HubSpot and Stripe.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hosted-ai.png
layout: provider
modified: '2026-10-06'
name: Hosted·ai
nav: Providers
network: true
overview: 'Hosted·ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, GPU, GPUaaS, and Cloud Infrastructure.


  Hosted·ai''s developer surface includes engineering blog, documentation, API reference, pricing, support, authentication, changelog, and 15 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 47.0
    discoverability: 66.1
    operational_transparency: 28.9
  previous_composite: 25.1
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hosted-ai/hosted-ai-2026-07-25T221443.png
security:
- kind: authentication
  name: Hosted Ai Authentication
  slug: hosted-ai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Hosted Ai Domain Security
  slug: hosted-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Inventory and monitor GPUaaS capacity
  slug: hosted-ai-monitor-gpuaas
- name: Provision a GPU pool on a node
  slug: hosted-ai-provision-gpu-pool
slug: hosted-ai
tags:
- Company
- Artificial Intelligence
- GPU
- GPUaaS
- Cloud Infrastructure
- Neocloud
- Machine Learning
- AI Infrastructure
- Multi-Tenancy
- Service Providers
website: https://hosted.ai/
---
