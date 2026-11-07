---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: false
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/usenarrative-ai/well-known/usenarrative-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/usenarrative-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/usenarrative-ai/hosts/usenarrative-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usenarrative-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/usenarrative-ai/vendors/usenarrative-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usenarrative-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://usenarrative.ai/login
- group: docs
  title: ''
  type: Documentation
  url: https://dev.usenarrative.ai/
- group: auth
  href: https://artifacts.apis.io/usenarrative-ai/security/usenarrative-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usenarrative-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usenarrative.ai
- group: company
  title: ''
  type: Blog
  url: https://usenarrative.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://usenarrative.ai/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usenarrative.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usenarrative.ai/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.usenarrative.ai/mcp
  - status: 401
    url: https://api.usenarrative.ai/v1/graphql
  - status: 200
    url: http://www.usenarrative.ai
  reason: partner-login
  state: gated
created: '2026-10-24'
description: Usenarrative (operating as Narrative) provides an AI-powered video editing platform that automates cutting, stitching, and enhancing footage based on user prompts. Users can upload raw video, describe the desired final edit, and the AI generates a polished video with transitions, music, and captions. The service offers a web app and mobile apps for iOS, targeting creators, marketers, and businesses seeking fast video production without manual editing expertise. Narrative emphasizes ease of use, rapid turnaround, and AI-driven creativity.
image: https://usenarrative.ai/og.jpg
layout: provider
modified: '2026-10-24'
name: Usenarrative
nav: Providers
network: true
overview: 'Usenarrative is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Video Editing, Software-as-a-Service, and Creator Tools.


  Usenarrative''s developer surface includes documentation, engineering blog, support, and 8 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/usenarrative-ai/usenarrative-ai-2026-11-03T145534.png
security:
- kind: domain-security
  name: Usenarrative Ai Domain Security
  slug: usenarrative-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: usenarrative-ai
tags:
- Company
- Artificial Intelligence
- Video Editing
- Software-as-a-Service
- Creator Tools
website: https://usenarrative.ai
---
