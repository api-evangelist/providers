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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/pangle/hosts/pangle-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pangle-hosts.yml
- group: other
  href: https://artifacts.apis.io/pangle/vendors/pangle-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pangle-vendors.yml
- group: auth
  href: https://artifacts.apis.io/pangle/security/pangle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pangle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pangleglobal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pangleglobal.com/resource
- group: start
  title: ''
  type: GettingStarted
  url: https://www.pangleglobal.com/monetization
- group: operate
  title: ''
  type: Support
  url: https://www.pangleglobal.com/help-center
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pangleglobal.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pangleglobal.com/terms
coverage:
  checked: '2026-10-27'
  detail: Documentation pages return HTML shells and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://www.pangleglobal.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Pangle is a mobile advertising platform owned by TikTok, offering in‑app ad solutions for publishers worldwide. It provides various ad formats, real‑time bidding, and brand‑safety tools, helping developers monetize apps through the TikTok for Business network.
layout: provider
modified: '2026-10-26'
name: Pangle
nav: Providers
network: true
overview: 'Pangle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Mobile, Monetization, TikTok, and In‑App.


  Pangle''s developer surface includes documentation, getting-started guide, support, and 6 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Pangle Domain Security
  slug: pangle-domain-security
  summary_line: TLSv1.3
slug: pangle
tags:
- Advertising
- Mobile
- Monetization
- TikTok
- In‑App
website: https://pangleglobal.com/
---
