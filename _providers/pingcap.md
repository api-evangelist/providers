---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
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
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 93
  human_in_the_loop: 5
  name: Pingcap Agentic Access
  operation_count: 192
  slug: pingcap-agentic-access
  summary_line: 192 operations · 93 acting · 5 human-in-the-loop
api_count: 22
apis:
- description: Official Model Context Protocol server maintained by PingCAP that exposes a TiDB or TiDB Cloud database to MCP-capable agents and IDEs. Ships in the pytidb package, runs over stdio by default or SSE w
  name: TiDB MCP Server
  slug: tidb-mcp-server
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The API Key API from PingCAP — 2 operation(s) for api key.
  name: PingCAP API Key API
  slug: pingcap-api-key-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The Audit Log API from PingCAP — 1 operation(s) for audit log.
  name: PingCAP Audit Log API
  slug: pingcap-audit-log-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Create, get, modify, and delete backups for TiDB clusters. For TiDB Cloud Starter instances, you cannot create or manage backups via API. You can use [Dumpling](https://docs.pingcap.com/tidb/stable/du
  name: PingCAP Backup API
  slug: pingcap-backup-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The Billing API from PingCAP — 4 operation(s) for billing.
  name: PingCAP Billing API
  slug: pingcap-billing-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The Branch API from PingCAP — 3 operation(s) for branch.
  name: PingCAP Branch API
  slug: pingcap-branch-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: List changefeed RCU options, list changefeeds, create a changefeed, get a changefeed, delete a changefeed, update a changefeed downstream config, pause a changefeed, resume a changefeed, and scale a c
  name: PingCAP Changefeed API
  slug: pingcap-changefeed-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The Chat2Query API from PingCAP — 1 operation(s) for chat2query.
  name: PingCAP Chat2 Query API
  slug: pingcap-chat2query-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Create, get, update, delete, pause, resume, reset the root password, and list node quotas of a cluster.
  name: PingCAP Cluster API
  slug: pingcap-cluster-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The Collections API from PingCAP — 6 operation(s) for collections.
  name: PingCAP Collections API
  slug: pingcap-collections-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Create, get, update, delete, and list Data API keys of a Data App. The Data API key in Data Service is different from the key used in the [TiDB Cloud API](https://docs.pingcap.com/tidbcloud/api/v1beta
  name: PingCAP Data API Key API
  slug: pingcap-data-api-key-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Create, get, update, delete, and list Data Apps.
  name: PingCAP Data App API
  slug: pingcap-data-app-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Create, get, delete, and list data sources of a Data App.
  name: PingCAP Data Source API
  slug: pingcap-data-source-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Create, get, and list deployments of a Data App.
  name: PingCAP Deployment API
  slug: pingcap-deployment-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The doc API from PingCAP — 2 operation(s) for doc.
  name: PingCAP Doc API
  slug: pingcap-doc-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Create, get, delete, list, and test endpoints of a Data App.
  name: PingCAP Endpoint API
  slug: pingcap-endpoint-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The Export API from PingCAP — 3 operation(s) for export.
  name: PingCAP Export API
  slug: pingcap-export-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: List import tasks, create an import task, get an import task, and cancel an import task.
  name: PingCAP Import API
  slug: pingcap-import-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: List integrations, create an integration, and delete an integration.
  name: PingCAP Integration API
  slug: pingcap-integration-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The Issue Creators API from PingCAP — 4 operation(s) for issue creators.
  name: PingCAP Issue Creators API
  slug: pingcap-issue-creators-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The Member API from PingCAP — 4 operation(s) for member.
  name: PingCAP Member API
  slug: pingcap-member-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Get the OpenAPI specification of a Data App.
  name: PingCAP OpenAPI Specification API
  slug: pingcap-openapi-specification-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Get private link service for a TiDB node group, create a private endpoint connection, list private endpoint connections, get a private endpoint connection, and delete a private endpoint connection.
  name: PingCAP Private Endpoint Connection API
  slug: pingcap-private-endpoint-connection-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: List projects.
  name: PingCAP Project API
  slug: pingcap-project-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The PublicShadowPoolService API from PingCAP — 1 operation(s) for publicshadowpoolservice.
  name: PingCAP Public Shadow Pool Service API
  slug: pingcap-publicshadowpoolservice-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The Pull Request Creators API from PingCAP — 4 operation(s) for pull request creators.
  name: PingCAP Pull Request Creators API
  slug: pingcap-pull-request-creators-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: List regions, get a region, and list cloud providers and node specs of a region.
  name: PingCAP Region API
  slug: pingcap-region-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Get and create restore tasks for TiDB clusters. You can only restore data to a new cluster. For more information on restoration on TiDB Cloud, refer to [Restore](https://docs.pingcap.com/tidbcloud/bac
  name: PingCAP Restore API
  slug: pingcap-restore-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: source
  name: PingCAP Source API
  slug: pingcap-source-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The Stargazers API from PingCAP — 3 operation(s) for stargazers.
  name: PingCAP Stargazers API
  slug: pingcap-stargazers-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: task
  name: PingCAP Task API
  slug: pingcap-task-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The Trends API from PingCAP — 1 operation(s) for trends.
  name: PingCAP Trends API
  slug: pingcap-trends-api
- baseURL: https://docs.pingcap.com/ai/tidb-mcp-server/
  baseurl_source: declared
  description: The Account API from PingCAP — 3 operation(s) for account.
  name: PingCAP Account API
  slug: pingcap-account-api
- baseURL: https://docs.pingcap.com/ai/tidb-mcp-server/
  baseurl_source: declared
  description: Operations for translating natural language questions into SQL and executing them against TiDB Cloud clusters.
  name: PingCAP Chat2 Data API
  slug: pingcap-chat2data-api
- baseURL: https://docs.pingcap.com/ai/tidb-mcp-server/
  baseurl_source: declared
  description: Operations for generating and managing AI summaries of database schemas used as context for SQL generation.
  name: PingCAP Data Summaries API
  slug: pingcap-data-summaries-api
- baseURL: https://docs.pingcap.com/ai/tidb-mcp-server/
  baseurl_source: declared
  description: Endpoints for managing and inspecting DDL jobs, including ownership and history.
  name: PingCAP DDL API
  slug: pingcap-ddl-api
- baseURL: https://docs.pingcap.com/ai/tidb-mcp-server/
  baseurl_source: declared
  description: Endpoints for downloading debug information and managing server diagnostics.
  name: PingCAP Diagnostics API
  slug: pingcap-diagnostics-api
- baseURL: https://docs.pingcap.com/ai/tidb-mcp-server/
  baseurl_source: declared
  description: Endpoints for retrieving multi-version concurrency control (MVCC) key details for debugging.
  name: PingCAP MVCC API
  slug: pingcap-mvcc-api
- baseURL: https://docs.pingcap.com/ai/tidb-mcp-server/
  baseurl_source: declared
  description: Endpoints for retrieving database and table schema information from the TiDB information schema.
  name: PingCAP Schema API
  slug: pingcap-schema-api
- baseURL: https://docs.pingcap.com/ai/tidb-mcp-server/
  baseurl_source: declared
  description: Operations for creating and managing multi-round conversational chat sessions.
  name: PingCAP Sessions API
  slug: pingcap-sessions-api
- baseURL: https://docs.pingcap.com/ai/tidb-mcp-server/
  baseurl_source: declared
  description: Endpoints for retrieving and modifying TiDB server runtime settings.
  name: PingCAP Settings API
  slug: pingcap-settings-api
- baseURL: https://docs.pingcap.com/ai/tidb-mcp-server/
  baseurl_source: declared
  description: Operations for refining and improving previously generated SQL queries.
  name: PingCAP SQL Refinement API
  slug: pingcap-sql-refinement-api
- baseURL: https://docs.pingcap.com/ai/tidb-mcp-server/
  baseurl_source: declared
  description: Endpoints for exporting optimizer statistics used for query planning.
  name: PingCAP Statistics API
  slug: pingcap-statistics-api
- baseURL: https://docs.pingcap.com/ai/tidb-mcp-server/
  baseurl_source: declared
  description: Endpoints for retrieving the operational status of the TiDB server instance.
  name: PingCAP Status API
  slug: pingcap-status-api
- baseURL: https://docs.pingcap.com/ai/tidb-mcp-server/
  baseurl_source: declared
  description: Manage the lifecycle and configuration of TiDB Cloud Premium instances, including passwords, CA certificates, and cloud provider information.
  name: PingCAP TiDB Cloud Premium Instance API
  slug: pingcap-tidb-cloud-premium-instance-api
artifact_total: 97
collections:
- collection_type: open
  name: IAM System OPEN API Key API
  slug: open-pingcap-api-key-api
- collection_type: open
  name: IAM System OPEN Audit Log API
  slug: open-pingcap-audit-log-api
- collection_type: open
  name: TiDB Cloud Backup API
  slug: open-pingcap-backup-api
- collection_type: open
  name: System OPEN Billing API
  slug: open-pingcap-billing-api
- collection_type: open
  name: TiDB Cloud Starter and Essential Branch API
  slug: open-pingcap-branch-api
- collection_type: open
  name: TiDB Cloud Dedicated Changefeed API
  slug: open-pingcap-changefeed-api
- collection_type: open
  name: TiDB Cloud Data Service OPEN Chat2 Query API
  slug: open-pingcap-chat2query-api
- collection_type: open
  name: Pingcap Cluster API
  slug: open-pingcap-cluster-api
- collection_type: open
  name: OSSInsight Public Collections API
  slug: open-pingcap-collections-api
- collection_type: open
  name: TiDB Cloud Data Service OPEN Data API Key API
  slug: open-pingcap-data-api-key-api
- collection_type: open
  name: TiDB Cloud Data Service OPEN Data App API
  slug: open-pingcap-data-app-api
- collection_type: open
  name: TiDB Cloud Data Service OPEN Data Source API
  slug: open-pingcap-data-source-api
- collection_type: open
  name: TiDB Cloud Data Service OPEN Deployment API
  slug: open-pingcap-deployment-api
- collection_type: open
  name: DM OpenAPI Doc API
  slug: open-pingcap-doc-api
- collection_type: open
  name: TiDB Cloud Data Service OPEN Endpoint API
  slug: open-pingcap-endpoint-api
- collection_type: open
  name: TiDB Cloud Starter and Essential Export API
  slug: open-pingcap-export-api
- collection_type: open
  name: Pingcap Import API
  slug: open-pingcap-import-api
- collection_type: open
  name: TiDB Cloud Dedicated Integration API
  slug: open-pingcap-integration-api
- collection_type: open
  name: OSSInsight Public Issue Creators API
  slug: open-pingcap-issue-creators-api
- collection_type: open
  name: IAM System OPEN Member API
  slug: open-pingcap-member-api
- collection_type: open
  name: TiDB Cloud Data Service OPEN OpenAPI Specification API
  slug: open-pingcap-openapi-specification-api
- collection_type: open
  name: TiDB Cloud Dedicated Private Endpoint Connection API
  slug: open-pingcap-private-endpoint-connection-api
- collection_type: open
  name: TiDB Cloud Project API
  slug: open-pingcap-project-api
- collection_type: open
  name: Control Plane Internal Public Shadow Pool Service API
  slug: open-pingcap-publicshadowpoolservice-api
- collection_type: open
  name: OSSInsight Public Pull Request Creators API
  slug: open-pingcap-pull-request-creators-api
- collection_type: open
  name: TiDB Cloud Dedicated Region API
  slug: open-pingcap-region-api
- collection_type: open
  name: TiDB Cloud Restore API
  slug: open-pingcap-restore-api
- collection_type: open
  name: DM OpenAPI DOC Source API
  slug: open-pingcap-source-api
- collection_type: open
  name: OSSInsight Public Stargazers API
  slug: open-pingcap-stargazers-api
- collection_type: open
  name: DM OpenAPI DOC Task API
  slug: open-pingcap-task-api
- collection_type: open
  name: OSSInsight Public Trends API
  slug: open-pingcap-trends-api
common:
- group: commercial
  href: https://artifacts.apis.io/pingcap/plans/pingcap-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pingcap-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.pingcap.com/feed/
- group: other
  href: https://artifacts.apis.io/pingcap/overlays/tidb-premium-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tidb-premium-overlay.yaml
- group: other
  href: https://artifacts.apis.io/pingcap/overlays/tidb-msp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tidb-msp-overlay.yaml
- group: other
  href: https://artifacts.apis.io/pingcap/capabilities/pingcap-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/pingcap-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/pingcap/pytidb/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/pingcap/pytidb/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/pingcap/pytidb/blob/main/CONTRIBUTING.md
- group: other
  href: https://artifacts.apis.io/pingcap/overlays/pingcap-ossinsight-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pingcap-ossinsight-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/pingcap/pytidb/blob/main/LICENSE
- group: agent
  href: https://artifacts.apis.io/pingcap/agentic-access/pingcap-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pingcap-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/pingcap/security/pingcap-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/pingcap-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.pingcap.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pingcap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pingcap.com/tidbcloud/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pingcap.com/tidbcloud/api-overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pingcap.com/tidbcloud/tidb-cloud-quickstart/
- group: operate
  title: ''
  type: Support
  url: https://tidb.support.pingcap.com/servicedesk/customer/portals
- group: operate
  title: ''
  type: HelpCenter
  url: https://tidb.support.pingcap.com/servicedesk/customer/portals
- group: company
  title: ''
  type: Blog
  url: https://www.pingcap.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pingcap
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/pingcap/tidb
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pingcap.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://tidbcloud.com/free-trial
- group: start
  title: ''
  type: Login
  url: https://tidbcloud.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pingcap.com/legal/tidb-cloud-services-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pingcap.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.pingcap.com/trust-hub/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.pingcap.com/trust-hub/
- group: operate
  title: ''
  type: SLA
  url: https://www.pingcap.com/legal/service-level-agreement-for-tidb-cloud-services/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tidbcloud.com/
- group: auth
  title: ''
  type: Security
  url: https://www.pingcap.com/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.pingcap.com/tidbcloud/tidb-cloud-release-notes/
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/KVRZBR2DrG
- group: agent
  href: https://artifacts.apis.io/pingcap/llms/pingcap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pingcap-llms.txt
- group: agent
  href: https://artifacts.apis.io/pingcap/well-known/pingcap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pingcap-well-known.yml
- group: build
  href: https://artifacts.apis.io/pingcap/packages/pingcap-packages.yml
  title: ''
  type: Packages
  url: packages/pingcap-packages.yml
- group: build
  href: https://artifacts.apis.io/pingcap/packages/pingcap-packages.yml
  title: ''
  type: SDKs
  url: packages/pingcap-packages.yml
- group: build
  href: https://artifacts.apis.io/pingcap/cli/pingcap-cli.yml
  title: ''
  type: CLI
  url: cli/pingcap-cli.yml
- group: start
  href: https://artifacts.apis.io/pingcap/sandbox/pingcap-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/pingcap-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/pingcap/mcp/pingcap-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pingcap-mcp.yml
- group: build
  href: https://artifacts.apis.io/pingcap/mcp/pingcap-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/pingcap-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/pingcap/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/pingcap/authentication/pingcap-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pingcap-authentication.yml
- group: design
  href: https://artifacts.apis.io/pingcap/conventions/pingcap-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pingcap-conventions.yml
- group: operate
  href: https://artifacts.apis.io/pingcap/rate-limits/pingcap-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pingcap-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/pingcap/errors/pingcap-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pingcap-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pingcap/errors/pingcap-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/pingcap-error-codes.yml
- group: design
  href: https://artifacts.apis.io/pingcap/lifecycle/pingcap-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pingcap-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/pingcap/conformance/pingcap-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pingcap-conformance.yml
- group: design
  href: https://artifacts.apis.io/pingcap/data-model/pingcap-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pingcap-data-model.yml
- group: auth
  href: https://artifacts.apis.io/pingcap/security/pingcap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pingcap-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/pingcap/security/pingcap-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pingcap-vulnerability-disclosure.yml
- group: operate
  href: https://artifacts.apis.io/pingcap/changelog/pingcap-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pingcap-changelog.yml
created: '2026-08-02'
description: PingCAP is the company behind TiDB, an open-source, MySQL-compatible distributed SQL database built for hybrid transactional and analytical processing (HTAP), horizontal scale-out, Raft-based strong consistency, and vector search for AI workloads. PingCAP operates TiDB Cloud, the fully managed DBaaS delivered in Starter, Essential, Premium, Dedicated, BYOC and Lake tiers across AWS, Google Cloud, Azure and Alibaba Cloud. Developers manage the platform programmatically through the TiDB Cloud REST API family (cluster, branch, import, export, changefeed, IAM, billing and Data Service surfaces), the `ticloud` CLI, a Terraform provider, the TiDB Cloud Serverless JavaScript driver, the PyTiDB Python SDK, and an official TiDB MCP Server for agents. PingCAP also publishes OpenAPI for the TiDB Data Migration (DM) control plane and the OSS Insight public API.
finops:
- has_sources: true
  method: derived
  name: Pingcap Finops
  primary_unit: compute
  service_category: ''
  slug: pingcap-finops
  template: false
image: https://static.pingcap.com/files/2024/09/11005522/Homepage-Ad.png
json_schemas:
- name: TiDB Cloud Cluster
  property_count: 14
  slug: tidb-cluster
- name: TiDB Cloud Data Service
  property_count: 6
  slug: tidb-data-service
layout: provider
mcp_servers:
- description: MCP server; 7 tools listed.
  name: PingCAP MCP Server
  slug: tidb-mcp-server
modified: '2026-10-06'
name: PingCAP
nav: Providers
network: true
overview: 'PingCAP publishes 45 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Key API, Audit Log API, Backup API, and 42 more. Tagged areas include Distributed SQL, Database, tidb, HTAP, and MySQL Compatible.


  The PingCAP catalog on APIs.io includes 1 Spectral governance ruleset.


  PingCAP''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 47 more developer resources.'
plans:
- name: Pingcap Plans Pricing
  plan_count: 8
  slug: pingcap-plans-pricing
- name: Pingcap Price Estimates
  plan_count: 0
  slug: pingcap-price-estimates
random_paper: 18
rate_limits:
- limit_count: 1
  name: Pingcap Rate Limits
  slug: pingcap-rate-limits
- limit_count: 6
  name: Tidb Rate Limits
  slug: tidb-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: PingCAP API Rules
  rule_count: 54
  severity_counts:
    error: 29
    hint: 0
    info: 6
    warn: 19
  slug: pingcap-rules
score:
  band: exemplar
  composite: 69.8
  coverage:
    artifact_dirs: 32
    catalog_earned: 67.5
    catalog_earned_first_party: 20.0
    catalog_gap: 47.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 31.8
    contract_quality: 49.1
    developer_ergonomics: 85.7
    discoverability: 76.7
    operational_transparency: 65.8
  open_source:
    applies: true
    score: 50.0
  previous_composite: 69.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 62.2
      derived: 0
      marker_coverage: 0.0
      total: 44
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/pingcap/pingcap-2026-08-17T081238.png
security:
- kind: authentication
  name: Pingcap Authentication
  slug: pingcap-authentication
  summary_line: http · 4 schemes
- kind: authentication
  name: Tidb Authentication
  slug: tidb-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pingcap Domain Security
  slug: pingcap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pingcap Vulnerability Disclosure
  slug: pingcap-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Pingcap Trust Center
  slug: pingcap-trust-center
  summary_line: ISO 27001, ISO 27701, SOC 2, PCI DSS, GDPR, HIPAA, EU-US Data Privacy Framework
skill_count: 6
skills:
- name: mysql
  slug: pingcap-agent-rules-mysql
- name: pytidb
  slug: pingcap-agent-rules-pytidb
- name: tidb-cloud-zero
  slug: pingcap-agent-rules-tidb-cloud-zero
- name: tidb-query-tuning
  slug: pingcap-agent-rules-tidb-query-tuning
- name: tidb-zero
  slug: pingcap-tidbcloud-tidb-zero
- name: tidbcloud-manager
  slug: pingcap-tidbcloud-tidbcloud-manager
slug: pingcap
tags:
- Distributed SQL
- Database
- tidb
- HTAP
- MySQL Compatible
- Cloud Database
- Database-as-a-Service
- Vector Search
- Data Migration
- Change Data Capture
- Open Source
- Infrastructure
website: https://www.pingcap.com/
---
