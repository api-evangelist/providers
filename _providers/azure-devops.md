---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Azure Devops Agentic Access
  operation_count: 12
  slug: azure-devops-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 9
apis:
- description: The Azure DevOps Git Repositories API provides REST endpoints for managing Git repositories, branches, commits, pull requests, and code reviews. APIs enable automation of repository management, pull r
  name: Azure DevOps Git Repositories API
  slug: azure-devops-git-api
- description: The Azure DevOps Artifacts API provides REST endpoints for managing package feeds including NuGet, npm, Maven, Python, and Universal Packages. APIs support feed creation, package publishing, version m
  name: Azure DevOps Artifacts API
  slug: azure-devops-artifacts-api
- description: 'The Azure DevOps Test Plans API provides REST endpoints for managing test plans, test suites, test cases, and test runs. APIs support automated test management, test result reporting, and integration '
  name: Azure DevOps Test Plans API
  slug: azure-devops-test-plans-api
- description: The Azure DevOps Release API provides REST endpoints for managing release pipelines, deployments, and environments. APIs support release definition management, deployment approvals, environment config
  name: Azure DevOps Release API
  slug: azure-devops-release-api
- description: Work item field definitions
  name: Azure DevOps Fields API
  slug: azure-devops-fields-api
- description: Pipeline definition management
  name: Azure DevOps Pipelines API
  slug: azure-devops-pipelines-api
- description: Work item query execution
  name: Azure DevOps Queries API
  slug: azure-devops-queries-api
- description: Pipeline run execution and monitoring
  name: Azure DevOps Runs API
  slug: azure-devops-runs-api
- description: Work item CRUD and management
  name: Azure DevOps WorkItems API
  slug: azure-devops-workitems-api
artifact_total: 78
asyncapis:
- description: Azure DevOps Service Hooks deliver event notifications for work item changes, build completions, pull request events, code pushes, and release deployments. Service hooks are configured in Azure DevOps
  name: Azure DevOps Service Hooks (Webhooks)
  slug: azure-devops-hooks-asyncapi
collections:
- collection_type: postman
  name: Azure DevOps Pipelines Fields API
  slug: postman-azure-devops-fields-api
- collection_type: postman
  name: Azure DevOps Fields Pipelines API
  slug: postman-azure-devops-pipelines-api
- collection_type: postman
  name: Azure DevOps Pipelines Fields Queries API
  slug: postman-azure-devops-queries-api
- collection_type: postman
  name: Azure DevOps Pipelines Fields Runs API
  slug: postman-azure-devops-runs-api
- collection_type: postman
  name: Azure DevOps Pipelines Fields WorkItems API
  slug: postman-azure-devops-workitems-api
- collection_type: open
  name: Azure DevOps Pipelines API
  slug: open-azure-devops-pipelines
- collection_type: open
  name: Azure DevOps Work Item Tracking API
  slug: open-azure-devops-work-items
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-devops/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-devops-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-devops-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-devops-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-devops-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-devops-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/microsoft-azure-devops
- group: docs
  title: ''
  type: Documentation
  url: https://azure.microsoft.com/en-us/products/devops
- group: start
  title: ''
  type: Portal
  url: https://learn.microsoft.com/en-us/rest/api/azure/devops/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.2
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/how-to/call-rest-api?view=azure-devops
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance?view=azure-devops
- group: operate
  title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/rate-limits?view=azure-devops
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/devops/release-notes/features-timeline-released
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/devops/dev-resources/?view=azure-devops
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: build
  title: Node.js SDK
  type: SDKs
  url: https://github.com/microsoft/azure-devops-node-api
- group: build
  title: Python SDK
  type: SDKs
  url: https://github.com/microsoft/azure-devops-python-api
- group: build
  title: Go SDK
  type: SDKs
  url: https://github.com/microsoft/azure-devops-go-api
- group: build
  title: Java SDK
  type: SDKs
  url: https://github.com/microsoft/azure-devops-java-api
- group: build
  title: Azure DevOps CLI Extension
  type: CLI
  url: https://github.com/Azure/azure-devops-cli-extension
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/azure-devops-work-items-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/azure-devops-pipelines-openapi.yml
- group: docs
  title: Create Pipeline Request Schema
  type: JSONSchema
  url: json-schema/azure-devops-pipelines-create-pipeline-request-schema.json
- group: docs
  title: Pipelines Error Schema
  type: JSONSchema
  url: json-schema/azure-devops-pipelines-error-schema.json
- group: docs
  title: Pipeline Run Schema
  type: JSONSchema
  url: json-schema/azure-devops-pipelines-pipeline-run-schema.json
- group: docs
  title: Pipeline Schema
  type: JSONSchema
  url: json-schema/azure-devops-pipelines-pipeline-schema.json
