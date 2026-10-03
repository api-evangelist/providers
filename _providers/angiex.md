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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/angiex/refs/heads/main/hosts/angiex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/angiex-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://angiex.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://angiex.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://angiex.com/ASSETS/DOCS/Angiex-World_ADC_POSTER_Final.pdf
- group: company
  title: ''
  type: Blog
  url: https://angiex.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/angiex/refs/heads/main/security/angiex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/angiex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://angiex.com/
coverage:
  checked: 2026-09-24
  detail: Angiex provides only corporate website and PDF poster with no developer program or API documentation.
  evidence:
  - status: 200
    url: https://angiex.com/ASSETS/DOCS/Angiex-World_ADC_POSTER_Final.pdf
  reason: no-developer-program
  state: none
created: '2026-09-24'
description: Angiex is developing first‑in‑class Nuclear‑Delivered Antibody‑Drug Conjugates™ (ND‑ADCs) to address cancer lethality. The company aims to make cancer a non‑lethal disease, leveraging novel biology to deliver safe and effective therapies. Over one‑third of people in developed countries develop cancer, with 10 million deaths annually; Angiex’s vision is that no one should die of cancer.
image: https://angiex.com/ASSETS/IMG/news/_1200x630_crop_center-center_none/news-default.png
layout: provider
modified: '2026-09-24'
name: Angiex
nav: Providers
network: true
overview: 'Angiex is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Oncology, Drug Development, Antibody-Drug Conjugates, and Cancer Therapy.


  Angiex''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 8.6
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
    developer_ergonomics: 11.9
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
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Angiex Domain Security
  slug: angiex-domain-security
  summary_line: TLSv1.3 · DMARC
slug: angiex
tags:
- Biotechnology
- Oncology
- Drug Development
- Antibody-Drug Conjugates
- Cancer Therapy
- Company
website: https://angiex.com/
---
