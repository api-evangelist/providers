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
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: KubeVela uses Kubernetes CRDs to define applications using the Open Application Model. The Application resource combines components (workload definitions), traits (operational capabilities like scalin
  name: KubeVela Application API
  slug: kubevela-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kubevela-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://kubevela.io/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/kubevela/kubevela
- group: company
  title: ''
  type: Blog
  url: https://kubevela.io/blog/rss.xml
created: '2026-03-16'
description: KubeVela is a CNCF incubating application delivery and management platform that makes deploying and operating applications across hybrid and multi-cloud environments easier. Built on the Open Application Model (OAM), it provides a higher-level abstraction for defining applications with components, traits, and policies. KubeVela supports workflow-based delivery pipelines and multi-cluster deployment.
finops:
- name: Kubevela Finops
  service_category: API
  slug: kubevela-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kubevela.png
layout: provider
modified: '2026-04-28'
name: KubeVela
nav: Providers
network: true
overview: 'KubeVela publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Application Delivery, Cloud Native, Incubating, Kubernetes, and Multi-Cloud.


  KubeVela''s developer surface includes documentation, engineering blog, and 2 more developer resources.'
plans:
- name: Kubevela Plans Pricing
  plan_count: 3
  slug: kubevela-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 5
  name: Kubevela Rate Limits
  slug: kubevela-rate-limits
score:
  band: emerging
  composite: 13.7
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 13.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kubevela/refs/heads/main/screenshots/kubevela-2026-06-20T184209.png
security:
- kind: domain-security
  name: Kubevela Domain Security
  slug: kubevela-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kubevela
tags:
- Application Delivery
- Cloud Native
- Incubating
- Kubernetes
- Multi-Cloud
- OAM
website: https://kubevela.io
---
