---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 63.1
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 93
  human_in_the_loop: 5
  name: Pingcap Agentic Access
  operation_count: 192
  slug: pingcap-agentic-access
  summary_line: 192 operations · 93 acting · 5 human-in-the-loop
api_count: 10
apis:
- description: 'REST API for managing TiDB Cloud Starter and TiDB Cloud Essential instances: cluster lifecycle, database branches, data export tasks and data import tasks. HTTPS-only, JSON entities, HTTP Digest authe'
  name: TiDB Cloud Starter and Essential API (v1beta1)
  slug: tidb-cloud-starter-and-essential-api-v1beta1
- description: 'REST API for managing TiDB Cloud Dedicated clusters: cluster CRUD, pause/resume, root password reset, node quota, regions and node specs, private endpoint connections, data imports, third-party integr'
  name: TiDB Cloud Dedicated API (v1beta1)
  slug: tidb-cloud-dedicated-api-v1beta1
- description: 'REST API for TiDB Cloud identity and access management: create, list, update and delete organization API keys, list audit logs, and manage organization members and their roles including batch updates '
  name: TiDB Cloud IAM API (v1beta1)
  slug: tidb-cloud-iam-api-v1beta1
- description: 'REST API for TiDB Cloud billing: retrieve the monthly bill for an organization, retrieve line-item bill details, and query the cost explorer with supported grouping and filter arguments.'
  name: TiDB Cloud Billing API (v1beta1)
  slug: tidb-cloud-billing-api-v1beta1
- description: 'REST API for TiDB Cloud Data Service: manage Data Apps, data sources, custom HTTP endpoints backed by SQL, deployments and Data API keys. Data Service also generates an OpenAPI 3.0 specification per D'
  name: TiDB Cloud Data Service API (v1beta1)
  slug: tidb-cloud-data-service-api-v1beta1
- description: 'The original TiDB Cloud administrative REST API covering projects, clusters, backups, restores and the deprecated import surface. Superseded by the v1beta1 tier-specific APIs but still documented and '
  name: TiDB Cloud API (v1beta, legacy)
  slug: tidb-cloud-api-v1beta-legacy
- description: Unauthenticated REST API that provisions a disposable, MySQL-compatible TiDB database in a single call. Instances auto-expire after 30 days unless claimed into a regular TiDB Cloud Starter instance. U
  name: TiDB Cloud Zero API (v1alpha1)
  slug: tidb-cloud-zero-api-v1alpha1
- description: OpenAPI 3.0 control-plane API for TiDB Data Migration, the platform that replicates MySQL-compatible upstreams into TiDB. Covers upstream source registration, relay log control, migration task lifecyc
  name: TiDB Data Migration (DM) OpenAPI
  slug: tidb-data-migration-dm-openapi
- description: Public read-only REST API behind OSS Insight, the PingCAP-built open-source analytics service that queries billions of GitHub events stored in TiDB. Exposes repository, developer, organization, collec
  name: OSS Insight Public API
  slug: oss-insight-public-api
- description: Official Model Context Protocol server maintained by PingCAP that exposes a TiDB or TiDB Cloud database to MCP-capable agents and IDEs. Ships in the pytidb package, runs over stdio by default or SSE w
  name: TiDB MCP Server
  slug: tidb-mcp-server
artifact_total: 17
common:
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
overview: 'PingCAP publishes 9 APIs on the [APIs.io](https://apis.io/) network, including TiDB Cloud Starter and Essential API (v1beta1), TiDB Cloud Dedicated API (v1beta1), TiDB Cloud IAM API (v1beta1), and 6 more. Tagged areas include distributed-sql, database, tidb, htap, and mysql-compatible.


  PingCAP''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
random_paper: 73
rate_limits:
- limit_count: 1
  name: Pingcap Rate Limits
  slug: pingcap-rate-limits
score:
  band: strong
  composite: 62.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 49.3
    developer_ergonomics: 87.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 68.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 11.1
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
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
