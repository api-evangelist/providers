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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: KubeEdge extends the Kubernetes API to manage edge nodes and devices. It includes custom resources for device management, edge application deployment, and node grouping. The EdgeController and DeviceC
  name: KubeEdge Edge API
  slug: kubeedge-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kubeedge-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://kubeedge.io/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/kubeedge/kubeedge
- group: company
  title: ''
  type: Blog
  url: https://kubeedge.io/blog/rss.xml
created: '2026-03-16'
description: KubeEdge is a CNCF graduated project that extends Kubernetes to edge computing. It provides infrastructure support for networking, application deployment, and metadata synchronization between cloud and edge. KubeEdge enables containerized application orchestration at the edge with offline autonomy, ensuring edge nodes continue functioning when disconnected from the cloud.
finops:
- name: Kubeedge Finops
  service_category: API
  slug: kubeedge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kubeedge.png
layout: provider
modified: '2026-04-28'
name: KubeEdge
nav: Providers
network: true
overview: 'KubeEdge publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Native, Edge Computing, Graduated, IoT, and Kubernetes.


  KubeEdge''s developer surface includes documentation, engineering blog, and 2 more developer resources.'
plans:
- name: Kubeedge Plans Pricing
  plan_count: 3
  slug: kubeedge-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Kubeedge Rate Limits
  slug: kubeedge-rate-limits
score:
  band: emerging
  composite: 21.5
  delta: -1.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 22.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kubeedge/refs/heads/main/screenshots/kubeedge-2026-06-20T184204.png
security:
- kind: domain-security
  name: Kubeedge Domain Security
  slug: kubeedge-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kubeedge
tags:
- Cloud Native
- Edge Computing
- Graduated
- IoT
- Kubernetes
website: https://kubeedge.io
---
