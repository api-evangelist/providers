---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Microsoft Azure Blob Storage Agentic Access
  operation_count: 45
  slug: microsoft-azure-blob-storage-agentic-access
  summary_line: 45 operations · 29 acting
api_count: 3
apis:
- description: The Azure Data Lake Storage Gen2 REST APIs allow interaction with Azure Blob Storage through a file system interface. They enable creation and management of file systems, directories, and files on sto
  name: Azure Data Lake Storage Gen2 REST API
  slug: azure-data-lake-storage-gen2-rest-api
- baseURL: https://{accountName}.blob.core.windows.net
  baseurl_source: declared
  description: Operations specific to append blobs including append block
  name: Azure Blob Storage Append Blobs API
  slug: microsoft-azure-blob-storage-append-blobs-api
- description: The Azure Blob Storage REST API API from Azure Blob Storage — 1 operation(s) for azure blob storage rest api.
  name: Azure Blob Storage Azure Blob Storage REST API
  slug: microsoft-azure-blob-storage-azure-blob-storage-rest-api-api
- baseURL: https://{accountName}.blob.core.windows.net
  baseurl_source: declared
  description: Operations on blobs including get, put, delete, and metadata
  name: Azure Blob Storage Blobs API
  slug: microsoft-azure-blob-storage-blobs-api
- baseURL: https://{accountName}.blob.core.windows.net
  baseurl_source: declared
  description: Operations specific to block blobs including put block and put block list
  name: Azure Blob Storage Block Blobs API
  slug: microsoft-azure-blob-storage-block-blobs-api
- baseURL: https://{accountName}.blob.core.windows.net
  baseurl_source: declared
  description: Operations on blob containers
  name: Azure Blob Storage Containers API
  slug: microsoft-azure-blob-storage-containers-api
- baseURL: https://{accountName}.blob.core.windows.net
  baseurl_source: declared
  description: Operations specific to page blobs including put page and get page ranges
  name: Azure Blob Storage Page Blobs API
  slug: microsoft-azure-blob-storage-page-blobs-api
- baseURL: https://{accountName}.dfs.core.windows.net
  baseurl_source: declared
  description: The appendblob API from Azure Blob Storage — 3 operation(s) for appendblob.
  name: Azure Blob Storage Appendblob API
  slug: microsoft-azure-blob-storage-appendblob-api
- baseURL: https://{accountName}.dfs.core.windows.net
  baseurl_source: declared
  description: The blob API from Azure Blob Storage — 23 operation(s) for blob.
  name: Azure Blob Storage Blob API
  slug: microsoft-azure-blob-storage-blob-api
- baseURL: https://{accountName}.dfs.core.windows.net
  baseurl_source: declared
  description: The blockblob API from Azure Blob Storage — 3 operation(s) for blockblob.
  name: Azure Blob Storage Blockblob API
  slug: microsoft-azure-blob-storage-blockblob-api
- baseURL: https://{accountName}.dfs.core.windows.net
  baseurl_source: declared
  description: The container API from Azure Blob Storage — 13 operation(s) for container.
  name: Azure Blob Storage Container API
  slug: microsoft-azure-blob-storage-container-api
- baseURL: https://{accountName}.dfs.core.windows.net
  baseurl_source: declared
  description: The pageblob API from Azure Blob Storage — 8 operation(s) for pageblob.
  name: Azure Blob Storage Pageblob API
  slug: microsoft-azure-blob-storage-pageblob-api
- baseURL: https://{accountName}.dfs.core.windows.net
  baseurl_source: declared
  description: The service API from Azure Blob Storage — 7 operation(s) for service.
  name: Azure Blob Storage Service API
  slug: microsoft-azure-blob-storage-service-api
artifact_total: 65
asyncapis:
- description: ''
  name: Microsoft Azure Blob Storage Events
  slug: microsoft-azure-blob-storage-events
collections:
- collection_type: postman
  name: Azure Blob Storage REST Append Blobs API
  slug: postman-microsoft-azure-blob-storage-append-blobs-api
- collection_type: postman
  name: Azure Blob Storage REST Append Blobs Azure Blob Storage REST API API
  slug: postman-microsoft-azure-blob-storage-azure-blob-storage-rest-api-api
- collection_type: postman
  name: Azure Blob Storage REST Append Blobs API
  slug: postman-microsoft-azure-blob-storage-blobs-api
- collection_type: postman
  name: Azure Blob Storage REST Append Blobs Block Blobs API
  slug: postman-microsoft-azure-blob-storage-block-blobs-api
- collection_type: postman
  name: Azure Blob Storage REST Append Blobs ?comp=blobs API
  slug: postman-microsoft-azure-blob-storage-comp-blobs-api
