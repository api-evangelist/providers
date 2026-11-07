---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/ava-me/plans/ava-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ava-me-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/ava-me/llms/ava-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ava-me-llms.txt
- group: auth
  href: https://artifacts.apis.io/ava-me/well-known/ava-me-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ava-me-help-security.txt
- group: agent
  href: https://artifacts.apis.io/ava-me/well-known/ava-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ava-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/ava-me/hosts/ava-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ava-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/ava-me/vendors/ava-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ava-me-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ava.me/terms
- group: operate
  title: ''
  type: Support
  url: https://help.ava.me
- group: auth
  title: ''
  type: Security
  url: https://www.ava.me/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ava.me/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ava.me/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.ava.me/blog/changelog
- group: company
  title: ''
  type: Blog
  url: https://blog.ava.me/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.ava.me/en/articles/3157558-use-and-setup-ava-at-work
- group: docs
  title: ''
  type: Documentation
  url: https://help.ava.me/
- group: auth
  href: https://artifacts.apis.io/ava-me/security/ava-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ava-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ava.me/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://blog.ava.me/mcp
  - status: 403
    url: https://help.ava.me/mcp
  - status: 200
    url: https://ava.me/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Ava offers AI‑based live captioning, transcription, and ASL interpretation services that make conversations accessible for Deaf and hard‑of‑hearing people. Its solutions are provided to organizations in sectors such as office and remote work, education, healthcare, retail, and live events, and integrate with major video‑meeting platforms. The service is available on web, desktop (Windows, Mac) and mobile (iOS, Android) and claims 99% caption accuracy.
image: https://cdn.prod.website-files.com/5f0a37756175633fbb9b9e84/5f4d62c0cd5653719f74e890_mobile-desktop-3.jpg
layout: provider
modified: '2026-10-22'
name: Ava
nav: Providers
network: true
overview: 'Ava is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Captions, Transcription, ASL Interpretation, Accessibility, and Video Conferencing.


  Ava''s developer surface includes support, pricing, changelog, engineering blog, getting-started guide, documentation, and 11 more developer resources.'
plans:
- name: Ava Me Plans Pricing
  plan_count: 5
  slug: ava-me-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 55.4
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 27.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ava-me/ava-me-2026-11-03T121410.png
security:
- kind: domain-security
  name: Ava Me Domain Security
  slug: ava-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ava-me
tags:
- Captions
- Transcription
- ASL Interpretation
- Accessibility
- Video Conferencing
- Education
- Healthcare
- Retail
website: https://ava.me/
---
