---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Free Text‑to‑Speech API providing up to ~60 phrases per hour, with bearer token authentication. See the documentation for limits and usage.
  name: 101soundboards TTS API
  slug: tts-api
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/101soundboards-com/well-known/101soundboards-com-101soundboards-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/101soundboards-com-101soundboards-security.txt
- group: operate
  href: https://artifacts.apis.io/101soundboards-com/rate-limits/101soundboards-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/101soundboards-com-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/101soundboards-com/changelog/101soundboards-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/101soundboards-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/101soundboards-com/authentication/101soundboards-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/101soundboards-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/101soundboards-com/lifecycle/101soundboards-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/101soundboards-com-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/101soundboards-com/well-known/101soundboards-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/101soundboards-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/101soundboards-com/hosts/101soundboards-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/101soundboards-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/101soundboards-com/vendors/101soundboards-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/101soundboards-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://101soundboards.statuspage.io/
- group: start
  title: ''
  type: Login
  url: https://www.101soundboards.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.101soundboards.com/changelog
- group: auth
  href: https://artifacts.apis.io/101soundboards-com/security/101soundboards-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/101soundboards-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://101soundboards.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.101soundboards.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.101soundboards.com/pages/help
- group: docs
  title: ''
  type: APIReference
  url: https://www.101soundboards.com/docs/api
- group: company
  title: ''
  type: Blog
  url: https://www.101soundboards.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.101soundboards.com/pages/terms_and_privacy#terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.101soundboards.com/pages/terms_and_privacy#privacy
- group: operate
  title: ''
  type: Support
  url: https://www.101soundboards.com/pages/help
coverage:
  checked: '2026-10-31'
  detail: The public API documentation is readable but no OpenAPI or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://www.101soundboards.com/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 101 Soundboards operates the website https://www.101soundboards.com, offering a massive library of over 78 million free audio clips in formats such as MP3, WAV, FLAC and OGG. Users can browse, download, and create personal soundboards, as well as generate text‑to‑speech voices using a free TTS API. The platform includes mobile apps for iOS and Android, supports virtual audio routing, and provides community features like favorites, sharing, and leaderboards. It is funded by advertisements and offers optional credits for downloads.
image: https://www.101soundboards.com/favicon.ico
layout: provider
modified: '2026-10-31'
name: 101 Soundboards
nav: Providers
network: true
overview: '101 Soundboards is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Audio, soundboard, Free, Text-to-Speech, and Community.


  101 Soundboards'' developer surface includes changelog, authentication, documentation, API reference, engineering blog, support, and 14 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 2
  name: 101Soundboards Com Rate Limits
  slug: 101soundboards-com-rate-limits
scopes:
- name: 101Soundboards Com Scopes
  scope_count: 0
  slug: 101soundboards-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 47.4
  previous_composite: 32.4
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 101Soundboards Com Authentication
  slug: 101soundboards-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 101Soundboards Com Domain Security
  slug: 101soundboards-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 101soundboards-com
tags:
- Audio
- soundboard
- Free
- Text-to-Speech
- Community
website: https://101soundboards.com/
---
