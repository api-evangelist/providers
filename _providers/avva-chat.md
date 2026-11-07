---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/avva-chat/llms/avva-chat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avva-chat-llms.txt
- group: agent
  href: https://artifacts.apis.io/avva-chat/mcp/avva-chat-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/avva-chat-mcp.yml
- group: agent
  href: https://artifacts.apis.io/avva-chat/well-known/avva-chat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avva-chat-well-known.yml
- group: other
  href: https://artifacts.apis.io/avva-chat/hosts/avva-chat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avva-chat-hosts.yml
- group: other
  href: https://artifacts.apis.io/avva-chat/vendors/avva-chat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avva-chat-vendors.yml
- group: auth
  href: https://artifacts.apis.io/avva-chat/security/avva-chat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avva-chat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avva.chat/
- group: company
  title: ''
  type: Blog
  url: https://avva.chat/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avva.chat/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avva.chat/terms
- group: operate
  title: ''
  type: Support
  url: https://avva.chat/help
- group: start
  title: ''
  type: GettingStarted
  url: https://avva.chat/for-experts
coverage:
  checked: '2026-11-02'
  detail: No public API documentation or machine-readable contract was found after probing standard spec locations.
  evidence:
  - status: 404
    url: https://avva.chat/openapi.json
  - status: 404
    url: https://avva.chat/openapi.yaml
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: avva enables professionals to publish the decisions they actually made, creating decision models that AI agents can consult before answering. Built from your past decisions, the platform is ready for any AI to consult, offering free access during beta. It lets experts share how they decide as a Decision Model, allowing AI agents to check one over MCP before they answer.
image: https://avva.chat/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at avva.chat.
  name: avva MCP Server
  slug: avva-chat-mcp-yml
modified: '2026-11-02'
name: avva
nav: Providers
network: true
overview: 'avva is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, DecisionModel, Expertise, Platform, and Barcelona.


  avva''s developer surface includes engineering blog, support, getting-started guide, and 9 more developer resources.'
plans:
- name: Avva Chat Plans Pricing
  plan_count: 0
  slug: avva-chat-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Avva Chat Rate Limits
  slug: avva-chat-rate-limits
scopes:
- name: Avva Chat Scopes
  scope_count: 0
  slug: avva-chat-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 14.7
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Avva Chat Authentication
  slug: avva-chat-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Avva Chat Domain Security
  slug: avva-chat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: avva-chat
tags:
- Artificial Intelligence
- DecisionModel
- Expertise
- Platform
- Barcelona
website: https://avva.chat/
---
