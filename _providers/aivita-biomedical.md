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
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aivita-biomedical/refs/heads/main/security/aivita-biomedical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aivita-biomedical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aivitabiomedical.com/
coverage:
  checked: 2026-09-22
  detail: The site renders documentation via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 406
    url: https://aivitabiomedical.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-22'
description: AIVITA Biomedical is a biotechnology company developing personalized vaccines for the prevention of infectious diseases and treatment of cancer. It uses an autologous cell platform to create multi‑pathogen vaccine kits and novel cancer immunotherapies, leveraging stem‑cell technology for safe, efficient manufacturing. The company was founded in 2016 and focuses on personalized medicine, with programs in cancer, infectious disease, vision loss, and skincare.
layout: provider
modified: '2026-09-22'
name: AiVita Biomedical
nav: Providers
network: true
overview: AiVita Biomedical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Personalized Medicine, Cancer, Infectious Disease, and Stem Cell.
random_paper: 0
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  previous_composite: 4.6
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aivita Biomedical Domain Security
  slug: aivita-biomedical-domain-security
  summary_line: TLSv1.3
slug: aivita-biomedical
tags:
- Biotechnology
- Personalized Medicine
- Cancer
- Infectious Disease
- Stem Cell
website: https://aivitabiomedical.com/
---
