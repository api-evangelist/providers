---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Microsoft Fabric Agentic Access
  operation_count: 17
  slug: microsoft-fabric-agentic-access
  summary_line: 17 operations · 9 acting
api_count: 3
apis:
- description: 'Microsoft Fabric provides SQL connectivity to lakehouses and data warehouses through TDS endpoints. Developers can query Fabric data using standard SQL tools, JDBC/ODBC drivers, and client libraries, '
  name: Microsoft Fabric SQL Connection
  slug: sql-connection-api
- baseURL: https://api.fabric.microsoft.com/v1/
  baseurl_source: declared
  description: The Capacities API from Microsoft Fabric — 1 operation(s) for capacities.
  name: Microsoft Fabric Capacities API
  slug: microsoft-fabric-capacities-api
- baseURL: https://api.fabric.microsoft.com/v1/
  baseurl_source: declared
  description: The Connections API from Microsoft Fabric — 1 operation(s) for connections.
  name: Microsoft Fabric Connections API
  slug: microsoft-fabric-connections-api
- baseURL: https://api.fabric.microsoft.com/v1/
  baseurl_source: declared
  description: The Items API from Microsoft Fabric — 6 operation(s) for items.
  name: Microsoft Fabric Items API
  slug: microsoft-fabric-items-api
- baseURL: https://api.fabric.microsoft.com/v1/
  baseurl_source: declared
  description: The Workspaces API from Microsoft Fabric — 2 operation(s) for workspaces.
  name: Microsoft Fabric Workspaces API
  slug: microsoft-fabric-workspaces-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Activation API from Microsoft Fabric — 3 operation(s) for activation.
  name: Microsoft Fabric Activation API
  slug: microsoft-fabric-activation-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Activations API from Microsoft Fabric — 1 operation(s) for activations.
  name: Microsoft Fabric Activations API
  slug: microsoft-fabric-activations-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The CapacitySettings API from Microsoft Fabric — 1 operation(s) for capacitysettings.
  name: Microsoft Fabric Capacity Settings API
  slug: microsoft-fabric-capacitysettings-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Catalog API from Microsoft Fabric — 1 operation(s) for catalog.
  name: Microsoft Fabric Catalog API
  slug: microsoft-fabric-catalog-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Compute API from Microsoft Fabric — 2 operation(s) for compute.
  name: Microsoft Fabric Compute API
  slug: microsoft-fabric-compute-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Copilot API from Microsoft Fabric — 1 operation(s) for copilot.
  name: Microsoft Fabric Copilot API
  slug: microsoft-fabric-copilot-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The CustomPools API from Microsoft Fabric — 4 operation(s) for custompools.
  name: Microsoft Fabric Custom Pools API
  slug: microsoft-fabric-custompools-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The DataCollection API from Microsoft Fabric — 2 operation(s) for datacollection.
  name: Microsoft Fabric Data Collection API
  slug: microsoft-fabric-datacollection-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The DeploymentPipelines API from Microsoft Fabric — 12 operation(s) for deploymentpipelines.
  name: Microsoft Fabric Deployment Pipelines API
  slug: microsoft-fabric-deploymentpipelines-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Discovery API from Microsoft Fabric — 5 operation(s) for discovery.
  name: Microsoft Fabric Discovery API
  slug: microsoft-fabric-discovery-api
- baseURL: https://api.fabric.microsoft.com/v1/admin
  baseurl_source: declared
  description: The Domains API from Microsoft Fabric — 16 operation(s) for domains.
  name: Microsoft Fabric Domains API
  slug: microsoft-fabric-domains-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Endpoint API from Microsoft Fabric — 8 operation(s) for endpoint.
  name: Microsoft Fabric Endpoint API
  slug: microsoft-fabric-endpoint-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Environment API from Microsoft Fabric — 3 operation(s) for environment.
  name: Microsoft Fabric Environment API
  slug: microsoft-fabric-environment-api
