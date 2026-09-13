---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-09-12'
api_count: 1
apis:
- description: OAuth-protected remote Model Context Protocol endpoint served from the AgentSmyth Kong Enterprise gateway. An unauthenticated POST of an MCP tools/list request returns HTTP 401 with an RFC 9728 WWW-Au
  name: AgentSmyth MCP Server
  slug: agentsmyth-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://agentsmyth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.agentsmyth.com/
- group: start
  title: ''
  type: SignUp
  url: https://9dlk6s8r2pl.typeform.com/to/zLCApa1Y
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentsmyth.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentsmyth.com/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://agentsmyth.com/institutional-trust
- group: auth
  title: ''
  type: Compliance
  url: conformance/agentsmyth-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agentsmyth-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/agentsmyth-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/agentsmyth-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agentsmyth-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/agentsmyth-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agentsmyth-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agentsmyth-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agentsmyth-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agentsmyth-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agentsmyth-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agentsmyth-rate-limits.yml
created: '2026-09-12'
description: AgentSmyth is a New York based financial-technology company building autonomous AI agents for institutional trading and investment research. The platform orchestrates a set of specialized agents - Macro, Sentiment, Quant, Options and Earnings, plus an Agent Wealth beta - that compress the research-to-trade workflow from hours to seconds and return cited, auditable market intelligence to traders, hedge funds, banks and asset managers. Delivery is an enterprise SaaS desk with per-tenant isolation, SSO/SAML with SCIM, model allow/deny governance and optional VPC/on-prem inference. The company runs a Kong Enterprise API gateway at api.agentsmyth.com, a private Kong Konnect developer portal, and an OAuth-protected remote MCP server that exposes the agent desk to MCP clients. Founded in 2024 by Pulkit Jaiswal, Daniel McCooey and Robert DiFazio, it has raised 11.2M dollars including an 8.7M dollar seed co-led by FinTech Collective and Thomson Reuters, with BNY participating through
  its Ascent program.
image: https://cdn.sanity.io/images/rpz1t3s7/production/92d6674aeab06f9dfd19cbe31b81923ac1c1a9f7-128x128.png
layout: provider
mcp_servers:
- description: ''
  name: AgentSmyth MCP Server
  slug: agentsmyth-mcp-server
modified: '2026-09-12'
name: AgentSmyth
nav: Providers
network: true
overview: 'AgentSmyth publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Capital Markets, Artificial Intelligence, AI Agents, and Trading.


  AgentSmyth''s developer surface includes signup flow, authentication, and 16 more developer resources.'
plans:
- name: Agentsmyth Plans Pricing
  plan_count: 0
  slug: agentsmyth-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Agentsmyth Rate Limits
  slug: agentsmyth-rate-limits
scopes:
- name: Agentsmyth Scopes
  scope_count: 0
  slug: agentsmyth-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 76.7
  schema_version: 0.22.0
  scored_at: '2026-09-12'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentsmyth Authentication
  slug: agentsmyth-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agentsmyth Domain Security
  slug: agentsmyth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentsmyth
tags:
- Financial Services
- Capital Markets
- Artificial Intelligence
- AI Agents
- Trading
- Investment Research
- Market Intelligence
- MCP
- agent-native
- FinTech
website: https://agentsmyth.com/
---
