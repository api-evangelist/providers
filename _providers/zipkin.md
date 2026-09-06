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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Zipkin Agentic Access
  operation_count: 9
  slug: zipkin-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- baseURL: http://localhost:9411
  baseurl_source: spec
  description: Autocomplete tag key and value lookups
  name: Zipkin Autocomplete API
  slug: zipkin-autocomplete-api
- baseURL: http://localhost:9411
  baseurl_source: spec
  description: Query service dependency links
  name: Zipkin Dependencies API
  slug: zipkin-dependencies-api
- baseURL: http://localhost:9411
  baseurl_source: spec
  description: Server health check
  name: Zipkin Health API
  slug: zipkin-health-api
- baseURL: http://localhost:9411
  baseurl_source: spec
  description: Query registered service names
  name: Zipkin Services API
  slug: zipkin-services-api
- baseURL: http://localhost:9411
  baseurl_source: spec
  description: Submit and query span names
  name: Zipkin Spans API
  slug: zipkin-spans-api
- baseURL: http://localhost:9411
  baseurl_source: spec
  description: Search and retrieve distributed traces
  name: Zipkin Traces API
  slug: zipkin-traces-api
artifact_total: 49
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zipkin API v2
  slug: open-zipkin-api-v2
- collection_type: open
  name: Zipkin API v2 Autocomplete API
  slug: open-zipkin-autocomplete-api
- collection_type: open
  name: Zipkin API v2 Autocomplete Dependencies API
  slug: open-zipkin-dependencies-api
- collection_type: open
  name: Zipkin API v2 Autocomplete Health API
  slug: open-zipkin-health-api
- collection_type: open
  name: Zipkin API v2 Autocomplete Services API
  slug: open-zipkin-services-api
- collection_type: open
  name: Zipkin API v2 Autocomplete Spans API
  slug: open-zipkin-spans-api
- collection_type: open
  name: Zipkin API v2 Autocomplete Traces API
  slug: open-zipkin-traces-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/openzipkin/zipkin/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/openzipkin/zipkin/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/openzipkin/zipkin/blob/master/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/openzipkin/zipkin/blob/master/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/openzipkin/zipkin/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zipkin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zipkin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zipkin.io
- group: docs
  title: ''
  type: Documentation
  url: https://zipkin.io/pages/quickstart.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openzipkin
- group: build
  title: ''
  type: SDKs
  url: https://github.com/openzipkin/brave
- group: build
  title: ''
  type: SDKs
  url: https://github.com/openzipkin/zipkin-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/openzipkin/zipkin-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/openzipkin/zipkin-ruby
- group: design
  title: ''
  type: JSONLD
  url: json-ld/zipkin-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/zipkin-spectral.yaml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/zipkin-vocabulary.yaml
created: '2026-03-25'
description: Zipkin is an open source distributed tracing system for gathering timing data to troubleshoot latency problems in microservice architectures. It was originally developed at Twitter based on the Google Dapper paper, and is now a CNCF-related project maintained by the OpenZipkin community. Zipkin provides a collector, storage, and query service with a UI for visualizing trace data across distributed services.
examples:
- key_count: 4
  name: Zipkin Api V2 Get Dependencies Example
  slug: zipkin-api-v2-get-dependencies-example
- key_count: 4
  name: Zipkin Api V2 Get Services Example
  slug: zipkin-api-v2-get-services-example
- key_count: 4
  name: Zipkin Api V2 Report Spans Example
  slug: zipkin-api-v2-report-spans-example
- key_count: 4
  name: Zipkin Api V2 Search Traces Example
  slug: zipkin-api-v2-search-traces-example
features:
- description: End-to-end tracing of requests across microservices.
  name: Distributed Tracing
- description: Ingestion of spans via HTTP, Kafka, and other transports.
  name: Span Collection
- description: Query traces by service, span name, tags, and time range.
  name: Trace Search
- description: Derived service-to-service dependency links from spans.
  name: Dependency Graph
- description: Web-based UI for exploring traces and dependency graphs.
  name: UI
- description: Pluggable backends including in-memory, MySQL, Cassandra, and Elasticsearch.
  name: Pluggable Storage
finops:
- name: Zipkin Finops
  service_category: API
  slug: zipkin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zipkin.png
integrations:
- description: Java instrumentation library for OpenZipkin.
  name: Brave
- description: OpenTelemetry can export traces to Zipkin.
  name: OpenTelemetry
- description: Spring framework integration emitting Zipkin traces.
  name: Spring Cloud Sleuth
- description: Span transport via Kafka for asynchronous ingestion.
  name: Kafka
- description: Storage backend for spans and traces at scale.
  name: Elasticsearch
json_schemas:
- name: Annotation
  property_count: 2
  slug: zipkin-api-v2-annotation
- name: DependencyLink
  property_count: 4
  slug: zipkin-api-v2-dependency-link
- name: Endpoint
  property_count: 4
  slug: zipkin-api-v2-endpoint
- name: Span
  property_count: 13
  slug: zipkin-api-v2-span
json_structures:
- name: Zipkin Api V2 Annotation Structure
  property_count: 2
  slug: zipkin-api-v2-annotation-structure
- name: Zipkin Api V2 Dependency Link Structure
  property_count: 4
  slug: zipkin-api-v2-dependency-link-structure
- name: Zipkin Api V2 Endpoint Structure
  property_count: 4
  slug: zipkin-api-v2-endpoint-structure
- name: Zipkin Api V2 Span Structure
  property_count: 13
  slug: zipkin-api-v2-span-structure
jsonld:
- class_count: 4
  name: Zipkin Context
  property_count: 20
  slug: zipkin-context
layout: provider
modified: '2026-05-19'
name: Zipkin
nav: Providers
network: true
overview: 'Zipkin publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Dependencies API, Health API, and 3 more. Tagged areas include Distributed Tracing, Observability, Open-Source, and Microservices.


  The Zipkin catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Zipkin''s developer surface includes documentation and 16 more developer resources.'
plans:
- name: Zipkin Plans Pricing
  plan_count: 3
  slug: zipkin-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Zipkin Rate Limits
  slug: zipkin-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Zipkin API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: zipkin-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Zipkin API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: zipkin-spectral
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 63.5
    catalog_earned_first_party: 0.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 61.2
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 28.8
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 85.0
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zipkin/refs/heads/main/screenshots/zipkin-2026-06-20T201916.png
security:
- kind: domain-security
  name: Zipkin Domain Security
  slug: zipkin-domain-security
  summary_line: TLSv1.3
slug: zipkin
tags:
- Distributed Tracing
- Observability
- Open-Source
- Microservices
use_cases:
- description: Identify slow services and operations in a microservice architecture.
  name: Microservices Latency Debugging
- description: Trace failed requests across services to find error origin.
  name: Error Investigation
- description: Visualize which services call which, with call counts.
  name: Service Dependency Mapping
- description: Identify hotspots and optimize critical-path operations.
  name: Performance Optimization
website: https://zipkin.io
---
