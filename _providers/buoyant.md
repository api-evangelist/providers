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
api_count: 2
apis:
- description: Linkerd is a CNCF-graduated service mesh for Kubernetes that transparently adds mutual TLS encryption, latency-aware load balancing, retries, timeouts, circuit breaking, and observability to any Kuber
  name: Linkerd Service Mesh
  slug: linkerd
- description: Buoyant Enterprise Linkerd is the enterprise-supported distribution of Linkerd with additional features including FIPS-validated cryptography, lifecycle automation, multi-cluster networking, and enter
  name: Buoyant Enterprise Linkerd (BEL)
  slug: buoyant-enterprise-linkerd
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buoyant-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/buoyantio
- group: start
  title: ''
  type: Portal
  url: https://buoyant.io/
- group: docs
  title: ''
  type: Documentation
  url: https://linkerd.io/2.x/overview/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linkerd
- group: company
  title: ''
  type: Blog
  url: https://buoyant.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://buoyant.io/pricing/
- group: operate
  title: ''
  type: Slack
  url: https://slack.linkerd.io/
- group: operate
  title: ''
  type: Community
  url: https://linkerd.io/community/
created: '2026-01-02'
description: Buoyant is the creator of Linkerd, the CNCF-graduated service mesh for Kubernetes. Linkerd provides zero-trust security via mutual TLS, ultra-high availability with automated failover, and observability for microservices including AI/LLM workloads. Buoyant Enterprise Linkerd adds enterprise features including FIPS 140-2/140-3 validated encryption and multi-cluster support.
finops:
- name: Buoyant Finops
  service_category: API
  slug: buoyant-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/buoyant.png
layout: provider
modified: '2026-04-21'
name: Buoyant
nav: Providers
network: true
overview: 'Buoyant publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Observability, Kubernetes, Linkerd, mTLS, and Observability.


  Buoyant''s developer surface includes developer portal, documentation, engineering blog, pricing, and 5 more developer resources.'
plans:
- name: Buoyant Plans Pricing
  plan_count: 3
  slug: buoyant-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 5
  name: Buoyant Rate Limits
  slug: buoyant-rate-limits
score:
  band: emerging
  composite: 25.5
  delta: -2.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 27.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/buoyant/refs/heads/main/screenshots/buoyant-2026-06-20T173802.png
security:
- kind: domain-security
  name: Buoyant Domain Security
  slug: buoyant-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: buoyant
tags:
- AI Observability
- Kubernetes
- Linkerd
- mTLS
- Observability
- Service Mesh
- Zero Trust
website: https://buoyant.io/
---
