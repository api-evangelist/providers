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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 26
  human_in_the_loop: 1
  name: Azure Storage Accounts Agentic Access
  operation_count: 40
  slug: azure-storage-accounts-agentic-access
  summary_line: 40 operations · 26 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: The BlobContainers API from Azure Storage Accounts — 8 operation(s) for blobcontainers.
  name: Azure Storage Accounts BlobContainers API
  slug: azure-storage-accounts-blobcontainers-api
- description: The BlobService API from Azure Storage Accounts — 2 operation(s) for blobservice.
  name: Azure Storage Accounts BlobService API
  slug: azure-storage-accounts-blobservice-api
- description: The LocationUsage API from Azure Storage Accounts — 1 operation(s) for locationusage.
  name: Azure Storage Accounts LocationUsage API
  slug: azure-storage-accounts-locationusage-api
- description: The ManagementPolicies API from Azure Storage Accounts — 1 operation(s) for managementpolicies.
  name: Azure Storage Accounts ManagementPolicies API
  slug: azure-storage-accounts-managementpolicies-api
- description: The Operations API from Azure Storage Accounts — 1 operation(s) for operations.
  name: Azure Storage Accounts Operations API
  slug: azure-storage-accounts-operations-api
- description: The PrivateEndpointConnections API from Azure Storage Accounts — 1 operation(s) for privateendpointconnections.
  name: Azure Storage Accounts PrivateEndpointConnections API
  slug: azure-storage-accounts-privateendpointconnections-api
- description: The PrivateLinkResources API from Azure Storage Accounts — 1 operation(s) for privatelinkresources.
  name: Azure Storage Accounts PrivateLinkResources API
  slug: azure-storage-accounts-privatelinkresources-api
- description: The Skus API from Azure Storage Accounts — 1 operation(s) for skus.
  name: Azure Storage Accounts Skus API
  slug: azure-storage-accounts-skus-api
- description: The StorageAccounts API from Azure Storage Accounts — 11 operation(s) for storageaccounts.
  name: Azure Storage Accounts StorageAccounts API
  slug: azure-storage-accounts-storageaccounts-api
artifact_total: 157
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-storage-accounts-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-storage-accounts-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-storage-accounts-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-storage-accounts-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Storage%2FStorageAccounts
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/storage/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/rest/api/storageservices/authorize-requests-to-azure-storage
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/azure/storage/common/storage-apis-and-sdks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/azure-storage-accounts/refs/heads/main/rules/azure-storage-accounts-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/azure-storage-accounts/refs/heads/main/vocabulary/azure-storage-accounts-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/azure-storage-accounts/refs/heads/main/json-ld/azure-storage-accounts-context.jsonld
created: '2024-01-01'
description: Azure Storage is Microsoft's cloud storage solution for modern data storage scenarios offering highly available, massively scalable, durable, and secure storage for blobs, files, queues, tables, and disks.
examples:
- key_count: 8
  name: Azure Storage Accounts Account Sas Parameters Example
  slug: azure-storage-accounts-account-sas-parameters-example
- key_count: 6
  name: Azure Storage Accounts Active Directory Properties Example
  slug: azure-storage-accounts-active-directory-properties-example
- key_count: 1
  name: Azure Storage Accounts Azure Files Identity Based Authentication Example
  slug: azure-storage-accounts-azure-files-identity-based-authentication-example
- key_count: 0
  name: Azure Storage Accounts Blob Container Example
  slug: azure-storage-accounts-blob-container-example
- key_count: 2
  name: Azure Storage Accounts Blob Restore Parameters Example
  slug: azure-storage-accounts-blob-restore-parameters-example
- key_count: 2
  name: Azure Storage Accounts Blob Restore Range Example
  slug: azure-storage-accounts-blob-restore-range-example
- key_count: 3
  name: Azure Storage Accounts Blob Restore Status Example
  slug: azure-storage-accounts-blob-restore-status-example
- key_count: 1
  name: Azure Storage Accounts Blob Service Items Example
  slug: azure-storage-accounts-blob-service-items-example
- key_count: 2
  name: Azure Storage Accounts Blob Service Properties Example
  slug: azure-storage-accounts-blob-service-properties-example
- key_count: 1
  name: Azure Storage Accounts Change Feed Example
  slug: azure-storage-accounts-change-feed-example
- key_count: 3
  name: Azure Storage Accounts Check Name Availability Result Example
  slug: azure-storage-accounts-check-name-availability-result-example
- key_count: 8
  name: Azure Storage Accounts Container Properties Example
  slug: azure-storage-accounts-container-properties-example
