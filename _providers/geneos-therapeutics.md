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
  url: https://www.geneostx.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.geneostx.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.geneostx.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.geneostx.com/press-releases/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/geneos-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/geneos-therapeutics-llms.txt
coverage:
  checked: '2026-08-16'
  detail: Geneos Therapeutics is a Phase 2b clinical-stage cancer-immunotherapy developer whose product is a DNA plasmid drug, not software; its six-page WordPress corporate site has no developer, API or technology-integration section at all, api/docs/developer(s)/portal subdomains of geneostx.com do not resolve (NXDOMAIN), there is no GitHub organization and no package in npm or PyPI, and every contract-discovery and /.well-known/ path probed returned 404.
  evidence:
  - status: 404
    url: https://www.geneostx.com/openapi.json
  - status: 404
    url: https://www.geneostx.com/.well-known/agent-card.json
  - status: 404
    url: https://www.geneostx.com/api
  - status: 404
    url: https://api.github.com/orgs/geneostx
  - status: 200
    url: https://www.geneostx.com/sitemap_index.xml
  reason: not-a-software-company
  state: none
created: '2026-08-16'
description: 'Geneos Therapeutics is a clinical-stage (Phase 2b) biotherapeutics company in Philadelphia, Pennsylvania developing DNA-based personalized immunotherapies for cancer (PICs). Its GT-EPIC neoantigen-targeting platform sequences a patient''s tumor, identifies the targetable neoantigens, and encodes up to roughly 40 of them into a synthetic DNA plasmid drug product delivered intradermally alongside a plasmid-encoded IL-12 adjuvant and CELLECTRA electroporation. Geneos was spun out of Inovio Pharmaceuticals and licenses that immunotherapy platform exclusively; it has run clinical work in hepatocellular carcinoma (HCC) and glioblastoma (GBM) and is advancing toward a Phase 2b HCC trial. Geneos is a therapeutics developer, not a software vendor: it publishes no public API, SDK, developer portal or machine-readable contract of any kind.'
image: https://www.geneostx.com/wp-content/uploads/2021/09/logo-color.svg
layout: provider
modified: '2026-08-16'
name: Geneos Therapeutics
nav: Providers
network: true
overview: 'Geneos Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Immunotherapy, and Oncology.


  Geneos Therapeutics'' developer surface includes support, engineering blog, and 4 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 8.3
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.3
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
  name: Geneos Therapeutics Domain Security
  slug: geneos-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: geneos-therapeutics
tags:
- Company
- Biotechnology
- Therapeutics
- Immunotherapy
- Oncology
- Precision Medicine
- Clinical Stage
- Life Sciences
website: https://www.geneostx.com/
---
