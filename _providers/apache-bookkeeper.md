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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Apache Bookkeeper Agentic Access
  operation_count: 19
  slug: apache-bookkeeper-agentic-access
  summary_line: 19 operations · 5 acting
api_count: 6
apis:
- description: The BookKeeper Java client API provides programmatic access for creating, writing, reading, and managing ledgers. It supports both the legacy LedgerHandle API and the newer Ledger API with explicit du
  name: Apache BookKeeper Java Client API
  slug: apache-bookkeeper-java-client
- description: Under-replication detection and bookie recovery operations.
  name: Apache BookKeeper Auto Recovery API
  slug: apache-bookkeeper-auto-recovery-api
- description: Bookie node management and status operations.
  name: Apache BookKeeper Bookies API
  slug: apache-bookkeeper-bookies-api
- description: Server configuration management.
  name: Apache BookKeeper Configuration API
  slug: apache-bookkeeper-configuration-api
- description: Ledger management and inspection operations.
  name: Apache BookKeeper Ledgers API
  slug: apache-bookkeeper-ledgers-api
- description: Health checks and metrics endpoints.
  name: Apache BookKeeper Monitoring API
  slug: apache-bookkeeper-monitoring-api
artifact_total: 62
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache BookKeeper Admin Auto Recovery API
  slug: open-apache-bookkeeper-auto-recovery-api
- collection_type: open
  name: Apache BookKeeper Admin Auto Recovery Bookies API
  slug: open-apache-bookkeeper-bookies-api
- collection_type: open
  name: Apache BookKeeper Admin Auto Recovery Configuration API
  slug: open-apache-bookkeeper-configuration-api
- collection_type: open
  name: Apache BookKeeper Admin Auto Recovery Ledgers API
  slug: open-apache-bookkeeper-ledgers-api
- collection_type: open
  name: Apache BookKeeper Admin Auto Recovery Monitoring API
  slug: open-apache-bookkeeper-monitoring-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/bookkeeper/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/bookkeeper/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/bookkeeper/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-bookkeeper-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-bookkeeper-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-bookkeeper-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/bookkeeper
- group: docs
  title: ''
  type: Documentation
  url: https://bookkeeper.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://bookkeeper.apache.org/docs/getting-started/installation
- group: operate
  title: ''
  type: Support
  url: https://bookkeeper.apache.org/community/mailing-lists
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/apache/bookkeeper/releases
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-bookkeeper-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-bookkeeper-vocabulary.yaml
created: '2026-03-16'
description: Apache BookKeeper is a scalable, fault-tolerant, and low-latency storage service optimized for real-time workloads developed by the Apache Software Foundation. It provides a simple log-oriented storage abstraction called ledgers for reliable, replicated storage of sequential data. BookKeeper is used as the durable log storage layer in Apache Pulsar and other distributed messaging and stream processing systems. It provides a Java client API and an HTTP Admin REST API for cluster management, bookie monitoring, and auto-recovery operations.
examples:
- key_count: 1
  name: Bookkeeper Admin Auditor Info Example
  slug: bookkeeper-admin-auditor-info-example
- key_count: 2
  name: Bookkeeper Admin Bookie Info Example
  slug: bookkeeper-admin-bookie-info-example
- key_count: 4
  name: Bookkeeper Admin Bookie State Example
  slug: bookkeeper-admin-bookie-state-example
- key_count: 8
  name: Bookkeeper Admin Cluster Info Example
  slug: bookkeeper-admin-cluster-info-example
- key_count: 7
  name: Bookkeeper Admin Ledger Metadata Example
  slug: bookkeeper-admin-ledger-metadata-example
features:
- description: Append-only log segments called ledgers provide the foundational storage primitive for reliable sequential data storage.
  name: Ledger Storage
- description: Data is written to a configurable ensemble of bookies with write quorum and ack quorum parameters for fault tolerance.
  name: Ensemble Replication
- description: Built-in under-replication detection and automatic ledger re-replication when bookie nodes fail.
  name: Auto-Recovery
- description: RESTful HTTP Admin API for managing ledgers, bookies, cluster configuration, and triggering recovery operations.
  name: HTTP Admin API
- description: Prometheus-format metrics endpoint for monitoring bookie performance and storage utilization.
  name: Metrics Export
- description: ZooKeeper-based leader election for the auditor role responsible for detecting under-replicated ledgers.
  name: Auditor Election
- description: Configurable garbage collection for reclaiming storage from deleted or expired ledger data.
  name: Garbage Collection
- description: Separate journal and ledger storage paths optimized for sequential write throughput and random read performance.
  name: Journal and Ledger Storage
finops:
- name: Apache Bookkeeper Finops
  service_category: API
  slug: apache-bookkeeper-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-bookkeeper.png
