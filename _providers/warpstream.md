---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Warpstream Agentic Access
  operation_count: 15
  slug: warpstream-agentic-access
  summary_line: 15 operations · 12 acting
api_count: 8
apis:
- description: Manage Kafka ACL rules for access control
  name: WarpStream ACLs API
  slug: warpstream-acls-api
- description: Manage API keys and access grants
  name: WarpStream API Keys API
  slug: warpstream-api-keys-api
- description: Monitor consumer groups and cluster health
  name: WarpStream Monitoring API
  slug: warpstream-monitoring-api
- description: Manage data pipelines (Bento, Orbit, Schema Linking)
  name: WarpStream Pipelines API
  slug: warpstream-pipelines-api
- description: Manage Kafka topics within virtual clusters
  name: WarpStream Topics API
  slug: warpstream-topics-api
- description: Manage SASL/SCRAM credentials for virtual cluster access
  name: WarpStream Virtual Cluster Credentials API
  slug: warpstream-virtual-cluster-credentials-api
- description: Manage Kafka-compatible virtual clusters
  name: WarpStream Virtual Clusters API
  slug: warpstream-virtual-clusters-api
- description: Manage WarpStream workspaces (account-level)
  name: WarpStream Workspaces API
  slug: warpstream-workspaces-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/warpstream-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/warpstream-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/warpstream-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/warpstream-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.warpstream.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.warpstream.com/warpstream
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/warpstreamlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/warpstream/
- group: company
  title: ''
  type: Blog
  url: https://www.warpstream.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.warpstream.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.warpstream.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/warpstream_labs
- group: commercial
  title: ''
  type: Plans
  url: plans/warpstream-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/warpstream-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/warpstream-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/warpstream-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/warpstream-context.jsonld
- group: company
  title: ''
  type: BlogRSS
  url: https://www.warpstream.com/blog/rss.xml
created: 2026-06-13
description: WarpStream is a diskless, Apache Kafka-compatible data streaming platform built directly on top of cloud object storage such as S3, GCP, and Azure. It eliminates the need for local disks, brokers to rebalance, and ZooKeeper, delivering Kafka compatibility through a single, stateless Go binary deployed as auto-scaling agents in customer VPCs. WarpStream offers a REST management API for programmatically controlling workspaces, virtual clusters, topics, ACLs, pipelines, agent pools, and BYOC deployments. The platform supports Exactly Once Semantics, transactions, a built-in Schema Registry, and Tableflow for streaming data into Iceberg tables, with pricing based purely on compute minutes and uncompressed data written and stored.
examples:
- key_count: 2
  name: Create Topic
  slug: create-topic
- key_count: 2
  name: Create Virtual Cluster
  slug: create-virtual-cluster
finops:
- name: Warpstream Finops
  service_category: ''
  slug: warpstream-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/warpstream.png
json_schemas:
- name: ApiKey
  property_count: 5
  slug: api-key
- name: Topic
  property_count: 6
  slug: topic
- name: VirtualCluster
  property_count: 10
  slug: virtual-cluster
jsonld:
- class_count: 13
  name: Warpstream Context
  property_count: 51
  slug: warpstream-context
layout: provider
modified: 2026-06-13
name: WarpStream
nav: Providers
network: true
overview: 'WarpStream publishes 8 APIs on the [APIs.io](https://apis.io/) network, including ACLs API, API Keys API, Monitoring API, and 5 more. Tagged areas include Kafka, Streaming, Serverless, Object Storage, and BYOC.


  The WarpStream catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  WarpStream''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Warpstream Plans Pricing
  plan_count: 6
  slug: warpstream-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 0
  name: Warpstream Rate Limits
  slug: warpstream-rate-limits
rules:
- name: WarpStream API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: warpstream-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.6
  delta: -4.5
  facets:
    commercial_clarity: 57.9
    contract_quality: 68.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 56.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/warpstream/refs/heads/main/screenshots/warpstream-2026-06-20T201333.png
security:
- kind: authentication
  name: Warpstream Authentication
  slug: warpstream-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Warpstream Domain Security
  slug: warpstream-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Warpstream Trust Center
  slug: warpstream-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017
slug: warpstream
tags:
- Kafka
- Streaming
- Serverless
- Object Storage
- BYOC
- Data Streaming
- Apache Kafka
- Message Queue
- Event Streaming
website: https://www.warpstream.com/
---
