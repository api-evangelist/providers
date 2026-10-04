---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.3
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.aptiv.com
- group: company
  title: ''
  type: Blog
  url: https://www.aptiv.com/en/insights
- group: company
  title: ''
  type: Newsroom
  url: https://www.aptiv.com/en/newsroom
- group: operate
  title: ''
  type: Support
  url: https://www.aptiv.com/en/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aptiv.com/en/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aptiv.com/en/privacy-statement
- group: company
  title: ''
  type: Careers
  url: https://www.aptiv.com/en/jobs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aptiv
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aptiv
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aptiv/refs/heads/main/well-known/aptiv-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aptiv-well-known.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aptiv/refs/heads/main/plans/aptiv-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aptiv-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aptiv/refs/heads/main/rate-limits/aptiv-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aptiv-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aptiv/refs/heads/main/finops/aptiv-finops.yml
  title: ''
  type: FinOps
  url: finops/aptiv-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aptiv/refs/heads/main/security/aptiv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aptiv-domain-security.yml
coverage:
  checked: '2026-09-18'
  detail: 'Aptiv is a Tier-1 automotive/aerospace supplier with no developer program: the api.aptiv.com and developer.aptiv.com hosts the prior record carried have no DNS record at all, the 2,020-URL www.aptiv.com sitemap contains no developer, docs or API page, the GitHub org has zero public repositories, and the LINC, ADAS-software and Connect Qualifier pages only describe "open APIs" inside OEM-contracted platforms behind contact and demo forms.'
  evidence:
  - status: 0
    url: https://developer.aptiv.com/docs
  - status: 0
    url: https://api.aptiv.com/openapi.json
  - status: 404
    url: https://www.aptiv.com/openapi.json
  - status: 404
    url: https://www.aptiv.com/llms.txt
  - status: 200
    url: https://api.github.com/orgs/aptiv
  - status: 200
    url: https://www.aptiv.com/en/solutions/linc
  reason: no-developer-program
  state: none
created: '2026-04-19'
description: 'Aptiv is a Fortune 500 Tier-1 automotive and aerospace technology supplier headquartered in Dublin, Ireland, formed from Delphi Automotive in 2017. It sells electrical architecture and interconnect systems (connectors, cabling, busbars, HellermannTyton fastening), advanced driver-assistance systems, digital cockpit and advanced compute hardware, and embedded software: the Aptiv LINC software platform, ADAS software, and Aptiv Connect Qualifier preproduction validation analytics, with Wind River (acquired 2022) as its intelligent-edge software business. Aptiv publishes no public API, developer portal, SDK or machine-readable contract; its software platforms are delivered to OEMs under program contracts, and its only public developer-facing material is marketing prose about the "open APIs" inside those platforms.'
finops:
- name: Aptiv Finops
  service_category: Industrial / Automotive
  slug: aptiv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aptiv.png
layout: provider
modified: '2026-09-18'
name: Aptiv
nav: Providers
network: true
overview: 'Aptiv is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Electrical Systems, Technology, Aerospace and Defense, and Advanced Driver-Assistance Systems.


  Aptiv''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: Aptiv Plans Pricing
  plan_count: 0
  slug: aptiv-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Aptiv Rate Limits
  slug: aptiv-rate-limits
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 49.1
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - ireland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 13.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/aptiv/refs/heads/main/screenshots/aptiv-2026-06-20T172341.png
security:
- kind: domain-security
  name: Aptiv Domain Security
  slug: aptiv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aptiv
tags:
- Automotive
- Electrical Systems
- Technology
- Aerospace and Defense
- Advanced Driver-Assistance Systems
- Connectors
- Software Defined Vehicles
- Embedded Software
website: https://www.aptiv.com
---
