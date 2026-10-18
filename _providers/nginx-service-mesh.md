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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The NGINX Service Mesh control plane exposes a REST API used by the `nginx-meshctl` CLI to manage mesh configuration, sidecar injection, certificate authority operations, traffic policies, and resourc
  name: NGINX Service Mesh Control Plane API
  slug: control-plane-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/nginx-service-mesh/refs/heads/main/plans/nginx-service-mesh-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nginx-service-mesh-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/nginx-service-mesh/refs/heads/main/rate-limits/nginx-service-mesh-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nginx-service-mesh-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/nginx-service-mesh/refs/heads/main/finops/nginx-service-mesh-finops.yml
  title: ''
  type: FinOps
  url: finops/nginx-service-mesh-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nginx-service-mesh/refs/heads/main/security/nginx-service-mesh-domain-security.yml
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
- has_sources: false
  method: generated
  name: Nginx Service Mesh Finops
  primary_unit: ''
  service_category: API
  slug: nginx-service-mesh-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nginx-service-mesh.png
layout: provider
modified: '2026-04-28'
name: NGINX Service Mesh
nav: Providers
network: true
overview: 'NGINX Service Mesh is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Container Networking, End of Sale, F5, Kubernetes, and mTLS.


  NGINX Service Mesh''s developer surface includes documentation, getting-started guide, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Nginx Service Mesh Plans Pricing
  plan_count: 3
  slug: nginx-service-mesh-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Nginx Service Mesh Rate Limits
  slug: nginx-service-mesh-rate-limits
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 64.3
    operational_transparency: 13.2
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
