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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: K3s lightweight Kubernetes distribution with built-in containerd, Flannel networking, and Traefik ingress controller.
  name: K3s
  slug: k3s
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/k3s-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rancher
- group: company
  title: ''
  type: Website
  url: https://k3s.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.k3s.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/k3s-io/k3s
created: '2025-01-01'
description: K3s is a lightweight Kubernetes distribution designed for resource-constrained environments, edge computing, IoT devices, and CI/CD pipelines. K3s is a fully compliant Kubernetes distribution with a reduced memory footprint and simplified installation.
finops:
- name: K3S Finops
  service_category: API
  slug: k3s-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/k3s.png
layout: provider
modified: '2026-04-28'
name: K3s
nav: Providers
network: true
overview: 'K3s publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud-Native, Container Orchestration, DevOps, Edge Computing, and Kubernetes.


  K3s'' developer surface includes documentation and 4 more developer resources.'
plans:
- name: K3S Plans Pricing
  plan_count: 3
  slug: k3s-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: K3S Rate Limits
  slug: k3s-rate-limits
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 14.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/k3s/refs/heads/main/screenshots/k3s-2026-06-20T183846.png
security:
- kind: domain-security
  name: K3S Domain Security
  slug: k3s-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: k3s
tags:
- Cloud-Native
- Container Orchestration
- DevOps
- Edge Computing
- Kubernetes
website: https://k3s.io/
---
