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
  url: security/hellofresh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.hellofresh.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hellofresh
- group: company
  title: ''
  type: Blog
  url: https://www.hellofresh.com/blog
- group: company
  title: ''
  type: Careers
  url: https://careers.hellofresh.com/
- group: company
  title: ''
  type: CorporateWebsite
  url: https://www.hellofreshgroup.com/
created: '2026-07-17'
description: 'HelloFresh SE is a publicly listed (Frankfurt Stock Exchange: HFG), Berlin-headquartered global meal-kit and food-solutions company that ships recipes and pre-portioned ingredients to households across North America, Europe, and Asia-Pacific. Its brand portfolio includes HelloFresh, Factor, Green Chef, EveryPlate, Chefs Plate, Youfoodz, and Good Chop. HelloFresh does not publish a public consumer developer API; its engineering organization is active in open source on GitHub, maintaining widely used infrastructure tooling such as the Janus API gateway, the health-go healthcheck library, and the goengine event-sourcing framework. This profile was surfaced as a portfolio company of HV Capital and Insight Partners and enriched by the API Evangelist pipeline.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hellofresh.png
layout: provider
modified: '2026-07-19'
name: HelloFresh
nav: Providers
network: true
overview: 'HelloFresh is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Food and Beverage, Meal Kit, and E-Commerce.


  HelloFresh''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 5.8
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 5.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hellofresh/refs/heads/main/screenshots/hellofresh-2026-07-25T220936.png
security:
- kind: domain-security
  name: Hellofresh Domain Security
  slug: hellofresh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hellofresh
tags:
- Company
- Consumer
- Food and Beverage
- Meal Kit
- E-Commerce
- Subscription
- Open-Source
- Retail
website: http://www.hellofresh.com/
---
