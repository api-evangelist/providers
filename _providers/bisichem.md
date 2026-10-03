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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bisichem/refs/heads/main/hosts/bisichem-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bisichem-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bisichem/refs/heads/main/security/bisichem-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bisichem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bisichem.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bisichem.com/default/
- group: docs
  title: ''
  type: Documentation
  url: https://bisichem.com/default/
- group: company
  title: ''
  type: AboutUs
  url: https://bisichem.com/default/#about
- group: operate
  title: ''
  type: Contact
  url: https://bisichem.com/default/#contact
- group: company
  title: ''
  type: News
  url: https://bisichem.com/default/#news
coverage:
  checked: '2026-09-28'
  detail: The developer portal at https://bisichem.com/default/ returns a JavaScript shell with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://bisichem.com/default/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: BiSiChem is a leading biotech company focused on discovery and development of innovative therapeutic drugs in immuno‑oncology, targeted therapy, and neuro‑degenerative diseases. They partner early‑stage programs, retain profit rights, and aim for first‑in‑class or second‑generation small‑molecule drugs, emphasizing good lives, better innovation, and best therapy.
layout: provider
modified: '2026-09-28'
name: Bisichem
nav: Providers
network: true
overview: 'Bisichem is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Drug Discovery, Immuno-Oncology, Targeted Therapy, and Neurodegenerative.


  Bisichem''s developer surface includes documentation, product news, and 6 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bisichem Domain Security
  slug: bisichem-domain-security
  summary_line: TLSv1.2
slug: bisichem
tags:
- Biotechnology
- Drug Discovery
- Immuno-Oncology
- Targeted Therapy
- Neurodegenerative
website: https://bisichem.com
---
