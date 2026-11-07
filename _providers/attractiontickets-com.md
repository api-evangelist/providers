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
  href: https://artifacts.apis.io/attractiontickets-com/hosts/attractiontickets-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/attractiontickets-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/attractiontickets-com/vendors/attractiontickets-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/attractiontickets-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.attractiontickets.com/en/terms-and-conditions.htm
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.attractiontickets.com/en/privacy-policy.htm
- group: start
  title: ''
  type: Login
  url: https://www.attractiontickets.com/en/customer/login
- group: auth
  href: https://artifacts.apis.io/attractiontickets-com/security/attractiontickets-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/attractiontickets-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://attractiontickets.com/
- group: company
  title: ''
  type: Blog
  url: https://www.attractiontickets.com/en/blog
coverage:
  checked: '2026-11-02'
  detail: Public website provides ticket information but no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://www.attractiontickets.com/en/disneylandr-paris-guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: AttractionTickets.com is a UK‑based ticket reseller specializing in Orlando theme‑park experiences. As official partners of Disney and Universal for over 20 years, they offer discounted tickets and hotel packages for Walt Disney World, Universal Studios, and other Florida attractions. Their platform lets customers browse deals, compare prices, and book tickets online, providing savings and flexible options for families and travelers.
image: https://www.attractiontickets.com/themes/custom/atd/favicons/apple-touch-icon.png
layout: provider
modified: '2026-11-02'
name: Attraction Tickets
nav: Providers
network: true
overview: 'Attraction Tickets is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Ticketing, Travel, Orlando, Disney, and Universal.


  Attraction Tickets'' developer surface includes engineering blog and 7 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 11.9
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Attractiontickets Com Domain Security
  slug: attractiontickets-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: attractiontickets-com
tags:
- Ticketing
- Travel
- Orlando
- Disney
- Universal
website: https://attractiontickets.com/
---
