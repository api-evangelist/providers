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
  url: security/syapse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://syapse.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/syapse
- group: build
  title: ''
  type: Packages
  url: packages/syapse-packages.yml
coverage:
  checked: '2026-08-29'
  detail: 'Syapse was fully absorbed into N-Power Medicine (stock-for-stock, closed 2024-12-30) and its entire web property was retired the same week: syapse.com and www.syapse.com now answer every path — including an invented control path — with the identical 292-byte HTML meta-refresh stub to npowermedicine.com, Last-Modified 2025-01-12, so there is no docs host, no API host and no contract left to read.'
  evidence:
  - status: 200
    url: https://syapse.com/
  - status: 200
    url: https://syapse.com/this-path-does-not-exist-9f3a
  - status: 200
    url: https://syapse.com/openapi.json
  - status: 200
    url: https://www.syapse.com/.well-known/security.txt
  - status: 404
    url: https://www.npowermedicine.com/openapi.json
  reason: defunct
  state: none
created: '2026-08-29'
description: 'Syapse was a San Francisco precision-medicine software company, founded in 2008, that built a real-world evidence platform for community oncology. Its product integrated structured clinical data from health-system EHRs with genomic/NGS results to support molecular tumor boards, care coordination, quality improvement and life-sciences research, and it ran the Syapse Learning Health Network of community health systems alongside collaborations with Roche, Amgen and the US Department of Veterans Affairs. Syapse Holdings was acquired by N-Power Medicine in a stock-for-stock exchange that closed 2024-12-30 and was announced 2025-01-12; its network of 1,000+ community oncologists, its data and technology stack, and its team were folded into N-Power Medicine''s always-on community clinical-research model. The Syapse brand has since been fully retired: syapse.com now serves nothing but a 292-byte meta-refresh stub redirecting to npowermedicine.com, dated 2025-01-12. Syapse never published
  a public developer program, and no public API, OpenAPI/AsyncAPI/GraphQL contract, SDK or developer portal survives.'
image: https://avatars.githubusercontent.com/u/1268822?v=4
layout: provider
modified: '2026-08-29'
name: Syapse
nav: Providers
network: true
overview: Syapse is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Oncology, Precision Medicine, and Real-World Evidence.
random_paper: 10
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 3.7
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
  name: Syapse Domain Security
  slug: syapse-domain-security
  summary_line: TLSv1.3 · DMARC
slug: syapse
tags:
- Company
- Healthcare
- Oncology
- Precision Medicine
- Real-World Evidence
- Clinical Research
- Health Data
- Life Sciences
- Acquired
website: https://syapse.com/
---
