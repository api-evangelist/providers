---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the Bond Pet Foods website at www.bondpets.com: the route index of the site''s content management system, catalogued as one site surface rather than as separa'
  name: Bond Pet Foods Website (WordPress REST)
  slug: bondpets-com-website-wordpress-rest
artifact_total: 8
asyncapis:
- description: ''
  name: Bond Pet Foods Webhooks
  slug: bond-pet-foods-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-bond-pet-foods-wp-rest-index-original
common:
- group: other
  href: https://artifacts.apis.io/bond-pet-foods/overlays/bond-pet-foods-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bond-pet-foods-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.bondpets.com/
- group: other
  title: ''
  type: Company
  url: https://www.bondpets.com/our-mission/
- group: other
  title: ''
  type: Team
  url: https://www.bondpets.com/our-team/
- group: other
  title: ''
  type: Products
  url: https://www.bondpets.com/shop/
- group: operate
  title: ''
  type: Support
  url: https://www.bondpets.com/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://www.bondpets.com/faqs/
- group: company
  title: ''
  type: Blog
  url: https://www.bondpets.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.bondpets.com/feed/
- group: company
  title: ''
  type: Press
  url: https://www.bondpets.com/press/
- group: company
  title: ''
  type: Careers
  url: https://www.bondpets.com/careers/
- group: company
  title: ''
  type: Newsletter
  url: https://www.bondpets.com/newsletter/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bondpets.com/privacy-policy/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
- group: auth
  href: https://artifacts.apis.io/bond-pet-foods/authentication/bond-pet-foods-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bond-pet-foods-authentication.yml
- group: design
  href: https://artifacts.apis.io/bond-pet-foods/conventions/bond-pet-foods-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bond-pet-foods-conventions.yml
- group: design
  href: https://artifacts.apis.io/bond-pet-foods/errors/bond-pet-foods-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bond-pet-foods-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bond-pet-foods/lifecycle/bond-pet-foods-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bond-pet-foods-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bond-pet-foods/conformance/bond-pet-foods-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bond-pet-foods-conformance.yml
- group: design
  href: https://artifacts.apis.io/bond-pet-foods/data-model/bond-pet-foods-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bond-pet-foods-data-model.yml
- group: auth
  href: https://artifacts.apis.io/bond-pet-foods/security/bond-pet-foods-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bond-pet-foods-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/bond-pet-foods/llms/bond-pet-foods-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bond-pet-foods-llms.txt
- group: agent
  href: https://artifacts.apis.io/bond-pet-foods/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-08'
description: Bond Pet Foods is a Boulder, Colorado food-biotechnology company that makes animal proteins for pet food by precision fermentation rather than by farming animals. Its process pairs a chicken DNA sequence with brewer's yeast and runs it through a roughly 48-hour controlled fermentation, after which the protein is harvested, dried and milled into a powder that pet food makers formulate into finished products. The company operates a 15,000 square-foot food lab in central Boulder, is led by founder and CEO Rich Kelleman, markets itself as an "Ally For All Animals", and has announced a $17.5M Series A, an investment from Symrise AG, and development partnerships with Hill's Pet Nutrition and Wilbur-Ellis Nutrition. Bond Pet Foods runs no developer program and publishes no API documentation, but its own site at www.bondpets.com runs on WordPress and WooCommerce and exposes a genuinely public, machine-readable API surface - a WordPress REST API discovery index advertising 970 routes
  across 57 namespaces, and an anonymously readable WooCommerce Store API covering the merchandise catalog, categories and cart.
image: https://www.bondpets.com/wp-content/uploads/2022/09/Bond_SocialShare_1_Home_Mission.jpg
layout: provider
modified: '2026-08-08'
name: Bond Pet Foods
nav: Providers
network: true
overview: 'Bond Pet Foods publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Website (WordPress REST). Tagged areas include Pet Food, Alternative Protein, Precision Fermentation, Food Technology, and Biotechnology.


  The Bond Pet Foods catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Bond Pet Foods'' developer surface includes support, FAQ, engineering blog, authentication, and 19 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Bond Pet Foods API Rules
  rule_count: 54
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 3
  slug: bond-pet-foods-rules
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 25.6
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 26.0
  provenance:
    conformance: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bond-pet-foods/bond-pet-foods-2026-09-02T144936.png
security:
- kind: authentication
  name: Bond Pet Foods Authentication
  slug: bond-pet-foods-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Bond Pet Foods Domain Security
  slug: bond-pet-foods-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: bond-pet-foods-browse-catalog
  slug: bond-pet-foods-browse-catalog
- name: bond-pet-foods-read-content
  slug: bond-pet-foods-read-content
slug: bond-pet-foods
tags:
- Pet Food
- Alternative Protein
- Precision Fermentation
- Food Technology
- Biotechnology
- Animal Nutrition
- Sustainability
- E-Commerce
- WooCommerce
- WordPress
website: https://www.bondpets.com/
---
