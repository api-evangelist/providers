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
    agent_skills: unknown
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 16.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Model Context Protocol (MCP) API for beverage marketplace operations.
  name: bev-buyer-ai-mcp
  slug: bev-buyer-ai-mcp
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/bev-buyer-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://agent-bev.ai/security
- group: agent
  href: https://artifacts.apis.io/bev-buyer-ai/llms/bev-buyer-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bev-buyer-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/bev-buyer-ai/a2a/bev-buyer-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bev-buyer-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/bev-buyer-ai/mcp/bev-buyer-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bev-buyer-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bev-buyer-ai/mcp/bev-buyer-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bev-buyer-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/bev-buyer-ai/well-known/bev-buyer-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bev-buyer-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/bev-buyer-ai/well-known/bev-buyer-ai-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bev-buyer-ai-mcp-security.txt
- group: auth
  href: https://artifacts.apis.io/bev-buyer-ai/well-known/bev-buyer-ai-agent-bev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bev-buyer-ai-agent-bev-security.txt
- group: agent
  href: https://artifacts.apis.io/bev-buyer-ai/well-known/bev-buyer-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bev-buyer-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bev-buyer-ai/hosts/bev-buyer-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bev-buyer-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bev-buyer-ai/vendors/bev-buyer-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bev-buyer-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bev-buyer-ai/security/bev-buyer-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bev-buyer-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bev-buyer-ai/security/bev-buyer-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bev-buyer-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bev-buyer.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agent-bev.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://agent-bev.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://agent-bev.ai/docs
- group: operate
  title: ''
  type: Support
  url: https://agent-bev.ai/contact
- group: commercial
  title: ''
  type: Legal
  url: https://agent-bev.ai/legal
created: '2026-11-02'
description: Agentic Enterprises S.A. operates the agent-bev platform, a business‑to‑business hub for the beverage alcohol sector. It provides a unified catalogue where buyers and sellers can discover, compare, and order products across all makers and markets. The service runs on the Model Context Protocol (MCP) and integrates with AI models like Claude, ChatGPT, and Gemini, offering a neutral, ad‑free marketplace for agents.
image: https://agent-bev.ai/icon-1024.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.bev-buyer.ai.
  name: Agentic Enterprises MCP Server
  slug: bev-buyer-ai-mcp-yml
modified: '2026-11-02'
name: Agentic Enterprises
nav: Providers
network: true
overview: 'Agentic Enterprises is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Beverages, B2B, Marketplace, Artificial Intelligence, and OpenAPI.


  Agentic Enterprises'' developer surface includes documentation, getting-started guide, support, legal docs, and 16 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 24.3
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bev Buyer Ai Domain Security
  slug: bev-buyer-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Bev Buyer Ai Vulnerability Disclosure
  slug: bev-buyer-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bev-buyer-ai
tags:
- Beverages
- B2B
- Marketplace
- Artificial Intelligence
- OpenAPI
website: https://bev-buyer.ai/
---
