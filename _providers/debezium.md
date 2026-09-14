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
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Debezium Agentic Access
  operation_count: 19
  slug: debezium-agentic-access
  summary_line: 19 operations · 10 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: http://localhost:8083
  baseurl_source: declared
  description: The Cluster API from Debezium — 1 operation(s) for cluster.
  name: Debezium Cluster API
  slug: debezium-cluster-api
- baseURL: http://localhost:8083
  baseurl_source: declared
  description: The Connectors API from Debezium — 7 operation(s) for connectors.
  name: Debezium Connectors API
  slug: debezium-connectors-api
- baseURL: http://localhost:8083
  baseurl_source: declared
  description: The Offsets API from Debezium — 1 operation(s) for offsets.
  name: Debezium Offsets API
  slug: debezium-offsets-api
- baseURL: http://localhost:8083
  baseurl_source: declared
  description: The Plugins API from Debezium — 2 operation(s) for plugins.
  name: Debezium Plugins API
  slug: debezium-plugins-api
- baseURL: http://localhost:8083
  baseurl_source: declared
  description: The Tasks API from Debezium — 3 operation(s) for tasks.
  name: Debezium Tasks API
  slug: debezium-tasks-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Debezium Kafka Connect REST Cluster API
  slug: open-debezium-cluster-api
- collection_type: open
  name: Debezium Kafka Connect REST API
  slug: open-debezium-connect
- collection_type: open
  name: Debezium Kafka Connect REST Cluster Connectors API
  slug: open-debezium-connectors-api
- collection_type: open
  name: Debezium Kafka Connect REST Cluster Offsets API
  slug: open-debezium-offsets-api
- collection_type: open
  name: Debezium Kafka Connect REST Cluster Plugins API
  slug: open-debezium-plugins-api
- collection_type: open
  name: Debezium Kafka Connect REST Cluster Tasks API
  slug: open-debezium-tasks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/debezium-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/debezium-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/debezium
- group: company
  title: ''
  type: Website
  url: https://debezium.io/
- group: docs
  title: ''
  type: Documentation
  url: https://debezium.io/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://debezium.io/documentation/reference/stable/tutorial.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/debezium/debezium
- group: company
  title: ''
  type: Blog
  url: https://debezium.io/blog/
- group: operate
  title: ''
  type: Community
  url: https://debezium.io/community/
- group: commercial
  title: ''
  type: License
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: design
  title: ''
  type: JSONLD
  url: json-ld/debezium-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/debezium-vocabulary.yml
created: '2026-03-26'
description: Debezium is an open source distributed platform for change data capture (CDC) that converts changes in existing databases into event streams, enabling applications to detect and respond to row-level changes in databases in real time.
finops:
- name: Debezium Finops
  service_category: API
  slug: debezium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/debezium.png
json_schemas:
- name: Debezium Change Event
  property_count: 2
  slug: debezium-change-event
jsonld:
- class_count: 4
  name: Debezium Context
  property_count: 9
  slug: debezium-context
layout: provider
modified: '2026-05-19'
name: Debezium
nav: Providers
network: true
overview: 'Debezium publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Cluster API, Connectors API, Offsets API, and 2 more. Tagged areas include Apache Kafka, Change Data Capture, Databases, Event Streaming, and Open-Source.


  The Debezium catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Debezium''s developer surface includes documentation, getting-started guide, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Debezium Plans Pricing
  plan_count: 3
  slug: debezium-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Debezium Rate Limits
  slug: debezium-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Debezium API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: debezium-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Debezium API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: debezium-kafka-connect-api-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/debezium/refs/heads/main/screenshots/debezium-2026-06-20T175745.png
security:
- kind: domain-security
  name: Debezium Domain Security
  slug: debezium-domain-security
  summary_line: TLSv1.3
slug: debezium
tags:
- Apache Kafka
- Change Data Capture
- Databases
- Event Streaming
- Open-Source
website: https://debezium.io/
---
