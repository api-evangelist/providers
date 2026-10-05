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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/argentmill/refs/heads/main/hosts/argentmill-hosts.yml
  title: ''
  type: Hosts
  url: hosts/argentmill-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/argentmill/refs/heads/main/vendors/argentmill-vendors.yml
  title: ''
  type: Vendors
  url: vendors/argentmill-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/argentmill/refs/heads/main/security/argentmill-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/argentmill-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/argentmill
coverage:
  checked: '2026-09-26'
  detail: Venue listing on EquityZen returns 403 and provides no company website or API docs.
  evidence:
  - status: 403
    url: https://equityzen.com/company/argentmill
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Argentmill is listed on equity and business directories such as EquityZen, D&B, and Bloomberg as a corporate entity. Limited public information is available; it appears to be a financial or investment related company. No dedicated corporate website could be identified, and attempts to access the listed EquityZen page returned a 403. This stub remains pending further verification.
layout: provider
modified: '2026-09-26'
name: Argentmill
nav: Providers
network: true
overview: Argentmill is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Investment, Directory, and Stub.
random_paper: 15
score:
  band: minimal
  composite: 3.0
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
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Argentmill Domain Security
  slug: argentmill-domain-security
  summary_line: TLSv1.3 · DMARC
slug: argentmill
tags:
- Company
- Finance
- Investment
- Directory
- Stub
website: https://equityzen.com/company/argentmill
---
