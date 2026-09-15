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
  scored_at: '2026-09-14'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.jssict.com/en/
- group: operate
  title: ''
  type: Support
  url: https://www.jssict.com/en/fw.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aichengtechnology/refs/heads/main/security/aichengtechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aichengtechnology-domain-security.yml
coverage:
  checked: '2026-09-14'
  detail: Aicheng Technology is Suzhou Innovation Ceramic Technology (SiCT), a ceramic substrate factory selling AlN/Si3N4 DCB and AMB plates — its entire public site is 46 static HTML pages with a PDF download center, no /robots.txt, no sitemap and no path under /.well-known/ that returns anything but the 404 page.
  evidence:
  - status: 200
    url: https://www.jssict.com/en/about.html
  - status: 404
    url: https://www.jssict.com/openapi.json
  - status: 404
    url: https://www.jssict.com/.well-known/api-catalog
  - status: 404
    url: https://www.jssict.com/robots.txt
  reason: not-a-software-company
  state: none
created: '2026-09-14'
description: 'Aicheng Technology (Suzhou Innovation Ceramic Technology Co., Ltd., "SiCT" — 苏州艾成科技技术有限公司) is a Suzhou, China advanced-ceramics manufacturer founded in July 2021 that makes power-electronics substrates: AlN and Si3N4 ceramic substrates, DCB (direct copper bonding) and AMB (active metal brazing) substrates, DPC, and active solder/brazing pastes, for industrial control, new energy, consumer electronics and rail transport. It states it is the only Chinese manufacturer running the full "ceramic blank — copper bonding — etching — electroless plating" flow in mass production, with a factory and head office in the Suzhou High-Tech District and an R&D center in Korea. It sells physical components to hardware and semiconductor packaging customers; it operates no developer program, publishes no API, and its public site is a static corporate brochure with a product catalog, a datasheet download center, and a contact form.'
image: https://www.jssict.com/en/web/img/logo.png
layout: provider
modified: '2026-09-14'
name: Aicheng Technology
nav: Providers
network: true
overview: 'Aicheng Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Advanced Materials, Ceramics, and Manufacturing.


  Aicheng Technology''s developer surface includes support and 2 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 0.0
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aichengtechnology Domain Security
  slug: aichengtechnology-domain-security
  summary_line: TLSv1.2 · DMARC
slug: aichengtechnology
tags:
- Company
- Semiconductors
- Advanced Materials
- Ceramics
- Manufacturing
- Electronic Components
- Hardware
website: https://www.jssict.com/en/
---
