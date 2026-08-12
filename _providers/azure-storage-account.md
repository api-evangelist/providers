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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 26
  human_in_the_loop: 1
  name: Azure Storage Account Agentic Access
  operation_count: 40
  slug: azure-storage-account-agentic-access
  summary_line: 40 operations · 26 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: The BlobContainers API from Azure Storage Account — 8 operation(s) for blobcontainers.
  name: Azure Storage Account BlobContainers API
  slug: azure-storage-account-blobcontainers-api
- description: The BlobService API from Azure Storage Account — 2 operation(s) for blobservice.
  name: Azure Storage Account BlobService API
  slug: azure-storage-account-blobservice-api
- description: The LocationUsage API from Azure Storage Account — 1 operation(s) for locationusage.
  name: Azure Storage Account LocationUsage API
  slug: azure-storage-account-locationusage-api
- description: The ManagementPolicies API from Azure Storage Account — 1 operation(s) for managementpolicies.
  name: Azure Storage Account ManagementPolicies API
  slug: azure-storage-account-managementpolicies-api
- description: The Operations API from Azure Storage Account — 1 operation(s) for operations.
  name: Azure Storage Account Operations API
  slug: azure-storage-account-operations-api
- description: The PrivateEndpointConnections API from Azure Storage Account — 1 operation(s) for privateendpointconnections.
  name: Azure Storage Account PrivateEndpointConnections API
  slug: azure-storage-account-privateendpointconnections-api
- description: The PrivateLinkResources API from Azure Storage Account — 1 operation(s) for privatelinkresources.
  name: Azure Storage Account PrivateLinkResources API
  slug: azure-storage-account-privatelinkresources-api
- description: The Skus API from Azure Storage Account — 1 operation(s) for skus.
  name: Azure Storage Account Skus API
  slug: azure-storage-account-skus-api
- description: The StorageAccounts API from Azure Storage Account — 11 operation(s) for storageaccounts.
  name: Azure Storage Account StorageAccounts API
  slug: azure-storage-account-storageaccounts-api
artifact_total: 166
collections:
- collection_type: postman
  name: StorageManagementClient BlobContainers API
  slug: postman-azure-storage-account-blobcontainers-api
- collection_type: postman
  name: StorageManagementClient BlobContainers BlobService API
  slug: postman-azure-storage-account-blobservice-api
- collection_type: postman
  name: StorageManagementClient BlobContainers LocationUsage API
  slug: postman-azure-storage-account-locationusage-api
- collection_type: postman
  name: StorageManagementClient BlobContainers ManagementPolicies API
  slug: postman-azure-storage-account-managementpolicies-api
- collection_type: postman
  name: StorageManagementClient BlobContainers Operations API
  slug: postman-azure-storage-account-operations-api
- collection_type: postman
  name: StorageManagementClient BlobContainers PrivateEndpointConnections API
  slug: postman-azure-storage-account-privateendpointconnections-api
- collection_type: postman
  name: StorageManagementClient BlobContainers PrivateLinkResources API
  slug: postman-azure-storage-account-privatelinkresources-api
- collection_type: postman
  name: StorageManagementClient BlobContainers Skus API
  slug: postman-azure-storage-account-skus-api
- collection_type: postman
  name: StorageManagementClient BlobContainers StorageAccounts API
  slug: postman-azure-storage-account-storageaccounts-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-storage-account/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-storage-account-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-storage-account-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-storage-account-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-storage-account-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/storage/
- group: build
  title: ''
  type: SDKs
  url: https://azure.microsoft.com/en-us/downloads/
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
  url: https://raw.githubusercontent.com/api-evangelist/azure-storage-account/refs/heads/main/rules/azure-storage-account-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/azure-storage-account/refs/heads/main/vocabulary/azure-storage-account-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/azure-storage-account/refs/heads/main/json-ld/azure-storage-account-context.jsonld
created: '2024-01-01'
description: Collection of APIs for Azure Storage Account services including Blob, Queue, Table, and File storage, providing highly available, massively scalable, durable, and secure storage for a variety of data objects.
examples:
- key_count: 8
  name: Azure Storage Account Account Sas Parameters Example
  slug: azure-storage-account-account-sas-parameters-example
- key_count: 6
  name: Azure Storage Account Active Directory Properties Example
  slug: azure-storage-account-active-directory-properties-example
- key_count: 1
  name: Azure Storage Account Azure Files Identity Based Authentication Example
  slug: azure-storage-account-azure-files-identity-based-authentication-example
