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
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API reference (requires sign‑in) for todox platform.
  name: todox API
  slug: todox-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/todox-dev/llms/todox-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/todox-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/todox-dev/hosts/todox-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/todox-dev-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://todox.dev/privacy
- group: company
  title: ''
  type: Blog
  url: https://todox.dev/blog
- group: auth
  href: https://artifacts.apis.io/todox-dev/security/todox-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/todox-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://todox.dev/
coverage:
  checked: '2026-10-31'
  detail: API reference pages redirect to a sign‑in page, preventing access to machine‑readable specifications.
  reason: auth-required
  state: gated
created: '2026-10-31'
description: todox is a working memory platform for developers and their AI coding agents. It lets teams capture projects, tasks, and logs that persist across sessions, enabling seamless collaboration and context retention. Founded by Furkan Beydemir, todox aims to streamline development workflows by providing a searchable, persistent knowledge base that integrates with coding tools and agents.
image: https://todox.dev/opengraph-image.png
layout: provider
modified: '2026-10-31'
name: todox-dev
nav: Providers
network: true
overview: 'todox-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Productivity, AI, and Collaboration.


  todox-dev''s developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Todox Dev Plans Pricing
  plan_count: 0
  slug: todox-dev-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Todox Dev Rate Limits
  slug: todox-dev-rate-limits
scopes:
- name: Todox Dev Scopes
  scope_count: 0
  slug: todox-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Todox Dev Authentication
  slug: todox-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Todox Dev Domain Security
  slug: todox-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: todox-dev
tags:
- Company
- Developer Tools
- Productivity
- AI
- Collaboration
website: https://todox.dev/
---
