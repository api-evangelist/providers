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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.airloom.energy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airloom-energy/refs/heads/main/security/airloom-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airloom-energy-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: mailto:info@airloom.energy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airloom-energy/
- group: company
  title: ''
  type: Careers
  url: https://ats.rippling.com/airloom-open-roles/jobs
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airloom-energy/refs/heads/main/llms/airloom-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airloom-energy-llms.txt
coverage:
  checked: '2026-09-19'
  detail: 'Airloom Energy is a Laramie, Wyoming wind-turbine hardware startup whose only web presence is a single-page Next.js marketing site at www.airloom.energy: no api./docs./developer./mcp. subdomain resolves, every OpenAPI/GraphQL/AsyncAPI/llms.txt and /.well-known/ path returns a real 404, its GitHub org (AirloomEnergy) has zero public repositories, and the Nasdaq Private Market page the stub carried as its Website was a secondary-market venue listing, not the company.'
  evidence:
  - status: 200
    url: https://www.airloom.energy/
  - status: 404
    url: https://www.airloom.energy/openapi.json
  - status: 404
    url: https://www.airloom.energy/docs
  - status: 404
    url: https://www.airloom.energy/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/airloomenergy
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: not-a-software-company
  state: none
created: '2026-09-19'
description: Airloom Energy is a Laramie, Wyoming wind-energy hardware company engineering next-generation utility-scale turbines that use a low-profile track-and-wing architecture instead of a conventional tower, aiming for low-cost, mass-manufacturable, high-energy-density generation that can be deployed at low-wind, height-restricted and hard-to-access sites. Backed by Breakthrough Energy Ventures, Lowercarbon Capital, MCJ, Crosscut and Woven Earth, the company ran a kilowatt-scale prototype in 2023, engineered a pilot system in 2024, is operating the pilot in 2025 and targets a commercial demonstration in 2027. It builds physical generation equipment and publishes no developer program, API, SDK or machine-readable contract.
image: https://www.airloom.energy/favicon/favicon-32x32.png
layout: provider
modified: '2026-09-19'
name: Airloom Energy
nav: Providers
network: true
overview: 'Airloom Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Wind Energy, Renewable Energy, and Clean Energy.


  Airloom Energy''s developer surface includes support and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 5.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airloom Energy Domain Security
  slug: airloom-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airloom-energy
tags:
- Company
- Energy
- Wind Energy
- Renewable Energy
- Clean Energy
- Hardware
- Climate Tech
- Utilities
website: https://www.airloom.energy/
---
