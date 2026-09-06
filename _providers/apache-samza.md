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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Apache Samza Agentic Access
  operation_count: 6
  slug: apache-samza-agentic-access
  summary_line: 6 operations · 2 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://samza.example.com/v1
  baseurl_source: spec
  description: The Checkpoints API from Apache Samza — 1 operation(s) for checkpoints.
  name: Apache Samza Checkpoints API
  slug: apache-samza-checkpoints-api
- baseURL: https://samza.example.com/v1
  baseurl_source: spec
  description: The Jobs API from Apache Samza — 4 operation(s) for jobs.
  name: Apache Samza Jobs API
  slug: apache-samza-jobs-api
- baseURL: https://samza.example.com/v1
  baseurl_source: spec
  description: The Tasks API from Apache Samza — 1 operation(s) for tasks.
  name: Apache Samza Tasks API
  slug: apache-samza-tasks-api
artifact_total: 54
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Samza REST Checkpoints API
  slug: open-apache-samza-checkpoints-api
- collection_type: open
  name: Apache Samza REST Checkpoints Jobs API
  slug: open-apache-samza-jobs-api
- collection_type: open
  name: Apache Samza REST Checkpoints Tasks API
  slug: open-apache-samza-tasks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-samza-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-samza-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-samza-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/samza
- group: docs
  title: ''
  type: Documentation
  url: https://samza.apache.org/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-samza-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-samza-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-samza-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://samza.apache.org/blog/
created: '2026-03-16'
description: Apache Samza is a distributed stream processing framework that provides a simple API for building stateful stream processing applications. It integrates with Apache Kafka for messaging and supports both stream and batch processing.
examples:
- key_count: 3
  name: Apache Samza Checkpoint Example
  slug: apache-samza-checkpoint-example
- key_count: 1
  name: Apache Samza Checkpoint List Example
  slug: apache-samza-checkpoint-list-example
- key_count: 5
  name: Apache Samza Job Example
  slug: apache-samza-job-example
- key_count: 1
  name: Apache Samza Job List Example
  slug: apache-samza-job-list-example
- key_count: 4
  name: Apache Samza Job Status Example
  slug: apache-samza-job-status-example
- key_count: 3
  name: Apache Samza Partition Example
  slug: apache-samza-partition-example
- key_count: 4
  name: Apache Samza Task Example
  slug: apache-samza-task-example
- key_count: 1
  name: Apache Samza Task List Example
  slug: apache-samza-task-list-example
features:
- description: Native Apache Kafka consumer/producer for stream processing
  name: Kafka Integration
- description: Runs on Apache YARN for resource management and fault tolerance
  name: YARN Execution
- description: Local state stores with RocksDB for low-latency stateful computations
  name: Stateful Processing
- description: Transactional state stores for exactly-once semantics
  name: Exactly-Once Processing
- description: Run on YARN, Kubernetes, or standalone
  name: Flexible Deployment
- description: Fluent API and SQL support for stream transformations
  name: High Level API
finops:
- name: Apache Samza Finops
  service_category: API
  slug: apache-samza-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-samza.png
integrations:
- description: Primary messaging system for Samza input and output streams
  name: Apache Kafka
- description: Resource management and job scheduling on Hadoop
  name: Apache YARN
- description: HDFS integration for checkpoint storage
  name: Apache Hadoop
- description: Embedded state store for local stateful processing
  name: RocksDB
json_schemas:
- name: CheckpointList
  property_count: 1
  slug: apache-samza-checkpoint-list
- name: Checkpoint
  property_count: 3
  slug: apache-samza-checkpoint
- name: JobList
  property_count: 1
  slug: apache-samza-job-list
- name: Job
  property_count: 5
  slug: apache-samza-job
- name: JobStatus
  property_count: 4
  slug: apache-samza-job-status
- name: Partition
  property_count: 3
  slug: apache-samza-partition
- name: TaskList
  property_count: 1
  slug: apache-samza-task-list
- name: Task
  property_count: 4
  slug: apache-samza-task
json_structures:
- name: Apache Samza Checkpoint List Structure
  property_count: 1
  slug: apache-samza-checkpoint-list-structure
- name: Apache Samza Checkpoint Structure
  property_count: 3
  slug: apache-samza-checkpoint-structure
- name: Apache Samza Job List Structure
  property_count: 1
  slug: apache-samza-job-list-structure
- name: Apache Samza Job Status Structure
  property_count: 4
  slug: apache-samza-job-status-structure
- name: Apache Samza Job Structure
  property_count: 5
  slug: apache-samza-job-structure
- name: Apache Samza Partition Structure
  property_count: 3
  slug: apache-samza-partition-structure
- name: Apache Samza Task List Structure
  property_count: 1
  slug: apache-samza-task-list-structure
- name: Apache Samza Task Structure
  property_count: 4
  slug: apache-samza-task-structure
jsonld:
- class_count: 8
  name: Apache Samza Context
  property_count: 17
  slug: apache-samza-context
layout: provider
modified: '2026-05-19'
name: Apache Samza
nav: Providers
network: true
overview: 'Apache Samza publishes 3 APIs on the [APIs.io](https://apis.io/) network: Checkpoints API, Jobs API, and Tasks API. Tagged areas include Big Data, Hadoop, Kafka, Stream Processing, and Streaming.


  The Apache Samza catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Samza''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Apache Samza Plans Pricing
  plan_count: 3
  slug: apache-samza-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Apache Samza Rate Limits
  slug: apache-samza-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache Samza API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-samza-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Apache Samza API Rules
  rule_count: 13
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 7
  slug: apache-samza-spectral-rules
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 52.4
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 29.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-samza/refs/heads/main/screenshots/apache-samza-2026-06-20T172138.png
security:
- kind: domain-security
  name: Apache Samza Domain Security
  slug: apache-samza-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Samza Vulnerability Disclosure
  slug: apache-samza-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-samza
tags:
- Big Data
- Hadoop
- Kafka
- Stream Processing
- Streaming
- Apache
- Open-Source
use_cases:
- description: Real-time processing of Kafka event streams
  name: Event Stream Processing
- description: Windowed aggregations over streaming data
  name: Stateful Aggregations
- description: Join multiple Kafka streams for enrichment
  name: Stream Joins
- description: Process CDC events from databases in real time
  name: Change Data Capture
---
