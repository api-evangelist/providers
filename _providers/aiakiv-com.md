---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    auth_clarity: bearer
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AiAkiv's Model Context Protocol (MCP) JSON-RPC API for memory storage and retrieval.
  name: AiAkiv Memory API
  slug: aiakiv-memory-api
artifact_total: 7
common:
- group: auth
  href: https://artifacts.apis.io/aiakiv-com/authentication/aiakiv-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aiakiv-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aiakiv-com/scopes/aiakiv-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aiakiv-com-scopes.yml
- group: agent
  href: https://artifacts.apis.io/aiakiv-com/llms/aiakiv-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiakiv-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aiakiv-com/mcp/aiakiv-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aiakiv-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aiakiv-com/well-known/aiakiv-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiakiv-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aiakiv-com/hosts/aiakiv-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiakiv-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiakiv-com/vendors/aiakiv-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiakiv-com-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aiakiv.com/use-cases/developers
- group: auth
  href: https://artifacts.apis.io/aiakiv-com/security/aiakiv-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiakiv-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aiakiv.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.aiakiv.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.aiakiv.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aiakiv.com/#start
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aiakiv.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aiakiv.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aiakiv.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/DpnC7ZEs4W
coverage:
  checked: '2026-11-01'
  detail: Developer documentation is public markdown but provides no machine‑readable OpenAPI, GraphQL, AsyncAPI, or gRPC spec.
  evidence:
  - status: 200
    url: https://www.aiakiv.com/docs/en/auth.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AiAkiv is a Korean-language platform that captures the context of AI-assisted work, turning AI-generated memories into searchable, shareable records for teams. It offers features like RAG, memory organization, project management, and integrations with popular models such as ChatGPT, Claude, and Gemini, helping users retain and reuse AI insights across projects.
image: https://www.aiakiv.com/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at aiakiv.com.
  name: AiAkiv MCP Server
  slug: aiakiv-com-mcp-yml
modified: '2026-11-01'
name: AiAkiv
nav: Providers
network: true
overview: 'AiAkiv is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Knowledge Management, Team Collaboration, Memory, and RAG.


  AiAkiv''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, support, and 11 more developer resources.'
plans:
- name: Aiakiv Com Plans Pricing
  plan_count: 0
  slug: aiakiv-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Aiakiv Com Rate Limits
  slug: aiakiv-com-rate-limits
scopes:
- name: Aiakiv Com Scopes
  scope_count: 3
  slug: aiakiv-com-scopes
  summary_line: 3 scopes
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 25.6
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aiakiv Com Authentication
  slug: aiakiv-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Aiakiv Com Domain Security
  slug: aiakiv-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aiakiv-com
tags:
- Artificial Intelligence
- Knowledge Management
- Team Collaboration
- Memory
- RAG
website: https://www.aiakiv.com/
---
