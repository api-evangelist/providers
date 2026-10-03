---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 31
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering managed databases and database-as-a-service offerings exposing APIs. Database APIs enable developers to provision, configure, query, migrate, and scale relational, document, key-value, wide-column, vector, graph, time-series, and analytical data stores through programmatic interfaces rather than through manual server administration. This collection includes managed PostgreSQL platforms like Neon, Supabase, and Render; MySQL platforms like PlanetScale and Vitess; document databases like MongoDB Atlas and Couchbase; key-value and wide-column stores like DynamoDB, Cassandra, and Aerospike; serverless databases like Fauna, Convex, and Cloudflare D1; vector databases like Pinecone, Weaviate, Qdrant, and Milvus; graph databases like Neo4j and Stardog; time-series databases like InfluxDB, TimescaleDB, and QuestDB; and analytical data warehouses like Snowflake, BigQuery, Redshift, Databricks, ClickHouse, and Firebolt.
examples:
- key_count: 16
  name: Database Instance Example
  slug: database-instance-example
- key_count: 15
  name: Database Schema Migration Example
  slug: database-schema-migration-example
features:
- description: Database APIs let teams create, configure, resize, and tear down database instances on demand without filing tickets or running infrastructure scripts, making databases first-class deployable resources.
  name: Programmatic Database Provisioning
- description: Modern serverless database platforms like Neon, PlanetScale, and Supabase expose branching APIs that let developers create isolated copies of a production database for development, testing, and pull request previews.
  name: Branching and Forking
- description: Databases like Neon, Supabase, PlanetScale, and Cloudflare D1 expose SQL execution through HTTPS endpoints, enabling stateless query access from serverless functions and edge runtimes without persistent TCP connections.
  name: HTTP and SQL-over-HTTP Query Interfaces
- description: Vector databases like Pinecone, Weaviate, Qdrant, and Milvus expose APIs for storing high-dimensional embeddings and running nearest-neighbor similarity search, powering retrieval-augmented generation and semantic search.
  name: Vector Search and Embeddings
- description: Database platforms provide APIs for managing schema migrations, deploy requests, and zero-downtime schema changes, integrating database evolution into CI/CD pipelines.
  name: Schema Migration and Versioning
- description: Cloud data warehouses like Snowflake, BigQuery, Redshift, Databricks, and ClickHouse expose REST and SQL APIs for executing analytical queries, managing warehouses, and orchestrating data pipelines at petabyte scale.
  name: Analytical Query and Warehouse APIs
- description: Distributed and serverless databases expose APIs for configuring read replicas, regional failover, and edge-local reads, reducing latency for globally distributed applications.
  name: Multi-Region Replication and Edge Reads
- description: Managed database APIs provide programmatic control over backups, snapshots, restore points, and point-in-time recovery, treating data protection as code rather than a manual operations process.
  name: Backups, Snapshots, and Point-in-Time Recovery
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Serverless PostgreSQL platform with branching, scale-to-zero compute, and an HTTP query endpoint designed for serverless and edge runtimes.
  name: Neon
- description: Open-source PostgreSQL platform with auto-generated REST and GraphQL APIs, realtime subscriptions, auth, storage, and edge functions.
  name: Supabase
- description: Serverless MySQL platform built on Vitess with non-blocking schema changes, deploy requests, and branching for safe production database evolution.
  name: PlanetScale
- description: Managed multi-cloud document database with Atlas Data API, Atlas Search, Atlas Vector Search, and a fully managed control plane API.
  name: MongoDB Atlas
- description: Cloud data warehouse with SQL API, REST control plane, and Snowpipe for streaming data ingestion across AWS, Azure, and GCP.
  name: Snowflake
- description: Managed vector database with REST and gRPC APIs for storing embeddings and running low-latency similarity search at scale.
  name: Pinecone
- description: Lakehouse platform with REST APIs for SQL warehouses, jobs, Unity Catalog, model serving, and Delta Lake table management.
  name: Databricks
- description: Distributed document-relational serverless database with a unified HTTP API, FQL query language, and ACID transactions across regions.
  name: Fauna
json_schemas:
- name: DatabaseInstance
  property_count: 16
  slug: database-instance
- name: SchemaMigration
  property_count: 15
  slug: database-schema-migration
json_structures:
- name: Database Instance Structure
  property_count: 16
  slug: database-instance-structure
- name: Database Schema Migration Structure
  property_count: 15
  slug: database-schema-migration-structure
jsonld:
- class_count: 5
  name: Database Context
  property_count: 27
  slug: database-context
layout: provider
modified: '2026-05-19'
name: Database
nav: Providers
network: true
overview: 'Database is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Database-as-a-Service, Managed Database, SQL, and NoSQL.


  The Database catalog on APIs.io includes 1 JSON-LD context.


  Database''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: database
tags:
- Database
- Database-as-a-Service
- Managed Database
- SQL
- NoSQL
- Document Database
- Graph Database
- Vector Database
- Time Series
- Data Warehouse
- Key-Value Store
use_cases:
- description: Developers use serverless database APIs from Neon, Supabase, Fauna, Convex, and Cloudflare D1 to back serverless functions and edge applications without managing connection pools or persistent infrastructure.
  name: Serverless Application Backends
- description: SaaS platforms use database provisioning APIs to spin up isolated database instances or branches per customer, providing strong tenant isolation and per-tenant backup, recovery, and scaling.
  name: Database-per-Tenant Provisioning
- description: AI applications use vector database APIs from Pinecone, Weaviate, Qdrant, Milvus, and pgvector-backed services to index document embeddings and retrieve semantically relevant context for LLM prompts.
  name: Retrieval-Augmented Generation (RAG)
- description: Time-series and columnar APIs from ClickHouse, InfluxDB, TimescaleDB, QuestDB, and Tinybird power real-time dashboards, observability platforms, and user-facing analytics on high-volume event streams.
  name: Real-Time Analytics and Observability
- description: Analytics and data teams use APIs from Snowflake, BigQuery, Redshift, and Databricks to load data, run transformations, manage warehouses, and integrate with dbt, Fivetran, and orchestration tooling.
  name: Data Warehouse Integration and ELT
- description: Teams use deploy-request and migration APIs from PlanetScale, Neon, and Supabase to gate schema changes through pull requests, run them in branches, and apply them safely to production.
  name: Schema Migrations in CI/CD
- description: Applications use graph database APIs from Neo4j, Stardog, and Amazon Neptune to model relationships, run path and traversal queries, and back knowledge graphs and recommendation engines.
  name: Graph Workloads and Knowledge Graphs
- description: Edge databases like Cloudflare D1, Convex, and Supabase expose APIs that synchronize state between edge runtimes, mobile clients, and central data stores with built-in conflict resolution.
  name: Edge and Mobile Data Sync
website: https://apievangelist.com
---
