---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Accelbyte Agentic Access
  operation_count: 23
  slug: accelbyte-agentic-access
  summary_line: 23 operations · 13 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://demo.accelbyte.io/iam
  baseurl_source: declared
  description: Achievement definitions and player unlocks.
  name: AccelByte Achievement API
  slug: accelbyte-achievement-api
- baseURL: https://demo.accelbyte.io/iam
  baseurl_source: declared
  description: Player profiles and basic user data.
  name: AccelByte Basic API
  slug: accelbyte-basic-api
- baseURL: https://demo.accelbyte.io/iam
  baseurl_source: declared
  description: Player and game record storage.
  name: AccelByte Cloud Save API
  slug: accelbyte-cloud-save-api
- baseURL: https://demo.accelbyte.io/iam
  baseurl_source: declared
  description: Dedicated Server Manager (Armada) fleets and sessions.
  name: AccelByte DSMC API
  slug: accelbyte-dsmc-api
- baseURL: https://demo.accelbyte.io/iam
  baseurl_source: declared
  description: Gameplay and client telemetry ingestion.
  name: AccelByte Game Telemetry API
  slug: accelbyte-game-telemetry-api
- baseURL: https://demo.accelbyte.io/iam
  baseurl_source: declared
  description: Identity and Access Management - OAuth2 tokens, users, roles.
  name: AccelByte IAM API
  slug: accelbyte-iam-api
- baseURL: https://demo.accelbyte.io/iam
  baseurl_source: declared
  description: Ranked leaderboards derived from statistics.
  name: AccelByte Leaderboard API
  slug: accelbyte-leaderboard-api
- baseURL: https://demo.accelbyte.io/iam
  baseurl_source: declared
  description: Matchmaking V2 pools and tickets.
  name: AccelByte Matchmaking API
  slug: accelbyte-matchmaking-api
- baseURL: https://demo.accelbyte.io/iam
  baseurl_source: declared
  description: Commerce - stores, items, entitlements, wallets, orders.
  name: AccelByte Platform API
  slug: accelbyte-platform-api
- baseURL: https://demo.accelbyte.io/iam
  baseurl_source: declared
  description: Seasons, passes, tiers, and rewards.
  name: AccelByte Season Pass API
  slug: accelbyte-season-pass-api
- baseURL: https://demo.accelbyte.io/iam
  baseurl_source: declared
  description: Game sessions and parties (Session V2).
  name: AccelByte Session API
  slug: accelbyte-session-api
- baseURL: https://demo.accelbyte.io/iam
  baseurl_source: declared
  description: Player statistics and configurations.
  name: AccelByte Statistics API
  slug: accelbyte-statistics-api
- baseURL: https://demo.accelbyte.io/iam
  baseurl_source: declared
  description: User-generated content channels and contents.
  name: AccelByte UGC API
  slug: accelbyte-ugc-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AccelByte Gaming Services (AGS) Achievement API
  slug: open-accelbyte-achievement-api
- collection_type: open
  name: AccelByte Gaming Services (AGS) Achievement Basic API
  slug: open-accelbyte-basic-api
- collection_type: open
  name: AccelByte Gaming Services (AGS) Achievement Cloud Save API
  slug: open-accelbyte-cloud-save-api
- collection_type: open
  name: AccelByte Gaming Services (AGS) Achievement DSMC API
  slug: open-accelbyte-dsmc-api
- collection_type: open
  name: AccelByte Gaming Services (AGS) Achievement Game Telemetry API
  slug: open-accelbyte-game-telemetry-api
- collection_type: open
  name: AccelByte Gaming Services (AGS) Achievement IAM API
  slug: open-accelbyte-iam-api
- collection_type: open
  name: AccelByte Gaming Services (AGS) Achievement Leaderboard API
  slug: open-accelbyte-leaderboard-api
- collection_type: open
  name: AccelByte Gaming Services (AGS) Achievement Matchmaking API
  slug: open-accelbyte-matchmaking-api
- collection_type: open
  name: AccelByte Gaming Services (AGS) Achievement Platform API
  slug: open-accelbyte-platform-api
- collection_type: open
  name: AccelByte Gaming Services (AGS) Achievement Season Pass API
  slug: open-accelbyte-season-pass-api
- collection_type: open
  name: AccelByte Gaming Services (AGS) Achievement Session API
  slug: open-accelbyte-session-api
- collection_type: open
  name: AccelByte Gaming Services (AGS) Achievement Statistics API
  slug: open-accelbyte-statistics-api
- collection_type: open
  name: AccelByte Gaming Services (AGS) Achievement UGC API
  slug: open-accelbyte-ugc-api
- collection_type: open
  name: AccelByte Gaming Services (AGS) API
  slug: open-accelbyte
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/accelbyte-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accelbyte-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/accelbyte-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AccelByte
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/accelbyte
- group: company
  title: ''
  type: Website
  url: https://accelbyte.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.accelbyte.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/accelbyte-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/accelbyte-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/accelbyte-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://accelbyte.io/blog/rss.xml
created: '2026-07-01'
description: AccelByte provides AccelByte Gaming Services (AGS), a modular backend platform for live games. Its REST services cover player accounts and IAM, player profiles, cloud save, statistics and leaderboards, matchmaking, lobby and session, commerce and monetization, seasons and battle pass, achievements, dedicated server management (Armada/DSMC), analytics and telemetry, and user-generated content, all secured with OAuth2 client credentials and namespace-scoped IAM.
finops:
- name: Accelbyte Finops
  service_category: Developer Tools and Platform
  slug: accelbyte-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/accelbyte.png
layout: provider
modified: '2026-07-01'
name: AccelByte
nav: Providers
network: true
overview: 'AccelByte publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Achievement API, Basic API, Cloud Save API, and 10 more. Tagged areas include Gaming, Backend, Backend-as-a-Service, Live Services, and Player Accounts.


  AccelByte''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Accelbyte Plans Pricing
  plan_count: 3
  slug: accelbyte-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Accelbyte Rate Limits
  slug: accelbyte-rate-limits
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 49.8
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/accelbyte/refs/heads/main/screenshots/accelbyte-2026-07-25T181428.png
security:
- kind: authentication
  name: Accelbyte Authentication
  slug: accelbyte-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Accelbyte Domain Security
  slug: accelbyte-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: accelbyte
tags:
- Gaming
- Backend
- Backend-as-a-Service
- Live Services
- Player Accounts
- Commerce
website: https://accelbyte.io/
---
