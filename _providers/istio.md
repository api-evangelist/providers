---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 36
  human_in_the_loop: 0
  name: Istio Agentic Access
  operation_count: 60
  slug: istio-agentic-access
  summary_line: 60 operations · 36 acting
api_count: 14
apis:
- description: The Istio Telemetry API (telemetry.istio.io) provides configuration resources for managing observability within an Istio service mesh. The Telemetry resource enables flexible configuration of metrics,
  name: Istio Telemetry API
  slug: telemetry-api
- description: The Istio Mesh Config API (istio.mesh.v1alpha1) provides global configuration for the Istio service mesh control plane and data plane proxy behavior. It includes MeshConfig for mesh-wide settings such
  name: Istio Mesh Config API
  slug: mesh-config-api
- description: The Istio Operator API (istio.operator.v1alpha1) defines the IstioOperator custom resource used to install, configure, and upgrade Istio on Kubernetes clusters. It provides a declarative interface for
  name: Istio Operator API
  slug: operator-api
- description: Fine-grained access control policies for workloads
  name: Istio AuthorizationPolicy API
  slug: istio-authorizationpolicy-api
- description: Policies applied to traffic after routing (load balancing, connection pool, outlier detection)
  name: Istio DestinationRule API
  slug: istio-destinationrule-api
- description: Load balancer configuration at the edge of the mesh
  name: Istio Gateway API
  slug: istio-gateway-api
- description: Mutual TLS configuration for peer-to-peer communication
  name: Istio PeerAuthentication API
  slug: istio-peerauthentication-api
- description: JWT-based request authentication policies
  name: Istio RequestAuthentication API
  slug: istio-requestauthentication-api
- description: External service entries added to the mesh service registry
  name: Istio ServiceEntry API
  slug: istio-serviceentry-api
- description: Sidecar proxy configuration for inbound and outbound traffic
  name: Istio Sidecar API
  slug: istio-sidecar-api
- description: HTTP/TCP routing rules for traffic management
  name: Istio VirtualService API
  slug: istio-virtualservice-api
- description: WebAssembly plugin configuration for Envoy proxy extensions
  name: Istio WasmPlugin API
  slug: istio-wasmplugin-api
- description: Non-Kubernetes workload (VM/bare metal) endpoint properties
  name: Istio WorkloadEntry API
  slug: istio-workloadentry-api
- description: Collection of workload instances sharing common properties
  name: Istio WorkloadGroup API
  slug: istio-workloadgroup-api
artifact_total: 37
collections:
- collection_type: open
  name: Istio Extensions API
  slug: open-istio-extensions-api
- collection_type: open
  name: Istio Networking API
  slug: open-istio-networking-api
- collection_type: open
  name: Istio Security API
  slug: open-istio-security-api
- collection_type: open
  name: Istio Telemetry API
  slug: open-istio-telemetry-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/istio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/istio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/istio-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/istio
- group: design
  title: ''
  type: JSONLD
  url: json-ld/istio-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/virtual-service.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/destination-rule.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gateway.json
- group: company
  title: ''
  type: Website
  url: https://istio.io/
- group: company
  title: ''
  type: Blog
  url: https://istio.io/latest/blog/
- group: company
  title: ''
  type: News
  url: https://istio.io/latest/news/
- group: docs
  title: ''
  type: Documentation
  url: https://istio.io/latest/docs/
- group: other
  title: ''
  type: Glossary
  url: https://istio.io/latest/docs/reference/glossary/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/istio/istio
- group: build
  title: ''
  type: GitHub
  url: https://github.com/istio/api
- group: start
  title: ''
  type: GettingStarted
  url: https://istio.io/latest/docs/setup/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/istio
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/istio/istio/releases
- group: operate
  title: ''
  type: Community
  url: https://istio.io/latest/get-involved/
- group: operate
  title: ''
  type: Support
  url: https://discuss.istio.io/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/istio
- group: auth
  title: ''
  type: Security
  url: https://istio.io/latest/docs/releases/security-vulnerabilities/
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/istio/istio/issues
created: '2025-06-05'
description: Istio is an open-source service mesh platform that provides a comprehensive solution for managing, securing, and monitoring microservices in a distributed system. It acts as a middle layer between services, handling communication, routing, and load balancing, as well as providing visibility into the traffic flowing between services. Istio also offers advanced security features such as access control, authentication, and encryption to ensure that communication between services is secure.
finops:
- name: Istio Finops
  service_category: Service Mesh / Networking
  slug: istio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/istio.png
json_schemas:
- name: Istio AuthorizationPolicy
  property_count: 5
  slug: authorization-policy
- name: Istio DestinationRule
  property_count: 5
  slug: destination-rule
- name: Istio Gateway
  property_count: 2
  slug: gateway
- name: Istio PeerAuthentication
  property_count: 3
  slug: peer-authentication
- name: Istio RequestAuthentication
  property_count: 3
  slug: request-authentication
- name: Istio ServiceEntry
  property_count: 9
  slug: service-entry
- name: Istio Sidecar
  property_count: 5
  slug: sidecar
- name: Istio Telemetry
  property_count: 5
  slug: telemetry
- name: Istio VirtualService
  property_count: 6
  slug: virtual-service
- name: Istio WasmPlugin
  property_count: 14
  slug: wasm-plugin
- name: Istio WorkloadEntry
  property_count: 4
  slug: workload-entry
jsonld:
- class_count: 0
  name: Istio Context
  property_count: 10
  slug: istio-context
layout: provider
modified: '2026-05-19'
name: Istio
nav: Providers
network: true
overview: 'Istio publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Telemetry API, AuthorizationPolicy API, DestinationRule API, and 9 more. Tagged areas include CNCF, Kubernetes, Microservices, Open Source, and Service Mesh.


  The Istio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Istio''s developer surface includes authentication, engineering blog, product news, documentation, GitHub presence, getting-started guide, changelog, and 16 more developer resources.'
plans:
- name: Istio Plans Pricing
  plan_count: 1
  slug: istio-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 1
  name: Istio Rate Limits
  slug: istio-rate-limits
rules:
- name: Istio API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: istio-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 72.9
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/istio/refs/heads/main/screenshots/istio-2026-06-20T183628.png
security:
- kind: authentication
  name: Istio Authentication
  slug: istio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Istio Domain Security
  slug: istio-domain-security
  summary_line: TLSv1.3 · HSTS
slug: istio
tags:
- CNCF
- Kubernetes
- Microservices
- Open Source
- Service Mesh
website: https://istio.io/
---
