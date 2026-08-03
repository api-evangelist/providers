---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Scylladb Agentic Access
  operation_count: 40
  slug: scylladb-agentic-access
  summary_line: 40 operations · 20 acting
api_count: 9
apis:
- description: Node-level administrative REST API exposing endpoints to check and update configuration, retrieve cluster-level and node-level information, and execute administrative operations. Exposed locally on po
  name: ScyllaDB Admin REST API
  slug: admin-rest-api
- description: The Account API from ScyllaDB — 5 operation(s) for account.
  name: ScyllaDB Account API
  slug: scylladb-account-api
- description: The Account Cluster Network API from ScyllaDB — 4 operation(s) for account cluster network.
  name: ScyllaDB Account Cluster Network API
  slug: scylladb-account-cluster-network-api
- description: The Account network cluster connection API from ScyllaDB — 2 operation(s) for account network cluster connection.
  name: ScyllaDB Account network cluster connection API
  slug: scylladb-account-network-cluster-connection-api
- description: The Cluster API from ScyllaDB — 10 operation(s) for cluster.
  name: ScyllaDB Cluster API
  slug: scylladb-cluster-api
- description: The Cluster Request API from ScyllaDB — 2 operation(s) for cluster request.
  name: ScyllaDB Cluster Request API
  slug: scylladb-cluster-request-api
- description: The Deployment API from ScyllaDB — 4 operation(s) for deployment.
  name: ScyllaDB Deployment API
  slug: scylladb-deployment-api
- description: The Pricing API from ScyllaDB — 1 operation(s) for pricing.
  name: ScyllaDB Pricing API
  slug: scylladb-pricing-api
- description: The VectorSearch API from ScyllaDB — 1 operation(s) for vectorsearch.
  name: ScyllaDB VectorSearch API
  slug: scylladb-vectorsearch-api
artifact_total: 33
collections:
- collection_type: postman
  name: ScyllaDB Cloud Account API
  slug: postman-scylladb-account-api
- collection_type: postman
  name: ScyllaDB Cloud Account Account Cluster Network API
  slug: postman-scylladb-account-cluster-network-api
- collection_type: postman
  name: ScyllaDB Cloud Account Account network cluster connection API
  slug: postman-scylladb-account-network-cluster-connection-api
- collection_type: postman
  name: ScyllaDB Cloud Account Cluster API
  slug: postman-scylladb-cluster-api
- collection_type: postman
  name: ScyllaDB Cloud Account Cluster Request API
  slug: postman-scylladb-cluster-request-api
- collection_type: postman
  name: ScyllaDB Cloud Account Deployment API
  slug: postman-scylladb-deployment-api
- collection_type: postman
  name: ScyllaDB Cloud Account Pricing API
  slug: postman-scylladb-pricing-api
- collection_type: postman
  name: ScyllaDB Cloud Account VectorSearch API
  slug: postman-scylladb-vectorsearch-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/scylladb/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scylladb-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/scylladb-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scylladb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scylladb-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.scylladb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scylladb.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.scylladb.com/stable/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scylladb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scylladb
- group: other
  title: ''
  type: X
  url: https://x.com/ScyllaDB
- group: company
  title: ''
  type: Blog
  url: https://resources.scylladb.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.scylladb.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.scylladb.com/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.scylladb.com/product/release-notes/
- group: operate
  title: ''
  type: Forums
  url: https://forum.scylladb.com/
- group: other
  title: ''
  type: University
  url: https://university.scylladb.com/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/scylladb-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/scylladb-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: commercial
  title: ''
  type: Plans
  url: plans/scylladb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scylladb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/scylladb-finops.yml
created: '2026-06-12'
description: ScyllaDB is a high-performance distributed NoSQL database engineered for real-time, data-intensive applications, offering close-to-the-metal architecture with predictable single-digit millisecond latencies and millions of operations per second. It is fully compatible with Apache Cassandra's CQL interface and Amazon DynamoDB's API (via Project Alternator), enabling drop-in migration from either platform. ScyllaDB Cloud is a fully managed database-as-a-service available on AWS and GCP, providing a REST management API for automating cluster provisioning, scaling, networking, and configuration. The platform supports vector search, multi-region active-active replication, and a Kubernetes operator for self-managed deployments.
examples:
- key_count: 10
  name: Scylladb Create Cluster Example
  slug: scylladb-create-cluster-example
- key_count: 1
  name: Scylladb Firewall Rules Example
  slug: scylladb-firewall-rules-example
- key_count: 1
  name: Scylladb List Clusters Example
  slug: scylladb-list-clusters-example
- key_count: 1
  name: Scylladb Node Info Example
  slug: scylladb-node-info-example
finops:
- name: Scylladb Finops
  service_category: Database
  slug: scylladb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scylladb.png
json_schemas:
- name: ClusterInfo
  property_count: 24
  slug: scylladb-cluster
- name: FirewallRule
  property_count: 3
  slug: scylladb-firewall-rule
- name: NodeInfo
  property_count: 17
  slug: scylladb-node
jsonld:
- class_count: 13
  name: Scylladb Context
  property_count: 25
  slug: scylladb-context
layout: provider
modified: '2026-06-12'
name: ScyllaDB
nav: Providers
network: true
overview: 'ScyllaDB publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Account Cluster Network API, Account network cluster connection API, and 5 more. Tagged areas include Database, NoSQL, Cassandra Compatible, DynamoDB Compatible, and Distributed Database.


  The ScyllaDB catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ScyllaDB''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, release notes, and 17 more developer resources.'
plans:
- name: Scylladb Plans Pricing
  plan_count: 4
  slug: scylladb-plans-pricing
random_paper: 86
rate_limits:
- limit_count: 2
  name: Scylladb Rate Limits
  slug: scylladb-rate-limits
rules:
- name: ScyllaDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: scylladb-jsonschema-spectral-rules
score:
  band: strong
  composite: 59.6
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 73.4
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 57.9
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scylladb/refs/heads/main/screenshots/scylladb-2026-06-20T193611.png
security:
- kind: authentication
  name: Scylladb Authentication
  slug: scylladb-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Scylladb Domain Security
  slug: scylladb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Scylladb Trust Center
  slug: scylladb-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS
slug: scylladb
tags:
- Database
- NoSQL
- Cassandra Compatible
- DynamoDB Compatible
- Distributed Database
- Real-Time
- Vector Search
- Cloud Database
website: https://www.scylladb.com/
---
