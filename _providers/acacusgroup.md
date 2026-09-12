---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acacusgroup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.acacusgroup.com/
- group: company
  title: ''
  type: About
  url: https://www.acacusgroup.com/about-acacus
- group: operate
  title: ''
  type: Support
  url: https://www.acacusgroup.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acacusgroup.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AcacusTechnologies
- group: other
  title: ''
  type: CaseStudies
  url: https://www.acacusgroup.com/acacus-case-studies
- group: operate
  title: ''
  type: PressReleases
  url: https://www.acacusgroup.com/press-releases
- group: company
  title: ''
  type: Partners
  url: https://www.acacusgroup.com/our-partners
- group: company
  title: ''
  type: Careers
  url: https://www.acacusgroup.com/careers-current-opportunities
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acacusgroup-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/acacusgroup-plans-pricing.yml
coverage:
  checked: '2026-09-06'
  detail: Acacus sells Lynx fleet management as an enterprise SaaS on a Squarespace marketing site whose own sitemap lists 39 pages with no developer, API, docs or pricing section, and DNS returns NXDOMAIN for api., docs., developer., app., portal., console. and lynx.acacusgroup.com, so there is no host anywhere that could serve a contract.
  evidence:
  - status: 200
    url: https://www.acacusgroup.com/sitemap.xml
  - status: 404
    url: https://www.acacusgroup.com/openapi.json
  - status: 404
    url: https://www.acacusgroup.com/.well-known/api-catalog
  - status: 404
    url: https://www.acacusgroup.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/AcacusTechnologies/repos
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: Acacus Group (Acacus Technologies) is a Dubai-headquartered mobility technology company founded in 2013 that builds artificial-intelligence and machine-learning software for the transportation and airline industries. Its Lynx product family — Lynx, Lynx Pro and Lynx Vision — provides intelligent fleet management, optimized dispatch built on mathematical combinatorics, disruption management, telematics and vehicle diagnostics, and deep-learning video analytics from in-vehicle cameras covering driver fatigue, lane departure, tailgating and passenger counting. Acacus also develops autonomous vehicle technology and Peregrine, an optimization solution for airline crew and airport operations. It won Best Global Startup at GITEX 2016 in Dubai and signed an MOU with Dubai Police for driverless patrol vehicles. Lynx sells as an enterprise SaaS subscription through a demo request; Acacus publishes no public developer program or machine-readable API contract.
image: https://static1.squarespace.com/static/5438b714e4b075b9ee96a464/t/694a21920a2f3425959c63b6/1766465938951/2.png?format=1500w
layout: provider
modified: '2026-09-06'
name: Acacus Group
nav: Providers
network: true
overview: 'Acacus Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fleet Management, Transportation, Logistics, and Mobility.


  Acacus Group''s developer surface includes support and 11 more developer resources.'
plans:
- name: Acacusgroup Plans Pricing
  plan_count: 0
  slug: acacusgroup-plans-pricing
random_paper: 5
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 8.4
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acacusgroup Domain Security
  slug: acacusgroup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acacusgroup
tags:
- Company
- Fleet Management
- Transportation
- Logistics
- Mobility
- Artificial Intelligence
- Machine Learning
- Autonomous Vehicles
- Telematics
- Aviation
website: https://www.acacusgroup.com/
---
