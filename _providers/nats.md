---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nats Agentic Access
  operation_count: 10
  slug: nats-agentic-access
  summary_line: 10 operations
api_count: 2
apis:
- description: Asynchronous messaging API supporting core pub-sub, request-reply, queue groups, and JetStream persistent messaging with streams, consumers, key-value stores, and object stores.
  name: NATS Messaging API
  slug: nats-messaging-api
- description: 'The JetStream wire API provides a protocol-level management interface for configuring and operating JetStream streams, consumers, key-value buckets, and object stores. Requests are made by publishing '
  name: NATS JetStream Management API
  slug: nats-jetstream-management-api
- description: The NATS Key-Value Store API is a JetStream-backed abstraction that provides immediately consistent, persistent associative array semantics. Clients can create buckets, get, put, delete, and watch key
  name: NATS Key-Value Store API
  slug: nats-kv-api
- description: The NATS Object Store API is a JetStream-backed abstraction for storing and retrieving arbitrarily large binary objects using a chunking mechanism. Objects are identified by a bucket and a name, and t
  name: NATS Object Store API
  slug: nats-object-store-api
- baseURL: http://localhost:8222
  baseurl_source: declared
  description: The Accounts API from NATS — 1 operation(s) for accounts.
  name: NATS Accounts API
  slug: nats-accounts-api
- baseURL: http://localhost:8222
  baseurl_source: declared
  description: The Connections API from NATS — 1 operation(s) for connections.
  name: NATS Connections API
  slug: nats-connections-api
- baseURL: http://localhost:8222
  baseurl_source: declared
  description: The Gateways API from NATS — 1 operation(s) for gateways.
  name: NATS Gateways API
  slug: nats-gateways-api
- baseURL: http://localhost:8222
  baseurl_source: declared
  description: The Health API from NATS — 1 operation(s) for health.
  name: NATS Health API
  slug: nats-health-api
- baseURL: http://localhost:8222
  baseurl_source: declared
  description: The JetStream API from NATS — 1 operation(s) for jetstream.
  name: NATS JetStream API
  slug: nats-jetstream-api
- baseURL: http://localhost:8222
  baseurl_source: declared
  description: The Leaf Nodes API from NATS — 1 operation(s) for leaf nodes.
  name: NATS Leaf Nodes API
  slug: nats-leaf-nodes-api
- baseURL: http://localhost:8222
  baseurl_source: declared
  description: The Routes API from NATS — 1 operation(s) for routes.
  name: NATS Routes API
  slug: nats-routes-api
- baseURL: http://localhost:8222
  baseurl_source: declared
  description: The Server API from NATS — 2 operation(s) for server.
  name: NATS Server API
  slug: nats-server-api
- baseURL: http://localhost:8222
  baseurl_source: declared
  description: The Subscriptions API from NATS — 1 operation(s) for subscriptions.
  name: NATS Subscriptions API
  slug: nats-subscriptions-api
artifact_total: 34
asyncapis:
- description: NATS provides cloud-native messaging with core pub-sub, request-reply, and queue group patterns, plus JetStream for persistent streaming with streams, consumers, key-value stores, and object stores.
  name: NATS Core and JetStream Messaging API
  slug: nats-messaging
collections:
- collection_type: open
  name: NATS Monitoring HTTP Accounts API
  slug: open-nats-accounts-api
- collection_type: open
  name: NATS Monitoring HTTP Accounts Clustering API
  slug: open-nats-clustering-api
- collection_type: open
  name: NATS Monitoring HTTP Accounts Connections API
  slug: open-nats-connections-api
- collection_type: open
  name: NATS Monitoring HTTP Accounts Gateways API
  slug: open-nats-gateways-api
- collection_type: open
  name: NATS Monitoring HTTP Accounts Health API
  slug: open-nats-health-api
- collection_type: open
  name: NATS Monitoring HTTP Accounts JetStream API
  slug: open-nats-jetstream-api
- collection_type: open
  name: NATS Monitoring HTTP Accounts Leaf Nodes API
  slug: open-nats-leaf-nodes-api
- collection_type: open
  name: NATS HTTP Accounts Monitoring API
  slug: open-nats-monitoring-api
- collection_type: open
  name: NATS Monitoring HTTP API
  slug: open-nats-monitoring
- collection_type: open
  name: NATS Monitoring HTTP Accounts Routes API
  slug: open-nats-routes-api
