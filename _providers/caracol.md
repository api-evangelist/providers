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
  href: https://raw.githubusercontent.com/api-evangelist/caracol/refs/heads/main/hosts/caracol-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caracol-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caracol/refs/heads/main/vendors/caracol-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caracol-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caracol/refs/heads/main/security/caracol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caracol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.caracoltv.com
coverage:
  checked: '2026-10-07'
  detail: No public developer program or API documentation is available on the company's website.
  evidence:
  - status: 200
    url: https://www.caracoltv.com
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Caracol Televisión S.A. is a major Colombian television network offering a wide range of entertainment, news, and reality programming. Founded in 1969 as a production company and launched as a national broadcaster in 1998, it operates multiple channels and digital platforms, reaching millions of viewers across Colombia and the Spanish‑speaking world. The company also runs associated media properties such as Noticias Caracol, Blu Radio, and Caracol TV corporate services.
image: https://caracoltv.brightspotcdn.com/dims4/default/a14764e/2147483647/strip/true/crop/1120x630+40+0/resize/1280x720!/format/webp/quality/75/?url=https%3A%2F%2Fcaracol-brightspot.s3.us-west-2.amazonaws.com%2Fe7%2F47%2F8e11490445fa970f4e73f7757615%2Fcaracoltv.jpg
layout: provider
modified: '2026-10-06'
name: Caracol
nav: Providers
network: true
overview: Caracol is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Television, Colombia, and Entertainment.
random_paper: 21
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
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
  name: Caracol Domain Security
  slug: caracol-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: caracol
tags:
- Company
- Media
- Television
- Colombia
- Entertainment
- News
website: https://www.caracoltv.com
---
