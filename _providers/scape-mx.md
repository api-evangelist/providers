---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/scape-mx/llms/scape-mx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scape-mx-llms.txt
- group: other
  href: https://artifacts.apis.io/scape-mx/hosts/scape-mx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scape-mx-hosts.yml
- group: other
  href: https://artifacts.apis.io/scape-mx/vendors/scape-mx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scape-mx-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.scapewellness.com/terms-conditions-f1
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scapewellness.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.scapewellness.com/press
- group: company
  title: ''
  type: Blog
  url: https://www.scapewellness.com/blog
- group: auth
  href: https://artifacts.apis.io/scape-mx/security/scape-mx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scape-mx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scapewellness.com
coverage:
  checked: '2026-10-25'
  detail: No public API documentation or machine‑readable contract was found for Scape.
  evidence:
  - status: 0
    url: https://api.scape.mx/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Scape Wellness is an on‑demand wellness technology platform operating in Latin America. It lets customers book professional spa and massage services delivered to their home, office or hotel, offering a premium wellness experience with licensed therapists. The service is available across multiple countries and integrates scheduling, payment and therapist management through its web platform.
layout: provider
modified: '2026-10-25'
name: Scape
nav: Providers
network: true
overview: 'Scape is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Wellness, On-demand, Spa, Latin America, and Booking.


  Scape''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Scape Mx Domain Security
  slug: scape-mx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scape-mx
tags:
- Wellness
- On-demand
- Spa
- Latin America
- Booking
website: https://www.scapewellness.com
---