- group: docs
  title: Run Pipeline Request Schema
  type: JSONSchema
  url: json-schema/azure-devops-pipelines-run-pipeline-request-schema.json
- group: docs
  title: Work Items Error Schema
  type: JSONSchema
  url: json-schema/azure-devops-work-items-error-schema.json
- group: docs
  title: JSON Patch Operation Schema
  type: JSONSchema
  url: json-schema/azure-devops-work-items-json-patch-operation-schema.json
- group: docs
  title: WIQL Result Schema
  type: JSONSchema
  url: json-schema/azure-devops-work-items-wiql-result-schema.json
- group: docs
  title: Work Item Field Schema
  type: JSONSchema
  url: json-schema/azure-devops-work-items-work-item-field-schema.json
- group: docs
  title: Work Item Relation Schema
  type: JSONSchema
  url: json-schema/azure-devops-work-items-work-item-relation-schema.json
- group: docs
  title: Work Item Schema
  type: JSONSchema
  url: json-schema/azure-devops-work-items-work-item-schema.json
- group: docs
  title: Work Item Schema (Legacy)
  type: JSONSchema
  url: json-schema/azure-devops-workitem-schema.json
- group: design
  title: Azure DevOps JSON-LD Context
  type: JSONLD
  url: json-ld/azure-devops-context.jsonld
- group: design
  title: Pipelines JSON-LD Context
  type: JSONLD
  url: json-ld/azure-devops-pipelines-context.jsonld
- group: design
  title: Work Items JSON-LD Context
  type: JSONLD
  url: json-ld/azure-devops-work-items-context.jsonld
- group: design
  title: Azure DevOps Vocabulary
  type: Vocabulary
  url: vocabulary/azure-devops-vocabulary.yaml
- group: design
  title: Spectral Rules
  type: Rules
  url: rules/azure-devops-spectral-rules.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/microsoft/azure-devops-mcp
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/devops/feed/
created: '2024-01-01'
description: Learn the basic patterns for using the REST APIs for Azure DevOps Services and Azure DevOps Server.
examples:
- key_count: 3
  name: Azure Devops Pipelines Create Pipeline Request Example
  slug: azure-devops-pipelines-create-pipeline-request-example
- key_count: 2
  name: Azure Devops Pipelines Error Example
  slug: azure-devops-pipelines-error-example
- key_count: 7
  name: Azure Devops Pipelines Pipeline Example
  slug: azure-devops-pipelines-pipeline-example
- key_count: 10
  name: Azure Devops Pipelines Pipeline Run Example
  slug: azure-devops-pipelines-pipeline-run-example
- key_count: 4
  name: Azure Devops Pipelines Run Pipeline Request Example
  slug: azure-devops-pipelines-run-pipeline-request-example
- key_count: 7
  name: Azure Devops Work Items Error Example
  slug: azure-devops-work-items-error-example
- key_count: 4
  name: Azure Devops Work Items Json Patch Operation Example
  slug: azure-devops-work-items-json-patch-operation-example
- key_count: 4
  name: Azure Devops Work Items Wiql Result Example
  slug: azure-devops-work-items-wiql-result-example
- key_count: 5
  name: Azure Devops Work Items Work Item Example
  slug: azure-devops-work-items-work-item-example
- key_count: 6
  name: Azure Devops Work Items Work Item Field Example
  slug: azure-devops-work-items-work-item-field-example
- key_count: 3
  name: Azure Devops Work Items Work Item Relation Example
  slug: azure-devops-work-items-work-item-relation-example
features:
- description: Create, update, query, and manage work items across Azure Boards
  name: Work Item Tracking
- description: Build, test, and deploy with YAML-based and classic pipelines
  name: CI/CD Pipelines
- description: Host and manage Git repositories with branch policies and pull requests
  name: Git Repositories
- description: Package management for NuGet, npm, Maven, Python, and Universal Packages
  name: Artifacts
- description: Comprehensive test management with automated and manual testing
  name: Test Plans
- description: Multi-stage deployment pipelines with approval workflows
  name: Release Management
finops:
- name: Azure Devops Finops
  service_category: Developer Tools
  slug: azure-devops-finops
image: https://raw.githubusercontent.com/api-evangelist/azure-devops/refs/heads/main/image.png
integrations:
- description: Import repositories and trigger pipelines from GitHub events
  name: GitHub
- description: Notifications for pipeline runs and work item updates
  name: Slack
- description: Bidirectional sync of work items with Jira issues
  name: Jira
json_schemas:
- name: CreatePipelineRequest
  property_count: 3
  slug: azure-devops-pipelines-create-pipeline-request
- name: Error
  property_count: 2
  slug: azure-devops-pipelines-error
- name: PipelineRun
  property_count: 10
  slug: azure-devops-pipelines-pipeline-run
