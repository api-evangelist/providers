---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 22
  human_in_the_loop: 1
  name: Yodeck Signage Agentic Access
  operation_count: 36
  slug: yodeck-signage-agentic-access
  summary_line: 36 operations · 22 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Multi-zone screen layouts that split a display into regions.
  name: Yodeck Layouts API
  slug: yodeck-signage-layouts-api
- description: Images, videos, documents, web pages, and app content assets.
  name: Yodeck Media API
  slug: yodeck-signage-media-api
- description: Ordered sequences of media with per-item duration and transitions.
  name: Yodeck Playlists API
  slug: yodeck-signage-playlists-api
- description: Time-based rules controlling what plays where and when.
  name: Yodeck Schedules API
  slug: yodeck-signage-schedules-api
- description: Screens (monitors/players), their status, and remote control.
  name: Yodeck Screens API
  slug: yodeck-signage-screens-api
- description: Reusable groupings of media, playlists, and layouts.
  name: Yodeck Shows API
  slug: yodeck-signage-shows-api
- description: Separate environments with their own users, permissions, and content.
  name: Yodeck Workspaces API
  slug: yodeck-signage-workspaces-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Yodeck REST API (Modeled) Layouts API
  slug: open-yodeck-signage-layouts-api
- collection_type: open
  name: Yodeck REST API (Modeled) Layouts Media API
  slug: open-yodeck-signage-media-api
- collection_type: open
  name: Yodeck REST API (Modeled) Layouts Playlists API
  slug: open-yodeck-signage-playlists-api
- collection_type: open
  name: Yodeck REST API (Modeled) Layouts Schedules API
  slug: open-yodeck-signage-schedules-api
- collection_type: open
  name: Yodeck REST API (Modeled) Layouts Screens API
  slug: open-yodeck-signage-screens-api
- collection_type: open
  name: Yodeck REST API (Modeled) Layouts Shows API
  slug: open-yodeck-signage-shows-api
- collection_type: open
  name: Yodeck REST API (Modeled) Layouts Workspaces API
  slug: open-yodeck-signage-workspaces-api
- collection_type: open
  name: Yodeck REST API (Modeled)
  slug: open-yodeck-signage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yodeck-signage-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yodeck-signage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yodeck-signage-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.yodeck.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yodeck
- group: docs
  title: ''
  type: Documentation
  url: https://www.yodeck.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://app.yodeck.com/api-docs/
- group: start
  title: ''
  type: SignUp
  url: https://app.yodeck.com/signup/
- group: commercial
  title: ''
  type: Plans
  url: plans/yodeck-signage-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yodeck-signage-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yodeck-signage-finops.yml
created: '2026-07-05'
description: Yodeck is a cloud-based digital signage platform for managing screens and content at scale, typically on Raspberry Pi based players. It lets teams upload and organize media, build playlists and multi-zone layouts, schedule content, group shows, and monitor and control players remotely. Alongside the web app, Yodeck publishes a REST API (documented at app.yodeck.com/api-docs and available to Premium and Enterprise plans) that programmatically manages media, playlists, layouts, screens/monitors, schedules, shows, and workspaces using named, role-scoped API tokens. Players also expose a local-only Player HTTP API for on-device apps. The public REST reference is behind an account login, so the API surface documented here is modeled from Yodeck's published resource set rather than copied from live spec files.
finops:
- name: Yodeck Signage Finops
  service_category: Digital Signage and Screen Management
  slug: yodeck-signage-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yodeck-signage.png
layout: provider
modified: '2026-07-05'
name: Yodeck
nav: Providers
network: true
overview: 'Yodeck publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Layouts API, Media API, Playlists API, and 4 more. Tagged areas include Digital Signage, Screen Management, Content Management, Media, and Playlists.


  Yodeck''s developer surface includes authentication, documentation, API reference, signup flow, and 7 more developer resources.'
plans:
- name: Yodeck Signage Plans Pricing
  plan_count: 4
  slug: yodeck-signage-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 3
  name: Yodeck Signage Rate Limits
  slug: yodeck-signage-rate-limits
score:
  band: thin
  composite: 40.8
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 54.2
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Yodeck Signage Authentication
  slug: yodeck-signage-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Yodeck Signage Domain Security
  slug: yodeck-signage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yodeck-signage
tags:
- Digital Signage
- Screen Management
- Content Management
- Media
- Playlists
- Scheduling
- Raspberry Pi
website: https://www.yodeck.com
---
