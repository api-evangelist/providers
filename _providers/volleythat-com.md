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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Volley voice‑powered games platform, documented at the developer portal.
  name: Volley Games API
  slug: volley-games-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/volleythat-com/llms/volleythat-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/volleythat-com-llms.txt
- group: other
  href: https://artifacts.apis.io/volleythat-com/hosts/volleythat-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/volleythat-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/volleythat-com/vendors/volleythat-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/volleythat-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.weekend.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.weekend.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.weekend.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.weekend.com/press
- group: company
  title: ''
  type: Blog
  url: https://www.weekend.com/blog
- group: auth
  href: https://artifacts.apis.io/volleythat-com/security/volleythat-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/volleythat-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.weekend.com/volleygames
coverage:
  detail: Developer portal pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.weekend.com/volleygames
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Volley develops voice‑powered games for smart TVs and voice assistants, bringing interactive family entertainment like Jeopardy! and Wheel of Fortune to living‑room screens. The platform enables users to play games aloud, turning TV time into together time with friends and family. It partners with major TV manufacturers and voice platforms to deliver seamless experiences.
layout: provider
modified: '2026-10-29'
name: Volley
nav: Providers
network: true
overview: 'Volley is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Voice AI, Gaming, Smart TV, and Entertainment.


  Volley''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 61.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/volleythat-com/volleythat-com-2026-11-03T145914.png
security:
- kind: domain-security
  name: Volleythat Com Domain Security
  slug: volleythat-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: volleythat-com
tags:
- Company
- Voice AI
- Gaming
- Smart TV
- Entertainment
website: https://www.weekend.com/volleygames
---
