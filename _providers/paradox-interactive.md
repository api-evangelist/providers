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
api_count: 1
apis:
- description: API documentation for Paradox Interactive services.
  name: Paradox Interactive API
  slug: paradox-interactive-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paradox-interactive/refs/heads/main/hosts/paradox-interactive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/paradox-interactive-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paradox-interactive/refs/heads/main/vendors/paradox-interactive-vendors.yml
  title: ''
  type: Vendors
  url: vendors/paradox-interactive-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paradoxinteractive.com/games/age-of-wonders-4/quiz/terms-and-conditions
- group: start
  title: ''
  type: Sandbox
  url: https://www.paradoxinteractive.com/games/crusader-kings-iii/console
- group: company
  title: ''
  type: Newsroom
  url: https://www.paradoxinteractive.com/games/stellaris/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/paradox-interactive/refs/heads/main/security/paradox-interactive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paradox-interactive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://paradoxinteractive.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.paradoxinteractive.com/our-company
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.paradoxplaza.com/privacy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://api.paradoxplaza.com/mcp
  - status: 200
    url: https://paradoxinteractive.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Paradox Interactive is a Swedish video game developer and publisher known for grand strategy, simulation, and role‑playing titles. The company creates deep, historically‑inspired games such as Crusader Kings, Europa Universalis, Hearts of Iron, and Stellaris, serving millions of players worldwide. It operates multiple studios across Europe, focuses on community‑driven development, and offers regular expansions and downloadable content. Paradox Interactive also runs a vibrant modding community and provides tools for developers through its Paradox Plaza platform.
image: https://images.ctfassets.net/u73tyf0fa8v1/3C6nNwKRhrulkBzPucbjPj/9be1ee0d9361743b1df8daf1f302e2fe/paradox-interactive.jpg
layout: provider
modified: '2026-10-15'
name: Paradox Interactive
nav: Providers
network: true
overview: 'Paradox Interactive is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video Games, GrandStrategy, Simulation, and Community.


  Paradox Interactive''s developer surface includes sandbox, documentation, and 7 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Paradox Interactive Domain Security
  slug: paradox-interactive-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: paradox-interactive
tags:
- Company
- Video Games
- GrandStrategy
- Simulation
- Community
website: https://paradoxinteractive.com/
---
