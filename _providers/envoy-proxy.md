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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 16
  human_in_the_loop: 4
  name: Envoy Proxy Agentic Access
  operation_count: 32
  slug: envoy-proxy-agentic-access
  summary_line: 32 operations · 16 acting · 4 human-in-the-loop
api_count: 2
apis:
- description: The Envoy Rate Limit Service (RLS) is a gRPC-based API that allows Envoy to delegate rate limiting decisions to an external service. When a request matches a configured rate limit rule, Envoy calls th
  name: Envoy Proxy Rate Limit Service API
  slug: rate-limit-service-api
- description: The Envoy Health Discovery Service (HDS) is a gRPC-based API that enables a management server to instruct Envoy to perform health checks on behalf of the control plane and report results back. This al
  name: Envoy Proxy Health Discovery Service API
  slug: health-discovery-service-api
- description: The Envoy gRPC Access Log Service (ALS) API provides a streaming gRPC interface for receiving access log entries from Envoy instances in real time. It enables centralized log aggregation by allowing E
  name: Envoy Proxy gRPC Access Log Service API
  slug: access-log-service-api
- description: The Envoy External Processing API is a gRPC-based service that enables an external server to inspect and modify HTTP requests and responses as they pass through Envoy. This extensibility mechanism sup
  name: Envoy Proxy External Processing API
  slug: external-processing-api
- description: The Envoy External Authorization API provides a gRPC or HTTP interface for delegating authorization decisions to an external service. When a request arrives, Envoy calls the ext_authz service, which c
  name: Envoy Proxy External Authorization API
  slug: external-authorization-api
- description: The Envoy Metrics Service API is a gRPC-based interface for streaming Envoy's statistics and metrics to a remote metrics collection service. It allows operators to centralize telemetry data from multi
  name: Envoy Proxy Metrics Service API
  slug: metrics-service-api
- description: The Envoy Tap Service API provides a mechanism for intercepting and recording HTTP and TCP traffic passing through Envoy. The tap filter matches requests and responses based on configurable conditions
  name: Envoy Proxy Tap Service API
  slug: tap-service-api
- description: TLS certificate information endpoints.
  name: Envoy Proxy Certificates API
  slug: envoy-proxy-certificates-api
- description: Cluster Discovery Service (CDS) endpoints for dynamically discovering upstream clusters.
  name: Envoy Proxy Cluster Discovery API
  slug: envoy-proxy-cluster-discovery-api
- description: Cluster management and information endpoints.
  name: Envoy Proxy Clusters API
  slug: envoy-proxy-clusters-api
- description: Configuration inspection and dump endpoints.
  name: Envoy Proxy Configuration API
  slug: envoy-proxy-configuration-api
- description: Debugging and traffic inspection endpoints.
  name: Envoy Proxy Debugging API
  slug: envoy-proxy-debugging-api
- description: Endpoint Discovery Service (EDS) endpoints for dynamically discovering cluster endpoints.
  name: Envoy Proxy Endpoint Discovery API
  slug: envoy-proxy-endpoint-discovery-api
- description: General admin interface endpoints.
  name: Envoy Proxy General API
  slug: envoy-proxy-general-api
- description: Health check management endpoints.
  name: Envoy Proxy Health API
  slug: envoy-proxy-health-api
- description: Listener Discovery Service (LDS) endpoints for dynamically discovering listeners.
  name: Envoy Proxy Listener Discovery API
  slug: envoy-proxy-listener-discovery-api
- description: Listener management endpoints.
  name: Envoy Proxy Listeners API
  slug: envoy-proxy-listeners-api
- description: Logging level management endpoints.
  name: Envoy Proxy Logging API
  slug: envoy-proxy-logging-api
- description: CPU and heap profiling endpoints.
  name: Envoy Proxy Profiling API
  slug: envoy-proxy-profiling-api
- description: Route Discovery Service (RDS) endpoints for dynamically discovering route configurations.
  name: Envoy Proxy Route Discovery API
  slug: envoy-proxy-route-discovery-api
- description: Runtime configuration management endpoints.
  name: Envoy Proxy Runtime API
  slug: envoy-proxy-runtime-api
- description: Runtime Discovery Service (RTDS) endpoints for dynamically discovering runtime configuration layers.
  name: Envoy Proxy Runtime Discovery API
  slug: envoy-proxy-runtime-discovery-api
- description: Secret Discovery Service (SDS) endpoints for dynamically discovering TLS certificates and keys.
  name: Envoy Proxy Secret Discovery API
  slug: envoy-proxy-secret-discovery-api
- description: Server information and lifecycle endpoints.
  name: Envoy Proxy Server API
  slug: envoy-proxy-server-api
- description: Statistics and metrics endpoints.
  name: Envoy Proxy Statistics API
  slug: envoy-proxy-statistics-api
artifact_total: 57
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Envoy Proxy Admin API
  slug: open-envoy-proxy-admin-api
- collection_type: open
  name: Envoy Proxy Admin Certificates API
  slug: open-envoy-proxy-certificates-api
- collection_type: open
  name: Envoy Proxy Admin Certificates Cluster Discovery API
  slug: open-envoy-proxy-cluster-discovery-api
- collection_type: open
  name: Envoy Proxy Admin Certificates Clusters API
  slug: open-envoy-proxy-clusters-api
- collection_type: open
  name: Envoy Proxy Admin Certificates Configuration API
  slug: open-envoy-proxy-configuration-api
