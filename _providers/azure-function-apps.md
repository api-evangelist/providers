---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Azure Function Apps Agentic Access
  operation_count: 37
  slug: azure-function-apps-agentic-access
  summary_line: 37 operations · 26 acting
api_count: 1
apis:
- description: The WebApps API from Azure Function Apps — 30 operation(s) for webapps.
  name: Azure Function Apps WebApps API
  slug: azure-function-apps-webapps-api
artifact_total: 72
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Functions Management WebApps API
  slug: open-azure-function-apps-webapps-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-function-apps-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-function-apps-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/azure-functions/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/azure-functions/bg-p/AzureFunctionsBlog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure/azure-functions
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
  url: https://raw.githubusercontent.com/api-evangelist/azure-function-apps/refs/heads/main/rules/azure-function-apps-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/azure-function-apps/refs/heads/main/vocabulary/azure-function-apps-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/azure-function-apps/refs/heads/main/json-ld/azure-function-apps-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Azure/azure-functions-mcp-extension
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2024-01-01'
description: Azure Functions is a serverless compute service that lets you run event-triggered code without having to explicitly provision or manage infrastructure, with APIs for managing function apps, deployments, and runtime operations.
examples:
- key_count: 9
  name: Azure Function Apps Api Kv Reference Example
  slug: azure-function-apps-api-kv-reference-example
- key_count: 0
  name: Azure Function Apps Application Logs Config Example
  slug: azure-function-apps-application-logs-config-example
- key_count: 3
  name: Azure Function Apps Azure Blob Storage Application Logs Config Example
  slug: azure-function-apps-azure-blob-storage-application-logs-config-example
- key_count: 3
  name: Azure Function Apps Azure Blob Storage Http Logs Config Example
  slug: azure-function-apps-azure-blob-storage-http-logs-config-example
- key_count: 6
  name: Azure Function Apps Azure Storage Info Value Example
  slug: azure-function-apps-azure-storage-info-value-example
- key_count: 1
  name: Azure Function Apps Azure Storage Property Dictionary Resource Example
  slug: azure-function-apps-azure-storage-property-dictionary-resource-example
- key_count: 2
  name: Azure Function Apps Azure Table Storage Application Logs Config Example
  slug: azure-function-apps-azure-table-storage-application-logs-config-example
- key_count: 2
  name: Azure Function Apps Backup Item Collection Example
  slug: azure-function-apps-backup-item-collection-example
- key_count: 1
  name: Azure Function Apps Backup Item Example
  slug: azure-function-apps-backup-item-example
- key_count: 1
  name: Azure Function Apps Backup Request Example
  slug: azure-function-apps-backup-request-example
- key_count: 6
  name: Azure Function Apps Backup Schedule Example
  slug: azure-function-apps-backup-schedule-example
- key_count: 2
  name: Azure Function Apps Conn String Value Type Pair Example
  slug: azure-function-apps-conn-string-value-type-pair-example
- key_count: 1
  name: Azure Function Apps Connection String Dictionary Example
  slug: azure-function-apps-connection-string-dictionary-example
- key_count: 2
  name: Azure Function Apps Container Cpu Statistics Example
  slug: azure-function-apps-container-cpu-statistics-example
- key_count: 4
  name: Azure Function Apps Container Cpu Usage Example
  slug: azure-function-apps-container-cpu-usage-example
- key_count: 4
  name: Azure Function Apps Container Info Example
  slug: azure-function-apps-container-info-example
- key_count: 3
  name: Azure Function Apps Container Memory Statistics Example
  slug: azure-function-apps-container-memory-statistics-example
- key_count: 8
  name: Azure Function Apps Container Network Interface Statistics Example
  slug: azure-function-apps-container-network-interface-statistics-example
- key_count: 3
  name: Azure Function Apps Container Throttling Data Example
  slug: azure-function-apps-container-throttling-data-example
- key_count: 1
  name: Azure Function Apps Continuous Web Job Example
  slug: azure-function-apps-continuous-web-job-example
finops:
- name: Azure Function Apps Finops
  service_category: API
  slug: azure-function-apps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-function-apps.png
json_schemas:
- name: ApiKVReference
  property_count: 9
  slug: azure-function-apps-api-kv-reference
- name: ApplicationLogsConfig
  property_count: 3
  slug: azure-function-apps-application-logs-config
- name: AzureBlobStorageApplicationLogsConfig
  property_count: 3
  slug: azure-function-apps-azure-blob-storage-application-logs-config
- name: AzureBlobStorageHttpLogsConfig
  property_count: 3
  slug: azure-function-apps-azure-blob-storage-http-logs-config
- name: AzureStorageInfoValue
  property_count: 6
  slug: azure-function-apps-azure-storage-info-value
- name: AzureStoragePropertyDictionaryResource
  property_count: 1
  slug: azure-function-apps-azure-storage-property-dictionary-resource
- name: AzureTableStorageApplicationLogsConfig
  property_count: 2
  slug: azure-function-apps-azure-table-storage-application-logs-config
- name: BackupItemCollection
  property_count: 2
  slug: azure-function-apps-backup-item-collection
- name: BackupItem
  property_count: 1
  slug: azure-function-apps-backup-item
- name: BackupRequest
  property_count: 1
  slug: azure-function-apps-backup-request
