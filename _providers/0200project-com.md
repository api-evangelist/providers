---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: 0200Project Com Agentic Access
  operation_count: 3
  slug: 0200project-com-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.0200project.com
  baseurl_source: declared
  description: The Blockchain API from 0200project — 3 operation(s) for blockchain.
  name: 0200project Blockchain API
  slug: 0200project-com-blockchain-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/0200project-com/agentic-access/0200project-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/0200project-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/0200project-com/rules/0200project-com-rules.yml
  title: ''
  type: Spectral
  url: rules/0200project-com-rules.yml
- group: design
  href: https://artifacts.apis.io/0200project-com/vocabulary/0200project-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/0200project-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/0200project-com/errors/0200project-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/0200project-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/0200project-com/conformance/0200project-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/0200project-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/0200project-com/llms/0200project-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/0200project-com-llms.txt
- group: build
  href: https://artifacts.apis.io/0200project-com/mcp/0200project-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/0200project-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/0200project-com/mcp/0200project-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/0200project-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/0200project-com/hosts/0200project-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/0200project-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/0200project-com/vendors/0200project-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/0200project-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://0200project.com/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://0200project.com/status/
- group: auth
  title: ''
  type: Security
  url: https://0200project.com/security/
- group: start
  title: ''
  type: Sandbox
  url: https://0200project.com/playground/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://0200project.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://0200project.com/changelog/
- group: docs
  title: ''
  type: Documentation
  url: https://0200project.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://0200project.com/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://0200project.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://0200project.com/faq/
- group: auth
  href: https://artifacts.apis.io/0200project-com/security/0200project-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/0200project-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/0200project-com/security/0200project-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/0200project-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://0200project.com/
created: '2026-10-31'
description: 0200project provides machine‑native tools for AI agents, offering a Base transaction decoder that translates blockchain transaction hashes into plain English explanations and strict JSON. The service includes a free tier of 50 calls per day per IP, with paid plans for higher volume. It targets developers building autonomous AI agents, finance teams, and blockchain applications, emphasizing transparency, risk‑flagging, and easy integration via an API.
image: https://0200project.com/assets/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.0200project.com.
  name: 0200project MCP Server
  slug: 0200project-com-mcp-yml
modified: '2026-10-31'
name: 0200project
nav: Providers
network: true
overview: '0200project publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Blockchain API. Tagged areas include AI Agents, Transaction decoder, and Finance tools.


  The 0200project catalog on APIs.io includes 1 Spectral governance ruleset.


  0200project''s developer surface includes sandbox, changelog, documentation, pricing, getting-started guide, support, and 17 more developer resources.'
plans:
- name: 0200Project Com Plans Pricing
  plan_count: 3
  slug: 0200project-com-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: 0200Project Com Rate Limits
  slug: 0200project-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: 0200project API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: 0200project-com-rules
scopes:
- name: 0200Project Com Scopes
  scope_count: 0
  slug: 0200project-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 57.8
    catalog_earned_first_party: 20.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 44.3
    developer_ergonomics: 16.7
    discoverability: 56.7
    operational_transparency: 42.1
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 0200Project Com Authentication
  slug: 0200project-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 0200Project Com Domain Security
  slug: 0200project-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: 0200Project Com Vulnerability Disclosure
  slug: 0200project-com-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 1
skills:
- name: explain-transaction
  slug: 0200project-com-explain-transaction
slug: 0200project-com
tags:
- AI Agents
- Transaction decoder
- Finance tools
website: https://0200project.com/
---
