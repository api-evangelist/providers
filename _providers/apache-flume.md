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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Apache Flume Agentic Access
  operation_count: 1
  slug: apache-flume-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- description: Java API for building custom Flume sources, channels, sinks, and interceptors. Provides interfaces for developing pluggable data ingestion components.
  name: Apache Flume Java API
  slug: apache-flume-java-api
- description: The Monitoring API from Apache Flume — 1 operation(s) for monitoring.
  name: Apache Flume Monitoring API
  slug: apache-flume-monitoring-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Flume Monitoring API
  slug: open-apache-flume-monitoring-api
- collection_type: open
  name: Apache Flume Monitoring API
  slug: open-apache-flume-monitoring
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/flume/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/logging-flume/blob/trunk/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/flume/blob/trunk/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-flume-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-flume-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-flume-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://flume.apache.org/documentation.html
- group: start
  title: ''
  type: GettingStarted
  url: https://flume.apache.org/FlumeUserGuide.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/flume
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-flume-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-flume-vocabulary.yaml
created: '2026-03-16'
description: Apache Flume is a distributed, reliable, and available service for efficiently collecting, aggregating, and moving large amounts of log and event data. It provides a simple and flexible architecture based on streaming data flows with pluggable sources, channels, and sinks, plus a REST monitoring API for agent metrics.
examples:
- key_count: 0
  name: Flume Monitoring Agent Metrics Example
  slug: flume-monitoring-agent-metrics-example
- key_count: 18
  name: Flume Monitoring Component Metrics Example
  slug: flume-monitoring-component-metrics-example
features:
- description: Extensible source architecture supporting Avro, Thrift, Exec, Taildir, Kafka, HTTP, Syslog, and custom sources.
  name: Pluggable Sources
- description: Multiple channel implementations including memory, file-backed, and Kafka-backed channels for different durability requirements.
  name: Durable Channels
- description: Write events to HDFS, HBase, Solr, Elasticsearch, Kafka, and custom sink destinations.
  name: Multi-Destination Sinks
- description: Aggregate events from multiple agent sources into a single destination for centralized log collection.
  name: Fan-In Consolidation
- description: Route events from a single source to multiple channel/sink combinations for parallel processing.
  name: Fan-Out Distribution
- description: Event transformation interceptors for filtering, enrichment, and routing based on event content.
  name: Interceptors
- description: TLS encryption support across Avro, Thrift, Kafka, HTTP, and Syslog components.
  name: SSL/TLS Security
- description: HTTP monitoring endpoint exposing source, channel, and sink metrics for agent health monitoring.
  name: Monitoring REST API
- description: Chain multiple Flume agents via Avro/Thrift RPC for tiered log aggregation architectures.
  name: Multi-Hop Flows
finops:
- name: Apache Flume Finops
  service_category: API
  slug: apache-flume-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-flume.png
integrations:
- description: Kafka source and channel for consuming events, and Kafka sink for writing events to topics.
  name: Apache Kafka
- description: Primary sink for writing log data to Hadoop Distributed File System for batch analytics.
  name: Apache HDFS
- description: HBase sink for writing events directly to HBase tables for random-access analytics.
  name: Apache HBase
- description: Solr sink for indexing log events for full-text search capabilities.
  name: Apache Solr
- description: Elasticsearch sink for indexing and searching aggregated log data.
  name: Elasticsearch
json_schemas:
- name: AgentMetrics
  property_count: 0
  slug: flume-monitoring-agent-metrics
- name: ComponentMetrics
  property_count: 18
  slug: flume-monitoring-component-metrics
json_structures:
- name: Flume Monitoring Agent Metrics Structure
  property_count: 0
  slug: flume-monitoring-agent-metrics-structure
- name: Flume Monitoring Component Metrics Structure
  property_count: 18
  slug: flume-monitoring-component-metrics-structure
jsonld:
- class_count: 2
  name: Apache Flume Monitoring Context
  property_count: 18
  slug: apache-flume-monitoring-context
layout: provider
modified: '2026-05-19'
name: Apache Flume
nav: Providers
network: true
overview: 'Apache Flume publishes 1 API on the [APIs.io](https://apis.io/) network: Monitoring API. Tagged areas include Apache, Data Collection, ETL, Log Aggregation, and Open-Source.


  The Apache Flume catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Flume''s developer surface includes documentation, getting-started guide, and 11 more developer resources.'
plans:
- name: Apache Flume Plans Pricing
  plan_count: 3
  slug: apache-flume-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Apache Flume Rate Limits
  slug: apache-flume-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache Flume API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: apache-flume-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Apache Flume API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 4
  slug: apache-flume-spectral-rules
score:
  band: thin
  composite: 30.2
  delta: 1.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 55.1
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 28.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-flume/refs/heads/main/screenshots/apache-flume-2026-06-20T172058.png
security:
- kind: domain-security
  name: Apache Flume Domain Security
  slug: apache-flume-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Flume Vulnerability Disclosure
  slug: apache-flume-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-flume
tags:
- Apache
- Data Collection
- ETL
- Log Aggregation
- Open-Source
- Streaming
use_cases:
- description: Collect application logs from hundreds of servers and aggregate them into HDFS, Kafka, or Elasticsearch.
  name: Centralized Log Aggregation
- description: Tail application log files in real time using Taildir source for immediate event processing.
  name: Real-Time Log Tailing
- description: Ingest RFC-3164 and RFC-5424 syslog events from network devices into centralized storage.
  name: Syslog Ingestion
- description: Bridge Kafka topics to HDFS or other storage for batch analytics on streaming event data.
  name: Kafka Event Ingestion
- description: Build tiered data collection with edge collectors forwarding to aggregation agents and final destinations.
  name: Multi-Tier Architectures
---
