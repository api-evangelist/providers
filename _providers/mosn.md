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
- description: MOSN is a cloud-native network proxy that supports multiple protocols (HTTP/1.1, HTTP/2, gRPC), dynamic routing, load balancing, observability via Prometheus metrics, TLS, and WASM-based custom extens
  name: MOSN
  slug: mosn
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mosn-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://mosn.io/index.xml
created: '2026-04-28'
description: MOSN (Modular Open Smart Network) is a cloud-native network proxy written in Go, open-sourced by Ant Group. It serves as a Service Mesh data plane and can function as L4/L7 load balancer, API gateway, and cloud-native ingress, with multi-protocol support including HTTP/1.1, HTTP/2, and gRPC.
finops:
- name: Mosn Finops
  service_category: API
  slug: mosn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mosn.png
layout: provider
modified: '2026-04-28'
name: MOSN
nav: Providers
network: true
overview: 'MOSN publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Service Mesh, Proxy, API Gateway, Cloud Native, and Open Source.


  MOSN''s developer surface includes engineering blog and 1 more developer resources.'
plans:
- name: Mosn Plans Pricing
  plan_count: 3
  slug: mosn-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 5
  name: Mosn Rate Limits
  slug: mosn-rate-limits
score:
  band: emerging
  composite: 18.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 18.4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mosn/refs/heads/main/screenshots/mosn-2026-06-20T185820.png
security:
- kind: domain-security
  name: Mosn Domain Security
  slug: mosn-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: mosn
tags:
- Service Mesh
- Proxy
- API Gateway
- Cloud Native
- Open Source
---
