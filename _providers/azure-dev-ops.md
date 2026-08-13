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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Azure Dev Ops Agentic Access
  operation_count: 8
  slug: azure-dev-ops-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 3
apis:
- description: The Operations API from Azure DevOps — 1 operation(s) for operations.
  name: Azure DevOps Operations API
  slug: azure-dev-ops-operations-api
- description: The Pipelines API from Azure DevOps — 3 operation(s) for pipelines.
  name: Azure DevOps Pipelines API
  slug: azure-dev-ops-pipelines-api
- description: The PipelineTemplateDefinitions API from Azure DevOps — 1 operation(s) for pipelinetemplatedefinitions.
  name: Azure DevOps PipelineTemplateDefinitions API
  slug: azure-dev-ops-pipelinetemplatedefinitions-api
artifact_total: 62
collections:
- collection_type: postman
  name: Azure DevOps Operations API
  slug: postman-azure-dev-ops-operations-api
- collection_type: postman
  name: Azure DevOps Operations Pipelines API
  slug: postman-azure-dev-ops-pipelines-api
- collection_type: postman
  name: Azure DevOps Operations PipelineTemplateDefinitions API
  slug: postman-azure-dev-ops-pipelinetemplatedefinitions-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.dev.azure.com/{organization}
- group: docs
  title: ''
  type: MCPDocumentation
  url: https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-devops/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-dev-ops-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-dev-ops-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-dev-ops-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-dev-ops-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/microsoft-azure-devops
- group: start
  title: ''
  type: Portal
  url: https://dev.azure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/devops/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/devops/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dev.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/devops/
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/devops/
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
  url: https://raw.githubusercontent.com/api-evangelist/azure-dev-ops/refs/heads/main/rules/azure-dev-ops-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/azure-dev-ops/refs/heads/main/vocabulary/azure-dev-ops-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/azure-dev-ops/refs/heads/main/json-ld/azure-dev-ops-context.jsonld
created: '2024-01-01'
description: Azure DevOps provides developer services for support teams to plan work, collaborate on code development, and build and deploy applications through a comprehensive set of REST APIs covering builds, releases, Git, pipelines, work items, test management, and artifacts.
examples:
- key_count: 2
  name: Azure Dev Ops Authorization Example
  slug: azure-dev-ops-authorization-example
- key_count: 0
  name: Azure Dev Ops Bootstrap Configuration Example
  slug: azure-dev-ops-bootstrap-configuration-example
- key_count: 4
  name: Azure Dev Ops Code Repository Example
  slug: azure-dev-ops-code-repository-example
- key_count: 4
  name: Azure Dev Ops Input Descriptor Example
  slug: azure-dev-ops-input-descriptor-example
- key_count: 2
  name: Azure Dev Ops Input Value Example
  slug: azure-dev-ops-input-value-example
- key_count: 4
  name: Azure Dev Ops Operation Display Value Example
  slug: azure-dev-ops-operation-display-value-example
- key_count: 2
  name: Azure Dev Ops Organization Reference Example
  slug: azure-dev-ops-organization-reference-example
- key_count: 0
  name: Azure Dev Ops Pipeline Example
  slug: azure-dev-ops-pipeline-example
- key_count: 2
  name: Azure Dev Ops Pipeline List Result Example
  slug: azure-dev-ops-pipeline-list-result-example
- key_count: 1
  name: Azure Dev Ops Pipeline Properties Example
  slug: azure-dev-ops-pipeline-properties-example
- key_count: 3
  name: Azure Dev Ops Pipeline Template Definition Example
  slug: azure-dev-ops-pipeline-template-definition-example
- key_count: 2
  name: Azure Dev Ops Pipeline Template Definition List Result Example
  slug: azure-dev-ops-pipeline-template-definition-list-result-example
- key_count: 2
  name: Azure Dev Ops Pipeline Template Example
  slug: azure-dev-ops-pipeline-template-example
- key_count: 1
  name: Azure Dev Ops Pipeline Update Parameters Example
  slug: azure-dev-ops-pipeline-update-parameters-example
- key_count: 2
  name: Azure Dev Ops Project Reference Example
  slug: azure-dev-ops-project-reference-example
finops:
- name: Azure Dev Ops Finops
  service_category: API
  slug: azure-dev-ops-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-dev-ops.png
json_schemas:
- name: Authorization
  property_count: 2
  slug: azure-dev-ops-authorization
- name: BootstrapConfiguration
  property_count: 2
  slug: azure-dev-ops-bootstrap-configuration
- name: CodeRepository
  property_count: 5
  slug: azure-dev-ops-code-repository
- name: InputDescriptor
  property_count: 4
  slug: azure-dev-ops-input-descriptor
- name: InputValue
  property_count: 2
  slug: azure-dev-ops-input-value
- name: OperationDisplayValue
  property_count: 4
  slug: azure-dev-ops-operation-display-value
- name: OrganizationReference
  property_count: 2
  slug: azure-dev-ops-organization-reference
