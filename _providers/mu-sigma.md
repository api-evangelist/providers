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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.mu-sigma.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mu-sigma.com/blogs/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.mu-sigma.com/blogs/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.mu-sigma.com/client-queries/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mu-sigma.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Mu-Sigma
- group: build
  title: ''
  type: Packages
  url: packages/mu-sigma-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mu-sigma-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mu-sigma-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mu-sigma-plans-pricing.yml
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/mu-sigma_stock/
coverage:
  checked: '2026-08-26'
  detail: Mu Sigma sells decision-science engagements and delivered platforms (muAoPS, Akashic Architecture, muTalos) with no developer program behind them — its 41-page WordPress site has no developer, docs, API or pricing page at all, and every contract-discovery path probed on www.mu-sigma.com and labs.mu-sigma.com missed, leaving the github.com/Mu-Sigma R packages as the only machine-readable thing it publishes.
  evidence:
  - status: 200
    url: https://www.mu-sigma.com/openapi.json
  - status: 200
    url: https://www.mu-sigma.com/developers
  - status: 404
    url: https://labs.mu-sigma.com/openapi.json
  - status: 200
    url: https://www.mu-sigma.com/page-sitemap.xml
  - status: 200
    url: https://www.mu-sigma.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Mu Sigma is a decision sciences and AI services company founded in 2004, headquartered in Northbrook, Illinois with its principal delivery centre in Bangalore, India, working with 140+ Fortune 500 clients across retail, pharma, financial services, manufacturing, energy, technology and logistics. Its work is delivered as engagements and platforms rather than as a public developer product: the Art of Problem Solving System (muAoPS), the Akashic Architecture enterprise intelligence foundation, the muTalos agentic-AI ecosystem, Enablers of Confidence, and a Continuous Service-as-a-Software operating model. Mu Sigma publishes no developer portal, no API reference and no machine-readable API contract; its only public machine-readable engineering output is a set of open-source R packages for decision science (HVT, muHVT, analysisPipelines, RImpala, Rdrools) released to CRAN from the github.com/Mu-Sigma organization.'
image: https://www.mu-sigma.com/wp-content/uploads/2025/10/mu-small-logo.png
layout: provider
modified: '2026-08-26'
name: Mu Sigma
nav: Providers
network: true
overview: 'Mu Sigma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Data Science, Decision Sciences, and Artificial Intelligence.


  Mu Sigma''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Mu Sigma Plans Pricing
  plan_count: 0
  slug: mu-sigma-plans-pricing
random_paper: 2
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 7
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 6.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mu-sigma/refs/heads/main/screenshots/mu-sigma-2026-09-02T150647.png
security:
- kind: domain-security
  name: Mu Sigma Domain Security
  slug: mu-sigma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mu-sigma
tags:
- Company
- Analytics
- Data Science
- Decision Sciences
- Artificial Intelligence
- Machine-Learning
- Consulting
- Business Intelligence
- Data Engineering
- Professional Services
website: https://www.mu-sigma.com/
---
