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
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Karmada extends the Kubernetes API with custom resources for multi-cluster management including PropagationPolicy for distributing resources across clusters, OverridePolicy for cluster-specific custom
  name: Karmada Multi-Cluster API
  slug: karmada-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/karmada-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://karmada.io/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/karmada-io/karmada
- group: company
  title: ''
  type: Blog
  url: https://karmada.io/blog/rss.xml
created: '2026-03-16'
description: Karmada is a CNCF incubating Kubernetes management system that enables running applications across multiple Kubernetes clusters and clouds. It provides a unified control plane for multi-cluster scheduling, failover, and traffic management. Karmada uses Kubernetes-native APIs and supports propagation policies, override policies, and federated resource management.
finops:
- name: Karmada Finops
  service_category: API
  slug: karmada-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/karmada.png
layout: provider
modified: '2026-03-16'
name: Karmada
nav: Providers
network: true
overview: 'Karmada publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Native, Federation, Incubating, Kubernetes, and Multi-Cluster.


  Karmada''s developer surface includes documentation, engineering blog, and 2 more developer resources.'
plans:
- name: Karmada Plans Pricing
  plan_count: 3
  slug: karmada-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Karmada Rate Limits
  slug: karmada-rate-limits
score:
  band: emerging
  composite: 21.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/karmada/refs/heads/main/screenshots/karmada-2026-06-20T183921.png
security:
- kind: domain-security
  name: Karmada Domain Security
  slug: karmada-domain-security
  summary_line: TLSv1.3 · HSTS
slug: karmada
tags:
- Cloud Native
- Federation
- Incubating
- Kubernetes
- Multi-Cluster
- Scheduling
website: https://karmada.io
---
