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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 0
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/johnson-and-johnson/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vinetiworks
coverage:
  checked: '2026-08-05'
  detail: Vineti's PTM software was acquired by Johnson & Johnson in 2023 and the company no longer operates — vineti.com has no A record at all (its name servers are now ns01-04.jnjdns.com), every subdomain probed (api., app., docs., developer., portal., status.) is NXDOMAIN, and the last Wayback capture of the site is 2023-04-07, so there is no host left to run contract discovery against.
  evidence:
  - status: 0
    url: https://vineti.com/
  - status: 0
    url: https://api.vineti.com/openapi.json
  - status: 0
    url: https://vineti.com/.well-known/agent-card.json
  - status: 200
    url: https://web.archive.org/web/20230407042038/https://vineti.com/
  - status: 200
    url: https://github.com/vinetiworks
  reason: defunct
  state: none
created: '2026-08-05'
description: 'Vineti was an enterprise software company for cell and gene therapy supply chain management, headquartered in San Francisco and founded in 2016. Its Personalized Therapy Management (PTM) platform — sold as PTM Enterprise and PTM Essentials — orchestrated the patient-centric supply chain behind autologous and allogeneic cell therapies, gene therapies and personalized cancer vaccines: chain of identity, chain of custody, apheresis and manufacturing scheduling, clinical-site workflows, and regulatory reporting. PTM was delivered as a configurable aPaaS on AWS, with HIPAA compliance certified by Avertium and GAMP-aligned validation. Vineti was named a World Economic Forum Technology Pioneer and raised a $35M Series C in 2020. The PTM software was acquired by Johnson & Johnson in 2023 to continue supporting its commercial therapy rollouts and clinical trials, and Vineti ceased to operate as an independent company: vineti.com no longer resolves and the domain now sits on Johnson
  & Johnson name servers. This profile is retained as a historical record — there is no live API surface to catalog.'
image: https://web.archive.org/web/2023id_/https://vineti.com/wp-content/uploads/2021/05/cropped-Vineti_Favicon-1-192x192.png
layout: provider
modified: '2026-08-05'
name: Vineti
nav: Providers
network: true
overview: Vineti is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cell and Gene Therapy, Life Sciences, Supply Chain, and Healthcare.
random_paper: 4
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 0
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  previous_composite: 2.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
slug: vineti
tags:
- Company
- Cell and Gene Therapy
- Life Sciences
- Supply Chain
- Healthcare
- Clinical Trials
- Pharmaceuticals
- Enterprise Software
- Defunct
---
