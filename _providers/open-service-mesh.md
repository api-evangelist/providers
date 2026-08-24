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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'Service mesh control plane for Kubernetes that implements the Service Mesh Interface (SMI) specification, providing traffic management, security, and observability for microservices via Envoy sidecar '
  name: Open Service Mesh
  slug: open-service-mesh
artifact_total: 5
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/openservicemesh/osm/blob/main/LICENSE
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
overview: 'Open Service Mesh publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud-Native, Envoy, Kubernetes, Microservices, and Service Mesh.


  Open Service Mesh''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Open Service Mesh Plans Pricing
  plan_count: 3
  slug: open-service-mesh-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Open Service Mesh Rate Limits
  slug: open-service-mesh-rate-limits
score:
  band: emerging
  composite: 12.0
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 12.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-service-mesh/refs/heads/main/screenshots/open-service-mesh-2026-06-20T190850.png
security:
- kind: domain-security
  name: Open Service Mesh Domain Security
  slug: open-service-mesh-domain-security
  summary_line: TLSv1.3 · HSTS
slug: open-service-mesh
tags:
- Cloud-Native
- Envoy
- Kubernetes
- Microservices
- Service Mesh
- SMI
website: https://openservicemesh.io
---
