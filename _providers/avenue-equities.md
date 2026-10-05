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
  href: https://raw.githubusercontent.com/api-evangelist/avenue-equities/refs/heads/main/hosts/avenue-equities-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avenue-equities-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avenue-equities/refs/heads/main/vendors/avenue-equities-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avenue-equities-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avenue-equities/refs/heads/main/security/avenue-equities-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avenue-equities-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: 2026-09-26
  detail: The provider's website https://www.avenue-equities.com returns a JavaScript shell that cannot be rendered, preventing access to any machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://www.avenue-equities.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Avenue Equities operates within the Nasdaq Private Market ecosystem, providing a platform for buying and selling private company stock, facilitating liquidity solutions, and offering data intelligence for secondary market transactions. The company enables employees, shareholders, and accredited investors to access private equity opportunities through a regulated marketplace.
layout: provider
modified: '2026-09-26'
name: Avenue Equities
nav: Providers
network: true
overview: Avenue Equities is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Private-Market, Equity, and Trading.
random_paper: 0
score:
  band: minimal
  composite: 2.2
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
  name: Avenue Equities Domain Security
  slug: avenue-equities-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: avenue-equities
tags:
- Company
- Finance
- Private-Market
- Equity
- Trading
website: https://www.nasdaqprivatemarket.com/
---
