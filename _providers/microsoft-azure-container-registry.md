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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Microsoft Azure Container Registry Agentic Access
  operation_count: 6
  slug: microsoft-azure-container-registry-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 4
apis:
- baseURL: https://{registry}.azurecr.io/
  baseurl_source: declared
  description: The Blobs API from microsoft-azure-container-registry — 1 operation(s) for blobs.
  name: microsoft-azure-container-registry Blobs API
  slug: microsoft-azure-container-registry-blobs-api
- baseURL: https://{registry}.azurecr.io/
  baseurl_source: declared
  description: The Manifests API from microsoft-azure-container-registry — 1 operation(s) for manifests.
  name: microsoft-azure-container-registry Manifests API
  slug: microsoft-azure-container-registry-manifests-api
- baseURL: https://{registry}.azurecr.io/
  baseurl_source: declared
  description: The Repositories API from microsoft-azure-container-registry — 1 operation(s) for repositories.
  name: microsoft-azure-container-registry Repositories API
  slug: microsoft-azure-container-registry-repositories-api
- baseURL: https://{registry}.azurecr.io/
  baseurl_source: declared
  description: The Tags API from microsoft-azure-container-registry — 1 operation(s) for tags.
  name: microsoft-azure-container-registry Tags API
  slug: microsoft-azure-container-registry-tags-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Container Registry REST Blobs API
  slug: open-microsoft-azure-container-registry-blobs-api
- collection_type: open
  name: Azure Container Registry REST Blobs Manifests API
  slug: open-microsoft-azure-container-registry-manifests-api
- collection_type: open
  name: Azure Container Registry REST Blobs Repositories API
  slug: open-microsoft-azure-container-registry-repositories-api
- collection_type: open
  name: Azure Container Registry REST Blobs Tags API
  slug: open-microsoft-azure-container-registry-tags-api
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
name: Azure Container Registry
nav: Providers
network: true
overview: 'Azure Container Registry publishes 4 APIs on the [APIs.io](https://apis.io/) network, including microsoft-azure-container-registry Blobs API, microsoft-azure-container-registry Manifests API, microsoft-azure-container-registry Repositories API, and 1 more.


  Azure Container Registry''s developer surface includes authentication, developer portal, pricing, documentation, support, and 5 more developer resources.'
plans:
- name: Microsoft Azure Container Registry Plans Pricing
  plan_count: 3
  slug: microsoft-azure-container-registry-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Microsoft Azure Container Registry Rate Limits
  slug: microsoft-azure-container-registry-rate-limits
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 35.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: false
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