- collection_type: open
  name: NATS Monitoring HTTP Accounts Server API
  slug: open-nats-server-api
- collection_type: open
  name: NATS Monitoring HTTP Accounts Subscriptions API
  slug: open-nats-subscriptions-api
common:
- group: commercial
  href: https://artifacts.apis.io/nats/plans/nats-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nats-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/nats/rate-limits/nats-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nats-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/nats/finops/nats-finops.yml
  title: ''
  type: FinOps
  url: finops/nats-finops.yml
- group: other
  href: https://artifacts.apis.io/nats/capabilities/nats-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/nats-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/nats/agentic-access/nats-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nats-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/nats/security/nats-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nats-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nats.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nats.io
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nats.io/running-a-nats-service/introduction/installation
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/nats-io/nats-server
- group: company
  title: ''
  type: Blog
  url: https://nats.io/blog/
- group: operate
  title: ''
  type: Slack
  url: https://slack.nats.io
- group: operate
  title: ''
  type: Issues
  url: https://github.com/nats-io/nats-server/issues
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/nats-io/nats-server/releases
- group: build
  title: ''
  type: Examples
  url: https://natsbyexample.com
- group: build
  title: ''
  type: CLI
  url: https://docs.nats.io/using-nats/nats-tools/nats_cli
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nats-io
- group: docs
  href: https://artifacts.apis.io/nats/properties/nats-server-config-json-schema.json
  title: ''
  type: JSONSchema
  url: properties/nats-server-config-json-schema.json
- group: docs
  href: https://artifacts.apis.io/nats/properties/nats-jetstream-config-json-schema.json
  title: ''
  type: JSONSchema
  url: properties/nats-jetstream-config-json-schema.json
- group: docs
  href: https://artifacts.apis.io/nats/properties/nats-kv-schema.json
  title: ''
  type: JSONSchema
  url: properties/nats-kv-schema.json
- group: docs
  href: https://artifacts.apis.io/nats/properties/nats-object-store-schema.json
  title: ''
  type: JSONSchema
  url: properties/nats-object-store-schema.json
- group: design
  href: https://artifacts.apis.io/nats/properties/nats-context-jsonld.json
  title: ''
  type: JSONLD
  url: properties/nats-context-jsonld.json
- group: operate
  title: ''
  type: Support
  url: https://nats.io/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nats.io/privacy/
- group: operate
  title: ''
  type: Community
  url: https://nats.io/community/
- group: build
  title: ''
  type: SDKs
  url: https://docs.nats.io/using-nats/developer
- group: other
  title: ''
  type: Download
  url: https://nats.io/download/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.nats.io/llms.txt
created: '2025-01-01'
description: A high-performance, cloud-native messaging system for microservices, IoT, and edge computing. Provides pub-sub, request-reply, and queue-based messaging patterns with at-most-once and at-least-once delivery guarantees.
finops:
- has_sources: true
  method: generated
  name: Nats Finops
  primary_unit: month
  service_category: Messaging + Streaming
  slug: nats-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nats.png
json_schemas:
- name: NATS JetStream Stream Configuration
  property_count: 19
  slug: nats-stream-config
layout: provider
modified: '2026-05-19'
name: NATS
nav: Providers
network: true
overview: 'NATS publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Messaging API, JetStream Management API, Accounts API, and 10 more. Tagged areas include NATS, Cloud-Native, IoT, Message Broker, and Microservices.


  The NATS catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  NATS''s developer surface includes documentation, getting-started guide, engineering blog, changelog, code examples, CLI, support, and 21 more developer resources.'
plans:
- name: Nats Plans Pricing
  plan_count: 8
  slug: nats-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 8
  name: Nats Rate Limits
  slug: nats-rate-limits
rules:
- authorship: generated
  effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: NATS — asyncapi rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 5
  slug: nats-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: NATS — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: nats-jsonschema-spectral-rules
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 50.9
    catalog_earned_first_party: 0.0
    catalog_gap: 64.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 54.5
    developer_ergonomics: 50.0
    discoverability: 64.3
    operational_transparency: 28.9
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/nats/nats-2026-06-20T190052.png
security:
- kind: domain-security
  name: Nats Domain Security
  slug: nats-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nats
tags:
- NATS
- Cloud-Native
- IoT
- Message Broker
- Microservices
- Pub/Sub
- Real-Time
website: https://nats.io
---
