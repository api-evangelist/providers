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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/nutcracker-therapeutics_stock/
coverage:
  checked: '2026-08-04'
  detail: Nutcracker Therapeutics was acquired by Medici Therapeutics in December 2025; nutcrackerx.com now answers with a shared HDMZ hosting placeholder behind a mismatched *.hdmz.com certificate, its former pages (/platform/, /crdmo-services/) return 404, and the sitemap.xml it still serves belongs to an unrelated tenant (store.repligen.com).
  evidence:
  - status: 200
    url: https://www.nutcrackerx.com/
  - status: 404
    url: https://www.nutcrackerx.com/platform/
  - status: 404
    url: https://www.nutcrackerx.com/.well-known/agent-card.json
  - status: 404
    url: https://www.nutcrackerx.com/openapi.json
  - status: 404
    url: https://www.nutcrackerx.com/llms.txt
  reason: defunct
  state: none
created: '2026-08-04'
description: Nutcracker Therapeutics was an RNA therapeutics company founded in 2018 and headquartered in Emeryville, California, operating as a contract research, development and manufacturing organization (CRDMO) for RNA-based medicines. Its ACORN platform compressed RNA drug manufacturing onto single-use microfluidic biochips, and its NMU-Symphony system targeted on-demand, individualized production of personalized RNA therapeutics. The company raised more than $200 million across Series A through C rounds led by ARCH Venture Partners and others. Its business was laboratory instrumentation and GMP biomanufacturing services, not software, and it never published a developer program, public API, SDK or machine-readable specification. In December 2025 the company was acquired by Medici Therapeutics, the oncology platform formed by ARCH Venture Partners and the Parker Institute for Cancer Immunotherapy. Its corporate site at nutcrackerx.com went dark shortly afterwards and now returns a shared
  hosting placeholder.
layout: provider
modified: '2026-08-04'
name: Nutcracker Therapeutics
nav: Providers
network: true
overview: Nutcracker Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, RNA, and Therapeutics.
random_paper: 1
score:
  band: minimal
  composite: 1.8
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
    - owner: catalog
      reason: never_enriched
  previous_composite: 1.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
slug: nutcracker-therapeutics
tags:
- Company
- Biotechnology
- Life Sciences
- RNA
- Therapeutics
- Biomanufacturing
- Acquired
website: https://forgeglobal.com/nutcracker-therapeutics_stock/
---