- key_count: 0
  name: Azure Storage Account Blob Container Example
  slug: azure-storage-account-blob-container-example
- key_count: 2
  name: Azure Storage Account Blob Restore Parameters Example
  slug: azure-storage-account-blob-restore-parameters-example
- key_count: 2
  name: Azure Storage Account Blob Restore Range Example
  slug: azure-storage-account-blob-restore-range-example
- key_count: 3
  name: Azure Storage Account Blob Restore Status Example
  slug: azure-storage-account-blob-restore-status-example
- key_count: 1
  name: Azure Storage Account Blob Service Items Example
  slug: azure-storage-account-blob-service-items-example
- key_count: 2
  name: Azure Storage Account Blob Service Properties Example
  slug: azure-storage-account-blob-service-properties-example
- key_count: 1
  name: Azure Storage Account Change Feed Example
  slug: azure-storage-account-change-feed-example
- key_count: 3
  name: Azure Storage Account Check Name Availability Result Example
  slug: azure-storage-account-check-name-availability-result-example
- key_count: 8
  name: Azure Storage Account Container Properties Example
  slug: azure-storage-account-container-properties-example
- key_count: 2
  name: Azure Storage Account Custom Domain Example
  slug: azure-storage-account-custom-domain-example
- key_count: 1
  name: Azure Storage Account Date After Creation Example
  slug: azure-storage-account-date-after-creation-example
- key_count: 1
  name: Azure Storage Account Date After Modification Example
  slug: azure-storage-account-date-after-modification-example
- key_count: 2
  name: Azure Storage Account Dimension Example
  slug: azure-storage-account-dimension-example
- key_count: 1
  name: Azure Storage Account Encryption Example
  slug: azure-storage-account-encryption-example
- key_count: 3
  name: Azure Storage Account Encryption Service Example
  slug: azure-storage-account-encryption-service-example
- key_count: 0
  name: Azure Storage Account Encryption Services Example
  slug: azure-storage-account-encryption-services-example
- key_count: 6
  name: Azure Storage Account Endpoints Example
  slug: azure-storage-account-endpoints-example
- key_count: 3
  name: Azure Storage Account Geo Replication Stats Example
  slug: azure-storage-account-geo-replication-stats-example
- key_count: 3
  name: Azure Storage Account Identity Example
  slug: azure-storage-account-identity-example
- key_count: 0
  name: Azure Storage Account Immutability Policy Example
  slug: azure-storage-account-immutability-policy-example
- key_count: 2
  name: Azure Storage Account Immutability Policy Properties Example
  slug: azure-storage-account-immutability-policy-properties-example
- key_count: 2
  name: Azure Storage Account Immutability Policy Property Example
  slug: azure-storage-account-immutability-policy-property-example
- key_count: 2
  name: Azure Storage Account Ip Rule Example
  slug: azure-storage-account-ip-rule-example
- key_count: 3
  name: Azure Storage Account Key Vault Properties Example
  slug: azure-storage-account-key-vault-properties-example
- key_count: 5
  name: Azure Storage Account Lease Container Request Example
  slug: azure-storage-account-lease-container-request-example
- key_count: 2
  name: Azure Storage Account Lease Container Response Example
  slug: azure-storage-account-lease-container-response-example
- key_count: 2
  name: Azure Storage Account Legal Hold Example
  slug: azure-storage-account-legal-hold-example
- key_count: 2
  name: Azure Storage Account Legal Hold Properties Example
  slug: azure-storage-account-legal-hold-properties-example
- key_count: 1
  name: Azure Storage Account List Account Sas Response Example
  slug: azure-storage-account-list-account-sas-response-example
- key_count: 0
  name: Azure Storage Account List Container Item Example
  slug: azure-storage-account-list-container-item-example
- key_count: 2
  name: Azure Storage Account List Container Items Example
  slug: azure-storage-account-list-container-items-example
- key_count: 1
  name: Azure Storage Account List Service Sas Response Example
  slug: azure-storage-account-list-service-sas-response-example
- key_count: 0
  name: Azure Storage Account Management Policy Action Example
  slug: azure-storage-account-management-policy-action-example
- key_count: 0
  name: Azure Storage Account Management Policy Base Blob Example
  slug: azure-storage-account-management-policy-base-blob-example
- key_count: 0
  name: Azure Storage Account Management Policy Definition Example
  slug: azure-storage-account-management-policy-definition-example
- key_count: 0
  name: Azure Storage Account Management Policy Example
  slug: azure-storage-account-management-policy-example
