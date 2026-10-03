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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avationmedical/refs/heads/main/security/avationmedical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avationmedical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avation.com
- group: company
  title: ''
  type: Blog
  url: https://avation.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://avation.com/clinical-evidence
- group: start
  title: ''
  type: GettingStarted
  url: https://avation.com/how-vivally-works
- group: operate
  title: ''
  type: Support
  url: https://avation.com/contact
created: '2026-09-26'
description: Avation Medical manufactures the Vivally System, the only FDA‑cleared wearable closed‑loop neuromodulation device for overactive bladder. The company provides at‑home treatment using transcutaneous tibial nerve stimulation, offering patients a non‑invasive solution for urge urinary incontinence. Avation focuses on digital health and neuromodulation, delivering clinical evidence, patient resources, and a leadership team dedicated to advancing medical technology.
layout: provider
modified: '2026-09-26'
name: Avationmedical
nav: Providers
network: true
overview: 'Avationmedical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Devices, Digital Health, Neuromodulation, WearableTech, and OveractiveBladder.


  Avationmedical''s developer surface includes engineering blog, documentation, getting-started guide, support, and 2 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avationmedical Domain Security
  slug: avationmedical-domain-security
  summary_line: TLSv1.3 · HSTS
slug: avationmedical
tags:
- Medical Devices
- Digital Health
- Neuromodulation
- WearableTech
- OveractiveBladder
website: https://avation.com
---
