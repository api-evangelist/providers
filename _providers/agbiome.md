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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-12'
  detail: AgBiome wound down across 2023-2024 — all 123 staff on a WARN notice, Howler and Theia sold to Certis Biologicals in March 2024 and the microbial platform sold to Ginkgo Bioworks in April 2024 — and agbiome.com now answers from a Nexcess shared-hosting placeholder under a mismatched CN=nxcli.net certificate, returning a bare Apache 403 on every /.well-known/ path and 404 on /openapi.json, /llms.txt, /robots.txt and /apis.json, while api., docs., developer., app. and status.agbiome.com are all NXDOMAIN and a Wayback sweep of every archived agbiome.com path from 2014 to 2026 finds no developer or specification URL.
  evidence:
  - status: 200
    url: https://agbiome.com/
  - status: 404
    url: https://agbiome.com/openapi.json
  - status: 404
    url: https://agbiome.com/llms.txt
  - status: 403
    url: https://agbiome.com/.well-known/agent-card.json
  - status: 403
    url: https://agbiome.com/.well-known/agent.json
  - status: 403
    url: https://agbiome.com/.well-known/security.txt
  - status: 404
    url: https://agbiome.com/apis.json
  - status: 525
    url: https://portal.agbiome.com/
  - status: 403
    url: https://blog.agbiome.com/
  - status: 200
    url: https://api.github.com/orgs/agbiome
  reason: defunct
  state: none
created: '2026-09-12'
description: 'AgBiome was an agricultural biotechnology company headquartered in Research Triangle Park, Durham, North Carolina. Founded in 2012 by Scott Uknes, Eric Ward, Jeff Dangl, John Ryals and Paul Schulze-Lefert, it built the proprietary GENESIS discovery platform — a collection of more than 100,000 fully sequenced, isolated plant-associated microbial strains and hundreds of millions of gene sequences, screened with high-throughput assays for insect, disease and nematode control — and turned it into crop-protection biologicals. It commercialized the Howler and Theia biofungicides and had a third, Esendo, before the EPA, and it spun out the genome-editing venture LifeEDIT Therapeutics in October 2020 (acquired by ElevateBio in October 2021). Backed by Syngenta, Novozymes, Monsanto, ARCH Venture Partners, Polaris, the Bill & Melinda Gates Foundation, Pontifax and UTIMCO, the company nonetheless failed to raise further capital: it filed a North Carolina WARN notice in late 2023 covering
  its entire staff of 123, sold Howler and Theia to Certis Biologicals (a Mitsui & Co. subsidiary) in March 2024, and sold its platform assets to Ginkgo Bioworks in April 2024 for roughly $18.2 million in stock. AgBiome never published a developer program, public API, SDK, or machine-readable specification, and agbiome.com no longer serves the company site — it answers from a Nexcess shared-hosting placeholder under a certificate issued to CN=nxcli.net. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-09-12'
name: AgBiome
nav: Providers
network: true
overview: AgBiome is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Agriculture, AgTech, and Biotechnology.
random_paper: 20
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: agbiome
tags:
- Company
- Defunct
- Agriculture
- AgTech
- Biotechnology
- Microbiology
- Crop Protection
- Biologicals
- Life Sciences
- Research
---