- key_count: 2
  name: Azure Storage Account Management Policy Filter Example
  slug: azure-storage-account-management-policy-filter-example
- key_count: 1
  name: Azure Storage Account Management Policy Properties Example
  slug: azure-storage-account-management-policy-properties-example
- key_count: 3
  name: Azure Storage Account Management Policy Rule Example
  slug: azure-storage-account-management-policy-rule-example
- key_count: 1
  name: Azure Storage Account Management Policy Schema Example
  slug: azure-storage-account-management-policy-schema-example
- key_count: 2
  name: Azure Storage Account Restore Policy Properties Example
  slug: azure-storage-account-restore-policy-properties-example
- key_count: 5
  name: Azure Storage Account Tag Property Example
  slug: azure-storage-account-tag-property-example
- key_count: 6
  name: Azure Storage Account Update History Property Example
  slug: azure-storage-account-update-history-property-example
finops:
- name: Azure Storage Account Finops
  service_category: Storage
  slug: azure-storage-account-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-storage-account.png
json_schemas:
- name: AccountSasParameters
  property_count: 8
  slug: azure-storage-account-account-sas-parameters
- name: ActiveDirectoryProperties
  property_count: 6
  slug: azure-storage-account-active-directory-properties
- name: AzureFilesIdentityBasedAuthentication
  property_count: 2
  slug: azure-storage-account-azure-files-identity-based-authentication
- name: BlobContainer
  property_count: 1
  slug: azure-storage-account-blob-container
- name: BlobRestoreParameters
  property_count: 2
  slug: azure-storage-account-blob-restore-parameters
- name: BlobRestoreRange
  property_count: 2
  slug: azure-storage-account-blob-restore-range
- name: BlobRestoreStatus
  property_count: 4
  slug: azure-storage-account-blob-restore-status
- name: BlobServiceItems
  property_count: 1
  slug: azure-storage-account-blob-service-items
- name: BlobServiceProperties
  property_count: 2
  slug: azure-storage-account-blob-service-properties
- name: ChangeFeed
  property_count: 1
  slug: azure-storage-account-change-feed
- name: CheckNameAvailabilityResult
  property_count: 3
  slug: azure-storage-account-check-name-availability-result
- name: ContainerProperties
  property_count: 10
  slug: azure-storage-account-container-properties
- name: CustomDomain
  property_count: 2
  slug: azure-storage-account-custom-domain
- name: DateAfterCreation
  property_count: 1
  slug: azure-storage-account-date-after-creation
- name: DateAfterModification
  property_count: 1
  slug: azure-storage-account-date-after-modification
- name: Dimension
  property_count: 2
  slug: azure-storage-account-dimension
- name: Encryption
  property_count: 3
  slug: azure-storage-account-encryption
- name: EncryptionService
  property_count: 3
  slug: azure-storage-account-encryption-service
- name: EncryptionServices
  property_count: 4
  slug: azure-storage-account-encryption-services
- name: Endpoints
  property_count: 8
  slug: azure-storage-account-endpoints
- name: GeoReplicationStats
  property_count: 3
  slug: azure-storage-account-geo-replication-stats
- name: Identity
  property_count: 3
  slug: azure-storage-account-identity
- name: ImmutabilityPolicyProperties
  property_count: 3
  slug: azure-storage-account-immutability-policy-properties
- name: ImmutabilityPolicyProperty
  property_count: 2
  slug: azure-storage-account-immutability-policy-property
- name: ImmutabilityPolicy
  property_count: 1
  slug: azure-storage-account-immutability-policy
- name: IPRule
  property_count: 2
  slug: azure-storage-account-ip-rule
- name: KeyVaultProperties
  property_count: 3
  slug: azure-storage-account-key-vault-properties
- name: LeaseContainerRequest
  property_count: 5
  slug: azure-storage-account-lease-container-request
- name: LeaseContainerResponse
  property_count: 2
  slug: azure-storage-account-lease-container-response
- name: LegalHoldProperties
  property_count: 2
  slug: azure-storage-account-legal-hold-properties
- name: LegalHold
  property_count: 2
  slug: azure-storage-account-legal-hold
- name: ListAccountSasResponse
  property_count: 1
  slug: azure-storage-account-list-account-sas-response
- name: ListContainerItem
  property_count: 1
  slug: azure-storage-account-list-container-item
- name: ListContainerItems
  property_count: 2
  slug: azure-storage-account-list-container-items
- name: ListServiceSasResponse
  property_count: 1
  slug: azure-storage-account-list-service-sas-response
