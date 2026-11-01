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
    dynamic_client_registration: true
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
  score: 18.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Blog
  url: https://blog.ticktick.com/
- group: commercial
  href: https://artifacts.apis.io/ticktick/plans/ticktick-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ticktick-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/ticktick/llms/ticktick-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ticktick-llms.txt
- group: agent
  href: https://artifacts.apis.io/ticktick/well-known/ticktick-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ticktick-well-known.yml
- group: other
  href: https://artifacts.apis.io/ticktick/hosts/ticktick-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ticktick-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://ticktick.com/about/security
- group: start
  title: ''
  type: Login
  url: https://ticktick.com/signin
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ticktick.com/
- group: auth
  href: https://artifacts.apis.io/ticktick/security/ticktick-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ticktick-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ticktick.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ticktick.com/about
- group: commercial
  title: ''
  type: Pricing
  url: https://ticktick.com/upgrade
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ticktick.com/about/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ticktick.com/about/privacy
- group: operate
  title: ''
  type: Support
  url: https://help.ticktick.com
coverage:
  checked: '2026-10-26'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL files were found on the provider's documented hosts.
  evidence:
  - status: 200
    url: https://developer.ticktick.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: TickTick is a productivity platform offering a to‑do list, calendar, habit tracker, and Pomodoro timer. It helps individuals and teams organize tasks, schedule events, track habits, and collaborate across devices. The service provides AI‑assisted task creation, real‑time sync, and integrations via MCP, CLI, and OpenAPI APIs for developers to automate workflows.
image: https://d107mjio2rjf74.cloudfront.net/web/static/build/resources/images/card.png
layout: provider
modified: '2026-10-26'
name: TickTick
nav: Providers
network: true
overview: 'TickTick is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Productivity, Task Management, Calendar, and Collaboration.


  TickTick''s developer surface includes engineering blog, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Ticktick Plans Pricing
  plan_count: 2
  slug: ticktick-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ticktick Domain Security
  slug: ticktick-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: ticktick
tags:
- Company
- Productivity
- Task Management
- Calendar
- Collaboration
website: https://ticktick.com/
---
