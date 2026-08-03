---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-03'
api_count: 4
apis:
- description: VTGate is the stateless proxy that routes queries to the appropriate VTTablet instances. It exposes a MySQL-compatible interface and a gRPC API that clients use to interact with the Vitess cluster, ha
  name: Vitess VTGate API
  slug: vtgate-api
- description: VTAdmin is the administrative web application and REST API for managing Vitess clusters. It provides endpoints for inspecting cluster topology, tablets, keyspaces, shards, schemas, and VReplication wo
  name: Vitess VTAdmin API
  slug: vtadmin-api
- description: VTCtld is the Vitess topology management daemon that exposes a gRPC and HTTP API for administrative operations on the cluster topology including creating and managing keyspaces, shards, tablets, and e
  name: Vitess VTCtld API
  slug: vtctld-api
- description: VReplication is the Vitess framework for replicating and transforming data streams within and across Vitess clusters. It powers features such as MoveTables, Reshard, Materialize, and CreateLookupVinde
  name: Vitess VReplication API
  slug: vreplication-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vitess-domain-security.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/vitess-topology-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/vitess-context.jsonld
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/vitess-tablet-structure.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/vitess-vtadmin-openapi.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/vitess-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/vitess-vocabulary.yml
- group: company
  title: ''
  type: Website
  url: https://vitess.io
- group: docs
  title: ''
  type: Documentation
  url: https://vitess.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://vitess.io/docs/get-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vitessio
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/vitessio/vitess
- group: company
  title: ''
  type: Blog
  url: https://vitess.io/blog/
- group: operate
  title: ''
  type: Community
  url: https://vitess.io/community/
- group: operate
  title: ''
  type: Slack
  url: https://vitess.io/slack
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/vitessio/vitess/blob/main/changelog/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/vitess
- group: auth
  title: ''
  type: Security
  url: https://github.com/vitessio/vitess/blob/main/SECURITY.md
created: '2025'
description: Vitess is a CNCF graduated database clustering system for horizontal scaling of MySQL through generalized sharding. It provides MySQL protocol compatibility, automated resharding, query routing, and connection pooling, making it suitable for running large-scale MySQL deployments on Kubernetes or other container orchestration platforms.
examples:
- key_count: 2
  name: Vitess Vtadmin Gettablets Example
  slug: vitess-vtadmin-getTablets-example
- key_count: 2
  name: Vitess Vtadmin Getworkflows Example
  slug: vitess-vtadmin-getWorkflows-example
finops:
- name: Vitess Finops
  service_category: Open Source Database
  slug: vitess-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vitess.png
json_schemas:
- name: Vitess Topology
  property_count: 0
  slug: vitess-topology
json_structures:
- name: Vitess Tablet Structure
  property_count: 0
  slug: vitess-tablet-structure
jsonld:
- class_count: 0
  name: Vitess Context
  property_count: 9
  slug: vitess-context
layout: provider
modified: '2026-05-03'
name: Vitess
nav: Providers
network: true
overview: 'Vitess publishes 1 API on the [APIs.io](https://apis.io/) network: VTAdmin API. Tagged areas include Cloud Native, CNCF, Database, Distributed Systems, and Graduated.


  The Vitess catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vitess'' developer surface includes documentation, getting-started guide, engineering blog, changelog, Stack Overflow tag, and 13 more developer resources.'
plans:
- name: Vitess Plans Pricing
  plan_count: 1
  slug: vitess-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Vitess Rate Limits
  slug: vitess-rate-limits
rules:
- name: Vitess API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: vitess-jsonschema-spectral-rules
- name: Vitess API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 2
    info: 0
    warn: 5
  slug: vitess-rules
score:
  band: developing
  composite: 43.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 40.3
    developer_ergonomics: 26.1
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 43.4
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vitess/refs/heads/main/screenshots/vitess-2026-06-20T201108.png
security:
- kind: domain-security
  name: Vitess Domain Security
  slug: vitess-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vitess
tags:
- Cloud Native
- CNCF
- Database
- Distributed Systems
- Graduated
- MySQL
- Sharding
website: https://vitess.io
---
