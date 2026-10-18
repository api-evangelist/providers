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
  href: https://raw.githubusercontent.com/api-evangelist/uefa/refs/heads/main/hosts/uefa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/uefa-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/uefa/refs/heads/main/vendors/uefa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/uefa-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/uefa/refs/heads/main/security/uefa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uefa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uefa.com
created: '2026-10-13'
description: UEFA.com is the official site of UEFA, the Union of European Football Associations, and the governing body of football in Europe. UEFA works to promote, protect and develop European football across its 55 member associations and organises some of the world’s most famous football competitions, including the UEFA Champions League, UEFA Women’s Champions League, the UEFA Europa League, UEFA EURO and many more. The site features the latest European football news, goals, an extensive archive of video and stats, as well as insights into how the organisation works, including information on financial fair play, how UEFA supports grassroots football and the UEFA HatTrick funding scheme.
layout: provider
modified: '2026-10-13'
name: UEFA
nav: Providers
network: true
overview: UEFA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Football, Europe, and GoverningBody.
random_paper: 21
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 6
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
  provenance:
    mcp: derived
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
  name: Uefa Domain Security
  slug: uefa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: uefa
tags:
- Company
- Sports
- Football
- Europe
- GoverningBody
website: https://www.uefa.com
---
