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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-09-06'
api_count: 1
apis:
- baseURL: https://www.entergy.com/wp-json
  baseurl_source: declared
  description: The public, anonymous, machine-readable REST API that entergy.com's own content management system serves at https://www.entergy.com/wp-json/. It is the WordPress core REST API (plus site plugins), adv
  name: Entergy WordPress REST API
  slug: entergy-wordpress-rest-api
- description: Entergy's electric-network GIS platform at gis.entergy.com, running Esri ArcGIS Server 10.7.1. The service-info document answers anonymously and declares token-based security with a token service at h
  name: Entergy ArcGIS Server
  slug: entergy-arcgis-server
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/entergy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/entergy
- group: company
  title: ''
  type: Website
  url: https://www.entergy.com
- group: start
  title: ''
  type: CustomerPortal
  url: https://www.myentergy.com/s/login/
- group: other
  title: ''
  type: OutageMap
  url: https://www.entergy.com/outages/
- group: company
  title: ''
  type: Careers
  url: https://www.entergy.com/careers/
- group: company
  title: ''
  type: Blog
  url: https://www.entergy.com/feed/
- group: auth
  title: ''
  type: Authentication
  url: authentication/entergy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/entergy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/entergy-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/entergy-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/entergy-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/entergy-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/entergy-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/entergy-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/entergy-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.entergy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.entergy.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.entergy.com/contact
- group: start
  title: ''
  type: Login
  url: https://www.myentergy.com/s/login/
- group: company
  title: ''
  type: Newsroom
  url: https://www.entergy.com/news
created: '2026-03-21'
description: Entergy Corporation is an integrated energy company headquartered in New Orleans, Louisiana, providing electricity to more than 3 million utility customers across Arkansas, Louisiana, Mississippi, and Texas. The company operates power generation, transmission, and distribution infrastructure including nuclear, renewable, and hydroelectric resources. While Entergy does not publish a public developer API portal, it operates customer-facing digital tools (myEntergy account portal, outage map, energy efficiency toolkit) that interact with internal systems via private APIs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/entergy.png
layout: provider
modified: '2026-09-06'
name: Entergy
nav: Providers
network: true
overview: 'Entergy publishes 1 API on the [APIs.io](https://apis.io/) network: WordPress REST API. Tagged areas include Electricity, Energy, Fortune 500, Utility, and Nuclear.


  Entergy''s developer surface includes engineering blog, authentication, support, and 19 more developer resources.'
plans:
- name: Entergy Plans Pricing
  plan_count: 0
  slug: entergy-plans-pricing
press:
- date: '2026-05-25'
  title: Entergy announces $5B in customer savings delivered by ...
  url: https://www.prnewswire.com/news-releases/entergy-announces-5b-in-customer-savings-delivered-by-data-center-agreements-issues-fair-share-plus-pledge-302705301.html
- date: '2026-05-25'
  title: Entergy shares expertise on how data centers, energy ...
  url: https://www.entergy.com/blog/entergy-shares-expertise-on-how-data-centers-energy-demand-are-shaping-future
- date: '2026-05-25'
  title: Meta is building a 10 billion dollar AI data center ...
  url: https://www.facebook.com/Neewtoop/posts/meta-is-building-a-10-billion-dollar-ai-data-center-in-northeast-louisiana-the-s/996636072944252/
- date: '2026-05-25'
  title: Entergy Louisiana announces a new agreement with Meta ...
  url: https://www.entergy.com/news/entergy-louisiana-announces-a-new-agreement-with-meta-that-will-deliver-an-additional-2b-in-customer-savings
- date: '2026-05-25'
  title: Data centers and Entergy customers - We power life.
  url: https://www.entergy.com/datacenters
random_paper: 10
rate_limits:
- limit_count: 0
  name: Entergy Rate Limits
  slug: entergy-rate-limits
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 25.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 17.2
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 2.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 44.6
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/entergy/refs/heads/main/screenshots/entergy-2026-06-20T180727.png
security:
- kind: authentication
  name: Entergy Authentication
  slug: entergy-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Entergy Domain Security
  slug: entergy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: entergy
tags:
- Electricity
- Energy
- Fortune 500
- Utility
- Nuclear
- Power Generation
- Louisiana
- Geospatial
website: https://www.entergy.com
---
