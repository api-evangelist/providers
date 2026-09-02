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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Krakend Agentic Access
  operation_count: 5
  slug: krakend-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- description: KrakenD Community Edition is an ultra-high performance API gateway that aggregates multiple service calls into a single endpoint, transforming and filtering responses with a declarative JSON configura
  name: KrakenD
  slug: krakend
- description: 'The KrakenD Async Agent enables event-driven API consumption by connecting KrakenD to message brokers and event queues such as AMQP, Kafka, and NATS. It allows KrakenD to consume messages from topics '
  name: KrakenD Async Agent
  slug: krakend-async-agent
- description: The Debug API from KrakenD — 2 operation(s) for debug.
  name: KrakenD Debug API
  slug: krakend-debug-api
- description: The Health API from KrakenD — 1 operation(s) for health.
  name: KrakenD Health API
  slug: krakend-health-api
- description: The Metrics API from KrakenD — 1 operation(s) for metrics.
  name: KrakenD Metrics API
  slug: krakend-metrics-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: KrakenD Service Debug API
  slug: open-krakend-debug-api
- collection_type: open
  name: KrakenD Service Debug Health API
  slug: open-krakend-health-api
- collection_type: open
  name: KrakenD Service Debug Metrics API
  slug: open-krakend-metrics-api
- collection_type: open
  name: KrakenD Service API
  slug: open-krakend-service-api
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/krakend/krakend-ce/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/krakend/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/krakend/.github/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/krakend/krakend-ce/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/krakend-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/krakend-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/krakend
- group: company
  title: ''
  type: Website
  url: https://www.krakend.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.krakend.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.krakend.io/docs/overview/introduction/
- group: company
  title: ''
  type: Blog
  url: https://www.krakend.io/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/krakend/krakend-ce/releases
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/krakend
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/krakend/krakend-ce
- group: operate
  title: ''
  type: Community
  url: https://community.krakend.io/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/krakend
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/krakend/krakend-ce/issues
- group: build
  title: ''
  type: Developer Tools
  url: https://designer.krakend.io/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/service-config.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/krakend-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/krakend/mcp-server
created: '2026-03-18'
description: KrakenD is a stateless, distributed, high-performance open-source API gateway written in Go, focused on API aggregation, transformation, and security with a declarative configuration approach.
finops:
- name: Krakend Finops
  service_category: API Management
  slug: krakend-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/krakend.png
json_schemas:
- name: KrakenD Async Agent
  property_count: 6
  slug: async-agent
- name: KrakenD Backend
  property_count: 12
  slug: backend
- name: KrakenD Endpoint
  property_count: 12
  slug: endpoint
- name: KrakenD Plugin Configuration
  property_count: 2
  slug: plugin
- name: KrakenD Service Configuration
  property_count: 17
  slug: service-config
- name: KrakenD TLS Configuration
  property_count: 10
  slug: tls
jsonld:
- class_count: 0
  name: Krakend Context
  property_count: 6
  slug: krakend-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: KrakenD
nav: Providers
network: true
overview: 'KrakenD publishes 3 APIs on the [APIs.io](https://apis.io/) network: Debug API, Health API, and Metrics API. Tagged areas include Aggregation, API Gateway, Go, and Open-Source.


  The KrakenD catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  KrakenD''s developer surface includes documentation, getting-started guide, engineering blog, changelog, Stack Overflow tag, and 16 more developer resources.'
plans:
- name: Krakend Plans Pricing
  plan_count: 2
  slug: krakend-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Krakend Rate Limits
  slug: krakend-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: KrakenD API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: krakend-jsonschema-spectral-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 70.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 51.7
    developer_ergonomics: 33.3
    discoverability: 48.1
    governance: 9.8
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/krakend/refs/heads/main/screenshots/krakend-2026-06-20T184150.png
security:
- kind: domain-security
  name: Krakend Domain Security
  slug: krakend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: krakend
tags:
- Aggregation
- API Gateway
- Go
- Open-Source
website: https://www.krakend.io/
---
