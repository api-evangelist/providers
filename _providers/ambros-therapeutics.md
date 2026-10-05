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
  href: https://raw.githubusercontent.com/api-evangelist/ambros-therapeutics/refs/heads/main/hosts/ambros-therapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ambros-therapeutics-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ambros-therapeutics/refs/heads/main/security/ambros-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ambros-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ambrostherapeutics.com/
created: '2026-09-24'
description: Ambros Therapeutics is a biotechnology company focused on developing innovative therapeutic solutions for serious diseases. Leveraging cutting‑edge research in molecular biology and immunology, Ambros aims to bring novel treatments from discovery through clinical development to patients in need. The company emphasizes robust scientific collaboration, advanced platform technologies, and a commitment to addressing unmet medical needs across oncology, rare diseases, and other critical therapeutic areas.
image: https://ambrostherapeutics.com/wp-content/themes/ambros_theme/assets/images/logo.png
layout: provider
modified: '2026-09-24'
name: Ambros Therapeutics
nav: Providers
network: true
overview: Ambros Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Innovation, and Research.
random_paper: 6
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 3.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ambros Therapeutics Domain Security
  slug: ambros-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ambros-therapeutics
tags:
- Company
- Biotechnology
- Therapeutics
- Innovation
- Research
website: https://ambrostherapeutics.com/
---
