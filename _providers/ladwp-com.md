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
  href: https://raw.githubusercontent.com/api-evangelist/ladwp-com/refs/heads/main/hosts/ladwp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ladwp-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ladwp-com/refs/heads/main/vendors/ladwp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ladwp-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ladwp.com/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.ladwp.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ladwp.com/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ladwp-com/refs/heads/main/security/ladwp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ladwp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ladwp.com
- group: other
  title: ''
  type: OpenData
  url: https://data.lacity.org/browse?q=LADWP
coverage:
  checked: '2026-10-13'
  detail: 'Probed www.ladwp.com, myaccount.ladwp.com and api.ladwp.com: no OpenAPI, AsyncAPI, GraphQL or MCP surface and no developer portal. No Green Button Download My Data or Connect My Data page exists in the ladwp.com sitemap (green-button paths 404); a third-party guide (nectarclimate.com) also reports none, unconfirmed by LADWP. The only machine-readable surface is 33 LADWP-attributed datasets (outages, water supply, solar interconnection, CO2) on data.lacity.org, served by the City of Los Angeles Socrata platform, not by LADWP.'
  evidence:
  - status: 200
    url: https://www.ladwp.com/
  - status: 404
    url: https://api.ladwp.com/
  - status: 200
    url: https://data.lacity.org/
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: The Los Angeles Department of Water and Power (LADWP) is the largest municipal utility in the United States, a department of the City of Los Angeles providing water and electric service. It publishes no public developer API; operational datasets attributed to LADWP are published on the City of Los Angeles open data portal (Socrata).
layout: provider
modified: '2026-10-13'
name: Los Angeles Department of Water and Power
nav: Providers
network: true
overview: 'Los Angeles Department of Water and Power is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Utilities, Electricity, Water, and Government.


  Los Angeles Department of Water and Power''s developer surface includes support and 7 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ladwp Com Domain Security
  slug: ladwp-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: ladwp-com
tags:
- Company
- Utilities
- Electricity
- Water
- Government
- Open Data
website: https://www.ladwp.com
---