- baseURL: https://api.fabric.microsoft.com/v1/admin
  baseurl_source: declared
  description: The ExternalDataSharesProvider API from Microsoft Fabric — 4 operation(s) for externaldatasharesprovider.
  name: Microsoft Fabric External Data Shares Provider API
  slug: microsoft-fabric-externaldatasharesprovider-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The ExternalDataSharesRecipient API from Microsoft Fabric — 2 operation(s) for externaldatasharesrecipient.
  name: Microsoft Fabric External Data Shares Recipient API
  slug: microsoft-fabric-externaldatasharesrecipient-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Files API from Microsoft Fabric — 2 operation(s) for files.
  name: Microsoft Fabric Files API
  slug: microsoft-fabric-files-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Folders API from Microsoft Fabric — 3 operation(s) for folders.
  name: Microsoft Fabric Folders API
  slug: microsoft-fabric-folders-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Gateways API from Microsoft Fabric — 10 operation(s) for gateways.
  name: Microsoft Fabric Gateways API
  slug: microsoft-fabric-gateways-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Git API from Microsoft Fabric — 11 operation(s) for git.
  name: Microsoft Fabric Git API
  slug: microsoft-fabric-git-api
- baseURL: https://api.fabric.microsoft.com/v1/admin
  baseurl_source: declared
  description: The Labels API from Microsoft Fabric — 2 operation(s) for labels.
  name: Microsoft Fabric Labels API
  slug: microsoft-fabric-labels-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The LivySessions API from Microsoft Fabric — 11 operation(s) for livysessions.
  name: Microsoft Fabric Livy Sessions API
  slug: microsoft-fabric-livysessions-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The LongRunningOperations API from Microsoft Fabric — 2 operation(s) for longrunningoperations.
  name: Microsoft Fabric Long Running Operations API
  slug: microsoft-fabric-longrunningoperations-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The ManagedPrivateEndpoints API from Microsoft Fabric — 2 operation(s) for managedprivateendpoints.
  name: Microsoft Fabric Managed Private Endpoints API
  slug: microsoft-fabric-managedprivateendpoints-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The MaterializedLakeViews API from Microsoft Fabric — 2 operation(s) for materializedlakeviews.
  name: Microsoft Fabric Materialized Lake Views API
  slug: microsoft-fabric-materializedlakeviews-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Mirroring API from Microsoft Fabric — 6 operation(s) for mirroring.
  name: Microsoft Fabric Mirroring API
  slug: microsoft-fabric-mirroring-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Monitoring API from Microsoft Fabric — 2 operation(s) for monitoring.
  name: Microsoft Fabric Monitoring API
  slug: microsoft-fabric-monitoring-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The OneLakeDataAccessSecurity API from Microsoft Fabric — 2 operation(s) for onelakedataaccesssecurity.
  name: Microsoft Fabric One Lake Data Access Security API
  slug: microsoft-fabric-onelakedataaccesssecurity-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The OneLakeLifecyclePolicy API from Microsoft Fabric — 2 operation(s) for onelakelifecyclepolicy.
  name: Microsoft Fabric One Lake Lifecycle Policy API
  slug: microsoft-fabric-onelakelifecyclepolicy-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The OneLakeSettings API from Microsoft Fabric — 5 operation(s) for onelakesettings.
  name: Microsoft Fabric One Lake Settings API
  slug: microsoft-fabric-onelakesettings-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The OneLakeShortcuts API from Microsoft Fabric — 4 operation(s) for onelakeshortcuts.
  name: Microsoft Fabric One Lake Shortcuts API
  slug: microsoft-fabric-onelakeshortcuts-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The PolicyRules API from Microsoft Fabric — 3 operation(s) for policyrules.
  name: Microsoft Fabric Policy Rules API
  slug: microsoft-fabric-policyrules-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The PoolActivations API from Microsoft Fabric — 2 operation(s) for poolactivations.
  name: Microsoft Fabric Pool Activations API
  slug: microsoft-fabric-poolactivations-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The PoolManagement API from Microsoft Fabric — 2 operation(s) for poolmanagement.
  name: Microsoft Fabric Pool Management API
  slug: microsoft-fabric-poolmanagement-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Published API from Microsoft Fabric — 13 operation(s) for published.
  name: Microsoft Fabric Published API
  slug: microsoft-fabric-published-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The RecoverableItems API from Microsoft Fabric — 3 operation(s) for recoverableitems.
  name: Microsoft Fabric Recoverable Items API
  slug: microsoft-fabric-recoverableitems-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Refresh API from Microsoft Fabric — 2 operation(s) for refresh.
  name: Microsoft Fabric Refresh API
  slug: microsoft-fabric-refresh-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Requirements API from Microsoft Fabric — 2 operation(s) for requirements.
  name: Microsoft Fabric Requirements API
  slug: microsoft-fabric-requirements-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The RestorePoints API from Microsoft Fabric — 3 operation(s) for restorepoints.
  name: Microsoft Fabric Restore Points API
  slug: microsoft-fabric-restorepoints-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Settings API from Microsoft Fabric — 2 operation(s) for settings.
  name: Microsoft Fabric Settings API
  slug: microsoft-fabric-settings-api
