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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for ChangeBook platform, providing access to codebase mapping and AI integration.
  name: ChangeBook API
  slug: changebook-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/changebook-app/security/changebook-app-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/changebook-app-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/changebook-app/llms/changebook-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/changebook-app-llms.txt
- group: auth
  href: https://artifacts.apis.io/changebook-app/well-known/changebook-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/changebook-app-security.txt
- group: auth
  href: https://artifacts.apis.io/changebook-app/well-known/changebook-app-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/changebook-app-api-security.txt
- group: agent
  href: https://artifacts.apis.io/changebook-app/well-known/changebook-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/changebook-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/changebook-app/hosts/changebook-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/changebook-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/changebook-app/vendors/changebook-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/changebook-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/changebook-app/security/changebook-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/changebook-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/changebook-app/security/changebook-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/changebook-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://changebook.app/
- group: start
  title: ''
  type: GettingStarted
  url: https://changebook.app/install
- group: commercial
  title: ''
  type: Pricing
  url: https://changebook.app/pricing
- group: docs
  title: ''
  type: APIReference
  url: https://changebook.app/mcp
coverage:
  checked: '2026-11-03'
  detail: Provider documentation pages exist but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL spec was found.
  evidence:
  - status: 404
    url: https://api.changebook.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: ChangeBook provides a living map of your codebase designed for AI agents. It offers a platform where developers can visualize, explore, and interact with their code repositories, enabling AI-driven insights, automated documentation, and intelligent code navigation. The service includes installation options via a GitHub App, MCP integration, or browser extension, and offers pricing tiers for individuals and teams. Documentation covers how it works, installation guides, connection setup, and benchmarking tools.
image: https://changebook.app/og.png
layout: provider
modified: '2026-11-03'
name: ChangeBook
nav: Providers
network: true
overview: 'ChangeBook is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Codebase, Visualization, and Documentation.


  ChangeBook''s developer surface includes getting-started guide, pricing, API reference, and 10 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Changebook App Domain Security
  slug: changebook-app-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Changebook App Vulnerability Disclosure
  slug: changebook-app-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: changebook-app
tags:
- Company
- Artificial Intelligence
- Codebase
- Visualization
- Documentation
- Integration
website: https://changebook.app/
---
