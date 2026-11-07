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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: operate
  href: https://artifacts.apis.io/ytapi-dev/rate-limits/ytapi-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ytapi-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ytapi-dev/plans/ytapi-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ytapi-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ytapi-dev/conventions/ytapi-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ytapi-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/ytapi-dev/authentication/ytapi-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ytapi-dev-authentication.yml
- group: agent
  href: https://artifacts.apis.io/ytapi-dev/llms/ytapi-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ytapi-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/ytapi-dev/well-known/ytapi-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ytapi-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/ytapi-dev/hosts/ytapi-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ytapi-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/ytapi-dev/vendors/ytapi-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ytapi-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ytapi.dev/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ytapi.dev/legal/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://ytapi.dev/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ytapi
- group: company
  title: ''
  type: Blog
  url: https://ytapi.dev/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ytapi.dev/agent-setup
- group: auth
  href: https://artifacts.apis.io/ytapi-dev/security/ytapi-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ytapi-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ytapi.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ytapi.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://ytapi.dev/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://ytapi.dev/pricing.md
- group: operate
  title: ''
  type: Changelog
  url: https://ytapi.dev/changelog
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://ytapi.dev/openapi.json
  - status: 401
    url: https://api.ytapi.dev/mcp
  - status: 200
    url: https://ytapi.dev/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: YTAPI provides a Transcript API for YouTube videos, enabling retrieval of captions, word timings, and various subtitle formats such as Markdown, SRT, and VTT. It also supports batch endpoints for exporting whole channels and playlists as zip files via a dashboard or Chrome extension, requiring no code. The service offers search, channel, playlist, and comment data, with a single HTTPS call returning comprehensive video details. Documentation, pricing, changelog, and OpenAPI specifications are publicly available.
image: https://ytapi.dev/images/og/home.png
layout: provider
modified: '2026-10-31'
name: ytapi-dev
nav: Providers
network: true
overview: 'ytapi-dev is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, Transcripts, and YouTube.


  ytapi-dev''s developer surface includes authentication, engineering blog, getting-started guide, documentation, API reference, pricing, changelog, and 13 more developer resources.'
plans:
- name: Ytapi Dev Plans Pricing
  plan_count: 4
  slug: ytapi-dev-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Ytapi Dev Rate Limits
  slug: ytapi-dev-rate-limits
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 46.0
    catalog_earned_first_party: 24.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 27.4
    discoverability: 39.3
    operational_transparency: 34.2
  previous_composite: 34.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ytapi Dev Authentication
  slug: ytapi-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ytapi Dev Domain Security
  slug: ytapi-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ytapi-dev
tags:
- Company
- Video
- Transcripts
- YouTube
website: https://ytapi.dev/
---
