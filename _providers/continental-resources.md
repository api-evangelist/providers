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
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/continental-resources-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/continental-resources-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clr.com/
- group: company
  title: ''
  type: AboutUs
  url: https://www.clr.com/about-continental/
- group: other
  title: ''
  type: Operations
  url: https://www.clr.com/operations/
- group: other
  title: ''
  type: International
  url: https://www.clr.com/international/
- group: other
  title: ''
  type: Sustainability
  url: https://www.clr.com/hse/
- group: operate
  title: ''
  type: Community
  url: https://www.clr.com/community/
- group: company
  title: ''
  type: Newsroom
  url: https://www.prnewswire.com/news/continental-resources/
- group: company
  title: ''
  type: Careers
  url: https://www.clr.com/careers/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.clr.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clr.com/legal/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/continental-resources-2/
coverage:
  checked: '2026-09-05'
  detail: 'Continental Resources is an oil and natural gas producer that ships no software product, and its own 56-page sitemap contains no developer, API, docs or reference page — the only machine-readable endpoint anywhere on clr.com is the WordPress wp-json root, which the company has deliberately switched off with a 401 "DRA: Only authenticated users can access the REST API."'
  evidence:
  - status: 401
    url: https://www.clr.com/wp-json
  - status: 200
    url: https://www.clr.com/sitemap_index.xml
  - status: 404
    url: https://www.clr.com/.well-known/api-catalog
  - status: 0
    url: https://www.continental-resources.com/
  reason: not-a-software-company
  state: none
created: '2026-03-23'
description: Continental Resources, Inc. is a privately held independent oil and natural gas exploration and production company headquartered in Oklahoma City, Oklahoma, and present on the web at clr.com. Its U.S. asset base spans the Bakken of North Dakota, South Dakota and Montana, the Anadarko Basin of Oklahoma, the Powder River Basin of Wyoming and the Permian Basin of Texas, with international positions in Argentina's Vaca Muerta shale and a joint venture in the Diyarbakir Basin of Turkey. The company was taken private in November 2022 in a $4.3B transaction with the Hamm family and is no longer publicly traded. Continental Resources publishes no developer program, API documentation, or machine-readable contract of any kind; this profile catalogs its corporate, owner-relations, operational and sustainability web properties and records that its royalty-owner, vendor-invoicing and employee-access surfaces are each operated by a third-party software vendor rather than by Continental itself.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/continental-resources.png
layout: provider
modified: '2026-09-05'
name: Continental Resources
nav: Providers
network: true
overview: Continental Resources is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Oil and Gas, Exploration, Production, and Upstream.
press:
- date: '2026-05-25'
  title: 'Corporate Analysis: Continental Resources | Q4 2025'
  url: https://novilabs.com/blog/corporate-analysis-continental-resources-q4-2025/
- date: '2026-05-25'
  title: Continental Resources Expands Vaca Muerta Position ...
  url: https://www.prnewswire.com/news-releases/continental-resources-expands-vaca-muerta-position-through-agreement-with-pan-american-energy-302652298.html
- date: '2026-05-25'
  title: Annual Report for Fiscal Year Ending December 31, 2024 ...
  url: https://www.publicnow.com/view/8A71D46A2596FC26A5DEB8FE565DF773D769D3A7
- date: '2026-05-25'
  title: From the @america250 x Forbes America Innovates stage, ...
  url: https://www.facebook.com/forbes/posts/from-the-america250-x-forbes-america-innovates-stage-harold-hamm-founder-and-cha/1358751936114793/
- date: '2026-05-25'
  title: Continental Resources Acquires Vaca Muerta Interests ...
  url: https://www.linkedin.com/posts/continental-resources-2_continental-resources-expands-vaca-muerta-activity-7414019500192268288-3o30
random_paper: 10
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.6
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Continental Resources Domain Security
  slug: continental-resources-domain-security
  summary_line: TLSv1.3 · DMARC
slug: continental-resources
tags:
- Energy
- Oil and Gas
- Exploration
- Production
- Upstream
- Natural Gas
- Petroleum
- Mineral Rights
website: https://www.clr.com/
---
