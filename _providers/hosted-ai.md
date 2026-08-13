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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.4
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: 'REST API for the Hosted·ai neocloud platform, split into an Admin Panel API (GPUaaS infrastructure: GPU pools, nodes, GPU/NPU hardware discovery, high availability, floating IPs, regions) and a User P'
  name: Hosted·ai Platform API
  slug: hostedai-platform-api
artifact_total: 4
common:
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
  title: ''
  type: Authentication
  url: authentication/hosted-ai-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hosted-ai-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hosted-ai-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/hosted-ai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hosted-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hosted-ai-problem-types.yml
- group: build
  title: ''
  type: Packages
  url: packages/hosted-ai-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hosted-ai-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hosted-ai-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hosted-ai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hosted-ai-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/hosted-ai-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Hosted·ai is a San Jose, California software company (founded 2024, public launch early 2025) providing a turnkey neocloud / GPU-as-a-Service (GPUaaS) platform that lets service providers, telcos and hosts turn NVIDIA GPU fleets into high-margin, multi-tenant AI cloud infrastructure. The platform delivers software-defined GPU orchestration (multi-tenant pooling, adaptive scheduling, GPU overcommit 2x-10x), monetization and neocloud operations (billing, metering, user management, white-label self-service panels), and a GPU Mesh wholesale capacity network. It exposes a full REST API across an Admin Panel API (GPUaaS infrastructure: pools, nodes, GPU/NPU discovery, high availability, floating IPs) and a User Panel API, documented at docs.hosted.ai and Swagger-generated, with bearer API-token authentication, IP allowlisting, and prebuilt integrations for WHMCS, HubSpot and Stripe.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hosted-ai.png
layout: provider
mcp_servers:
- description: ''
  name: hosted-ai-mcp.yml
  slug: hosted-ai-mcpyml
modified: '2026-07-19'
name: Hosted·ai
nav: Providers
network: true
overview: 'Hosted·ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, GPU, GPUaaS, and Cloud Infrastructure.


  Hosted·ai''s developer surface includes documentation, API reference, pricing, support, authentication, changelog, and 15 more developer resources.'
random_paper: 54
score:
  band: emerging
  composite: 24.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 28.9
  previous_composite: 24.5
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hosted-ai/refs/heads/main/screenshots/hosted-ai-2026-07-25T221443.png
security:
- kind: authentication
  name: Hosted Ai Authentication
  slug: hosted-ai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Hosted Ai Domain Security
  slug: hosted-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hosted-ai
tags:
- Company
- Ai
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
