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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/dhruvaspace/hosts/dhruvaspace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dhruvaspace-hosts.yml
- group: other
  href: https://artifacts.apis.io/dhruvaspace/vendors/dhruvaspace-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dhruvaspace-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DhruvaSpace
- group: auth
  href: https://artifacts.apis.io/dhruvaspace/security/dhruvaspace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dhruvaspace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dhruvaspace.com
- group: company
  title: ''
  type: About
  url: https://www.dhruvaspace.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.dhruvaspace.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dhruvaspace.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dhruvaspace.com/terms-of-use
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.dhruvaspace.com/trust-centre
coverage:
  checked: '2026-10-23'
  detail: The provider's website is a JavaScript‑rendered site with no machine‑readable API spec discovered.
  evidence:
  - status: 200
    url: https://www.dhruvaspace.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Dhruvaspace is an Indian space technology company that designs, builds, and operates small satellite platforms, launch services, and ground station infrastructure. It provides end‑to‑end space solutions including satellite buses, solar arrays, launch integration, and data‑downlink services for commercial, governmental, and research customers worldwide.
image: https://cdn.prod.website-files.com/6755291c52809136ad435619/67cc2052c957f1d484917436_7afb9df44f2181f66c6743dcef153fb1_Home%20page_Dhruva%20Space.avif
layout: provider
modified: '2026-10-23'
name: Dhruvaspace
nav: Providers
network: true
overview: 'Dhruvaspace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Satellite, Launches, and Ground Station.


  Dhruvaspace''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dhruvaspace Domain Security
  slug: dhruvaspace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dhruvaspace
tags:
- Company
- Space
- Satellite
- Launches
- Ground Station
website: https://www.dhruvaspace.com
---
