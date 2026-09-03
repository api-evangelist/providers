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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sonothera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sonothera.com/
- group: company
  title: ''
  type: About
  url: https://sonothera.com/about-us/
- group: other
  title: ''
  type: Research
  url: https://sonothera.com/science/
- group: company
  title: ''
  type: News
  url: https://sonothera.com/news/
- group: company
  title: ''
  type: Careers
  url: https://sonothera.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://sonothera.com/contact-us/
- group: operate
  title: ''
  type: Support
  url: https://sonothera.com/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sonothera
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sonothera-llms.txt
coverage:
  checked: '2026-08-28'
  detail: SonoThera is a clinical-stage, ultrasound-mediated gene therapy company founded in 2022 whose product is a preclinical drug pipeline (DMD and ADPKD), not software — sonothera.com is a seven-page WordPress marketing site on WP Engine with no developer, docs or API section, every contract-discovery path (/openapi.json, /swagger.json, /api-docs, /docs, /api, /developers) and every /.well-known/* path returns a real 404, api./dev./docs./developer./mcp..sonothera.com are NXDOMAIN rather than wildcarded, and api.github.com/orgs/sonothera 404s, so there is no organization, package or specification anywhere to harvest.
  evidence:
  - status: 200
    url: https://sonothera.com/
  - status: 404
    url: https://sonothera.com/openapi.json
  - status: 404
    url: https://sonothera.com/api-docs
  - status: 404
    url: https://sonothera.com/developers
  - status: 404
    url: https://sonothera.com/.well-known/security.txt
  - status: 404
    url: https://sonothera.com/.well-known/agent-card.json
  - status: 404
    url: https://sonothera.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/sonothera
  reason: not-a-software-company
  state: none
created: '2026-08-28'
description: 'SonoThera, Inc. is a privately held, clinical-stage biotechnology company headquartered at 201 Haskins Way in South San Francisco, California, founded in 2022 to make genetic medicine deliverable without a viral vector. Its RIPPLE platform pairs an intravenously administered lipid-and-microbubble formulation with an externally applied diagnostic ultrasound probe: the acoustic energy transiently permeabilizes cell membranes in the targeted organ so a nucleic-acid payload enters only where the probe is pointed, an approach built on the roughly 35 million ultrasound contrast-agent doses given safely each year in cardiac imaging. A companion payload engineering platform, PORE, carries DNA and RNA constructs, gene editing and gene silencing cargo of varied size and format. The company holds an exclusive license to GE HealthCare''s Optison and Sonazoid microbubble products for use with the platform, and has raised approximately $186 million — a $60.75 million Series A and an oversubscribed
  $125 million Series B — from ARCH Venture Partners, Johnson & Johnson, Illumina Ventures and Eli Lilly, to push lead programs in Duchenne muscular dystrophy and autosomal dominant polycystic kidney disease into the clinic, with preclinical work in Alport syndrome and hemophilia A. It was co-founded by Kenneth Greenberg (CEO), Steve Feinstein (Chief Scientific Officer) and Michael H. Davidson (Executive Chairman). SonoThera sells therapeutics, not software: it runs no developer program, publishes no API, SDK or machine-readable specification, and maintains no public source-code organization.'
layout: provider
modified: '2026-08-28'
name: SonoThera
nav: Providers
network: true
overview: 'SonoThera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Gene Therapy, and Genetic Medicine.


  SonoThera''s developer surface includes product news, support, and 8 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sonothera/refs/heads/main/screenshots/sonothera-2026-09-02T160221.png
security:
- kind: domain-security
  name: Sonothera Domain Security
  slug: sonothera-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sonothera
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Gene Therapy
- Genetic Medicine
- Drug Delivery
- Ultrasound
- Life Sciences
- Clinical Trials
- Rare Disease
website: https://sonothera.com/
---
