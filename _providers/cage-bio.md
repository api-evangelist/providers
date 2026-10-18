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
  href: https://raw.githubusercontent.com/api-evangelist/cage-bio/refs/heads/main/hosts/cage-bio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cage-bio-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cage-bio/refs/heads/main/security/cage-bio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cage-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cagebio.com
coverage:
  checked: '2026-10-06'
  detail: No public API specifications or documentation were found for Cage Bio.
  evidence:
  - status: 404
    url: https://cagebio.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-10-06'
description: Cage Bio Inc. is a clinical‑stage biotechnology company developing localized therapies for dermatology, inflammation, and immunology using its proprietary deep eutectic ionic liquid platform. The company aims to provide high‑efficacy, skin‑targeted treatments that reduce systemic exposure while maintaining therapeutic potency.
image: https://img1.wsimg.com/isteam/ip/146d5b77-ddc7-4513-9d31-be7720da74e8/blob-6432372.png
layout: provider
modified: '2026-10-06'
name: Cage Bio
nav: Providers
network: true
overview: Cage Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Dermatology, Immunology, and Ionic Liquids.
random_paper: 11
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 6
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
  provenance:
    mcp: unknown
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
  name: Cage Bio Domain Security
  slug: cage-bio-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cage-bio
tags:
- Company
- Biotechnology
- Dermatology
- Immunology
- Ionic Liquids
- Clinical Stage
website: https://cagebio.com
---
