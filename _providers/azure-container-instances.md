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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Azure Container Instances Agentic Access
  operation_count: 16
  slug: azure-container-instances-agentic-access
  summary_line: 16 operations · 8 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The Operations API from Azure Container Instances — 1 operation(s) for operations.
  name: Azure Container Instances Operations API
  slug: azure-container-instances-operations-api
- description: The Subscriptions API from Azure Container Instances — 12 operation(s) for subscriptions.
  name: Azure Container Instances Subscriptions API
  slug: azure-container-instances-subscriptions-api
artifact_total: 97
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-container-instances-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-container-instances-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-container-instances-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-container-instances-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-container-instances-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/container-instances
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/container-instances/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/container-instances/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/azure-container-instances/refs/heads/main/rules/azure-container-instances-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/azure-container-instances/refs/heads/main/vocabulary/azure-container-instances-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/azure-container-instances/refs/heads/main/json-ld/azure-container-instances-context.jsonld
created: '2026-03-26'
description: Azure Container Instances (ACI) is the fastest and simplest way to run containers in Azure without having to manage virtual machines or adopt a higher-level orchestration service. It offers serverless containers with per-second billing, custom sizes, and seamless integration with the Azure ecosystem for burst and event-driven workloads.
examples:
- key_count: 4
  name: Azure Container Instances Azure File Volume Example
  slug: azure-container-instances-azure-file-volume-example
- key_count: 2
  name: Azure Container Instances Cached Images List Result Example
  slug: azure-container-instances-cached-images-list-result-example
- key_count: 6
  name: Azure Container Instances Capabilities Example
  slug: azure-container-instances-capabilities-example
- key_count: 2
  name: Azure Container Instances Capabilities List Result Example
  slug: azure-container-instances-capabilities-list-result-example
- key_count: 1
  name: Azure Container Instances Container Example
  slug: azure-container-instances-container-example
- key_count: 1
  name: Azure Container Instances Container Exec Example
  slug: azure-container-instances-container-exec-example
- key_count: 2
  name: Azure Container Instances Container Exec Request Example
  slug: azure-container-instances-container-exec-request-example
- key_count: 2
  name: Azure Container Instances Container Exec Response Example
  slug: azure-container-instances-container-exec-response-example
- key_count: 0
  name: Azure Container Instances Container Group Diagnostics Example
  slug: azure-container-instances-container-group-diagnostics-example
- key_count: 0
  name: Azure Container Instances Container Group Example
  slug: azure-container-instances-container-group-example
- key_count: 4
  name: Azure Container Instances Container Group Identity Example
  slug: azure-container-instances-container-group-identity-example
- key_count: 2
  name: Azure Container Instances Container Group List Result Example
  slug: azure-container-instances-container-group-list-result-example
- key_count: 1
  name: Azure Container Instances Container Group Network Profile Example
  slug: azure-container-instances-container-group-network-profile-example
- key_count: 3
  name: Azure Container Instances Container Http Get Example
  slug: azure-container-instances-container-http-get-example
- key_count: 2
  name: Azure Container Instances Container Port Example
  slug: azure-container-instances-container-port-example
- key_count: 5
  name: Azure Container Instances Container Probe Example
  slug: azure-container-instances-container-probe-example
- key_count: 6
  name: Azure Container Instances Container Properties Example
  slug: azure-container-instances-container-properties-example
- key_count: 5
  name: Azure Container Instances Container State Example
  slug: azure-container-instances-container-state-example
- key_count: 3
  name: Azure Container Instances Dns Configuration Example
  slug: azure-container-instances-dns-configuration-example
- key_count: 0
  name: Azure Container Instances Empty Dir Volume Example
  slug: azure-container-instances-empty-dir-volume-example
- key_count: 3
  name: Azure Container Instances Environment Variable Example
  slug: azure-container-instances-environment-variable-example
- key_count: 6
  name: Azure Container Instances Event Example
  slug: azure-container-instances-event-example
- key_count: 3
  name: Azure Container Instances Git Repo Volume Example
  slug: azure-container-instances-git-repo-volume-example
- key_count: 2
  name: Azure Container Instances Gpu Resource Example
  slug: azure-container-instances-gpu-resource-example
- key_count: 3
  name: Azure Container Instances Image Registry Credential Example
  slug: azure-container-instances-image-registry-credential-example
