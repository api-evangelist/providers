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
api_count: 1
apis:
- description: RESO Web API (OData) and RETS servers delivering NAVICA MLS data conforming to the RESO Data Dictionary to licensed third parties under a board/MLS, office, vendor and SEI agreement with monthly fees.
  name: NAVICA RESO Web API and RETS Data Feeds
  slug: navica-reso-web-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seisystems/refs/heads/main/hosts/seisystems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seisystems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seisystems/refs/heads/main/vendors/seisystems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seisystems-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seisystems/refs/heads/main/security/seisystems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seisystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.seisystems.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.seisystems.com/data.html
- group: operate
  title: ''
  type: Support
  url: https://www.seisystems.com/contact.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/systems-engineering-incorporated
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.seisystems.com/
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: 'Systems Engineering, Inc. (SEI) is a US multiple listing service (MLS) software vendor whose NAVICA product line serves REALTOR boards and associations: NAVICA MLS, NAVICA NEXT, Showing Manager, Mobile Plus and Client apps, Association Management System (AMS), STREAMline, Data Share, Tax/public-data and web solutions. For data access SEI operates both RETS and RESO Web API servers that meet RESO compliance requirements including the RESO Data Dictionary (RESO certification record T00000075); access requires an agreement between the board/MLS, the participating office, the third party and SEI, with monthly fees. Partner integrations (dotloop, zipLogix, CRS, Property Panorama) use SSO and per-listing integration. No public API reference, base URL or machine-readable contract is published.'
layout: provider
modified: '2026-10-13'
name: Systems Engineering, Inc. (SEI)
nav: Providers
network: true
overview: 'Systems Engineering, Inc. (SEI) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, MLS, RESO, and RESO Web API.


  Systems Engineering, Inc. (SEI)''s developer surface includes documentation, support, and 5 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 53.6
    operational_transparency: 0.0
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
  name: Seisystems Domain Security
  slug: seisystems-domain-security
  summary_line: TLSv1.3
slug: seisystems
tags:
- Company
- Real Estate
- MLS
- RESO
- RESO Web API
- RETS
- Property Data
website: https://www.seisystems.com/
---
