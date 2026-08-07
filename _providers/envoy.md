---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 2
  name: Envoy Agentic Access
  operation_count: 23
  slug: envoy-agentic-access
  summary_line: 23 operations · 9 acting · 2 human-in-the-loop
api_count: 15
apis:
- description: 'The xDS (x Discovery Service) APIs provide dynamic configuration for Envoy proxies via a management server, including LDS, RDS, CDS, EDS, SDS, and ADS. xDS APIs are served over gRPC or REST and allow '
  name: Envoy xDS APIs
  slug: envoy-xds-api
- description: The Envoy API v3 is the current stable protobuf-based configuration and extension API for Envoy proxy. It defines the configuration types for all Envoy subsystems including listeners, clusters, routes
  name: Envoy API V3
  slug: envoy-api-v3
- description: Envoy Gateway manages Envoy Proxy as a standalone or Kubernetes-based application gateway, implementing and extending the Kubernetes Gateway API. It provides Gateway API extensions including BackendTr
  name: Envoy Gateway API
  slug: envoy-gateway-api
- description: TLS certificate inspection endpoints
  name: Envoy Certificates API
  slug: envoy-certificates-api
- description: Chat completions endpoints compatible with the OpenAI Chat API. Routes requests to configured AI backends based on AIGatewayRoute rules.
  name: Envoy Chat API
  slug: envoy-chat-api
- description: Upstream cluster inspection and status endpoints
  name: Envoy Clusters API
  slug: envoy-clusters-api
- description: Configuration dump and inspection endpoints
  name: Envoy Configuration API
  slug: envoy-configuration-api
- description: Health check management endpoints
  name: Envoy Health API
  slug: envoy-health-api
- description: Listener inspection and drain endpoints
  name: Envoy Listeners API
  slug: envoy-listeners-api
- description: Log level management endpoints
  name: Envoy Logging API
  slug: envoy-logging-api
- description: Model listing endpoints for discovering available AI models configured in the gateway routes.
  name: Envoy Models API
  slug: envoy-models-api
- description: Runtime settings management endpoints
  name: Envoy Runtime API
  slug: envoy-runtime-api
- description: Server management, lifecycle, and information endpoints
  name: Envoy Server API
  slug: envoy-server-api
- description: Statistics, metrics, and Prometheus endpoints
  name: Envoy Statistics API
  slug: envoy-statistics-api
- description: Legacy text completions endpoints compatible with the OpenAI completions API.
  name: Envoy Text Completions API
  slug: envoy-text-completions-api
artifact_total: 29
collections:
- collection_type: open
  name: Envoy Admin API
  slug: open-envoy-admin-api
- collection_type: open
  name: Envoy AI Gateway API
  slug: open-envoy-ai-gateway
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/envoy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/envoy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/envoy-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/envoy-inc
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
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/envoy-bootstrap.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/envoy-cluster.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/envoy-listener.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/envoy-route-configuration.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/envoy-context.jsonld
created: '2025-01-01'
description: Envoy is a high-performance, open-source edge and service proxy designed for cloud-native applications and microservice architectures. It provides advanced load balancing, observability, and traffic management features, and serves as the data plane for many service mesh implementations including Istio.
finops:
- name: Envoy Finops
  service_category: Open-Source Networking / Service Mesh
  slug: envoy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/envoy.png
json_schemas:
- name: Envoy Bootstrap Configuration
  property_count: 10
  slug: envoy-bootstrap
- name: Envoy Cluster
  property_count: 17
  slug: envoy-cluster
- name: Envoy Listener
  property_count: 14
  slug: envoy-listener
- name: Envoy Route Configuration
  property_count: 10
  slug: envoy-route-configuration
jsonld:
- class_count: 0
  name: Envoy Context
  property_count: 10
  slug: envoy-context
layout: provider
modified: '2026-05-19'
name: Envoy
nav: Providers
network: true
overview: 'Envoy publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Certificates API, Chat API, Clusters API, and 9 more. Tagged areas include Cloud Native, Load Balancing, Proxy, and Service Mesh.


  The Envoy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Envoy''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, and 12 more developer resources.'
plans:
- name: Envoy Plans Pricing
  plan_count: 2
  slug: envoy-plans-pricing
random_paper: 109
rate_limits:
- limit_count: 3
  name: Envoy Rate Limits
  slug: envoy-rate-limits
rules:
- name: Envoy API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: envoy-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 65.6
    developer_ergonomics: 37.0
    discoverability: 63.0
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/envoy/refs/heads/main/screenshots/envoy-2026-06-20T180740.png
security:
- kind: authentication
  name: Envoy Authentication
  slug: envoy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Envoy Domain Security
  slug: envoy-domain-security
  summary_line: TLSv1.3 · HSTS
slug: envoy
tags:
- Cloud Native
- Load Balancing
- Proxy
- Service Mesh
website: https://www.envoyproxy.io/
---
