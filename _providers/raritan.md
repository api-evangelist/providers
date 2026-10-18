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
  href: https://raw.githubusercontent.com/api-evangelist/raritan/refs/heads/main/hosts/raritan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/raritan-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/raritan/refs/heads/main/packages/raritan-packages.yml
  title: ''
  type: SDKs
  url: packages/raritan-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/raritan/refs/heads/main/packages/raritan-packages.yml
  title: ''
  type: Packages
  url: packages/raritan-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.raritan.com/about-us/legal/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.raritan.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.raritan.com/about-us/legal/privacy-statement
- group: company
  title: ''
  type: Newsroom
  url: https://www.raritan.com/about-us/newsroom
- group: start
  title: ''
  type: Login
  url: https://www.raritan.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.raritan.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/raritan/refs/heads/main/security/raritan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/raritan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.raritan.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.raritan.com
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Raritan is a leading provider of power management solutions, DCIM software, and KVM-over-IP for data centers of all sizes. They offer reliable power distribution, intelligent rack PDUs, and comprehensive data center infrastructure management tools to help enterprises monitor and control power usage, improve efficiency, and ensure uptime across IT equipment.
layout: provider
modified: '2026-10-14'
name: Raritan
nav: Providers
network: true
overview: 'Raritan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Power Management, DCIM, KVM-over-IP, and Data Center.


  Raritan''s developer surface includes support, engineering blog, and 9 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Raritan Domain Security
  slug: raritan-domain-security
  summary_line: TLSv1.3
slug: raritan
tags:
- Company
- Power Management
- DCIM
- KVM-over-IP
- Data Center
website: https://www.raritan.com
---
