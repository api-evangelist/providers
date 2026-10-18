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
  href: https://raw.githubusercontent.com/api-evangelist/celea-therapeutics/refs/heads/main/hosts/celea-therapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/celea-therapeutics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/celea-therapeutics/refs/heads/main/vendors/celea-therapeutics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/celea-therapeutics-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.celeatx.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/celea-therapeutics/refs/heads/main/security/celea-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/celea-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.celeatx.com
coverage:
  checked: '2026-10-07'
  detail: No API or developer documentation was found for Celea Therapeutics.
  evidence:
  - status: 0
    url: https://api.celeatx.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Celea Therapeutics is a biopharmaceutical company focused on developing next‑generation therapies for serious respiratory diseases, notably idiopathic pulmonary fibrosis. Their lead program deupirfenidone is in Phase 3, aiming to become a new standard of care. The company emphasizes patient‑centric science and innovative drug development.
image: http://static1.squarespace.com/static/68f24efd0976f3155cb544a1/t/69011232979bd576aa553264/1761677874337/Celea_Logo_RGB.png?format=1500w
layout: provider
modified: '2026-10-07'
name: Celea Therapeutics
nav: Providers
network: true
overview: Celea Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharma, Respiratory, IPF, and Therapeutics.
random_paper: 0
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 4
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
    discoverability: 50.0
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
  name: Celea Therapeutics Domain Security
  slug: celea-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: celea-therapeutics
tags:
- Company
- Biopharma
- Respiratory
- IPF
- Therapeutics
website: https://www.celeatx.com
---
