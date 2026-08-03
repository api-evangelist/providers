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
api_count: 6
apis:
- description: Mirantis enterprise Kubernetes and container platform overview, indexing product, documentation, and developer resources.
  name: Mirantis
  slug: mirantis
- description: Mirantis Kubernetes Engine (MKE) is an enterprise container orchestration platform that delivers production-ready Kubernetes for hybrid and multi-cloud environments.
  name: Mirantis Kubernetes Engine
  slug: mke
- description: k0rdent is a composable Kubernetes management platform for centrally provisioning, observing, and securing fleets of clusters across clouds and edge.
  name: Mirantis k0rdent
  slug: k0rdent
- description: k0s is a single-binary, lightweight, certified Kubernetes distribution that runs on any infrastructure from cloud to edge.
  name: k0s
  slug: k0s
- description: MOSK delivers OpenStack on top of Kubernetes for cloud and telco workloads.
  name: Mirantis OpenStack for Kubernetes
  slug: mosk
- description: Lens is a Kubernetes IDE for managing, observing, and troubleshooting clusters.
  name: Lens Desktop
  slug: lens
artifact_total: 11
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mirantis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mirantis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mirantis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mirantis.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mirantis.com/blog/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Mirantis
- group: operate
  title: ''
  type: Support
  url: https://www.mirantis.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mirantis.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://www.mirantis.com/company/careers/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/MirantisIT
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mirantis
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/mirantisinc
created: '2026-03-26'
description: Mirantis provides enterprise Kubernetes and container platform solutions for multi-cloud, hybrid-cloud, and edge deployments. Its product line includes Mirantis Kubernetes Engine (MKE), k0rdent Enterprise, Mirantis OpenStack for Kubernetes (MOSK), Mirantis Container Runtime, Mirantis Secure Registry, Lens Desktop, and the open source k0s Kubernetes distribution and k0smotron orchestrator.
finops:
- name: Mirantis Finops
  service_category: API
  slug: mirantis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mirantis.png
layout: provider
modified: '2026-04-28'
name: Mirantis
nav: Providers
network: true
overview: 'Mirantis publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Kubernetes, Containers, Cloud, DevOps, and OpenStack.


  Mirantis'' developer surface includes documentation, engineering blog, GitHub presence, support, pricing, YouTube channel, and 6 more developer resources.'
plans:
- name: Mirantis Plans Pricing
  plan_count: 3
  slug: mirantis-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Mirantis Rate Limits
  slug: mirantis-rate-limits
score:
  band: emerging
  composite: 24.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 24.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mirantis/refs/heads/main/screenshots/mirantis-2026-06-20T185609.png
security:
- kind: domain-security
  name: Mirantis Domain Security
  slug: mirantis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mirantis Vulnerability Disclosure
  slug: mirantis-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mirantis
tags:
- Kubernetes
- Containers
- Cloud
- DevOps
- OpenStack
website: https://www.mirantis.com/
---
