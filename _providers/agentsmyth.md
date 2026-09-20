---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-09-19'
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
  href: https://raw.githubusercontent.com/api-evangelist/agentsmyth/refs/heads/main/conformance/agentsmyth-conformance.yml
  title: ''
  type: Compliance
  url: conformance/agentsmyth-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentsmyth/refs/heads/main/llms/agentsmyth-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentsmyth-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentsmyth/refs/heads/main/well-known/agentsmyth-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentsmyth-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentsmyth/refs/heads/main/mcp/agentsmyth-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentsmyth-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentsmyth/refs/heads/main/authentication/agentsmyth-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentsmyth-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentsmyth/refs/heads/main/scopes/agentsmyth-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agentsmyth-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentsmyth/refs/heads/main/conformance/agentsmyth-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentsmyth-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentsmyth/refs/heads/main/conventions/agentsmyth-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentsmyth-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentsmyth/refs/heads/main/lifecycle/agentsmyth-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentsmyth-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentsmyth/refs/heads/main/security/agentsmyth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentsmyth-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agentsmyth/refs/heads/main/plans/agentsmyth-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentsmyth-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agentsmyth/refs/heads/main/rate-limits/agentsmyth-rate-limits.yml
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
overview: 'AgentSmyth publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Capital Markets, Artificial Intelligence, AI Agents, and Trading.


  AgentSmyth''s developer surface includes signup flow, authentication, and 16 more developer resources.'
plans:
- name: Agentsmyth Plans Pricing
  plan_count: 0
  slug: agentsmyth-plans-pricing
random_paper: 14
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
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    operational_transparency: 0.0
  previous_composite: 25.7
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
  scored_at: '2026-09-19'
  trend: flat
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
- Financial-Services
- Capital Markets
- Artificial Intelligence
- AI Agents
- Trading
- Investment Research
- Market Intelligence
- MCP
- agent-native
- Fintech
website: https://agentsmyth.com/
---
