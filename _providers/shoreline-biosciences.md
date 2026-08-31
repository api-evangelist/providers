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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shoreline-biosciences-domain-security.yml
coverage:
  checked: '2026-08-27'
  detail: Shoreline Biosciences' own domain shorelinebio.com no longer serves a website — both the apex and www answer HTTP 404 with a Squarespace "Website Expired" holding page — so there is no homepage, developer area, docs host or resolvable api./docs./developer. subdomain left to profile.
  evidence:
  - status: 404
    url: https://www.shorelinebio.com/
  - status: 404
    url: https://shorelinebio.com/
  - status: 404
    url: https://www.shorelinebio.com/.well-known/agent-card.json
  - status: 404
    url: https://www.shorelinebio.com/openapi.json
  - status: 404
    url: https://www.shorelinebio.com/llms.txt
  - status: 403
    url: https://forgeglobal.com/shoreline-biosciences_stock/
  reason: defunct
  state: none
created: '2026-08-27'
description: 'Shoreline Biosciences was a San Diego, California clinical-stage biotechnology company developing off-the-shelf, allogeneic cell therapies from induced pluripotent stem cells (iPSCs), principally iPSC-derived natural killer (iNK) cells and macrophages engineered for oncology indications. It raised roughly $140M, acquired Editas Medicine''s iNK cell franchise and related gene-editing technologies in 2023, and signed collaborations with Kite Pharma (Gilead) and BeiGene with headline values above $4B. Therapeutics, not software, were the product: no developer program, API, SDK or machine-readable specification was ever published. As of this profiling pass the company''s own domain, shorelinebio.com, no longer serves a website — it answers HTTP 404 with a Squarespace "Website Expired" holding page — and the company is tracked here only as a secondary-market entity.'
layout: provider
modified: '2026-08-27'
name: Shoreline Biosciences
nav: Providers
network: true
overview: Shoreline Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Cell Therapy, and Immunotherapy.
random_paper: 10
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
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Shoreline Biosciences Domain Security
  slug: shoreline-biosciences-domain-security
  summary_line: TLSv1.3
slug: shoreline-biosciences
tags:
- Company
- Biotechnology
- Life Sciences
- Cell Therapy
- Immunotherapy
- Oncology
- Stem Cells
- Pharmaceuticals
---
