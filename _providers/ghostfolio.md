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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Ghostfolio provides a developer API documented at the Ghostfolio documentation site.
  name: Ghostfolio API
  slug: ghostfolio-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/ghostfolio/hosts/ghostfolio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ghostfolio-hosts.yml
- group: build
  href: https://artifacts.apis.io/ghostfolio/packages/ghostfolio-packages.yml
  title: ''
  type: SDKs
  url: packages/ghostfolio-packages.yml
- group: build
  href: https://artifacts.apis.io/ghostfolio/packages/ghostfolio-packages.yml
  title: ''
  type: Packages
  url: packages/ghostfolio-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ghostfol.io/ca/sobre/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://ghostfol.io/en/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ghostfol.io/nl/over/privacybeleid
- group: operate
  title: ''
  type: ChangeLog
  url: https://ghostfol.io/ca/sobre/changelog
- group: auth
  href: https://artifacts.apis.io/ghostfolio/security/ghostfolio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ghostfolio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ghostfol.io/
- group: docs
  title: ''
  type: Documentation
  url: https://ghostfol.io/en/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://ghostfol.io/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://ghostfol.io/en/blog
- group: operate
  title: ''
  type: Support
  url: https://ghostfol.io/en/faq
- group: start
  title: ''
  type: GettingStarted
  url: https://ghostfol.io/en/demo
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ghostfolio
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://ghostfol.io/en/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Ghostfolio is an open source wealth management software built with modern web technologies. It enables individuals to track stocks, ETFs, and cryptocurrencies, providing data‑driven insights for personal investment decisions. The platform offers a self‑hosted version and a premium cloud service, supporting continuous portfolio monitoring and financial planning.
image: https://ghostfol.io/assets/cover.png
layout: provider
modified: '2026-10-28'
name: Ghostfolio
nav: Providers
network: true
overview: 'Ghostfolio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Wealth Management, Open Source, Software-as-a-Service, and Portfolio.


  Ghostfolio''s developer surface includes signup flow, changelog, documentation, pricing, engineering blog, support, getting-started guide, and 8 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 24.3
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
screenshot: https://apis.io/screenshots/ghostfolio/ghostfolio-2026-11-03T132818.png
security:
- kind: domain-security
  name: Ghostfolio Domain Security
  slug: ghostfolio-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ghostfolio
tags:
- Finance
- Wealth Management
- Open Source
- Software-as-a-Service
- Portfolio
website: https://ghostfol.io/
---
