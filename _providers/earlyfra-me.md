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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Stateful webhook fan‑out API for routing inbound webhooks to multiple destinations.
  name: EarlyFra.me Edge Signal Orchestration API
  slug: earlyfra-me-edge-signal-orchestration-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/earlyfra-me/conformance/earlyfra-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/earlyfra-me-conformance.yml
- group: agent
  href: https://artifacts.apis.io/earlyfra-me/llms/earlyfra-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/earlyfra-me-llms.txt
- group: agent
  href: https://artifacts.apis.io/earlyfra-me/mcp/earlyfra-me-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/earlyfra-me-mcp.yml
- group: other
  href: https://artifacts.apis.io/earlyfra-me/hosts/earlyfra-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/earlyfra-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/earlyfra-me/vendors/earlyfra-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/earlyfra-me-vendors.yml
- group: auth
  href: https://artifacts.apis.io/earlyfra-me/security/earlyfra-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/earlyfra-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://earlyfra.me/
- group: docs
  title: ''
  type: Documentation
  url: https://earlyfra.me/docs/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://earlyfra.me/.well-known/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://earlyfra.me/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://earlyfra.me/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://earlyfra.me/privacy
created: '2026-11-06'
description: EarlyFrame provides a stateful edge webhook orchestration platform with a Model Context Protocol (MCP) server. It intercepts raw webhook payloads, transforms them into structured JSON, de‑duplicates, applies conditional routing, and fans out to Discord, Slack, Telegram and custom APIs. The service offers tiered plans, including a free sandbox, and supports AI‑agent integration via JSON‑RPC MCP.
image: https://earlyfra.me/favicon.png
layout: provider
mcp_servers:
- description: Remote MCP server at relay.earlyfra.me requiring an API key.
  name: EarlyFrame MCP Server
  slug: earlyfra-me-mcp-yml
modified: '2026-11-06'
name: EarlyFrame
nav: Providers
network: true
overview: 'EarlyFrame is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Webhook, Edge Computing, MCP, AI Integration, and Automation.


  EarlyFrame''s developer surface includes documentation, API reference, pricing, and 9 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Earlyfra Me Domain Security
  slug: earlyfra-me-domain-security
  summary_line: TLSv1.3 · DMARC
slug: earlyfra-me
tags:
- Webhook
- Edge Computing
- MCP
- AI Integration
- Automation
website: https://earlyfra.me/
---
