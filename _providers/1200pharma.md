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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1200pharma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://1200pharma.com/
coverage:
  checked: '2026-09-05'
  detail: '1200 Pharma is a pre-clinical small-molecule oncology discovery lab whose product is drug IP and partnerships rather than software — no GitHub organization exists, no package is published to npm or PyPI, and api/docs/developer/portal/app/data/platform hostnames all return NXDOMAIN under its domain — and its one web property, 1200pharma.com, could not be read at all because the Cloudflare edge in front of it terminates every TLS handshake with alert 40 before presenting a certificate (reproduced independently from a third-party headless-browser egress) and answers plain HTTP on every path with 409 Conflict / "error code: 1001".'
  evidence:
  - status: 0
    url: https://1200pharma.com/
  - status: 409
    url: http://1200pharma.com/
  - status: 409
    url: http://1200pharma.com/.well-known/security.txt
  - status: 200
    url: https://api.github.com/search/users?q=1200pharma
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: '1200 Pharma LLC is a privately held pre-clinical drug discovery company founded in 2017 and headquartered in Culver City, California, with roots in Pasadena. It was launched by Caltech chemist Brian Stoltz, UCLA translational oncologist Dennis Slamon and chief executive David Licata, and it pairs Caltech medicinal-chemistry methodology with UCLA biomarker-driven screening assays to identify novel small-molecule oncology candidates — including KRAS and CDK inhibitors — at a fraction of the industry-average cost and timeline. The company employs roughly 20-50 people, has filed patents covering indole-based anti-cancer compounds, and has raised approximately $14.1 million from Kairos Ventures, Vest Coast Capital, OCV Partners, Alexandria Venture Investments, Pasadena Bio and the National Institutes of Health. Its product is drug intellectual property and discovery partnerships, not software: no developer program, public API, SDK, developer portal or machine-readable contract of
  any kind could be found, and no api/docs/developer hostname exists under its domain. At the time of profiling its only web property, 1200pharma.com, was not being served — the Cloudflare edge in front of it terminated every TLS handshake and answered plain HTTP with error 1001 — so the corporate site itself could not be read.'
layout: provider
modified: '2026-09-05'
name: 1200 Pharma
nav: Providers
network: true
overview: 1200 Pharma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and Medicinal Chemistry.
random_paper: 9
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
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 1200Pharma Domain Security
  slug: 1200pharma-domain-security
  summary_line: no transport/DNS hardening detected
slug: 1200pharma
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- Medicinal Chemistry
- Oncology
- Small Molecule
- Life Sciences
- Healthcare
- United States
website: https://1200pharma.com/
---
