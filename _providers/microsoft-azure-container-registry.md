---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Microsoft Azure Container Registry Agentic Access
  operation_count: 6
  slug: microsoft-azure-container-registry-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 4
apis:
- description: The Blobs API from microsoft-azure-container-registry — 1 operation(s) for blobs.
  name: microsoft-azure-container-registry Blobs API
  slug: microsoft-azure-container-registry-blobs-api
- description: The Manifests API from microsoft-azure-container-registry — 1 operation(s) for manifests.
  name: microsoft-azure-container-registry Manifests API
  slug: microsoft-azure-container-registry-manifests-api
- description: The Repositories API from microsoft-azure-container-registry — 1 operation(s) for repositories.
  name: microsoft-azure-container-registry Repositories API
  slug: microsoft-azure-container-registry-repositories-api
- description: The Tags API from microsoft-azure-container-registry — 1 operation(s) for tags.
  name: microsoft-azure-container-registry Tags API
  slug: microsoft-azure-container-registry-tags-api
artifact_total: 11
collections:
- collection_type: open
  name: Azure Container Registry REST API
  slug: open-microsoft-azure-container-registry
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-container-registry-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-container-registry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-container-registry-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AzureCR
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
description: 'Azure Container Registry is a managed, private Docker registry service for storing and managing container images, Helm charts, and OCI artifacts. This collection documents the REST APIs for repository management, image distribution, geo-replication, task-based builds, and webhook notifications used across cloud-native workloads. - url: https://azure.microsoft.com/en-us/blog/containers-docker-windows-and-trends/ type: Blog'
finops:
- name: Microsoft Azure Container Registry Finops
  service_category: API
  slug: microsoft-azure-container-registry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-container-registry.png
layout: provider
modified: '2026-05-19'
name: microsoft-azure-container-registry
nav: Providers
network: true
overview: 'microsoft-azure-container-registry publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Blobs API, Manifests API, Repositories API, and 1 more.


  microsoft-azure-container-registry''s developer surface includes authentication, developer portal, pricing, documentation, support, and 5 more developer resources.'
plans:
- name: Microsoft Azure Container Registry Plans Pricing
  plan_count: 3
  slug: microsoft-azure-container-registry-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Microsoft Azure Container Registry Rate Limits
  slug: microsoft-azure-container-registry-rate-limits
score:
  band: thin
  composite: 38.4
  delta: -8.3
  facets:
    commercial_clarity: 47.4
    contract_quality: 56.7
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-container-registry/refs/heads/main/screenshots/microsoft-azure-container-registry-2026-06-20T185406.png
security:
- kind: authentication
  name: Microsoft Azure Container Registry Authentication
  slug: microsoft-azure-container-registry-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Azure Container Registry Domain Security
  slug: microsoft-azure-container-registry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-container-registry
website: https://portal.azure.com/
---