- key_count: 2
  name: Azure Storage Accounts Custom Domain Example
  slug: azure-storage-accounts-custom-domain-example
- key_count: 1
  name: Azure Storage Accounts Date After Creation Example
  slug: azure-storage-accounts-date-after-creation-example
- key_count: 1
  name: Azure Storage Accounts Date After Modification Example
  slug: azure-storage-accounts-date-after-modification-example
- key_count: 2
  name: Azure Storage Accounts Dimension Example
  slug: azure-storage-accounts-dimension-example
- key_count: 1
  name: Azure Storage Accounts Encryption Example
  slug: azure-storage-accounts-encryption-example
- key_count: 3
  name: Azure Storage Accounts Encryption Service Example
  slug: azure-storage-accounts-encryption-service-example
- key_count: 0
  name: Azure Storage Accounts Encryption Services Example
  slug: azure-storage-accounts-encryption-services-example
- key_count: 6
  name: Azure Storage Accounts Endpoints Example
  slug: azure-storage-accounts-endpoints-example
- key_count: 3
  name: Azure Storage Accounts Geo Replication Stats Example
  slug: azure-storage-accounts-geo-replication-stats-example
- key_count: 3
  name: Azure Storage Accounts Identity Example
  slug: azure-storage-accounts-identity-example
- key_count: 0
  name: Azure Storage Accounts Immutability Policy Example
  slug: azure-storage-accounts-immutability-policy-example
- key_count: 2
  name: Azure Storage Accounts Immutability Policy Properties Example
  slug: azure-storage-accounts-immutability-policy-properties-example
- key_count: 2
  name: Azure Storage Accounts Immutability Policy Property Example
  slug: azure-storage-accounts-immutability-policy-property-example
- key_count: 2
  name: Azure Storage Accounts Ip Rule Example
  slug: azure-storage-accounts-ip-rule-example
- key_count: 3
  name: Azure Storage Accounts Key Vault Properties Example
  slug: azure-storage-accounts-key-vault-properties-example
- key_count: 5
  name: Azure Storage Accounts Lease Container Request Example
  slug: azure-storage-accounts-lease-container-request-example
- key_count: 2
  name: Azure Storage Accounts Lease Container Response Example
  slug: azure-storage-accounts-lease-container-response-example
- key_count: 2
  name: Azure Storage Accounts Legal Hold Example
  slug: azure-storage-accounts-legal-hold-example
- key_count: 2
  name: Azure Storage Accounts Legal Hold Properties Example
  slug: azure-storage-accounts-legal-hold-properties-example
- key_count: 1
  name: Azure Storage Accounts List Account Sas Response Example
  slug: azure-storage-accounts-list-account-sas-response-example
- key_count: 0
  name: Azure Storage Accounts List Container Item Example
  slug: azure-storage-accounts-list-container-item-example
- key_count: 2
  name: Azure Storage Accounts List Container Items Example
  slug: azure-storage-accounts-list-container-items-example
- key_count: 1
  name: Azure Storage Accounts List Service Sas Response Example
  slug: azure-storage-accounts-list-service-sas-response-example
- key_count: 0
  name: Azure Storage Accounts Management Policy Action Example
  slug: azure-storage-accounts-management-policy-action-example
- key_count: 0
  name: Azure Storage Accounts Management Policy Base Blob Example
  slug: azure-storage-accounts-management-policy-base-blob-example
- key_count: 0
  name: Azure Storage Accounts Management Policy Definition Example
  slug: azure-storage-accounts-management-policy-definition-example
- key_count: 0
  name: Azure Storage Accounts Management Policy Example
  slug: azure-storage-accounts-management-policy-example
- key_count: 2
  name: Azure Storage Accounts Management Policy Filter Example
  slug: azure-storage-accounts-management-policy-filter-example
- key_count: 1
  name: Azure Storage Accounts Management Policy Properties Example
  slug: azure-storage-accounts-management-policy-properties-example
- key_count: 3
  name: Azure Storage Accounts Management Policy Rule Example
  slug: azure-storage-accounts-management-policy-rule-example
- key_count: 1
  name: Azure Storage Accounts Management Policy Schema Example
  slug: azure-storage-accounts-management-policy-schema-example
- key_count: 2
  name: Azure Storage Accounts Restore Policy Properties Example
  slug: azure-storage-accounts-restore-policy-properties-example
- key_count: 5
  name: Azure Storage Accounts Tag Property Example
  slug: azure-storage-accounts-tag-property-example
