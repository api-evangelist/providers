---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 7.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Pocket provides a GraphQL API for accessing personal finance data and an MCP endpoint for tool interactions.
  name: Pocket API
  slug: pocket-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/heypocket-com/llms/heypocket-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/heypocket-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/heypocket-com/well-known/heypocket-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/heypocket-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/heypocket-com/hosts/heypocket-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/heypocket-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/heypocket-com/vendors/heypocket-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/heypocket-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/heypocket-com/security/heypocket-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/heypocket-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://heypocket.com
- group: company
  title: ''
  type: Blog
  url: https://heypocket.com/blogs/blog
- group: company
  title: ''
  type: Newsroom
  url: https://heypocket.com/blogs/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://heypocket.com/pages/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://heypocket.com/pages/terms
coverage:
  checked: '2026-10-29'
  detail: Provider's API documentation is only available via JavaScript‑rendered pages, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://heypocket.com/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Pocket (operating as heypocket.com) is a fintech platform offering AI‑enhanced personal finance tools, budgeting assistance, and transaction insights. The service integrates with users’ bank accounts to provide real‑time spending analytics, automated savings recommendations, and personalized financial advice. Pocket’s public API includes a GraphQL endpoint for data queries and an MCP endpoint for tool interactions, both documented on the company site. Backed by Y Combinator, Pocket aims to simplify money management through intelligent automation and a user‑friendly web interface.
image: http://heypocket.com/cdn/shop/files/Thumnail_1.png?v=1772470703
layout: provider
modified: '2026-10-29'
name: Pocket
nav: Providers
network: true
overview: 'Pocket is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, AI, PersonalFinance, and Budgeting.


  Pocket''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Heypocket Com Domain Security
  slug: heypocket-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: heypocket-com
tags:
- Company
- Fintech
- AI
- PersonalFinance
- Budgeting
website: https://heypocket.com
---
