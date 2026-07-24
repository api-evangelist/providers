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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: 'Service mesh control plane for Kubernetes that implements the Service Mesh Interface (SMI) specification, providing traffic management, security, and observability for microservices via Envoy sidecar '
  name: Open Service Mesh
  slug: open-service-mesh
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-service-mesh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openservicemesh.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openservicemesh.io
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/openservicemesh/osm
created: '2026-04-28'
description: Open Service Mesh (OSM) is a lightweight, extensible, cloud native service mesh built on Envoy and the Service Mesh Interface (SMI) specification. OSM provides traffic shifting, mutual TLS, access control, observability, and automatic sidecar injection for Kubernetes-based microservices. The project is now archived by the CNCF.
finops:
- name: Open Service Mesh Finops
  service_category: API
  slug: open-service-mesh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-service-mesh.png
layout: provider
modified: '2026-04-28'
name: Open Service Mesh
nav: Providers
network: true
overview: 'Open Service Mesh publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Native, Envoy, Kubernetes, Microservices, and Service Mesh.


  Open Service Mesh''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Open Service Mesh Plans Pricing
  plan_count: 3
  slug: open-service-mesh-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Open Service Mesh Rate Limits
  slug: open-service-mesh-rate-limits
score:
  band: emerging
  composite: 21.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 21.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-service-mesh/refs/heads/main/screenshots/open-service-mesh-2026-06-20T190850.png
security:
- kind: domain-security
  name: Open Service Mesh Domain Security
  slug: open-service-mesh-domain-security
  summary_line: TLSv1.3 · HSTS
slug: open-service-mesh
tags:
- Cloud Native
- Envoy
- Kubernetes
- Microservices
- Service Mesh
- SMI
website: https://openservicemesh.io
---
