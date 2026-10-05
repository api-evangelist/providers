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
- description: Brich provides audio and video distribution services; their developer portal is not publicly documented.
  name: Brich API
  slug: brich-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brich/refs/heads/main/hosts/brich-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brich-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brich/refs/heads/main/vendors/brich-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brich-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brich/refs/heads/main/security/brich-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brich-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/brich
coverage:
  checked: '2026-10-03'
  detail: Brich does not provide a public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.brichco.com
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: 'Brich is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-03'
name: Brich
nav: Providers
network: true
overview: Brich publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 14
score:
  band: minimal
  composite: 2.1
  coverage:
    artifact_dirs: 4
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
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brich Domain Security
  slug: brich-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brich
tags:
- Company
website: https://equityzen.com/company/brich
---
