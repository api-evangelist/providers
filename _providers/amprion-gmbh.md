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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amprion-gmbh/refs/heads/main/llms/amprion-gmbh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amprion-gmbh-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amprion-gmbh/refs/heads/main/hosts/amprion-gmbh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amprion-gmbh-hosts.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.amprion.net/Ueber-uns/Management/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amprion-gmbh/refs/heads/main/security/amprion-gmbh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amprion-gmbh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amprion.net/
coverage:
  detail: Amprion provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.amprion.net/
  reason: no-developer-program
  state: none
created: '2026-09-23'
description: Amprion is a leading European transmission system operator managing a high‑voltage electricity grid spanning over 11,000 km across Germany. It connects renewable energy sources, ensures reliable power supply for millions, and drives grid expansion and sustainability initiatives.
image: https://www.amprion.net/Bilder/Social-Media-Logos/amprion-default-img.png
layout: provider
modified: '2026-09-23'
name: Amprion
nav: Providers
network: true
overview: Amprion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Transmission, Grid, and Infrastructure.
random_paper: 7
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 5
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
    discoverability: 57.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amprion Gmbh Domain Security
  slug: amprion-gmbh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amprion-gmbh
tags:
- Company
- Energy
- Transmission
- Grid
- Infrastructure
website: https://www.amprion.net/
---