- baseURL: https://api.fabric.microsoft.com/v1/admin
  baseurl_source: declared
  description: The SharingLinks API from Microsoft Fabric — 2 operation(s) for sharinglinks.
  name: Microsoft Fabric Sharing Links API
  slug: microsoft-fabric-sharinglinks-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The SQLAuditSettings API from Microsoft Fabric — 5 operation(s) for sqlauditsettings.
  name: Microsoft Fabric SQL Audit Settings API
  slug: microsoft-fabric-sqlauditsettings-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The SQLPools API from Microsoft Fabric — 1 operation(s) for sqlpools.
  name: Microsoft Fabric SQL Pools API
  slug: microsoft-fabric-sqlpools-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Staging API from Microsoft Fabric — 21 operation(s) for staging.
  name: Microsoft Fabric Staging API
  slug: microsoft-fabric-staging-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The SurgeProtection API from Microsoft Fabric — 7 operation(s) for surgeprotection.
  name: Microsoft Fabric Surge Protection API
  slug: microsoft-fabric-surgeprotection-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Tables API from Microsoft Fabric — 3 operation(s) for tables.
  name: Microsoft Fabric Tables API
  slug: microsoft-fabric-tables-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The TableShortcuts API from Microsoft Fabric — 2 operation(s) for tableshortcuts.
  name: Microsoft Fabric Table Shortcuts API
  slug: microsoft-fabric-tableshortcuts-api
- baseURL: https://api.fabric.microsoft.com/v1/admin
  baseurl_source: declared
  description: The Tags API from Microsoft Fabric — 5 operation(s) for tags.
  name: Microsoft Fabric Tags API
  slug: microsoft-fabric-tags-api
- baseURL: https://api.fabric.microsoft.com/v1/admin
  baseurl_source: declared
  description: The Tenants API from Microsoft Fabric — 8 operation(s) for tenants.
  name: Microsoft Fabric Tenants API
  slug: microsoft-fabric-tenants-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Topology API from Microsoft Fabric — 11 operation(s) for topology.
  name: Microsoft Fabric Topology API
  slug: microsoft-fabric-topology-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Upgrade API from Microsoft Fabric — 2 operation(s) for upgrade.
  name: Microsoft Fabric Upgrade API
  slug: microsoft-fabric-upgrade-api
- baseURL: https://api.fabric.microsoft.com/v1/admin
  baseurl_source: declared
  description: The Users API from Microsoft Fabric — 1 operation(s) for users.
  name: Microsoft Fabric Users API
  slug: microsoft-fabric-users-api
