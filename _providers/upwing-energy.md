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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upwing-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.upwingenergy.com/
- group: company
  title: ''
  type: About
  url: https://www.upwingenergy.com/company/what-were-about
- group: operate
  title: ''
  type: Support
  url: https://www.upwingenergy.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.upwingenergy.com/news-and-events
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.upwingenergy.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upwingenergy.com/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://www.upwingenergy.com/company/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/upwing-energy/
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/upwing-energy-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upwing-energy-llms.txt
coverage:
  checked: '2026-09-02'
  detail: Upwing Energy manufactures downhole gas-compression hardware and sells a field service around it; its own sitemap enumerates 90 pages of products, impact, careers and press with no developer, docs or API page, api./developer./docs.upwingenergy.com do not resolve in DNS, and its GitHub organization Upwing-Energy has zero public repositories.
  evidence:
  - status: 200
    url: https://www.upwingenergy.com/sitemap.xml
  - status: 404
    url: https://www.upwingenergy.com/openapi.json
  - status: 404
    url: https://www.upwingenergy.com/.well-known/agent-card.json
  - status: 0
    url: https://api.upwingenergy.com/
  - status: 200
    url: https://api.github.com/orgs/Upwing-Energy/repos
  reason: not-a-software-company
  state: none
created: '2026-09-02'
description: Upwing Energy is an energy technology company founded in 2016 and headquartered in Cerritos, California, with service operations near Houston, Texas, operating as an affiliate of Calnetix Technologies. It designs, manufactures and deploys the Subsurface Compressor System (SCS) — a downhole gas compressor installed up to two miles inside a natural gas well — along with Magnetic Drive Systems and the supporting high-speed permanent magnet motors, passive magnetic radial bearings, active magnetic thrust bearings, magnetic couplings and sensorless long-step-out variable speed drives that make it work. The company sells hardware and an end-to-end field service (planning and completions, deployment and startup, operations and monitoring, analysis and predictions) to natural gas operators worldwide, including deployments with Equinor, ENAP and operators across MENA and Central Asia. It publishes no developer program, public API, SDK or machine-readable specification.
image: https://www.upwingenergy.com/logo.svg
layout: provider
modified: '2026-09-02'
name: Upwing Energy
nav: Providers
network: true
overview: 'Upwing Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Oil and Gas, Natural Gas, and Artificial Lift.


  Upwing Energy''s developer surface includes support, engineering blog, and 9 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 10.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Upwing Energy Domain Security
  slug: upwing-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upwing-energy
tags:
- Company
- Energy
- Oil and Gas
- Natural Gas
- Artificial Lift
- Gas Compression
- Industrial Hardware
- Manufacturing
- Turbomachinery
- Field Services
website: https://www.upwingenergy.com/
---
