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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Microsoft Azure Blob Storage Agentic Access
  operation_count: 45
  slug: microsoft-azure-blob-storage-agentic-access
  summary_line: 45 operations · 30 acting
api_count: 12
apis:
- description: The Azure Data Lake Storage Gen2 REST APIs allow interaction with Azure Blob Storage through a file system interface. They enable creation and management of file systems, directories, and files on sto
  name: Azure Data Lake Storage Gen2 REST API
  slug: azure-data-lake-storage-gen2-rest-api
- description: Operations specific to append blobs including append block
  name: Azure Blob Storage Append Blobs API
  slug: microsoft-azure-blob-storage-append-blobs-api
- description: The Azure Blob Storage REST API API from Azure Blob Storage — 1 operation(s) for azure blob storage rest api.
  name: Azure Blob Storage Azure Blob Storage REST API API
  slug: microsoft-azure-blob-storage-azure-blob-storage-rest-api-api
- description: Operations on blobs including get, put, delete, and metadata
  name: Azure Blob Storage Blobs API
  slug: microsoft-azure-blob-storage-blobs-api
- description: Operations specific to block blobs including put block and put block list
  name: Azure Blob Storage Block Blobs API
  slug: microsoft-azure-blob-storage-block-blobs-api
- description: The ?comp=blobs API from Azure Blob Storage — 1 operation(s) for ?comp=blobs.
  name: Azure Blob Storage ?comp=blobs API
  slug: microsoft-azure-blob-storage-comp-blobs-api
- description: Operations on blob containers
  name: Azure Blob Storage Containers API
  slug: microsoft-azure-blob-storage-containers-api
- description: Operations specific to page blobs including put page and get page ranges
  name: Azure Blob Storage Page Blobs API
  slug: microsoft-azure-blob-storage-page-blobs-api
- description: The ?restype=service&comp=batch API from Azure Blob Storage — 1 operation(s) for ?restype=service&comp=batch.
  name: Azure Blob Storage ?restype=service&comp=batch API
  slug: microsoft-azure-blob-storage-restype-service-comp-batch-api
- description: The ?restype=service&comp=properties API from Azure Blob Storage — 1 operation(s) for ?restype=service&comp=properties.
  name: Azure Blob Storage ?restype=service&comp=properties API
  slug: microsoft-azure-blob-storage-restype-service-comp-properties-api
- description: The ?restype=service&comp=stats API from Azure Blob Storage — 1 operation(s) for ?restype=service&comp=stats.
  name: Azure Blob Storage ?restype=service&comp=stats API
  slug: microsoft-azure-blob-storage-restype-service-comp-stats-api
- description: The ?restype=service&comp=userdelegationkey API from Azure Blob Storage — 1 operation(s) for ?restype=service&comp=userdelegationkey.
  name: Azure Blob Storage ?restype=service&comp=userdelegationkey API
  slug: microsoft-azure-blob-storage-restype-service-comp-userdelegationkey-api
artifact_total: 29
collections:
- collection_type: open
  name: Azure Blob Storage REST API
  slug: open-azure-blob-storage-rest
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-blob-storage-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-blob-storage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-blob-storage-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/options/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/topics/storage/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/rest/api/storageservices/previous-azure-storage-service-versions
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/storage/blobs/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/rest/api/storageservices/authorize-requests-to-azure-storage
- group: operate
  title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/azure/storage/blobs/scalability-targets
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/storage/blobs/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: start
  title: ''
  type: Console
  url: https://portal.azure.com/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/azure/storage/common/storage-srp-overview
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-blob-storage
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: build
  title: ''
  type: Developer Tools
  url: https://azure.microsoft.com/en-us/products/storage/storage-explorer
- group: auth
  title: ''
  type: Security
  url: https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/storage-security-baseline
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/storage/blobs/
created: '2024'
description: Microsoft Azure Blob Storage is a service for storing large amounts of unstructured object data, such as text or binary data, that can be accessed from anywhere in the world via HTTP or HTTPS.
finops:
- name: Microsoft Azure Blob Storage Finops
  service_category: Storage / Object Storage
  slug: microsoft-azure-blob-storage-finops
image: https://azure.microsoft.com/svghandler/storage-blobs/
json_schemas:
- name: Blob
  property_count: 4
  slug: azure-blob-storage-blob
- name: BlobList
  property_count: 8
  slug: azure-blob-storage-bloblist
- name: Container
  property_count: 3
  slug: azure-blob-storage-container
- name: ContainerList
  property_count: 5
  slug: azure-blob-storage-containerlist
- name: CorsRule
  property_count: 5
  slug: azure-blob-storage-corsrule
- name: Metrics
  property_count: 4
  slug: azure-blob-storage-metrics
- name: RetentionPolicy
  property_count: 2
  slug: azure-blob-storage-retentionpolicy
- name: StorageServiceProperties
  property_count: 7
  slug: azure-blob-storage-storageserviceproperties
json_structures:
- name: Azure Blob Storage Structure
  property_count: 0
  slug: azure-blob-storage-structure
layout: provider
modified: '2026-05-19'
name: Azure Blob Storage
nav: Providers
network: true
overview: 'Azure Blob Storage publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Append Blobs API, Azure Blob Storage REST API API, Blobs API, and 8 more. Tagged areas include Azure, Blobs, Cloud Storage, Microsoft, and Object Storage.


  The Azure Blob Storage catalog on APIs.io includes 1 Spectral governance ruleset.


  Azure Blob Storage''s developer surface includes authentication, developer portal, support, engineering blog, getting-started guide, changelog, documentation, and 16 more developer resources.'
plans:
- name: Microsoft Azure Blob Storage Plans Pricing
  plan_count: 6
  slug: microsoft-azure-blob-storage-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 6
  name: Microsoft Azure Blob Storage Rate Limits
  slug: microsoft-azure-blob-storage-rate-limits
rules:
- name: Azure Blob Storage API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-azure-blob-storage-jsonschema-spectral-rules
score:
  band: strong
  composite: 68.1
  delta: 3.3
  facets:
    commercial_clarity: 71.1
    contract_quality: 57.0
    developer_ergonomics: 58.7
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 78.9
  previous_composite: 64.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-blob-storage/refs/heads/main/screenshots/microsoft-azure-blob-storage-2026-06-20T185402.png
security:
- kind: authentication
  name: Microsoft Azure Blob Storage Authentication
  slug: microsoft-azure-blob-storage-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Microsoft Azure Blob Storage Domain Security
  slug: microsoft-azure-blob-storage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-blob-storage
tags:
- Azure
- Blobs
- Cloud Storage
- Microsoft
- Object Storage
- Storage
website: https://azure.microsoft.com/en-us/products/storage/blobs/
---