- name: BackupSchedule
  property_count: 6
  slug: azure-function-apps-backup-schedule
- name: ConnStringValueTypePair
  property_count: 2
  slug: azure-function-apps-conn-string-value-type-pair
- name: ConnectionStringDictionary
  property_count: 1
  slug: azure-function-apps-connection-string-dictionary
- name: ContainerCpuStatistics
  property_count: 4
  slug: azure-function-apps-container-cpu-statistics
- name: ContainerCpuUsage
  property_count: 4
  slug: azure-function-apps-container-cpu-usage
- name: ContainerInfo
  property_count: 8
  slug: azure-function-apps-container-info
- name: ContainerMemoryStatistics
  property_count: 3
  slug: azure-function-apps-container-memory-statistics
- name: ContainerNetworkInterfaceStatistics
  property_count: 8
  slug: azure-function-apps-container-network-interface-statistics
- name: ContainerThrottlingData
  property_count: 3
  slug: azure-function-apps-container-throttling-data
- name: ContinuousWebJob
  property_count: 1
  slug: azure-function-apps-continuous-web-job
json_structures:
- name: Azure Function Apps Api Kv Reference Structure
  property_count: 9
  slug: azure-function-apps-api-kv-reference-structure
- name: Azure Function Apps Application Logs Config Structure
  property_count: 3
  slug: azure-function-apps-application-logs-config-structure
- name: Azure Function Apps Azure Blob Storage Application Logs Config Structure
  property_count: 3
  slug: azure-function-apps-azure-blob-storage-application-logs-config-structure
- name: Azure Function Apps Azure Blob Storage Http Logs Config Structure
  property_count: 3
  slug: azure-function-apps-azure-blob-storage-http-logs-config-structure
- name: Azure Function Apps Azure Storage Info Value Structure
  property_count: 6
  slug: azure-function-apps-azure-storage-info-value-structure
- name: Azure Function Apps Azure Storage Property Dictionary Resource Structure
  property_count: 1
  slug: azure-function-apps-azure-storage-property-dictionary-resource-structure
- name: Azure Function Apps Azure Table Storage Application Logs Config Structure
  property_count: 2
  slug: azure-function-apps-azure-table-storage-application-logs-config-structure
- name: Azure Function Apps Backup Item Collection Structure
  property_count: 2
  slug: azure-function-apps-backup-item-collection-structure
- name: Azure Function Apps Backup Item Structure
  property_count: 1
  slug: azure-function-apps-backup-item-structure
- name: Azure Function Apps Backup Request Structure
  property_count: 1
  slug: azure-function-apps-backup-request-structure
- name: Azure Function Apps Backup Schedule Structure
  property_count: 6
  slug: azure-function-apps-backup-schedule-structure
- name: Azure Function Apps Conn String Value Type Pair Structure
  property_count: 2
  slug: azure-function-apps-conn-string-value-type-pair-structure
- name: Azure Function Apps Connection String Dictionary Structure
  property_count: 1
  slug: azure-function-apps-connection-string-dictionary-structure
- name: Azure Function Apps Container Cpu Statistics Structure
  property_count: 4
  slug: azure-function-apps-container-cpu-statistics-structure
- name: Azure Function Apps Container Cpu Usage Structure
  property_count: 4
  slug: azure-function-apps-container-cpu-usage-structure
- name: Azure Function Apps Container Info Structure
  property_count: 8
  slug: azure-function-apps-container-info-structure
- name: Azure Function Apps Container Memory Statistics Structure
  property_count: 3
  slug: azure-function-apps-container-memory-statistics-structure
- name: Azure Function Apps Container Network Interface Statistics Structure
  property_count: 8
  slug: azure-function-apps-container-network-interface-statistics-structure
- name: Azure Function Apps Container Throttling Data Structure
  property_count: 3
  slug: azure-function-apps-container-throttling-data-structure
- name: Azure Function Apps Continuous Web Job Structure
  property_count: 1
  slug: azure-function-apps-continuous-web-job-structure
jsonld:
- class_count: 21
  name: Azure Function Apps Context
  property_count: 60
  slug: azure-function-apps-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Azure Function Apps
nav: Providers
network: true
overview: 'Azure Function Apps publishes 1 API on the [APIs.io](https://apis.io/) network: WebApps API. Tagged areas include Azure, Compute, Function-as-a-Service, Functions, and Serverless.


  The Azure Function Apps catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Azure Function Apps'' developer surface includes developer portal, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Azure Function Apps Plans Pricing
  plan_count: 3
  slug: azure-function-apps-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Azure Function Apps Rate Limits
  slug: azure-function-apps-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Azure Function Apps API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: azure-function-apps-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Azure Function Apps API Rules
  rule_count: 18
  severity_counts:
    error: 5
    hint: 0
    info: 4
    warn: 9
  slug: azure-function-apps-spectral-rules
score:
  band: developing
  composite: 44.1
  delta: 4.8
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.8
    contract_quality: 55.8
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-function-apps/refs/heads/main/screenshots/azure-function-apps-2026-06-20T172854.png
security:
- kind: domain-security
  name: Azure Function Apps Domain Security
  slug: azure-function-apps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azure-function-apps
tags:
- Azure
- Compute
- Function-as-a-Service
- Functions
- Serverless
website: https://portal.azure.com
---
