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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/accupedo/hosts/accupedo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/accupedo-hosts.yml
- group: other
  href: https://artifacts.apis.io/accupedo/vendors/accupedo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/accupedo-vendors.yml
- group: auth
  href: https://artifacts.apis.io/accupedo/security/accupedo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accupedo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accupedo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://accupedo.com/usermanual.html
- group: operate
  title: ''
  type: FAQ
  url: https://accupedo.com/faq.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accupedo.com/privacy.html
- group: operate
  title: ''
  type: Contact
  url: https://accupedo.com/contact.html
- group: company
  title: ''
  type: AboutUs
  url: https://accupedo.com/about.html
coverage:
  checked: '2026-10-26'
  detail: The provider offers a consumer pedometer app with no public API documentation.
  evidence:
  - status: 200
    url: https://accupedo.com
  reason: not-a-software-company
  state: none
created: '2026-10-26'
description: Accupedo is a daily pedometer app that accurately tracks your steps using intelligent 3D motion recognition algorithms. It works on Android and iOS, allowing users to set goals, monitor progress, and view detailed walking statistics. The app filters non-walking activities to ensure precise step counts, supporting health and fitness tracking.
layout: provider
modified: '2026-10-26'
name: Accupedo
nav: Providers
network: true
overview: 'Accupedo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Fitness, Mobile App, and Pedometer.


  Accupedo''s developer surface includes documentation, FAQ, and 7 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 6.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/accupedo/accupedo-2026-11-03T120158.png
security:
- kind: domain-security
  name: Accupedo Domain Security
  slug: accupedo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: accupedo
tags:
- Company
- Health
- Fitness
- Mobile App
- Pedometer
website: https://accupedo.com/
---
