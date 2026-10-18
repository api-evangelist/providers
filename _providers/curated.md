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
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/curated/refs/heads/main/plans/curated-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/curated-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curated/refs/heads/main/hosts/curated-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curated-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curated/refs/heads/main/vendors/curated-vendors.yml
  title: ''
  type: Vendors
  url: vendors/curated-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curated/refs/heads/main/security/curated-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curated-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/curated_stock/
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI or other machine-readable contract found at https://www.curated.co/openapi.json (404).
  evidence:
  - status: 404
    url: https://www.curated.co/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Curated is a consumer and lifestyle company tracked on Forge Global. It has raised $265.3M across Series A to C rounds, with notable investors like CapitalG, Forerunner, and Greylock Partners. The platform provides stock price history, funding details, and valuation data, though current price data is no longer available.
layout: provider
modified: '2026-10-12'
name: Curated
nav: Providers
network: true
overview: Curated is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Consumer, Lifestyle, Finance, Stocks, and Funding.
plans:
- name: Curated Plans Pricing
  plan_count: 8
  slug: curated-plans-pricing
random_paper: 18
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
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
  name: Curated Domain Security
  slug: curated-domain-security
  summary_line: TLSv1.3 · DMARC
slug: curated
tags:
- Consumer
- Lifestyle
- Finance
- Stocks
- Funding
- Company
website: https://forgeglobal.com/curated_stock/
---
