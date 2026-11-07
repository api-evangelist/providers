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
    error_semantics: derived
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
  score: 6.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the LEAF4Life website at leafforlife.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate API'
  name: LEAF4Life Website (WordPress REST)
  slug: leafforlife-com-website-wordpress-rest
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://leafforlife.com/
- group: company
  title: ''
  type: About
  url: https://leafforlife.com/our-science/
- group: other
  title: ''
  type: Leadership
  url: https://leafforlife.com/management-team/
- group: other
  title: ''
  type: AdvisoryBoard
  url: https://leafforlife.com/advisory-board/
- group: operate
  title: ''
  type: Contact
  url: https://leafforlife.com/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leaf4life-inc
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/leaf4life/
- group: auth
  href: https://artifacts.apis.io/leaf4life/authentication/leaf4life-authentication.yml
  title: ''
  type: Authentication
  url: authentication/leaf4life-authentication.yml
- group: design
  href: https://artifacts.apis.io/leaf4life/conventions/leaf4life-conventions.yml
  title: ''
  type: Conventions
  url: conventions/leaf4life-conventions.yml
- group: design
  href: https://artifacts.apis.io/leaf4life/conformance/leaf4life-conformance.yml
  title: ''
  type: Conformance
  url: conformance/leaf4life-conformance.yml
- group: design
  href: https://artifacts.apis.io/leaf4life/errors/leaf4life-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/leaf4life-problem-types.yml
- group: design
  href: https://artifacts.apis.io/leaf4life/lifecycle/leaf4life-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/leaf4life-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/leaf4life/data-model/leaf4life-data-model.yml
  title: ''
  type: DataModel
  url: data-model/leaf4life-data-model.yml
- group: auth
  href: https://artifacts.apis.io/leaf4life/security/leaf4life-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leaf4life-domain-security.yml
- group: operate
  href: https://artifacts.apis.io/leaf4life/rate-limits/leaf4life-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/leaf4life-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/leaf4life/plans/leaf4life-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/leaf4life-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/leaf4life/llms/leaf4life-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leaf4life-llms.txt
- group: agent
  href: https://artifacts.apis.io/leaf4life/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-25'
description: LEAF4Life Inc. is a privately held, clinical-stage biopharmaceutical company headquartered in Woburn, Massachusetts, founded in 2018 by Dr. Clet Niyikiza to develop transformative therapies for hypoxia — insufficient oxygen at the tissue and cellular level — which the company describes as implicated in the world's ten leading causes of death and more than 30 million deaths a year. Its lead asset, KizaVie™ (LEAF-4L6715), is a proprietary liposomal formulation of transcrocetin, a naturally occurring carotenoid from saffron and cape jasmine, designed to enhance oxygen diffusion in plasma and interstitium, restore microcirculatory oxygen delivery and repair hypoxia-driven microvascular and tissue damage, thereby improving the effectiveness of standard-of-care treatment. KizaVie™ is in three Phase 3 registrational studies in Europe — acute respiratory distress syndrome (ARDS), glioblastoma and sarcoma — and has received Compassionate Use Authorization in France for ARDS. The company
  also describes application to shock and trauma, cardiovascular disease, neurodegenerative disorders and aging. LEAF4Life runs no developer program and publishes no product API, developer portal, API reference, SDK or OpenAPI definition. The only machine-readable surface reachable without credentials is the WordPress REST content API behind leafforlife.com, catalogued here, and even that returns page identity and media only — every page body is empty over the API because the site is assembled by a page builder.
image: https://leafforlife.com/wp-content/uploads/2025/11/LEAF4Life_logo_cropped_final.png
layout: provider
modified: '2026-08-25'
name: LEAF4Life
nav: Providers
network: true
overview: 'LEAF4Life is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Clinical Trials, and Oncology.


  LEAF4Life''s developer surface includes authentication and 17 more developer resources.'
plans:
- name: Leaf4Life Plans Pricing
  plan_count: 0
  slug: leaf4life-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Leaf4Life Rate Limits
  slug: leaf4life-rate-limits
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 18.5
    discoverability: 58.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 11.2
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/leaf4life/leaf4life-2026-09-02T150230.png
security:
- kind: authentication
  name: Leaf4Life Authentication
  slug: leaf4life-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Leaf4Life Domain Security
  slug: leaf4life-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Describe the LEAF4Life API deployment before calling it
  slug: leaf4life-describe-the-deployment
- name: Harvest the LEAF4Life media library
  slug: leaf4life-harvest-media-library
- name: Index the LEAF4Life public site
  slug: leaf4life-index-the-public-site
slug: leaf4life
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Clinical Trials
- Oncology
- Critical Care
- Drug Development
- Life Sciences
- Rare Disease
- content-api
website: https://leafforlife.com/
---
