---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Agenticplug Ai Agentic Access
  operation_count: 1
  slug: agenticplug-ai-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Public HTTP API for agenticplug.ai. Includes an OAuth-protected Model Context Protocol (MCP) endpoint and public form/utility endpoints.
  name: agenticplug.ai API
  slug: agenticplug-ai-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/agenticplug-ai/agentic-access/agenticplug-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agenticplug-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/agenticplug-ai/plans/agenticplug-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agenticplug-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agenticplug-ai/rules/agenticplug-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/agenticplug-ai-rules.yml
- group: agent
  href: https://artifacts.apis.io/agenticplug-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/agenticplug-ai/authentication/agenticplug-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agenticplug-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agenticplug-ai/scopes/agenticplug-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agenticplug-ai-scopes.yml
- group: design
  href: https://artifacts.apis.io/agenticplug-ai/errors/agenticplug-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agenticplug-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agenticplug-ai/conformance/agenticplug-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenticplug-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agenticplug-ai/llms/agenticplug-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenticplug-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/agenticplug-ai/a2a/agenticplug-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agenticplug-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/agenticplug-ai/mcp/agenticplug-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agenticplug-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agenticplug-ai/mcp/agenticplug-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agenticplug-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agenticplug-ai/well-known/agenticplug-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenticplug-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/agenticplug-ai/hosts/agenticplug-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenticplug-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenticplug-ai/vendors/agenticplug-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenticplug-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agenticplug.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agenticplug.ai/privacy-policy
- group: auth
  href: https://artifacts.apis.io/agenticplug-ai/security/agenticplug-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenticplug-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenticplug.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://agenticplug.ai/agenticweb.md
- group: docs
  title: ''
  type: APIReference
  url: https://agenticplug.ai/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://agenticplug.ai/blog
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://agenticplug.ai/openapi.json
  - status: 401
    url: https://agenticplug.ai/api/mcp
  - status: 200
    url: https://agenticplug.ai/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: agenticplug.ai is an AI Search Optimization company specializing in Answer Engine Optimization (AEO), Generative Engine Optimization (GEO), and Agentic Commerce. It helps businesses dominate AI search results and become authoritative answers on platforms such as ChatGPT, Perplexity, Google AI, and Claude, offering analytics, optimization strategies, and agentic commerce solutions.
image: https://agenticplug.ai/images/agenticplug-logo-horizontal.png
layout: provider
mcp_servers:
- description: Remote MCP server at agenticplug.ai requiring OAuth.
  name: agenticplug.ai MCP Server
  slug: agenticplug-ai-mcp-yml
modified: '2026-11-01'
name: agenticplug.ai
nav: Providers
network: true
overview: 'agenticplug.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Search Optimization, Answer Engine Optimization, Generative Engine Optimization, Agentic Commerce, and Marketing.


  The agenticplug.ai catalog on APIs.io includes 1 Spectral governance ruleset.


  agenticplug.ai''s developer surface includes authentication, documentation, API reference, engineering blog, and 18 more developer resources.'
plans:
- name: Agenticplug Ai Plans Pricing
  plan_count: 2
  slug: agenticplug-ai-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Agenticplug Ai Rate Limits
  slug: agenticplug-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: agenticplug.ai API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: agenticplug-ai-rules
scopes:
- name: Agenticplug Ai Scopes
  scope_count: 1
  slug: agenticplug-ai-scopes
  summary_line: 1 scope
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 31.6
    contract_governance: 31.8
    contract_quality: 0.0
    developer_ergonomics: 27.9
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 29.1
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agenticplug Ai Authentication
  slug: agenticplug-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agenticplug Ai Domain Security
  slug: agenticplug-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: mcp-consultation
  slug: agenticplug-ai-mcp-consultation
slug: agenticplug-ai
tags:
- AI Search Optimization
- Answer Engine Optimization
- Generative Engine Optimization
- Agentic Commerce
- Marketing
website: https://agenticplug.ai/
---
