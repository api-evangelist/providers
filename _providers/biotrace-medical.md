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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biotrace-medical/refs/heads/main/hosts/biotrace-medical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biotrace-medical-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biotrace-medical/refs/heads/main/vendors/biotrace-medical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biotrace-medical-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biotrace-medical/refs/heads/main/security/biotrace-medical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biotrace-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: '2026-09-28'
  detail: BioTrace Medical provides medical devices and regenerative solutions with no public API.
  evidence:
  - status: 200
    url: https://biotracemed.com
  reason: not-a-software-company
  state: none
created: '2026-09-28'
description: BioTrace Medical Inc. is a venture‑backed medical device company based in Menlo Park, California, focused on reinventing temporary cardiac pacing solutions to improve patient outcomes and reduce hospital costs. Founded in 2013, the company develops innovative pacing technologies and aims to integrate them into clinical practice, leveraging partnerships and potential acquisition pathways. For more information, see their LinkedIn profile and referenced website.
layout: provider
modified: '2026-09-28'
name: BioTrace Medical
nav: Providers
network: true
overview: BioTrace Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical, Device, Cardiology, Pacing, and Menlo Park.
random_paper: 21
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biotrace Medical Domain Security
  slug: biotrace-medical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biotrace-medical
tags:
- Medical
- Device
- Cardiology
- Pacing
- Menlo Park
- Venture Backed
website: https://www.nasdaqprivatemarket.com/
---
