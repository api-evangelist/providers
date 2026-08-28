---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 24
  human_in_the_loop: 1
  name: Talend Agentic Access
  operation_count: 43
  slug: talend-agentic-access
  summary_line: 43 operations · 24 acting · 1 human-in-the-loop
api_count: 18
apis:
- description: Manages user, group, and role identity information for Talend Cloud accounts. Supports SCIM v2 for automated provisioning from enterprise identity providers.
  name: Talend Cloud Identities Management API
  slug: talend-identities-api
- description: Load account audit logs for monitoring activities on Talend Cloud applications, ensuring data security and regulatory compliance.
  name: Talend Cloud Audit Logs API
  slug: talend-audit-logs-api
- description: Administers connections used by datasets and crawlers to retrieve data at scale.
  name: Talend Cloud Connections API
  slug: talend-connections-api
- description: Retrieve logs about task runs for debugging and monitoring data integration pipeline executions.
  name: Talend Cloud Execution Logs API
  slug: talend-execution-logs-api
- description: The Artifacts API from Talend — 1 operation(s) for artifacts.
  name: Talend Artifacts API
  slug: talend-artifacts-api
- description: The Connections API from Talend — 1 operation(s) for connections.
  name: Talend Connections API
  slug: talend-connections-api
- description: The Environments API from Talend — 1 operation(s) for environments.
  name: Talend Environments API
  slug: talend-environments-api
- description: The Plan Executions API from Talend — 4 operation(s) for plan executions.
  name: Talend Plan Executions API
  slug: talend-plan-executions-api
- description: The Plans API from Talend — 2 operation(s) for plans.
  name: Talend Plans API
  slug: talend-plans-api
- description: The Promotion Executions API from Talend — 1 operation(s) for promotion executions.
  name: Talend Promotion Executions API
  slug: talend-promotion-executions-api
- description: The Promotions API from Talend — 1 operation(s) for promotions.
  name: Talend Promotions API
  slug: talend-promotions-api
- description: The Remote Engine Clusters API from Talend — 1 operation(s) for remote engine clusters.
  name: Talend Remote Engine Clusters API
  slug: talend-remote-engine-clusters-api
- description: The Remote Engines API from Talend — 2 operation(s) for remote engines.
  name: Talend Remote Engines API
  slug: talend-remote-engines-api
- description: The Run Profiles API from Talend — 2 operation(s) for run profiles.
  name: Talend Run Profiles API
  slug: talend-run-profiles-api
- description: The Schedules API from Talend — 1 operation(s) for schedules.
  name: Talend Schedules API
  slug: talend-schedules-api
- description: The Task Executions API from Talend — 3 operation(s) for task executions.
  name: Talend Task Executions API
  slug: talend-task-executions-api
- description: The Tasks API from Talend — 3 operation(s) for tasks.
  name: Talend Tasks API
  slug: talend-tasks-api
- description: The Workspaces API from Talend — 2 operation(s) for workspaces.
  name: Talend Workspaces API
  slug: talend-workspaces-api
artifact_total: 68
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Talend Cloud Orchestration Artifacts API
  slug: open-talend-artifacts-api
- collection_type: open
  name: Talend Cloud Orchestration Artifacts Connections API
  slug: open-talend-connections-api
- collection_type: open
  name: Talend Cloud Orchestration Artifacts Environments API
  slug: open-talend-environments-api
- collection_type: open
  name: Talend Cloud Orchestration API
  slug: open-talend-orchestration
- collection_type: open
  name: Talend Cloud Orchestration Artifacts Plan Executions API
  slug: open-talend-plan-executions-api
- collection_type: open
  name: Talend Cloud Orchestration Artifacts Plans API
  slug: open-talend-plans-api
- collection_type: open
  name: Talend Cloud Processing API
  slug: open-talend-processing
- collection_type: open
  name: Talend Cloud Orchestration Artifacts Promotion Executions API
  slug: open-talend-promotion-executions-api
- collection_type: open
  name: Talend Cloud Orchestration Artifacts Promotions API
  slug: open-talend-promotions-api
- collection_type: open
  name: Talend Cloud Orchestration Artifacts Remote Engine Clusters API
  slug: open-talend-remote-engine-clusters-api
- collection_type: open
  name: Talend Cloud Orchestration Artifacts Remote Engines API
  slug: open-talend-remote-engines-api
- collection_type: open
  name: Talend Cloud Orchestration Artifacts Run Profiles API
  slug: open-talend-run-profiles-api
- collection_type: open
  name: Talend Cloud Orchestration Artifacts Schedules API
  slug: open-talend-schedules-api
- collection_type: open
  name: Talend Cloud Orchestration Artifacts Task Executions API
  slug: open-talend-task-executions-api
