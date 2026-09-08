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
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accutar-biotechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.accutarbio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.accutarbio.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.accutarbio.com/feed/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.accutarbio.com/news/
- group: operate
  title: ''
  type: Contact
  url: https://www.accutarbio.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://www.accutarbio.com/careers/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accutar-biotechnology-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/accutar-biotechnology-plans-pricing.yml
coverage:
  checked: '2026-09-06'
  detail: Accutar's AI products are offered only as end-user tools reached by emailing bd@accutarbio.com or demoinsightone@accutarbio.com for a demo — there is no developer section on accutarbio.com, api./docs./developer./app.accutarbio.com all fail to resolve in DNS, and the only machine-readable surface on the site is the stock WordPress /wp-json/ CMS endpoint, which is not an Accutar product.
  evidence:
  - status: 200
    url: https://www.accutarbio.com/products/
  - status: 200
    url: https://www.accutarbio.com/genusone/
  - status: 404
    url: https://www.accutarbio.com/openapi.json
  - status: 404
    url: https://www.accutarbio.com/llms.txt
  - status: 404
    url: https://www.accutarbio.com/.well-known/agent-card.json
  - status: 404
    url: https://www.accutarbio.com/.well-known/ae-control-probe
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: 'Accutar Biotechnology Inc. is a clinical-stage biotechnology company headquartered in Cranbury, New Jersey, founded in 2015 and previously based in Brooklyn, New York, with operations in Shanghai. It applies deep learning to small-molecule drug discovery and runs its own oncology pipeline, including the AC0682 and AC0176 protein degraders in Phase 1 trials. Its computational platform is a set of in-house AI products used in its own preclinical workflow and offered to partners: ChemiRise (retrosynthesis), Orbital (neural-network docking), Virtual Screen, Intelligent-SAR, Chemi-Net (ADME prediction) and the PatentOne AI suite (InsightOne, GenusOne). Accutar publishes no developer program: no public API, developer portal, reference documentation, machine-readable specification or SDK exists on any host it operates. Access to the AI products is arranged by email enquiry for a trial or demo.'
image: https://www.accutarbio.com/wp-content/themes/accutar/images/logo.svg
layout: provider
modified: '2026-09-06'
name: Accutar Biotechnology
nav: Providers
network: true
overview: 'Accutar Biotechnology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and Artificial Intelligence.


  Accutar Biotechnology''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Accutar Biotechnology Plans Pricing
  plan_count: 0
  slug: accutar-biotechnology-plans-pricing
random_paper: 19
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 4
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 3.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Accutar Biotechnology Domain Security
  slug: accutar-biotechnology-domain-security
  summary_line: TLSv1.3 · DMARC
slug: accutar-biotechnology
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- Artificial Intelligence
- Machine Learning
- Cheminformatics
- Oncology
- Life Sciences
- Health
website: https://www.accutarbio.com/
---