- collection_type: postman
  name: Azure Blob Storage REST Append Blobs Containers API
  slug: postman-microsoft-azure-blob-storage-containers-api
- collection_type: postman
  name: Azure Blob Storage REST Append Blobs Page Blobs API
  slug: postman-microsoft-azure-blob-storage-page-blobs-api
- collection_type: postman
  name: Azure Blob Storage REST Append Blobs ?restype=service&comp=batch API
  slug: postman-microsoft-azure-blob-storage-restype-service-comp-batch-api
- collection_type: postman
  name: Azure Blob Storage REST Append Blobs ?restype=service&comp=properties API
  slug: postman-microsoft-azure-blob-storage-restype-service-comp-properties-api
- collection_type: postman
  name: Azure Blob Storage REST Append Blobs ?restype=service&comp=stats API
  slug: postman-microsoft-azure-blob-storage-restype-service-comp-stats-api
- collection_type: postman
  name: Azure Blob Storage REST Append Blobs ?restype=service&comp=userdelegationkey API
  slug: postman-microsoft-azure-blob-storage-restype-service-comp-userdelegationkey-api
- collection_type: open
  name: Azure Blob Storage REST API
  slug: open-azure-blob-storage-rest
- collection_type: open
  name: Azure Blob Storage REST Append Blobs API
  slug: open-microsoft-azure-blob-storage-append-blobs-api
- collection_type: open
  name: Azure Blob Storage REST Append Blobs Azure Blob Storage REST API API
  slug: open-microsoft-azure-blob-storage-azure-blob-storage-rest-api-api
- collection_type: open
  name: Azure Blob Storage REST Append Blobs API
  slug: open-microsoft-azure-blob-storage-blobs-api
- collection_type: open
  name: Azure Blob Storage REST Append Blobs Block Blobs API
  slug: open-microsoft-azure-blob-storage-block-blobs-api
- collection_type: open
  name: Azure Blob Storage REST Append Blobs ?comp=blobs API
  slug: open-microsoft-azure-blob-storage-comp-blobs-api
- collection_type: open
  name: Azure Blob Storage REST Append Blobs Containers API
  slug: open-microsoft-azure-blob-storage-containers-api
- collection_type: open
  name: Azure Blob Storage REST Append Blobs Page Blobs API
  slug: open-microsoft-azure-blob-storage-page-blobs-api
- collection_type: open
  name: Azure Blob Storage REST Append Blobs ?restype=service&comp=batch API
  slug: open-microsoft-azure-blob-storage-restype-service-comp-batch-api
- collection_type: open
  name: Azure Blob Storage REST Append Blobs ?restype=service&comp=properties API
  slug: open-microsoft-azure-blob-storage-restype-service-comp-properties-api
- collection_type: open
  name: Azure Blob Storage REST Append Blobs ?restype=service&comp=stats API
  slug: open-microsoft-azure-blob-storage-restype-service-comp-stats-api
- collection_type: open
  name: Azure Blob Storage REST Append Blobs ?restype=service&comp=userdelegationkey API
  slug: open-microsoft-azure-blob-storage-restype-service-comp-userdelegationkey-api
common:
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/rate-limits/microsoft-azure-blob-storage-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-blob-storage-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/rules/microsoft-azure-blob-storage-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-blob-storage-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/rules/microsoft-azure-blob-storage-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-blob-storage-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/json-ld/microsoft-azure-blob-storage-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-blob-storage-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/vocabulary/microsoft-azure-blob-storage-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-blob-storage-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/vocabulary/azure-blob-storage-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/azure-blob-storage-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/data-model/microsoft-azure-blob-storage-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-blob-storage-data-model.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/cli/microsoft-azure-blob-storage-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-blob-storage-cli.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/conventions/microsoft-azure-blob-storage-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-blob-storage-conventions.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/rest/api/storageservices/previous-azure-storage-service-versions
- group: design
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/lifecycle/microsoft-azure-blob-storage-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-blob-storage-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/errors/microsoft-azure-blob-storage-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-blob-storage-error-codes.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/errors/microsoft-azure-blob-storage-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-blob-storage-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/conformance/microsoft-azure-blob-storage-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-blob-storage-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/llms/microsoft-azure-blob-storage-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-blob-storage-llms.txt
- group: build
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/mcp/microsoft-azure-blob-storage-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-azure-blob-storage-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/mcp/microsoft-azure-blob-storage-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-azure-blob-storage-mcp.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/hosts/microsoft-azure-blob-storage-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-blob-storage-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/integrations/microsoft-azure-blob-storage-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-azure-blob-storage-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/vendors/microsoft-azure-blob-storage-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-blob-storage-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/packages/microsoft-azure-blob-storage-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-blob-storage-packages.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/plans/microsoft-azure-blob-storage-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-blob-storage-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/finops/microsoft-azure-blob-storage-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-blob-storage-finops.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/capabilities/microsoft-azure-blob-storage-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-azure-blob-storage-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Azure/azure-rest-api-specs/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Azure/azure-rest-api-specs/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Azure/azure-rest-api-specs/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Azure/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Azure/azure-rest-api-specs/blob/main/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Azure/azure-rest-api-specs/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-blob-storage/overview
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/agentic-access/microsoft-azure-blob-storage-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-blob-storage-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/security/microsoft-azure-blob-storage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-blob-storage-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-blob-storage/authentication/microsoft-azure-blob-storage-authentication.yml
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
description: Microsoft Azure Blob Storage is a service for storing large amounts of unstructured object data, such as text or binary data, that can be accessed from anywhere in the world via HTTP or HTTPS. Its date-versioned REST API (x-ms-version, latest 2027-03-07) manages containers and block, append and page blobs at https://{accountName}.blob.core.windows.net, with official SDKs for .NET, Java, JavaScript, Python, Go and Rust, the Azure CLI, and storage tools in the Azure MCP Server.
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Blob Storage Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-blob-storage-finops
  template: true
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
- name: BlobList
  property_count: 8
  slug: microsoft-azure-blob-storage-blob-list