- name: PipelineListResult
  property_count: 2
  slug: azure-dev-ops-pipeline-list-result
- name: PipelineProperties
  property_count: 4
  slug: azure-dev-ops-pipeline-properties
- name: Pipeline
  property_count: 1
  slug: azure-dev-ops-pipeline
- name: PipelineTemplateDefinitionListResult
  property_count: 2
  slug: azure-dev-ops-pipeline-template-definition-list-result
- name: PipelineTemplateDefinition
  property_count: 3
  slug: azure-dev-ops-pipeline-template-definition
- name: PipelineTemplate
  property_count: 2
  slug: azure-dev-ops-pipeline-template
- name: PipelineUpdateParameters
  property_count: 1
  slug: azure-dev-ops-pipeline-update-parameters
- name: ProjectReference
  property_count: 2
  slug: azure-dev-ops-project-reference
json_structures:
- name: Azure Dev Ops Authorization Structure
  property_count: 2
  slug: azure-dev-ops-authorization-structure
- name: Azure Dev Ops Bootstrap Configuration Structure
  property_count: 2
  slug: azure-dev-ops-bootstrap-configuration-structure
- name: Azure Dev Ops Code Repository Structure
  property_count: 5
  slug: azure-dev-ops-code-repository-structure
- name: Azure Dev Ops Input Descriptor Structure
  property_count: 4
  slug: azure-dev-ops-input-descriptor-structure
- name: Azure Dev Ops Input Value Structure
  property_count: 2
  slug: azure-dev-ops-input-value-structure
- name: Azure Dev Ops Operation Display Value Structure
  property_count: 4
  slug: azure-dev-ops-operation-display-value-structure
- name: Azure Dev Ops Organization Reference Structure
  property_count: 2
  slug: azure-dev-ops-organization-reference-structure
- name: Azure Dev Ops Pipeline List Result Structure
  property_count: 2
  slug: azure-dev-ops-pipeline-list-result-structure
- name: Azure Dev Ops Pipeline Properties Structure
  property_count: 4
  slug: azure-dev-ops-pipeline-properties-structure
- name: Azure Dev Ops Pipeline Structure
  property_count: 1
  slug: azure-dev-ops-pipeline-structure
- name: Azure Dev Ops Pipeline Template Definition List Result Structure
  property_count: 2
  slug: azure-dev-ops-pipeline-template-definition-list-result-structure
- name: Azure Dev Ops Pipeline Template Definition Structure
  property_count: 3
  slug: azure-dev-ops-pipeline-template-definition-structure
- name: Azure Dev Ops Pipeline Template Structure
  property_count: 2
  slug: azure-dev-ops-pipeline-template-structure
- name: Azure Dev Ops Pipeline Update Parameters Structure
  property_count: 1
  slug: azure-dev-ops-pipeline-update-parameters-structure
- name: Azure Dev Ops Project Reference Structure
  property_count: 2
  slug: azure-dev-ops-project-reference-structure
jsonld:
- class_count: 17
  name: Azure Dev Ops Context
  property_count: 23
  slug: azure-dev-ops-context
layout: provider
mcp_servers:
- description: ''
  name: Azure DevOps Remote MCP Server
  slug: azure-devops-remote-mcp-server
modified: '2026-08-06'
name: Azure DevOps
nav: Providers
network: true
overview: 'Azure DevOps publishes 3 APIs on the [APIs.io](https://apis.io/) network: Operations API, Pipelines API, and PipelineTemplateDefinitions API. Tagged areas include Azure, CI/CD, DevOps, Project Management, and Version Control.


  The Azure DevOps catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Azure DevOps'' developer surface includes authentication, developer portal, documentation, getting-started guide, support, engineering blog, and 14 more developer resources.'
plans:
- name: Azure Dev Ops Plans Pricing
  plan_count: 3
  slug: azure-dev-ops-plans-pricing
random_paper: 98
rate_limits:
- limit_count: 5
  name: Azure Dev Ops Rate Limits
  slug: azure-dev-ops-rate-limits
rules:
- name: Azure DevOps API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: azure-dev-ops-jsonschema-spectral-rules
- name: Azure DevOps API Rules
  rule_count: 18
  severity_counts:
    error: 5
    hint: 0
    info: 4
    warn: 9
  slug: azure-dev-ops-spectral-rules
scopes:
- name: Azure Dev Ops Scopes
  scope_count: 1
  slug: azure-dev-ops-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 52.6
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 58.9
    developer_ergonomics: 58.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 23.7
  previous_composite: 52.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-dev-ops/refs/heads/main/screenshots/azure-dev-ops-2026-06-20T172849.png
security:
- kind: authentication
  name: Azure Dev Ops Authentication
  slug: azure-dev-ops-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Azure Dev Ops Domain Security
  slug: azure-dev-ops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azure-dev-ops
tags:
- Azure
- CI/CD
- DevOps
- Project Management
- Version Control
website: https://dev.azure.com/
---
