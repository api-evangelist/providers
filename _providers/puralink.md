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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/puralink/hosts/puralink-hosts.yml
  title: ''
  type: Hosts
  url: hosts/puralink-hosts.yml
- group: other
  href: https://artifacts.apis.io/puralink/vendors/puralink-vendors.yml
  title: ''
  type: Vendors
  url: vendors/puralink-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://puralink.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://puralink.com/news/
- group: start
  title: ''
  type: GettingStarted
  url: https://puralink.com/get-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/puralink
- group: auth
  href: https://artifacts.apis.io/puralink/security/puralink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/puralink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.puralink.com.au/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.puralink.com.au/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Puralink provides autonomous pipe inspection robots, called the Ferret, that navigate complex wastewater, sewer, stormwater, oil and gas, mining tailings, water supply, and data‑center cooling pipe networks. The modular robot captures 360° HD footage, asset location and 3D data, and streams live via a 1 km tether, while its PuralinkOS platform stores footage, observations and condition assessments for inspection teams.
image: https://puralink.com/images/og-default.jpg
layout: provider
modified: '2026-10-24'
name: Puralink
nav: Providers
network: true
overview: 'Puralink is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include pipe inspection, Autonomous Robots, Infrastructure, Robotics, and Wastewater.


  Puralink''s developer surface includes getting-started guide and 7 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 49.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 6.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/puralink/puralink-2026-11-03T141718.png
security:
- kind: domain-security
  name: Puralink Domain Security
  slug: puralink-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: puralink
tags:
- pipe inspection
- Autonomous Robots
- Infrastructure
- Robotics
- Wastewater
- Oil and Gas
- Mining
- Data Center
website: https://www.puralink.com.au/
---
