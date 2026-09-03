---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://levitasbio.com/
- group: company
  title: ''
  type: Blog
  url: https://levitasbio.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://levitasbio.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://levitasbio.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://levitasbio.com/terms-of-use/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/levitasbio-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/levitasbio-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/levitasbio-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/levitasbio-packages.yml
coverage:
  checked: '2026-08-25'
  detail: LevitasBio is a benchtop cell-separation instrument maker whose only software, LeviMetrics, ships on the LeviCell EOS itself; the whole levitasbio.com WordPress site has no developer, API, docs or portal page in its sitemap, api./developer./docs.levitasbio.com do not resolve, and every contract probe (openapi.json, llms.txt, graphql, MCP, agent card, /.well-known/*) returned 404 on the only host that exists.
  evidence:
  - status: 404
    url: https://levitasbio.com/openapi.json
  - status: 404
    url: https://levitasbio.com/llms.txt
  - status: 404
    url: https://levitasbio.com/.well-known/api-catalog
  - status: 404
    url: https://levitasbio.com/.well-known/agent-card.json
  - status: 200
    url: https://levitasbio.com/page-sitemap.xml
  - status: 200
    url: https://api.github.com/search/users?q=levitasbio
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: LevitasBio is a Menlo Park, California life-science instrumentation company, founded in 2017, that commercializes magnetic levitation technology developed at Stanford and Harvard for label-free separation and characterization of living cells. Its LeviCell family of benchtop instruments (LeviCell 1.0, LeviCell Access 1.0, LeviCell EOS and the high-throughput LeviCell 96) suspends cells in three-dimensional space and separates viable cells from dead cells and debris without antibodies, beads or other labels. The platform is surrounded by LeviPrep tissue dissociation and nuclei extraction kits, the Nuvo automated tissue prep system, LeviSelect untouched depletion kits (tissue RBC, immune cell, mouse myelin, cell debris) and LeviMetrics, an AI-based analysis software layer that reads bright-field and fluorescence imagery captured during a run to characterize the sample. Customers use the platform for viable cell enrichment, single-cell genomics, cancer profiling and 3D culture/organoid
  workflows. LevitasBio sells instruments and consumables through a direct and distributor channel and, as of this profiling pass, publishes no public developer program, API, SDK or machine-readable interface contract.
image: https://levitasbio.com/wp-content/uploads/2024/01/Levitas-Fallback-for-Social-Share-Images.png
layout: provider
modified: '2026-08-25'
name: LevitasBio
nav: Providers
network: true
overview: 'LevitasBio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Biotechnology, Laboratory Instruments, and Cell Separation.


  LevitasBio''s developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Levitasbio Plans Pricing
  plan_count: 0
  slug: levitasbio-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/levitasbio/refs/heads/main/screenshots/levitasbio-2026-09-02T150247.png
security:
- kind: domain-security
  name: Levitasbio Domain Security
  slug: levitasbio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: levitasbio
tags:
- Company
- Life Sciences
- Biotechnology
- Laboratory Instruments
- Cell Separation
- Single-Cell Genomics
- Scientific Software
- Research Tools
website: https://levitasbio.com/
---