- key_count: 6
  name: Azure Storage Accounts Update History Property Example
  slug: azure-storage-accounts-update-history-property-example
finops:
- name: Azure Storage Accounts Finops
  service_category: API
  slug: azure-storage-accounts-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-storage-accounts.png
json_schemas:
- name: AccountSasParameters
  property_count: 8
  slug: azure-storage-accounts-account-sas-parameters
- name: ActiveDirectoryProperties
  property_count: 6
  slug: azure-storage-accounts-active-directory-properties
- name: AzureFilesIdentityBasedAuthentication
  property_count: 2
  slug: azure-storage-accounts-azure-files-identity-based-authentication
- name: BlobContainer
  property_count: 1
  slug: azure-storage-accounts-blob-container
- name: BlobRestoreParameters
  property_count: 2
  slug: azure-storage-accounts-blob-restore-parameters
- name: BlobRestoreRange
  property_count: 2
  slug: azure-storage-accounts-blob-restore-range
- name: BlobRestoreStatus
  property_count: 4
  slug: azure-storage-accounts-blob-restore-status
- name: BlobServiceItems
  property_count: 1
  slug: azure-storage-accounts-blob-service-items
- name: BlobServiceProperties
  property_count: 2
  slug: azure-storage-accounts-blob-service-properties
- name: ChangeFeed
  property_count: 1
  slug: azure-storage-accounts-change-feed
- name: CheckNameAvailabilityResult
  property_count: 3
  slug: azure-storage-accounts-check-name-availability-result
- name: ContainerProperties
  property_count: 10
  slug: azure-storage-accounts-container-properties
- name: CustomDomain
  property_count: 2
  slug: azure-storage-accounts-custom-domain
- name: DateAfterCreation
  property_count: 1
  slug: azure-storage-accounts-date-after-creation
- name: DateAfterModification
  property_count: 1
  slug: azure-storage-accounts-date-after-modification
- name: Dimension
  property_count: 2
  slug: azure-storage-accounts-dimension
- name: Encryption
  property_count: 3
  slug: azure-storage-accounts-encryption
- name: EncryptionService
  property_count: 3
  slug: azure-storage-accounts-encryption-service
- name: EncryptionServices
  property_count: 4
  slug: azure-storage-accounts-encryption-services
- name: Endpoints
  property_count: 8
  slug: azure-storage-accounts-endpoints
- name: GeoReplicationStats
  property_count: 3
  slug: azure-storage-accounts-geo-replication-stats
- name: Identity
  property_count: 3
  slug: azure-storage-accounts-identity
- name: ImmutabilityPolicyProperties
  property_count: 3
  slug: azure-storage-accounts-immutability-policy-properties
- name: ImmutabilityPolicyProperty
  property_count: 2
  slug: azure-storage-accounts-immutability-policy-property
- name: ImmutabilityPolicy
  property_count: 1
  slug: azure-storage-accounts-immutability-policy
- name: IPRule
  property_count: 2
  slug: azure-storage-accounts-ip-rule
- name: KeyVaultProperties
  property_count: 3
  slug: azure-storage-accounts-key-vault-properties
- name: LeaseContainerRequest
  property_count: 5
  slug: azure-storage-accounts-lease-container-request
- name: LeaseContainerResponse
  property_count: 2
  slug: azure-storage-accounts-lease-container-response
- name: LegalHoldProperties
  property_count: 2
  slug: azure-storage-accounts-legal-hold-properties
- name: LegalHold
  property_count: 2
  slug: azure-storage-accounts-legal-hold
- name: ListAccountSasResponse
  property_count: 1
  slug: azure-storage-accounts-list-account-sas-response
- name: ListContainerItem
  property_count: 1
  slug: azure-storage-accounts-list-container-item
- name: ListContainerItems
  property_count: 2
  slug: azure-storage-accounts-list-container-items
- name: ListServiceSasResponse
  property_count: 1
  slug: azure-storage-accounts-list-service-sas-response
- name: ManagementPolicyAction
  property_count: 2
  slug: azure-storage-accounts-management-policy-action
- name: ManagementPolicyBaseBlob
  property_count: 3
  slug: azure-storage-accounts-management-policy-base-blob
- name: ManagementPolicyDefinition
  property_count: 2
  slug: azure-storage-accounts-management-policy-definition
- name: ManagementPolicyFilter
  property_count: 2
  slug: azure-storage-accounts-management-policy-filter
- name: ManagementPolicyProperties
  property_count: 2
  slug: azure-storage-accounts-management-policy-properties
