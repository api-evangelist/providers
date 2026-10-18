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
  href: https://raw.githubusercontent.com/api-evangelist/cadent-therapeutics/refs/heads/main/hosts/cadent-therapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cadent-therapeutics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cadent-therapeutics/refs/heads/main/vendors/cadent-therapeutics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cadent-therapeutics-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cadent-therapeutics/refs/heads/main/security/cadent-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cadent-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/cadent-therapeutics_stock/
coverage:
  checked: '2026-10-06'
  detail: Cadent Therapeutics is a biopharmaceutical company with no public API surface.
  evidence:
  - status: unreachable
    url: https://cadenttherapeutics.com
  reason: not-a-software-company
  state: none
created: '2026-10-06'
description: Cadent Therapeutics is a biopharmaceutical company focused on developing novel therapies for neuropsychiatric disorders, particularly schizophrenia. Founded in 2020, the company aims to leverage cutting‑edge neuroscience and clinical research to address unmet medical needs. It was acquired by Novartis in 2021, integrating its pipeline into Novartis’s broader neuroscience portfolio. While its original website is no longer active, the company’s activities are documented through press releases, regulatory filings, and third‑party industry profiles.
layout: provider
modified: '2026-10-06'
name: Cadent Therapeutics
nav: Providers
network: true
overview: Cadent Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biopharma, Neuroscience, Schizophrenia, Clinical Trials, and Novartis.
random_paper: 7
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 3
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cadent Therapeutics Domain Security
  slug: cadent-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cadent-therapeutics
tags:
- Biopharma
- Neuroscience
- Schizophrenia
- Clinical Trials
- Novartis
- Company
website: https://forgeglobal.com/cadent-therapeutics_stock/
---
