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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/amfi-india/hosts/amfi-india-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amfi-india-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amfiindia.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amfiindia.com/privacy-notice
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.amfiindia.com/
- group: auth
  href: https://artifacts.apis.io/amfi-india/security/amfi-india-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amfi-india-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amfiindia.com/
coverage:
  checked: '2026-10-27'
  detail: The developer portal at https://portal.amfiindia.com/ returns a frameset with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://portal.amfiindia.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: The Association of Mutual Funds in India (AMFI) is the industry standards body representing the mutual fund sector in India. It provides research, data, regulatory guidance, and resources for investors, distributors, and fund houses, including NAV data, fund performance, and industry insights.
layout: provider
modified: '2026-10-27'
name: AMFI India
nav: Providers
network: true
overview: AMFI India is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Mutual Funds, India, and Regulation.
random_paper: 15
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amfi India Domain Security
  slug: amfi-india-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amfi-india
tags:
- Company
- Finance
- Mutual Funds
- India
- Regulation
website: https://www.amfiindia.com/
---
