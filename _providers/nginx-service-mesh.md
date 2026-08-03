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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The NGINX Service Mesh control plane exposes a REST API used by the `nginx-meshctl` CLI to manage mesh configuration, sidecar injection, certificate authority operations, traffic policies, and resourc
  name: NGINX Service Mesh Control Plane API
  slug: control-plane-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nginx-service-mesh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.nginx.com/nginx-service-mesh/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nginx.com/nginx-service-mesh/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nginx.com/nginx-service-mesh/get-started/
- group: other
  title: ''
  type: Architecture
  url: https://docs.nginx.com/nginx-service-mesh/about/architecture/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/nginxinc/nginx-service-mesh
- group: other
  title: ''
  type: Successor
  url: https://docs.nginx.com/nginx-gateway-fabric/
- group: company
  title: ''
  type: Blog
  url: https://www.f5.com/company/blog/nginx
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.nginx.com/llms.txt
created: '2026-04-28'
description: NGINX Service Mesh (NSM) is a service mesh from F5 NGINX powered by NGINX Plus, designed to manage container-to-container traffic in Kubernetes environments. It provides mTLS, traffic policies via the Service Mesh Interface (SMI), traffic splitting, rate limiting, observability (Prometheus, Grafana, Jaeger), and integration with NGINX Plus Ingress Controller. NGINX Service Mesh exposes a control-plane REST API and a `nginx-meshctl` CLI for installation, sidecar injection, certificate management, and policy configuration. The upstream GitHub repository is archived; F5 announced End of Sale (EoS) for the NGINX Microservices Bundle as of July 1, 2023, and the project's successor for ingress and L7 routing is NGINX Gateway Fabric.
finops:
- name: Nginx Service Mesh Finops
  service_category: API
  slug: nginx-service-mesh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nginx-service-mesh.png
layout: provider
modified: '2026-04-28'
name: NGINX Service Mesh
nav: Providers
network: true
overview: 'NGINX Service Mesh publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Container Networking, End of Sale, F5, Kubernetes, and mTLS.


  NGINX Service Mesh''s developer surface includes documentation, getting-started guide, GitHub presence, engineering blog, and 5 more developer resources.'
plans:
- name: Nginx Service Mesh Plans Pricing
  plan_count: 3
  slug: nginx-service-mesh-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Nginx Service Mesh Rate Limits
  slug: nginx-service-mesh-rate-limits
score:
  band: emerging
  composite: 23.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 23.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nginx-service-mesh/refs/heads/main/screenshots/nginx-service-mesh-2026-06-20T190307.png
security:
- kind: domain-security
  name: Nginx Service Mesh Domain Security
  slug: nginx-service-mesh-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nginx-service-mesh
tags:
- Container Networking
- End of Sale
- F5
- Kubernetes
- mTLS
- NGINX
- Observability
- Service Mesh
- SMI
- Traffic Management
website: https://docs.nginx.com/nginx-service-mesh/
---
