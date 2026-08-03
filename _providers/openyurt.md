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
- description: OpenYurt extends Kubernetes with CRDs for edge computing including NodePool for grouping edge nodes, YurtAppSet for deploying applications across node pools, YurtAppDaemon for pool-scoped daemon workl
  name: OpenYurt Edge Management API
  slug: openyurt-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openyurt-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://openyurt.io/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/openyurtio/openyurt
- group: company
  title: ''
  type: Blog
  url: https://openyurt.io/blog/rss.xml
created: '2026-03-16'
description: OpenYurt is a CNCF incubating project that extends Kubernetes for edge and cloud-edge collaboration scenarios. It provides node autonomy for edge nodes to continue operating during cloud-edge network disconnections, seamless node conversion between cloud and edge modes, and unified management of edge resources through NodePool and YurtAppSet abstractions.
finops:
- name: Openyurt Finops
  service_category: API
  slug: openyurt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openyurt.png
layout: provider
modified: '2026-04-28'
name: OpenYurt
nav: Providers
network: true
overview: 'OpenYurt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Native, Cloud-Edge, Edge Computing, Incubating, and IoT.


  OpenYurt''s developer surface includes documentation, engineering blog, and 2 more developer resources.'
plans:
- name: Openyurt Plans Pricing
  plan_count: 3
  slug: openyurt-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 5
  name: Openyurt Rate Limits
  slug: openyurt-rate-limits
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
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openyurt/refs/heads/main/screenshots/openyurt-2026-06-20T191055.png
security:
- kind: domain-security
  name: Openyurt Domain Security
  slug: openyurt-domain-security
  summary_line: TLSv1.3 · HSTS
slug: openyurt
tags:
- Cloud Native
- Cloud-Edge
- Edge Computing
- Incubating
- IoT
- Kubernetes
website: https://openyurt.io
---
