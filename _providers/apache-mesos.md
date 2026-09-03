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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Apache Mesos Agentic Access
  operation_count: 1
  slug: apache-mesos-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 2
apis:
- description: The Mesos Scheduler HTTP API at /api/v1/scheduler enables framework schedulers to subscribe to resource offers, launch tasks, kill tasks, reconcile status, and manage framework lifecycle over a persis
  name: Apache Mesos Scheduler HTTP API
  slug: mesos-scheduler-http-api
- baseURL: http://localhost:5050
  baseurl_source: spec
  description: The Apache Mesos Operator HTTP API API from Apache Mesos — 1 operation(s) for apache mesos operator http api.
  name: Apache Mesos Apache Mesos Operator HTTP API API
  slug: apache-mesos-apache-mesos-operator-http-api-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Mesos Operator HTTP Apache Mesos Operator HTTP API API
  slug: open-apache-mesos-apache-mesos-operator-http-api-api
- collection_type: open
  name: Apache Mesos Operator HTTP API
  slug: open-apache-mesos
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/mesos/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/mesos/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-mesos-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-mesos-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-mesos-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://mesos.apache.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/mesos
- group: docs
  title: ''
  type: Documentation
  url: https://mesos.apache.org/documentation/latest/
- group: company
  title: ''
  type: Blog
  url: https://mesos.apache.org/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
created: '2026-03-16'
description: Apache Mesos is a retired cluster manager (now in the Apache Attic) that provided efficient resource isolation and sharing across distributed applications or frameworks. It abstracted CPU, memory, storage, and other compute resources from machines, enabling fault-tolerant and elastic distributed systems. Mesos exposed comprehensive HTTP APIs for schedulers, operators, executors, and agents.
features:
- description: Abstracts CPU, memory, storage, and other compute resources from physical machines across the entire cluster.
  name: Resource Abstraction
- description: Framework schedulers receive resource offers from Mesos and decide how to use them, enabling coexistence of diverse workloads.
  name: Two-Level Scheduling
- description: Proven to scale to tens of thousands of nodes with fault-tolerant replicated master using ZooKeeper.
  name: Linear Scalability
- description: Native Docker and AppC container image support for running containerized workloads.
  name: Container Support
- description: Comprehensive HTTP API supporting JSON and Protobuf encoding for schedulers, operators, executors, and agents.
  name: HTTP API
- description: Fault-tolerant master failover via ZooKeeper with automatic leader election and state recovery.
  name: High Availability
- description: Static and dynamic resource reservations for frameworks and roles with quota management.
  name: Resource Reservations
- description: Built-in maintenance window scheduling for graceful draining and reactivation of agent nodes.
  name: Maintenance Scheduling
finops:
- name: Apache Mesos Finops
  service_category: API
  slug: apache-mesos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-mesos.png
integrations:
- description: Run Hadoop MapReduce jobs on Mesos-managed cluster resources.
  name: Apache Hadoop
- description: Apache Spark supports Mesos as a cluster manager for distributed job execution.
  name: Apache Spark
- description: Kafka brokers can be scheduled and managed on Mesos clusters.
  name: Apache Kafka
- description: ZooKeeper provides leader election and state storage for Mesos master high availability.
  name: Apache ZooKeeper
- description: Native Docker container image and runtime support for containerized workload execution.
  name: Docker
- description: Elasticsearch can be deployed and managed as a framework on Mesos clusters.
  name: Elasticsearch
layout: provider
modified: '2026-05-19'
name: Apache Mesos
nav: Providers
network: true
overview: 'Apache Mesos publishes 1 API on the [APIs.io](https://apis.io/) network: Apache Mesos Operator HTTP API API. Tagged areas include Cluster Management, Distributed Systems, Resource Management, Scheduling, and Retired.


  Apache Mesos'' developer surface includes developer portal, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Apache Mesos Plans Pricing
  plan_count: 3
  slug: apache-mesos-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Apache Mesos Rate Limits
  slug: apache-mesos-rate-limits
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  open_source:
    applies: true
    score: 40.0
  previous_composite: 28.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-mesos/refs/heads/main/screenshots/apache-mesos-2026-06-20T172121.png
security:
- kind: domain-security
  name: Apache Mesos Domain Security
  slug: apache-mesos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Mesos Vulnerability Disclosure
  slug: apache-mesos-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-mesos
tags:
- Cluster Management
- Distributed Systems
- Resource Management
- Scheduling
- Retired
use_cases:
- description: Run multiple distributed frameworks including Hadoop, Spark, and Kafka on shared cluster resources.
  name: Distributed Systems Orchestration
- description: Schedule and manage containerized workloads across a datacenter with resource isolation.
  name: Container Orchestration
- description: Run Apache Spark, Hadoop MapReduce, and other big data frameworks on Mesos-managed resources.
  name: Big Data Processing
- description: Host microservices workloads with Marathon framework providing long-running service scheduling on Mesos.
  name: Microservices Platform
website: https://mesos.apache.org/
---
