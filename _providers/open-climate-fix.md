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
api_count: 1
apis:
- description: Open Climate Fix provides AI-driven forecasting APIs for solar, wind, and demand energy systems.
  name: Open Climate Fix API
  slug: open-climate-fix-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/open-climate-fix/refs/heads/main/hosts/open-climate-fix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/open-climate-fix-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/open-climate-fix/refs/heads/main/vendors/open-climate-fix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/open-climate-fix-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.openclimatefix.org/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-climate-fix/refs/heads/main/security/open-climate-fix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/open-climate-fix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openclimatefix.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.openclimatefix.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.openclimatefix.org
- group: start
  title: ''
  type: GettingStarted
  url: https://www.openclimatefix.org/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.openclimatefix.org/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openclimatefix
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.openclimatefix.org/privacy-policy
coverage:
  checked: '2026-10-13'
  detail: The provider's website lists API solutions but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications were found.
  evidence:
  - status: 0
    url: https://api.openclimatefix.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Open Climate Fix delivers AI-driven forecasting solutions for solar, wind, and demand energy systems. By leveraging satellite data and advanced models, they provide accurate, minutes‑to‑hours ahead predictions to help grids run cleaner and more efficiently. Their work spans solar forecasting, wind forecasting, cloud‑casting, and data unlocking, supporting the global energy transition.
image: https://cdn.sanity.io/images/x5ci0v8g/production/c1e7ebcee93ab22e4f4040a4acc4446116b1f76e-1920x1080.png?rect=0,36,1920,1008&w=1200&h=630&fit=max&auto=format
layout: provider
modified: '2026-10-13'
name: Open Climate Fix
nav: Providers
network: true
overview: 'Open Climate Fix is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Artificial Intelligence, Forecasting, and Climate.


  Open Climate Fix''s developer surface includes documentation, getting-started guide, support, and 8 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 58.9
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 7.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Open Climate Fix Domain Security
  slug: open-climate-fix-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: open-climate-fix
tags:
- Company
- Energy
- Artificial Intelligence
- Forecasting
- Climate
website: https://openclimatefix.org
---
