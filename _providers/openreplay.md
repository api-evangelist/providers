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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Openreplay Agentic Access
  operation_count: 13
  slug: openreplay-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 6
apis:
- description: Retrieve live Assist sessions (Enterprise Edition only).
  name: OpenReplay Assist API
  slug: openreplay-assist-api
- description: Retrieve events captured within a recorded session.
  name: OpenReplay Events API
  slug: openreplay-events-api
- description: Manage background jobs such as user-deletion tasks.
  name: OpenReplay Jobs API
  slug: openreplay-jobs-api
- description: Create and retrieve projects.
  name: OpenReplay Projects API
  slug: openreplay-projects-api
- description: Retrieve recorded sessions for a given user.
  name: OpenReplay Sessions API
  slug: openreplay-sessions-api
- description: Search, retrieve, and delete users and their associated data.
  name: OpenReplay Users API
  slug: openreplay-users-api
artifact_total: 13
collections:
- collection_type: open
  name: OpenReplay API
  slug: open-openreplay
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openreplay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openreplay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openreplay-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openreplay
- group: company
  title: ''
  type: Website
  url: https://openreplay.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openreplay.com
- group: company
  title: ''
  type: Blog
  url: https://blog.openreplay.com
- group: commercial
  title: ''
  type: Pricing
  url: https://openreplay.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/openreplay/openreplay
- group: start
  title: ''
  type: Login
  url: https://app.openreplay.com
- group: start
  title: ''
  type: Signup
  url: https://app.openreplay.com/signup
- group: other
  title: ''
  type: SelfHosting
  url: https://docs.openreplay.com/deployment
- group: operate
  title: ''
  type: Support
  url: https://openreplay.com/support
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.openreplay.com/llms.txt
created: '2026-03-26'
description: OpenReplay is an open source session replay and product analytics platform that helps developers debug web applications by recording and replaying user sessions, tracking errors, and monitoring performance.
finops:
- name: Openreplay Finops
  service_category: API
  slug: openreplay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openreplay.png
layout: provider
modified: '2026-05-19'
name: OpenReplay
nav: Providers
network: true
overview: 'OpenReplay publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Assist API, Events API, Jobs API, and 3 more. Tagged areas include Debugging, Error Tracking, Open Source, Performance Monitoring, and Session Replay.


  OpenReplay''s developer surface includes authentication, documentation, engineering blog, pricing, GitHub presence, signup flow, support, and 7 more developer resources.'
plans:
- name: Openreplay Plans Pricing
  plan_count: 3
  slug: openreplay-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Openreplay Rate Limits
  slug: openreplay-rate-limits
score:
  band: thin
  composite: 38.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.7
    developer_ergonomics: 26.1
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openreplay/refs/heads/main/screenshots/openreplay-2026-06-20T191026.png
security:
- kind: authentication
  name: Openreplay Authentication
  slug: openreplay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openreplay Domain Security
  slug: openreplay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openreplay
tags:
- Debugging
- Error Tracking
- Open Source
- Performance Monitoring
- Session Replay
- User Behavior
website: https://openreplay.com
---
