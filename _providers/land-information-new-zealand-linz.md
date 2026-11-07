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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/land-information-new-zealand-linz/well-known/land-information-new-zealand-linz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/land-information-new-zealand-linz-well-known.yml
- group: other
  href: https://artifacts.apis.io/land-information-new-zealand-linz/hosts/land-information-new-zealand-linz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/land-information-new-zealand-linz-hosts.yml
- group: other
  href: https://artifacts.apis.io/land-information-new-zealand-linz/vendors/land-information-new-zealand-linz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/land-information-new-zealand-linz-vendors.yml
- group: build
  href: https://artifacts.apis.io/land-information-new-zealand-linz/packages/land-information-new-zealand-linz-packages.yml
  title: ''
  type: SDKs
  url: packages/land-information-new-zealand-linz-packages.yml
- group: build
  href: https://artifacts.apis.io/land-information-new-zealand-linz/packages/land-information-new-zealand-linz-packages.yml
  title: ''
  type: Packages
  url: packages/land-information-new-zealand-linz-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.linz.govt.nz/resources/oia-release/registered-notices-pursuant-section-111a-national-roads-act-1953
- group: auth
  title: ''
  type: Security
  url: https://www.linz.govt.nz/guidance/landonline-support/digital-certificates-remote-access-tool-and-security/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linz.govt.nz/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.linz.govt.nz/guidance/survey/plans-supporting-notice-intention-take-land-under-section-23-public-works-act-1981
- group: company
  title: ''
  type: Newsroom
  url: https://www.linz.govt.nz/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linz
- group: auth
  href: https://artifacts.apis.io/land-information-new-zealand-linz/security/land-information-new-zealand-linz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/land-information-new-zealand-linz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.linz.govt.nz
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://lrs.linz.govt.nz/mcp
  - status: 200
    url: http://www.linz.govt.nz
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: 'Land Information New Zealand (LINZ) is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio) and added to the network as a stub for full-pipeline profiling.'
image: https://www.linz.govt.nz/sites/default/files/styles/social_media/public/static/linz-home-page_social.jpg
layout: provider
modified: '2026-10-23'
name: Land Information New Zealand (LINZ)
nav: Providers
network: true
overview: 'Land Information New Zealand (LINZ) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Property information, Crown land management, Overseas investment regulation, Land registration, and Geospatial Data.


  Land Information New Zealand (LINZ)''s developer surface includes signup flow, pricing, and 11 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 40.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.6
  provenance:
    conformance: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Land Information New Zealand Linz Domain Security
  slug: land-information-new-zealand-linz-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: land-information-new-zealand-linz
tags:
- Property information
- Crown land management
- Overseas investment regulation
- Land registration
- Geospatial Data
- Mapping
website: http://www.linz.govt.nz
---
