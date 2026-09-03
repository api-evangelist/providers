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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Azure Container Registry Agentic Access
  operation_count: 25
  slug: azure-container-registry-agentic-access
  summary_line: 25 operations · 16 acting
api_count: 1
apis:
- baseURL: https://management.azure.com
  baseurl_source: spec
  description: The Operation API from Azure Container Registry — 2 operation(s) for operation.
  name: Azure Container Registry Operation API
  slug: azure-container-registry-operation-api
- baseURL: https://management.azure.com
  baseurl_source: spec
  description: The Registries API from Azure Container Registry — 7 operation(s) for registries.
  name: Azure Container Registry Registries API
  slug: azure-container-registry-registries-api
- baseURL: https://management.azure.com
  baseurl_source: spec
  description: The Replications API from Azure Container Registry — 2 operation(s) for replications.
  name: Azure Container Registry Replications API
  slug: azure-container-registry-replications-api
- baseURL: https://management.azure.com
  baseurl_source: spec
  description: The Webhooks API from Azure Container Registry — 5 operation(s) for webhooks.
  name: Azure Container Registry Webhooks API
  slug: azure-container-registry-webhooks-api
artifact_total: 107
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ContainerRegistryManagementClient Operation API
  slug: open-azure-container-registry-operation-api
- collection_type: open
  name: ContainerRegistryManagementClient Operation Registries API
  slug: open-azure-container-registry-registries-api
- collection_type: open
  name: ContainerRegistryManagementClient Operation Replications API
  slug: open-azure-container-registry-replications-api
- collection_type: open
  name: ContainerRegistryManagementClient Operation Webhooks API
  slug: open-azure-container-registry-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-container-registry-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-container-registry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-container-registry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-container-registry-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-container-registry-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/container-registry
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/container-registry/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/container-registry/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/azure-container-registry/refs/heads/main/rules/azure-container-registry-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/azure-container-registry/refs/heads/main/vocabulary/azure-container-registry-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/azure-container-registry/refs/heads/main/json-ld/azure-container-registry-context.jsonld
created: '2026-03-26'
description: Azure Container Registry is a managed Docker registry service based on the open-source Docker Registry for storing and managing private container images and artifacts. It supports automated container image builds, geo-replication, and integrates with Azure Kubernetes Service and other Azure deployment targets.
examples:
- key_count: 1
  name: Azure Container Registry Actor Example
  slug: azure-container-registry-actor-example
- key_count: 2
  name: Azure Container Registry Callback Config Example
  slug: azure-container-registry-callback-config-example
- key_count: 1
  name: Azure Container Registry Encryption Property Example
  slug: azure-container-registry-encryption-property-example
- key_count: 3
  name: Azure Container Registry Event Content Example
  slug: azure-container-registry-event-content-example
- key_count: 0
  name: Azure Container Registry Event Example
  slug: azure-container-registry-event-example
- key_count: 1
  name: Azure Container Registry Event Info Example
  slug: azure-container-registry-event-info-example
- key_count: 2
  name: Azure Container Registry Event List Result Example
  slug: azure-container-registry-event-list-result-example
- key_count: 4
  name: Azure Container Registry Event Request Message Example
  slug: azure-container-registry-event-request-message-example
- key_count: 5
  name: Azure Container Registry Event Response Message Example
  slug: azure-container-registry-event-response-message-example
- key_count: 4
  name: Azure Container Registry Identity Properties Example
  slug: azure-container-registry-identity-properties-example
- key_count: 3
  name: Azure Container Registry Import Image Parameters Example
  slug: azure-container-registry-import-image-parameters-example
- key_count: 2
  name: Azure Container Registry Import Source Credentials Example
  slug: azure-container-registry-import-source-credentials-example
- key_count: 3
  name: Azure Container Registry Import Source Example
  slug: azure-container-registry-import-source-example
- key_count: 2
  name: Azure Container Registry Ip Rule Example
  slug: azure-container-registry-ip-rule-example
- key_count: 2
  name: Azure Container Registry Key Vault Properties Example
  slug: azure-container-registry-key-vault-properties-example
- key_count: 3
  name: Azure Container Registry Network Rule Set Example
  slug: azure-container-registry-network-rule-set-example
- key_count: 2
  name: Azure Container Registry Operation Definition Example
  slug: azure-container-registry-operation-definition-example
- key_count: 4
  name: Azure Container Registry Operation Display Definition Example
  slug: azure-container-registry-operation-display-definition-example
- key_count: 6
  name: Azure Container Registry Operation Metric Specification Definition Example
  slug: azure-container-registry-operation-metric-specification-definition-example
- key_count: 0
  name: Azure Container Registry Operation Properties Definition Example
  slug: azure-container-registry-operation-properties-definition-example
