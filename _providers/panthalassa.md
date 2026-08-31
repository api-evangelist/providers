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
  url: https://panthalassa.com/
- group: company
  title: ''
  type: Careers
  url: https://panthalassa.com/join
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/p9a/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/_panthalassa
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@panthalassa.energy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/panthalassa-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/panthalassa-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Panthalassa is a pre-commercial ocean wave-energy hardware company whose entire public web presence is two Prismic-backed pages (a homepage and a Greenhouse-fed careers page); it resolves no api/docs/developer/app/mcp subdomain, has no GitHub organization, and every /.well-known/ and spec path on panthalassa.com returns a hard 404.
  evidence:
  - status: 200
    url: https://panthalassa.com/
  - status: 404
    url: https://panthalassa.com/openapi.json
  - status: 404
    url: https://panthalassa.com/.well-known/api-catalog
  - status: 404
    url: https://panthalassa.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/panthalassa
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Panthalassa is a Portland, Oregon public-benefit corporation founded in 2016 that builds ocean wave-energy "nodes" — a buoyant sphere and central tube that convert deep-water wave motion into electricity in the open ocean. Rather than transmitting power to shore, the company pairs each node with sealed, seawater-cooled compute containers so the electrons power AI and data-center workloads at sea, backhauled over satellite link. It has run the Ocean-2 Pacific pilot and markets no public API, SDK, developer portal or machine-readable contract; this profile records that absence and the company's public web surface.
image: https://panthalassa.com/images/favicon.png
layout: provider
modified: '2026-08-26'
name: Panthalassa
nav: Providers
network: true
overview: 'Panthalassa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Renewable Energy, Wave Energy, and Ocean.


  Panthalassa''s developer surface includes YouTube channel and 6 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 3.3
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
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Panthalassa Domain Security
  slug: panthalassa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: panthalassa
tags:
- Company
- Energy
- Renewable Energy
- Wave Energy
- Ocean
- Data Centers
- Compute
- Climate Tech
- Hardware
- Public Benefit Corporation
website: https://panthalassa.com/
---
