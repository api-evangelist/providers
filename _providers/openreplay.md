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
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Openreplay Agentic Access
  operation_count: 13
  slug: openreplay-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.openreplay.com/v2
  baseurl_source: declared
  description: Retrieve live Assist sessions (Enterprise Edition only).
  name: OpenReplay Assist API
  slug: openreplay-assist-api
- baseURL: https://api.openreplay.com/v2
  baseurl_source: declared
  description: Retrieve events captured within a recorded session.
  name: OpenReplay Events API
  slug: openreplay-events-api
- baseURL: https://api.openreplay.com/v2
  baseurl_source: declared
  description: Manage background jobs such as user-deletion tasks.
  name: OpenReplay Jobs API
  slug: openreplay-jobs-api
- baseURL: https://api.openreplay.com/v2
  baseurl_source: declared
  description: Create and retrieve projects.
  name: OpenReplay Projects API
  slug: openreplay-projects-api
- baseURL: https://api.openreplay.com/v2
  baseurl_source: declared
  description: Retrieve recorded sessions for a given user.
  name: OpenReplay Sessions API
  slug: openreplay-sessions-api
- baseURL: https://api.openreplay.com/v2
  baseurl_source: declared
  description: Search, retrieve, and delete users and their associated data.
  name: OpenReplay Users API
  slug: openreplay-users-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenReplay Assist API
  slug: open-openreplay-assist-api
- collection_type: open
  name: OpenReplay Assist Events API
  slug: open-openreplay-events-api
- collection_type: open
  name: OpenReplay Assist Jobs API
  slug: open-openreplay-jobs-api
- collection_type: open
  name: OpenReplay Assist Projects API
  slug: open-openreplay-projects-api
- collection_type: open
  name: OpenReplay Assist Sessions API
  slug: open-openreplay-sessions-api
- collection_type: open
  name: OpenReplay Assist Users API
  slug: open-openreplay-users-api
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
overview: 'OpenReplay publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Assist API, Events API, Jobs API, and 3 more. Tagged areas include Debugging, Error Tracking, Open-Source, Performance Monitoring, and Session Replay.


  OpenReplay''s developer surface includes authentication, documentation, engineering blog, pricing, GitHub presence, signup flow, support, and 7 more developer resources.'
plans:
- name: Openreplay Plans Pricing
  plan_count: 3
  slug: openreplay-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Openreplay Rate Limits
  slug: openreplay-rate-limits
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 56.0
    developer_ergonomics: 32.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Open-Source
- Performance Monitoring
- Session Replay
- User Behavior
website: https://openreplay.com
---