- key_count: 1
  name: Azure Container Registry Operation Service Specification Definition Example
  slug: azure-container-registry-operation-service-specification-definition-example
- key_count: 0
  name: Azure Container Registry Policies Example
  slug: azure-container-registry-policies-example
- key_count: 1
  name: Azure Container Registry Quarantine Policy Example
  slug: azure-container-registry-quarantine-policy-example
- key_count: 1
  name: Azure Container Registry Regenerate Credential Parameters Example
  slug: azure-container-registry-regenerate-credential-parameters-example
- key_count: 0
  name: Azure Container Registry Registry Example
  slug: azure-container-registry-registry-example
- key_count: 2
  name: Azure Container Registry Registry List Credentials Result Example
  slug: azure-container-registry-registry-list-credentials-result-example
- key_count: 2
  name: Azure Container Registry Registry List Result Example
  slug: azure-container-registry-registry-list-result-example
- key_count: 2
  name: Azure Container Registry Registry Name Check Request Example
  slug: azure-container-registry-registry-name-check-request-example
- key_count: 3
  name: Azure Container Registry Registry Name Status Example
  slug: azure-container-registry-registry-name-status-example
finops:
- name: Azure Container Registry Finops
  service_category: API
  slug: azure-container-registry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-container-registry.png
json_schemas:
- name: Actor
  property_count: 1
  slug: azure-container-registry-actor
- name: CallbackConfig
  property_count: 2
  slug: azure-container-registry-callback-config
- name: EncryptionProperty
  property_count: 2
  slug: azure-container-registry-encryption-property
- name: EventContent
  property_count: 7
  slug: azure-container-registry-event-content
- name: EventInfo
  property_count: 1
  slug: azure-container-registry-event-info
- name: EventListResult
  property_count: 2
  slug: azure-container-registry-event-list-result
- name: EventRequestMessage
  property_count: 5
  slug: azure-container-registry-event-request-message
- name: EventResponseMessage
  property_count: 5
  slug: azure-container-registry-event-response-message
- name: Event
  property_count: 2
  slug: azure-container-registry-event
- name: IdentityProperties
  property_count: 4
  slug: azure-container-registry-identity-properties
- name: ImportImageParameters
  property_count: 4
  slug: azure-container-registry-import-image-parameters
- name: ImportSourceCredentials
  property_count: 2
  slug: azure-container-registry-import-source-credentials
- name: ImportSource
  property_count: 4
  slug: azure-container-registry-import-source
- name: IPRule
  property_count: 2
  slug: azure-container-registry-ip-rule
- name: KeyVaultProperties
  property_count: 2
  slug: azure-container-registry-key-vault-properties
- name: NetworkRuleSet
  property_count: 3
  slug: azure-container-registry-network-rule-set
- name: OperationDefinition
  property_count: 4
  slug: azure-container-registry-operation-definition
- name: OperationDisplayDefinition
  property_count: 4
  slug: azure-container-registry-operation-display-definition
- name: OperationMetricSpecificationDefinition
  property_count: 6
  slug: azure-container-registry-operation-metric-specification-definition
- name: OperationPropertiesDefinition
  property_count: 1
  slug: azure-container-registry-operation-properties-definition
- name: OperationServiceSpecificationDefinition
  property_count: 1
  slug: azure-container-registry-operation-service-specification-definition
- name: Policies
  property_count: 3
  slug: azure-container-registry-policies
- name: QuarantinePolicy
  property_count: 1
  slug: azure-container-registry-quarantine-policy
- name: RegenerateCredentialParameters
  property_count: 1
  slug: azure-container-registry-regenerate-credential-parameters
- name: RegistryListCredentialsResult
  property_count: 2
  slug: azure-container-registry-registry-list-credentials-result
- name: RegistryListResult
  property_count: 2
  slug: azure-container-registry-registry-list-result
- name: RegistryNameCheckRequest
  property_count: 2
  slug: azure-container-registry-registry-name-check-request
- name: RegistryNameStatus
  property_count: 3
  slug: azure-container-registry-registry-name-status
- name: Registry
  property_count: 3
  slug: azure-container-registry-registry
json_structures:
- name: Azure Container Registry Actor Structure
  property_count: 1
  slug: azure-container-registry-actor-structure
- name: Azure Container Registry Callback Config Structure
  property_count: 2
  slug: azure-container-registry-callback-config-structure
- name: Azure Container Registry Encryption Property Structure
  property_count: 2
  slug: azure-container-registry-encryption-property-structure
- name: Azure Container Registry Event Content Structure
  property_count: 7
  slug: azure-container-registry-event-content-structure
- name: Azure Container Registry Event Info Structure
  property_count: 1
  slug: azure-container-registry-event-info-structure
