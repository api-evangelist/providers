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
  href: https://raw.githubusercontent.com/api-evangelist/sobi/refs/heads/main/hosts/sobi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sobi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sobi/refs/heads/main/vendors/sobi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sobi-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sobi.com/en/terms-use
- group: company
  title: ''
  type: Newsroom
  url: https://www.sobi.com/en/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sobi/refs/heads/main/security/sobi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sobi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sobi.com/
coverage:
  checked: '2026-10-13'
  detail: Sobi is a biopharmaceutical company that does not expose a public API surface.
  evidence:
  - status: 404
    url: https://api.sobi.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-10-12'
description: Sobi (Swedish Orphan Biovitrum) is a global biopharmaceutical company focused on developing innovative medicines for rare diseases. The company aims to transform the lives of patients with rare and ultra‑rare conditions through a robust pipeline of therapies, extensive research, and collaborations worldwide. Sobi operates from its headquarters in Stockholm, Sweden, and maintains a presence across Europe and the United States, delivering treatments in hematology, immunology, and neurology.
image: https://www.sobi.com/sites/sobi/files/SOBI_logo.svg
layout: provider
modified: '2026-10-12'
name: Sobi (Swedish Orphan Biovitrum)
nav: Providers
network: true
overview: Sobi (Swedish Orphan Biovitrum) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharma, Rare Disease, Sweden, and Healthcare.
random_paper: 11
score:
  band: minimal
  composite: 6.5
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
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sobi Domain Security
  slug: sobi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sobi
tags:
- Company
- Biopharma
- Rare Disease
- Sweden
- Healthcare
website: https://www.sobi.com/
---
