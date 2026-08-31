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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: RocksDB C++ library API providing key-value storage operations including Get, Put, Delete, Merge, iterators, snapshots, column families, transactions, compaction, and backup. The primary interface for
  name: RocksDB Embedded API
  slug: rocksdb-embedded-api
- description: Official Java bindings for RocksDB providing full access to the RocksDB feature set from Java applications. Used in distributed systems like Apache Kafka Streams, Flink, and Cassandra as the underlyin
  name: RocksJava API
  slug: rocksjava-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rocksdb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rocksdb.org/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/facebook/rocksdb
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/facebook/rocksdb/wiki
- group: start
  title: ''
  type: GettingStarted
  url: https://rocksdb.org/docs/getting-started.html
- group: build
  title: ''
  type: Examples
  url: https://github.com/facebook/rocksdb/tree/main/examples
- group: build
  title: ''
  type: PackageManager
  url: https://mvnrepository.com/artifact/org.rocksdb/rocksdbjni
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/rocksdb-options-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/rocksdb-key-value-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/rocksdb-options-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/rocksdb-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/rocksdb-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://rocksdb.org/feed.xml
created: '2025-01-01'
description: RocksDB is an embeddable persistent key-value store for fast storage, developed at Facebook (Meta) based on LevelDB. It uses a Log-Structured Merge (LSM) tree design optimized for fast, low-latency storage on flash and RAM. RocksDB provides a C++ library with language bindings for Java, Python, Ruby, Rust, and other languages, and is widely used as the storage engine inside databases, data streaming systems, and distributed key-value stores.
examples:
- key_count: 6
  name: Rocksdb Get Example
  slug: rocksdb-get-example
- key_count: 6
  name: Rocksdb Put Example
  slug: rocksdb-put-example
finops:
- name: Rocksdb Finops
  service_category: API
  slug: rocksdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rocksdb.png
json_schemas:
- name: RocksDB Key-Value Entry
  property_count: 7
  slug: rocksdb-key-value
- name: RocksDB Options
  property_count: 18
  slug: rocksdb-options
json_structures:
- name: Rocksdb Options Structure
  property_count: 0
  slug: rocksdb-options-structure
jsonld:
- class_count: 13
  name: Rocksdb Context
  property_count: 14
  slug: rocksdb-context
layout: provider
modified: '2026-05-02'
name: RocksDB
nav: Providers
network: true
overview: 'RocksDB publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include RocksDB, Key-Value Store, Embedded Database, Storage Engine, and Open-Source.


  The RocksDB catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RocksDB''s developer surface includes documentation, getting-started guide, code examples, engineering blog, and 9 more developer resources.'
plans:
- name: Rocksdb Plans Pricing
  plan_count: 3
  slug: rocksdb-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Rocksdb Rate Limits
  slug: rocksdb-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: RocksDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: rocksdb-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 49.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 21.3
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 24.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rocksdb/refs/heads/main/screenshots/rocksdb-2026-06-20T193155.png
security:
- kind: domain-security
  name: Rocksdb Domain Security
  slug: rocksdb-domain-security
  summary_line: TLSv1.3
slug: rocksdb
tags:
- RocksDB
- Key-Value Store
- Embedded Database
- Storage Engine
- Open-Source
website: https://rocksdb.org/
---
