---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alumis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alumis.com/
- group: company
  title: ''
  type: About
  url: https://www.alumis.com/about/
- group: company
  title: ''
  type: Careers
  url: https://www.alumis.com/careers/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alumis.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alumis-co/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/_Alumis
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.alumis.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/alumis_stock/
coverage:
  checked: '2026-08-06'
  detail: Alumis is a clinical-stage biopharmaceutical company whose product is oral TYK2/IGF-1R drug candidates, not software; its site has only about/science/pipeline/patients/careers sections and every developer-shaped path (/developers, /api, /docs, /openapi.json, /graphql, /llms.txt, /.well-known/*) returns a hard 404, and the only "alumis" GitHub org is an unrelated Scandinavian TypeScript/C# shop.
  evidence:
  - status: 404
    url: https://www.alumis.com/developers
  - status: 404
    url: https://www.alumis.com/openapi.json
  - status: 404
    url: https://www.alumis.com/.well-known/agent-card.json
  - status: 404
    url: https://www.alumis.com/llms.txt
  - status: 200
    url: https://www.alumis.com/
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Alumis Inc. (NASDAQ: ALMS) is a clinical-stage biopharmaceutical company headquartered at 280 East Grand Avenue, South San Francisco, California, developing oral therapies for immune-mediated diseases. Incorporated in 2021 as Esker Therapeutics and renamed Alumis in January 2022, its pipeline is led by envudeucitinib, an oral allosteric TYK2 inhibitor in Phase 3 for moderate-to-severe plaque psoriasis and systemic lupus erythematosus; A-005, a CNS-penetrant TYK2 inhibitor for neuroinflammatory and neurodegenerative disease; and lonigutamab, a subcutaneously delivered anti-IGF-1R antibody for thyroid eye disease. Alumis describes a proprietary precision data-analytics platform that integrates genetic, genomic, proteomic, biological and clinical insight, but it is an internal therapeutic-development capability and is not exposed publicly. The company publishes no developer portal, API documentation, SDKs or machine-readable specifications.'
image: https://www.alumis.com/themes/default/images/logo.svg
layout: provider
modified: '2026-08-06'
name: Alumis
nav: Providers
network: true
overview: Alumis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Healthcare.
random_paper: 71
score:
  band: minimal
  composite: 7.9
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alumis/refs/heads/main/screenshots/alumis-2026-08-07T161254.png
security:
- kind: domain-security
  name: Alumis Domain Security
  slug: alumis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alumis
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Healthcare
- Immunology
- Drug Development
- Clinical Trials
website: https://www.alumis.com/
---
