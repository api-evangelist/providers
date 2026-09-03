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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Apache Geode Agentic Access
  operation_count: 14
  slug: apache-geode-agentic-access
  summary_line: 14 operations · 5 acting
api_count: 1
apis:
- description: Java API for cache operations, continuous queries, function execution, and data serialization in Apache Geode clusters.
  name: Apache Geode Java Client API
  slug: apache-geode-java-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Administration API from Apache Geode — 2 operation(s) for administration.
  name: Apache Geode Administration API
  slug: apache-geode-administration-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Functions API from Apache Geode — 2 operation(s) for functions.
  name: Apache Geode Functions API
  slug: apache-geode-functions-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Queries API from Apache Geode — 2 operation(s) for queries.
  name: Apache Geode Queries API
  slug: apache-geode-queries-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Regions API from Apache Geode — 4 operation(s) for regions.
  name: Apache Geode Regions API
  slug: apache-geode-regions-api
artifact_total: 69
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Geode REST Administration API
  slug: open-apache-geode-administration-api
- collection_type: open
  name: Apache Geode REST Administration Functions API
  slug: open-apache-geode-functions-api
- collection_type: open
  name: Apache Geode REST Administration Queries API
  slug: open-apache-geode-queries-api
- collection_type: open
  name: Apache Geode REST Administration Regions API
  slug: open-apache-geode-regions-api
- collection_type: open
  name: Apache Geode REST API
  slug: open-apache-geode-rest
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apache/geode/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/geode/blob/develop/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/geode/blob/develop/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-geode-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-geode-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-geode-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://geode.apache.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://geode.apache.org/docs/guide/latest/getting_started/book_intro.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/geode
- group: company
  title: ''
  type: Blog
  url: https://geode.apache.org/blog/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-geode-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-geode-vocabulary.yaml
created: '2026-03-16'
description: Apache Geode is an in-memory data management platform that provides real-time, consistent access to data-intensive applications throughout widely distributed cloud architectures. It pools memory, CPU, network resources, and local disk storage across multiple processes, offering a REST API for data access, OQL queries, function execution, and cluster management.
examples:
- key_count: 1
  name: Geode Rest Function List Response Example
  slug: geode-rest-function-list-response-example
- key_count: 1
  name: Geode Rest Function Result Example
  slug: geode-rest-function-result-example
- key_count: 1
  name: Geode Rest Key List Response Example
  slug: geode-rest-key-list-response-example
- key_count: 2
  name: Geode Rest Query Info Example
  slug: geode-rest-query-info-example
- key_count: 1
  name: Geode Rest Query List Response Example
  slug: geode-rest-query-list-response-example
- key_count: 1
  name: Geode Rest Query Result Example
  slug: geode-rest-query-result-example
- key_count: 0
  name: Geode Rest Region Data Example
  slug: geode-rest-region-data-example
- key_count: 4
  name: Geode Rest Region Info Example
  slug: geode-rest-region-info-example
- key_count: 1
  name: Geode Rest Region List Response Example
  slug: geode-rest-region-list-response-example
- key_count: 1
  name: Geode Rest Server List Response Example
  slug: geode-rest-server-list-response-example
features:
- description: Pool memory across distributed nodes for consistent sub-millisecond data access at scale.
  name: In-Memory Data Grid
- description: HTTP REST API for language-agnostic CRUD operations on Geode regions using JSON.
  name: REST Data API
- description: SQL-like Object Query Language for executing complex queries against in-memory data.
  name: OQL Query Language
- description: Register interest in data changes meeting OQL criteria for real-time event notification.
  name: Continuous Queries
- description: Deploy and execute Java functions on the cluster nodes to co-locate compute with data.
  name: Server-Side Functions
- description: Full ACID transaction support for consistent multi-region data operations.
  name: ACID Transactions
- description: Asynchronous and synchronous WAN gateway replication for geo-distributed data consistency.
  name: WAN Replication
- description: Configurable eviction policies (LRU, heap, disk) and TTL-based entry expiration.
  name: Eviction and Expiration
- description: Disk persistence option for data recovery after restart without network re-loading.
  name: Persistence
- description: High-performance C++ and .NET native client libraries for non-JVM applications.
  name: Native Clients
finops:
- name: Apache Geode Finops
  service_category: API
  slug: apache-geode-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-geode.png
