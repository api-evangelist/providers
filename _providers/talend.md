---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://www.talend.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.qlik.com/us/qlik-talend — a different registrable domain (talend.com -> qlik.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.9
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 92
  human_in_the_loop: 8
  name: Talend Agentic Access
  operation_count: 168
  slug: talend-agentic-access
  summary_line: 168 operations · 92 acting · 8 human-in-the-loop
api_count: 17
apis:
- description: Manages user, group, and role identity information for Talend Cloud accounts. Supports SCIM v2 for automated provisioning from enterprise identity providers.
  name: Talend Cloud Identities Management API
  slug: talend-identities-api
- description: Load account audit logs for monitoring activities on Talend Cloud applications, ensuring data security and regulatory compliance.
  name: Talend Cloud Audit Logs API
  slug: talend-audit-logs-api
- description: Administers connections used by datasets and crawlers to retrieve data at scale.
  name: Talend Cloud Connections API
  slug: talend-cloud-connections-api
- description: Retrieve logs about task runs for debugging and monitoring data integration pipeline executions.
  name: Talend Cloud Execution Logs API
  slug: talend-execution-logs-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Artifacts API from Talend — 1 operation(s) for artifacts.
  name: Talend Artifacts API
  slug: talend-artifacts-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Connections API from Talend — 1 operation(s) for connections.
  name: Talend Connections API
  slug: talend-connections-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Environments API from Talend — 1 operation(s) for environments.
  name: Talend Environments API
  slug: talend-environments-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Plan Executions API from Talend — 4 operation(s) for plan executions.
  name: Talend Plan Executions API
  slug: talend-plan-executions-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Plans API from Talend — 2 operation(s) for plans.
  name: Talend Plans API
  slug: talend-plans-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Promotion Executions API from Talend — 1 operation(s) for promotion executions.
  name: Talend Promotion Executions API
  slug: talend-promotion-executions-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Promotions API from Talend — 1 operation(s) for promotions.
  name: Talend Promotions API
  slug: talend-promotions-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Remote Engine Clusters API from Talend — 1 operation(s) for remote engine clusters.
  name: Talend Remote Engine Clusters API
  slug: talend-remote-engine-clusters-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Remote Engines API from Talend — 2 operation(s) for remote engines.
  name: Talend Remote Engines API
  slug: talend-remote-engines-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Run Profiles API from Talend — 2 operation(s) for run profiles.
  name: Talend Run Profiles API
  slug: talend-run-profiles-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Schedules API from Talend — 1 operation(s) for schedules.
  name: Talend Schedules API
  slug: talend-schedules-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Task Executions API from Talend — 3 operation(s) for task executions.
  name: Talend Task Executions API
  slug: talend-task-executions-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Tasks API from Talend — 3 operation(s) for tasks.
  name: Talend Tasks API
  slug: talend-tasks-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Workspaces API from Talend — 2 operation(s) for workspaces.
  name: Talend Workspaces API
  slug: talend-workspaces-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Account API from Talend — 4 operation(s) for account.
  name: Talend Account API
  slug: talend-account-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: 'The account :: subscription API from Talend — 1 operation(s) for account :: subscription.'
  name: 'Talend account :: subscription API'
  slug: talend-account-subscription-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The attributes API from Talend — 2 operation(s) for attributes.
  name: Talend Attributes API
  slug: talend-attributes-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The ConnectionScan API from Talend — 1 operation(s) for connectionscan.
  name: Talend Connection Scan API
  slug: talend-connectionscan-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Crawler API from Talend — 6 operation(s) for crawler.
  name: Talend Crawler API
  slug: talend-crawler-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The dataset API from Talend — 5 operation(s) for dataset.
  name: Talend Dataset API
  slug: talend-dataset-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Datasets API from Talend — 2 operation(s) for datasets.
  name: Talend Datasets API
  slug: talend-datasets-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The dynamic-engine-controller API from Talend — 5 operation(s) for dynamic-engine-controller.
  name: Talend Dynamic Engine Controller API
  slug: talend-dynamic-engine-controller-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The dynamic-engine-version-controller API from Talend — 1 operation(s) for dynamic-engine-version-controller.
  name: Talend Dynamic Engine Version Controller API
  slug: talend-dynamic-engine-version-controller-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Eligibles API from Talend — 1 operation(s) for eligibles.
  name: Talend Eligibles API
  slug: talend-eligibles-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The environment-controller API from Talend — 2 operation(s) for environment-controller.
  name: Talend Environment Controller API
  slug: talend-environment-controller-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The IP Allowlist Management API from Talend — 3 operation(s) for ip allowlist management.
  name: Talend IP Allowlist Management API
  slug: talend-ip-allowlist-management-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Levels API from Talend — 1 operation(s) for levels.
  name: Talend Levels API
  slug: talend-levels-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Monitoring API from Talend — 4 operation(s) for monitoring.
  name: Talend Monitoring API
  slug: talend-monitoring-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Orchestration API from Talend — 4 operation(s) for orchestration.
  name: Talend Orchestration API
  slug: talend-orchestration-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The SCIM 2.0 Group Management API from Talend — 3 operation(s) for scim 2.0 group management.
  name: Talend SCIM 2.0 Group Management API
  slug: talend-scim-2-0-group-management-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The SCIM 2.0 Resource Type API from Talend — 2 operation(s) for scim 2.0 resource type.
  name: Talend SCIM 2.0 Resource Type API
  slug: talend-scim-2-0-resource-type-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The SCIM 2.0 Role Management API from Talend — 3 operation(s) for scim 2.0 role management.
  name: Talend SCIM 2.0 Role Management API
  slug: talend-scim-2-0-role-management-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The SCIM 2.0 Schema API from Talend — 2 operation(s) for scim 2.0 schema.
  name: Talend SCIM 2.0 Schema API
  slug: talend-scim-2-0-schema-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The SCIM 2.0 Service Provider Config API from Talend — 1 operation(s) for scim 2.0 service provider config.
  name: Talend SCIM 2.0 Service Provider Config API
  slug: talend-scim-2-0-service-provider-config-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The SCIM 2.0 User Management API from Talend — 3 operation(s) for scim 2.0 user management.
  name: Talend SCIM 2.0 User Management API
  slug: talend-scim-2-0-user-management-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Security API from Talend — 3 operation(s) for security.
  name: Talend Security API
  slug: talend-security-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: 'The service accounts :: workspaces :: permissions API from Talend — 3 operation(s) for service accounts :: workspaces :: permissions.'
  name: 'Talend service accounts :: workspaces :: permissions API'
  slug: talend-service-accounts-workspaces-permissions-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The Sharings API from Talend — 3 operation(s) for sharings.
  name: Talend Sharings API
  slug: talend-sharings-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: The SharingSet API from Talend — 2 operation(s) for sharingset.
  name: Talend Sharing Set API
  slug: talend-sharingset-api
