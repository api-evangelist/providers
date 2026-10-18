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
- description: API surface referenced on Vattenfall's developer pages, but no machine‑readable contract discovered.
  name: Vattenfall API
  slug: vattenfall-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vattenfall/refs/heads/main/hosts/vattenfall-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vattenfall-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vattenfall/refs/heads/main/vendors/vattenfall-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vattenfall-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/vattenfall/refs/heads/main/packages/vattenfall-packages.yml
  title: ''
  type: SDKs
  url: packages/vattenfall-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/vattenfall/refs/heads/main/packages/vattenfall-packages.yml
  title: ''
  type: Packages
  url: packages/vattenfall-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://group.vattenfall.com/site-assets/privacy-policy---general/
- group: company
  title: ''
  type: Newsroom
  url: https://group.vattenfall.com/press-and-media/newsroom/2026/thermal-cameras-shed-new-light-on-bird-activity-at-sea/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vattenfall
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vattenfall/refs/heads/main/security/vattenfall-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vattenfall-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vattenfall.com/
coverage:
  checked: '2026-10-15'
  detail: Attempts to fetch OpenAPI, Swagger, and GraphQL specifications from https://api.vattenfall.com returned HTTP 502 errors, indicating no machine‑readable contract is publicly available.
  evidence:
  - status: 502
    url: https://api.vattenfall.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Vattenfall is a leading European energy company focused on delivering sustainable, carbon‑free electricity and heat. Operating in multiple countries, it invests in renewable generation, energy storage, and digital solutions to accelerate the transition to fossil‑free energy. The company emphasizes innovation, customer‑centric services, and a commitment to climate goals, positioning itself as a major player in the European utilities sector.
image: https://group.vattenfall.com/globalassets/vattenfall-logo-light-blue-bg_5x3.png
layout: provider
modified: '2026-10-14'
name: Vattenfall
nav: Providers
network: true
overview: Vattenfall is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Utilities, Renewables, and Sustainability.
random_paper: 17
score:
  band: minimal
  composite: 9.3
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
    developer_ergonomics: 7.1
    discoverability: 58.9
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Vattenfall Domain Security
  slug: vattenfall-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: vattenfall
tags:
- Company
- Energy
- Utilities
- Renewables
- Sustainability
website: https://vattenfall.com/
---