integrations:
- description: Geode-Spark connector for using Geode regions as Spark RDD/DataFrame data sources.
  name: Apache Spark
- description: Spring Data integration for repository-based data access and caching annotations.
  name: Spring Data Geode
- description: Kubernetes operator for deploying and managing Geode clusters on Kubernetes.
  name: Kubernetes
- description: Cloud Foundry service broker for provisioning Geode instances as managed services.
  name: Pivotal Cloud Foundry
json_schemas:
- name: FunctionListResponse
  property_count: 1
  slug: geode-rest-function-list-response
- name: FunctionResult
  property_count: 1
  slug: geode-rest-function-result
- name: KeyListResponse
  property_count: 1
  slug: geode-rest-key-list-response
- name: QueryInfo
  property_count: 2
  slug: geode-rest-query-info
- name: QueryListResponse
  property_count: 1
  slug: geode-rest-query-list-response
- name: QueryResult
  property_count: 1
  slug: geode-rest-query-result
- name: RegionData
  property_count: 0
  slug: geode-rest-region-data
- name: RegionInfo
  property_count: 4
  slug: geode-rest-region-info
- name: RegionListResponse
  property_count: 1
  slug: geode-rest-region-list-response
- name: ServerListResponse
  property_count: 1
  slug: geode-rest-server-list-response
json_structures:
- name: Geode Rest Function List Response Structure
  property_count: 1
  slug: geode-rest-function-list-response-structure
- name: Geode Rest Function Result Structure
  property_count: 1
  slug: geode-rest-function-result-structure
- name: Geode Rest Key List Response Structure
  property_count: 1
  slug: geode-rest-key-list-response-structure
- name: Geode Rest Query Info Structure
  property_count: 2
  slug: geode-rest-query-info-structure
- name: Geode Rest Query List Response Structure
  property_count: 1
  slug: geode-rest-query-list-response-structure
- name: Geode Rest Query Result Structure
  property_count: 1
  slug: geode-rest-query-result-structure
- name: Geode Rest Region Data Structure
  property_count: 0
  slug: geode-rest-region-data-structure
- name: Geode Rest Region Info Structure
  property_count: 4
  slug: geode-rest-region-info-structure
- name: Geode Rest Region List Response Structure
  property_count: 1
  slug: geode-rest-region-list-response-structure
- name: Geode Rest Server List Response Structure
  property_count: 1
  slug: geode-rest-server-list-response-structure
jsonld:
- class_count: 11
  name: Apache Geode Rest Context
  property_count: 11
  slug: apache-geode-rest-context
layout: provider
modified: '2026-05-19'
name: Apache Geode
nav: Providers
network: true
overview: 'Apache Geode publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Administration API, Functions API, Queries API, and 1 more. Tagged areas include Apache, Caching, Data Grid, Distributed Systems, and In-Memory.


  The Apache Geode catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Geode''s developer surface includes documentation, getting-started guide, engineering blog, and 10 more developer resources.'
plans:
- name: Apache Geode Plans Pricing
  plan_count: 3
  slug: apache-geode-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Apache Geode Rate Limits
  slug: apache-geode-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache Geode API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-geode-jsonschema-spectral-rules
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Apache Geode API Rules
  rule_count: 14
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 8
  slug: apache-geode-spectral-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 47.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 54.5
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 40.0
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-geode/refs/heads/main/screenshots/apache-geode-2026-06-20T172059.png
security:
- kind: domain-security
  name: Apache Geode Domain Security
  slug: apache-geode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Geode Vulnerability Disclosure
  slug: apache-geode-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-geode
tags:
- Apache
- Caching
- Data Grid
- Distributed Systems
- In-Memory
- Open-Source
use_cases:
- description: Replace Redis or Memcached with Geode for distributed session caching with ACID guarantees.
  name: Session Caching
- description: Perform OQL queries on in-flight event data for real-time analytical processing.
  name: Real-Time Analytics
- description: Low-latency transaction processing with ACID guarantees for financial trading and payments.
  name: Financial Transaction Processing
- description: Share state between microservices with consistent in-memory data across distributed nodes.
  name: Microservices Shared State
- description: Aggregate and query high-velocity IoT telemetry data in memory for real-time responses.
  name: IoT Data Aggregation
---