- baseURL: https://api.fabric.microsoft.com/v1/admin
  baseurl_source: declared
  description: The Workloads API from Microsoft Fabric — 3 operation(s) for workloads.
  name: Microsoft Fabric Workloads API
  slug: microsoft-fabric-workloads-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The WorkspaceSettings API from Microsoft Fabric — 2 operation(s) for workspacesettings.
  name: Microsoft Fabric Workspace Settings API
  slug: microsoft-fabric-workspacesettings-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Background Jobs API from Microsoft Fabric — 19 operation(s) for background jobs.
  name: Microsoft Fabric Background Jobs API
  slug: microsoft-fabric-background-jobs-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Job Scheduler API from Microsoft Fabric — 6 operation(s) for job scheduler.
  name: Microsoft Fabric Job Scheduler API
  slug: microsoft-fabric-job-scheduler-api
- baseURL: https://api.fabric.microsoft.com/v1/admin
  baseurl_source: declared
  description: The Policy Sets API from Microsoft Fabric — 3 operation(s) for policy sets.
  name: Microsoft Fabric Policy Sets API
  slug: microsoft-fabric-policy-sets-api
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: The Query Execution API from Microsoft Fabric — 1 operation(s) for query execution.
  name: Microsoft Fabric Query Execution API
  slug: microsoft-fabric-query-execution-api
artifact_total: 83
collections:
- collection_type: open
  name: Microsoft Fabric REST API (Core) Capacities API
  slug: open-microsoft-fabric-capacities-api
- collection_type: open
  name: Microsoft Fabric REST API (Core) Capacities Connections API
  slug: open-microsoft-fabric-connections-api
- collection_type: open
  name: Microsoft Fabric REST API (Core) Capacities Items API
  slug: open-microsoft-fabric-items-api
- collection_type: open
  name: Microsoft Fabric REST API (Core) Capacities Workspaces API
  slug: open-microsoft-fabric-workspaces-api
- collection_type: open
  name: Microsoft Fabric REST API (Core)
  slug: open-microsoft-fabric
common:
- group: operate
  href: https://artifacts.apis.io/microsoft-fabric/changelog/microsoft-fabric-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-fabric-changelog.yml
- group: start
  href: https://artifacts.apis.io/microsoft-fabric/sandbox/microsoft-fabric-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/microsoft-fabric-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://servicetrust.microsoft.com/
- group: auth
  href: https://artifacts.apis.io/microsoft-fabric/security/microsoft-fabric-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-fabric-trust-center.yml
- group: design
  href: https://artifacts.apis.io/microsoft-fabric/rules/microsoft-fabric-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-fabric-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-fabric/json-ld/microsoft-fabric-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-fabric-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-fabric/vocabulary/microsoft-fabric-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-fabric-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-fabric/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-fabric/data-model/microsoft-fabric-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-fabric-data-model.yml
- group: build
  href: https://artifacts.apis.io/microsoft-fabric/cli/microsoft-fabric-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-fabric-cli.yml
- group: design
  href: https://artifacts.apis.io/microsoft-fabric/conventions/microsoft-fabric-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-fabric-conventions.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-fabric/scopes/microsoft-fabric-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-fabric-scopes.yml
- group: design
  href: https://artifacts.apis.io/microsoft-fabric/lifecycle/microsoft-fabric-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-fabric-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-fabric/errors/microsoft-fabric-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-fabric-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-fabric/conformance/microsoft-fabric-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-fabric-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-fabric/llms/microsoft-fabric-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-fabric-llms.txt
- group: build
  href: https://artifacts.apis.io/microsoft-fabric/mcp/microsoft-fabric-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-fabric-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-fabric/mcp/microsoft-fabric-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-fabric-mcp.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-fabric/well-known/microsoft-fabric-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-fabric-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-fabric/well-known/microsoft-fabric-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-fabric-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-fabric/hosts/microsoft-fabric-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-fabric-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-fabric/integrations/microsoft-fabric-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-fabric-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-fabric/vendors/microsoft-fabric-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-fabric-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-fabric/packages/microsoft-fabric-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-fabric-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-fabric/packages/microsoft-fabric-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-fabric-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: commercial
  href: https://artifacts.apis.io/microsoft-fabric/plans/microsoft-fabric-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-fabric-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-fabric/rate-limits/microsoft-fabric-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-fabric-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-fabric/finops/microsoft-fabric-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-fabric-finops.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-fabric/agentic-access/microsoft-fabric-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-fabric-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-fabric/security/microsoft-fabric-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-fabric-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-fabric/security/microsoft-fabric-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-fabric-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-fabric/authentication/microsoft-fabric-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-fabric-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoftfabric
