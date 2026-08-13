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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Azure Functions Agentic Access
  operation_count: 37
  slug: azure-functions-agentic-access
  summary_line: 37 operations · 26 acting
api_count: 1
apis:
- description: The WebApps API from Azure Functions — 30 operation(s) for webapps.
  name: Azure Functions WebApps API
  slug: azure-functions-webapps-api
artifact_total: 70
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-functions-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-functions-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/azure-functions/
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/azure-functions/bg-p/AzureFunctionsBlog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/options/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure/Azure-Functions
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/azure-functions/refs/heads/main/rules/azure-functions-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/azure-functions/refs/heads/main/vocabulary/azure-functions-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/azure-functions/refs/heads/main/json-ld/azure-functions-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Azure/azure-functions-mcp-extension
created: '2024-01-01'
description: Azure Functions is a serverless compute service that lets you run event-triggered code without having to explicitly provision or manage infrastructure, supporting multiple programming languages and integration patterns.
examples:
- key_count: 9
  name: Azure Functions Api Kv Reference Example
  slug: azure-functions-api-kv-reference-example
- key_count: 0
  name: Azure Functions Application Logs Config Example
  slug: azure-functions-application-logs-config-example
- key_count: 3
  name: Azure Functions Azure Blob Storage Application Logs Config Example
  slug: azure-functions-azure-blob-storage-application-logs-config-example
- key_count: 3
  name: Azure Functions Azure Blob Storage Http Logs Config Example
  slug: azure-functions-azure-blob-storage-http-logs-config-example
- key_count: 6
  name: Azure Functions Azure Storage Info Value Example
  slug: azure-functions-azure-storage-info-value-example
- key_count: 1
  name: Azure Functions Azure Storage Property Dictionary Resource Example
  slug: azure-functions-azure-storage-property-dictionary-resource-example
- key_count: 2
  name: Azure Functions Azure Table Storage Application Logs Config Example
  slug: azure-functions-azure-table-storage-application-logs-config-example
- key_count: 2
  name: Azure Functions Backup Item Collection Example
  slug: azure-functions-backup-item-collection-example
- key_count: 1
  name: Azure Functions Backup Item Example
  slug: azure-functions-backup-item-example
- key_count: 1
  name: Azure Functions Backup Request Example
  slug: azure-functions-backup-request-example
- key_count: 6
  name: Azure Functions Backup Schedule Example
  slug: azure-functions-backup-schedule-example
- key_count: 2
  name: Azure Functions Conn String Value Type Pair Example
  slug: azure-functions-conn-string-value-type-pair-example
- key_count: 1
  name: Azure Functions Connection String Dictionary Example
  slug: azure-functions-connection-string-dictionary-example
- key_count: 2
  name: Azure Functions Container Cpu Statistics Example
  slug: azure-functions-container-cpu-statistics-example
- key_count: 4
  name: Azure Functions Container Cpu Usage Example
  slug: azure-functions-container-cpu-usage-example
- key_count: 4
  name: Azure Functions Container Info Example
  slug: azure-functions-container-info-example
- key_count: 3
  name: Azure Functions Container Memory Statistics Example
  slug: azure-functions-container-memory-statistics-example
- key_count: 8
  name: Azure Functions Container Network Interface Statistics Example
  slug: azure-functions-container-network-interface-statistics-example
- key_count: 3
  name: Azure Functions Container Throttling Data Example
  slug: azure-functions-container-throttling-data-example
- key_count: 1
  name: Azure Functions Continuous Web Job Example
  slug: azure-functions-continuous-web-job-example
finops:
- name: Azure Functions Finops
  service_category: API
  slug: azure-functions-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-functions.png
json_schemas:
- name: ApiKVReference
  property_count: 9
  slug: azure-functions-api-kv-reference
- name: ApplicationLogsConfig
  property_count: 3
  slug: azure-functions-application-logs-config
- name: AzureBlobStorageApplicationLogsConfig
  property_count: 3
  slug: azure-functions-azure-blob-storage-application-logs-config
- name: AzureBlobStorageHttpLogsConfig
  property_count: 3
  slug: azure-functions-azure-blob-storage-http-logs-config
- name: AzureStorageInfoValue
  property_count: 6
  slug: azure-functions-azure-storage-info-value
- name: AzureStoragePropertyDictionaryResource
  property_count: 1
  slug: azure-functions-azure-storage-property-dictionary-resource
- name: AzureTableStorageApplicationLogsConfig
  property_count: 2
  slug: azure-functions-azure-table-storage-application-logs-config
- name: BackupItemCollection
  property_count: 2
  slug: azure-functions-backup-item-collection
- name: BackupItem
  property_count: 1
  slug: azure-functions-backup-item
- name: BackupRequest
  property_count: 1
  slug: azure-functions-backup-request
- name: BackupSchedule
  property_count: 6
  slug: azure-functions-backup-schedule
- name: ConnStringValueTypePair
  property_count: 2
  slug: azure-functions-conn-string-value-type-pair
