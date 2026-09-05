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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Azure File Storage Agentic Access
  operation_count: 11
  slug: azure-file-storage-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- description: Data-plane HTTPS REST API for operations on file shares, directories, and files in Azure Files, including create, copy, lease, list, range, and snapshot operations. Authentication uses shared key, sha
  name: Azure Files FileREST API
  slug: filerest-api
- description: Azure Resource Manager REST API for managing storage accounts, FileService settings, and FileShare resources at the control-plane level. Authentication uses Microsoft Entra ID OAuth 2.0 bearer tokens.
  name: Azure Storage Resource Provider API (File Services / Shares)
  slug: storage-rp-api
- baseURL: https://{account-name}.file.core.windows.net
  baseurl_source: declared
  description: Account-level file service operations
  name: Azure Files Account API
  slug: azure-file-storage-account-api
- baseURL: https://{account-name}.file.core.windows.net
  baseurl_source: declared
  description: Directory operations within a share
  name: Azure Files Directories API
  slug: azure-file-storage-directories-api
- baseURL: https://{account-name}.file.core.windows.net
  baseurl_source: declared
  description: File operations
  name: Azure Files Files API
  slug: azure-file-storage-files-api
- baseURL: https://{account-name}.file.core.windows.net
  baseurl_source: declared
  description: File share operations
  name: Azure Files Shares API
  slug: azure-file-storage-shares-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Files FileREST Account API
  slug: open-azure-file-storage-account-api
- collection_type: open
  name: Azure Files FileREST Account Directories API
  slug: open-azure-file-storage-directories-api
- collection_type: open
  name: Azure FileREST Account Files API
  slug: open-azure-file-storage-files-api
- collection_type: open
  name: Azure Files FileREST Account Shares API
  slug: open-azure-file-storage-shares-api
- collection_type: open
  name: Azure Files FileREST API
  slug: open-azure-file-storage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-file-storage-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-file-storage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-file-storage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-file-storage-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-file-storage-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/storage/files/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/storage/files/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/storage/files/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=AzureStorageBlog
created: '2026-05-11'
description: Azure Files is a fully managed cloud file share service from Microsoft Azure that provides hosted SMB and NFS file shares accessible from cloud and on-premises clients using standard file system protocols and the FileREST HTTPS API. It supports identity-based authentication via Active Directory and Microsoft Entra ID, snapshots, soft delete, and Azure File Sync for hybrid scenarios. The FileREST data-plane API uses shared key, shared access signatures (SAS), or Microsoft Entra ID OAuth 2.0 bearer tokens for authentication, while the control plane uses Azure Resource Manager.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-file-storage.png
layout: provider
modified: '2026-05-11'
name: Azure Files
nav: Providers
network: true
overview: 'Azure Files publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Directories API, Files API, and 1 more. Tagged areas include Storage, File Storage, File Shares, SMB, and NFS.


  Azure Files'' developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 5 more developer resources.'
random_paper: 8
scopes:
- name: Azure File Storage Scopes
  scope_count: 1
  slug: azure-file-storage-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 51.4
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-file-storage/refs/heads/main/screenshots/azure-file-storage-2026-06-20T172902.png
security:
- kind: authentication
  name: Azure File Storage Authentication
  slug: azure-file-storage-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Azure File Storage Domain Security
  slug: azure-file-storage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Azure File Storage Vulnerability Disclosure
  slug: azure-file-storage-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: azure-file-storage
tags:
- Storage
- File Storage
- File Shares
- SMB
- NFS
- Cloud
- Azure
website: https://azure.microsoft.com/en-us/products/storage/files/
---
