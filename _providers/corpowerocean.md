---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/corpowerocean/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/corpowerocean/refs/heads/main/llms/corpowerocean-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/corpowerocean-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/corpowerocean/refs/heads/main/well-known/corpowerocean-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/corpowerocean-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/corpowerocean/refs/heads/main/hosts/corpowerocean-hosts.yml
  title: ''
  type: Hosts
  url: hosts/corpowerocean-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/corpowerocean/refs/heads/main/vendors/corpowerocean-vendors.yml
  title: ''
  type: Vendors
  url: vendors/corpowerocean-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/corpowerocean/refs/heads/main/security/corpowerocean-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/corpowerocean-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://corpowerocean.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://corpowerocean.com
  - status: 403
    url: https://equityzen.com/company/corpowerocean
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: CorPower Ocean AB is a wave energy technology company headquartered in Stockholm, Sweden. It develops modular wave energy converters that deliver up to five times more energy per equipment compared to conventional solutions. The company offers services from opportunity assessment to project delivery, and operates globally with offices in Oslo, Viana do Castelo, and Stromness. Its patented WaveSpring technology uses air pressure to improve buoy efficiency and resilience in harsh ocean conditions, aiming to provide clean, firm renewable power at scale.
image: https://corpowerocean.com/wp-content/uploads/2026/03/corpower-ocean-c5-wave-energy-converter-ocean-deployment.jpg
layout: provider
modified: '2026-10-11'
name: Corpowerocean
nav: Providers
network: true
overview: Corpowerocean is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, WavePower, Renewables, and Technology.
random_paper: 13
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Corpowerocean Domain Security
  slug: corpowerocean-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: corpowerocean
tags:
- Company
- Energy
- WavePower
- Renewables
- Technology
website: https://corpowerocean.com
---
