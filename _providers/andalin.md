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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/andalin/refs/heads/main/hosts/andalin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/andalin-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/andalin/refs/heads/main/vendors/andalin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/andalin-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/andalin/refs/heads/main/security/andalin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/andalin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/andalin
coverage:
  checked: 2026-09-24
  detail: Andalin website renders only a JavaScript shell, preventing machine-readable docs discovery.
  evidence:
  - status: 200
    url: https://www.andalin.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-24'
description: Andalin is a stub entry in the API Evangelist catalog, currently lacking publicly available API documentation or a verifiable corporate website. The company appears in secondary-market harvest data but no owned domain or API endpoints have been identified. Further investigation is required to determine its services, offerings, and technical interfaces.
layout: provider
modified: '2026-09-24'
name: Andalin
nav: Providers
network: true
overview: Andalin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Data, and Platform.
random_paper: 1
score:
  band: minimal
  composite: 2.1
  coverage:
    artifact_dirs: 3
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
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
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Andalin Domain Security
  slug: andalin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: andalin
tags:
- Company
- Technology
- Data
- Platform
website: https://equityzen.com/company/andalin
---
