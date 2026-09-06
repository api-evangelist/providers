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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soley-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://soleytherapeutics.com/
- group: company
  title: ''
  type: About
  url: https://soleytherapeutics.com/about/
- group: other
  title: ''
  type: Pipeline
  url: https://soleytherapeutics.com/pipeline/
- group: operate
  title: ''
  type: Contact
  url: https://soleytherapeutics.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Soley-Therapeutics
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/soley-therapeutics-stock
coverage:
  checked: '2026-08-05'
  detail: 'Soley sells therapeutics, not software - its cell stress sensing platform is an internal discovery engine - and no API host exists to document: wildcard DNS makes api/docs/developer subdomains resolve to the same WordPress marketing host whose TLS certificate covers only the apex and www, the GitHub org holds only two forks of third-party ML infrastructure (NVIDIA dcgm-exporter), and no npm or PyPI package exists. Note the 202s below are a SiteGround "sg-captcha: challenge" interstitial that answers every path including a nonsense control, so the marketing site itself was never readable by our probe - the no-API finding rests on the DNS, TLS, GitHub and registry evidence, not on that host.'
  evidence:
  - status: 200
    url: https://github.com/Soley-Therapeutics
  - status: 200
    url: https://api.github.com/orgs/soley-therapeutics/repos
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=soley%20therapeutics
  - status: 404
    url: https://pypi.org/pypi/soley-therapeutics/json
  - status: 202
    url: https://soleytherapeutics.com/.well-known/agent-card.json
  - status: 202
    url: https://soleytherapeutics.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'Soley Therapeutics is a science-first, tech-enabled drug discovery and development company headquartered in South San Francisco, California, using human cells as biological sensors to uncover first-in-class medicines. Its cell stress sensing platform captures time-resolved cellular responses across thousands of features and applies computer vision and machine learning to compress them into compact signatures, screening hundreds of thousands of compounds per week on proprietary automation and robotics. The company is advancing a lead oncology asset for acute myeloid leukemia toward an IND filing, a second oncology asset for solid tumors in IND-enabling studies, and non-oncology stress-reducing candidates for neurodegenerative and metabolic disease. Soley raised a $200M Series C in January 2026, bringing total funding to roughly $290M. The platform is an internal discovery engine: Soley is a therapeutics developer, not a software vendor, and publishes no public API, developer
  portal, or machine-readable specification.'
layout: provider
modified: '2026-08-05'
name: Soley Therapeutics
nav: Providers
network: true
overview: Soley Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Drug Discovery, and Oncology.
random_paper: 8
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soley-therapeutics/refs/heads/main/screenshots/soley-therapeutics-2026-09-02T160128.png
security:
- kind: domain-security
  name: Soley Therapeutics Domain Security
  slug: soley-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: soley-therapeutics
tags:
- Company
- Biotechnology
- Therapeutics
- Drug Discovery
- Oncology
- Artificial Intelligence
- Machine-Learning
- Life Sciences
- Healthcare
website: https://soleytherapeutics.com/
---
