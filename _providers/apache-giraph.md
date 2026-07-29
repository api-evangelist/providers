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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Apache Giraph Agentic Access
  operation_count: 3
  slug: apache-giraph-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: Java API based on the Bulk Synchronous Parallel (BSP) model for implementing graph algorithms, with Vertex, Edge, and Master compute APIs for distributed graph processing on Hadoop.
  name: Apache Giraph Java API
  slug: apache-giraph-java-api
- description: The Cluster API from Apache Giraph — 1 operation(s) for cluster.
  name: Apache Giraph Cluster API
  slug: apache-giraph-cluster-api
- description: The Job Management API from Apache Giraph — 2 operation(s) for job management.
  name: Apache Giraph Job Management API
  slug: apache-giraph-job-management-api
artifact_total: 43
collections:
- collection_type: open
  name: Apache Giraph Job Monitoring API
  slug: open-apache-giraph-job
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-giraph-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-giraph-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-giraph-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://giraph.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://giraph.apache.org/quick_start.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/giraph
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-giraph-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-giraph-vocabulary.yaml
created: '2026-03-16'
description: Apache Giraph is an iterative graph processing system built for high scalability on Apache Hadoop. It is modeled after Google's Pregel and provides a simple yet flexible Java API for graph algorithms at massive scale using the Bulk Synchronous Parallel (BSP) model. Note - Apache Giraph has been retired as of 2024.
examples:
- key_count: 12
  name: Giraph Job Application Info Example
  slug: giraph-job-application-info-example
- key_count: 1
  name: Giraph Job Application Response Example
  slug: giraph-job-application-response-example
- key_count: 1
  name: Giraph Job Applications Response Example
  slug: giraph-job-applications-response-example
- key_count: 1
  name: Giraph Job Cluster Metrics Response Example
  slug: giraph-job-cluster-metrics-response-example
features:
- description: Google Pregel-inspired BSP computation model where vertices communicate through supersteps.
  name: Bulk Synchronous Parallel (BSP) Model
- description: Write graph algorithms by defining per-vertex compute functions that exchange messages with neighbors.
  name: Vertex-Centric Programming
- description: Global coordination API for aggregating results and controlling algorithm termination across supersteps.
  name: Master Compute API
- description: Sharded aggregators for collecting global statistics across all vertices during computation.
  name: Aggregators
- description: Flexible input formats for loading graphs from HDFS, Hive, Gora, and Rexster sources.
  name: Edge-Oriented Input
- description: Spill graph data to disk for processing graphs larger than available memory.
  name: Out-of-Core Computation
- description: Runs as a MapReduce job on Apache Hadoop YARN for resource management and fault tolerance.
  name: Hadoop Integration
- description: Checkpoint-based recovery for fault tolerance across superstep boundaries.
  name: Fault Tolerance
finops:
- name: Apache Giraph Finops
  service_category: API
  slug: apache-giraph-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-giraph.png
integrations:
- description: Runs on Hadoop YARN as a MapReduce application for cluster resource management.
  name: Apache Hadoop
- description: Hive I/O module for loading graph data from Hive tables.
  name: Apache Hive
- description: Gora I/O module for loading graph data from various NoSQL data stores.
  name: Apache Gora
- description: Rexster graph server I/O module for loading data from TinkerPop graph databases.
  name: Rexster
- description: HBase integration for storing and loading vertex and edge data.
  name: Apache HBase
json_schemas:
- name: ApplicationInfo
  property_count: 12
  slug: giraph-job-application-info
- name: ApplicationResponse
  property_count: 1
  slug: giraph-job-application-response
- name: ApplicationsResponse
  property_count: 1
  slug: giraph-job-applications-response
- name: ClusterMetricsResponse
  property_count: 1
  slug: giraph-job-cluster-metrics-response
json_structures:
- name: Giraph Job Application Info Structure
  property_count: 12
  slug: giraph-job-application-info-structure
- name: Giraph Job Application Response Structure
  property_count: 1
  slug: giraph-job-application-response-structure
- name: Giraph Job Applications Response Structure
  property_count: 1
  slug: giraph-job-applications-response-structure
- name: Giraph Job Cluster Metrics Response Structure
  property_count: 1
  slug: giraph-job-cluster-metrics-response-structure
jsonld:
- class_count: 5
  name: Apache Giraph Job Context
  property_count: 14
  slug: apache-giraph-job-context
layout: provider
modified: '2026-05-19'
name: Apache Giraph
nav: Providers
network: true
overview: 'Apache Giraph publishes 2 APIs on the [APIs.io](https://apis.io/) network: Cluster API and Job Management API. Tagged areas include Apache, Big Data, BSP, Graph Processing, and Hadoop.


  The Apache Giraph catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Giraph''s developer surface includes documentation, getting-started guide, and 7 more developer resources.'
plans:
- name: Apache Giraph Plans Pricing
  plan_count: 3
  slug: apache-giraph-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 5
  name: Apache Giraph Rate Limits
  slug: apache-giraph-rate-limits
rules:
- name: Apache Giraph API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-giraph-jsonschema-spectral-rules
- name: Apache Giraph API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 6
  slug: apache-giraph-spectral-rules
score:
  band: developing
  composite: 46.6
  delta: -5.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.0
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-giraph/refs/heads/main/screenshots/apache-giraph-2026-06-20T172100.png
security:
- kind: domain-security
  name: Apache Giraph Domain Security
  slug: apache-giraph-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Giraph Vulnerability Disclosure
  slug: apache-giraph-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-giraph
tags:
- Apache
- Big Data
- BSP
- Graph Processing
- Hadoop
- Open Source
- Retired
use_cases:
- description: Analyze social network connections, communities, and influence at billions-of-vertices scale (as used at Facebook).
  name: Social Graph Analysis
- description: Compute web page or entity rankings using iterative link analysis algorithms.
  name: PageRank Computation
- description: Find shortest paths between vertices for network routing and recommendation problems.
  name: Shortest Path Computation
- description: Identify clusters and connected components in large graphs for community detection.
  name: Connected Components
- description: Generate graph-structural features for machine learning models at scale.
  name: Graph Machine Learning Features
---
