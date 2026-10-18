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
- description: Catenoid provides AI video technology platform. Documentation is at the website but no machine-readable API spec was found.
  name: Catenoid API
  slug: catenoid-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/catenoid/refs/heads/main/hosts/catenoid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/catenoid-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/catenoid/refs/heads/main/vendors/catenoid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/catenoid-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/catenoid/refs/heads/main/security/catenoid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/catenoid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/catenoid
coverage:
  checked: '2026-10-07'
  detail: The Catenoid website provides HTML documentation but no OpenAPI, GraphQL, or other machine-readable API contract was discovered after probing common spec endpoints.
  evidence:
  - status: 200
    url: https://www.catenoid.net/en/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Catenoid is a technology company identified through the API Evangelist secondary-market harvest. While detailed public information is limited, the stub indicates the organization is positioned to develop or provide API-driven services. Further investigation is required to ascertain its product offerings, target markets, and operational scope. The current profile serves as a placeholder pending discovery of official documentation, website, and API specifications.
layout: provider
modified: '2026-10-07'
name: Catenoid
nav: Providers
network: true
overview: Catenoid is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Platform, and Services.
random_paper: 3
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Catenoid Domain Security
  slug: catenoid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: catenoid
tags:
- Company
- Technology
- Platform
- Services
website: https://equityzen.com/company/catenoid
---
