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
    agentic_access: derived
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
  score: 10.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cutiss Agentic Access
  operation_count: 15
  slug: cutiss-agentic-access
  summary_line: 15 operations
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the CUTISS website at cutiss.swiss: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: CUTISS Website (WordPress REST)
  slug: cutiss-swiss-website-wordpress-rest
artifact_total: 9
common:
- group: other
  href: https://artifacts.apis.io/cutiss/capabilities/cutiss-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cutiss-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://cutiss.swiss/
- group: company
  title: ''
  type: About
  url: https://cutiss.swiss/about-us/
- group: other
  title: ''
  type: Technology
  url: https://cutiss.swiss/technology/
- group: other
  title: ''
  type: Pipeline
  url: https://cutiss.swiss/clinical-problem-scars/
- group: company
  title: ''
  type: Blog
  url: https://cutiss.swiss/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://cutiss.swiss/feed/
- group: company
  title: ''
  type: News
  url: https://cutiss.swiss/newsroom/
- group: company
  title: ''
  type: Press
  url: https://cutiss.swiss/media/
- group: company
  title: ''
  type: Investors
  url: https://cutiss.swiss/investors/
- group: company
  title: ''
  type: Careers
  url: https://cutiss.swiss/career/
- group: operate
  title: ''
  type: Support
  url: https://cutiss.swiss/contact/
- group: other
  title: ''
  type: Awards
  url: https://cutiss.swiss/awards/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cutiss.swiss/data-protection/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cutiss.swiss/impressum-en/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cutiss-ag/
- group: auth
  href: https://artifacts.apis.io/cutiss/authentication/cutiss-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cutiss-authentication.yml
- group: design
  href: https://artifacts.apis.io/cutiss/conventions/cutiss-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cutiss-conventions.yml
- group: design
  href: https://artifacts.apis.io/cutiss/conformance/cutiss-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cutiss-conformance.yml
- group: design
  href: https://artifacts.apis.io/cutiss/lifecycle/cutiss-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cutiss-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/cutiss/security/cutiss-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cutiss-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/cutiss/agentic-access/cutiss-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cutiss-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/cutiss/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/cutiss/llms/cutiss-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cutiss-llms.txt
- group: build
  href: https://artifacts.apis.io/cutiss/packages/cutiss-packages.yml
  title: ''
  type: Packages
  url: packages/cutiss-packages.yml
- group: commercial
  href: https://artifacts.apis.io/cutiss/plans/cutiss-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cutiss-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cutiss/rate-limits/cutiss-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cutiss-rate-limits.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
- group: design
  href: https://artifacts.apis.io/cutiss/data-model/cutiss-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cutiss-data-model.yml
- group: design
  href: https://artifacts.apis.io/cutiss/errors/cutiss-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cutiss-problem-types.yml
created: '2026-08-11'
description: 'CUTISS AG is a Swiss late-stage clinical TechBio company headquartered at the Bio-Technopark in Schlieren, Zurich, founded in 2017 as a spin-off of the Tissue Biology Research Unit (TBRU) at the University of Zurich and the University Children''s Hospital Zurich, and accelerated through Wyss Zurich. Its lead product, denovoSkin, is a first-in-class bioengineered, personalized dermo-epidermal skin graft grown from a small biopsy of a patient''s own skin to treat large and deep skin defects in children and adults; it holds Orphan Drug Designation for burns from Swissmedic, the EMA and the FDA and is in late-stage clinical development. With CSEM the company built denovoCast, described as the world''s first machine for automated production of personalized human skin tissue, funded in part by Innosuisse and EU Horizon 2020. CUTISS has raised roughly CHF 50 million and employs around 50 people. It is a therapeutics manufacturer, not a software vendor: it publishes no product API,
  no developer portal, no SDKs and no pricing. The only machine-readable API on its public host is the WordPress REST API behind cutiss.swiss, which serves the newsroom, blog, corporate pages, team directory, teams taxonomy and media library as JSON, read-only without credentials.'
image: https://cutiss.swiss/wp-content/uploads/2019/08/Cutiss-Logo.png
layout: provider
modified: '2026-08-11'
name: CUTISS
nav: Providers
network: true
overview: 'CUTISS publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Regenerative Medicine, Tissue Engineering, and Life Sciences.


  CUTISS''s developer surface includes engineering blog, product news, support, authentication, and 26 more developer resources.'
plans:
- name: Cutiss Plans Pricing
  plan_count: 0
  slug: cutiss-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Cutiss Rate Limits
  slug: cutiss-rate-limits
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 58.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 17.8
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/cutiss/cutiss-2026-09-02T145209.png
security:
- kind: authentication
  name: Cutiss Authentication
  slug: cutiss-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cutiss Domain Security
  slug: cutiss-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: cutiss-harvest-press-assets
  slug: cutiss-harvest-press-assets
- name: cutiss-map-organization
  slug: cutiss-map-organization
- name: cutiss-monitor-newsroom
  slug: cutiss-monitor-newsroom
slug: cutiss
tags:
- Company
- Biotechnology
- Regenerative Medicine
- Tissue Engineering
- Life Sciences
- Medical Devices
- Clinical Trials
- Dermatology
- Healthcare
- Switzerland
- Research
website: https://cutiss.swiss/
---