- baseURL: https://api.{region}.cloud.talend.com
  baseurl_source: declared
  description: 'The workspaces :: permissions API from Talend — 3 operation(s) for workspaces :: permissions.'
  name: 'Talend workspaces :: permissions API'
  slug: talend-workspaces-permissions-api
artifact_total: 108
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
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/finops/talend-finops.yml
  title: ''
  type: FinOps
  url: finops/talend-finops.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/rate-limits/talend-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/talend-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/plans/talend-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/talend-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/rules/talend-rules.yml
  title: ''
  type: Spectral
  url: rules/talend-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/rules/talend-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/talend-jsonschema-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/rules/talend-api-rules.yml
  title: ''
  type: Spectral
  url: rules/talend-api-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/json-ld/talend-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/talend-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/vocabulary/talend-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/talend-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/data-model/talend-data-model.yml
  title: ''
  type: DataModel
  url: data-model/talend-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/errors/talend-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/talend-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/conformance/talend-conformance.yml
  title: ''
  type: Conformance
  url: conformance/talend-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/llms/talend-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/talend-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/a2a/talend-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/talend-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/well-known/talend-apis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/talend-apis-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/well-known/talend-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/talend-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/hosts/talend-hosts.yml
  title: ''
  type: Hosts
  url: hosts/talend-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/vendors/talend-vendors.yml
  title: ''
  type: Vendors
  url: vendors/talend-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/packages/talend-packages.yml
  title: ''
  type: SDKs
  url: packages/talend-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/packages/talend-packages.yml
  title: ''
  type: Packages
  url: packages/talend-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.qlik.com/us/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qlik.com/us/legal/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://help.qlik.com/
