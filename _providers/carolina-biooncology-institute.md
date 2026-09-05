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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carolina-biooncology-institute-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carolina-biooncology-institute-llms.txt
- group: company
  title: ''
  type: Website
  url: https://carolinabiooncology.org/
- group: company
  title: ''
  type: About
  url: https://carolinabiooncology.org/about-us/
- group: company
  title: ''
  type: Blog
  url: https://carolinabiooncology.org/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://carolinabiooncology.org/feed/
- group: operate
  title: ''
  type: Support
  url: https://carolinabiooncology.org/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carolinabiooncology.org/privacy-policy/
- group: operate
  title: ''
  type: FAQ
  url: https://carolinabiooncology.org/faq/
- group: company
  title: ''
  type: Careers
  url: https://carolinabiooncology.org/careers/
coverage:
  checked: '2026-09-02'
  detail: Carolina BioOncology Institute is a Phase I oncology clinic and cGMP cell-processing lab, not a software vendor — its site is a 34-page WordPress brochure whose only machine-readable endpoint is the CMS's own /wp-json/ route index, and openapi.json, swagger.json, api-docs, graphql, llms.txt and every named /.well-known/ path all 404 while api. and developer. subdomains do not resolve.
  evidence:
  - status: 404
    url: https://carolinabiooncology.org/openapi.json
  - status: 404
    url: https://carolinabiooncology.org/graphql
  - status: 404
    url: https://carolinabiooncology.org/.well-known/agent-card.json
  - status: 404
    url: https://carolinabiooncology.org/llms.txt
  - status: 200
    url: https://carolinabiooncology.org/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-09-02'
description: Carolina BioOncology Institute (CBOI) is a physician-owned Phase I oncology clinical research clinic and translational laboratory in Huntersville, North Carolina, founded by Dr. John Powderly II. It runs first-in-human and early-phase immunotherapy trials for patients with advanced solid tumors, having opened more than 100 oncology trials over fifteen years, and operates the Human Applications Lab — a cGMP-capable cell-processing and biorepository facility developing autologous cellular therapies — alongside research-use-only analytical and clinical lab analysis services for trial sponsors. CBOI is the parent company of BioCytics and an openEHR Industry Partner. It publishes no public API, developer portal, SDK or machine-readable contract; the only machine-readable surface on its domain is the stock WordPress REST API its CMS emits, which is not a product API and is deliberately not registered here.
image: https://carolinabiooncology.org/wp-content/uploads/2020/09/CBOI-Logo.png
layout: provider
modified: '2026-09-02'
name: Carolina BioOncology Institute
nav: Providers
network: true
overview: 'Carolina BioOncology Institute is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Care, Oncology, Clinical Trials, and Clinical Research.


  Carolina BioOncology Institute''s developer surface includes engineering blog, support, FAQ, and 7 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Carolina Biooncology Institute Domain Security
  slug: carolina-biooncology-institute-domain-security
  summary_line: TLSv1.3 · DMARC
slug: carolina-biooncology-institute
tags:
- Company
- Health Care
- Oncology
- Clinical Trials
- Clinical Research
- Biotechnology
- Cell Therapy
- Laboratory
- Life Sciences
- North Carolina
website: https://carolinabiooncology.org/
---
