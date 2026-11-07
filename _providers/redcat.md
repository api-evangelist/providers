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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/redcat/hosts/redcat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/redcat-hosts.yml
- group: other
  href: https://artifacts.apis.io/redcat/vendors/redcat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/redcat-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.redcatht.com/helpcentre/sign-up-with-google-facebook-and-apple
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redcatht.com/en-au/about-us/privacy-policy?hsLang=en-gb
- group: company
  title: ''
  type: Blog
  url: https://www.redcatht.com/en-au/resources/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.redcat.com.au/
- group: auth
  href: https://artifacts.apis.io/redcat/security/redcat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/redcat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.redcatht.com/en-au/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://redcat.com.au/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Redcat provides a hospitality IT platform offering digital ordering, loyalty, delivery, and operational tools for restaurants and cafes. Their solutions include online and kiosk ordering, QR code table ordering, virtual brands, drive‑thru, catering, POS‑less ordering, delivery partner integration, flat‑fee delivery, loyalty programs, mobile apps, digital media boards, gift‑card sales, and comprehensive reporting dashboards. The platform serves fast‑casual, QSR, franchise and restaurant‑group sectors across Australia and New Zealand, helping businesses streamline ordering, marketing, and back‑office operations.
layout: provider
modified: '2026-10-28'
name: Redcat
nav: Providers
network: true
overview: 'Redcat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Hospitality, RestaurantTech, Ordering, Loyalty, and Delivery.


  Redcat''s developer surface includes signup flow, engineering blog, documentation, and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/redcat/redcat-2026-11-03T142109.png
security:
- kind: domain-security
  name: Redcat Domain Security
  slug: redcat-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: redcat
tags:
- Hospitality
- RestaurantTech
- Ordering
- Loyalty
- Delivery
website: https://www.redcatht.com/en-au/
---
