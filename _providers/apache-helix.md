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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Apache Helix Agentic Access
  operation_count: 10
  slug: apache-helix-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 5
apis:
- description: Java API for implementing Helix participant, spectator, and controller roles, with APIs for resource management, task execution, and state machine definitions.
  name: Apache Helix Java API
  slug: apache-helix-java-api
- description: Cluster management operations
  name: Apache Helix Clusters API
  slug: apache-helix-clusters-api
- description: Instance management operations
  name: Apache Helix Instances API
  slug: apache-helix-instances-api
- description: Resource management operations
  name: Apache Helix Resources API
  slug: apache-helix-resources-api
- description: Partition state operations
  name: Apache Helix State API
  slug: apache-helix-state-api
artifact_total: 55
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Helix REST Clusters API
  slug: open-apache-helix-clusters-api
- collection_type: open
  name: Apache Helix REST Clusters Instances API
  slug: open-apache-helix-instances-api
- collection_type: open
  name: Apache Helix REST Clusters Resources API
  slug: open-apache-helix-resources-api
- collection_type: open
  name: Apache Helix REST API
  slug: open-apache-helix-rest
- collection_type: open
  name: Apache Helix REST Clusters State API
  slug: open-apache-helix-state-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/helix/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apache/helix/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/helix/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/helix/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-helix-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-helix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-helix-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://helix.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://helix.apache.org/0.9.9-docs/Quickstart.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/helix
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-helix-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-helix-vocabulary.yaml
created: '2026-03-16'
description: Apache Helix is a generic cluster management framework for partitioned and replicated distributed resources. It automates partition management, replication, fault tolerance, and cluster expansion for distributed systems, providing a REST API for cluster administration and a Java API for participant, spectator, and controller roles.
examples:
- key_count: 5
  name: Helix Rest Cluster Example
  slug: helix-rest-cluster-example
- key_count: 2
  name: Helix Rest Externalview Example
  slug: helix-rest-externalview-example
- key_count: 3
  name: Helix Rest Idealstate Example
  slug: helix-rest-idealstate-example
- key_count: 5
  name: Helix Rest Instance Example
  slug: helix-rest-instance-example
- key_count: 2
  name: Helix Rest Partition Example
  slug: helix-rest-partition-example
- key_count: 5
  name: Helix Rest Resource Example
  slug: helix-rest-resource-example
features:
- description: Automatically assign and balance partitions across cluster nodes using pluggable rebalancer algorithms.
  name: Automatic Partition Management
- description: Define custom resource state machines (e.g., Master-Slave, Leader-Standby) for any distributed service.
  name: State Machine Framework
- description: Detect node failures and automatically reassign partitions to maintain replication targets.
  name: Fault Tolerance
- description: HTTP REST API for cluster administration, resource management, and state inspection.
  name: REST API
- description: Distributed task scheduling framework for batch jobs and recurring workflows with failure handling.
  name: Task Framework
- description: Uses Apache ZooKeeper as the distributed coordination backend for cluster state storage.
  name: ZooKeeper Integration
- description: Read-only API for external services to observe resource state and routing decisions.
  name: Spectator API
- description: Rack and zone-aware partition placement for fault-domain isolation in cloud environments.
  name: Cloud-Aware Rebalancing
finops:
- name: Apache Helix Finops
  service_category: API
  slug: apache-helix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-helix.png
integrations:
- description: ZooKeeper is the required coordination backend for Helix cluster state management.
  name: Apache ZooKeeper
- description: Helix is used internally by some Kafka ecosystem projects for partition management.
  name: Apache Kafka
- description: Apache Pinot uses Helix for real-time OLAP cluster partition and segment management.
  name: LinkedIn Pinot
- description: Venice feature store uses Helix for managing data store partition assignments.
  name: LinkedIn Venice
json_schemas:
- name: Cluster
  property_count: 5
  slug: helix-rest-cluster
- name: ExternalView
  property_count: 2
  slug: helix-rest-externalview
- name: IdealState
  property_count: 3
  slug: helix-rest-idealstate
- name: Instance
  property_count: 5
  slug: helix-rest-instance
- name: Partition
  property_count: 2
  slug: helix-rest-partition
- name: Resource
  property_count: 5
  slug: helix-rest-resource
json_structures:
- name: Helix Rest Cluster Structure
  property_count: 5
  slug: helix-rest-cluster-structure
- name: Helix Rest Externalview Structure
  property_count: 2
  slug: helix-rest-externalview-structure
- name: Helix Rest Idealstate Structure
  property_count: 3
  slug: helix-rest-idealstate-structure
- name: Helix Rest Instance Structure
  property_count: 5
  slug: helix-rest-instance-structure
- name: Helix Rest Partition Structure
  property_count: 2
  slug: helix-rest-partition-structure
- name: Helix Rest Resource Structure
  property_count: 5
  slug: helix-rest-resource-structure
jsonld:
- class_count: 16
  name: Apache Helix Rest Context
  property_count: 0
  slug: apache-helix-rest-context
layout: provider
modified: '2026-05-19'
name: Apache Helix
nav: Providers
network: true
overview: 'Apache Helix publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Clusters API, Instances API, Resources API, and 1 more. Tagged areas include Apache, Cluster Management, Distributed Systems, Open Source, and Partitioning.


  The Apache Helix catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Helix''s developer surface includes documentation, getting-started guide, and 12 more developer resources.'
plans:
- name: Apache Helix Plans Pricing
  plan_count: 3
  slug: apache-helix-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Apache Helix Rate Limits
  slug: apache-helix-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache Helix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-helix-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Apache Helix API Rules
  rule_count: 13
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 9
  slug: apache-helix-spectral-rules
score:
  band: thin
  composite: 35.7
  delta: -6.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 55.9
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 36.8
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-helix/refs/heads/main/screenshots/apache-helix-2026-06-20T172103.png
security:
- kind: domain-security
  name: Apache Helix Domain Security
  slug: apache-helix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Helix Vulnerability Disclosure
  slug: apache-helix-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-helix
tags:
- Apache
- Cluster Management
- Distributed Systems
- Open Source
- Partitioning
- Replication
use_cases:
- description: Manage shard assignment and replication for distributed databases like DistributedLog or Espresso.
  name: Distributed Database Cluster Management
- description: Automatically balance and assign search index shards across a cluster of query servers.
  name: Search Index Partition Management
- description: Schedule and execute distributed batch tasks with automatic retry and failure recovery.
  name: Distributed Task Scheduling
- description: Use Helix spectator API to implement client-side load balancing based on partition state.
  name: Microservices Load Balancing
- description: Perform rolling upgrades and partition migrations without service downtime.
  name: Stateful Service Migration
---
