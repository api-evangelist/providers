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
  href: https://raw.githubusercontent.com/api-evangelist/bynd2/refs/heads/main/hosts/bynd2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bynd2-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bynd2/refs/heads/main/vendors/bynd2-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bynd2-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bynd2/refs/heads/main/security/bynd2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bynd2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/bynd2
coverage:
  checked: '2026-10-06'
  detail: The company website redirects to a placeholder domain with no developer documentation or API endpoints.
  evidence:
  - status: 302
    url: https://bynd2.com
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Bynd2 is a pre-IPO company listed on EquityZen, offering investors the opportunity to purchase shares before a public offering. The company focuses on innovative solutions in its sector, though detailed public information is limited. As a stub entry, this profile aims to gather comprehensive API and service data as it becomes available, providing a foundation for future integration and analysis.
layout: provider
modified: '2026-10-06'
name: Bynd2
nav: Providers
network: true
overview: Bynd2 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Investment, Pre-IPO, and Technology.
random_paper: 17
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 3
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
  name: Bynd2 Domain Security
  slug: bynd2-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bynd2
tags:
- Company
- Finance
- Investment
- Pre-IPO
- Technology
website: https://equityzen.com/company/bynd2
---
