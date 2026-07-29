---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: 'The Gremlin Server provides WebSocket and HTTP endpoints for submitting Gremlin traversals to a remote graph database. The HTTP API accepts POST requests with Gremlin traversal strings or bytecode at '
  name: Apache TinkerPop Gremlin Server API
  slug: apache-tinkerpop-gremlin-server-api
- description: The Gremlin graph traversal language and API provide a functional, data-flow-based language for expressing complex graph queries and mutations. Gremlin steps include vertex/edge traversals (V, E, out,
  name: Apache TinkerPop Gremlin Traversal API
  slug: apache-tinkerpop-gremlin-api
artifact_total: 24
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-tinkerpop-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-tinkerpop-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tinkerpop
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/tinkerpop
- group: docs
  title: ''
  type: Documentation
  url: https://tinkerpop.apache.org/docs/current/reference/
- group: start
  title: ''
  type: Portal
  url: https://tinkerpop.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://tinkerpop.apache.org/docs/current/tutorials/getting-started/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/apache/tinkerpop/releases
- group: operate
  title: ''
  type: Support
  url: https://groups.google.com/g/gremlin-users
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
created: '2026-03-16'
description: Apache TinkerPop is a graph computing framework for both graph databases (OLTP) and graph analytic systems (OLAP). It provides the Gremlin graph traversal language which works with any TinkerPop-enabled graph system. TinkerPop abstracts the underlying graph database, allowing applications to work with Neo4j, Amazon Neptune, Azure Cosmos DB, JanusGraph, Amazon DynamoDB, and other graph databases using a single consistent API. It is maintained by the Apache Software Foundation.
features:
- description: Single API working across Neo4j, JanusGraph, Amazon Neptune, Azure Cosmos DB, and 20+ graph systems.
  name: Graph Database Abstraction
- description: Expressive functional graph traversal language for both queries and mutations.
  name: Gremlin Language
- description: Bulk/analytical graph processing via SparkGraphComputer for large-scale graph algorithms.
  name: OLAP Graph Processing
- description: Compact binary serialization format for efficient Gremlin traversal encoding.
  name: GraphBinary Serialization
- description: JSON-based graph serialization format for human-readable graph data exchange.
  name: GraphSON Format
- description: Standalone server hosting Gremlin traversal execution over WebSocket or HTTP.
  name: Gremlin Server
- description: Official Gremlin SDKs for Java, Python, JavaScript, Go, and .NET.
  name: Multi-Language SDKs
finops:
- name: Apache Tinkerpop Finops
  service_category: API
  slug: apache-tinkerpop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-tinkerpop.png
integrations:
- description: AWS managed graph database with full TinkerPop and Gremlin compatibility.
  name: Amazon Neptune
- description: Azure Cosmos DB Gremlin API for TinkerPop-compatible graph storage.
  name: Azure Cosmos DB
- description: Distributed graph database with TinkerPop/Gremlin interface and Cassandra/HBase backend.
  name: JanusGraph
- description: Neo4j TinkerPop plugin for Gremlin traversal on Neo4j graph data.
  name: Neo4j
- description: SparkGraphComputer for OLAP graph analytics on Spark clusters.
  name: Apache Spark
layout: provider
modified: '2026-04-19'
name: Apache TinkerPop
nav: Providers
network: true
overview: 'Apache TinkerPop publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Graph Computing, Graph Database, Gremlin, OLAP, and OLTP.


  Apache TinkerPop''s developer surface includes documentation, developer portal, getting-started guide, release notes, support, and 5 more developer resources.'
plans:
- name: Apache Tinkerpop Plans Pricing
  plan_count: 3
  slug: apache-tinkerpop-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Apache Tinkerpop Rate Limits
  slug: apache-tinkerpop-rate-limits
score:
  band: thin
  composite: 28.6
  delta: -2.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 30.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-tinkerpop/refs/heads/main/screenshots/apache-tinkerpop-2026-06-20T172154.png
security:
- kind: domain-security
  name: Apache Tinkerpop Domain Security
  slug: apache-tinkerpop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Tinkerpop Vulnerability Disclosure
  slug: apache-tinkerpop-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-tinkerpop
tags:
- Graph Computing
- Graph Database
- Gremlin
- OLAP
- OLTP
- Open Source
use_cases:
- description: Build and query knowledge graphs for entity relationship modeling.
  name: Knowledge Graphs
- description: Traverse and analyze social graph relationships and influence patterns.
  name: Social Network Analysis
- description: Detect fraud rings and suspicious patterns via graph relationship traversal.
  name: Fraud Detection
- description: Graph-based collaborative filtering and content recommendation.
  name: Recommendation Engines
- description: Model and query complex permission hierarchies and role relationships.
  name: Identity and Access Management
website: https://tinkerpop.apache.org/
---
