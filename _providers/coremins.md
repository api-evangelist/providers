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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coremins/refs/heads/main/hosts/coremins-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coremins-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coremins/refs/heads/main/vendors/coremins-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coremins-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coreandmain.com/terms-of-sale/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coreandmain.com/privacy-notice/
- group: commercial
  title: ''
  type: Pricing
  url: https://coreandmain.com/price-announcements-archive/
- group: company
  title: ''
  type: Newsroom
  url: https://coreandmain.com/news
- group: other
  title: ''
  type: Leadership
  url: https://coreandmain.com/who-we-are/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coremins/refs/heads/main/security/coremins-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coremins-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coreandmain.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://jobs.coreandmain.com/mcp
  - status: 200
    url: https://coreandmain.com
  - status: 403
    url: https://equityzen.com/company/coremins
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: Coremins is a provider of water and wastewater infrastructure solutions, offering a broad portfolio that includes pipe, valves, fittings, fire protection, HDPE fusible piping, metering, storm drainage, geosynthetics, and treatment plant equipment. The company serves utilities and industrial customers across the United States, delivering products and services that support reliable water supply, efficient waste management, and resilient infrastructure. Coremins emphasizes sustainability, innovation, and comprehensive support throughout project lifecycles.
image: https://coreandmain.com/wp-content/plugins/bb-custom/modules//connected-circle-cta/img/path.svg
layout: provider
modified: '2026-10-10'
name: Coremins
nav: Providers
network: true
overview: 'Coremins is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Water, Infrastructure, Utilities, Engineering, and Sustainability.


  Coremins'' developer surface includes pricing and 8 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coremins Domain Security
  slug: coremins-domain-security
  summary_line: TLSv1.3 · DMARC
slug: coremins
tags:
- Water
- Infrastructure
- Utilities
- Engineering
- Sustainability
- Company
website: https://coreandmain.com
---
