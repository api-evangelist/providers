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
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Google Cloud Service Mesh Agentic Access
  operation_count: 22
  slug: google-cloud-service-mesh-agentic-access
  summary_line: 22 operations · 11 acting
api_count: 13
apis:
- description: The Network Security API manages security policies for Cloud Service Mesh, including authorization policies, client TLS policies, and server TLS policies. It provides REST endpoints for creating and m
  name: Google Cloud Network Security API
  slug: network-security-api
- description: Cloud Service Mesh uses the open-source xDS v3 control plane API to distribute configuration to Envoy sidecar proxies and proxyless gRPC clients. Configurations defined via the Network Services and Ne
  name: Google Cloud Service Mesh xDS Control Plane API
  slug: xds-control-plane-api
- description: The EndpointPolicies API from Google Cloud Service Mesh — 1 operation(s) for endpointpolicies.
  name: Google Cloud Service Mesh EndpointPolicies API
  slug: google-cloud-service-mesh-endpointpolicies-api
- description: The Gateways API from Google Cloud Service Mesh — 1 operation(s) for gateways.
  name: Google Cloud Service Mesh Gateways API
  slug: google-cloud-service-mesh-gateways-api
- description: The Google Cloud Network Services API (Service Mesh) API from Google Cloud Service Mesh — 2 operation(s) for google cloud network services api (service mesh).
  name: Google Cloud Service Mesh Google Cloud Network Services API (Service Mesh) API
  slug: google-cloud-service-mesh-google-cloud-network-services-api-service-mesh-api
- description: The GrpcRoutes API from Google Cloud Service Mesh — 1 operation(s) for grpcroutes.
  name: Google Cloud Service Mesh GrpcRoutes API
  slug: google-cloud-service-mesh-grpcroutes-api
- description: The HttpRoutes API from Google Cloud Service Mesh — 1 operation(s) for httproutes.
  name: Google Cloud Service Mesh HttpRoutes API
  slug: google-cloud-service-mesh-httproutes-api
- description: The Locations API from Google Cloud Service Mesh — 1 operation(s) for locations.
  name: Google Cloud Service Mesh Locations API
  slug: google-cloud-service-mesh-locations-api
- description: The Meshes API from Google Cloud Service Mesh — 1 operation(s) for meshes.
  name: Google Cloud Service Mesh Meshes API
  slug: google-cloud-service-mesh-meshes-api
- description: The Operations API from Google Cloud Service Mesh — 1 operation(s) for operations.
  name: Google Cloud Service Mesh Operations API
  slug: google-cloud-service-mesh-operations-api
- description: The ServiceLbPolicies API from Google Cloud Service Mesh — 1 operation(s) for servicelbpolicies.
  name: Google Cloud Service Mesh ServiceLbPolicies API
  slug: google-cloud-service-mesh-servicelbpolicies-api
- description: The TcpRoutes API from Google Cloud Service Mesh — 1 operation(s) for tcproutes.
  name: Google Cloud Service Mesh TcpRoutes API
  slug: google-cloud-service-mesh-tcproutes-api
- description: The TlsRoutes API from Google Cloud Service Mesh — 1 operation(s) for tlsroutes.
  name: Google Cloud Service Mesh TlsRoutes API
  slug: google-cloud-service-mesh-tlsroutes-api
artifact_total: 22
collections:
- collection_type: open
  name: Google Cloud Network Services API (Service Mesh)
  slug: open-google-cloud-service-mesh
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-service-mesh-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-service-mesh-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-service-mesh-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-service-mesh-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-service-mesh-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: company
  title: ''
  type: Website
  url: https://cloud.google.com/service-mesh
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/service-mesh/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/service-mesh/docs/onboarding/provision-control-plane
- group: docs
  title: ''
  type: Reference
  url: https://cloud.google.com/service-mesh/docs/reference/network-services/rest
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/service-mesh/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://cloud.google.com/service-mesh/docs/release-notes
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/service-mesh/docs/getting-support
- group: auth
  title: ''
  type: Security
  url: https://cloud.google.com/service-mesh/docs/security-bulletins
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/feeds/service-mesh-release-notes.xml
created: '2026-03-16'
description: Google Cloud Service Mesh is Google's managed service mesh solution for GKE and supported GKE Enterprise environments, enabling secure, observable, and reliable communication between microservices. It provides a managed Istio control plane, Google Cloud-native service routing APIs, mTLS security, and built-in telemetry for distributed applications.
finops:
- name: Google Cloud Service Mesh Finops
  service_category: API
  slug: google-cloud-service-mesh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-service-mesh.png
layout: provider
modified: '2026-05-19'
name: Google Cloud Service Mesh
nav: Providers
network: true
overview: 'Google Cloud Service Mesh publishes 11 APIs on the [APIs.io](https://apis.io/) network, including EndpointPolicies API, Gateways API, Google Cloud Network Services API (Service Mesh) API, and 8 more. Tagged areas include Google Cloud, Istio, Kubernetes, Microservices, and Service Mesh.


  Google Cloud Service Mesh''s developer surface includes authentication, documentation, getting-started guide, pricing, changelog, support, engineering blog, and 8 more developer resources.'
plans:
- name: Google Cloud Service Mesh Plans Pricing
  plan_count: 3
  slug: google-cloud-service-mesh-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Google Cloud Service Mesh Rate Limits
  slug: google-cloud-service-mesh-rate-limits
scopes:
- name: Google Cloud Service Mesh Scopes
  scope_count: 1
  slug: google-cloud-service-mesh-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 46.8
  delta: -2.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.0
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 63.2
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-service-mesh/refs/heads/main/screenshots/google-cloud-service-mesh-2026-06-20T182137.png
security:
- kind: authentication
  name: Google Cloud Service Mesh Authentication
  slug: google-cloud-service-mesh-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Service Mesh Domain Security
  slug: google-cloud-service-mesh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Service Mesh Vulnerability Disclosure
  slug: google-cloud-service-mesh-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-service-mesh
tags:
- Google Cloud
- Istio
- Kubernetes
- Microservices
- Service Mesh
website: https://cloud.google.com/service-mesh
---
