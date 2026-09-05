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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vita-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vitatx.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vita-therapeutics
coverage:
  checked: '2026-09-04'
  detail: 'Vita Therapeutics is a clinical-stage iPSC cell-therapy developer whose product is a biologic, not software: there is no developer program, no GitHub organization, no package on any registry, and its own corporate site at www.vitatx.com is currently unpublished and returns a Webflow 404 on every path, while the apex vitatx.com fails the TLS handshake outright.'
  evidence:
  - status: 404
    url: https://www.vitatx.com/
  - status: 404
    url: https://www.vitatx.com/.well-known/agent-card.json
  - status: 404
    url: https://www.vitatx.com/openapi.json
  - status: 404
    url: https://www.vitatx.com/llms.txt
  - status: 0
    url: https://vitatx.com/
  reason: not-a-software-company
  state: none
created: '2026-09-04'
description: 'Vita Therapeutics is a Baltimore, Maryland cell engineering company, spun out of Johns Hopkins University in 2019 and formally founded in 2020, that develops induced pluripotent stem cell (iPSC) derived cellular therapies for neuromuscular disease and solid tumors. Its programs pair an autologous approach with an allogeneic, universal hypoimmunogenic approach, and include VTA-100 and VTA-110 for limb-girdle muscular dystrophy and related muscular dystrophies such as FSHD. The company raised a $31M Series B led by Cambrian BioPharma and Solve FSHD and operates from the University of Maryland BioPark. It is a clinical-stage biotechnology company: it sells no software, runs no developer program, and publishes no public API, SDK, webhook or machine-readable contract of any kind.'
layout: provider
modified: '2026-09-04'
name: Vita Therapeutics
nav: Providers
network: true
overview: Vita Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Cell Therapy, Life Sciences, and Health.
random_paper: 14
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: domain-security
  name: Vita Therapeutics Domain Security
  slug: vita-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vita-therapeutics
tags:
- Company
- Biotechnology
- Cell Therapy
- Life Sciences
- Health
- Pharmaceuticals
- Research
website: https://www.vitatx.com/
---
