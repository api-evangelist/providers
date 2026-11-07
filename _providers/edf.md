---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://vdp.edf.fr
- group: auth
  href: https://artifacts.apis.io/edf/well-known/edf-particulier-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/edf-particulier-security.txt
- group: auth
  href: https://artifacts.apis.io/edf/well-known/edf-opendata-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/edf-opendata-security.txt
- group: agent
  href: https://artifacts.apis.io/edf/well-known/edf-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/edf-well-known.yml
- group: other
  href: https://artifacts.apis.io/edf/hosts/edf-hosts.yml
  title: ''
  type: Hosts
  url: hosts/edf-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.edf.fr/en/edf-pulse/edf-pulse-ventures/news/itw-deepintech
- group: other
  title: ''
  type: Leadership
  url: https://www.edf.fr/en/the-edf-group/inventing-the-future-of-energy/r-d-global-expertise/our-activities/edf-lab-asia-pacific/team
- group: auth
  href: https://artifacts.apis.io/edf/security/edf-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/edf-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/edf/security/edf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/edf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://edf.fr/
coverage:
  checked: '2026-10-28'
  detail: EDF website provides no public developer portal or API documentation.
  evidence:
  - status: 200
    url: https://www.edf.fr/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: EDF (Tempo tariff) is a French electric utility and energy provider, part of the Groupe EDF group. It supplies electricity and gas to residential, commercial and industrial customers, and offers various tariffs such as the Tempo tariff for electricity consumption. EDF focuses on decarbonisation, renewable energy development, and digital services for energy management. The company operates a large portfolio of nuclear, hydro, wind and solar power plants, and provides public information, developer resources, and corporate data through its website.
image: https://www.edf.fr/themes/custom/nova/assets/images/logos/logo_edf_carre.png
layout: provider
modified: '2026-10-27'
name: EDF (Tempo tariff)
nav: Providers
network: true
overview: EDF (Tempo tariff) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Utilities, France, and Renewables.
random_paper: 15
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/edf/edf-2026-11-03T131308.png
security:
- kind: domain-security
  name: Edf Domain Security
  slug: edf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Edf Vulnerability Disclosure
  slug: edf-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: edf
tags:
- Company
- Energy
- Utilities
- France
- Renewables
website: https://edf.fr/
---
