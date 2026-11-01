---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API reference for Skybridge framework providing endpoints for AI app integration.
  name: Skybridge API
  slug: skybridge-api
artifact_total: 4
asyncapis:
- description: ''
  name: Skybridge Tech Webhooks
  slug: skybridge-tech-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/skybridge-tech/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/skybridge-tech/asyncapi/skybridge-tech-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/skybridge-tech-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/skybridge-tech/changelog/skybridge-tech-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/skybridge-tech-changelog.yml
- group: auth
  href: https://artifacts.apis.io/skybridge-tech/authentication/skybridge-tech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/skybridge-tech-authentication.yml
- group: agent
  href: https://artifacts.apis.io/skybridge-tech/llms/skybridge-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skybridge-tech-llms.txt
- group: other
  href: https://artifacts.apis.io/skybridge-tech/a2a/skybridge-tech-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/skybridge-tech-a2a.yml
- group: other
  href: https://artifacts.apis.io/skybridge-tech/hosts/skybridge-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skybridge-tech-hosts.yml
- group: other
  href: https://artifacts.apis.io/skybridge-tech/vendors/skybridge-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/skybridge-tech-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.skybridge.tech/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.skybridge.tech/get-started/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.skybridge.tech/
- group: auth
  href: https://artifacts.apis.io/skybridge-tech/security/skybridge-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skybridge-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skybridge.tech/
coverage:
  checked: '2026-10-29'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://docs.skybridge.tech/api-reference/overview
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Skybridge is the leading open-source TypeScript framework for building MCP Apps that run on Claude, ChatGPT, VSCode, and any MCP client. It offers a full-stack React architecture, supports 100K monthly downloads, and provides extensive documentation, SDKs, and tooling for developers to create and deploy AI‑powered applications quickly and securely.
image: https://skybridge.tech/assets/Skybridge-og.jpg
layout: provider
modified: '2026-10-29'
name: skybridge-tech
nav: Providers
network: true
overview: 'skybridge-tech is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Framework, OpenSource, TypeScript, and AI.


  The skybridge-tech catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  skybridge-tech''s developer surface includes changelog, authentication, getting-started guide, documentation, and 9 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 39.8
    discoverability: 57.1
    operational_transparency: 23.7
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Skybridge Tech Authentication
  slug: skybridge-tech-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Skybridge Tech Domain Security
  slug: skybridge-tech-domain-security
  summary_line: TLSv1.3 · HSTS
slug: skybridge-tech
tags:
- Company
- Framework
- OpenSource
- TypeScript
- AI
website: https://skybridge.tech/
---
