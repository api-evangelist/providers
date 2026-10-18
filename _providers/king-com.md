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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for King digital entertainment services
  name: King API
  slug: king-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/king-com/refs/heads/main/well-known/king-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/king-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/king-com/refs/heads/main/hosts/king-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/king-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/king-com/refs/heads/main/vendors/king-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/king-com-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/king-com/refs/heads/main/packages/king-com-packages.yml
  title: ''
  type: SDKs
  url: packages/king-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/king-com/refs/heads/main/packages/king-com-packages.yml
  title: ''
  type: Packages
  url: packages/king-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://king.com/termsAndConditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://king.com/privacyPolicy
- group: company
  title: ''
  type: Newsroom
  url: https://community.king.com/en/lounge/categories/news
- group: start
  title: ''
  type: Login
  url: https://community.king.com/en/entry/signin
- group: other
  title: ''
  type: Leadership
  url: https://www.king.com/corporate-and-media/team/
- group: start
  title: ''
  type: GettingStarted
  url: https://community.king.com/guide
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/king
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/king-com/refs/heads/main/security/king-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/king-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://king.com/
coverage:
  checked: '2026-10-15'
  detail: Community docs return redirects and no OpenAPI spec, indicating JavaScript‑rendered documentation.
  evidence:
  - status: 302
    url: https://community.king.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: King operates a leading digital entertainment company offering popular casual games like Candy Crush Saga, Farm Heroes, and Bubble Witch across web, mobile, and tablet platforms. With millions of daily active users worldwide, King delivers engaging, free‑to‑play experiences that sync progress across devices, fostering a vibrant community of players. The company focuses on fun, accessible gaming and continuous innovation in the online gaming space.
layout: provider
modified: '2026-10-14'
name: King
nav: Providers
network: true
overview: 'King is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, CasualGames, Mobile, and Online.


  King''s developer surface includes getting-started guide and 13 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: King Com Domain Security
  slug: king-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: king-com
tags:
- Company
- Gaming
- CasualGames
- Mobile
- Online
website: https://king.com/
---
