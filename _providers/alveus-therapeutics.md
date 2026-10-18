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
  href: https://raw.githubusercontent.com/api-evangelist/alveus-therapeutics/refs/heads/main/hosts/alveus-therapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alveus-therapeutics-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alveustx.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alveustx.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://alveustx.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alveus-therapeutics/refs/heads/main/security/alveus-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alveus-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alveustx.com
coverage:
  checked: '2026-10-05'
  detail: Alveus Therapeutics does not appear to expose any public API surface.
  evidence:
  - status: 0
    url: https://api.alveustx.com
  reason: not-a-software-company
  state: none
created: '2026-09-24'
description: Alveus Therapeutics is a clinical‑stage biotechnology company focused on developing next‑generation obesity and metabolic disease therapies. Based in Philadelphia, the firm aims to create sustainable weight‑loss treatments with improved efficacy and tolerability, leveraging extensive leadership experience in metabolic medicine.
layout: provider
modified: '2026-09-24'
name: Alveus Therapeutics
nav: Providers
network: true
overview: Alveus Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Obesity, Metabolic Disease, Clinical Stage, and Philadelphia.
random_paper: 18
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.4
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  previous_composite: 0.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alveus Therapeutics Domain Security
  slug: alveus-therapeutics-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: alveus-therapeutics
tags:
- Biotechnology
- Obesity
- Metabolic Disease
- Clinical Stage
- Philadelphia
website: https://alveustx.com
---
