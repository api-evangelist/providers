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
- description: Koordinator QoS-based scheduling system for hybrid workloads on Kubernetes with colocation and resource optimization.
  name: Koordinator
  slug: koordinator
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/koordinator-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://koordinator.sh
- group: docs
  title: ''
  type: Documentation
  url: https://koordinator.sh/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/koordinator-sh/koordinator
- group: company
  title: ''
  type: Blog
  url: https://koordinator.sh/blog/rss.xml
created: '2025-01-01'
description: Koordinator is a QoS-based scheduling system for hybrid workloads orchestration on Kubernetes, providing colocation, interference detection, and resource optimization capabilities to improve cluster utilization.
finops:
- name: Koordinator Finops
  service_category: API
  slug: koordinator-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/koordinator.png
layout: provider
modified: '2026-04-28'
name: Koordinator
nav: Providers
network: true
overview: 'Koordinator publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Kubernetes, QoS, Resource Management, Scheduling, and Workload Orchestration.


  Koordinator''s developer surface includes documentation, engineering blog, and 3 more developer resources.'
plans:
- name: Koordinator Plans Pricing
  plan_count: 3
  slug: koordinator-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Koordinator Rate Limits
  slug: koordinator-rate-limits
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/koordinator/refs/heads/main/screenshots/koordinator-2026-06-20T184138.png
security:
- kind: domain-security
  name: Koordinator Domain Security
  slug: koordinator-domain-security
  summary_line: TLSv1.3 · HSTS
slug: koordinator
tags:
- Kubernetes
- QoS
- Resource Management
- Scheduling
- Workload Orchestration
website: https://koordinator.sh
---
