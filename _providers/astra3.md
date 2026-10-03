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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Public API reference discovered at https://astra3.com but no machine‑readable contract was found.
  name: Astra3 API
  slug: astra3-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/astra3/refs/heads/main/vendors/astra3-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astra3-vendors.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/astra3/refs/heads/main/hosts/astra3-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astra3-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/astra3
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/astra3/refs/heads/main/security/astra3-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astra3-domain-security.yml
coverage:
  checked: '2026-09-26'
  detail: The API reference page https://astra3.com returns an HTML shell with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://astra3.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Astra3 is a company identified in the API Evangelist secondary-market harvest. It currently exists as a stub entry pending full profiling. No public website or API endpoints have been discovered yet, and the company’s online presence appears minimal or non‑existent. Further investigation may reveal additional details as they become available.
layout: provider
modified: '2026-09-26'
name: Astra3
nav: Providers
network: true
overview: Astra3 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Finance, Data, and Services.
random_paper: 18
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Astra3 Domain Security
  slug: astra3-domain-security
  summary_line: TLSv1.3
slug: astra3
tags:
- Company
- Technology
- Finance
- Data
- Services
website: https://equityzen.com/company/astra3
---
