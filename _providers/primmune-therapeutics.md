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
- group: company
  title: ''
  type: Website
  url: https://www.primmunerx.com/
- group: company
  title: ''
  type: Blog
  url: https://www.primmunerx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.primmunerx.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.primmunerx.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/primmune-therapeutics-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/primmune-therapeutics-domain-security.yml
coverage:
  checked: '2026-08-26'
  detail: 'Primmune is a clinical-stage drug developer whose product is the oral TLR7 agonist PRTX007, not software: its single public host www.primmunerx.com is a WordPress marketing and investor site where /openapi.json, /swagger.json, /api-docs, /graphql, /mcp and every /.well-known/ path return 404, and the only machine-readable surfaces are a Yoast-generated /llms.txt listing team and press-release pages and WordPress''s stock /wp-json/ CMS endpoint, which is theme infrastructure rather than an API the company publishes.'
  evidence:
  - status: 404
    url: https://www.primmunerx.com/openapi.json
  - status: 404
    url: https://www.primmunerx.com/graphql
  - status: 404
    url: https://www.primmunerx.com/.well-known/agent-card.json
  - status: 200
    url: https://www.primmunerx.com/llms.txt
  - status: 200
    url: https://www.primmunerx.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Primmune Therapeutics is a clinical-stage biotechnology company headquartered in Carlsbad, California, developing systemic cancer immunotherapies designed to activate the immune system in a precise and controlled manner. Its lead program, PRTX007, is an orally administered, systemically active small-molecule agonist of toll-like receptor 7 (TLR7) engineered to activate plasmacytoid dendritic cells so they produce interferons, enhance antigen presentation, recruit natural killer cells and support cytotoxic T cell expansion, while minimizing pro-inflammatory signaling. The company was founded by researchers in oral small-molecule drug design and immune agonist pharmacology and has completed Phase 1 evaluation in healthy volunteers. Primmune operates no developer program and publishes no API product, SDK, or interface contract; its public web presence is a WordPress marketing and investor-relations site, whose only machine-readable surfaces are the Yoast-generated /llms.txt and
  WordPress's default /wp-json/ CMS endpoint.
image: https://www.primmunerx.com/wp-content/uploads/2017/12/cropped-primmune-favicon-192x192.png
layout: provider
modified: '2026-08-26'
name: Primmune Therapeutics
nav: Providers
network: true
overview: 'Primmune Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Clinical Stage, and Immunotherapy.


  Primmune Therapeutics'' developer surface includes engineering blog and 5 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Primmune Therapeutics Domain Security
  slug: primmune-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: primmune-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Clinical Stage
- Immunotherapy
- Oncology
- Life Sciences
- Drug Discovery
website: https://www.primmunerx.com/
---
