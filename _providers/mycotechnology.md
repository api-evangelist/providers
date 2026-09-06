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
  url: security/mycotechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mycoiq.com/
- group: company
  title: ''
  type: About
  url: https://www.mycoiq.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.mycoiq.com/newsroom/
- group: operate
  title: ''
  type: Support
  url: https://www.mycoiq.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mycoiq.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mycoiq.com/privacy-policy/
- group: other
  title: ''
  type: Products
  url: https://www.mycoiq.com/ingredients/
- group: other
  title: ''
  type: Resources
  url: https://www.mycoiq.com/resources/
- group: company
  title: ''
  type: Careers
  url: https://www.mycoiq.com/careers/
- group: other
  title: ''
  type: Patents
  url: https://www.mycoiq.com/patents/
- group: other
  title: ''
  type: Profile
  url: https://forgeglobal.com/mycotechnology_stock/
coverage:
  checked: '2026-08-04'
  detail: MycoTechnology sells mushroom-mycelium fermented food ingredients (ClearIQ, ClearHT, Zukora honey truffle sweet protein) to food manufacturers; its only web property is the WordPress marketing site at www.mycoiq.com, which has no developer section, and api./developer./docs./app.mycoiq.com resolve to no DNS records at all.
  evidence:
  - status: 404
    url: https://www.mycoiq.com/openapi.json
  - status: 404
    url: https://www.mycoiq.com/llms.txt
  - status: 404
    url: https://www.mycoiq.com/.well-known/agent-card.json
  - status: 404
    url: https://www.mycoiq.com/developers
  - status: 403
    url: https://forgeglobal.com/mycotechnology_stock/
  reason: not-a-software-company
  state: none
created: '2026-08-04'
description: 'MycoTechnology, Inc. is a Colorado-based food ingredient technology company that uses mushroom mycelial fermentation to create naturally derived ingredients for the food and beverage industry. Operating publicly as Myco (mycoiq.com), the company develops and manufactures flavor-modulation and sweetening ingredients — ClearIQ natural flavor, ClearHT natural flavor, and Zukora honey truffle sweet protein — used for bitterness masking, off-note mitigation, sugar reduction, and clean-label formulation in plant proteins, meat analogues, dairy alternatives, and health and wellness products. It also offers Fermentation as a Service (FaaS) and a MyCulinary culinary science program for food brands. This is an ingredient manufacturing and food science business, not a software or API company: it publishes no developer portal, no API documentation, and no machine-readable API contract.'
image: https://www.mycoiq.com/wp-content/uploads/2023/06/Mycotech-logo-header_203x71.svg
layout: provider
modified: '2026-08-04'
name: MycoTechnology
nav: Providers
network: true
overview: 'MycoTechnology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Ingredients, Fermentation, and Biotechnology.


  MycoTechnology''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
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
  previous_composite: 10.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mycotechnology/refs/heads/main/screenshots/mycotechnology-2026-08-07T184513.png
security:
- kind: domain-security
  name: Mycotechnology Domain Security
  slug: mycotechnology-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mycotechnology
tags:
- Company
- Food
- Ingredients
- Fermentation
- Biotechnology
- Food Science
- Manufacturing
- Agriculture
website: https://www.mycoiq.com/
---