- group: start
  title: ''
  type: Portal
  url: https://app.fabric.microsoft.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-fabric
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/fabric/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/fabric/get-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/microsoft-fabric/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/fabric/security/permission-model
- group: company
  title: ''
  type: Blog
  url: https://blog.fabric.microsoft.com/
- group: operate
  title: ''
  type: Community
  url: https://community.fabric.microsoft.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fabric.microsoft.com/
created: '2024-01-01'
description: Microsoft Fabric is a unified analytics platform that brings together data engineering, data science, real-time analytics, and business intelligence. It provides REST APIs for managing workspaces, lakehouses, warehouses, data pipelines, notebooks, and other Fabric items.
finops:
- has_sources: true
  method: derived
  name: Microsoft Fabric Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-fabric-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-fabric.png
json_schemas:
- name: GenericList
  property_count: 1
  slug: microsoft-fabric-generic-list
- name: GenericObject
  property_count: 0
  slug: microsoft-fabric-generic-object
jsonld:
- class_count: 1
  name: Microsoft Fabric Context
  property_count: 1
  slug: microsoft-fabric-context
layout: provider
mcp_servers:
- description: 'Microsoft publishes a first-party Fabric MCP server (open source, in github.com/microsoft/mcp) that runs locally over stdio, distributed via npm (@microsoft/fabric-mcp), NuGet (Microsoft.Fabric.Mcp), '
  name: Microsoft Fabric MCP Server
  slug: microsoft-fabric-mcp-server
modified: '2026-05-19'
name: Microsoft Fabric
nav: Providers
network: true
overview: 'Microsoft Fabric publishes 62 API contracts indexed on the [APIs.io](https://apis.io/) network, including Capacities API, Connections API, Items API, and 59 more. Tagged areas include Data Analytics, Data Engineering, Data Platform, Lakehouse, and Microsoft.


  The Microsoft Fabric catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Fabric''s developer surface includes changelog, sandbox, CLI, authentication, developer portal, documentation, getting-started guide, and 42 more developer resources.'
plans:
- name: Microsoft Fabric Plans Pricing
  plan_count: 0
  slug: microsoft-fabric-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Microsoft Fabric Rate Limits
  slug: microsoft-fabric-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Microsoft Fabric API Rules
  rule_count: 51
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 13
  slug: microsoft-fabric-rules
scopes:
- name: Microsoft Fabric Scopes
  scope_count: 83
  slug: microsoft-fabric-scopes
  summary_line: 83 scopes
score:
  band: strong
  composite: 61.4
  coverage:
    artifact_dirs: 34
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 19.4
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 56.6
    developer_ergonomics: 73.2
    discoverability: 78.3
    operational_transparency: 68.4
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 62
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-fabric/microsoft-fabric-2026-06-20T185503.png
security:
- kind: authentication
  name: Microsoft Fabric Authentication
  slug: microsoft-fabric-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Fabric Domain Security
  slug: microsoft-fabric-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Fabric Vulnerability Disclosure
  slug: microsoft-fabric-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Fabric Trust Center
  slug: microsoft-fabric-trust-center
  summary_line: HIPAA BAA, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27001, ISO/IEC 27701
skill_count: 2
skills:
- name: create-and-run-fabric-item
  slug: microsoft-fabric-create-and-run-item
- name: recover-deleted-fabric-item
  slug: microsoft-fabric-recover-deleted-item
slug: microsoft-fabric
tags:
- Data Analytics
- Data Engineering
- Data Platform
- Lakehouse
- Microsoft
website: https://www.microsoft.com/en-us/microsoft-fabric
---
