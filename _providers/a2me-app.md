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
- description: A2Me provides a private family connection platform with features such as family tree, messaging, events, and AI integration.
  name: A2Me API
  slug: a2me-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/a2me-app/llms/a2me-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/a2me-app-llms.txt
- group: other
  href: https://artifacts.apis.io/a2me-app/hosts/a2me-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/a2me-app-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://a2me.app/login
- group: docs
  title: ''
  type: Documentation
  url: https://dev.a2me.app/
- group: auth
  href: https://artifacts.apis.io/a2me-app/security/a2me-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/a2me-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://a2me.app/
- group: operate
  title: ''
  type: Support
  url: https://a2me.app/help
- group: commercial
  title: ''
  type: Pricing
  url: https://a2me.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://a2me.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://a2me.app/privacy
- group: company
  title: ''
  type: Blog
  url: https://a2me.app/news
coverage:
  checked: '2026-10-31'
  detail: Public developer portal provides feature documentation but no machine-readable API specification.
  evidence:
  - status: 200
    url: https://dev.a2me.app/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: A2Me (Ancestors to Me) is a family connection platform — Connect Today. Remember Forever. Share memories, plan events and trips, build your family tree, and preserve your legacy, without the distractions of traditional social media.
image: https://a2me.app/og-image.png
layout: provider
modified: '2026-10-31'
name: A2Me
nav: Providers
network: true
overview: 'A2Me is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Family, Social, Legacy, Photo Sharing, and Mobile App.


  A2Me''s developer surface includes documentation, support, pricing, engineering blog, and 7 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 17.8
  provenance:
    mcp: derived
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
security:
- kind: domain-security
  name: A2Me App Domain Security
  slug: a2me-app-domain-security
  summary_line: TLSv1.3
slug: a2me-app
tags:
- Family
- Social
- Legacy
- Photo Sharing
- Mobile App
website: https://a2me.app/
---