integrations:
- description: BookKeeper serves as the durable log storage layer for Apache Pulsar messaging topics.
  name: Apache Pulsar
- description: ZooKeeper is used for bookie coordination, auditor election, and cluster metadata management.
  name: Apache ZooKeeper
- description: BookKeeper can be used with Hadoop ecosystem tools for reliable log storage alongside HDFS.
  name: Apache Hadoop
- description: BookKeeper exports Prometheus-format metrics for cluster monitoring and alerting.
  name: Prometheus
- description: Grafana dashboards consume BookKeeper Prometheus metrics for operational visibility.
  name: Grafana
json_schemas:
- name: AuditorInfo
  property_count: 1
  slug: bookkeeper-admin-auditor-info
- name: BookieInfo
  property_count: 2
  slug: bookkeeper-admin-bookie-info
- name: BookieList
  property_count: 0
  slug: bookkeeper-admin-bookie-list
- name: BookieState
  property_count: 4
  slug: bookkeeper-admin-bookie-state
- name: ClusterInfo
  property_count: 8
  slug: bookkeeper-admin-cluster-info
- name: GcStatus
  property_count: 1
  slug: bookkeeper-admin-gc-status
- name: LedgerEntries
  property_count: 0
  slug: bookkeeper-admin-ledger-entries
- name: LedgerList
  property_count: 0
  slug: bookkeeper-admin-ledger-list
- name: LedgerMetadata
  property_count: 7
  slug: bookkeeper-admin-ledger-metadata
json_structures:
- name: Bookkeeper Admin Auditor Info Structure
  property_count: 0
  slug: bookkeeper-admin-auditor-info-structure
- name: Bookkeeper Admin Bookie Info Structure
  property_count: 0
  slug: bookkeeper-admin-bookie-info-structure
- name: Bookkeeper Admin Bookie List Structure
  property_count: 0
  slug: bookkeeper-admin-bookie-list-structure
- name: Bookkeeper Admin Bookie State Structure
  property_count: 0
  slug: bookkeeper-admin-bookie-state-structure
- name: Bookkeeper Admin Cluster Info Structure
  property_count: 0
  slug: bookkeeper-admin-cluster-info-structure
- name: Bookkeeper Admin Gc Status Structure
  property_count: 0
  slug: bookkeeper-admin-gc-status-structure
- name: Bookkeeper Admin Ledger Entries Structure
  property_count: 0
  slug: bookkeeper-admin-ledger-entries-structure
- name: Bookkeeper Admin Ledger List Structure
  property_count: 0
  slug: bookkeeper-admin-ledger-list-structure
- name: Bookkeeper Admin Ledger Metadata Structure
  property_count: 0
  slug: bookkeeper-admin-ledger-metadata-structure
jsonld:
- class_count: 9
  name: Apache Bookkeeper Context
  property_count: 23
  slug: apache-bookkeeper-context
layout: provider
modified: '2026-05-19'
name: Apache BookKeeper
nav: Providers
network: true
overview: 'Apache BookKeeper publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Auto Recovery API, Bookies API, Configuration API, and 2 more. Tagged areas include Apache, Distributed Systems, Log Storage, Open-Source, and Storage.


  The Apache BookKeeper catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache BookKeeper''s developer surface includes documentation, getting-started guide, support, changelog, and 12 more developer resources.'
plans:
- name: Apache Bookkeeper Plans Pricing
  plan_count: 3
  slug: apache-bookkeeper-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Apache Bookkeeper Rate Limits
  slug: apache-bookkeeper-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache BookKeeper API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-bookkeeper-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Apache BookKeeper API Rules
  rule_count: 17
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 12
  slug: apache-bookkeeper-spectral-rules
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 20.0
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 65.0
  previous_composite: 32.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-bookkeeper/refs/heads/main/screenshots/apache-bookkeeper-2026-06-20T172044.png
security:
- kind: domain-security
  name: Apache Bookkeeper Domain Security
  slug: apache-bookkeeper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Bookkeeper Vulnerability Disclosure
  slug: apache-bookkeeper-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-bookkeeper
tags:
- Apache
- Distributed Systems
- Log Storage
- Open-Source
- Storage
- Streaming
use_cases:
- description: Serve as the replicated, durable write-ahead log for Apache Pulsar topics and distributed streaming systems.
  name: Durable Log Storage
- description: Store distributed transaction log segments for systems requiring exactly-once semantics and durable commit records.
  name: Distributed Transaction Logs
- description: Persist metadata and configuration data for distributed systems requiring consistent, replicated storage.
  name: Metadata Store
- description: Provide low-latency, high-throughput sequential storage for real-time stream processing pipelines.
  name: Stream Processing Storage
- description: Monitor and manage BookKeeper clusters using the HTTP Admin API for operational visibility and recovery.
  name: Cluster Administration
---
