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
  href: https://raw.githubusercontent.com/api-evangelist/convalifepharmaceuticals/refs/heads/main/hosts/convalifepharmaceuticals-hosts.yml
  title: ''
  type: Hosts
  url: hosts/convalifepharmaceuticals-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/convalifepharmaceuticals/refs/heads/main/security/convalifepharmaceuticals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/convalifepharmaceuticals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://convalife.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://convalife.com
  - status: 403
    url: https://equityzen.com/company/convalifepharmaceuticals
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: 'Convalifepharmaceuticals is a Shanghai-based biopharmaceutical company focused on innovative drug research and development, targeting tumor, antiviral and aging related diseases. The firm develops small-molecule, antibody-drug conjugate and other therapeutic platforms, and holds multiple patents and clinical trials. It operates primarily in China and is listed on the Hong Kong stock exchange, with recent licensing agreements expanding its global reach. (Source: https://duckduckgo.com/html/?q=Convalifepharmaceuticals, https://convalife.com/en/)'
layout: provider
modified: '2026-10-10'
name: Convalifepharmaceuticals
nav: Providers
network: true
overview: Convalifepharmaceuticals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharma, China, Oncology, and Antiviral.
random_paper: 11
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 4
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
  name: Convalifepharmaceuticals Domain Security
  slug: convalifepharmaceuticals-domain-security
  summary_line: TLSv1.3 · HSTS
slug: convalifepharmaceuticals
tags:
- Company
- Biopharma
- China
- Oncology
- Antiviral
website: https://convalife.com
---
