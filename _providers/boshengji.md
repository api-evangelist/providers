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
  href: https://raw.githubusercontent.com/api-evangelist/boshengji/refs/heads/main/hosts/boshengji-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boshengji-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.persongen.com/privacy-protection.html
- group: company
  title: ''
  type: Newsroom
  url: https://www.persongen.com/news/117.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boshengji/refs/heads/main/security/boshengji-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boshengji-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.persongen.com
coverage:
  checked: '2026-10-02'
  detail: Boshengji provides no public developer documentation or API specifications.
  evidence:
  - status: 200
    url: https://www.persongen.com
  reason: no-developer-program
  state: none
created: '2026-10-02'
description: Boshengji is a pharmaceutical technology company focused on developing innovative cell therapy solutions. It emerged in the secondary-market harvest and is being profiled for its API offerings. The company aims to advance biotechnological research and commercialize novel treatments, partnering with research institutions and investors to bring cutting‑edge therapies to market.
image: https://www.persongen.com/logo.png
layout: provider
modified: '2026-10-02'
name: Boshengji
nav: Providers
network: true
overview: Boshengji is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Cell Therapy, CAR-T, Pharmaceuticals, and China.
random_paper: 7
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boshengji Domain Security
  slug: boshengji-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boshengji
tags:
- Biotechnology
- Cell Therapy
- CAR-T
- Pharmaceuticals
- China
website: https://www.persongen.com
---
