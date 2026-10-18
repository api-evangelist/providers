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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hitch/refs/heads/main/hosts/hitch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hitch-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hitch/refs/heads/main/vendors/hitch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hitch-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hitch.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.hitch.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hitch.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.hitch.com/newsroom
- group: docs
  title: ''
  type: Documentation
  url: https://help.hitch.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hitch/refs/heads/main/security/hitch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hitch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hitch.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.hitch.com
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Hitch is a city‑to‑city ridesharing platform that connects drivers and passengers for long‑distance trips across the United States. Offering both private and shared rides, Hitch provides door‑to‑door service, transparent pricing starting at $15, and a mobile app on iOS and Android. With over a million seats sold and a 4.3‑star rating, the company emphasizes safety through driver background checks and vehicle standards. It serves multiple states including Texas, Florida, and Oklahoma, and aims to simplify intercity travel for users seeking affordable, reliable transportation.
image: https://www.hitch.com/social_share.png
layout: provider
modified: '2026-10-12'
name: Hitch
nav: Providers
network: true
overview: 'Hitch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ride Hailing, Transportation, Mobile App, and LongDistance.


  Hitch''s developer surface includes support, documentation, and 7 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hitch Domain Security
  slug: hitch-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hitch
tags:
- Company
- Ride Hailing
- Transportation
- Mobile App
- LongDistance
website: https://www.hitch.com
---
