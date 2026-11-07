---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Azure File Storage Agentic Access
  operation_count: 11
  slug: azure-file-storage-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 3
apis:
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
  name: Azure Files API
  slug: azure-file-storage-files-api
- baseURL: https://{account-name}.file.core.windows.net
  baseurl_source: declared
  description: File share operations
  name: Azure Files Shares API
  slug: azure-file-storage-shares-api
- baseURL: https://{account}.file.core.windows.net/
  baseurl_source: declared
  description: Shares operations
  name: Azure File Storage Shares API
  slug: microsoft-azure-file-storage-shares-api
- baseURL: https://{account-name}.file.core.windows.net
  baseurl_source: declared
  description: The directory API from Azure Files — 7 operation(s) for directory.
  name: Azure Files Directory API
  slug: azure-file-storage-directory-api
- baseURL: https://{account-name}.file.core.windows.net
  baseurl_source: declared
  description: The file API from Azure Files — 17 operation(s) for file.
  name: Azure Files File API
  slug: azure-file-storage-file-api
- baseURL: https://{account-name}.file.core.windows.net
  baseurl_source: declared
  description: The service API from Azure Files — 3 operation(s) for service.
  name: Azure Files Service API
  slug: azure-file-storage-service-api
- baseURL: https://{account-name}.file.core.windows.net
  baseurl_source: declared
  description: The share API from Azure Files — 13 operation(s) for share.
  name: Azure Files Share API
  slug: azure-file-storage-share-api
artifact_total: 32
collections:
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
  href: https://artifacts.apis.io/azure-file-storage/llms/azure-file-storage-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/azure-file-storage-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: operate
  href: https://artifacts.apis.io/azure-file-storage/rate-limits/azure-file-storage-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/azure-file-storage-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/azure-file-storage/plans/azure-file-storage-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/azure-file-storage-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/azure-file-storage/rules/azure-file-storage-rules.yml
  title: ''
  type: Spectral
  url: rules/azure-file-storage-rules.yml
- group: design
  href: https://artifacts.apis.io/azure-file-storage/json-ld/azure-file-storage-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/azure-file-storage-context.jsonld
- group: design
  href: https://artifacts.apis.io/azure-file-storage/vocabulary/azure-file-storage-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/azure-file-storage-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/azure-file-storage/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/azure-file-storage/data-model/azure-file-storage-data-model.yml
  title: ''
  type: DataModel
  url: data-model/azure-file-storage-data-model.yml
- group: design
  href: https://artifacts.apis.io/azure-file-storage/conventions/azure-file-storage-conventions.yml
  title: ''
  type: Conventions
  url: conventions/azure-file-storage-conventions.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: design
  href: https://artifacts.apis.io/azure-file-storage/lifecycle/azure-file-storage-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/azure-file-storage-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/azure-file-storage/errors/azure-file-storage-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/azure-file-storage-error-codes.yml
- group: design
  href: https://artifacts.apis.io/azure-file-storage/errors/azure-file-storage-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/azure-file-storage-problem-types.yml
- group: design
  href: https://artifacts.apis.io/azure-file-storage/conformance/azure-file-storage-conformance.yml
  title: ''
  type: Conformance
  url: conformance/azure-file-storage-conformance.yml
- group: auth
  href: https://artifacts.apis.io/azure-file-storage/well-known/azure-file-storage-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/azure-file-storage-www-security.txt
- group: agent
  href: https://artifacts.apis.io/azure-file-storage/well-known/azure-file-storage-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/azure-file-storage-well-known.yml
- group: other
  href: https://artifacts.apis.io/azure-file-storage/hosts/azure-file-storage-hosts.yml
  title: ''
  type: Hosts
  url: hosts/azure-file-storage-hosts.yml
- group: other
  href: https://artifacts.apis.io/azure-file-storage/vendors/azure-file-storage-vendors.yml
  title: ''
  type: Vendors
  url: vendors/azure-file-storage-vendors.yml
- group: build
  href: https://artifacts.apis.io/azure-file-storage/packages/azure-file-storage-packages.yml
  title: ''
  type: SDKs
  url: packages/azure-file-storage-packages.yml
- group: build
  href: https://artifacts.apis.io/azure-file-storage/packages/azure-file-storage-packages.yml
  title: ''
  type: Packages
  url: packages/azure-file-storage-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
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
- group: agent
  href: https://artifacts.apis.io/azure-file-storage/agentic-access/azure-file-storage-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-file-storage-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/azure-file-storage/security/azure-file-storage-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-file-storage-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/azure-file-storage/security/azure-file-storage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/azure-file-storage-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/azure-file-storage/authentication/azure-file-storage-authentication.yml
  title: ''
  type: Authentication
  url: authentication/azure-file-storage-authentication.yml
- group: auth
  href: https://artifacts.apis.io/azure-file-storage/scopes/azure-file-storage-scopes.yml
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
json_schemas:
- name: KeyInfo
  property_count: 3
  slug: azure-file-storage-key-info
- name: ListFilesAndDirectoriesSegmentResponse
  property_count: 11
  slug: azure-file-storage-list-files-and-directories-segment-response
- name: ListSharesResponse
  property_count: 6
  slug: azure-file-storage-list-shares-response
- name: SharePermission
  property_count: 2
  slug: azure-file-storage-share-permission
- name: StorageServiceProperties
  property_count: 4
  slug: azure-file-storage-storage-service-properties
- name: UserDelegationKey
  property_count: 8
  slug: azure-file-storage-user-delegation-key
jsonld:
- class_count: 34
  name: Azure File Storage Context
  property_count: 103
  slug: azure-file-storage-context
layout: provider
modified: '2026-09-16'
name: Azure Files
nav: Providers
network: true
overview: 'Azure Files publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Directories API, and 8 more. Tagged areas include Storage, File Storage, File Shares, NFS, and Cloud.


  The Azure Files catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Azure Files'' developer surface includes changelog, getting-started guide, developer portal, support, authentication, documentation, pricing, and 31 more developer resources.'
plans:
- name: Azure File Storage Plans Pricing
  plan_count: 3
  slug: azure-file-storage-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 7
  name: Azure File Storage Rate Limits
  slug: azure-file-storage-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Azure Files API Rules
  rule_count: 61
  severity_counts:
    error: 45
    hint: 0
    info: 9
    warn: 7
  slug: azure-file-storage-rules
scopes:
- name: Azure File Storage Scopes
  scope_count: 1
  slug: azure-file-storage-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: strong
  composite: 65.7
  coverage:
    artifact_dirs: 29
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 24.6
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 60.7
    developer_ergonomics: 58.9
    discoverability: 78.6
    operational_transparency: 76.3
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/azure-file-storage/azure-file-storage-2026-06-20T172902.png
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
skill_count: 2
skills:
- name: azure-file-storage-restore-deleted-share
  slug: azure-file-storage-restore-deleted-share
- name: azure-file-storage-upload-file
  slug: azure-file-storage-upload-file
slug: azure-file-storage
tags:
- Storage
- File Storage
- File Shares
- NFS
- Cloud
- Microsoft Azure
- Server Message Block
website: https://azure.microsoft.com/en-us/products/storage/files/
---
