---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Yugabyte Agentic Access
  operation_count: 30
  slug: yugabyte-agentic-access
  summary_line: 30 operations · 2 acting
api_count: 10
apis:
- description: Programmatic management API for YugabyteDB Aeon, the fully managed cloud DBaaS. Deploy and manage clusters and read replicas, schedule and run on-demand backups and restores, manage IP allow lists, co
  name: YugabyteDB Aeon REST API
  slug: yugabytedb-aeon-rest-api
- description: APIs for getting backup Details
  name: Yugabyte backup-info API
  slug: yugabyte-backup-info-api
- description: APIs for cluster CRUD
  name: Yugabyte cluster API
  slug: yugabyte-cluster-api
- description: APIs for getting information about an existing cluster
  name: Yugabyte cluster-info API
  slug: yugabyte-cluster-info-api
- description: APIs for getting Point-in-Time Recovery (PITR) schedules
  name: Yugabyte pitr-info API
  slug: yugabyte-pitr-info-api
- description: APIs for getting restore Details
  name: Yugabyte restore-info API
  slug: yugabyte-restore-info-api
- description: APIs for getting information about Voyager migrations
  name: Yugabyte voyager-info API
  slug: yugabyte-voyager-info-api
- description: APIs for getting Voyager data migrations metrics
  name: Yugabyte voyager-metrics API
  slug: yugabyte-voyager-metrics-api
- description: The Xcluster Metrics API from Yugabyte — 1 operation(s) for xcluster metrics.
  name: Yugabyte Xcluster Metrics API
  slug: yugabyte-xcluster-metrics-api
- description: The Xcluster Namespace Details API from Yugabyte — 1 operation(s) for xcluster namespace details.
  name: Yugabyte Xcluster Namespace Details API
  slug: yugabyte-xcluster-namespace-details-api
artifact_total: 15
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.yugabyte.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.yugabyte.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.yugabyte.com/docs/managed-apis/9u5yqnccbe8lk-yugabyte-db-aeon-rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.yugabyte.com/stable/quick-start/
- group: operate
  title: ''
  type: Support
  url: https://forum.yugabyte.com/
- group: company
  title: ''
  type: Blog
  url: https://www.yugabyte.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yugabyte
- group: commercial
  title: ''
  type: Pricing
  url: https://www.yugabyte.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://cloud.yugabyte.com/signup
- group: start
  title: ''
  type: Login
  url: https://cloud.yugabyte.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.yugabyte.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yugabyte.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://yugabytedb.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.yugabyte.com/stable/releases/
- group: auth
  title: ''
  type: TrustCenter
  url: https://compliance.yugabyte.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.yugabyte.com/compliance/
- group: build
  title: ''
  type: Packages
  url: packages/yugabyte-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/yugabyte-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/yugabyte-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yugabyte-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/yugabyte-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yugabyte-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/yugabyte-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/yugabyte-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/yugabyte-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yugabyte-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/yugabyte-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/yugabyte-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/yugabyte-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/yugabyte-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yugabyte-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yugabyte-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Yugabyte is the company behind YugabyteDB, an open source (Apache 2.0), PostgreSQL-compatible distributed SQL database built for cloud-native and mission-critical applications. It pairs PostgreSQL wire-compatibility (the YSQL API) and a Cassandra-inspired API (YCQL) with horizontal scalability, built-in resilience, automatic sharding, and automatic failover across multi-region and multi-cloud deployments. Yugabyte ships the database in three form factors: self-managed YugabyteDB, YugabyteDB Anywhere for private and hybrid clouds, and YugabyteDB Aeon, a fully managed database-as-a-service. Developers integrate through PostgreSQL-compatible smart drivers, the YugabyteDB Aeon REST management API, the open source ybm CLI, a Terraform provider, and the yugabyted local admin API.'
image: https://github.com/yugabyte.png
layout: provider
mcp_servers:
- description: ''
  name: yugabyte-mcp.yml
  slug: yugabyte-mcpyml
modified: '2026-07-21'
name: Yugabyte
nav: Providers
network: true
overview: 'Yugabyte publishes 9 APIs on the [APIs.io](https://apis.io/) network, including backup-info API, cluster API, cluster-info API, and 6 more. Tagged areas include Company, Database, Distributed SQL, PostgreSQL, and Cloud.


  Yugabyte''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 55.3
  delta: -3.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.8
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 58.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Yugabyte Authentication
  slug: yugabyte-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Yugabyte Domain Security
  slug: yugabyte-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Yugabyte Trust Center
  slug: yugabyte-trust-center
  summary_line: SOC 2 Type II, SOC 3, ISO 27001, PCI DSS Level 1
slug: yugabyte
tags:
- Company
- Database
- Distributed SQL
- PostgreSQL
- Cloud
- DBaaS
- Open Source
- SQL
- Data
- Infrastructure
website: https://docs.yugabyte.com/
---
