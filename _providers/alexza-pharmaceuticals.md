---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/alexza-pharmaceuticals/hosts/alexza-pharmaceuticals-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alexza-pharmaceuticals-hosts.yml
- group: auth
  href: https://artifacts.apis.io/alexza-pharmaceuticals/security/alexza-pharmaceuticals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alexza-pharmaceuticals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alexza.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.alexza.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Alexza Pharmaceuticals, now operating as Nova Pneuma, Inc., is a biopharmaceutical company focused on innovative inhaled therapies. The website announces its transition and highlights technology platforms such as Staccato One Breath and the commercial product Adasuve. Press releases and corporate information are available, indicating recent acquisition activities and a strategic rebranding effort.
layout: provider
modified: '2026-10-22'
name: Alexza Pharmaceuticals
nav: Providers
network: true
overview: Alexza Pharmaceuticals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharma, InhaledTherapies, Rebranding, and Technology.
random_paper: 0
score:
  band: minimal
  composite: 3.1
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
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alexza Pharmaceuticals Domain Security
  slug: alexza-pharmaceuticals-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alexza-pharmaceuticals
tags:
- Company
- Biopharma
- InhaledTherapies
- Rebranding
- Technology
website: https://www.alexza.com/
---
