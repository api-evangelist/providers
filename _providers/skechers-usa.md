---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: Skechers operates a direct-to-consumer digital commerce platform at skechers.com that enables online shopping for footwear, apparel, and accessories. The platform integrates with e-commerce infrastruc
  name: Skechers E-Commerce API
  slug: ecommerce-api
- description: The Skechers Plus loyalty program enables customers to earn and redeem points across all purchase channels (online, in-store, and mobile). The loyalty system integrates with the e-commerce platform, i
  name: Skechers Plus Loyalty API
  slug: loyalty-api
- description: Skechers operates over 4,700 retail stores globally across company-owned, franchise, and licensed formats. The store locator functionality provides geographic search for nearby Skechers retail locatio
  name: Skechers Store Locator API
  slug: store-locator-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/skechers-usa/plans/skechers-usa-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/skechers-usa-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/skechers-usa/rate-limits/skechers-usa-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/skechers-usa-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/skechers-usa/finops/skechers-usa-finops.yml
  title: ''
  type: FinOps
  url: finops/skechers-usa-finops.yml
- group: auth
  href: https://artifacts.apis.io/skechers-usa/security/skechers-usa-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/skechers-usa-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/skechers-usa/security/skechers-usa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skechers-usa-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skechers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/skechers
- group: company
  title: ''
  type: Website
  url: https://www.skechers.com
- group: start
  title: ''
  type: Portal
  url: https://www.skechers.com/partners
- group: design
  href: https://artifacts.apis.io/skechers-usa/json-ld/skechers-usa-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/skechers-usa-context.jsonld
- group: design
  href: https://artifacts.apis.io/skechers-usa/vocabulary/skechers-usa-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/skechers-usa-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://about.skechers.com/feed
created: '2026-03-21'
description: Skechers U.S.A. is an American lifestyle and performance footwear company (Fortune 500) that designs, develops, and markets a diverse range of footwear for men, women, and children across 170+ countries. Skechers operates direct-to-consumer digital commerce through its website and mobile app, wholesale partnerships with retailers, and a global network of owned and franchised retail stores. Their digital commerce infrastructure relies on e-commerce APIs for product catalog management, inventory, order management, customer accounts, and loyalty programs.
finops:
- has_sources: false
  method: generated
  name: Skechers Usa Finops
  primary_unit: request
  service_category: API
  slug: skechers-usa-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skechers-usa.png
json_schemas:
- name: Skechers Product
  property_count: 17
  slug: skechers-usa-product
json_structures:
- name: Skechers Usa Structure
  property_count: 0
  slug: skechers-usa-structure
jsonld:
- class_count: 41
  name: Skechers Usa Context
  property_count: 1
  slug: skechers-usa-context
layout: provider
modified: '2026-05-02'
name: Skechers U.S.A.
nav: Providers
network: true
overview: 'Skechers U.S.A. is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Footwear, Retail, E-Commerce, Fortune 500, and Direct to Consumer.


  The Skechers U.S.A. catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Skechers U.S.A.''s developer surface includes developer portal, engineering blog, and 10 more developer resources.'
plans:
- name: Skechers Usa Plans Pricing
  plan_count: 3
  slug: skechers-usa-plans-pricing
press:
- date: ''
  title: SKECHERS | Business Wire - Via Ritzau
  url: https://via.ritzau.dk/pressemeddelelse/13951664/skechers?publisherId=90456
- date: ''
  title: o9 Solutions Partners With Skechers to Digitally Transform ...
  url: https://www.businesswire.com/news/home/20240122515552/en/o9-Solutions-Partners-With-Skechers-to-Digitally-Transform-the-Companys-Retail-Planning-Processes
- date: ''
  title: 오나인솔루션즈, 글로벌 스포츠 브랜드 스케쳐스(Skechers) ...
  url: https://o9solutions.com/ko/news/customer-case-skechers-o9-digital-brain
- date: ''
  title: The problem with generative AI, and how it relates to Skechers ...
  url: https://www.instagram.com/reel/DU_LgGaFSxG/
- date: ''
  title: 'When IR Met AI: How the Technology Is Shaping Earnings- ...'
  url: https://www.wsj.com/articles/when-ir-met-ai-how-the-technology-is-shaping-earnings-day-prep-5054a057
random_paper: 6
rate_limits:
- limit_count: 5
  name: Skechers Usa Rate Limits
  slug: skechers-usa-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Skechers U.S.A. — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: skechers-usa-jsonschema-spectral-rules
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 23.5
    contract_quality: 10.7
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 18.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/skechers-usa/skechers-usa-2026-06-20T194019.png
security:
- kind: domain-security
  name: Skechers Usa Domain Security
  slug: skechers-usa-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Skechers Usa Vulnerability Disclosure
  slug: skechers-usa-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: skechers-usa
tags:
- Footwear
- Retail
- E-Commerce
- Fortune 500
- Direct to Consumer
- Lifestyle
website: https://www.skechers.com
---