- name: ManagementPolicyAction
  property_count: 2
  slug: azure-storage-account-management-policy-action
- name: ManagementPolicyBaseBlob
  property_count: 3
  slug: azure-storage-account-management-policy-base-blob
- name: ManagementPolicyDefinition
  property_count: 2
  slug: azure-storage-account-management-policy-definition
- name: ManagementPolicyFilter
  property_count: 2
  slug: azure-storage-account-management-policy-filter
- name: ManagementPolicyProperties
  property_count: 2
  slug: azure-storage-account-management-policy-properties
- name: ManagementPolicyRule
  property_count: 4
  slug: azure-storage-account-management-policy-rule
- name: ManagementPolicySchema
  property_count: 1
  slug: azure-storage-account-management-policy-schema
- name: ManagementPolicy
  property_count: 1
  slug: azure-storage-account-management-policy
- name: RestorePolicyProperties
  property_count: 2
  slug: azure-storage-account-restore-policy-properties
- name: TagProperty
  property_count: 5
  slug: azure-storage-account-tag-property
- name: UpdateHistoryProperty
  property_count: 6
  slug: azure-storage-account-update-history-property
json_structures:
- name: Azure Storage Account Account Sas Parameters Structure
  property_count: 8
  slug: azure-storage-account-account-sas-parameters-structure
- name: Azure Storage Account Active Directory Properties Structure
  property_count: 6
  slug: azure-storage-account-active-directory-properties-structure
- name: Azure Storage Account Azure Files Identity Based Authentication Structure
  property_count: 2
  slug: azure-storage-account-azure-files-identity-based-authentication-structure
- name: Azure Storage Account Blob Container Structure
  property_count: 1
  slug: azure-storage-account-blob-container-structure
- name: Azure Storage Account Blob Restore Parameters Structure
  property_count: 2
  slug: azure-storage-account-blob-restore-parameters-structure
- name: Azure Storage Account Blob Restore Range Structure
  property_count: 2
  slug: azure-storage-account-blob-restore-range-structure
- name: Azure Storage Account Blob Restore Status Structure
  property_count: 4
  slug: azure-storage-account-blob-restore-status-structure
- name: Azure Storage Account Blob Service Items Structure
  property_count: 1
  slug: azure-storage-account-blob-service-items-structure
- name: Azure Storage Account Blob Service Properties Structure
  property_count: 2
  slug: azure-storage-account-blob-service-properties-structure
- name: Azure Storage Account Change Feed Structure
  property_count: 1
  slug: azure-storage-account-change-feed-structure
- name: Azure Storage Account Check Name Availability Result Structure
  property_count: 3
  slug: azure-storage-account-check-name-availability-result-structure
- name: Azure Storage Account Container Properties Structure
  property_count: 10
  slug: azure-storage-account-container-properties-structure
- name: Azure Storage Account Custom Domain Structure
  property_count: 2
  slug: azure-storage-account-custom-domain-structure
- name: Azure Storage Account Date After Creation Structure
  property_count: 1
  slug: azure-storage-account-date-after-creation-structure
- name: Azure Storage Account Date After Modification Structure
  property_count: 1
  slug: azure-storage-account-date-after-modification-structure
- name: Azure Storage Account Dimension Structure
  property_count: 2
  slug: azure-storage-account-dimension-structure
- name: Azure Storage Account Encryption Service Structure
  property_count: 3
  slug: azure-storage-account-encryption-service-structure
- name: Azure Storage Account Encryption Services Structure
  property_count: 4
  slug: azure-storage-account-encryption-services-structure
- name: Azure Storage Account Encryption Structure
  property_count: 3
  slug: azure-storage-account-encryption-structure
- name: Azure Storage Account Endpoints Structure
  property_count: 8
  slug: azure-storage-account-endpoints-structure
- name: Azure Storage Account Geo Replication Stats Structure
  property_count: 3
  slug: azure-storage-account-geo-replication-stats-structure
- name: Azure Storage Account Identity Structure
  property_count: 3
  slug: azure-storage-account-identity-structure
- name: Azure Storage Account Immutability Policy Properties Structure
  property_count: 3
  slug: azure-storage-account-immutability-policy-properties-structure
- name: Azure Storage Account Immutability Policy Property Structure
  property_count: 2
  slug: azure-storage-account-immutability-policy-property-structure
- name: Azure Storage Account Immutability Policy Structure
  property_count: 1
  slug: azure-storage-account-immutability-policy-structure
- name: Azure Storage Account Ip Rule Structure
  property_count: 2
  slug: azure-storage-account-ip-rule-structure
