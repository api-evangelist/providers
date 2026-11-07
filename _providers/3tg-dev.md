---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Testing-as-a-Service platform API (no public contract)
  name: 3TG API
  slug: 3tg-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/3tg-dev/security/3tg-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/3tg-dev-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/3tg-dev/llms/3tg-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/3tg-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/3tg-dev/well-known/3tg-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/3tg-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/3tg-dev/well-known/3tg-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/3tg-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/3tg-dev/hosts/3tg-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/3tg-dev-hosts.yml
- group: auth
  href: https://artifacts.apis.io/3tg-dev/security/3tg-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/3tg-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/3tg-dev/security/3tg-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/3tg-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://3tg.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://3tg.dev/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://3tg.dev/#pricing
- group: operate
  title: ''
  type: Support
  url: https://3tg.dev/#contact
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found at api.3tg.dev despite documentation pages.
  evidence:
  - status: unreachable
    url: https://api.3tg.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Coding Creed Technologies (operating as 3TG) provides a deterministic test generation platform that converts business rules written in Markdown tables into comprehensive TypeScript and React test suites. The service supports VS Code, IntelliJ, and any MCP agent, offering free and tiered paid plans for generating up to 50,000 tests per month. It emphasizes zero boilerplate, strong typing, and AI‑free deterministic outputs, targeting developers seeking reliable automated testing solutions.
image: https://3tg.dev/og-image.jpg
layout: provider
modified: '2026-10-31'
name: Coding Creed Technologies
nav: Providers
network: true
overview: 'Coding Creed Technologies is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Testing, TypeScript, React, Developer Tools, and Automation.


  Coding Creed Technologies'' developer surface includes documentation, pricing, support, and 8 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 11.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 3Tg Dev Domain Security
  slug: 3tg-dev-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: 3Tg Dev Vulnerability Disclosure
  slug: 3tg-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: 3tg-dev
tags:
- Testing
- TypeScript
- React
- Developer Tools
- Automation
- Company
website: https://3tg.dev/
---
