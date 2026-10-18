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
- description: Cringle does not appear to expose a public developer API. The website redirects to a login page with no documentation.
  name: Cringle API
  slug: cringle-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cringle/refs/heads/main/hosts/cringle-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cringle-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cringle/refs/heads/main/vendors/cringle-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cringle-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cringle/refs/heads/main/security/cringle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cringle-domain-security.yml
coverage:
  checked: '2026-10-11'
  detail: The company website redirects to a login page and provides no public API documentation or developer program.
  evidence:
  - status: 303
    url: https://www.cringle.org
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Cringle is a stub company identified in the API Evangelist secondary-market harvest. It currently lacks a public website or documented APIs. This entry serves as a placeholder for future enrichment when more information becomes available.
layout: provider
modified: '2026-10-11'
name: Cringle
nav: Providers
network: true
overview: Cringle is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Marketplace, Startups, and Technology.
random_paper: 14
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 6
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
  provenance:
    mcp: derived
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
  name: Cringle Domain Security
  slug: cringle-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cringle
tags:
- Company
- Finance
- Marketplace
- Startups
- Technology
---
