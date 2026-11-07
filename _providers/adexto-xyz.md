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
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Adexto Xyz Agentic Access
  operation_count: 1
  slug: adexto-xyz-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://x402.adexto.xyz
  baseurl_source: declared
  description: The X402 API from ADEXTO — 1 operation(s) for x402.
  name: ADEXTO X402 API
  slug: adexto-xyz-x402-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/adexto-xyz/agentic-access/adexto-xyz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adexto-xyz-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/adexto-xyz/rules/adexto-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/adexto-xyz-rules.yml
- group: agent
  href: https://artifacts.apis.io/adexto-xyz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/adexto-xyz/errors/adexto-xyz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adexto-xyz-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adexto-xyz/conformance/adexto-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adexto-xyz-conformance.yml
- group: other
  href: https://artifacts.apis.io/adexto-xyz/a2a/adexto-xyz-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/adexto-xyz-a2a.yml
- group: build
  href: https://artifacts.apis.io/adexto-xyz/mcp/adexto-xyz-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/adexto-xyz-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/adexto-xyz/mcp/adexto-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adexto-xyz-mcp.yml
- group: agent
  href: https://artifacts.apis.io/adexto-xyz/well-known/adexto-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adexto-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/adexto-xyz/hosts/adexto-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adexto-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/adexto-xyz/vendors/adexto-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adexto-xyz-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://adexto.xyz/security
- group: start
  title: ''
  type: GettingStarted
  url: https://adexto.xyz/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/adexto-xyz/security/adexto-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adexto-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adexto.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://adexto.xyz/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adexto.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adexto.xyz/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/0xcuy
created: '2026-10-31'
description: ADEXTO is a blockchain platform that lets creators launch AI-agent-bound tokens on a sovereign bonding curve without needing any liquidity deposit. 100 % of the token supply enters the curve, the creator holds none and earns a 0.70 % fee on every swap. Launches are gas‑only on multiple chains (Monad, Arbitrum, Robinhood Chain, Base, Arc, 0G) and support ERC‑8004 agent identities.
image: https://adexto.xyz/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at adexto.xyz.
  name: ADEXTO MCP Server
  slug: adexto-xyz-mcp-yml
modified: '2026-10-31'
name: ADEXTO
nav: Providers
network: true
overview: 'ADEXTO publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: X402 API. Tagged areas include DeFi, Token Launch, Bonding Curve, AI Agents, and Blockchain.


  The ADEXTO catalog on APIs.io includes 1 Spectral governance ruleset.


  ADEXTO''s developer surface includes getting-started guide, documentation, and 17 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: ADEXTO API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: adexto-xyz-rules
scopes:
- name: Adexto Xyz Scopes
  scope_count: 0
  slug: adexto-xyz-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 49.6
    developer_ergonomics: 17.1
    discoverability: 65.0
    operational_transparency: 7.9
  previous_composite: 34.9
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
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adexto Xyz Authentication
  slug: adexto-xyz-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Adexto Xyz Domain Security
  slug: adexto-xyz-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: buy-market
  slug: adexto-xyz-buy-market
slug: adexto-xyz
tags:
- DeFi
- Token Launch
- Bonding Curve
- AI Agents
- Blockchain
website: https://adexto.xyz/
---
