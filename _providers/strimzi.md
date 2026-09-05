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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Strimzi Agentic Access
  operation_count: 14
  slug: strimzi-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 1
apis:
- description: The Strimzi Operator API is expressed through Kubernetes Custom Resource Definitions (CRDs). Operators are controlled by creating and modifying Kafka, KafkaTopic, KafkaUser, KafkaConnect, KafkaMirrorM
  name: Strimzi Operator API
  slug: strimzi-operator-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Endpoints for managing consumer groups and consuming messages from Kafka topics via HTTP long-polling.
  name: Strimzi Consumer API
  slug: strimzi-consumer-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Endpoints for producing (sending) messages to Kafka topics via HTTP. Supports JSON and binary message formats.
  name: Strimzi Producer API
  slug: strimzi-producer-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Endpoints for seeking consumer positions within topic partitions.
  name: Strimzi Seek API
  slug: strimzi-seek-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Endpoints for querying Kafka topic metadata including partition counts, offsets, and configuration.
  name: Strimzi Topics API
  slug: strimzi-topics-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Strimzi Kafka Bridge REST Consumer API
  slug: open-strimzi-consumer-api
- collection_type: open
  name: Strimzi Kafka Bridge REST API
  slug: open-strimzi-kafka-bridge
- collection_type: open
  name: Strimzi Kafka Bridge REST Consumer Producer API
  slug: open-strimzi-producer-api
- collection_type: open
  name: Strimzi Kafka Bridge REST Consumer Seek API
  slug: open-strimzi-seek-api
- collection_type: open
  name: Strimzi Kafka Bridge REST Consumer Topics API
  slug: open-strimzi-topics-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/strimzi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/strimzi-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/strimzi
- group: company
  title: ''
  type: Website
  url: https://strimzi.io
- group: docs
  title: ''
  type: Documentation
  url: https://strimzi.io/docs/operators/latest/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/strimzi/strimzi-kafka-operator
- group: company
  title: ''
  type: Blog
  url: https://strimzi.io/blog/
- group: other
  title: ''
  type: Helm Chart
  url: https://artifacthub.io/packages/helm/strimzi/strimzi-kafka-operator
- group: operate
  title: ''
  type: Slack
  url: https://slack.cncf.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/strimzi/strimzi-kafka-operator/releases
- group: other
  title: ''
  type: CNCF
  url: https://www.cncf.io/projects/strimzi/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/strimzi/refs/heads/main/openapi/strimzi-kafka-bridge-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/strimzi/refs/heads/main/json-schema/strimzi-kafka-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/strimzi/refs/heads/main/json-ld/strimzi-context.jsonld
crds:
- name: kafka crd
  url: https://raw.githubusercontent.com/api-evangelist/strimzi/refs/heads/main/crd/kafka-crd.yml
- name: kafkatopic crd
  url: https://raw.githubusercontent.com/api-evangelist/strimzi/refs/heads/main/crd/kafkatopic-crd.yml
- name: kafkauser crd
  url: https://raw.githubusercontent.com/api-evangelist/strimzi/refs/heads/main/crd/kafkauser-crd.yml
created: '2025-01-01'
description: Strimzi is a CNCF project providing a Kubernetes-native operator for running Apache Kafka on Kubernetes and OpenShift. It simplifies the deployment, management, scaling, and configuration of Kafka clusters using Kubernetes Custom Resource Definitions (CRDs). Strimzi manages the full Kafka ecosystem including brokers, ZooKeeper/KRaft, Kafka Connect, Kafka MirrorMaker 2, Kafka Bridge, and Schema Registry. The operator pattern lets teams declare desired Kafka topology via YAML manifests managed by Kubernetes.
examples:
- key_count: 3
  name: Strimzi Bridge Produce Example
  slug: strimzi-bridge-produce-example
- key_count: 3
  name: Strimzi Kafka Cluster Example
  slug: strimzi-kafka-cluster-example
finops:
- name: Strimzi Finops
  service_category: API
  slug: strimzi-finops
image: https://strimzi.io/images/logo/strimzi-logo.png
json_schemas:
- name: Strimzi Kafka Custom Resource
  property_count: 4
  slug: strimzi-kafka
json_structures:
- name: Strimzi Kafka Structure
  property_count: 0
  slug: strimzi-kafka-structure
jsonld:
- class_count: 0
  name: Strimzi Context
  property_count: 4
  slug: strimzi-context
layout: provider
modified: '2026-05-19'
name: Strimzi
nav: Providers
network: true
overview: 'Strimzi publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Consumer API, Producer API, Seek API, and 1 more. Tagged areas include Kafka, Kubernetes, Messaging, Operator, and Streaming.


  The Strimzi catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Strimzi''s developer surface includes documentation, GitHub presence, engineering blog, changelog, and 10 more developer resources.'
plans:
- name: Strimzi Plans Pricing
  plan_count: 3
  slug: strimzi-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Strimzi Rate Limits
  slug: strimzi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Strimzi API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: strimzi-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Strimzi API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 3
    warn: 4
  slug: strimzi-rules
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 56.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 54.8
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 28.9
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/strimzi/refs/heads/main/screenshots/strimzi-2026-06-20T194621.png
security:
- kind: domain-security
  name: Strimzi Domain Security
  slug: strimzi-domain-security
  summary_line: TLSv1.3 · HSTS
slug: strimzi
tags:
- Kafka
- Kubernetes
- Messaging
- Operator
- Streaming
website: https://strimzi.io
---
