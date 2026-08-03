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
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
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
  score: 52.3
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Azure Agentic Access
  operation_count: 5
  slug: azure-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 3
apis:
- description: Manage Azure resource groups
  name: Microsoft Azure Resource Groups API
  slug: azure-resource-groups-api
- description: Manage Azure resources
  name: Microsoft Azure Resources API
  slug: azure-resources-api
- description: Manage Azure subscriptions
  name: Microsoft Azure Subscriptions API
  slug: azure-subscriptions-api
artifact_total: 45
collections:
- collection_type: postman
  name: Microsoft Azure Management Resource Groups API
  slug: postman-azure-resource-groups-api
- collection_type: postman
  name: Microsoft Azure Management Resource Groups Resources API
  slug: postman-azure-resources-api
- collection_type: postman
  name: Microsoft Azure Management Resource Groups Subscriptions API
  slug: postman-azure-subscriptions-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-azure/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
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
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/azure/refs/heads/main/rules/azure-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/azure/refs/heads/main/vocabulary/azure-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/azure/refs/heads/main/json-ld/azure-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Azure/azure-mcp
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/Azure/amg-skills
created: '2024-01-01'
description: Microsoft Azure is a comprehensive cloud computing platform offering IaaS, PaaS, and SaaS solutions for building, deploying, and managing applications through Microsoft's global network of datacenters.
examples:
- key_count: 8
  name: Azure Generic Resource Example
  slug: azure-generic-resource-example
- key_count: 6
  name: Azure Resource Group Example
  slug: azure-resource-group-example
- key_count: 2
  name: Azure Resource Group List Result Example
  slug: azure-resource-group-list-result-example
- key_count: 2
  name: Azure Resource List Result Example
  slug: azure-resource-list-result-example
- key_count: 7
  name: Azure Subscription Example
  slug: azure-subscription-example
- key_count: 2
  name: Azure Subscription List Result Example
  slug: azure-subscription-list-result-example
finops:
- name: Azure Finops
  service_category: Cloud Infrastructure
  slug: azure-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure.png
json_schemas:
- name: GenericResource
  property_count: 8
  slug: azure-generic-resource
- name: ResourceGroupListResult
  property_count: 2
  slug: azure-resource-group-list-result
- name: ResourceGroup
  property_count: 6
  slug: azure-resource-group
- name: ResourceListResult
  property_count: 2
  slug: azure-resource-list-result
- name: SubscriptionListResult
  property_count: 2
  slug: azure-subscription-list-result
- name: Subscription
  property_count: 7
  slug: azure-subscription
json_structures:
- name: Azure Generic Resource Structure
  property_count: 8
  slug: azure-generic-resource-structure
- name: Azure Resource Group List Result Structure
  property_count: 2
  slug: azure-resource-group-list-result-structure
- name: Azure Resource Group Structure
  property_count: 6
  slug: azure-resource-group-structure
- name: Azure Resource List Result Structure
  property_count: 2
  slug: azure-resource-list-result-structure
- name: Azure Subscription List Result Structure
  property_count: 2
  slug: azure-subscription-list-result-structure
- name: Azure Subscription Structure
  property_count: 7
  slug: azure-subscription-structure
jsonld:
- class_count: 7
  name: Azure Context
  property_count: 16
  slug: azure-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Microsoft Azure
nav: Providers
network: true
overview: 'Microsoft Azure publishes 3 APIs on the [APIs.io](https://apis.io/) network: Resource Groups API, Resources API, and Subscriptions API. Tagged areas include Cloud Computing, Databases, Infrastructure, Machine Learning, and Networking.


  The Microsoft Azure catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Microsoft Azure''s developer surface includes authentication, developer portal, documentation, support, engineering blog, signup flow, and 14 more developer resources.'
plans:
- name: Azure Plans Pricing
  plan_count: 5
  slug: azure-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 4
  name: Azure Rate Limits
  slug: azure-rate-limits
rules:
- name: Microsoft Azure API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: azure-jsonschema-spectral-rules
- name: Microsoft Azure API Rules
  rule_count: 21
  severity_counts:
    error: 5
    hint: 0
    info: 5
    warn: 11
  slug: azure-spectral-rules
scopes:
- name: Azure Scopes
  scope_count: 1
  slug: azure-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 49.9
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 22.9
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 49.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure/refs/heads/main/screenshots/azure-2026-06-20T172833.png
security:
- kind: authentication
  name: Azure Authentication
  slug: azure-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Azure Domain Security
  slug: azure-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 10
skills:
- name: amg-check-azure-spend
  slug: amg-check-azure-spend-2
- name: amg-check-azure-spend
  slug: amg-check-azure-spend
- name: amg-check-cosmosdb-mongo-ru
  slug: amg-check-cosmosdb-mongo-ru-2
- name: amg-check-cosmosdb-mongo-ru
  slug: amg-check-cosmosdb-mongo-ru
- name: amg-check-key-vault
  slug: amg-check-key-vault-2
- name: amg-check-key-vault
  slug: amg-check-key-vault
- name: amg-check-pg-flex
  slug: amg-check-pg-flex-2
- name: amg-check-pg-flex
  slug: amg-check-pg-flex
- name: amg-check-storage-account
  slug: amg-check-storage-account-2
- name: amg-check-storage-account
  slug: amg-check-storage-account
slug: azure
tags:
- Cloud Computing
- Databases
- Infrastructure
- Machine Learning
- Networking
- Platform as a Service
- Storage
website: https://portal.azure.com
---
