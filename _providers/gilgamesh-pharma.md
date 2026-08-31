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
  url: security/gilgamesh-pharma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gilgameshpharmaceutical.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gilgamesh-pharmaceuticals/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/gilgameshrx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mcusercontent.com/6c3f21fb747d330b7d588cc87/files/e79eefcc-bae9-6748-dc85-17d889fdb1af/Gilgamesh_Privacy_and_Expanded_Access_Policy_08.14.26.pdf
- group: other
  title: ''
  type: Listing
  url: https://forgeglobal.com/gilgamesh-pharma_stock/
coverage:
  checked: '2026-08-21'
  detail: Gilgamesh Pharma is a clinical-stage drug developer whose entire web presence is a single static marketing page on tiiny.host; /developers, /api, /docs, /openapi.json, /graphql, /llms.txt and every /.well-known/ path all return the site's own 404, and the company ships molecules (bretisilocin, blixeprodil) rather than software, so there is no API to publish.
  evidence:
  - status: 200
    url: https://www.gilgameshpharmaceutical.com/
  - status: 404
    url: https://www.gilgameshpharmaceutical.com/developers
  - status: 404
    url: https://www.gilgameshpharmaceutical.com/openapi.json
  - status: 404
    url: https://www.gilgameshpharmaceutical.com/.well-known/agent-card.json
  reason: not-a-software-company
  state: none
created: '2026-08-21'
description: 'Gilgamesh Pharma (Gilgamesh Pharmaceuticals, Inc.) is a New York based clinical-stage neuroscience company founded in 2019 that develops rapid-acting, next-generation therapeutics for psychiatric and substance use disorders. Its discovery and translational platform combines medicinal chemistry, neurocircuitry science, electrophysiology and machine learning to identify new chemical entities, and its pipeline spans short-acting 5-HT2A receptor agonists, NMDA receptor antagonists, non-hallucinogenic neuroplastogens, cardiac-safe ibogaine analogs and M1/M4 muscarinic programs. Lead assets include bretisilocin (GM-2505), acquired by AbbVie in August 2025, and blixeprodil (GM-1020), an orally bioavailable NMDAR antagonist in Phase 2 for major depressive disorder. Gilgamesh is a drug developer, not a software vendor: it publishes no developer program, public API, SDK or machine-readable specification of any kind.'
layout: provider
modified: '2026-08-21'
name: Gilgamesh Pharma
nav: Providers
network: true
overview: Gilgamesh Pharma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Biotechnology, Life Sciences, and Neuroscience.
random_paper: 6
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 2
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Gilgamesh Pharma Domain Security
  slug: gilgamesh-pharma-domain-security
  summary_line: TLSv1.3
slug: gilgamesh-pharma
tags:
- Company
- Pharmaceuticals
- Biotechnology
- Life Sciences
- Neuroscience
- Mental Health
- Clinical Trials
- Drug Discovery
- Health
website: https://www.gilgameshpharmaceutical.com/
---
