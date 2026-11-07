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
    agentic_commerce: self
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
  score: 7.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AI-powered SaaS Tool Intelligence Platform
  name: BizClaw API
  slug: bizclaw-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/bizclaw-xyz/conformance/bizclaw-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bizclaw-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bizclaw-xyz/llms/bizclaw-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bizclaw-xyz-llms.txt
- group: agent
  href: https://artifacts.apis.io/bizclaw-xyz/mcp/bizclaw-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bizclaw-xyz-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bizclaw-xyz/well-known/bizclaw-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bizclaw-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/bizclaw-xyz/hosts/bizclaw-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bizclaw-xyz-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bizclaw.xyz/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bizclaw.xyz/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://bizclaw.xyz/login
- group: auth
  href: https://artifacts.apis.io/bizclaw-xyz/security/bizclaw-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bizclaw-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bizclaw.xyz/
created: '2026-11-02'
description: BizClaw provides an AI-accessible business directory, enabling agents to discover, search, and interact with real-world companies. The platform offers a MCP server and REST API for natural language queries, category browsing, and detailed company profiles, supporting worldwide businesses across 25+ categories. It aims to bridge AI agents with structured business data, facilitating quote requests, capability insights, and automated task execution.
image: https://bizclaw.xyz/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at bizclaw.xyz.
  name: BizClaw MCP Server
  slug: bizclaw-xyz-mcp-yml
modified: '2026-11-02'
name: BizClaw
nav: Providers
network: true
overview: BizClaw is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Business, Directory, MCP, and REST API.
random_paper: 4
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
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
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bizclaw Xyz Domain Security
  slug: bizclaw-xyz-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bizclaw-xyz
tags:
- Artificial Intelligence
- Business
- Directory
- MCP
- REST API
- Discovery
website: https://bizclaw.xyz/
---
