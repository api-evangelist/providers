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
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/betterpost-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/betterpost-ai/llms/betterpost-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/betterpost-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/betterpost-ai/mcp/betterpost-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/betterpost-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/betterpost-ai/well-known/betterpost-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/betterpost-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/betterpost-ai/hosts/betterpost-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betterpost-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/betterpost-ai/vendors/betterpost-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/betterpost-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://betterpost.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://betterpost.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betterpost.ai/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://betterpost.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://betterpost.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/betterpost
- group: auth
  href: https://artifacts.apis.io/betterpost-ai/security/betterpost-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betterpost-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://betterpost.ai/
coverage:
  checked: '2026-11-02'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://betterpost.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BetterPost is a writing tool that surfaces this week’s most relevant articles, blogs, and news, then drafts a complete post with working links. It provides timely, well‑sourced drafts for newsletters, blog articles, LinkedIn, and social threads, grounded in dated sources. Ten free generations are available with no signup, making it easy for agents to call and get publish‑ready content.
image: https://betterpost.ai/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at betterpost.ai.
  name: BetterPost MCP Server
  slug: betterpost-ai-mcp-yml
modified: '2026-11-02'
name: BetterPost
nav: Providers
network: true
overview: 'BetterPost is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Content Generation, AI Writing, Newsletters, and Energy News.


  BetterPost''s developer surface includes support, documentation, engineering blog, and 11 more developer resources.'
random_paper: 3
scopes:
- name: Betterpost Ai Scopes
  scope_count: 0
  slug: betterpost-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.8
    discoverability: 40.0
    operational_transparency: 2.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 22.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Betterpost Ai Authentication
  slug: betterpost-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Betterpost Ai Domain Security
  slug: betterpost-ai-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: betterpost
  slug: betterpost-ai-skill
slug: betterpost-ai
tags:
- Content Generation
- AI Writing
- Newsletters
- Energy News
website: https://betterpost.ai/
---
