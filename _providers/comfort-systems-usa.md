---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/comfort-systems-usa/finops/comfort-systems-usa-finops.yml
  title: ''
  type: FinOps
  url: finops/comfort-systems-usa-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.comfortsystemsusa.com
- group: company
  title: ''
  type: About
  url: https://comfortsystemsusa.com/company-profile/
- group: other
  title: ''
  type: Leadership
  url: https://comfortsystemsusa.com/management-team/
- group: other
  title: ''
  type: BoardOfDirectors
  url: https://comfortsystemsusa.com/board-of-directors/
- group: company
  title: ''
  type: Careers
  url: https://comfortsystemsusa.com/careers/
- group: operate
  title: ''
  type: ContactUs
  url: https://comfortsystemsusa.com/contact-us/
- group: other
  title: ''
  type: Sustainability
  url: https://comfortsystemsusa.com/sustainability/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://comfortsystemsusa.com/privacy-policy/
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://comfortsystemsusa.com/privacy-policy/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.comfortsystemsusa.com/
- group: company
  title: ''
  type: Newsroom
  url: https://investors.comfortsystemsusa.com/news-releases
- group: other
  title: ''
  type: SECFilings
  url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001035983
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/comfort-systems-usa
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/ComfortSystemsUsa
- group: auth
  href: https://artifacts.apis.io/comfort-systems-usa/security/comfort-systems-usa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/comfort-systems-usa-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/comfort-systems-usa/well-known/comfort-systems-usa-well-known.yml
  title: ''
  type: WellKnownProbe
  url: well-known/comfort-systems-usa-well-known.yml
- group: other
  href: https://artifacts.apis.io/comfort-systems-usa/regulatory/comfort-systems-usa-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/comfort-systems-usa-regulatory-posture.yml
- group: commercial
  href: https://artifacts.apis.io/comfort-systems-usa/plans/comfort-systems-usa-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/comfort-systems-usa-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/comfort-systems-usa/rate-limits/comfort-systems-usa-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/comfort-systems-usa-rate-limits.yml
coverage:
  checked: '2026-09-19'
  detail: 'Comfort Systems USA is an HVAC, electrical and plumbing contractor (NYSE: FIX, SIC 1731 Electrical Work) whose only web surfaces are a SiteGround-hosted WordPress marketing site and a Notified investor-relations site with no developer, API, integration or partner page anywhere in their navigation; the api.comfortsystemsusa.com and developer.comfortsystemsusa.com hosts the prior scaffolded API entry named do not exist in DNS (NXDOMAIN), and every path on comfortsystemsusa.com — including /openapi.json, /llms.txt and every /.well-known/ document — answers a 202 sgcaptcha bot-challenge shell rather than a document.'
  evidence:
  - status: 0
    url: https://api.comfortsystemsusa.com/
  - status: 0
    url: https://developer.comfortsystemsusa.com/docs
  - status: 202
    url: https://www.comfortsystemsusa.com/openapi.json
  - status: 202
    url: https://www.comfortsystemsusa.com/llms.txt
  - status: 202
    url: https://www.comfortsystemsusa.com/.well-known/agent-card.json
  - status: 403
    url: https://investors.comfortsystemsusa.com/
  - status: 200
    url: https://api.github.com/orgs/comfort-systems-usa
  - status: 404
    url: https://pypi.org/pypi/comfortsystemsusa/json
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: 'Comfort Systems USA (NYSE: FIX) is a Houston-based mechanical, electrical and plumbing contractor — one of the largest in the United States — that installs, services and maintains HVAC, piping, electrical and building-automation systems for commercial, industrial and institutional buildings through more than 45 operating companies in over 170 locations. Its business lines are construction (engineering and design, prefabrication, virtual construction), modular and off-site construction, building services (maintenance, on-demand and retrofit) and building automation (controls, monitoring, security and energy management). The company publishes no public API, developer program, SDK or machine-readable contract; its web presence is a WordPress marketing site and an investor-relations site.'
finops:
- has_sources: true
  method: generated
  name: Comfort Systems Usa Finops
  primary_unit: ''
  service_category: Construction Services
  slug: comfort-systems-usa-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/comfort-systems-usa.png
layout: provider
modified: '2026-09-19'
name: Comfort Systems USA
nav: Providers
network: true
overview: Comfort Systems USA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include HVAC, Mechanical, Construction, Electrical, and Plumbing.
plans:
- name: Comfort Systems Usa Plans Pricing
  plan_count: 0
  slug: comfort-systems-usa-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Comfort Systems Usa Rate Limits
  slug: comfort-systems-usa-rate-limits
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 4.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/comfort-systems-usa/comfort-systems-usa-2026-06-20T174811.png
security:
- kind: domain-security
  name: Comfort Systems Usa Domain Security
  slug: comfort-systems-usa-domain-security
  summary_line: TLSv1.3 · DMARC
slug: comfort-systems-usa
tags:
- HVAC
- Mechanical
- Construction
- Electrical
- Plumbing
- Building Automation
- Modular Construction
- Building Services
- Energy Management
- Fortune 1000
website: https://www.comfortsystemsusa.com
---
