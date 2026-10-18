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
  href: https://raw.githubusercontent.com/api-evangelist/sdge-com/refs/heads/main/hosts/sdge-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sdge-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sdge-com/refs/heads/main/vendors/sdge-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sdge-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.sdge.com/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sdge.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SDGE
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sdge-com/refs/heads/main/security/sdge-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sdge-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sdge.com
coverage:
  checked: '2026-10-13'
  detail: 'No public API contract. developer.sdge.com and api.sdge.com yielded no OpenAPI/AsyncAPI/GraphQL; www.sdge.com returns 403 to automated clients (bot wall, incl. /mcp). Green Button Connect My Data (CPUC-mandated ESPI data sharing) exists for registered third parties per Green Button Alliance (2016: 28 registered third parties), but its registration and API docs are not publicly reachable, so no apis[] entry was recorded.'
  evidence:
  - status: 200
    url: https://developer.sdge.com/
  - status: 404
    url: https://api.sdge.com/
  - status: 200
    url: https://www.greenbuttonalliance.org/news/san-diego-gas-and-electric-sdge
  reason: customer-only-docs
  state: gated
created: '2026-10-13'
description: San Diego Gas & Electric (SDG&E) is a regulated electric and natural gas utility serving San Diego and southern Orange County, a subsidiary of Sempra. Under CPUC rules it offers Green Button Download My Data and Green Button Connect My Data, letting customers authorize registered third parties to receive their energy usage data via the SDG&E My Account portal. No public developer portal or machine-readable API contract was found.
layout: provider
modified: '2026-10-13'
name: San Diego Gas & Electric
nav: Providers
network: true
overview: 'San Diego Gas & Electric is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Utilities, Electricity, and Natural Gas.


  San Diego Gas & Electric''s developer surface includes getting-started guide, documentation, and 5 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 44.6
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sdge Com Domain Security
  slug: sdge-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sdge-com
tags:
- Company
- Energy
- Utilities
- Electricity
- Natural Gas
- Green Button
- Energy Data
website: https://www.sdge.com
---