- key_count: 5
  name: Azure Container Instances Ip Address Example
  slug: azure-container-instances-ip-address-example
- key_count: 4
  name: Azure Container Instances Log Analytics Example
  slug: azure-container-instances-log-analytics-example
- key_count: 1
  name: Azure Container Instances Logs Example
  slug: azure-container-instances-logs-example
finops:
- name: Azure Container Instances Finops
  service_category: API
  slug: azure-container-instances-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-container-instances.png
json_schemas:
- name: AzureFileVolume
  property_count: 4
  slug: azure-container-instances-azure-file-volume
- name: CachedImagesListResult
  property_count: 2
  slug: azure-container-instances-cached-images-list-result
- name: CapabilitiesListResult
  property_count: 2
  slug: azure-container-instances-capabilities-list-result
- name: Capabilities
  property_count: 6
  slug: azure-container-instances-capabilities
- name: ContainerExecRequest
  property_count: 2
  slug: azure-container-instances-container-exec-request
- name: ContainerExecResponse
  property_count: 2
  slug: azure-container-instances-container-exec-response
- name: ContainerExec
  property_count: 1
  slug: azure-container-instances-container-exec
- name: ContainerGroupDiagnostics
  property_count: 1
  slug: azure-container-instances-container-group-diagnostics
- name: ContainerGroupIdentity
  property_count: 4
  slug: azure-container-instances-container-group-identity
- name: ContainerGroupListResult
  property_count: 2
  slug: azure-container-instances-container-group-list-result
- name: ContainerGroupNetworkProfile
  property_count: 1
  slug: azure-container-instances-container-group-network-profile
- name: ContainerGroup
  property_count: 0
  slug: azure-container-instances-container-group
- name: ContainerHttpGet
  property_count: 3
  slug: azure-container-instances-container-http-get
- name: ContainerPort
  property_count: 2
  slug: azure-container-instances-container-port
- name: ContainerProbe
  property_count: 7
  slug: azure-container-instances-container-probe
- name: ContainerProperties
  property_count: 9
  slug: azure-container-instances-container-properties
- name: Container
  property_count: 2
  slug: azure-container-instances-container
- name: ContainerState
  property_count: 5
  slug: azure-container-instances-container-state
- name: DnsConfiguration
  property_count: 3
  slug: azure-container-instances-dns-configuration
- name: EmptyDirVolume
  property_count: 0
  slug: azure-container-instances-empty-dir-volume
- name: EnvironmentVariable
  property_count: 3
  slug: azure-container-instances-environment-variable
- name: Event
  property_count: 6
  slug: azure-container-instances-event
- name: GitRepoVolume
  property_count: 3
  slug: azure-container-instances-git-repo-volume
- name: GpuResource
  property_count: 2
  slug: azure-container-instances-gpu-resource
- name: ImageRegistryCredential
  property_count: 3
  slug: azure-container-instances-image-registry-credential
- name: IpAddress
  property_count: 5
  slug: azure-container-instances-ip-address
- name: LogAnalytics
  property_count: 4
  slug: azure-container-instances-log-analytics
- name: Logs
  property_count: 1
  slug: azure-container-instances-logs
json_structures:
- name: Azure Container Instances Azure File Volume Structure
  property_count: 4
  slug: azure-container-instances-azure-file-volume-structure
- name: Azure Container Instances Cached Images List Result Structure
  property_count: 2
  slug: azure-container-instances-cached-images-list-result-structure
- name: Azure Container Instances Capabilities List Result Structure
  property_count: 2
  slug: azure-container-instances-capabilities-list-result-structure
- name: Azure Container Instances Capabilities Structure
  property_count: 6
  slug: azure-container-instances-capabilities-structure
- name: Azure Container Instances Container Exec Request Structure
  property_count: 2
  slug: azure-container-instances-container-exec-request-structure
- name: Azure Container Instances Container Exec Response Structure
  property_count: 2
  slug: azure-container-instances-container-exec-response-structure
- name: Azure Container Instances Container Exec Structure
  property_count: 1
  slug: azure-container-instances-container-exec-structure
- name: Azure Container Instances Container Group Diagnostics Structure
  property_count: 1
  slug: azure-container-instances-container-group-diagnostics-structure
