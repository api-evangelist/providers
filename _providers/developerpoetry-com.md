---
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: The Developer Poetry platform provides an MCP endpoint but it requires authentication; no public machine‑readable contract is available.
  name: Developer Poetry API
  slug: developer-poetry-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/developerpoetry-com/llms/developerpoetry-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/developerpoetry-com-llms.txt
- group: other
  href: https://artifacts.apis.io/developerpoetry-com/hosts/developerpoetry-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/developerpoetry-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/developerpoetry-com/vendors/developerpoetry-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/developerpoetry-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/developerpoetry-com/security/developerpoetry-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/developerpoetry-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developerpoetry.com/
coverage:
  checked: '2026-10-30'
  detail: MCP endpoint at https://developerpoetry.com/mcp returns 406 for GET and 406 for POST tools/list, indicating authentication is required.
  evidence:
  - status: 405
    url: https://developerpoetry.com/mcp
  reason: auth-required
  state: gated
created: '2026-10-30'
description: Developer Poetry is a community platform where developers share poetic reflections on code, AI, and the human experience of software development. Users can read, submit, and explore poems after completing a simple code‑reading challenge, fostering a blend of creativity and technical insight.
image: https://developerpoetry.com/og.png
layout: provider
modified: '2026-10-30'
name: developerpoetry-com
nav: Providers
network: true
overview: developerpoetry-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Poetry, Developer, AI, Community, and Platform.
plans:
- name: Developerpoetry Com Plans Pricing
  plan_count: 0
  slug: developerpoetry-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Developerpoetry Com Rate Limits
  slug: developerpoetry-com-rate-limits
scopes:
- name: Developerpoetry Com Scopes
  scope_count: 0
  slug: developerpoetry-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Developerpoetry Com Authentication
  slug: developerpoetry-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Developerpoetry Com Domain Security
  slug: developerpoetry-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: developerpoetry-com
tags:
- Poetry
- Developer
- AI
- Community
- Platform
website: https://developerpoetry.com/
---
