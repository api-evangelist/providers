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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/korro-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://korrobio.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.korrobio.com/
- group: company
  title: ''
  type: Careers
  url: https://korrobio.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://korrobio.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://korrobio.com/privacy-policy/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/korro-bio_stock/
coverage:
  checked: '2026-08-23'
  detail: 'Korro Bio is a clinical-stage RNA-editing biopharmaceutical company (Nasdaq: KRRO) whose product is a drug pipeline, not software — there is no developer program, no API, no SDK on npm or PyPI and no GitHub organization; korrobio.com is a WordPress marketing site that answers every path, including the root, with a SiteGround robot-challenge (HTTP 202), and api./dev./docs./developer./mcp. are wildcard DNS to the same address rather than real hosts.'
  evidence:
  - status: 202
    url: https://korrobio.com/
  - status: 202
    url: https://korrobio.com/openapi.json
  - status: 404
    url: https://ir.korrobio.com/.well-known/security.txt
  - status: 404
    url: https://ir.korrobio.com/llms.txt
  - status: 200
    url: https://ir.korrobio.com/
  - status: 200
    url: https://api.github.com/search/users?q=korro+bio
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: 'Korro Bio, Inc. (Nasdaq: KRRO) is a Cambridge, Massachusetts clinical-stage biopharmaceutical company developing a new class of genetic medicines based on programmable RNA editing. Its proprietary OPERA (Oligonucleotide Promoted Editing of RNA) platform pairs data-driven oligonucleotide design and machine-learning optimization with linker chemistry and tissue-directed delivery to recruit the body''s own ADAR enzymes and make a precise, transient single-base edit to a native mRNA transcript — editing RNA rather than DNA so the change is tunable and reversible. The company was created and incubated by Atlas Venture with New Enterprise Associates in October 2019, raised a $91.5M Series A and a $116M Series B, and became public in 2023 through a merger with Frequency Therapeutics alongside a $117M private placement. Its pipeline targets liver and central nervous system indications and includes KRRO-110 (the REWRITE Phase 1/2a study in alpha-1 antitrypsin deficiency), KRRO-111 and
  KRRO-121, which holds EMA orphan drug designation for urea cycle disorders. Korro Bio sells therapeutics, not software: it operates no developer program, publishes no API, SDK or machine-readable specification, and maintains no public source-code organization.'
layout: provider
modified: '2026-08-23'
name: Korro Bio
nav: Providers
network: true
overview: Korro Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, RNA Editing, and Genetic Medicine.
random_paper: 13
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 2
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Korro Bio Domain Security
  slug: korro-bio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: korro-bio
tags:
- Company
- Biotechnology
- Pharmaceuticals
- RNA Editing
- Genetic Medicine
- Drug Discovery
- Life Sciences
- Clinical Trials
- Rare Disease
- Research
website: https://korrobio.com/
---
