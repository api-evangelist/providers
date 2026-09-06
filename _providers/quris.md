---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quris-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.quris.ai
- group: company
  title: ''
  type: About
  url: https://www.quris.ai/aboutus
- group: company
  title: ''
  type: Blog
  url: https://www.quris.ai/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quris.ai/privacypolicy
- group: operate
  title: ''
  type: Support
  url: https://www.quris.ai/contact
created: '2026-07-17'
description: Quris-AI is a Bio-AI company building what it describes as pharma's first AI safety-prediction platform, aiming to predict which drug candidates will be safe in humans before they reach clinical trials. Its approach couples machine learning with "Patients-on-a-Chip" technology — miniaturized, organ-representative human tissue models that generate automatically-tagged biological data used to train classification algorithms for drug-safety prediction. The company targets the roughly 89% of drugs that fail in clinical trials, seeking to de-risk and accelerate pharmaceutical development. Based in Boston and Tel Aviv, Quris was co-founded with pioneers including Moderna co-founder Robert Langer and Nobel Laureate Aaron Ciechanover. Quris is backed by SoftBank Vision Fund and is profiled in the API Evangelist network as a company lead.
image: https://www.quris.ai/favicon.ico
layout: provider
modified: '2026-07-20'
name: Quris
nav: Providers
network: true
overview: 'Quris is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Tech, Bio-AI, Drug Discovery, and Drug Safety.


  Quris'' developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 18
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quris/refs/heads/main/screenshots/quris-2026-09-02T152721.png
security:
- kind: domain-security
  name: Quris Domain Security
  slug: quris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: quris
tags:
- Company
- Health Tech
- Bio-AI
- Drug Discovery
- Drug Safety
- Clinical Trials
- Pharmaceuticals
- Artificial Intelligence
- Biotechnology
website: https://www.quris.ai
---
