---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 146
  human_in_the_loop: 5
  name: Arangodb Agentic Access
  operation_count: 254
  slug: arangodb-agentic-access
  summary_line: 254 operations · 146 acting · 5 human-in-the-loop
api_count: 1
apis:
- description: The control-plane API of the Arango Managed Platform (formerly ArangoGraph Insights Platform / Oasis) — the managed ArangoDB cloud. It is a gRPC API defined in protocol buffers, covering organizations
  name: Arango Managed Platform (AMP) API
  slug: amp-api
- description: 'SCIM 2.0 user and group provisioning endpoint for Arango Managed Platform organizations, used to synchronize identities from an external identity provider into an AMP organization. Authenticated with '
  name: Arango Managed Platform SCIM API
  slug: amp-scim-api
- description: Get server information, manage licenses, shut down nodes, and more
  name: ArangoDB Administration API
  slug: arangodb-administration-api
- description: Manage Analyzers for transforming data
  name: ArangoDB Analyzers API
  slug: arangodb-analyzers-api
- description: Manage session tokens and JWT secrets
  name: ArangoDB Authentication API
  slug: arangodb-authentication-api
- description: Run multiple operations using a single request
  name: ArangoDB Batch Requests API
  slug: arangodb-batch-requests-api
- description: Get information, monitor, and administrate cluster deployments
  name: ArangoDB Cluster API
  slug: arangodb-cluster-api
- description: Manage collections for organizing documents
  name: ArangoDB Collections API
  slug: arangodb-collections-api
- description: Manage databases for organizing collections
  name: ArangoDB Databases API
  slug: arangodb-databases-api
- description: Perform CRUD operations on JSON-based records
  name: ArangoDB Documents API
  slug: arangodb-documents-api
- description: Manage microservices written in JavaScript
  name: ArangoDB Foxx API
  slug: arangodb-foxx-api
- description: Manage named graphs and query edges
  name: ArangoDB Graphs API
  slug: arangodb-graphs-api
- description: Manage incremental data backups
  name: ArangoDB Hot Backups API
  slug: arangodb-hot-backups-api
- description: Load JSON data in bulk
  name: ArangoDB Import API
  slug: arangodb-import-api
- description: Improve the performance of queries
  name: ArangoDB Indexes API
  slug: arangodb-indexes-api
- description: Execute requests asynchronously
  name: ArangoDB Jobs API
  slug: arangodb-jobs-api
- description: Access logs, statistics, and metrics
  name: ArangoDB Monitoring API
  slug: arangodb-monitoring-api
- description: Run, process, and manage AQL queries
  name: ArangoDB Queries API
  slug: arangodb-queries-api
- description: Control data replication for deployments
  name: ArangoDB Replication API
  slug: arangodb-replication-api
- description: Configure audit logging, encryption at rest and encryption in transit
  name: ArangoDB Security API
  slug: arangodb-security-api
- description: Set up JavaScript code to run periodically or timed
  name: ArangoDB Tasks API
  slug: arangodb-tasks-api
- description: Execute JavaScript and Stream Transactions
  name: ArangoDB Transactions API
  slug: arangodb-transactions-api
- description: Manage ArangoDB user accounts
  name: ArangoDB Users API
  slug: arangodb-users-api
- description: Manage Views to use ArangoSearch for information retrieval
  name: ArangoDB Views API
  slug: arangodb-views-api
artifact_total: 51
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ArangoDB Core Administration API
  slug: open-arangodb-administration-api
- collection_type: open
  name: ArangoDB Core Analyzers API
  slug: open-arangodb-analyzers-api
- collection_type: open
  name: ArangoDB Core Authentication API
  slug: open-arangodb-authentication-api
- collection_type: open
  name: ArangoDB Core Batch Requests API
  slug: open-arangodb-batch-requests-api
- collection_type: open
  name: ArangoDB Core Cluster API
  slug: open-arangodb-cluster-api
- collection_type: open
  name: ArangoDB Core Collections API
  slug: open-arangodb-collections-api
- collection_type: open
  name: ArangoDB Core Databases API
  slug: open-arangodb-databases-api
- collection_type: open
  name: ArangoDB Core Documents API
  slug: open-arangodb-documents-api
