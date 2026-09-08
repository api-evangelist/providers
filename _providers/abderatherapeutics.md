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
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.abderatx.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/abderatherapeutics
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abderatherapeutics-domain-security.yml
coverage:
  checked: '2026-09-06'
  detail: Abdera Therapeutics is a clinical-stage radiopharmaceutical developer whose product is a drug candidate (ABD-147, ABD-320), not software — there is no developer program to profile, and the point is moot in any case because its entire corporate site at www.abderatx.com now returns a Flywheel "Unknown Domain" 404 on every path, including the root, behind a TLS certificate that expired on 2026-07-19.
  evidence:
  - status: 404
    url: https://www.abderatx.com/
  - status: 404
    url: https://abderatx.com/pipeline/
  - status: 404
    url: https://abderatx.com/.well-known/security.txt
  - status: 404
    url: https://abderatx.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/abderatx
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: Abdera Therapeutics is a clinical-stage biopharmaceutical company headquartered in South San Francisco, California, with research operations in Vancouver, British Columbia. It was launched in 2021 out of adMare BioInnovations with AbCellera as a founding partner and has raised roughly $148 million from investors including Versant Ventures, Foresite Capital, Johnson & Johnson Innovation (JJDC), Qiming Venture Partners USA, RTW Investments and venBio. The company engineers precision radiopharmaceuticals for solid tumours on its proprietary Radio Optimized Vector Engineering (ROVEr) platform, which pairs antibody-derived targeting vectors with potent alpha-emitting radioisotopes such as actinium-225. Its lead candidate, ABD-147, targets delta-like ligand 3 (DLL3) and is in a Phase 1 trial (NCT06736418) in small cell lung cancer and large cell neuroendocrine carcinoma under FDA Fast Track designation; a second program, ABD-320, targets 5T4. Abdera's product is a drug candidate,
  not software. It runs no developer program and publishes no API, developer portal, API reference, SDK, or machine-readable specification of any kind. As of 2026-09-06 the company's own corporate site at www.abderatx.com was additionally unreachable, returning a Flywheel "Unknown Domain" host error on every path behind a TLS certificate that expired on 2026-07-19.
layout: provider
modified: '2026-09-06'
name: Abdera Therapeutics
nav: Providers
network: true
overview: Abdera Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Radiopharmaceuticals, and Oncology.
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
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Abderatherapeutics Domain Security
  slug: abderatherapeutics-domain-security
  summary_line: DMARC
slug: abderatherapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Radiopharmaceuticals
- Oncology
- Drug Development
- Clinical Trials
- Life Sciences
website: https://www.abderatx.com/
---
