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
  href: https://raw.githubusercontent.com/api-evangelist/betaworks/refs/heads/main/hosts/betaworks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betaworks-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/betaworks/refs/heads/main/vendors/betaworks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/betaworks-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/betaworks/refs/heads/main/security/betaworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betaworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/betaworks_stock/
coverage:
  checked: '2026-09-28'
  detail: Betaworks website renders only via JavaScript and no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://www.betaworks.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Betaworks is an American startup studio and venture capital firm that builds and invests in internet products. Founded in 2007, it has launched and supported companies such as Giphy, Dots, and Bitly. Betaworks operates as a hybrid incubator, providing capital, product expertise, and engineering resources to help startups grow. The studio focuses on media, messaging, and consumer internet services, aiming to create and scale innovative digital experiences.
layout: provider
modified: '2026-09-28'
name: Betaworks
nav: Providers
network: true
overview: Betaworks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Startups, Venture Capital, Incubator, and Media.
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
    mcp: unknown
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
  name: Betaworks Domain Security
  slug: betaworks-domain-security
  summary_line: TLSv1.3 · DMARC
slug: betaworks
tags:
- Company
- Startups
- Venture Capital
- Incubator
- Media
website: https://forgeglobal.com/betaworks_stock/
---