- collection_type: open
  name: ArangoDB Core Foxx API
  slug: open-arangodb-foxx-api
- collection_type: open
  name: ArangoDB Core Graphs API
  slug: open-arangodb-graphs-api
- collection_type: open
  name: ArangoDB Core Hot Backups API
  slug: open-arangodb-hot-backups-api
- collection_type: open
  name: ArangoDB Core Import API
  slug: open-arangodb-import-api
- collection_type: open
  name: ArangoDB Core Indexes API
  slug: open-arangodb-indexes-api
- collection_type: open
  name: ArangoDB Core Jobs API
  slug: open-arangodb-jobs-api
- collection_type: open
  name: ArangoDB Core Monitoring API
  slug: open-arangodb-monitoring-api
- collection_type: open
  name: ArangoDB Core Queries API
  slug: open-arangodb-queries-api
- collection_type: open
  name: ArangoDB Core Replication API
  slug: open-arangodb-replication-api
- collection_type: open
  name: ArangoDB Core Security API
  slug: open-arangodb-security-api
- collection_type: open
  name: ArangoDB Core Tasks API
  slug: open-arangodb-tasks-api
- collection_type: open
  name: ArangoDB Core Transactions API
  slug: open-arangodb-transactions-api
- collection_type: open
  name: ArangoDB Core Users API
  slug: open-arangodb-users-api
- collection_type: open
  name: ArangoDB Core Views API
  slug: open-arangodb-views-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/arangodb-core-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://arango.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://arango.ai/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arango.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.arango.ai/arangodb/stable/develop/http-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.arango.ai/arangodb/stable/get-started/
- group: company
  title: ''
  type: Blog
  url: https://arango.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arangodb
- group: operate
  title: ''
  type: Support
  url: https://arango.ai/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://arango.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.arangodb.cloud/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arango.ai/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.arangodb.cloud/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.arango.ai/arangodb/stable/release-notes/deprecated-and-removed-features/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/arangodb-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/arangodb-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arangodb-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/arangodb-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/arangodb-error-codes.yml
- group: build
  title: ''
  type: Packages
  url: packages/arangodb-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/arangodb-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/arangodb-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/arangodb-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/arangodb-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arangodb-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/arangodb-well-known.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/
- group: design
  title: ''
  type: Conformance
  url: conformance/arangodb-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/arangodb-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arangodb-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arangodb-agentic-access.yml
created: '2026-08-02'
description: ArangoDB (now operating as Arango) is the company behind the open-source, graph-native multi-model database of the same name, which unifies graph, document, key/value, vector and full-text search in a single core with one declarative query language, AQL. The database exposes its entire feature surface over a RESTful HTTP API documented with OpenAPI 3.1, and the company also runs the Arango Managed Platform (AMP, formerly ArangoGraph Insights Platform / Oasis) — a managed cloud on AWS, GCP and Azure whose control plane is a gRPC/Protobuf API at api.cloud.arangodb.com with a companion oasisctl CLI. Arango publishes official drivers for JavaScript, Python, Java, Go and PHP, an official Model Context Protocol server for AQL generation, and a Kubernetes operator.
image: https://arango.ai/wp-content/uploads/2026/03/arango-home-social-horz-2026.03-compress.png
layout: provider
mcp_servers:
- description: ''
  name: ArangoDB MCP Server
  slug: arangodb-mcp-server
modified: '2026-08-02'
name: ArangoDB
nav: Providers
network: true
overview: 'ArangoDB publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Administration API, Analyzers API, Authentication API, and 19 more. Tagged areas include Company, Database, Graph Database, Multi-Model Database, and NoSQL.


  ArangoDB''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 25 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 46.8
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 47.0
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arangodb/refs/heads/main/screenshots/arangodb-2026-08-07T161603.png
security:
- kind: authentication
  name: Arangodb Authentication
  slug: arangodb-authentication
  summary_line: http/apiKey · 0 schemes
- kind: domain-security
  name: Arangodb Domain Security
  slug: arangodb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: arangodb
tags:
- Company
- Database
- Graph Database
- Multi-Model Database
- NoSQL
- Vector Search
- Knowledge Graph
- Developer Tools
- Cloud Infrastructure
- Artificial Intelligence
website: https://arango.ai/
---
