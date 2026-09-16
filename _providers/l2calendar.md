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
  scored_at: '2026-09-15'
api_count: 1
apis:
- description: Agent-native content surface exposing machine-readable summaries via llms.txt and llms-full.txt for AI assistants and crawlers to help players find Lineage 2 servers.
  name: L2Calendar Agent-Native Content
  slug: l2calendar-agent-native-content
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://l2calendar.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/l2calendar/refs/heads/main/security/l2calendar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/l2calendar-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/l2calendar/refs/heads/main/plans/l2calendar-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/l2calendar-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://l2calendar.com/addnews_vip
- group: company
  title: ''
  type: Blog
  url: https://l2calendar.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://l2calendar.com/addnews
coverage:
  checked: '2026-09-13'
  detail: L2Calendar is a Next.js content platform that publishes llms.txt and llms-full.txt for agents but exposes no public API; every OpenAPI/GraphQL/MCP and /.well-known probe 404s and the only /api/ path is an internal Next.js route that 301-redirects and is Disallowed in robots.txt.
  evidence:
  - status: 404
    url: https://l2calendar.com/openapi.json
  - status: 404
    url: https://l2calendar.com/graphql
  - status: 301
    url: https://l2calendar.com/api/
  - status: 200
    url: https://l2calendar.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: Multilingual Lineage 2 private server listing platform tracking upcoming and past server openings across every game chronicle, with filters by chronicle, rates, labels, and opening date. Server owners publish announcements with optional VIP placement.
image: https://l2calendar.com/images/logo.png
layout: provider
modified: '2026-09-13'
name: L2Calendar
nav: Providers
network: true
overview: 'L2Calendar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include lineage2, MMORPG, Game Servers, Gaming, and server-listing.


  L2Calendar''s developer surface includes pricing, engineering blog, signup flow, and 3 more developer resources.'
plans:
- name: L2Calendar Plans Pricing
  plan_count: 5
  slug: l2calendar-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 46.0
    catalog_earned_first_party: 12.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 70.4
    operational_transparency: 0.0
  previous_composite: 18.6
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: L2Calendar Domain Security
  slug: l2calendar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: l2calendar
tags:
- lineage2
- MMORPG
- Game Servers
- Gaming
- server-listing
- llms-txt
- agent-native-content
website: https://l2calendar.com
---
