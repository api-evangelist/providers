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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peel-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://peeltx.com/
- group: company
  title: ''
  type: About
  url: https://peeltx.com/about/
- group: company
  title: ''
  type: Blog
  url: https://peeltx.com/news/
- group: operate
  title: ''
  type: Support
  url: https://peeltx.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://peeltx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://peeltx.com/site-terms/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/peel-therapeutics/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/peel-therapeutics-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Peel Therapeutics is a clinical-stage drug developer whose product is a therapeutic pipeline (EP53 nanoparticles, PEEL-224); peeltx.com is a nine-page WordPress marketing site where every developer path — /api, /developers, /docs, /openapi.json, /swagger.json, /graphql — returns the theme's 404, the Darwin.AI discovery platform is internal-only and never exposed, and the sole machine-readable surface is the CMS's default, unadvertised /wp-json/ endpoint rather than a product API.
  evidence:
  - status: 404
    url: https://peeltx.com/openapi.json
  - status: 404
    url: https://peeltx.com/developers
  - status: 404
    url: https://peeltx.com/graphql
  - status: 404
    url: https://peeltx.com/.well-known/api-catalog
  - status: 404
    url: https://peeltx.com/.well-known/agent-card.json
  - status: 200
    url: https://peeltx.com/llms.txt
  - status: 200
    url: https://peeltx.com/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Peel Therapeutics is an evolutionary-medicine biotechnology company headquartered in Salt Lake City, Utah, with research teams in the United States and Israel. Co-founded in 2015 by pediatric oncologist Dr. Joshua Schiffman, the company translates molecules that evolution has already validated in nature into therapeutics for patients with cancer and inflammatory disease. Its founding program is built on elephant p53 (EP53) — elephants carry roughly forty copies of the p53 tumor-suppressor gene against the human two — delivered as liposomal protein nanoparticles, alongside PEEL-224, a TOP1 inhibitor in clinical development. Discovery runs on the company''s proprietary, internal Darwin.AI platform and the Darwin Biobank, a comparative-oncology sample collection. Peel is a therapeutics developer rather than a software vendor: it publishes no developer program, no public API, and no machine-readable API contract.'
image: https://peeltx.com/wp-content/uploads/peel_facebook_card-scaled.jpg
layout: provider
modified: '2026-08-26'
name: Peel Therapeutics
nav: Providers
network: true
overview: 'Peel Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Healthcare.


  Peel Therapeutics'' developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 5
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
screenshot: https://raw.githubusercontent.com/api-evangelist/peel-therapeutics/refs/heads/main/screenshots/peel-therapeutics-2026-09-02T150938.png
security:
- kind: domain-security
  name: Peel Therapeutics Domain Security
  slug: peel-therapeutics-domain-security
  summary_line: TLSv1.3
slug: peel-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Healthcare
- Oncology
- Drug Discovery
- Clinical Trials
- Research
website: https://peeltx.com/
---
