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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brexogen/refs/heads/main/hosts/brexogen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brexogen-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brexogen/refs/heads/main/security/brexogen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brexogen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://brexogen.com
coverage:
  checked: '2026-10-03'
  detail: The website renders only a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: http://brexogen.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Brexogen is a biotechnology company focused on developing exosome‑based therapeutics for dermatological and autoimmune conditions. Founded in 2020, the firm combines advanced RNA‑delivery platforms with proprietary pipelines to create next‑generation treatments. Brexogen’s public website provides detailed information on its pipeline, research collaborations, leadership team, and investor relations, indicating an active presence in the biotech sector.
layout: provider
modified: '2026-10-03'
name: Brexogen
nav: Providers
network: true
overview: Brexogen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Exosomes, and Healthcare.
random_paper: 0
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 4
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brexogen Domain Security
  slug: brexogen-domain-security
  summary_line: no transport/DNS hardening detected
slug: brexogen
tags:
- Company
- Biotechnology
- Therapeutics
- Exosomes
- Healthcare
website: http://brexogen.com
---
