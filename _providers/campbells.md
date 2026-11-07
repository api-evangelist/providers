---
access_model:
  confidence: high
  label: Public and unauthenticated, with no plan, signup or terms behind it
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the Campbell''s website at www.campbells.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate '
  name: Campbell's Website (WordPress REST, www.campbells.com)
  slug: campbells-com-website-wordpress-rest
- description: 'The public WordPress REST API (wp-json) of the Campbell''s website at www.thecampbellscompany.com: the route index of the site''s content management system, catalogued as one site surface rather than as'
  name: Campbell's Website (WordPress REST, www.thecampbellscompany.com)
  slug: thecampbellscompany-com-website-wordpress-rest
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/campbells/finops/campbells-finops.yml
  title: ''
  type: FinOps
  url: finops/campbells-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.campbells.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.thecampbellscompany.com/
- group: company
  title: ''
  type: Investor Relations
  url: https://investor.thecampbellscompany.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.thecampbellscompany.com/newsroom/
- group: company
  title: ''
  type: Careers
  url: https://careers.thecampbellscompany.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-campbells-company
- group: learn
  title: ''
  type: x-Recipes
  url: https://www.campbells.com/recipes/
- group: other
  title: ''
  type: x-Products
  url: https://www.campbells.com/products/
- group: operate
  title: ''
  type: Support
  url: https://www.campbells.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.campbells.com/faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thecampbellscompany.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thecampbellscompany.com/privacy-policy/
- group: agent
  href: https://artifacts.apis.io/campbells/llms/campbells-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/campbells-llms.txt
- group: auth
  href: https://artifacts.apis.io/campbells/authentication/campbells-authentication.yml
  title: ''
  type: Authentication
  url: authentication/campbells-authentication.yml
- group: design
  href: https://artifacts.apis.io/campbells/conventions/campbells-conventions.yml
  title: ''
  type: Conventions
  url: conventions/campbells-conventions.yml
- group: design
  href: https://artifacts.apis.io/campbells/errors/campbells-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/campbells-problem-types.yml
- group: design
  href: https://artifacts.apis.io/campbells/lifecycle/campbells-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/campbells-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/campbells/conformance/campbells-conformance.yml
  title: ''
  type: Conformance
  url: conformance/campbells-conformance.yml
- group: design
  href: https://artifacts.apis.io/campbells/data-model/campbells-data-model.yml
  title: ''
  type: DataModel
  url: data-model/campbells-data-model.yml
- group: operate
  href: https://artifacts.apis.io/campbells/rate-limits/campbells-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/campbells-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/campbells/plans/campbells-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/campbells-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/campbells/packages/campbells-packages.yml
  title: ''
  type: Packages
  url: packages/campbells-packages.yml
- group: agent
  href: https://artifacts.apis.io/campbells/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/campbells/discovery/campbells-discovery.yml
  title: ''
  type: x-Discovery
  url: discovery/campbells-discovery.yml
- group: auth
  href: https://artifacts.apis.io/campbells/security/campbells-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/campbells-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/campbells/skills/campbells-product-catalog.md
  title: ''
  type: AgentSkill
  url: skills/campbells-product-catalog.md
- group: agent
  href: https://artifacts.apis.io/campbells/skills/campbells-recipe-search.md
  title: ''
  type: AgentSkill
  url: skills/campbells-recipe-search.md
created: '2026-03-21'
description: Campbell's (Campbell Soup Company, now The Campbell's Company) is the consumer brand trusted for generations to provide authentic, flavourful, and readily available soups, meals, and recipes. It ran a Campbell's Kitchen Developer API that let developers embed Campbell's, Swanson, Pace, Prego and Pepperidge Farm recipes, products, nutrition and UPC data into their own applications; that programme has been retired and its developer domain no longer resolves. What Campbell's still serves is a live, public, unauthenticated content and recipe-search API on www.campbells.com — 316 recipes, 210 products, 85 recipe collections and 36 FAQs behind the WordPress REST namespaces the site is built on — plus a separately-hosted corporate content API. There is no developer portal, no documentation, no contract and no terms governing any of it.
finops:
- has_sources: true
  method: generated
  name: Campbells Finops
  primary_unit: ''
  service_category: Consumer Packaged Goods / Food
  slug: campbells-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/campbells.png
json_schemas:
- name: csc_faq
  property_count: 17
  slug: campbells-csc-faq
- name: external_product
  property_count: 22
  slug: campbells-external-product
- name: product
  property_count: 23
  slug: campbells-product
- name: recipe
  property_count: 19
  slug: campbells-recipe
layout: provider
modified: '2026-09-05'
name: Campbell's
nav: Providers
network: true
overview: 'Campbell''s is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Food, Consumer Packaged Goods, Recipes, Brands, and Nutrition.


  Campbell''s'' developer surface includes support, authentication, and 26 more developer resources.'
plans:
- name: Campbells Plans Pricing
  plan_count: 0
  slug: campbells-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Campbells Rate Limits
  slug: campbells-rate-limits
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 65.2
    operational_transparency: 0.0
  previous_composite: 20.0
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/campbells/campbells-2026-06-20T173911.png
security:
- kind: authentication
  name: Campbells Authentication
  slug: campbells-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Campbells Domain Security
  slug: campbells-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: campbells-product-catalog
  slug: campbells-product-catalog
- name: campbells-recipe-search
  slug: campbells-recipe-search
slug: campbells
tags:
- Food
- Consumer Packaged Goods
- Recipes
- Brands
- Nutrition
- Product Catalog
- WordPress
- Food and Beverage
website: https://www.campbells.com/
---
