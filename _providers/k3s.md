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
- description: K3s lightweight Kubernetes distribution with built-in containerd, Flannel networking, and Traefik ingress controller.
  name: K3s
  slug: k3s
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/k3s/refs/heads/main/plans/k3s-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/k3s-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/k3s/refs/heads/main/rate-limits/k3s-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/k3s-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/k3s/refs/heads/main/finops/k3s-finops.yml
  title: ''
  type: FinOps
  url: finops/k3s-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://docs.k3s.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://docs.k3s.io/blog/rss.xml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/k3s/refs/heads/main/security/k3s-domain-security.yml
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
- has_sources: false
  method: generated
  name: K3S Finops
  primary_unit: ''
  service_category: API
  slug: k3s-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/k3s.png
layout: provider
modified: '2026-10-06'
name: K3s
nav: Providers
network: true
overview: 'K3s is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud-Native, Container Orchestration, DevOps, Edge Computing, and Kubernetes.


  K3s'' developer surface includes engineering blog, documentation, and 8 more developer resources.'
plans:
- name: K3S Plans Pricing
  plan_count: 3
  slug: k3s-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: K3S Rate Limits
  slug: k3s-rate-limits
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 13.1
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