- name: ConnectionStringDictionary
  property_count: 1
  slug: azure-functions-connection-string-dictionary
- name: ContainerCpuStatistics
  property_count: 4
  slug: azure-functions-container-cpu-statistics
- name: ContainerCpuUsage
  property_count: 4
  slug: azure-functions-container-cpu-usage
- name: ContainerInfo
  property_count: 8
  slug: azure-functions-container-info
- name: ContainerMemoryStatistics
  property_count: 3
  slug: azure-functions-container-memory-statistics
- name: ContainerNetworkInterfaceStatistics
  property_count: 8
  slug: azure-functions-container-network-interface-statistics
- name: ContainerThrottlingData
  property_count: 3
  slug: azure-functions-container-throttling-data
- name: ContinuousWebJob
  property_count: 1
  slug: azure-functions-continuous-web-job
json_structures:
- name: Azure Functions Api Kv Reference Structure
  property_count: 9
  slug: azure-functions-api-kv-reference-structure
- name: Azure Functions Application Logs Config Structure
  property_count: 3
  slug: azure-functions-application-logs-config-structure
- name: Azure Functions Azure Blob Storage Application Logs Config Structure
  property_count: 3
  slug: azure-functions-azure-blob-storage-application-logs-config-structure
- name: Azure Functions Azure Blob Storage Http Logs Config Structure
  property_count: 3
  slug: azure-functions-azure-blob-storage-http-logs-config-structure
- name: Azure Functions Azure Storage Info Value Structure
  property_count: 6
  slug: azure-functions-azure-storage-info-value-structure
- name: Azure Functions Azure Storage Property Dictionary Resource Structure
  property_count: 1
  slug: azure-functions-azure-storage-property-dictionary-resource-structure
- name: Azure Functions Azure Table Storage Application Logs Config Structure
  property_count: 2
  slug: azure-functions-azure-table-storage-application-logs-config-structure
- name: Azure Functions Backup Item Collection Structure
  property_count: 2
  slug: azure-functions-backup-item-collection-structure
- name: Azure Functions Backup Item Structure
  property_count: 1
  slug: azure-functions-backup-item-structure
- name: Azure Functions Backup Request Structure
  property_count: 1
  slug: azure-functions-backup-request-structure
- name: Azure Functions Backup Schedule Structure
  property_count: 6
  slug: azure-functions-backup-schedule-structure
- name: Azure Functions Conn String Value Type Pair Structure
  property_count: 2
  slug: azure-functions-conn-string-value-type-pair-structure
- name: Azure Functions Connection String Dictionary Structure
  property_count: 1
  slug: azure-functions-connection-string-dictionary-structure
- name: Azure Functions Container Cpu Statistics Structure
  property_count: 4
  slug: azure-functions-container-cpu-statistics-structure
- name: Azure Functions Container Cpu Usage Structure
  property_count: 4
  slug: azure-functions-container-cpu-usage-structure
- name: Azure Functions Container Info Structure
  property_count: 8
  slug: azure-functions-container-info-structure
- name: Azure Functions Container Memory Statistics Structure
  property_count: 3
  slug: azure-functions-container-memory-statistics-structure
- name: Azure Functions Container Network Interface Statistics Structure
  property_count: 8
  slug: azure-functions-container-network-interface-statistics-structure
- name: Azure Functions Container Throttling Data Structure
  property_count: 3
  slug: azure-functions-container-throttling-data-structure
- name: Azure Functions Continuous Web Job Structure
  property_count: 1
  slug: azure-functions-continuous-web-job-structure
jsonld:
- class_count: 21
  name: Azure Functions Context
  property_count: 60
  slug: azure-functions-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Azure Functions
nav: Providers
network: true
overview: 'Azure Functions publishes 1 API on the [APIs.io](https://apis.io/) network: WebApps API. Tagged areas include Cloud, Compute, Event-Driven, Functions, and Serverless.


  The Azure Functions catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Azure Functions'' developer surface includes developer portal, documentation, engineering blog, support, and 10 more developer resources.'
plans:
- name: Azure Functions Plans Pricing
  plan_count: 3
  slug: azure-functions-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Azure Functions Rate Limits
  slug: azure-functions-rate-limits
rules:
- name: Azure Functions API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: azure-functions-jsonschema-spectral-rules
- name: Azure Functions API Rules
  rule_count: 18
  severity_counts:
    error: 5
    hint: 0
    info: 4
    warn: 9
  slug: azure-functions-spectral-rules
score:
  band: developing
  composite: 47.5
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 59.0
    developer_ergonomics: 32.6
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 28.9
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-functions/refs/heads/main/screenshots/azure-functions-2026-06-20T172856.png
security:
- kind: domain-security
  name: Azure Functions Domain Security
  slug: azure-functions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azure-functions
tags:
- Cloud
- Compute
- Event-Driven
- Functions
- Serverless
website: https://portal.azure.com
---