- name: ListBlobsFlatSegmentResponse
  property_count: 7
  slug: microsoft-azure-blob-storage-list-blobs-flat-segment-response
- name: ListBlobsHierarchySegmentResponse
  property_count: 8
  slug: microsoft-azure-blob-storage-list-blobs-hierarchy-segment-response
- name: ListContainersSegmentResponse
  property_count: 6
  slug: microsoft-azure-blob-storage-list-containers-segment-response
- name: QueryRequest
  property_count: 4
  slug: microsoft-azure-blob-storage-query-request
- name: StorageServiceProperties
  property_count: 7
  slug: microsoft-azure-blob-storage-storage-service-properties
- name: UserDelegationKey
  property_count: 8
  slug: microsoft-azure-blob-storage-user-delegation-key
json_structures:
- name: Azure Blob Storage Structure
  property_count: 0
  slug: azure-blob-storage-structure
jsonld:
- class_count: 49
  name: Microsoft Azure Blob Storage Context
  property_count: 128
  slug: microsoft-azure-blob-storage-context
layout: provider
mcp_servers:
- description: MCP server requiring OAuth; 7 tools listed.
  name: Azure MCP Server (storage tools)
  slug: azure-mcp-server-storage-tools
modified: '2026-11-05'
name: Azure Blob Storage
nav: Providers
network: true
overview: 'Azure Blob Storage publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Append Blobs API, Azure Blob Storage REST API, Blobs API, and 10 more. Tagged areas include Microsoft Azure, Blobs, Cloud Storage, Microsoft, and Object Storage.


  The Azure Blob Storage catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Azure Blob Storage''s developer surface includes CLI, authentication, developer portal, support, engineering blog, getting-started guide, changelog, and 48 more developer resources.'
plans:
- name: Microsoft Azure Blob Storage Plans Pricing
  plan_count: 0
  slug: microsoft-azure-blob-storage-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Microsoft Azure Blob Storage Rate Limits
  slug: microsoft-azure-blob-storage-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Azure Blob Storage — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-azure-blob-storage-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Azure Blob Storage API Rules
  rule_count: 59
  severity_counts:
    error: 43
    hint: 0
    info: 8
    warn: 8
  slug: microsoft-azure-blob-storage-rules
score:
  band: exemplar
  composite: 68.5
  coverage:
    artifact_dirs: 38
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 13.0
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 70.7
    developer_ergonomics: 81.5
    discoverability: 76.7
    operational_transparency: 84.2
  open_source:
    applies: true
    score: 100.0
  previous_composite: 55.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-azure-blob-storage/microsoft-azure-blob-storage-2026-06-20T185402.png
security:
- kind: authentication
  name: Microsoft Azure Blob Storage Authentication
  slug: microsoft-azure-blob-storage-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Microsoft Azure Blob Storage Domain Security
  slug: microsoft-azure-blob-storage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: recover-deleted-blob
  slug: microsoft-azure-blob-storage-recover-deleted-blob
- name: upload-and-download-blob
  slug: microsoft-azure-blob-storage-upload-and-download-blob
slug: microsoft-azure-blob-storage
tags:
- Microsoft Azure
- Blobs
- Cloud Storage
- Microsoft
- Object Storage
- Storage
website: https://azure.microsoft.com/en-us/products/storage/blobs/
---
