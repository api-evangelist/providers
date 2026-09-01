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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clasp-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clasp-therapeutics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.clasptx.com/
- group: company
  title: ''
  type: Blog
  url: https://www.clasptx.com/press-release-publications
- group: company
  title: ''
  type: BlogRSS
  url: https://www.clasptx.com/press-release-publications?format=rss
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clasptx.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clasp-therapeutics/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/clasp-therapeutics-stock
coverage:
  checked: '2026-08-09'
  detail: Clasp Therapeutics is a clinical-stage biotech whose product is a T cell engager drug candidate in a Phase 1 trial; its 41-URL Squarespace sitemap contains only leadership, founders, board, press-release and privacy-policy pages, and no api./developer./docs. subdomain resolves in DNS.
  evidence:
  - status: 200
    url: https://www.clasptx.com/sitemap.xml
  - status: 404
    url: https://www.clasptx.com/openapi.json
  - status: 404
    url: https://www.clasptx.com/developers
  - status: 404
    url: https://www.clasptx.com/graphql
  - status: 404
    url: https://www.clasptx.com/llms.txt
  - status: 404
    url: https://www.clasptx.com/.well-known/agent-card.json
  - status: 404
    url: https://www.clasptx.com/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: Clasp Therapeutics, Inc. is a clinical-stage precision immuno-oncology company developing next-generation T cell engagers (TCEs) built on its proprietary pHLAre platform, which redirects T cells to mutant peptides — such as p53 R175H and mutant KRAS — presented by specific HLA molecules on the surface of tumor cells. The approach is intended to yield off-the-shelf, antibody-like medicines that hit common oncogenic driver mutations with tumor-exclusive specificity. Its lead candidate CLSP-1025 (p53 R175H / HLA-A*02:01) is in the Phase 1 GUARDIAN-101 trial (NCT06778863), and CLSP-5282, a first-in-class KRas-directed TCE, was unveiled at AACR 2026. Founded on research from Bert Vogelstein, Drew Pardoll and colleagues at Johns Hopkins, the company launched in March 2024 with $150 million led by Catalio Capital Management, Third Rock Ventures and Novo Holdings, and operates from Cambridge, Massachusetts and Rockville, Maryland. Clasp Therapeutics is a therapeutics developer and publishes
  no public API, developer program, SDK, or machine-readable specification.
image: http://static1.squarespace.com/static/65d6268f8ea1f7001e49412c/t/65dea444ac80a07c1b522dbc/1709089860325/Clasp-logo-white-RGB.png?format=1500w
layout: provider
modified: '2026-08-09'
name: Clasp Therapeutics
nav: Providers
network: true
overview: 'Clasp Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Immuno-Oncology, Oncology, and Therapeutics.


  Clasp Therapeutics'' developer surface includes engineering blog and 7 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 3
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Clasp Therapeutics Domain Security
  slug: clasp-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: clasp-therapeutics
tags:
- Company
- Biotechnology
- Immuno-Oncology
- Oncology
- Therapeutics
- T Cell Engagers
- Precision Medicine
- Clinical Stage
- Life Sciences
website: https://www.clasptx.com/
---
