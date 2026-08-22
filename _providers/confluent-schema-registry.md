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
    agent_skills: true
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Confluent Schema Registry Agentic Access
  operation_count: 21
  slug: confluent-schema-registry-agentic-access
  summary_line: 21 operations · 9 acting
api_count: 5
apis:
- description: The Compatibility API from Confluent Schema Registry — 3 operation(s) for compatibility.
  name: Confluent Schema Registry Compatibility API
  slug: confluent-schema-registry-compatibility-api
- description: The Mode API from Confluent Schema Registry — 1 operation(s) for mode.
  name: Confluent Schema Registry Mode API
  slug: confluent-schema-registry-mode-api
- description: The Schemas API from Confluent Schema Registry — 3 operation(s) for schemas.
  name: Confluent Schema Registry Schemas API
  slug: confluent-schema-registry-schemas-api
- description: The Server API from Confluent Schema Registry — 1 operation(s) for server.
  name: Confluent Schema Registry Server API
  slug: confluent-schema-registry-server-api
- description: The Subjects API from Confluent Schema Registry — 6 operation(s) for subjects.
  name: Confluent Schema Registry Subjects API
  slug: confluent-schema-registry-subjects-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Confluent Schema Registry Compatibility API
  slug: open-confluent-schema-registry-compatibility-api
- collection_type: open
  name: Confluent Schema Registry Compatibility Mode API
  slug: open-confluent-schema-registry-mode-api
- collection_type: open
  name: Confluent Schema Registry Compatibility Schemas API
  slug: open-confluent-schema-registry-schemas-api
- collection_type: open
  name: Confluent Schema Registry Compatibility Server API
  slug: open-confluent-schema-registry-server-api
- collection_type: open
  name: Confluent Schema Registry Compatibility Subjects API
  slug: open-confluent-schema-registry-subjects-api
- collection_type: open
  name: Confluent Schema Registry API
  slug: open-schema-registry
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/confluent-schema-registry-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/confluent-schema-registry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/confluent-schema-registry-domain-security.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/confluentinc/agent-skills
- group: company
  title: ''
  type: Website
  url: https://www.confluent.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.confluent.io/platform/current/schema-registry/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.confluent.io/platform/current/schema-registry/develop/using.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.confluent.io/platform/current/schema-registry/develop/api.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/confluentinc/schema-registry
- group: commercial
  title: ''
  type: License
  url: https://www.confluent.io/confluent-community-license/
- group: company
  title: ''
  type: Blog
  url: https://www.confluent.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.confluent.io/pricing/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/confluent-schema-registry-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/confluent-schema-registry-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.confluent.io/llms.txt
created: '2026-03-26'
description: Confluent Schema Registry is the open-source serving layer for schema metadata used in Apache Kafka data pipelines. It exposes a RESTful interface for storing and retrieving Avro, JSON Schema, and Protobuf schemas, manages schema evolution through configurable compatibility rules (BACKWARD, FORWARD, FULL, and transitive variants), supports schema references and contexts, and integrates with Kafka producers and consumers via shipped serializers and deserializers. Schema Registry is distributed under the Confluent Community License and is a core component of both Confluent Platform and Confluent Cloud.
finops:
- name: Confluent Schema Registry Finops
  service_category: API
  slug: confluent-schema-registry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/confluent-schema-registry.png
json_schemas:
- name: Confluent Schema Registry Schema
  property_count: 7
  slug: schema-registry
jsonld:
- class_count: 0
  name: Confluent Schema Registry Context
  property_count: 10
  slug: confluent-schema-registry-context
layout: provider
modified: '2026-05-19'
name: Confluent Schema Registry
nav: Providers
network: true
overview: 'Confluent Schema Registry publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Compatibility API, Mode API, Schemas API, and 2 more. Tagged areas include Apache Kafka, Avro, Compatibility, Confluent, and Data Governance.


  The Confluent Schema Registry catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Confluent Schema Registry''s developer surface includes documentation, getting-started guide, API reference, GitHub presence, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Confluent Schema Registry Plans Pricing
  plan_count: 3
  slug: confluent-schema-registry-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Confluent Schema Registry Rate Limits
  slug: confluent-schema-registry-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Confluent Schema Registry API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: confluent-schema-registry-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Confluent Schema Registry API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: confluent-schema-registry-rules
score:
  band: thin
  composite: 35.9
  delta: -6.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 51.6
    developer_ergonomics: 38.1
    discoverability: 72.2
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/confluent-schema-registry/refs/heads/main/screenshots/confluent-schema-registry-2026-06-20T174859.png
security:
- kind: domain-security
  name: Confluent Schema Registry Domain Security
  slug: confluent-schema-registry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Confluent Schema Registry Vulnerability Disclosure
  slug: confluent-schema-registry-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 12
skills:
- name: Bad_Frontmatter
  slug: bad-frontmatter
- name: confluent-cloud-cdc-tableflow
  slug: confluent-cloud-cdc-tableflow
- name: confluent-skill-creator
  slug: confluent-skill-creator
- name: confluent-skill-reviewer
  slug: confluent-skill-reviewer
- name: developing-kafka-python-client
  slug: developing-kafka-python-client
- name: flink-udf
  slug: flink-udf
- name: good-skill
  slug: good-skill
- name: inlined-refs
  slug: inlined-refs
- name: kafka-schema-registry
  slug: kafka-schema-registry
- name: kafka-streams-programming
  slug: kafka-streams-programming
- name: stale-expectations
  slug: stale-expectations
- name: trigger-overlap
  slug: trigger-overlap
slug: confluent-schema-registry
tags:
- Apache Kafka
- Avro
- Compatibility
- Confluent
- Data Governance
- Data Streaming
- JSON Schema
- Open Source
- Protobuf
- REST
- Schema Evolution
- Schema Registry
website: https://www.confluent.io/
---