- group: auth
  title: ''
  type: Security
  url: https://www.talend.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.talend.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.talend.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.talend.com/about-us/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.qlik.com/us/company/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.qlik.com/us/blog
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/qlik/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/agentic-access/talend-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/talend-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/security/talend-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/talend-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/authentication/talend-authentication.yml
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
- name: ConnectionCreate
  property_count: 4
  slug: talend-connection-create
- name: Connection
  property_count: 5
  slug: talend-connection
- name: ConnectionCreate
  property_count: 4
  slug: talend-connectioncreate
- name: EnvironmentCreate
  property_count: 2
  slug: talend-environment-create
- name: Environment
  property_count: 5
  slug: talend-environment
- name: EnvironmentCreate
  property_count: 2
  slug: talend-environmentcreate
- name: Task Execution
  property_count: 12
  slug: talend-execution
- name: PlanCreate
  property_count: 4
  slug: talend-plan-create
- name: PlanExecutionRequest
  property_count: 3
  slug: talend-plan-execution-request
- name: PlanExecution
  property_count: 6
  slug: talend-plan-execution
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
- name: RemoteEngineCreate
  property_count: 3
  slug: talend-remote-engine-create
- name: RemoteEngine
  property_count: 7
  slug: talend-remote-engine
- name: RemoteEngine
  property_count: 7
  slug: talend-remoteengine
- name: RemoteEngineCreate
  property_count: 3
  slug: talend-remoteenginecreate
- name: RunProfileCreate
  property_count: 4
  slug: talend-run-profile-create
- name: RunProfileCreate
  property_count: 4
  slug: talend-runprofilecreate
- name: ScheduleCreate
  property_count: 3
  slug: talend-schedule-create
- name: Schedule
  property_count: 5
  slug: talend-schedule
- name: ScheduleCreate
  property_count: 3
  slug: talend-schedulecreate
- name: TaskCreate
  property_count: 4
  slug: talend-task-create
- name: TaskExecutionRequest
  property_count: 3
  slug: talend-task-execution-request
- name: TaskExecution
  property_count: 8
  slug: talend-task-execution
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
- name: WorkspaceCreate
  property_count: 2
  slug: talend-workspace-create
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
overview: 'Talend publishes 44 APIs on the [APIs.io](https://apis.io/) network, including Artifacts API, Connections API, Environments API, and 41 more. Tagged areas include API Management, Data Integration, Data Quality, ETL, and Orchestration.


  The Talend catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Talend''s developer surface includes support, pricing, engineering blog, authentication, developer portal, documentation, getting-started guide, and 37 more developer resources.'
plans:
- name: Talend Plans Pricing
  plan_count: 1
  slug: talend-plans-pricing
random_paper: 16
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
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Talend API Rules
  rule_count: 14
  severity_counts:
    error: 6
    hint: 0
    info: 4
    warn: 4
  slug: talend-rules
score:
  band: strong
  composite: 63.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 84.5
    catalog_earned_first_party: 0.0
    catalog_gap: 30.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 20.2
  facets:
    access_clarity: 52.6
    contract_governance: 57.4
    contract_quality: 65.8
    developer_ergonomics: 58.9
    discoverability: 82.1
    operational_transparency: 21.1
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 40
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 50.0
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
- Data Catalog
website: https://www.talend.com/
---
