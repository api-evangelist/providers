---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Tikv Agentic Access
  operation_count: 10
  slug: tikv-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 8
apis:
- description: The official Java client for TiKV. Supports raw key-value operations and transactional operations via gRPC. Available on Maven Central.
  name: TiKV Java Client
  slug: tikv-client-java
- description: The official Rust client for TiKV providing raw and transactional key-value access to TiKV clusters.
  name: TiKV Rust Client
  slug: tikv-client-rust
- description: The official Python client for TiKV supporting raw and transactional key-value operations.
  name: TiKV Python Client
  slug: tikv-client-python
- description: TiKV node configuration management
  name: TiKV Configuration API
  slug: tikv-configuration-api
- description: Debug and diagnostic endpoints
  name: TiKV Debug API
  slug: tikv-debug-api
- description: Prometheus metrics endpoint
  name: TiKV Metrics API
  slug: tikv-metrics-api
- description: Region management and inspection
  name: TiKV Regions API
  slug: tikv-regions-api
- description: Node status and health
  name: TiKV Status API
  slug: tikv-status-api
artifact_total: 21
collections:
- collection_type: open
  name: TiKV HTTP Management API
  slug: open-tikv-http-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tikv-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tikv-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pingcap
- group: company
  title: ''
  type: Website
  url: https://tikv.org/
- group: docs
  title: ''
  type: Documentation
  url: https://tikv.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://tikv.org/docs/7.1/concepts/overview/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tikv
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/tikv/tikv
- group: other
  title: ''
  type: Governance
  url: https://github.com/tikv/tikv/blob/master/GOVERNANCE.md
- group: other
  title: ''
  type: CNCF
  url: https://www.cncf.io/projects/tikv/
- group: company
  title: ''
  type: Blog
  url: https://tikv.org/blog/
- group: operate
  title: ''
  type: Community
  url: https://tikv.org/community/
- group: operate
  title: ''
  type: RoadMap
  url: https://github.com/tikv/tikv/blob/master/ROADMAP.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/tikv/tikv/blob/master/LICENSE
- group: operate
  title: ''
  type: Slack
  url: https://slack.tidb.io/invite?team=tikv-wg
- group: operate
  title: ''
  type: Forums
  url: https://internals.tidb.io/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tikv/client-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tikv/client-rust
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tikv/client-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tikv/client-go
created: '2025-01-01'
description: TiKV is a CNCF-graduated distributed transactional key-value database built in Rust with Raft consensus. Originally created to complement TiDB, it provides horizontal scalability, strong consistency, and high availability with ACID transaction support. Client APIs are available for Java, Rust, Python, Go, and C++. An HTTP management API provides status, configuration, and monitoring endpoints.
examples:
- key_count: 2
  name: Tikv Getregionbyid Example
  slug: tikv-getRegionById-example
- key_count: 2
  name: Tikv Getstatus Example
  slug: tikv-getStatus-example
finops:
- name: Tikv Finops
  service_category: Database
  slug: tikv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tikv.png
json_schemas:
- name: TiKV Region
  property_count: 10
  slug: tikv-region
json_structures:
- name: Tikv Region Structure
  property_count: 0
  slug: tikv-region-structure
jsonld:
- class_count: 14
  name: Tikv Context
  property_count: 0
  slug: tikv-context
layout: provider
modified: '2026-05-19'
name: TiKV
nav: Providers
network: true
overview: 'TiKV publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Configuration API, Debug API, Metrics API, and 2 more. Tagged areas include ACID, CNCF, Database, Distributed Systems, and Key-Value Store.


  The TiKV catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TiKV''s developer surface includes documentation, getting-started guide, engineering blog, and 17 more developer resources.'
plans:
- name: Tikv Plans Pricing
  plan_count: 1
  slug: tikv-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 1
  name: Tikv Rate Limits
  slug: tikv-rate-limits
rules:
- name: TiKV API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tikv-jsonschema-spectral-rules
- name: TiKV API Rules
  rule_count: 4
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 2
  slug: tikv-rules
score:
  band: developing
  composite: 44.9
  delta: -4.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 53.2
    developer_ergonomics: 41.3
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 49.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tikv/refs/heads/main/screenshots/tikv-2026-06-20T195351.png
security:
- kind: domain-security
  name: Tikv Domain Security
  slug: tikv-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tikv
tags:
- ACID
- CNCF
- Database
- Distributed Systems
- Key-Value Store
- Open Source
- Rust
website: https://tikv.org/
---
