---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://dyte.io/'', ''status'': 302, ''note'': ''declared website redirects to https://www.cloudflare.com/products/realtime/ — a different registrable domain (dyte.io -> cloudflare.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 13
  human_in_the_loop: 2
  name: Dyte Agentic Access
  operation_count: 27
  slug: dyte-agentic-access
  summary_line: 27 operations · 13 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.dyte.io/v2
  baseurl_source: declared
  description: Manage livestreams for a meeting.
  name: Dyte Livestreams API
  slug: dyte-livestreams-api
- baseURL: https://api.dyte.io/v2
  baseurl_source: declared
  description: Create and manage meeting rooms.
  name: Dyte Meetings API
  slug: dyte-meetings-api
- baseURL: https://api.dyte.io/v2
  baseurl_source: declared
  description: Add participants and issue/refresh their SDK auth tokens.
  name: Dyte Participants API
  slug: dyte-participants-api
- baseURL: https://api.dyte.io/v2
  baseurl_source: declared
  description: Start, stop, and fetch meeting recordings.
  name: Dyte Recordings API
  slug: dyte-recordings-api
- baseURL: https://api.dyte.io/v2
  baseurl_source: declared
  description: Query completed and active sessions.
  name: Dyte Sessions API
  slug: dyte-sessions-api
- baseURL: https://api.dyte.io/v2
  baseurl_source: declared
  description: Manage webhook event subscriptions.
  name: Dyte Webhooks API
  slug: dyte-webhooks-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dyte v2 REST Livestreams API
  slug: open-dyte-livestreams-api
- collection_type: open
  name: Dyte v2 REST Livestreams Meetings API
  slug: open-dyte-meetings-api
- collection_type: open
  name: Dyte v2 REST Livestreams Participants API
  slug: open-dyte-participants-api
- collection_type: open
  name: Dyte v2 REST Livestreams Recordings API
  slug: open-dyte-recordings-api
- collection_type: open
  name: Dyte v2 REST Livestreams Sessions API
  slug: open-dyte-sessions-api
- collection_type: open
  name: Dyte v2 REST Livestreams Webhooks API
  slug: open-dyte-webhooks-api
- collection_type: open
  name: Dyte v2 REST API
  slug: open-dyte
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cloudflare/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dyte-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dyte-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dyte-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dyte-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dyteio
- group: company
  title: ''
  type: Website
  url: https://dyte.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dyte.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/dyte-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dyte-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dyte-finops.yml
created: '2026-06-20'
description: Dyte is a live video and voice developer platform offering client SDKs plus a v2 REST API for programmatically creating meetings, adding participants and issuing their auth tokens, querying completed sessions, and managing recordings, livestreams, and webhooks. Dyte was acquired by Cloudflare in 2025 and is transitioning into Cloudflare RealtimeKit; the Dyte SDKs and APIs are in maintenance mode.
finops:
- name: Dyte Finops
  service_category: Communications and Real-Time Media
  slug: dyte-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dyte.png
layout: provider
modified: '2026-06-20'
name: Dyte
nav: Providers
network: true
overview: 'Dyte publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Livestreams API, Meetings API, Participants API, and 3 more. Tagged areas include Video, Voice, Real-Time, WebRTC, and SDK.


  Dyte''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Dyte Plans Pricing
  plan_count: 3
  slug: dyte-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Dyte Rate Limits
  slug: dyte-rate-limits
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.9
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dyte/refs/heads/main/screenshots/dyte-2026-06-20T180436.png
security:
- kind: authentication
  name: Dyte Authentication
  slug: dyte-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dyte Domain Security
  slug: dyte-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dyte
tags:
- Video
- Voice
- Real-Time
- WebRTC
- SDK
- Communications
website: https://dyte.io/
---
