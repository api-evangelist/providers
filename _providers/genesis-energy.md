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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.genesisenergy.com
- group: operate
  title: ''
  type: Support
  url: https://www.genesisenergy.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.genesisenergy.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.genesisenergy.com/terms-and-conditions
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/genesis-energy/refs/heads/main/security/genesis-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/genesis-energy-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/genesis-energy/refs/heads/main/conformance/genesis-energy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/genesis-energy-conformance.yml
coverage:
  checked: '2026-09-12'
  detail: Genesis Energy, L.P. is a Gulf of Mexico pipeline, marine transportation and soda ash operator with no developer program; the only machine-readable thing it publishes is a FERC informational posting website at gas.genlp.com serving NAESB WGQ location data as a CSV download, and its "Customer Activities" system at quorum.genlp.com answers an empty 404 on every anonymous path.
  evidence:
  - status: 404
    url: https://www.genesisenergy.com/openapi.json
  - status: 404
    url: https://www.genesisenergy.com/.well-known/api-catalog
  - status: 200
    url: https://gas.genlp.com/GNP_PRD_IPWS/IPWSFile/IPWSFileHandler?path=%5CTSP_30020%5C&fileName=Locations%2FLOCATIONDATA.CSV&d=True
  - status: 404
    url: https://quorum.genlp.com/
  reason: not-a-software-company
  state: none
created: '2026-03-24'
description: 'Genesis Energy, L.P. (NYSE: GEL) is a diversified midstream energy master limited partnership headquartered in Houston, Texas. It operates offshore crude oil and natural gas pipelines and platforms in the Gulf of Mexico, onshore pipelines and terminals, marine transportation for refined products and crude, and a sulfur services and soda ash (alkali) chemicals business serving refineries, producers, and industrial and commercial customers. It is a pipeline and chemicals operator, not a software vendor: it publishes no developer program, no API and no machine-readable API contract. Its only public machine-readable surface is the FERC-mandated informational posting website it runs for its interstate natural gas pipeline, which serves NAESB WGQ-shaped location and capacity data as anonymous file downloads.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/genesis-energy.png
layout: provider
modified: '2026-09-12'
name: Genesis Energy
nav: Providers
network: true
overview: 'Genesis Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Midstream, Oil and Gas, Pipelines, and Natural Gas.


  Genesis Energy''s developer surface includes support and 5 more developer resources.'
press:
- date: ''
  title: Genesis Mission has arrived. The world's most powerful ...
  url: https://www.facebook.com/energy/posts/genesis-mission-has-arrivedthe-worlds-most-powerful-scientific-platform-to-ever-/1149584817331006/
- date: ''
  title: Armada Agreement with United States Department of ...
  url: https://www.prnewswire.com/news-releases/armada-agreement-with-united-states-department-of-energy-to-accelerate-genesis-mission-302646196.html
- date: ''
  title: Energy Department Announces Collaboration Agreements ...
  url: https://www.energy.gov/articles/energy-department-announces-collaboration-agreements-24-organizations-advance-genesis
- date: ''
  title: Genesis Energy Adopts Databricks to Accelerate Data and ...
  url: https://kbi.media/press-release/genesis-energy-adopts-databricks-to-accelerate-data-and-ai-transformation/
- date: ''
  title: Genesis Energy excels in cloud data governance
  url: https://www.informatica.com/customer-success-stories/genesis-energy.html
random_paper: 15
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 55.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 11.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 15.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/genesis-energy/refs/heads/main/screenshots/genesis-energy-2026-06-20T181731.png
security:
- kind: domain-security
  name: Genesis Energy Domain Security
  slug: genesis-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: genesis-energy
tags:
- Energy
- Midstream
- Oil and Gas
- Pipelines
- Natural Gas
- Crude Oil
- Marine Transportation
- Soda Ash
website: https://www.genesisenergy.com
---