- collection_type: open
  name: Talend Cloud Orchestration Artifacts Tasks API
  slug: open-talend-tasks-api
- collection_type: open
  name: Talend Cloud Orchestration Artifacts Workspaces API
  slug: open-talend-workspaces-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/talend-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/talend-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/talend-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/talend
- group: start
  title: ''
  type: Portal
  url: https://talend.qlik.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://talend.qlik.dev/
- group: other
  title: ''
  type: APIs
  url: https://talend.qlik.dev/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://talend.qlik.dev/getting-started/
- group: company
  title: ''
  type: Website
  url: https://www.talend.com/
- group: other
  title: ''
  type: Qlik Data Fabric
  url: https://www.qlik.com/us/products/talend-data-fabric
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Talend
- group: operate
  title: ''
  type: Help
  url: https://help.qlik.com/en-US/cloud-services/Content/Sense_Helpsites/Home-talend-cloud.htm
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/json-schema/talend-task-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/vocabulary/talend-vocabulary.yml
created: '2026-03-16'
description: Talend (now part of Qlik) provides data integration, quality, and API management capabilities through cloud-native APIs for ETL, data pipelines, and application integration. The Qlik Talend Cloud platform exposes REST APIs for orchestrating tasks and plans, executing data integration jobs, managing remote engines, configuring connections, monitoring execution history, and administering identities, workspaces, and environments.
examples:
- key_count: 2
  name: Talend Execute Task Example
  slug: talend-execute-task-example
finops:
- name: Talend Finops
  service_category: Data Integration
  slug: talend-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/talend.png
json_schemas:
- name: Artifact
  property_count: 5
  slug: talend-artifact
- name: Connection
  property_count: 5
  slug: talend-connection
- name: ConnectionCreate
  property_count: 4
  slug: talend-connectioncreate
- name: Environment
  property_count: 5
  slug: talend-environment
- name: EnvironmentCreate
  property_count: 2
  slug: talend-environmentcreate
- name: Task Execution
  property_count: 12
  slug: talend-execution
- name: Plan
  property_count: 7
  slug: talend-plan
- name: PlanCreate
  property_count: 4
  slug: talend-plancreate
- name: PlanExecution
  property_count: 6
  slug: talend-planexecution
- name: PlanExecutionRequest
  property_count: 3
  slug: talend-planexecutionrequest
- name: RemoteEngine
  property_count: 7
  slug: talend-remoteengine
- name: RemoteEngineCreate
  property_count: 3
  slug: talend-remoteenginecreate
- name: RunProfileCreate
  property_count: 4
  slug: talend-runprofilecreate
- name: Schedule
  property_count: 5
  slug: talend-schedule
- name: ScheduleCreate
  property_count: 3
  slug: talend-schedulecreate
- name: Talend Task
  property_count: 12
  slug: talend-task
- name: TaskCreate
  property_count: 4
  slug: talend-taskcreate
- name: TaskExecution
  property_count: 8
  slug: talend-taskexecution
- name: TaskExecutionRequest
  property_count: 3
  slug: talend-taskexecutionrequest
- name: Workspace
  property_count: 6
  slug: talend-workspace
- name: WorkspaceCreate
  property_count: 2
  slug: talend-workspacecreate
json_structures:
- name: Talend Structure
  property_count: 0
  slug: talend-structure
- name: Talend Task Structure
  property_count: 0
  slug: talend-task-structure
jsonld:
- class_count: 10
  name: Talend Context
  property_count: 24
  slug: talend-context
layout: provider
modified: '2026-05-19'
name: Talend
nav: Providers
network: true
overview: 'Talend publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Cloud Connections API, Artifacts API, Connections API, and 12 more. Tagged areas include API Management, Data Integration, Data Quality, ETL, and Orchestration.


  The Talend catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Talend''s developer surface includes authentication, developer portal, documentation, getting-started guide, and 10 more developer resources.'
plans:
- name: Talend Plans Pricing
  plan_count: 1
  slug: talend-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Talend Rate Limits
  slug: talend-rate-limits
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Talend API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 5
  slug: talend-api-rules
- effective_rule_count: 5
  extends: []
  name: Talend API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: talend-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.0
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 69.7
    contract_quality: 62.7
    developer_ergonomics: 42.9
    discoverability: 74.1
    governance: 69.7
    operational_transparency: 10.5
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/screenshots/talend-2026-06-20T194901.png
security:
- kind: authentication
  name: Talend Authentication
  slug: talend-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Talend Domain Security
  slug: talend-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: talend
tags:
- API Management
- Data Integration
- Data Quality
- ETL
- Orchestration
- Pipelines
website: https://www.talend.com/
---