- name: Azure Container Registry Event List Result Structure
  property_count: 2
  slug: azure-container-registry-event-list-result-structure
- name: Azure Container Registry Event Request Message Structure
  property_count: 5
  slug: azure-container-registry-event-request-message-structure
- name: Azure Container Registry Event Response Message Structure
  property_count: 5
  slug: azure-container-registry-event-response-message-structure
- name: Azure Container Registry Event Structure
  property_count: 2
  slug: azure-container-registry-event-structure
- name: Azure Container Registry Identity Properties Structure
  property_count: 4
  slug: azure-container-registry-identity-properties-structure
- name: Azure Container Registry Import Image Parameters Structure
  property_count: 4
  slug: azure-container-registry-import-image-parameters-structure
- name: Azure Container Registry Import Source Credentials Structure
  property_count: 2
  slug: azure-container-registry-import-source-credentials-structure
- name: Azure Container Registry Import Source Structure
  property_count: 4
  slug: azure-container-registry-import-source-structure
- name: Azure Container Registry Ip Rule Structure
  property_count: 2
  slug: azure-container-registry-ip-rule-structure
- name: Azure Container Registry Key Vault Properties Structure
  property_count: 2
  slug: azure-container-registry-key-vault-properties-structure
- name: Azure Container Registry Network Rule Set Structure
  property_count: 3
  slug: azure-container-registry-network-rule-set-structure
- name: Azure Container Registry Operation Definition Structure
  property_count: 4
  slug: azure-container-registry-operation-definition-structure
- name: Azure Container Registry Operation Display Definition Structure
  property_count: 4
  slug: azure-container-registry-operation-display-definition-structure
- name: Azure Container Registry Operation Metric Specification Definition Structure
  property_count: 6
  slug: azure-container-registry-operation-metric-specification-definition-structure
- name: Azure Container Registry Operation Properties Definition Structure
  property_count: 1
  slug: azure-container-registry-operation-properties-definition-structure
- name: Azure Container Registry Operation Service Specification Definition Structure
  property_count: 1
  slug: azure-container-registry-operation-service-specification-definition-structure
- name: Azure Container Registry Policies Structure
  property_count: 3
  slug: azure-container-registry-policies-structure
- name: Azure Container Registry Quarantine Policy Structure
  property_count: 1
  slug: azure-container-registry-quarantine-policy-structure
- name: Azure Container Registry Regenerate Credential Parameters Structure
  property_count: 1
  slug: azure-container-registry-regenerate-credential-parameters-structure
- name: Azure Container Registry Registry List Credentials Result Structure
  property_count: 2
  slug: azure-container-registry-registry-list-credentials-result-structure
- name: Azure Container Registry Registry List Result Structure
  property_count: 2
  slug: azure-container-registry-registry-list-result-structure
- name: Azure Container Registry Registry Name Check Request Structure
  property_count: 2
  slug: azure-container-registry-registry-name-check-request-structure
- name: Azure Container Registry Registry Name Status Structure
  property_count: 3
  slug: azure-container-registry-registry-name-status-structure
- name: Azure Container Registry Registry Structure
  property_count: 3
  slug: azure-container-registry-registry-structure
jsonld:
- class_count: 22
  name: Azure Container Registry Context
  property_count: 52
  slug: azure-container-registry-context
layout: provider
modified: '2026-05-19'
name: Azure Container Registry
nav: Providers
network: true
overview: 'Azure Container Registry publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Operation API, Registries API, Replications API, and 1 more. Tagged areas include Azure, Container Images, Containers, Docker, and Registry.


  The Azure Container Registry catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Azure Container Registry''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, signup flow, and 10 more developer resources.'
plans:
- name: Azure Container Registry Plans Pricing
  plan_count: 3
  slug: azure-container-registry-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Azure Container Registry Rate Limits
  slug: azure-container-registry-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Azure Container Registry API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: azure-container-registry-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Azure Container Registry API Rules
  rule_count: 18
  severity_counts:
    error: 5
    hint: 0
    info: 4
    warn: 9
  slug: azure-container-registry-spectral-rules
scopes:
- name: Azure Container Registry Scopes
  scope_count: 1
  slug: azure-container-registry-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 55.1
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-container-registry/refs/heads/main/screenshots/azure-container-registry-2026-06-20T172845.png
security:
- kind: authentication
  name: Azure Container Registry Authentication
  slug: azure-container-registry-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Azure Container Registry Domain Security
  slug: azure-container-registry-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Azure Container Registry Vulnerability Disclosure
  slug: azure-container-registry-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: azure-container-registry
tags:
- Azure
- Container Images
- Containers
- Docker
- Registry
website: https://azure.microsoft.com/en-us/products/container-registry
---
