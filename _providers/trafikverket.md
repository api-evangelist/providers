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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/trafikverket/refs/heads/main/plans/trafikverket-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trafikverket-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trafikverket/refs/heads/main/well-known/trafikverket-bransch-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/trafikverket-bransch-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trafikverket/refs/heads/main/well-known/trafikverket-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trafikverket-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/trafikverket/refs/heads/main/hosts/trafikverket-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trafikverket-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/trafikverket/refs/heads/main/packages/trafikverket-packages.yml
  title: ''
  type: SDKs
  url: packages/trafikverket-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/trafikverket/refs/heads/main/packages/trafikverket-packages.yml
  title: ''
  type: Packages
  url: packages/trafikverket-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trafikverket.se/om-oss/nyheter/lansnyheter/jamtland/2026/tossobron-i-jarpen-fortsatt-avstangd-pa-obestamd-tid/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trafikverket.se/en/start/driving-licence/book-pay-and-cancel-tests/prices-for-tests-and-photos/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trafikverket
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trafikverket/refs/heads/main/security/trafikverket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trafikverket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.trafikverket.se/
- group: other
  title: ''
  type: Image
  url: https://www.trafikverket.se/favicon.ico
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://trafikverket.se/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Trafikverket, the Swedish Transport Administration, is a government agency responsible for the long-term planning, construction, operation and maintenance of the nation’s road and railway infrastructure. It oversees traffic safety, vehicle registration, and provides extensive data services related to traffic flow, road conditions, public transport schedules, and infrastructure projects. The agency works to ensure efficient, safe, and sustainable transport across Sweden, offering APIs for developers to access real-time traffic information, road work updates, and transport statistics.
image: https://www.trafikverket.se/contentassets/8089b60ca01544e4b54d06264576148c/45873.jpg?width=1200&height=630&quality=90&format=jpg
layout: provider
modified: '2026-10-15'
name: Trafikverket
nav: Providers
network: true
overview: 'Trafikverket is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Transport, Government, Sweden, and Infrastructure.


  Trafikverket''s developer surface includes pricing and 11 more developer resources.'
plans:
- name: Trafikverket Plans Pricing
  plan_count: 11
  slug: trafikverket-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Trafikverket Rate Limits
  slug: trafikverket-rate-limits
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Trafikverket Domain Security
  slug: trafikverket-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: trafikverket
tags:
- Company
- Transport
- Government
- Sweden
- Infrastructure
website: https://www.trafikverket.se/
---