- name: ManagementPolicyRule
  property_count: 4
  slug: azure-storage-accounts-management-policy-rule
- name: ManagementPolicySchema
  property_count: 1
  slug: azure-storage-accounts-management-policy-schema
- name: ManagementPolicy
  property_count: 1
  slug: azure-storage-accounts-management-policy
- name: RestorePolicyProperties
  property_count: 2
  slug: azure-storage-accounts-restore-policy-properties
- name: TagProperty
  property_count: 5
  slug: azure-storage-accounts-tag-property
- name: UpdateHistoryProperty
  property_count: 6
  slug: azure-storage-accounts-update-history-property
json_structures:
- name: Azure Storage Accounts Account Sas Parameters Structure
  property_count: 8
  slug: azure-storage-accounts-account-sas-parameters-structure
- name: Azure Storage Accounts Active Directory Properties Structure
  property_count: 6
  slug: azure-storage-accounts-active-directory-properties-structure
- name: Azure Storage Accounts Azure Files Identity Based Authentication Structure
  property_count: 2
  slug: azure-storage-accounts-azure-files-identity-based-authentication-structure
- name: Azure Storage Accounts Blob Container Structure
  property_count: 1
  slug: azure-storage-accounts-blob-container-structure
- name: Azure Storage Accounts Blob Restore Parameters Structure
  property_count: 2
  slug: azure-storage-accounts-blob-restore-parameters-structure
- name: Azure Storage Accounts Blob Restore Range Structure
  property_count: 2
  slug: azure-storage-accounts-blob-restore-range-structure
- name: Azure Storage Accounts Blob Restore Status Structure
  property_count: 4
  slug: azure-storage-accounts-blob-restore-status-structure
- name: Azure Storage Accounts Blob Service Items Structure
  property_count: 1
  slug: azure-storage-accounts-blob-service-items-structure
- name: Azure Storage Accounts Blob Service Properties Structure
  property_count: 2
  slug: azure-storage-accounts-blob-service-properties-structure
- name: Azure Storage Accounts Change Feed Structure
  property_count: 1
  slug: azure-storage-accounts-change-feed-structure
- name: Azure Storage Accounts Check Name Availability Result Structure
  property_count: 3
  slug: azure-storage-accounts-check-name-availability-result-structure
- name: Azure Storage Accounts Container Properties Structure
  property_count: 10
  slug: azure-storage-accounts-container-properties-structure
- name: Azure Storage Accounts Custom Domain Structure
  property_count: 2
  slug: azure-storage-accounts-custom-domain-structure
- name: Azure Storage Accounts Date After Creation Structure
  property_count: 1
  slug: azure-storage-accounts-date-after-creation-structure
- name: Azure Storage Accounts Date After Modification Structure
  property_count: 1
  slug: azure-storage-accounts-date-after-modification-structure
- name: Azure Storage Accounts Dimension Structure
  property_count: 2
  slug: azure-storage-accounts-dimension-structure
- name: Azure Storage Accounts Encryption Service Structure
  property_count: 3
  slug: azure-storage-accounts-encryption-service-structure
- name: Azure Storage Accounts Encryption Services Structure
  property_count: 4
  slug: azure-storage-accounts-encryption-services-structure
- name: Azure Storage Accounts Encryption Structure
  property_count: 3
  slug: azure-storage-accounts-encryption-structure
- name: Azure Storage Accounts Endpoints Structure
  property_count: 8
  slug: azure-storage-accounts-endpoints-structure
- name: Azure Storage Accounts Geo Replication Stats Structure
  property_count: 3
  slug: azure-storage-accounts-geo-replication-stats-structure
- name: Azure Storage Accounts Identity Structure
  property_count: 3
  slug: azure-storage-accounts-identity-structure
- name: Azure Storage Accounts Immutability Policy Properties Structure
  property_count: 3
  slug: azure-storage-accounts-immutability-policy-properties-structure
- name: Azure Storage Accounts Immutability Policy Property Structure
  property_count: 2
  slug: azure-storage-accounts-immutability-policy-property-structure
- name: Azure Storage Accounts Immutability Policy Structure
  property_count: 1
  slug: azure-storage-accounts-immutability-policy-structure
- name: Azure Storage Accounts Ip Rule Structure
  property_count: 2
  slug: azure-storage-accounts-ip-rule-structure
- name: Azure Storage Accounts Key Vault Properties Structure
  property_count: 3
  slug: azure-storage-accounts-key-vault-properties-structure
- name: Azure Storage Accounts Lease Container Request Structure
  property_count: 5
  slug: azure-storage-accounts-lease-container-request-structure