- name: Pipeline
  property_count: 7
  slug: azure-devops-pipelines-pipeline
- name: RunPipelineRequest
  property_count: 4
  slug: azure-devops-pipelines-run-pipeline-request
- name: Error
  property_count: 7
  slug: azure-devops-work-items-error
- name: JsonPatchOperation
  property_count: 4
  slug: azure-devops-work-items-json-patch-operation
- name: WiqlResult
  property_count: 4
  slug: azure-devops-work-items-wiql-result
- name: WorkItemField
  property_count: 6
  slug: azure-devops-work-items-work-item-field
- name: WorkItemRelation
  property_count: 3
  slug: azure-devops-work-items-work-item-relation
- name: WorkItem
  property_count: 5
  slug: azure-devops-work-items-work-item
- name: Azure DevOps Work Item
  property_count: 5
  slug: azure-devops-workitem
json_structures:
- name: Azure Devops Pipelines Create Pipeline Request Structure
  property_count: 3
  slug: azure-devops-pipelines-create-pipeline-request-structure
- name: Azure Devops Pipelines Error Structure
  property_count: 2
  slug: azure-devops-pipelines-error-structure
- name: Azure Devops Pipelines Pipeline Run Structure
  property_count: 10
  slug: azure-devops-pipelines-pipeline-run-structure
- name: Azure Devops Pipelines Pipeline Structure
  property_count: 7
  slug: azure-devops-pipelines-pipeline-structure
- name: Azure Devops Pipelines Run Pipeline Request Structure
  property_count: 4
  slug: azure-devops-pipelines-run-pipeline-request-structure
- name: Azure Devops Work Items Error Structure
  property_count: 7
  slug: azure-devops-work-items-error-structure
- name: Azure Devops Work Items Json Patch Operation Structure
  property_count: 4
  slug: azure-devops-work-items-json-patch-operation-structure
- name: Azure Devops Work Items Wiql Result Structure
  property_count: 4
  slug: azure-devops-work-items-wiql-result-structure
- name: Azure Devops Work Items Work Item Field Structure
  property_count: 6
  slug: azure-devops-work-items-work-item-field-structure
- name: Azure Devops Work Items Work Item Relation Structure
  property_count: 3
  slug: azure-devops-work-items-work-item-relation-structure
- name: Azure Devops Work Items Work Item Structure
  property_count: 5
  slug: azure-devops-work-items-work-item-structure
jsonld:
- class_count: 0
  name: Azure Devops Context
  property_count: 4
  slug: azure-devops-context
- class_count: 0
  name: Azure Devops Pipelines Context
  property_count: 0
  slug: azure-devops-pipelines-context
- class_count: 0
  name: Azure Devops Work Items Context
  property_count: 0
  slug: azure-devops-work-items-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Azure DevOps
nav: Providers
network: true
overview: 'Azure DevOps publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Fields API, Pipelines API, Queries API, and 2 more. Tagged areas include Azure, CI/CD, DevOps, Pipelines, and Work Items.


  The Azure DevOps catalog on APIs.io includes 1 event-driven AsyncAPI specification, 3 JSON-LD contexts, and 3 Spectral governance rulesets.


  Azure DevOps'' developer surface includes authentication, documentation, developer portal, API reference, getting-started guide, changelog, CLI, and 35 more developer resources.'
plans:
- name: Azure Devops Plans Pricing
  plan_count: 6
  slug: azure-devops-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 4
  name: Azure Devops Rate Limits
  slug: azure-devops-rate-limits
rules:
- name: Azure DevOps API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: azure-devops-asyncapi-spectral-rules
- name: Azure DevOps API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: azure-devops-jsonschema-spectral-rules
- name: Azure DevOps API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 6
  slug: azure-devops-spectral-rules
scopes:
- name: Azure Devops Scopes
  scope_count: 4
  slug: azure-devops-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 55.2
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 76.0
    developer_ergonomics: 82.6
    discoverability: 64.8
    governance: 52.1
    operational_transparency: 28.9
  previous_composite: 55.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-devops/refs/heads/main/screenshots/azure-devops-2026-06-20T172853.png
security:
- kind: authentication
  name: Azure Devops Authentication
  slug: azure-devops-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Azure Devops Domain Security
  slug: azure-devops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Azure Devops Vulnerability Disclosure
  slug: azure-devops-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: azure-devops
tags:
- Azure
- CI/CD
- DevOps
- Pipelines
- Work Items
use_cases:
- description: Track work items, sprints, and backlogs for Agile development teams
  name: Agile Project Management
- description: Automate build, test, and deployment workflows across environments
  name: CI/CD Automation
- description: Enforce branch policies and manage pull request workflows
  name: Code Review
website: https://learn.microsoft.com/en-us/rest/api/azure/devops/
---
