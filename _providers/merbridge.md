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
- description: Merbridge uses eBPF to accelerate service mesh data planes by replacing iptables-based traffic interception and shortening the datapath between sidecars and services. It is a CNCF Sandbox project comp
  name: Merbridge
  slug: merbridge
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/merbridge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://merbridge.io/
- group: docs
  title: ''
  type: Documentation
  url: https://merbridge.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/merbridge
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/merbridge/merbridge
- group: company
  title: ''
  type: Blog
  url: https://merbridge.io/blog/
- group: operate
  title: ''
  type: Slack
  url: https://join.slack.com/t/merbridge/shared_invite/zt-11uc3z0w7-DMyv42eQ6s5YUxO5mZ5hwQ
- group: other
  title: ''
  type: Group
  url: https://groups.google.com/g/merbridge
created: '2026-04-28'
description: Merbridge is an open source, eBPF-based service mesh acceleration tool that replaces iptables rules with eBPF traffic interception and uses msg_redirect to shorten the datapath between sidecars and services. It is a CNCF Sandbox project and supports Istio, Linkerd2, and Kuma.
finops:
- name: Merbridge Finops
  service_category: API
  slug: merbridge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/merbridge.png
layout: provider
modified: '2026-04-28'
name: Merbridge
nav: Providers
network: true
overview: 'Merbridge publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CNCF, eBPF, Networking, Performance, and Service Mesh.


  Merbridge''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Merbridge Plans Pricing
  plan_count: 3
  slug: merbridge-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Merbridge Rate Limits
  slug: merbridge-rate-limits
score:
  band: emerging
  composite: 20.8
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 22.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/merbridge/refs/heads/main/screenshots/merbridge-2026-06-20T185149.png
security:
- kind: domain-security
  name: Merbridge Domain Security
  slug: merbridge-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: merbridge
tags:
- CNCF
- eBPF
- Networking
- Performance
- Service Mesh
website: https://merbridge.io/
---
