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
  url: https://asherbio.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asherbio.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asherbio.com/terms-of-use/
- group: company
  title: ''
  type: Blog
  url: https://asherbio.com/news/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://asherbio.com/news/press-releases/feed/
- group: operate
  title: ''
  type: Contact
  url: https://asherbio.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://asherbio.com/careers/
- group: company
  title: ''
  type: About
  url: https://asherbio.com/about-us/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/asher-biotherapeutics_stock/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/asher-biotherapeutics-domain-security.yml
coverage:
  checked: '2026-08-06'
  detail: Asher Bio is a clinical-stage biologics developer whose product is a drug, not software — its entire WordPress site is four sections (platform, pipeline, news, careers) with no developer, API, or docs path; asherbio.com/api, /developers and /docs all return the site's 404 page.
  evidence:
  - status: 404
    url: https://asherbio.com/api
  - status: 404
    url: https://asherbio.com/developers
  - status: 404
    url: https://asherbio.com/openapi.json
  - status: 404
    url: https://asherbio.com/.well-known/agent-card.json
  - status: 404
    url: https://asherbio.com/llms.txt
  - status: 200
    url: https://asherbio.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Asher Biotherapeutics (Asher Bio) is a privately held, clinical-stage biotechnology company founded in 2019 and headquartered at 650 Gateway Blvd. in South San Francisco, California. The company develops cis-targeted immunotherapies — engineered biologics that simultaneously engage an immunomodulatory receptor and a cell-type-specific target on the same immune cell, so a cytokine is only activated on the intended cell population rather than acting indiscriminately across immune subsets. Its lead candidate, etakafusp alfa (AB248), is a cis-targeted IL-2 directed at CD8+ effector T cells and is in Phase 1a/1b clinical development in cancer, alongside earlier-stage programs AB821 and AB359 and a cis-targeted cytokine augmentation program for cell therapies. Asher Bio is a therapeutics developer, not a software or platform company: it publishes no developer program, public API, SDK, or machine-readable interface.'
image: https://asherbio.com/wp-content/uploads/2021/03/home-page-card-Asher-032221.jpg
layout: provider
modified: '2026-08-06'
name: Asher Biotherapeutics
nav: Providers
network: true
overview: 'Asher Biotherapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Immunotherapy, Oncology, and Therapeutics.


  Asher Biotherapeutics'' developer surface includes engineering blog and 9 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/asher-biotherapeutics/refs/heads/main/screenshots/asher-biotherapeutics-2026-08-07T161754.png
security:
- kind: domain-security
  name: Asher Biotherapeutics Domain Security
  slug: asher-biotherapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asher-biotherapeutics
tags:
- Company
- Biotechnology
- Immunotherapy
- Oncology
- Therapeutics
- Clinical Stage
- Life Sciences
- Cytokines
website: https://asherbio.com/
---
