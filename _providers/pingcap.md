---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 63.5
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 93
  human_in_the_loop: 5
  name: Pingcap Agentic Access
  operation_count: 192
  slug: pingcap-agentic-access
  summary_line: 192 operations · 93 acting · 5 human-in-the-loop
api_count: 32
apis:
- description: Official Model Context Protocol server maintained by PingCAP that exposes a TiDB or TiDB Cloud database to MCP-capable agents and IDEs. Ships in the pytidb package, runs over stdio by default or SSE w
  name: TiDB MCP Server
  slug: tidb-mcp-server
- description: The API Key API from PingCAP — 2 operation(s) for api key.
  name: PingCAP API Key API
  slug: pingcap-api-key-api
- description: The Audit Log API from PingCAP — 1 operation(s) for audit log.
  name: PingCAP Audit Log API
  slug: pingcap-audit-log-api
- description: Create, get, modify, and delete backups for TiDB clusters. For TiDB Cloud Starter instances, you cannot create or manage backups via API. You can use [Dumpling](https://docs.pingcap.com/tidb/stable/du
  name: PingCAP Backup API
  slug: pingcap-backup-api
- description: The Billing API from PingCAP — 4 operation(s) for billing.
  name: PingCAP Billing API
  slug: pingcap-billing-api
- description: The Branch API from PingCAP — 3 operation(s) for branch.
  name: PingCAP Branch API
  slug: pingcap-branch-api
- description: List changefeed RCU options, list changefeeds, create a changefeed, get a changefeed, delete a changefeed, update a changefeed downstream config, pause a changefeed, resume a changefeed, and scale a c
  name: PingCAP Changefeed API
  slug: pingcap-changefeed-api
- description: The Chat2Query API from PingCAP — 1 operation(s) for chat2query.
  name: PingCAP Chat2 Query API
  slug: pingcap-chat2query-api
- description: Create, get, update, delete, pause, resume, reset the root password, and list node quotas of a cluster.
  name: PingCAP Cluster API
  slug: pingcap-cluster-api
- description: The Collections API from PingCAP — 6 operation(s) for collections.
  name: PingCAP Collections API
  slug: pingcap-collections-api
- description: Create, get, update, delete, and list Data API keys of a Data App. The Data API key in Data Service is different from the key used in the [TiDB Cloud API](https://docs.pingcap.com/tidbcloud/api/v1beta
  name: PingCAP Data API Key API
  slug: pingcap-data-api-key-api
- description: Create, get, update, delete, and list Data Apps.
  name: PingCAP Data App API
  slug: pingcap-data-app-api
- description: Create, get, delete, and list data sources of a Data App.
  name: PingCAP Data Source API
  slug: pingcap-data-source-api
- description: Create, get, and list deployments of a Data App.
  name: PingCAP Deployment API
  slug: pingcap-deployment-api
- description: The doc API from PingCAP — 2 operation(s) for doc.
  name: PingCAP Doc API
  slug: pingcap-doc-api
- description: Create, get, delete, list, and test endpoints of a Data App.
  name: PingCAP Endpoint API
  slug: pingcap-endpoint-api
- description: The Export API from PingCAP — 3 operation(s) for export.
  name: PingCAP Export API
  slug: pingcap-export-api
- description: List import tasks, create an import task, get an import task, and cancel an import task.
  name: PingCAP Import API
  slug: pingcap-import-api
- description: List integrations, create an integration, and delete an integration.
  name: PingCAP Integration API
  slug: pingcap-integration-api
- description: The Issue Creators API from PingCAP — 4 operation(s) for issue creators.
  name: PingCAP Issue Creators API
  slug: pingcap-issue-creators-api
- description: The Member API from PingCAP — 4 operation(s) for member.
  name: PingCAP Member API
  slug: pingcap-member-api
- description: Get the OpenAPI specification of a Data App.
  name: PingCAP OpenAPI Specification API
  slug: pingcap-openapi-specification-api
- description: Get private link service for a TiDB node group, create a private endpoint connection, list private endpoint connections, get a private endpoint connection, and delete a private endpoint connection.
  name: PingCAP Private Endpoint Connection API
  slug: pingcap-private-endpoint-connection-api
- description: List projects.
  name: PingCAP Project API
  slug: pingcap-project-api
- description: The PublicShadowPoolService API from PingCAP — 1 operation(s) for publicshadowpoolservice.
  name: PingCAP Public Shadow Pool Service API
  slug: pingcap-publicshadowpoolservice-api
- description: The Pull Request Creators API from PingCAP — 4 operation(s) for pull request creators.
  name: PingCAP Pull Request Creators API
  slug: pingcap-pull-request-creators-api
- description: List regions, get a region, and list cloud providers and node specs of a region.
  name: PingCAP Region API
  slug: pingcap-region-api
- description: Get and create restore tasks for TiDB clusters. You can only restore data to a new cluster. For more information on restoration on TiDB Cloud, refer to [Restore](https://docs.pingcap.com/tidbcloud/bac
  name: PingCAP Restore API
  slug: pingcap-restore-api
- description: source
  name: PingCAP Source API
  slug: pingcap-source-api
- description: The Stargazers API from PingCAP — 3 operation(s) for stargazers.
  name: PingCAP Stargazers API
  slug: pingcap-stargazers-api
- description: task
  name: PingCAP Task API
  slug: pingcap-task-api
- description: The Trends API from PingCAP — 1 operation(s) for trends.
  name: PingCAP Trends API
  slug: pingcap-trends-api
artifact_total: 39
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/pingcap-ossinsight-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/pingcap/pytidb/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pingcap-agentic-access.yml
- group: auth
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
  title: ''
  type: LLMsTxt
  url: llms/pingcap-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pingcap-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/pingcap-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pingcap-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/pingcap-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pingcap-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pingcap-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/pingcap-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pingcap-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pingcap-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pingcap-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pingcap-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/pingcap-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pingcap-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pingcap-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pingcap-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pingcap-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pingcap-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pingcap-changelog.yml
created: '2026-08-02'
description: PingCAP is the company behind TiDB, an open-source, MySQL-compatible distributed SQL database built for hybrid transactional and analytical processing (HTAP), horizontal scale-out, Raft-based strong consistency, and vector search for AI workloads. PingCAP operates TiDB Cloud, the fully managed DBaaS delivered in Starter, Essential, Premium, Dedicated, BYOC and Lake tiers across AWS, Google Cloud, Azure and Alibaba Cloud. Developers manage the platform programmatically through the TiDB Cloud REST API family (cluster, branch, import, export, changefeed, IAM, billing and Data Service surfaces), the `ticloud` CLI, a Terraform provider, the TiDB Cloud Serverless JavaScript driver, the PyTiDB Python SDK, and an official TiDB MCP Server for agents. PingCAP also publishes OpenAPI for the TiDB Data Migration (DM) control plane and the OSS Insight public API.
image: https://static.pingcap.com/files/2024/09/11005522/Homepage-Ad.png
layout: provider
mcp_servers:
- description: ''
  name: pingcap-mcp.yml
  slug: pingcap-mcpyml
modified: '2026-08-02'
name: PingCAP
nav: Providers
network: true
overview: 'PingCAP publishes 31 APIs on the [APIs.io](https://apis.io/) network, including API Key API, Audit Log API, Backup API, and 28 more. Tagged areas include distributed-sql, database, tidb, htap, and mysql-compatible.


  PingCAP''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 39 more developer resources.'
random_paper: 42
rate_limits:
- limit_count: 1
  name: Pingcap Rate Limits
  slug: pingcap-rate-limits
score:
  band: strong
  composite: 61.2
  delta: 0.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 50.1
    developer_ergonomics: 87.0
    discoverability: 77.8
    governance: 20.8
    operational_transparency: 68.4
  previous_composite: 60.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 83.9
      derived: 0
      marker_coverage: 0.0
      total: 31
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Pingcap Authentication
  slug: pingcap-authentication
  summary_line: http · 4 schemes
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
slug: pingcap
tags:
- distributed-sql
- database
- tidb
- htap
- mysql-compatible
- cloud-database
- dbaas
- vector-search
- data-migration
- change-data-capture
- open-source
- infrastructure
website: https://www.pingcap.com/
---
