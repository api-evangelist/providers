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
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: The tldraw SDK is a React component library for embedding an infinite canvas with drawing tools, shapes, text, arrows, selection, accessibility, and theming. Used in production by Google, Shopify, Cli
  name: tldraw React SDK
  slug: tldraw-sdk
- description: tldraw provides a multiplayer sync layer (WebSocket-based) that customers can self-host or use through tldraw's offerings. Live cursors, real-time updates, persistence.
  name: tldraw Sync (Multiplayer)
  slug: tldraw-sync
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tldraw-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tldraw
- group: company
  title: ''
  type: Website
  url: https://www.tldraw.com/
- group: start
  title: ''
  type: Portal
  url: https://tldraw.dev/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/tldraw/tldraw
- group: commercial
  title: tldraw SDK License
  type: License
  url: https://github.com/tldraw/tldraw/blob/main/LICENSE.md
- group: commercial
  title: ''
  type: Plans
  url: plans/tldraw-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tldraw-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tldraw-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://tldraw.dev/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://tldraw.substack.com/feed
created: '2026-05-08'
description: tldraw is an infinite-canvas SDK for building whiteboard and canvas applications. The primary distribution is the `tldraw` React component package; tldraw also offers a multiplayer sync server. License is the tldraw SDK License (free with watermark for small businesses; paid commercial license to remove watermark).
finops:
- name: Tldraw Finops
  service_category: Collaboration
  slug: tldraw-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tldraw.png
layout: provider
modified: '2026-05-08'
name: tldraw
nav: Providers
network: true
overview: 'tldraw publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Whiteboard, SDK, Canvas, React, and Multiplayer.


  tldraw''s developer surface includes developer portal, engineering blog, and 9 more developer resources.'
plans:
- name: Tldraw Plans Pricing
  plan_count: 1
  slug: tldraw-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 1
  name: Tldraw Rate Limits
  slug: tldraw-rate-limits
score:
  band: emerging
  composite: 13.1
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 13.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tldraw/refs/heads/main/screenshots/tldraw-2026-06-20T195423.png
security:
- kind: domain-security
  name: Tldraw Domain Security
  slug: tldraw-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tldraw
tags:
- Whiteboard
- SDK
- Canvas
- React
- Multiplayer
website: https://www.tldraw.com/
---
