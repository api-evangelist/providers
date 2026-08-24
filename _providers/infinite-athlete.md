---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'FusionFeed is Infinite Athlete''s sports and performance data API, built on the Tempus Ex platform. It provides schedules, team rosters on a game-by-game basis, official stats delivered the moment the '
  name: FusionFeed
  slug: fusionfeed
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://infiniteathlete.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tempus-ex.com/fusionfeed
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tempus-ex.com/fusionfeed/rest/explorer-and-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tempus-ex.com/fusionfeed
- group: auth
  title: ''
  type: Authentication
  url: authentication/infinite-athlete-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/infinite-athlete-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/infinite-athlete-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.tempus-ex.com/fusionfeed/limits
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/infinite-athlete-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/infinite-athlete-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infinite-athlete-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/infinite-athlete-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infinite-athlete-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tempus-ex
- group: company
  title: ''
  type: Blog
  url: https://infiniteathlete.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://infiniteathlete.ai/contact
- group: start
  title: ''
  type: SignUp
  url: https://infiniteathlete.ai/developers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://infiniteathlete.ai/privacy
created: '2026-07-17'
description: Infinite Athlete is a sports technology company that brings together leading companies in performance biomechanics and real-time video to deliver data-driven, actionable insights for elite athlete evaluation, development, health, and safety. Its work spans athlete performance frameworks, biomechanics research and development, a real-time video and data capture technology platform, facility design and hardware installation, sports operational efficiency, and equipment/facility/surface analysis and certification for major leagues and teams. Its developer-facing product is FusionFeed, a sports and performance data API (REST, GraphQL, and the proprietary FQL query language) built on the Tempus Ex platform that exposes schedules, rosters, official and automated statistics, telemetry, video feeds, and virtual camera data. The developer platform is currently invite-only. Infinite Athlete is backed by a16z and has been recognized among the "10 Most Innovative Sports Tech Companies"
  by Sports Business Journal.
image: https://static.infiniteathlete.ai/logo_icon_dark_705bc0c5c9.svg
layout: provider
modified: '2026-07-19'
name: Infinite Athlete
nav: Providers
network: true
overview: 'Infinite Athlete publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Sports Technology, Sports Data, and Athlete Performance.


  Infinite Athlete''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, signup flow, and 11 more developer resources.'
random_paper: 4
scopes:
- name: Infinite Athlete Scopes
  scope_count: 7
  slug: infinite-athlete-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: emerging
  composite: 24.3
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 24.3
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infinite-athlete/refs/heads/main/screenshots/infinite-athlete-2026-07-25T222606.png
security:
- kind: authentication
  name: Infinite Athlete Authentication
  slug: infinite-athlete-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 5 schemes
- kind: domain-security
  name: Infinite Athlete Domain Security
  slug: infinite-athlete-domain-security
  summary_line: TLSv1.3 · DMARC
slug: infinite-athlete
tags:
- Company
- Sports
- Sports Technology
- Sports Data
- Athlete Performance
- Biomechanics
- Video
- Real-Time Data
- Analytics
- GraphQL
website: https://infiniteathlete.ai/developers
---
