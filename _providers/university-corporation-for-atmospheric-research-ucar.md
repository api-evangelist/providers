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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/university-corporation-for-atmospheric-research-ucar/hosts/university-corporation-for-atmospheric-research-ucar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/university-corporation-for-atmospheric-research-ucar-hosts.yml
- group: other
  href: https://artifacts.apis.io/university-corporation-for-atmospheric-research-ucar/vendors/university-corporation-for-atmospheric-research-ucar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/university-corporation-for-atmospheric-research-ucar-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ucar.edu/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ucar.edu/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.ucar.edu/terms-of-use/media
- group: other
  title: ''
  type: Leadership
  url: https://www.ucar.edu/who-we-are/leadership/ucar-community-programs-ucp-director-search/search-committee
- group: auth
  href: https://artifacts.apis.io/university-corporation-for-atmospheric-research-ucar/security/university-corporation-for-atmospheric-research-ucar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/university-corporation-for-atmospheric-research-ucar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.ucar.edu
coverage:
  checked: '2026-10-23'
  detail: UCAR provides scientific data and education but does not expose a public API.
  evidence:
  - status: 200
    url: https://www.ucar.edu
  reason: not-a-software-company
  state: none
created: '2026-10-23'
description: University Corporation for Atmospheric Research (UCAR) is a nonprofit consortium of universities and research institutions dedicated to advancing the atmospheric and Earth system sciences. UCAR operates the National Center for Atmospheric Research (NCAR) and provides a hub for scientific discovery, education, and community programs. Its mission includes supporting member institutions, accelerating research, and delivering data and services that enable scientists to better understand weather, climate, and the environment. UCAR’s public presence includes extensive resources, educational materials, and outreach, though it does not currently expose a public API for its services.
layout: provider
modified: '2026-10-23'
name: University Corporation for Atmospheric Research (UCAR)
nav: Providers
network: true
overview: University Corporation for Atmospheric Research (UCAR) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Research, AtmosphericScience, Education, and Nonprofit.
random_paper: 1
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: University Corporation For Atmospheric Research Ucar Domain Security
  slug: university-corporation-for-atmospheric-research-ucar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-corporation-for-atmospheric-research-ucar
tags:
- Company
- Research
- AtmosphericScience
- Education
- Nonprofit
website: http://www.ucar.edu
---
