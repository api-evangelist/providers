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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mozart-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mozart-tx.com/
- group: company
  title: ''
  type: About
  url: https://www.mozart-tx.com/about/
- group: other
  title: ''
  type: Science
  url: https://www.mozart-tx.com/science/
- group: other
  title: ''
  type: Pipeline
  url: https://www.mozart-tx.com/pipeline/
- group: company
  title: ''
  type: News
  url: https://www.mozart-tx.com/news/news-releases/
- group: company
  title: ''
  type: Careers
  url: https://www.mozart-tx.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.mozart-tx.com/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mozart-therapeutics
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/mozart-therapeutics_stock/
coverage:
  checked: '2026-08-26'
  detail: Mozart Therapeutics is a privately held clinical-stage biopharmaceutical company whose product is a bispecific-antibody pipeline (MTX-101, MTX-201), not software — www.mozart-tx.com is an eight-page brochure site (about, science, pipeline, news, careers, contact) with no developer, docs or API section, no robots.txt or sitemap.xml, and a real HTTP 404 on every spec path probed (/openapi.json, /swagger.json, /graphql, /llms.txt, all five /.well-known/ documents); mozart-tx.com serves wildcard DNS so api./docs./developer./mcp. resolve to the marketing site's address but no TLS service answers on them, there is no GitHub organization under any Mozart spelling, and no first-party package exists on npm or PyPI.
  evidence:
  - status: 200
    url: https://www.mozart-tx.com/
  - status: 404
    url: https://www.mozart-tx.com/openapi.json
  - status: 404
    url: https://www.mozart-tx.com/llms.txt
  - status: 404
    url: https://www.mozart-tx.com/robots.txt
  - status: 404
    url: https://www.mozart-tx.com/.well-known/agent-card.json
  - status: 404
    url: https://www.mozart-tx.com/developers/
  - status: 404
    url: https://dev.mozart-tx.com/openapi.json
  - status: 200
    url: https://api.github.com/search/users?q=mozart-therapeutics
  - status: 404
    url: https://pypi.org/pypi/mozart-therapeutics/json
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Mozart Therapeutics, Inc. is a privately held, clinical-stage biopharmaceutical company in Seattle, Washington, founded in 2020 to develop disease-modifying therapies for autoimmune and inflammatory disease. Its platform is built on the regulatory CD8 T cell (CD8 Treg) network — an upstream immune checkpoint that normally recognizes and eliminates the pathogenic immune cells that attack healthy tissue, and that becomes dysfunctional in autoimmune disease when inhibitory killer immunoglobulin-like receptors (KIR) block CD8 Treg activation. Rather than suppressing downstream inflammation, Mozart engineers bispecific CD8 Treg modulators intended to restore that checkpoint and re-establish long-term immune balance. Its pipeline comprises MTX-101, a KIR x CD8 bispecific antibody in Phase 1b study for type 1 diabetes, and MTX-201, a KIR x ICOS bispecific in preclinical development for inflammatory bowel disease. The company launched with a $55M Series A led by ARCH Venture Partners
  and Sofinnova Partners with participation from Eli Lilly, MRL Ventures Fund, Leaps by Bayer, Altitude Life Science Ventures and Alexandria Venture Investments, and later added a $25M extension including Pfizer Ventures, AbbVie Ventures, Ono Venture Investment and UPMC Enterprises. Mozart Therapeutics sells therapeutics, not software: it runs no developer program, publishes no API, SDK or machine-readable specification, and maintains no public source-code organization.'
image: https://www.mozart-tx.com/themes/default/images/logo_color.svg
layout: provider
modified: '2026-08-26'
name: Mozart Therapeutics
nav: Providers
network: true
overview: 'Mozart Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Immunology, and Autoimmune Disease.


  Mozart Therapeutics'' developer surface includes product news and 9 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
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
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mozart-therapeutics/refs/heads/main/screenshots/mozart-therapeutics-2026-09-02T150641.png
security:
- kind: domain-security
  name: Mozart Therapeutics Domain Security
  slug: mozart-therapeutics-domain-security
  summary_line: TLSv1.3
slug: mozart-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Immunology
- Autoimmune Disease
- Drug Discovery
- Life Sciences
- Clinical Trials
- Bispecific Antibodies
- Research
website: https://www.mozart-tx.com/
---
