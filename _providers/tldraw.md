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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
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
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/tldraw/tldraw/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/tldraw/tldraw/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/tldraw/tldraw/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/tldraw/tldraw/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/tldraw/tldraw/blob/main/CONTRIBUTING.md
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


  tldraw''s developer surface includes developer portal, engineering blog, and 14 more developer resources.'
plans:
- name: Tldraw Plans Pricing
  plan_count: 1
  slug: tldraw-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Tldraw Rate Limits
  slug: tldraw-rate-limits
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 27.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
