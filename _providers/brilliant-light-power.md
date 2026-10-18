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
  href: https://raw.githubusercontent.com/api-evangelist/brilliant-light-power/refs/heads/main/hosts/brilliant-light-power-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brilliant-light-power-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://brilliantlightpower.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://brilliantlightpower.com/management/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brilliant-light-power/refs/heads/main/security/brilliant-light-power-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brilliant-light-power-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brilliantlightpower.com/
- group: docs
  title: ''
  type: Documentation
  url: https://brilliantlightpower.com/technology/
- group: start
  title: ''
  type: GettingStarted
  url: https://brilliantlightpower.com/about/
- group: operate
  title: ''
  type: Support
  url: https://brilliantlightpower.com/contact/
coverage:
  checked: '2026-10-06'
  detail: The developer portal pages are plain HTML with no machine‑readable OpenAPI or other contract files.
  evidence:
  - status: 200
    url: https://brilliantlightpower.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Brilliant Light Power is a privately held energy technology company founded by Dr. Randell L. Mills. It claims to develop a novel method of extracting usable energy from hydrogen atoms, termed the SunCell® technology, which it says can produce clean, non‑polluting power. The company provides detailed information about its theory, validation reports, and commercial applications on its website, including business, technology, and research sections. It positions itself as a potential source of primary energy beyond conventional fossil fuels.
layout: provider
modified: '2026-10-06'
name: Brilliant Light Power
nav: Providers
network: true
overview: 'Brilliant Light Power is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Technology, CleanEnergy, Innovation, and Research.


  Brilliant Light Power''s developer surface includes documentation, getting-started guide, support, and 5 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brilliant Light Power Domain Security
  slug: brilliant-light-power-domain-security
  summary_line: TLSv1.3 · DMARC
slug: brilliant-light-power
tags:
- Energy
- Technology
- CleanEnergy
- Innovation
- Research
- Company
website: https://brilliantlightpower.com/
---
