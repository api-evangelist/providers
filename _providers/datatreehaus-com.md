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
    agent_card: conformant
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Skopia is a drawing and layout engine API providing document model operations, limits, and typed refusal codes.
  name: Skopia API
  slug: skopia-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/datatreehaus-com/security/datatreehaus-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/datatreehaus-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/datatreehaus-com/llms/datatreehaus-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datatreehaus-com-llms.txt
- group: other
  href: https://artifacts.apis.io/datatreehaus-com/a2a/datatreehaus-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/datatreehaus-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/datatreehaus-com/well-known/datatreehaus-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/datatreehaus-com-security.txt
- group: agent
  href: https://artifacts.apis.io/datatreehaus-com/well-known/datatreehaus-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datatreehaus-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/datatreehaus-com/hosts/datatreehaus-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datatreehaus-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/datatreehaus-com/vendors/datatreehaus-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datatreehaus-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/datatreehaus-com/security/datatreehaus-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/datatreehaus-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/datatreehaus-com/security/datatreehaus-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datatreehaus-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datatreehaus.com/
coverage:
  checked: '2026-11-05'
  detail: The API reference page is HTML with no machine‑readable OpenAPI/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://skopia.datatreehaus.com/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: 'Datatreehaus is a small UK software studio that designs and builds web applications, booking systems and remote Model Context Protocol (MCP) servers. It offers two main products: Skopia, a drawing and layout engine with a live free MCP server at https://skopia.datatreehaus.com, and Thezi, a table booking system for independent restaurants at https://thezi.app. All services are API‑first, with typed errors and idempotent operations, ensuring software can operate them as well as people can. Contact: hello@datatreehaus.com.'
image: https://datatreehaus.com/icon-512.png
layout: provider
modified: '2026-11-05'
name: Datatreehaus
nav: Providers
network: true
overview: Datatreehaus is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Software Studio, API-First, MCP, United Kingdom, and Web Applications.
random_paper: 7
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datatreehaus Com Domain Security
  slug: datatreehaus-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Datatreehaus Com Vulnerability Disclosure
  slug: datatreehaus-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: datatreehaus-com
tags:
- Software Studio
- API-First
- MCP
- United Kingdom
- Web Applications
website: https://datatreehaus.com/
---
