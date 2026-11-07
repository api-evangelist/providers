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
- description: ShadowBot provides a browser gaming platform with HTML5 games accessible via web. Documentation is at https://shadowbot.tech/about
  name: ShadowBot API
  slug: shadowbot-api
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/shadowbot/changelog/shadowbot-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/shadowbot-changelog.yml
- group: agent
  href: https://artifacts.apis.io/shadowbot/llms/shadowbot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shadowbot-llms.txt
- group: other
  href: https://artifacts.apis.io/shadowbot/hosts/shadowbot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shadowbot-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://shadowbot.tech/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://shadowbot.tech/developers
- group: auth
  href: https://artifacts.apis.io/shadowbot/security/shadowbot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shadowbot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shadowbot.tech/
- group: company
  title: ''
  type: Blog
  url: https://shadowbot.tech/blog
- group: docs
  title: ''
  type: Documentation
  url: https://shadowbot.tech/about
- group: start
  title: ''
  type: GettingStarted
  url: https://shadowbot.tech/faq
- group: operate
  title: ''
  type: Support
  url: https://shadowbot.tech/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shadowbot.tech/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shadowbot.tech/privacy
coverage:
  checked: '2026-10-22'
  detail: Documentation pages are rendered via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://shadowbot.tech/about
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: ShadowBot is a free browser gaming platform offering thousands of HTML5 games that can be played instantly without downloads or installations. It provides a wide catalog ranging from arcade classics to puzzles, racing, and strategy games, supporting daily challenges, tournaments, and community features like clans and leaderboards. The service aims to make gaming accessible to everyone across devices, with a focus on easy access and a vibrant collection for casual and dedicated players alike.
image: https://shadowbot.tech/opengraph-image?5d0623eb3eac3e38
layout: provider
modified: '2026-10-22'
name: ShadowBot
nav: Providers
network: true
overview: 'ShadowBot is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, HTML5, Free, and Browser.


  ShadowBot''s developer surface includes changelog, engineering blog, documentation, getting-started guide, support, and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 55.4
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.7
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/shadowbot/shadowbot-2026-11-03T143109.png
security:
- kind: domain-security
  name: Shadowbot Domain Security
  slug: shadowbot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shadowbot
tags:
- Gaming
- HTML5
- Free
- Browser
website: https://shadowbot.tech/
---
