---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
- description: 'The public WordPress REST API (wp-json) of the Habiteo website at www.habiteo.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Habiteo Website (WordPress REST)
  slug: habiteo-com-website-wordpress-rest
- description: A second, older JSON surface on www.habiteo.com, served by the WordPress "JSON API" plugin at /api/. GET https://www.habiteo.com/api/ returns {"status":"ok","json_api_version":"1.1.1","controllers":["
  name: Habiteo Site JSON API (WordPress JSON API plugin)
  slug: json-api-plugin
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/habiteo/plans/habiteo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/habiteo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/habiteo/rate-limits/habiteo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/habiteo-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://www.habiteo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.habiteo.com/fr/actualite-habiteo/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.habiteo.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.habiteo.com/fr/contact/
- group: start
  title: ''
  type: Login
  url: https://my.habiteo.com/connexion
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.habiteo.com/fr/conditions-generales-de-vente/
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.habiteo.com/fr/mentions-legales/
- group: company
  title: ''
  type: Press
  url: https://www.habiteo.com/fr/presse/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/habiteo-com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/HabiteoFR
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCXb9wxCl6kie-XcfLfvMGig
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/habiteofr/
- group: auth
  href: https://artifacts.apis.io/habiteo/authentication/habiteo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/habiteo-authentication.yml
- group: design
  href: https://artifacts.apis.io/habiteo/conventions/habiteo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/habiteo-conventions.yml
- group: design
  href: https://artifacts.apis.io/habiteo/errors/habiteo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/habiteo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/habiteo/data-model/habiteo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/habiteo-data-model.yml
- group: design
  href: https://artifacts.apis.io/habiteo/conformance/habiteo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/habiteo-conformance.yml
- group: design
  href: https://artifacts.apis.io/habiteo/lifecycle/habiteo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/habiteo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/habiteo/components/habiteo-components.yml
  title: ''
  type: Components
  url: components/habiteo-components.yml
- group: agent
  href: https://artifacts.apis.io/habiteo/llms/habiteo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/habiteo-llms.txt
- group: auth
  href: https://artifacts.apis.io/habiteo/security/habiteo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/habiteo-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/habiteo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-17'
description: 'Habiteo is a French PropTech company founded in 2014 in Paris that builds full-web 3D sales and marketing technology for new-build real estate. Its products let developers, house builders, commercial-property operators and their agencies model a programme in 3D before it is built: 3D floor plans and perspectives, virtual tours, drone-based site insertions and neighbourhood views (Modelisation and myHabiteo Studio), an interior configurator that lets a buyer choose materials and options in place of a physical showroom (Configurateur), a mobile on-site sales unit (Habiteo Truck), and the MegaWidget, a hosted mini-site that gathers every 3D asset for a programme behind a single link. myHabiteo is the operator platform that binds the 3D layer to commercialisation with a CRM, a reservation module, programme management and sales and marketing dashboards. More than 350 developers, including Nexity, Kaufman & Broad and Immobiliere 3F, have used the technology. Habiteo was acquired
  by the French listings portal Bien''ici in May 2022 and continues to operate under its own brand. Habiteo publishes no public developer programme, no API documentation and no machine-readable API contract for any of these products; the only anonymously readable machine surface on its domain is the WordPress REST API behind its marketing site.'
image: https://www.habiteo.com/wp-content/uploads/2017/02/Logo_Habiteo_Hz_Bg-transparent-1.png
layout: provider
modified: '2026-08-17'
name: Habiteo
nav: Providers
network: true
overview: 'Habiteo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, PropTech, 3D Visualization, and Property Marketing.


  Habiteo''s developer surface includes engineering blog, support, YouTube channel, authentication, and 20 more developer resources.'
plans:
- name: Habiteo Plans Pricing
  plan_count: 0
  slug: habiteo-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Habiteo Rate Limits
  slug: habiteo-rate-limits
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 1.7
    developer_ergonomics: 25.6
    discoverability: 58.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 17.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/habiteo/habiteo-2026-09-02T145647.png
security:
- kind: authentication
  name: Habiteo Authentication
  slug: habiteo-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Habiteo Domain Security
  slug: habiteo-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: habiteo-map-content-surface
  slug: habiteo-map-content-surface
- name: habiteo-read-newsroom
  slug: habiteo-read-newsroom
slug: habiteo
tags:
- Company
- Real Estate
- PropTech
- 3D Visualization
- Property Marketing
- Configurator
- CRM
- France
- Content
- WordPress
website: https://www.habiteo.com/
---
