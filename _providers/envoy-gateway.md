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
- description: Envoy Gateway provides an expressive, extensible, role-oriented API for Kubernetes gateway management built on Envoy Proxy. Configuration is done through Kubernetes Gateway API resources (Gateway, Gat
  name: Envoy Gateway
  slug: envoy-gateway
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/envoy-gateway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gateway.envoyproxy.io/
- group: docs
  title: ''
  type: Documentation
  url: https://gateway.envoyproxy.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/envoyproxy
- group: build
  title: ''
  type: Source Code
  url: https://github.com/envoyproxy/gateway
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/envoyproxy/gateway/releases
- group: operate
  title: ''
  type: Slack
  url: https://envoyproxy.slack.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://envoyproxy.slack.com/llms.txt
created: '2026-03-27'
description: Envoy Gateway is a CNCF project providing a Kubernetes-native API gateway built on Envoy Proxy, implementing the Kubernetes Gateway API for simplified traffic management and ingress control. Envoy Gateway exposes its functionality through Kubernetes Gateway API resources and Custom Resource Definitions rather than a traditional REST API.
finops:
- name: Envoy Gateway Finops
  service_category: API
  slug: envoy-gateway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/envoy-gateway.png
layout: provider
modified: '2026-04-28'
name: Envoy Gateway
nav: Providers
network: true
overview: 'Envoy Gateway publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Gateway, CNCF, Envoy, Kubernetes, and Open Source.


  Envoy Gateway''s developer surface includes documentation, release notes, and 6 more developer resources.'
plans:
- name: Envoy Gateway Plans Pricing
  plan_count: 3
  slug: envoy-gateway-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 5
  name: Envoy Gateway Rate Limits
  slug: envoy-gateway-rate-limits
score:
  band: emerging
  composite: 22.4
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 24.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/envoy-gateway/refs/heads/main/screenshots/envoy-gateway-2026-06-20T180742.png
security:
- kind: domain-security
  name: Envoy Gateway Domain Security
  slug: envoy-gateway-domain-security
  summary_line: TLSv1.3 · HSTS
slug: envoy-gateway
tags:
- API Gateway
- CNCF
- Envoy
- Kubernetes
- Open Source
website: https://gateway.envoyproxy.io/
---
