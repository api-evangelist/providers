---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/switch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://livekick.com
created: '2026-07-17'
description: Switch (operating as Livekick at livekick.com) is a 500 Global-backed company running a virtual fitness and yoga SaaS platform. The Livekick Serve product lets movement teachers and wellness creators deliver live and on-demand classes, videos, courses, and programs to students and communities, with subscription billing and creator tooling to grow an online audience. The public surface is a consumer/creator web and mobile application backed by an internal Django REST API; as of this enrichment pass Livekick publishes no public developer program — no developer portal, documentation, OpenAPI specification, SDKs, MCP server, or security.txt (all /.well-known and /llms.txt paths return the single-page-app shell). This profile is therefore identity-only, enriched with a probed domain-security posture rather than API artifacts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/switch.png
layout: provider
modified: '2026-07-21'
name: Switch
nav: Providers
network: true
overview: Switch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fitness, Yoga, Wellness, and Virtual Classes.
random_paper: 46
score:
  band: minimal
  composite: 7.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Switch Domain Security
  slug: switch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: switch
tags:
- Company
- Fitness
- Yoga
- Wellness
- Virtual Classes
- Creator Platform
- SaaS
- Health
website: https://livekick.com
---