- name: Azure Storage Accounts Lease Container Response Structure
  property_count: 2
  slug: azure-storage-accounts-lease-container-response-structure
- name: Azure Storage Accounts Legal Hold Properties Structure
  property_count: 2
  slug: azure-storage-accounts-legal-hold-properties-structure
- name: Azure Storage Accounts Legal Hold Structure
  property_count: 2
  slug: azure-storage-accounts-legal-hold-structure
- name: Azure Storage Accounts List Account Sas Response Structure
  property_count: 1
  slug: azure-storage-accounts-list-account-sas-response-structure
- name: Azure Storage Accounts List Container Item Structure
  property_count: 1
  slug: azure-storage-accounts-list-container-item-structure
- name: Azure Storage Accounts List Container Items Structure
  property_count: 2
  slug: azure-storage-accounts-list-container-items-structure
- name: Azure Storage Accounts List Service Sas Response Structure
  property_count: 1
  slug: azure-storage-accounts-list-service-sas-response-structure
- name: Azure Storage Accounts Management Policy Action Structure
  property_count: 2
  slug: azure-storage-accounts-management-policy-action-structure
- name: Azure Storage Accounts Management Policy Base Blob Structure
  property_count: 3
  slug: azure-storage-accounts-management-policy-base-blob-structure
- name: Azure Storage Accounts Management Policy Definition Structure
  property_count: 2
  slug: azure-storage-accounts-management-policy-definition-structure
- name: Azure Storage Accounts Management Policy Filter Structure
  property_count: 2
  slug: azure-storage-accounts-management-policy-filter-structure
- name: Azure Storage Accounts Management Policy Properties Structure
  property_count: 2
  slug: azure-storage-accounts-management-policy-properties-structure
- name: Azure Storage Accounts Management Policy Rule Structure
  property_count: 4
  slug: azure-storage-accounts-management-policy-rule-structure
- name: Azure Storage Accounts Management Policy Schema Structure
  property_count: 1
  slug: azure-storage-accounts-management-policy-schema-structure
- name: Azure Storage Accounts Management Policy Structure
  property_count: 1
  slug: azure-storage-accounts-management-policy-structure
- name: Azure Storage Accounts Restore Policy Properties Structure
  property_count: 2
  slug: azure-storage-accounts-restore-policy-properties-structure
- name: Azure Storage Accounts Tag Property Structure
  property_count: 5
  slug: azure-storage-accounts-tag-property-structure
- name: Azure Storage Accounts Update History Property Structure
  property_count: 6
  slug: azure-storage-accounts-update-history-property-structure
jsonld:
- class_count: 21
  name: Azure Storage Accounts Context
  property_count: 56
  slug: azure-storage-accounts-context
layout: provider
modified: '2026-05-19'
name: Azure Storage Accounts
nav: Providers
network: true
overview: 'Azure Storage Accounts publishes 9 APIs on the [APIs.io](https://apis.io/) network, including BlobContainers API, BlobService API, LocationUsage API, and 6 more. Tagged areas include Azure, Blob Storage, Cloud Storage, File Storage, and Queue Storage.


  The Azure Storage Accounts catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Azure Storage Accounts'' developer surface includes authentication, developer portal, documentation, getting-started guide, support, and 11 more developer resources.'
plans:
- name: Azure Storage Accounts Plans Pricing
  plan_count: 3
  slug: azure-storage-accounts-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Azure Storage Accounts Rate Limits
  slug: azure-storage-accounts-rate-limits
rules:
- name: Azure Storage Accounts API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: azure-storage-accounts-jsonschema-spectral-rules
- name: Azure Storage Accounts API Rules
  rule_count: 18
  severity_counts:
    error: 5
    hint: 0
    info: 4
    warn: 9
  slug: azure-storage-accounts-spectral-rules
scopes:
- name: Azure Storage Accounts Scopes
  scope_count: 1
  slug: azure-storage-accounts-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 63.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.5
    developer_ergonomics: 50.0
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 47.4
  previous_composite: 63.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-storage-accounts/refs/heads/main/screenshots/azure-storage-accounts-2026-06-20T172908.png
security:
- kind: authentication
  name: Azure Storage Accounts Authentication
  slug: azure-storage-accounts-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Azure Storage Accounts Domain Security
  slug: azure-storage-accounts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azure-storage-accounts
tags:
- Azure
- Blob Storage
- Cloud Storage
- File Storage
- Queue Storage
- Storage
- Table Storage
website: https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Storage%2FStorageAccounts
---
