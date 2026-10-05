---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/branded/refs/heads/main/well-known/branded-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/branded-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/branded/refs/heads/main/hosts/branded-hosts.yml
  title: ''
  type: Hosts
  url: hosts/branded-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/branded/refs/heads/main/vendors/branded-vendors.yml
  title: ''
  type: Vendors
  url: vendors/branded-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://joinbranded.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://joinbranded.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://joinbranded.com/leadership/
- group: company
  title: ''
  type: Blog
  url: https://joinbranded.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/branded/refs/heads/main/security/branded-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/branded-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://joinbranded.com/
coverage:
  checked: '2026-10-03'
  detail: The company website provides no API documentation or developer program.
  evidence:
  - status: 200
    url: https://joinbranded.com/
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: Branded is a placeholder company identified in the API Evangelist secondary-market harvest. It currently has no publicly documented API or official website. The entry exists to allow future enrichment should the company publish an API, documentation, or other digital assets. This stub includes basic maintainer information and placeholder tags, awaiting further discovery.
image: https://example.com/placeholder.png
layout: provider
modified: '2026-10-03'
name: Branded
nav: Providers
network: true
overview: 'Branded is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Private-Market, Secondary Market, Equity, and Placeholder.


  Branded''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Branded Domain Security
  slug: branded-domain-security
  summary_line: TLSv1.3 · DMARC
slug: branded
tags:
- Company
- Private-Market
- Secondary Market
- Equity
- Placeholder
website: https://joinbranded.com/
---
