---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
- description: Implements the Pusher protocol (channels, private channels, presence channels, encrypted channels) for drop-in compatibility with Pusher client SDKs. Server-side publish via REST, client-side subscrib
  name: Soketi Pusher-Compatible API
  slug: pusher-compatible-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/soketi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soketi-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/soketi
- group: start
  title: ''
  type: Portal
  url: https://soketi.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.soketi.app/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/soketi/soketi
- group: commercial
  title: ''
  type: License
  url: https://github.com/soketi/soketi/blob/master/LICENSE
- group: commercial
  title: ''
  type: Plans
  url: plans/soketi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/soketi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/soketi-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.soketi.app/llms.txt
created: '2026-05-08'
description: Soketi is a next-gen, Pusher-compatible, open-source WebSocket server. It implements the Pusher protocol so existing Pusher SDKs and applications can drop-in replace Pusher Channels with self-hosted Soketi. Written in Node/TypeScript with Rust adapter; deployed via npm, Docker, Kubernetes, or systemd. Open source under MIT license.
finops:
- name: Soketi Finops
  service_category: Realtime Infrastructure
  slug: soketi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soketi.png
layout: provider
modified: '2026-05-08'
name: Soketi
nav: Providers
network: true
overview: 'Soketi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Realtime, WebSockets, Open Source, Pusher Protocol, and Self-Host.


  Soketi''s developer surface includes developer portal, documentation, GitHub presence, and 8 more developer resources.'
plans:
- name: Soketi Plans Pricing
  plan_count: 1
  slug: soketi-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 3
  name: Soketi Rate Limits
  slug: soketi-rate-limits
score:
  band: emerging
  composite: 20.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 20.9
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soketi/refs/heads/main/screenshots/soketi-2026-06-20T194139.png
security:
- kind: domain-security
  name: Soketi Domain Security
  slug: soketi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Soketi Vulnerability Disclosure
  slug: soketi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: soketi
tags:
- Realtime
- WebSockets
- Open Source
- Pusher Protocol
- Self-Host
- Drop-in
website: https://soketi.app/
---