- name: Azure Storage Account Key Vault Properties Structure
  property_count: 3
  slug: azure-storage-account-key-vault-properties-structure
- name: Azure Storage Account Lease Container Request Structure
  property_count: 5
  slug: azure-storage-account-lease-container-request-structure
- name: Azure Storage Account Lease Container Response Structure
  property_count: 2
  slug: azure-storage-account-lease-container-response-structure
- name: Azure Storage Account Legal Hold Properties Structure
  property_count: 2
  slug: azure-storage-account-legal-hold-properties-structure
- name: Azure Storage Account Legal Hold Structure
  property_count: 2
  slug: azure-storage-account-legal-hold-structure
- name: Azure Storage Account List Account Sas Response Structure
  property_count: 1
  slug: azure-storage-account-list-account-sas-response-structure
- name: Azure Storage Account List Container Item Structure
  property_count: 1
  slug: azure-storage-account-list-container-item-structure
- name: Azure Storage Account List Container Items Structure
  property_count: 2
  slug: azure-storage-account-list-container-items-structure
- name: Azure Storage Account List Service Sas Response Structure
  property_count: 1
  slug: azure-storage-account-list-service-sas-response-structure
- name: Azure Storage Account Management Policy Action Structure
  property_count: 2
  slug: azure-storage-account-management-policy-action-structure
- name: Azure Storage Account Management Policy Base Blob Structure
  property_count: 3
  slug: azure-storage-account-management-policy-base-blob-structure
- name: Azure Storage Account Management Policy Definition Structure
  property_count: 2
  slug: azure-storage-account-management-policy-definition-structure
- name: Azure Storage Account Management Policy Filter Structure
  property_count: 2
  slug: azure-storage-account-management-policy-filter-structure
- name: Azure Storage Account Management Policy Properties Structure
  property_count: 2
  slug: azure-storage-account-management-policy-properties-structure
- name: Azure Storage Account Management Policy Rule Structure
  property_count: 4
  slug: azure-storage-account-management-policy-rule-structure
- name: Azure Storage Account Management Policy Schema Structure
  property_count: 1
  slug: azure-storage-account-management-policy-schema-structure
- name: Azure Storage Account Management Policy Structure
  property_count: 1
  slug: azure-storage-account-management-policy-structure
- name: Azure Storage Account Restore Policy Properties Structure
  property_count: 2
  slug: azure-storage-account-restore-policy-properties-structure
- name: Azure Storage Account Tag Property Structure
  property_count: 5
  slug: azure-storage-account-tag-property-structure
- name: Azure Storage Account Update History Property Structure
  property_count: 6
  slug: azure-storage-account-update-history-property-structure
jsonld:
- class_count: 21
  name: Azure Storage Account Context
  property_count: 56
  slug: azure-storage-account-context
layout: provider
modified: '2026-05-19'
name: Azure Storage Account
nav: Providers
network: true
overview: 'Azure Storage Account publishes 9 APIs on the [APIs.io](https://apis.io/) network, including BlobContainers API, BlobService API, LocationUsage API, and 6 more. Tagged areas include Azure, Blob Storage, Cloud Storage, File Storage, and Microsoft.


  The Azure Storage Account catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Azure Storage Account''s developer surface includes authentication, developer portal, documentation, support, and 11 more developer resources.'
plans:
- name: Azure Storage Account Plans Pricing
  plan_count: 5
  slug: azure-storage-account-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 13
  name: Azure Storage Account Rate Limits
  slug: azure-storage-account-rate-limits
rules:
- name: Azure Storage Account API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: azure-storage-account-jsonschema-spectral-rules
- name: Azure Storage Account API Rules
  rule_count: 18
  severity_counts:
    error: 5
    hint: 0
    info: 4
    warn: 9
  slug: azure-storage-account-spectral-rules
scopes:
- name: Azure Storage Account Scopes
  scope_count: 1
  slug: azure-storage-account-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 50.1
  delta: -8.4
  facets:
    commercial_clarity: 36.8
    contract_quality: 61.2
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 23.7
  previous_composite: 58.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-storage-account/refs/heads/main/screenshots/azure-storage-account-2026-06-20T172908.png
security:
- kind: authentication
  name: Azure Storage Account Authentication
  slug: azure-storage-account-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Azure Storage Account Domain Security
  slug: azure-storage-account-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azure-storage-account
tags:
- Azure
- Blob Storage
- Cloud Storage
- File Storage
- Microsoft
- Storage
website: https://portal.azure.com
---
