---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rabbit-r1-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rabbit-inc
- group: company
  title: ''
  type: Website
  url: https://www.rabbit.tech/
- group: other
  title: ''
  type: LAMPlayground
  url: https://www.rabbit.tech/lam-playground
- group: other
  title: ''
  type: rabbitOS
  url: https://www.rabbit.tech/rabbit-os
- group: commercial
  title: ''
  type: Plans
  url: plans/rabbit-r1-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rabbit-r1-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rabbit-r1-finops.yml
created: '2026-05-23'
description: Rabbit is the maker of the R1, a $199 handheld AI device running rabbitOS 2.1 with no subscription required. The R1 ships with Magic Recorder (unlimited recordings, transcripts, AI summaries), Magic Camera, Magic Voice, and DLAM — the Desktop Large Action Model, a plug-and-play controller that carries out tasks across the user's computer OS. Rabbit's Large Action Model is exposed to users via the LAM Playground on rabbit.tech. Industrial design is by Teenage Engineering. Partner integrations (e.g. OpenClaw for voice-activated task automation) are user-configured. No public developer API or SDK is documented; partner / developer access appears to be gated.
finops:
- name: Rabbit R1 Finops
  service_category: API
  slug: rabbit-r1-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rabbit-r1.png
layout: provider
modified: '2026-07-25'
name: Rabbit
nav: Providers
network: true
overview: Rabbit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Hardware, Handheld, Large Action Model, and LAM.
plans:
- name: Rabbit R1 Plans Pricing
  plan_count: 1
  slug: rabbit-r1-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 2
  name: Rabbit R1 Rate Limits
  slug: rabbit-r1-rate-limits
score:
  band: emerging
  composite: 13.5
  delta: -1.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rabbit-r1/refs/heads/main/screenshots/rabbit-r1-2026-06-20T192503.png
security:
- kind: domain-security
  name: Rabbit R1 Domain Security
  slug: rabbit-r1-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rabbit-r1
tags:
- AI
- Hardware
- Handheld
- Large Action Model
- LAM
- Agents
- Consumer
- rabbitOS
- Teenage Engineering
website: https://www.rabbit.tech/
---
