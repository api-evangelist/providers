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
- group: agent
  href: https://artifacts.apis.io/tryscope-com/llms/tryscope-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tryscope-com-llms.txt
- group: other
  href: https://artifacts.apis.io/tryscope-com/hosts/tryscope-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tryscope-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/tryscope-com/vendors/tryscope-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tryscope-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.tryscope.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.tryscope.com/blog
- group: auth
  href: https://artifacts.apis.io/tryscope-com/security/tryscope-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tryscope-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tryscope.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://tryscope.com
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Scope provides an AI‑powered platform that helps businesses discover, analyze, and optimize the interactions between AI agents and their products. By surfacing where agents encounter a brand, what tasks they attempt, and where they drop off, Scope enables teams to improve user experience, increase conversion, and unlock new revenue streams. Backed by Y‑Combinator, the company combines data analytics, user‑behavior tracking, and actionable insights to empower product and marketing teams.
layout: provider
modified: '2026-10-24'
name: Scope
nav: Providers
network: true
overview: 'Scope is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Analytics, Platform, and Marketing.


  Scope''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tryscope Com Domain Security
  slug: tryscope-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tryscope-com
tags:
- Company
- AI
- Analytics
- Platform
- Marketing
website: https://tryscope.com
---
