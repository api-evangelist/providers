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
- group: company
  title: ''
  type: Website
  url: https://www.kytopen.com/
- group: company
  title: ''
  type: Blog
  url: https://www.kytopen.com/news
- group: operate
  title: ''
  type: Support
  url: https://kytopen.atlassian.net/servicedesk/customer/portal/5
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kytopen
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kytopen-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kytopen-llms.txt
coverage:
  checked: '2026-08-23'
  detail: Kytopen sells Flowfect benchtop transfection instruments and consumables to biopharma labs - the product is laboratory hardware, its HubSpot marketing site has no developer section, its GitHub org has zero public repositories, and the only cloud data surface around Flowfect is Ganymede Bio's platform under Ganymede's own contract.
  evidence:
  - status: 404
    url: https://www.kytopen.com/openapi.json
  - status: 404
    url: https://www.kytopen.com/.well-known/agent-card.json
  - status: 404
    url: https://www.kytopen.com/llms.txt
  - status: 200
    url: https://api.github.com/orgs/kytopen
  - status: 200
    url: https://www.kytopen.com/products
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: 'Kytopen Corp. is a Cambridge, Massachusetts life-sciences instrument company, spun out of MIT, that builds non-viral, continuous-flow cellular engineering hardware for cell and gene therapy discovery and manufacturing. Its Flowfect technology combines continuous fluid flow with electric fields to deliver mRNA, DNA and CRISPR payloads into cells, and is sold as two benchtop platforms: Flowfect Discover, an automated small-volume system that runs up to 96 high-throughput transfections in about ten minutes, and Flowfect TX, a closed-system instrument that processes 10-50 million cells per mL at 25-50 mL per minute for GMP-scale manufacturing. The company sells laboratory instruments and consumables to biopharma and CDMO customers through a quote and technology-access motion; it publishes no developer program, no public API, and no machine-readable API contract of any kind. Instrument data integration for Flowfect customers is delivered by a third party, Ganymede Bio, under its
  own platform and its own contract - that surface belongs to Ganymede, not to Kytopen.'
image: https://www.kytopen.com/hs-fs/hubfs/raw_assets/public/Kytopen_December_2021/images/logo_300-1.png
layout: provider
modified: '2026-08-23'
name: Kytopen
nav: Providers
network: true
overview: 'Kytopen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Cell Therapy, and Gene Delivery.


  Kytopen''s developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.8
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
  name: Kytopen Domain Security
  slug: kytopen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kytopen
tags:
- Company
- Biotechnology
- Life Sciences
- Cell Therapy
- Gene Delivery
- Genome Engineering
- Laboratory Instruments
- Manufacturing
website: https://www.kytopen.com/
---