- name: Azure Container Instances Container Group Identity Structure
  property_count: 4
  slug: azure-container-instances-container-group-identity-structure
- name: Azure Container Instances Container Group List Result Structure
  property_count: 2
  slug: azure-container-instances-container-group-list-result-structure
- name: Azure Container Instances Container Group Network Profile Structure
  property_count: 1
  slug: azure-container-instances-container-group-network-profile-structure
- name: Azure Container Instances Container Group Structure
  property_count: 0
  slug: azure-container-instances-container-group-structure
- name: Azure Container Instances Container Http Get Structure
  property_count: 3
  slug: azure-container-instances-container-http-get-structure
- name: Azure Container Instances Container Port Structure
  property_count: 2
  slug: azure-container-instances-container-port-structure
- name: Azure Container Instances Container Probe Structure
  property_count: 7
  slug: azure-container-instances-container-probe-structure
- name: Azure Container Instances Container Properties Structure
  property_count: 9
  slug: azure-container-instances-container-properties-structure
- name: Azure Container Instances Container State Structure
  property_count: 5
  slug: azure-container-instances-container-state-structure
- name: Azure Container Instances Container Structure
  property_count: 2
  slug: azure-container-instances-container-structure
- name: Azure Container Instances Dns Configuration Structure
  property_count: 3
  slug: azure-container-instances-dns-configuration-structure
- name: Azure Container Instances Empty Dir Volume Structure
  property_count: 0
  slug: azure-container-instances-empty-dir-volume-structure
- name: Azure Container Instances Environment Variable Structure
  property_count: 3
  slug: azure-container-instances-environment-variable-structure
- name: Azure Container Instances Event Structure
  property_count: 6
  slug: azure-container-instances-event-structure
- name: Azure Container Instances Git Repo Volume Structure
  property_count: 3
  slug: azure-container-instances-git-repo-volume-structure
- name: Azure Container Instances Gpu Resource Structure
  property_count: 2
  slug: azure-container-instances-gpu-resource-structure
- name: Azure Container Instances Image Registry Credential Structure
  property_count: 3
  slug: azure-container-instances-image-registry-credential-structure
- name: Azure Container Instances Ip Address Structure
  property_count: 5
  slug: azure-container-instances-ip-address-structure
- name: Azure Container Instances Log Analytics Structure
  property_count: 4
  slug: azure-container-instances-log-analytics-structure
- name: Azure Container Instances Logs Structure
  property_count: 1
  slug: azure-container-instances-logs-structure
jsonld:
- class_count: 20
  name: Azure Container Instances Context
  property_count: 50
  slug: azure-container-instances-context
layout: provider
modified: '2026-05-19'
name: Azure Container Instances
nav: Providers
network: true
overview: 'Azure Container Instances publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Subscriptions API. Tagged areas include Azure, Cloud, Container Instances, Containers, and Microsoft.


  The Azure Container Instances catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Azure Container Instances'' developer surface includes authentication, documentation, pricing, engineering blog, signup flow, support, and 10 more developer resources.'
plans:
- name: Azure Container Instances Plans Pricing
  plan_count: 3
  slug: azure-container-instances-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 5
  name: Azure Container Instances Rate Limits
  slug: azure-container-instances-rate-limits
rules:
- name: Azure Container Instances API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: azure-container-instances-jsonschema-spectral-rules
- name: Azure Container Instances API Rules
  rule_count: 18
  severity_counts:
    error: 5
    hint: 0
    info: 4
    warn: 9
  slug: azure-container-instances-spectral-rules
scopes:
- name: Azure Container Instances Scopes
  scope_count: 1
  slug: azure-container-instances-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 55.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.5
    developer_ergonomics: 26.1
    discoverability: 80.0
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 55.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-container-instances/refs/heads/main/screenshots/azure-container-instances-2026-06-20T172844.png
security:
- kind: authentication
  name: Azure Container Instances Authentication
  slug: azure-container-instances-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Azure Container Instances Domain Security
  slug: azure-container-instances-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Azure Container Instances Vulnerability Disclosure
  slug: azure-container-instances-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: azure-container-instances
tags:
- Azure
- Cloud
- Container Instances
- Containers
- Microsoft
- Serverless
website: https://azure.microsoft.com/en-us/products/container-instances
---
