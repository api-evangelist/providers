---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/depureco-com/llms/depureco-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/depureco-com-llms.txt
- group: other
  href: https://artifacts.apis.io/depureco-com/hosts/depureco-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/depureco-com-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.depureco.com/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.depureco.com
- group: company
  title: ''
  type: Blog
  url: https://www.depureco.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.depureco.com/
- group: auth
  href: https://artifacts.apis.io/depureco-com/security/depureco-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/depureco-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://depureco.com/
coverage:
  checked: '2026-11-05'
  detail: The developer portal at https://dev.depureco.com provides only product information and no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://dev.depureco.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Depureco srl è un produttore italiano di aspiratori industriali e sistemi di aspirazione centralizzata dal 1972. L’azienda offre una gamma completa di aspiratori per ambienti industriali, impianti centralizzati e soluzioni personalizzate per la gestione dei fumi e delle particelle, servendo clienti in vari settori produttivi con esperienza decennale.
image: https://www.depureco.com/wp-content/uploads/2023/04/Aspiratori-industriali-Atex.png
layout: provider
modified: '2026-11-05'
name: Depureco
nav: Providers
network: true
overview: 'Depureco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Industrial, Vacuum, Manufacturing, Italy, and Equipment.


  Depureco''s developer surface includes engineering blog, documentation, and 6 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 7.9
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
    developer_ergonomics: 21.4
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Depureco Com Domain Security
  slug: depureco-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: depureco-com
tags:
- Industrial
- Vacuum
- Manufacturing
- Italy
- Equipment
website: https://depureco.com/
---
