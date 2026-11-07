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
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Ionetix website at ionetix.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Ionetix Website (WordPress REST)
  slug: ionetix-com-website-wordpress-rest
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://ionetix.com/
- group: company
  title: ''
  type: Blog
  url: https://ionetix.com/news-events/
- group: company
  title: ''
  type: BlogRSS
  url: https://ionetix.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://ionetix.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ionetix.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ionetix-corporation
- group: company
  title: ''
  type: Careers
  url: https://ionetix.com/careers/
- group: auth
  href: https://artifacts.apis.io/ionetix/authentication/ionetix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ionetix-authentication.yml
- group: design
  href: https://artifacts.apis.io/ionetix/conventions/ionetix-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ionetix-conventions.yml
- group: design
  href: https://artifacts.apis.io/ionetix/errors/ionetix-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ionetix-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ionetix/lifecycle/ionetix-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ionetix-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ionetix/conformance/ionetix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ionetix-conformance.yml
- group: design
  href: https://artifacts.apis.io/ionetix/data-model/ionetix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ionetix-data-model.yml
- group: build
  href: https://artifacts.apis.io/ionetix/examples/ionetix-examples.yml
  title: ''
  type: Examples
  url: examples/ionetix-examples.yml
- group: build
  href: https://artifacts.apis.io/ionetix/packages/ionetix-packages.yml
  title: ''
  type: Packages
  url: packages/ionetix-packages.yml
- group: agent
  href: https://artifacts.apis.io/ionetix/llms/ionetix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ionetix-llms.txt
- group: agent
  href: https://artifacts.apis.io/ionetix/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/ionetix/plans/ionetix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ionetix-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ionetix/rate-limits/ionetix-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ionetix-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/ionetix/security/ionetix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ionetix-domain-security.yml
created: '2026-08-23'
description: Ionetix (IONETIX Corporation) is a Lansing, Michigan radiopharmaceutical and cyclotron company founded in 2009 out of technology developed at the MIT Plasma Science and Fusion Center. It built the first commercial compact superconducting cyclotron, the ION-12SC, and operates a distributed network of those cyclotrons installed on or near the campuses of hospital PET programs to produce N-13 Ammonia, a short-half-life PET tracer used for cardiac perfusion imaging and the detection of coronary artery disease, sold to providers on a pay-by-the-dose basis. Alongside the cardiac PET network the company runs an alpha isotope manufacturing facility in Lansing built around a 30 MeV cyclotron for commercial-scale production of Actinium-225 and Astatine-211 for targeted alpha therapy, has an approved ANDA for Gallium Ga-68 Gozetotide (PSMA-11), and supply and development partnerships with AlfaRim Medical and Cellectar Biosciences. Ionetix completed a $30M+ financing and go-public transaction
  in April 2026. Ionetix publishes no developer platform, no API documentation, no SDK and no developer portal; the only machine-readable surface on ionetix.com is the WordPress REST API at /wp-json/, whose wp/v2 namespace is anonymously readable and serves the company newsroom, careers postings, conference and case-study archives, product pages, leadership profiles, the media library (including the ION-12SC cyclotron data sheet PDFs) and a site-wide search endpoint as JSON. The WordPress Abilities API namespace (wp-abilities/v1) is registered on the site but returns HTTP 401 to anonymous callers, and no MCP namespace is registered.
image: https://ionetix.com/wp-content/uploads/2021/10/favicon180-1.png
layout: provider
modified: '2026-08-23'
name: Ionetix
nav: Providers
network: true
overview: 'Ionetix is listed with 1 API on the [APIs.io](https://apis.io/) network: Website (WordPress REST). Tagged areas include Company, Healthcare, Life Sciences, Radiopharmaceuticals, and Nuclear Medicine.


  Ionetix''s developer surface includes engineering blog, support, authentication, code examples, and 16 more developer resources.'
plans:
- name: Ionetix Plans Pricing
  plan_count: 0
  slug: ionetix-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Ionetix Rate Limits
  slug: ionetix-rate-limits
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 30.5
    developer_ergonomics: 25.6
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 22.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ionetix/ionetix-2026-09-02T145923.png
security:
- kind: authentication
  name: Ionetix Authentication
  slug: ionetix-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ionetix Domain Security
  slug: ionetix-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: ionetix-harvest-media-and-datasheets
  slug: ionetix-harvest-media-and-datasheets
- name: ionetix-map-product-and-site-network
  slug: ionetix-map-product-and-site-network
- name: ionetix-track-company-news
  slug: ionetix-track-company-news
slug: ionetix
tags:
- Company
- Healthcare
- Life Sciences
- Radiopharmaceuticals
- Nuclear Medicine
- Medical Imaging
- Cardiology
- Oncology
- Isotopes
- Manufacturing
website: https://ionetix.com/
---
