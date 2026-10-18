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
  href: https://raw.githubusercontent.com/api-evangelist/dpd/refs/heads/main/hosts/dpd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dpd-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dpd/refs/heads/main/vendors/dpd-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dpd-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dpd/refs/heads/main/packages/dpd-packages.yml
  title: ''
  type: SDKs
  url: packages/dpd-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dpd/refs/heads/main/packages/dpd-packages.yml
  title: ''
  type: Packages
  url: packages/dpd-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dpd/refs/heads/main/security/dpd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dpd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dpd.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.dpd.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: DPD is a leading parcel delivery network, part of Geopost, operating in over 50 countries with brands such as DPD, Chronopost, SEUR, BRT, Speedy and Jadlog. It handles more than 8 million parcels daily, offering services across Europe, Asia, Africa and the Americas.
image: https://www.dpd.com/wp-content/uploads/2021/03/007-Startseite-Empfangen-Neu.jpg
layout: provider
modified: '2026-10-13'
name: DPD
nav: Providers
network: true
overview: DPD is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Parcel Delivery, International Shipping, and E-Commerce.
random_paper: 4
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dpd Domain Security
  slug: dpd-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dpd
tags:
- Company
- Logistics
- Parcel Delivery
- International Shipping
- E-Commerce
website: https://www.dpd.com
---
