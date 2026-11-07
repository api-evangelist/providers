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
- description: 'The public WordPress REST API (wp-json) of the Elixir Medical website at elixirmedical.com: the route index of the site''s content management system, catalogued as one site surface rather than as separ'
  name: Elixir Medical Website (WordPress REST)
  slug: elixirmedical-com-website-wordpress-rest
artifact_total: 8
collections:
- collection_type: open
  name: Elixir Medical Website Content API (WordPress REST wp/v2)
  slug: open-elixir-medical-wordpress-content
common:
- group: other
  href: https://artifacts.apis.io/elixir-medical/overlays/elixir-medical-wordpress-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elixir-medical-wordpress-content-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/elixir-medical/security/elixir-medical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elixir-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://elixirmedical.com/
- group: company
  title: ''
  type: About
  url: https://elixirmedical.com/us/about-us/
- group: operate
  title: ''
  type: Support
  url: https://elixirmedical.com/us/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://elixirmedical.com/ous/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://elixirmedical.com/us/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://elixirmedical.com/us/terms-of-use/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/elixir-medical_stock/
- group: agent
  href: https://artifacts.apis.io/elixir-medical/llms/elixir-medical-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elixir-medical-llms.txt
- group: design
  href: https://artifacts.apis.io/elixir-medical/lifecycle/elixir-medical-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/elixir-medical-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/elixir-medical/conformance/elixir-medical-conformance.yml
  title: ''
  type: Conformance
  url: conformance/elixir-medical-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/elixir-medical/plans/elixir-medical-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/elixir-medical-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/elixir-medical/rate-limits/elixir-medical-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/elixir-medical-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/elixir-medical/authentication/elixir-medical-authentication.yml
  title: ''
  type: Authentication
  url: authentication/elixir-medical-authentication.yml
- group: design
  href: https://artifacts.apis.io/elixir-medical/errors/elixir-medical-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/elixir-medical-problem-types.yml
- group: design
  href: https://artifacts.apis.io/elixir-medical/conventions/elixir-medical-conventions.yml
  title: ''
  type: Conventions
  url: conventions/elixir-medical-conventions.yml
- group: design
  href: https://artifacts.apis.io/elixir-medical/data-model/elixir-medical-data-model.yml
  title: ''
  type: DataModel
  url: data-model/elixir-medical-data-model.yml
- group: agent
  href: https://artifacts.apis.io/elixir-medical/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-12'
description: Elixir Medical Corporation is a privately held medical device company headquartered in Milpitas, California, developing implant and interventional platforms for coronary and peripheral artery disease. Its DynamX sirolimus-eluting coronary bioadaptor is designed to restore vessel pulsatility and compliance rather than permanently cage the artery, and holds a European CE mark, Japanese PMDA approval and a U.S. FDA Breakthrough Device designation; the LithiX Hertz Contact intravascular lithotripsy system and the DESyne family of drug-eluting stents round out the portfolio. Elixir Medical operates no developer program and publishes no product, device or clinical API. The only machine-readable surface it serves is the default WordPress REST API of its corporate marketing site, alongside an SEO-plugin-generated llms.txt.
image: https://elixirmedical.com/wp-content/uploads/2023/09/New-Elixir-Logo.png
layout: provider
modified: '2026-08-12'
name: Elixir Medical
nav: Providers
network: true
overview: 'Elixir Medical publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Health, Cardiovascular, and Coronary Intervention.


  Elixir Medical''s developer surface includes support, engineering blog, authentication, and 16 more developer resources.'
plans:
- name: Elixir Medical Plans Pricing
  plan_count: 0
  slug: elixir-medical-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Elixir Medical Rate Limits
  slug: elixir-medical-rate-limits
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 1.7
    developer_ergonomics: 25.6
    discoverability: 64.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 18.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
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
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/elixir-medical/elixir-medical-2026-09-02T145342.png
security:
- kind: authentication
  name: Elixir Medical Authentication
  slug: elixir-medical-authentication
  summary_line: http/none · 2 schemes
- kind: domain-security
  name: Elixir Medical Domain Security
  slug: elixir-medical-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Map the Elixir Medical content surface before querying it
  slug: elixir-medical-map-content-surface
- name: Track Elixir Medical clinical and corporate news
  slug: elixir-medical-track-clinical-news
slug: elixir-medical
tags:
- Company
- Medical Devices
- Health
- Cardiovascular
- Coronary Intervention
- Implants
- Life Sciences
- Content
- WordPress
website: https://elixirmedical.com/
---
