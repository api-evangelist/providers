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
  score: 13.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/european-centre-for-medium-range-weather-forecasts-ecmwf/conformance/european-centre-for-medium-range-weather-forecasts-ecmwf-conformance.yml
  title: ''
  type: Conformance
  url: conformance/european-centre-for-medium-range-weather-forecasts-ecmwf-conformance.yml
- group: agent
  href: https://artifacts.apis.io/european-centre-for-medium-range-weather-forecasts-ecmwf/well-known/european-centre-for-medium-range-weather-forecasts-ecmwf-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/european-centre-for-medium-range-weather-forecasts-ecmwf-well-known.yml
- group: other
  href: https://artifacts.apis.io/european-centre-for-medium-range-weather-forecasts-ecmwf/hosts/european-centre-for-medium-range-weather-forecasts-ecmwf-hosts.yml
  title: ''
  type: Hosts
  url: hosts/european-centre-for-medium-range-weather-forecasts-ecmwf-hosts.yml
- group: build
  href: https://artifacts.apis.io/european-centre-for-medium-range-weather-forecasts-ecmwf/packages/european-centre-for-medium-range-weather-forecasts-ecmwf-packages.yml
  title: ''
  type: SDKs
  url: packages/european-centre-for-medium-range-weather-forecasts-ecmwf-packages.yml
- group: build
  href: https://artifacts.apis.io/european-centre-for-medium-range-weather-forecasts-ecmwf/packages/european-centre-for-medium-range-weather-forecasts-ecmwf-packages.yml
  title: ''
  type: Packages
  url: packages/european-centre-for-medium-range-weather-forecasts-ecmwf-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ecmwf.int/en/terms-use
- group: operate
  title: ''
  type: Support
  url: https://www.ecmwf.int/en/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ecmwf.int/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ecmwf.int/en/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.ecmwf.int/en/about/media-centre/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ecmwf
- group: auth
  href: https://artifacts.apis.io/european-centre-for-medium-range-weather-forecasts-ecmwf/security/european-centre-for-medium-range-weather-forecasts-ecmwf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/european-centre-for-medium-range-weather-forecasts-ecmwf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.ecmwf.int
created: '2026-10-26'
description: The European Centre for Medium-Range Weather Forecasts (ECMWF) is an intergovernmental organization that provides comprehensive numerical weather prediction services and climate data to its member states and the broader scientific community. Operating one of the world’s most powerful supercomputing facilities, ECMWF conducts cutting‑edge research in atmospheric science, data assimilation, and climate modelling, delivering high‑resolution forecasts, reanalysis datasets, and specialized products for sectors such as aviation, marine, and emergency management. Its open data initiatives and collaborative platforms support global efforts to understand and mitigate weather‑related risks.
layout: provider
modified: '2026-10-26'
name: European Centre for Medium-Range Weather Forecasts (ECMWF)
nav: Providers
network: true
overview: 'European Centre for Medium-Range Weather Forecasts (ECMWF) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Weather, Forecasting, Climate, Research, and Supercomputing.


  European Centre for Medium-Range Weather Forecasts (ECMWF)''s developer surface includes support and 12 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 45.5
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/european-centre-for-medium-range-weather-forecasts-ecmwf/european-centre-for-medium-range-weather-forecasts-ecmwf-2026-11-03T131637.png
security:
- kind: domain-security
  name: European Centre For Medium Range Weather Forecasts Ecmwf Domain Security
  slug: european-centre-for-medium-range-weather-forecasts-ecmwf-domain-security
  summary_line: TLSv1.3 · DMARC
slug: european-centre-for-medium-range-weather-forecasts-ecmwf
tags:
- Weather
- Forecasting
- Climate
- Research
- Supercomputing
- Organization
website: http://www.ecmwf.int
---
