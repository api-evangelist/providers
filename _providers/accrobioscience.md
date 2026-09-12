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
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accrobioscience-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.accropeutics.com/
- group: company
  title: ''
  type: About
  url: https://www.accropeutics.com/about
- group: company
  title: ''
  type: Newsroom
  url: https://www.accropeutics.com/news
- group: operate
  title: ''
  type: Contact
  url: https://www.accropeutics.com/contact
- group: company
  title: ''
  type: Partners
  url: https://www.accropeutics.com/partnerships
- group: company
  title: ''
  type: Careers
  url: https://www.accropeutics.com/join
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/95295041/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/accrobioscience
coverage:
  checked: '2026-09-06'
  detail: Accro Bioscience (Suzhou) Limited is a clinical-stage biopharmaceutical company whose product is a small-molecule drug pipeline (AC-101, AC-201, AC-003), not software; its entire public surface is the accropeutics.com corporate site — about, focus areas, pipeline, partnerships, news, join us, contact — with no developer, docs, portal or integration link anywhere in the nav or footer, and the site does not even serve a /robots.txt or /sitemap.xml. Every REST/GraphQL/agent-card, /llms.txt and /.well-known/ path probed on both www.accropeutics.com and accropeutics.com returns an identical 548-byte hard 404, verified against a random control path returning the same body and byte count; api., dev., docs., developer., portal., data. and mcp..accropeutics.com do not resolve in DNS, and there is no GitHub organization and no npm or PyPI package under either the Accro Bioscience or Accropeutics name.
  evidence:
  - status: 200
    url: https://www.accropeutics.com/
  - status: 404
    url: https://www.accropeutics.com/openapi.json
  - status: 404
    url: https://www.accropeutics.com/swagger.json
  - status: 404
    url: https://www.accropeutics.com/api-docs
  - status: 404
    url: https://www.accropeutics.com/graphql
  - status: 404
    url: https://www.accropeutics.com/developers
  - status: 404
    url: https://www.accropeutics.com/llms.txt
  - status: 404
    url: https://www.accropeutics.com/robots.txt
  - status: 404
    url: https://www.accropeutics.com/.well-known/agent-card.json
  - status: 404
    url: https://www.accropeutics.com/.well-known/agent.json
  - status: 404
    url: https://www.accropeutics.com/.well-known/api-catalog
  - status: 404
    url: https://accropeutics.com/.well-known/security.txt
  - status: 404
    url: https://www.accropeutics.com/zz-api-evangelist-control-7c1e
  - status: 200
    url: https://api.github.com/search/users?q=accro+bioscience
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: 'Accro Bioscience (Suzhou) Limited, trading as Accropeutics, is a clinical-stage biopharmaceutical company founded in 2017 with operations in Suzhou, China and New York. It develops small-molecule therapeutics against regulated cell death — necroptosis, pyroptosis and ferroptosis — targeting the cell-death-to-inflammation loop behind inflammatory, fibrotic, autoimmune and oncology disease. Its pipeline is led by AC-101, an oral selective RIPK2 inhibitor in Phase Ib for ulcerative colitis with FDA clearance for a Phase II multi-regional IBD study; AC-201, a TYK2/JAK1 pseudokinase inhibitor licensed to Fosun Pharma for Greater China as FXS5626; and AC-003, a RIPK1 inhibitor in Phase Ib for acute graft-versus-host disease with FDA Orphan Drug Designation. It closed a $50M Series C led by OrbiMed in May 2026. Accro Bioscience sells drug candidates, not software: it runs no developer program and publishes no API, SDK or machine-readable API contract.'
image: https://www.accropeutics.com/upload/2024-05/171677317462138100.svg
layout: provider
modified: '2026-09-06'
name: Accro Bioscience
nav: Providers
network: true
overview: Accro Bioscience is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and Clinical Trials.
random_paper: 10
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Accrobioscience Domain Security
  slug: accrobioscience-domain-security
  summary_line: no transport/DNS hardening detected
slug: accrobioscience
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- Clinical Trials
- Life Sciences
- Immunology
- Inflammation
- Small Molecule
- Regulated Cell Death
website: https://www.accropeutics.com/
---
