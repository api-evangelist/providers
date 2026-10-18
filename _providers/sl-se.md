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
- description: Public transport data APIs for Stockholm (schedules, stops, routes).
  name: SL API
  slug: sl-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sl-se/refs/heads/main/security/sl-se-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/sl-se-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sl-se/refs/heads/main/hosts/sl-se-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sl-se-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sl-se/refs/heads/main/security/sl-se-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sl-se-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sl-se/refs/heads/main/security/sl-se-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sl-se-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sl.se/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://sl.se/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: SL Storstockholms Lokaltrafik (SL) is the public transport authority for Stockholm County in Sweden, operating buses, metros, commuter trains, trams and ferries. It provides travel planning, ticketing, real‑time departure information and service updates for millions of passengers each year. While its primary focus is on passenger services, SL also offers data feeds and APIs for developers to integrate schedule, stop, and route information into third‑party applications, supporting open data initiatives and smart mobility solutions.
image: https://afde-slweb-prod-axgjc2gedaepaveg.z01.azurefd.net/styleguide/70.3.2/images/og_image.jpg
layout: provider
modified: '2026-10-15'
name: SL Storstockholms Lokaltrafik
nav: Providers
network: true
overview: SL Storstockholms Lokaltrafik is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Transport, PublicTransit, Sweden, Stockholm, and Open Data.
random_paper: 0
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sl Se Domain Security
  slug: sl-se-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sl Se Vulnerability Disclosure
  slug: sl-se-vulnerability-disclosure
  summary_line: no policy recorded
slug: sl-se
tags:
- Transport
- PublicTransit
- Sweden
- Stockholm
- Open Data
website: https://sl.se/
---
