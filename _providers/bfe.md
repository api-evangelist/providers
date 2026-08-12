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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bfe Agentic Access
  operation_count: 7
  slug: bfe-agentic-access
  summary_line: 7 operations
api_count: 3
apis:
- description: Go pprof debugging and profiling endpoints
  name: BFE Debug API
  slug: bfe-debug-api
- description: Monitor metrics and categories for observability
  name: BFE Monitor API
  slug: bfe-monitor-api
- description: Configuration reload operations
  name: BFE Reload API
  slug: bfe-reload-api
artifact_total: 43
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/bfenetworks/bfe/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/bfenetworks/bfe/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/bfenetworks/bfe/blob/develop/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/bfenetworks/bfe/blob/develop/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/bfenetworks/bfe/blob/develop/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/bfenetworks/bfe/blob/develop/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bfe-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bfe-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bfe-networks.net/en_us/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bfe-networks.net/en_us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bfenetworks
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bfenetworks/bfe
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/bfe/refs/heads/main/vocabulary/bfe-vocabulary.yaml
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/bfe/refs/heads/main/rules/bfe-spectral-rules.yml
created: '2025-01-01'
description: BFE (Beyond Front End) is an open-source layer 7 load balancer developed by Baidu, providing advanced traffic routing, forwarding, and load balancing capabilities with support for HTTP, HTTPS, HTTP/2, WebSocket, TLS, and gRPC. BFE is a CNCF sandbox project licensed under Apache 2.0.
examples:
- key_count: 1
  name: Bfe Monitor Categories Response Example
  slug: bfe-monitor-categories-response-example
- key_count: 2
  name: Bfe Monitor Metrics Response Example
  slug: bfe-monitor-metrics-response-example
- key_count: 1
  name: Bfe Reload Entries Response Example
  slug: bfe-reload-entries-response-example
- key_count: 2
  name: Bfe Reload Entry Example
  slug: bfe-reload-entry-example
- key_count: 3
  name: Bfe Reload Response Example
  slug: bfe-reload-response-example
features:
- description: Advanced HTTP/HTTPS/HTTP2 load balancing with pluggable algorithms.
  name: Layer 7 Load Balancing
- description: Extensible plugin system enabling custom traffic management logic.
  name: Plugin Framework
- description: Isolated configuration and routing per tenant.
  name: Multi-tenancy
- description: DSL-based routing rules for fine-grained traffic control.
  name: Advanced Routing
- description: HTTP, HTTPS, SPDY, HTTP/2, gRPC, WebSocket, TLS, FastCGI protocols.
  name: Protocol Support
- description: Built-in metrics, logging, and distributed tracing integration.
  name: Observability
- description: Hot reload of routing and load balancing configuration without restart.
  name: Dynamic Configuration
- description: Hosted as a CNCF sandbox project with active community governance.
  name: CNCF Sandbox
finops:
- name: Bfe Finops
  service_category: API
  slug: bfe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bfe.png
integrations:
- description: Export metrics to Prometheus for monitoring and alerting.
  name: Prometheus
- description: Deploy BFE as an ingress controller in Kubernetes clusters.
  name: Kubernetes
- description: Run BFE in Docker containers for containerized deployments.
  name: Docker
- description: Visualize BFE metrics in Grafana dashboards.
  name: Grafana
json_schemas:
- name: MonitorCategoriesResponse
  property_count: 1
  slug: bfe-monitor-categories-response
- name: MonitorMetricsResponse
  property_count: 2
  slug: bfe-monitor-metrics-response
- name: ReloadEntriesResponse
  property_count: 1
  slug: bfe-reload-entries-response
- name: ReloadEntry
  property_count: 2
  slug: bfe-reload-entry
- name: ReloadResponse
  property_count: 3
  slug: bfe-reload-response
json_structures:
- name: Bfe Monitor Categories Response Structure
  property_count: 1
  slug: bfe-monitor-categories-response-structure
- name: Bfe Monitor Metrics Response Structure
  property_count: 2
  slug: bfe-monitor-metrics-response-structure
- name: Bfe Reload Entries Response Structure
  property_count: 1
  slug: bfe-reload-entries-response-structure
- name: Bfe Reload Entry Structure
  property_count: 2
  slug: bfe-reload-entry-structure
- name: Bfe Reload Response Structure
  property_count: 3
  slug: bfe-reload-response-structure
jsonld:
- class_count: 5
  name: Bfe Context
  property_count: 7
  slug: bfe-context
layout: provider
modified: '2026-05-19'
name: BFE
nav: Providers
network: true
overview: 'BFE publishes 3 APIs on the [APIs.io](https://apis.io/) network: Debug API, Monitor API, and Reload API. Tagged areas include Load Balancer, Networking, Open Source, Traffic Management, and CNCF.


  The BFE catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  BFE''s developer surface includes developer portal, documentation, and 12 more developer resources.'
plans:
- name: Bfe Plans Pricing
  plan_count: 3
  slug: bfe-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 5
  name: Bfe Rate Limits
  slug: bfe-rate-limits
rules:
- name: BFE API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bfe-jsonschema-spectral-rules
- name: BFE API Rules
  rule_count: 25
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 11
  slug: bfe-spectral-rules
score:
  band: thin
  composite: 31.2
  delta: -4.6
  facets:
    commercial_clarity: 15.8
    contract_quality: 18.8
    developer_ergonomics: 17.4
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 39.5
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bfe/refs/heads/main/screenshots/bfe-2026-06-20T173215.png
security:
- kind: domain-security
  name: Bfe Domain Security
  slug: bfe-domain-security
  summary_line: TLSv1.3
slug: bfe
tags:
- Load Balancer
- Networking
- Open Source
- Traffic Management
- CNCF
- Baidu
use_cases:
- description: Route and load balance API traffic with per-tenant isolation.
  name: Enterprise API Gateway
- description: Manage east-west and north-south traffic in microservices architectures.
  name: Microservices Traffic Management
- description: Terminate TLS/HTTPS at the edge and forward to backend HTTP services.
  name: TLS Termination
- description: Route fractions of traffic to canary deployments using routing rules.
  name: A/B Testing
- description: Use traffic management plugins to detect and mitigate DDoS attacks.
  name: DDoS Mitigation
website: https://www.bfe-networks.net/en_us/
---
