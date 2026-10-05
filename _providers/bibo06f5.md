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
api_count: 1
apis:
- description: API information not publicly documented; company provides automotive electronics solutions. No machine‑readable API contract discovered.
  name: BIBO Group API
  slug: bibo-group-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bibo06f5/refs/heads/main/vendors/bibo06f5-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bibo06f5-vendors.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bibo06f5/refs/heads/main/hosts/bibo06f5-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bibo06f5-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/bibo06f5
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bibo06f5/refs/heads/main/security/bibo06f5-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bibo06f5-domain-security.yml
coverage:
  checked: '2026-09-28'
  detail: Company website renders content via JavaScript, preventing automated extraction of API specifications.
  evidence:
  - status: 200
    url: https://en.bibo-group.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Bibo06f5 is a stub entry created by the API Evangelist harvest process. No public website, documentation, or API endpoints have been identified for this entity. It remains a placeholder pending further discovery or verification of any real services or digital presence. The entry was generated on 2026-09-28 and reflects the current lack of verifiable digital assets, serving as a marker for future investigation when more information becomes available.
layout: provider
modified: '2026-09-28'
name: Bibo06f5
nav: Providers
network: true
overview: Bibo06f5 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Stub, Placeholder, and Unverified.
random_paper: 9
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 6
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
  provenance:
    mcp: unknown
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
  name: Bibo06F5 Domain Security
  slug: bibo06f5-domain-security
  summary_line: TLSv1.3
slug: bibo06f5
tags:
- Company
- Stub
- Placeholder
- Unverified
website: https://equityzen.com/company/bibo06f5
---
