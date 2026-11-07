---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
    agent_card: near-conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://convrgent.ai
  baseurl_source: declared
  description: Convrgent API — KYH (Know Your Human) + BLAH (Be Like A Human) + KYB (Know Your Buyer)
  name: Convrgent API
  slug: convrgent-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/convrgent-ai/rules/convrgent-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/convrgent-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/convrgent-ai/conformance/convrgent-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/convrgent-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/convrgent-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/convrgent-ai/errors/convrgent-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/convrgent-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/convrgent-ai/llms/convrgent-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/convrgent-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/convrgent-ai/a2a/convrgent-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/convrgent-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/convrgent-ai/mcp/convrgent-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/convrgent-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/convrgent-ai/mcp/convrgent-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/convrgent-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/convrgent-ai/hosts/convrgent-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/convrgent-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/convrgent-ai/vendors/convrgent-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/convrgent-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/convrgent-ai/security/convrgent-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/convrgent-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://convrgent.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://convrgent.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://convrgent.ai/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Convrgent
created: '2026-10-30'
description: Convrgent is a personality intelligence platform for AI agents, offering 45 API endpoints across 11 personality frameworks such as Socionics, Enneagram, Human Design, BaZi, Vedic astrology, Numerology, and OCEAN. It operates on a pay‑per‑call model using the x402 protocol in USDC, requiring no API keys or signup. The service enables agents to profile humans, emulate human communication, and gain buyer intelligence, all without traditional authentication barriers.
image: https://convrgent.ai/opengraph-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at convrgent.ai.
  name: convrgent-ai MCP Server
  slug: convrgent-ai-mcp-yml
modified: '2026-10-30'
name: convrgent-ai
nav: Providers
network: true
overview: 'convrgent-ai publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Convrgent API. Tagged areas include Artificial Intelligence, Personality-Intelligence, x402, and Microservices.


  The convrgent-ai catalog on APIs.io includes 1 Spectral governance ruleset.


  convrgent-ai''s developer surface includes documentation, API reference, and 13 more developer resources.'
plans:
- name: Convrgent Ai Plans Pricing
  plan_count: 0
  slug: convrgent-ai-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Convrgent Ai Rate Limits
  slug: convrgent-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: convrgent-ai API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: convrgent-ai-rules
scopes:
- name: Convrgent Ai Scopes
  scope_count: 0
  slug: convrgent-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 0.0
    contract_governance: 15.9
    contract_quality: 24.0
    developer_ergonomics: 10.1
    discoverability: 56.7
    operational_transparency: 2.6
  previous_composite: 19.4
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/convrgent-ai/convrgent-ai-2026-11-03T125243.png
security:
- kind: authentication
  name: Convrgent Ai Authentication
  slug: convrgent-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Convrgent Ai Domain Security
  slug: convrgent-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: blah
  slug: convrgent-ai-blah-skill
- name: kyb
  slug: convrgent-ai-kyb-skill
- name: kyh
  slug: convrgent-ai-kyh-skill
- name: vault
  slug: convrgent-ai-vault-skill
slug: convrgent-ai
tags:
- Artificial Intelligence
- Personality-Intelligence
- x402
- Microservices
website: https://convrgent.ai/
---
