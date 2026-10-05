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
  href: https://raw.githubusercontent.com/api-evangelist/benxotccryptotrading/refs/heads/main/hosts/benxotccryptotrading-hosts.yml
  title: ''
  type: Hosts
  url: hosts/benxotccryptotrading-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/benxotccryptotrading/refs/heads/main/vendors/benxotccryptotrading-vendors.yml
  title: ''
  type: Vendors
  url: vendors/benxotccryptotrading-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/benxotccryptotrading/refs/heads/main/security/benxotccryptotrading-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/benxotccryptotrading-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/benxotccryptotrading
coverage:
  checked: '2026-09-27'
  detail: No public website or developer documentation was found; the equityzen listing returned HTTP 403 and no other domain could be identified.
  evidence:
  - status: 403
    url: https://equityzen.com/company/benxotccryptotrading
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Benxotccryptotrading is a stub entry created during the API Evangelist harvesting process. No public website, documentation, or API endpoints have been identified for this entity. The company appears in secondary-market listings but lacks verifiable online presence. It is listed among cryptocurrency trading firms but without any accessible resources, making it a candidate for further investigation or removal if no resources become available. This entry reflects the current state of knowledge as of the profiling date.
image: https://via.placeholder.com/150
layout: provider
modified: '2026-09-27'
name: Benxotccryptotrading
nav: Providers
network: true
overview: Benxotccryptotrading is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Trading, Finance, and Stub.
random_paper: 17
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
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
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 5.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Benxotccryptotrading Domain Security
  slug: benxotccryptotrading-domain-security
  summary_line: TLSv1.3 · DMARC
slug: benxotccryptotrading
tags:
- Company
- Cryptocurrency
- Trading
- Finance
- Stub
website: https://equityzen.com/company/benxotccryptotrading
---
