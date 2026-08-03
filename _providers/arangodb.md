---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 146
  human_in_the_loop: 5
  name: Arangodb Agentic Access
  operation_count: 254
  slug: arangodb-agentic-access
  summary_line: 254 operations · 146 acting · 5 human-in-the-loop
api_count: 3
apis:
- description: 'The RESTful HTTP API of the ArangoDB Core database system, version 3.12.10 (API v0). 174 paths and 254 operations across 22 tags covering documents, collections, databases, named graphs, indexes, AQL '
  name: ArangoDB Core API
  slug: arangodb-core-api
- description: The control-plane API of the Arango Managed Platform (formerly ArangoGraph Insights Platform / Oasis) — the managed ArangoDB cloud. It is a gRPC API defined in protocol buffers, covering organizations
  name: Arango Managed Platform (AMP) API
  slug: amp-api
- description: 'SCIM 2.0 user and group provisioning endpoint for Arango Managed Platform organizations, used to synchronize identities from an external identity provider into an AMP organization. Authenticated with '
  name: Arango Managed Platform SCIM API
  slug: amp-scim-api
artifact_total: 7
common:
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
  name: arangodb-mcp.yml
  slug: arangodb-mcpyml
modified: '2026-08-02'
name: ArangoDB
nav: Providers
network: true
overview: 'ArangoDB publishes 1 API on the [APIs.io](https://apis.io/) network: Core API. Tagged areas include Company, Database, Graph Database, Multi-Model Database, and NoSQL.


  ArangoDB''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 24 more developer resources.'
random_paper: 70
score:
  band: developing
  composite: 51.7
  facets:
    commercial_clarity: 34.2
    contract_quality: 53.2
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
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
