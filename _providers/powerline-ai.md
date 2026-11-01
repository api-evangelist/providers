---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Powerline provides AI-accessible email and DNS utilities via an MCP JSON‑RPC endpoint. Tools include domain health checks, DNS record validation, blacklist lookup, email header analysis, and spam‑word
  name: Powerline MCP API
  slug: powerline-mcp-api
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/powerline-ai/rate-limits/powerline-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/powerline-ai-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/powerline-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/powerline-ai/errors/powerline-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/powerline-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/powerline-ai/llms/powerline-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/powerline-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/powerline-ai/mcp/powerline-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/powerline-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/powerline-ai/mcp/powerline-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/powerline-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/powerline-ai/hosts/powerline-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/powerline-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/powerline-ai/vendors/powerline-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/powerline-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/powerline-ai/security/powerline-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/powerline-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://powerline.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://powerline.ai/inbox-preview/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://powerline.ai/terms
coverage:
  checked: '2026-10-30'
  detail: Powerline only provides an MCP JSON‑RPC endpoint without an OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://powerline.ai/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Powerline builds AI-accessible APIs that enable agents to interact with real-world services. Their flagship product, Inbox Preview, renders HTML emails across Gmail, Outlook, and Yahoo Mail, providing screenshots without requiring sign‑up. The company focuses on bridging AI models with operational tools, offering free utilities like domain and email header checks. Powerline aims to simplify AI integration for developers and enterprises.
image: https://powerline.ai/og/powerline.png
layout: provider
mcp_servers:
- description: Remote MCP server at powerline.ai.
  name: powerline-ai MCP Server
  slug: powerline-ai-mcp-yml
modified: '2026-10-30'
name: powerline-ai
nav: Providers
network: true
overview: 'powerline-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, APIs, Automation, and Email.


  powerline-ai''s developer surface includes getting-started guide and 11 more developer resources.'
plans:
- name: Powerline Ai Plans Pricing
  plan_count: 0
  slug: powerline-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Powerline Ai Rate Limits
  slug: powerline-ai-rate-limits
scopes:
- name: Powerline Ai Scopes
  scope_count: 0
  slug: powerline-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 18.3
    discoverability: 65.0
    operational_transparency: 21.1
  provenance:
    conformance: unknown
    mcp: first-party
    skills: unknown
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
  name: Powerline Ai Authentication
  slug: powerline-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Powerline Ai Domain Security
  slug: powerline-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: powerline-ai
tags:
- Company
- AI
- APIs
- Automation
- Email
- Productivity
website: https://powerline.ai/
---
