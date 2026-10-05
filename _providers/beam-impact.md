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
  href: https://raw.githubusercontent.com/api-evangelist/beam-impact/refs/heads/main/hosts/beam-impact-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beam-impact-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beam-impact/refs/heads/main/vendors/beam-impact-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beam-impact-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beam-impact/refs/heads/main/security/beam-impact-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beam-impact-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: '2026-09-27'
  detail: Beam Impact website renders content via JavaScript, providing no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.beamimpact.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Beam Impact enables investors and employees to buy and sell Beam Impact shares on the Nasdaq Private Market platform, providing liquidity for pre-IPO stock. The company offers a regulated marketplace for private company equity, facilitating secondary transactions and capital solutions for growth.
layout: provider
modified: '2026-09-27'
name: Beam Impact
nav: Providers
network: true
overview: Beam Impact is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Marketplace, Private Equity, and Liquidity.
random_paper: 10
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 4
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
    mcp: derived
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
  name: Beam Impact Domain Security
  slug: beam-impact-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beam-impact
tags:
- Company
- Finance
- Marketplace
- Private Equity
- Liquidity
website: https://www.nasdaqprivatemarket.com/
---
