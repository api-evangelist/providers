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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Azure File Storage Agentic Access
  operation_count: 7
  slug: microsoft-azure-file-storage-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- description: Shares operations
  name: Azure File Storage Shares API
  slug: microsoft-azure-file-storage-shares-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure File Storage REST Shares API
  slug: open-microsoft-azure-file-storage-shares-api
- collection_type: open
  name: Azure File Storage REST API
  slug: open-microsoft-azure-file-storage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-file-storage-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-file-storage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-file-storage-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
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
created: '2026-03-13'
description: The Azure Files FileREST protocol enables software vendors and regular Azure users to efficiently write applications and services that communicate with Azure file shares. It provides fully managed cloud file shares accessible via SMB and NFS protocols, with support for snapshots and Azure File Sync.
finops:
- name: Microsoft Azure File Storage Finops
  service_category: API
  slug: microsoft-azure-file-storage-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-file-storage.png
layout: provider
modified: '2026-05-19'
name: Azure File Storage
nav: Providers
network: true
overview: 'Azure File Storage publishes 1 API on the [APIs.io](https://apis.io/) network: Shares API. Tagged areas include Cloud Storage, File Shares, File Storage, NFS, and SMB.


  Azure File Storage''s developer surface includes authentication, developer portal, pricing, support, and 5 more developer resources.'
plans:
- name: Microsoft Azure File Storage Plans Pricing
  plan_count: 3
  slug: microsoft-azure-file-storage-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Microsoft Azure File Storage Rate Limits
  slug: microsoft-azure-file-storage-rate-limits
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-file-storage/refs/heads/main/screenshots/microsoft-azure-file-storage-2026-06-20T185414.png
security:
- kind: authentication
  name: Microsoft Azure File Storage Authentication
  slug: microsoft-azure-file-storage-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Microsoft Azure File Storage Domain Security
  slug: microsoft-azure-file-storage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-file-storage
tags:
- Cloud Storage
- File Shares
- File Storage
- NFS
- SMB
website: https://portal.azure.com/
---