- collection_type: open
  name: Envoy Proxy Admin Certificates Debugging API
  slug: open-envoy-proxy-debugging-api
- collection_type: open
  name: Envoy Proxy Admin Certificates Endpoint Discovery API
  slug: open-envoy-proxy-endpoint-discovery-api
- collection_type: open
  name: Envoy Proxy Admin Certificates General API
  slug: open-envoy-proxy-general-api
- collection_type: open
  name: Envoy Proxy Admin Certificates Health API
  slug: open-envoy-proxy-health-api
- collection_type: open
  name: Envoy Proxy Admin Certificates Listener Discovery API
  slug: open-envoy-proxy-listener-discovery-api
- collection_type: open
  name: Envoy Proxy Admin Certificates Listeners API
  slug: open-envoy-proxy-listeners-api
- collection_type: open
  name: Envoy Proxy Admin Certificates Logging API
  slug: open-envoy-proxy-logging-api
- collection_type: open
  name: Envoy Proxy Admin Certificates Profiling API
  slug: open-envoy-proxy-profiling-api
- collection_type: open
  name: Envoy Proxy Admin Certificates Route Discovery API
  slug: open-envoy-proxy-route-discovery-api
- collection_type: open
  name: Envoy Proxy Admin Certificates Runtime API
  slug: open-envoy-proxy-runtime-api
- collection_type: open
  name: Envoy Proxy Admin Certificates Runtime Discovery API
  slug: open-envoy-proxy-runtime-discovery-api
- collection_type: open
  name: Envoy Proxy Admin Certificates Secret Discovery API
  slug: open-envoy-proxy-secret-discovery-api
- collection_type: open
  name: Envoy Proxy Admin Certificates Server API
  slug: open-envoy-proxy-server-api
- collection_type: open
  name: Envoy Proxy Admin Certificates Statistics API
  slug: open-envoy-proxy-statistics-api
- collection_type: open
  name: Envoy Proxy xDS Discovery API
  slug: open-envoy-proxy-xds-discovery-api
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/envoyproxy/envoy/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/envoyproxy/envoy/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/envoyproxy/envoy/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/envoy-proxy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/envoy-proxy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.envoyproxy.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.envoyproxy.io/docs/envoy/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.envoyproxy.io/docs/envoy/latest/start/start
- group: company
  title: ''
  type: Blog
  url: https://blog.envoyproxy.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/envoyproxy/envoy/releases
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/envoyproxy
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/envoyproxy/envoy
- group: operate
  title: ''
  type: Community
  url: https://www.envoyproxy.io/community
- group: auth
  title: ''
  type: Security
  url: https://github.com/envoyproxy/envoy/blob/main/SECURITY.md
- group: design
  title: ''
  type: JSONLD
  url: json-ld/envoy-proxy-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/envoy-proxy-cluster.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/envoy-proxy-listener.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/envoy-proxy-route.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/envoy-proxy-endpoint.json
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/envoyproxy/envoy/issues
- group: operate
  title: ''
  type: Community
  url: https://envoyslack.cncf.io/
- group: operate
  title: ''
  type: Community
  url: https://www.cncf.io/projects/envoy/
- group: docs
  title: ''
  type: Reference
  url: https://www.envoyproxy.io/docs/envoy/latest/api-v3/api
created: '2026-01-02'
description: Envoy Proxy is an open-source edge and service proxy that is designed for cloud-native applications. It acts as a gateway for all incoming and outgoing traffic within a microservices architecture, providing functionalities such as load balancing, service discovery, encryption, authentication, and observability. Envoy Proxy is known for its high performance and low latency, making it a popular choice for companies seeking to optimize their network traffic and improve overall system efficiency.
finops:
- name: Envoy Proxy Finops
  service_category: Networking / API Gateway
  slug: envoy-proxy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/envoy-proxy.png
json_schemas:
- name: Envoy Proxy Cluster
  property_count: 10
  slug: envoy-proxy-cluster
- name: Envoy Proxy Endpoint
  property_count: 4
  slug: envoy-proxy-endpoint
- name: Envoy Proxy Listener
  property_count: 8
  slug: envoy-proxy-listener
- name: Envoy Proxy Route Configuration
  property_count: 4
  slug: envoy-proxy-route
jsonld:
- class_count: 4
  name: Envoy Proxy Context
  property_count: 10
  slug: envoy-proxy-context
layout: provider
modified: '2026-05-19'
name: Envoy Proxy
nav: Providers
network: true
overview: 'Envoy Proxy publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Certificates API, Cluster Discovery API, Clusters API, and 15 more. Tagged areas include Gateways and Proxies.


  The Envoy Proxy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Envoy Proxy''s developer surface includes documentation, getting-started guide, engineering blog, changelog, and 19 more developer resources.'
plans:
- name: Envoy Proxy Plans Pricing
  plan_count: 1
  slug: envoy-proxy-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Envoy Proxy Rate Limits
  slug: envoy-proxy-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Envoy Proxy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: envoy-proxy-jsonschema-spectral-rules
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 69.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 49.7
    developer_ergonomics: 35.7
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/envoy-proxy/refs/heads/main/screenshots/envoy-proxy-2026-06-20T180741.png
security:
- kind: domain-security
  name: Envoy Proxy Domain Security
  slug: envoy-proxy-domain-security
  summary_line: TLSv1.3 · HSTS
slug: envoy-proxy
tags:
- Gateways
- Proxies
website: https://www.envoyproxy.io/
---
