---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-09-21'
api_count: 2
apis:
- description: Remote Model Context Protocol server (Streamable HTTP) at https://travel.augworlds.ai/mcp. Clients authenticate with OAuth 2.1 — the client registers itself and runs authorization_code + PKCE with a b
  name: Travel World MCP Server
  slug: travel-world-mcp-server
- description: 'Agent-to-Agent surface declared by the A2A 1.0 agent card at https://travel.augworlds.ai/.well-known/agent-card.json: a JSONRPC binding at https://travel.augworlds.ai/a2a secured by a Travel World-iss'
  name: Travel World A2A Agent
  slug: travel-world-a2a-agent
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://augworlds.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://augworlds.ai/mcp
- group: start
  title: ''
  type: SignUp
  url: https://augworlds.ai/
- group: start
  title: ''
  type: Login
  url: https://travel.augworlds.ai/api/auth/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://travel.augworlds.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://travel.augworlds.ai/terms
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/augworlds-ai/refs/heads/main/mcp/augworlds-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/augworlds-ai-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/augworlds-ai/refs/heads/main/a2a/augworlds-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/augworlds-ai-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/augworlds-ai/refs/heads/main/well-known/augworlds-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/augworlds-ai-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augworlds-ai/refs/heads/main/scopes/augworlds-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/augworlds-ai-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augworlds-ai/refs/heads/main/authentication/augworlds-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/augworlds-ai-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/augworlds-ai/refs/heads/main/conformance/augworlds-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/augworlds-ai-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/augworlds-ai/refs/heads/main/conventions/augworlds-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/augworlds-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/augworlds-ai/refs/heads/main/errors/augworlds-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/augworlds-ai-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/augworlds-ai/refs/heads/main/rate-limits/augworlds-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/augworlds-ai-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/augworlds-ai/refs/heads/main/plans/augworlds-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/augworlds-ai-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/augworlds-ai/refs/heads/main/llms/augworlds-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/augworlds-ai-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augworlds-ai/refs/heads/main/security/augworlds-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/augworlds-ai-domain-security.yml
created: '2026-09-19'
description: Travel World is the agent-native travel product of Augmented Worlds (augworlds.ai), an invite-only private beta in which members get a personal travel agent that searches and compares real flights and hotels, checks airline flight status by number, pulls city guides, and shapes results with saved loyalty programs and preferences, then hands checkout to the member as a Stripe Link so nothing is charged without a human present. It is exposed to agents as a remote MCP server gated by OAuth 2.1 (dynamic client registration + PKCE) or a tvl_ personal access token, and as an A2A 1.0 agent card with a bearer-gated JSON-RPC endpoint, both on travel.augworlds.ai. No REST contract, SDK or CLI is published; membership is free but by invitation.
image: https://travel.augworlds.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Travel World MCP Server
  slug: travel-world-mcp-server
- description: ''
  name: Travel World MCP Server
  slug: travel-world-mcp-server-2
modified: '2026-09-19'
name: Travel World
nav: Providers
network: true
overview: 'Travel World publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Flights, Hotels, and Travel Agent.


  Travel World''s developer surface includes documentation, signup flow, authentication, and 15 more developer resources.'
plans:
- name: Augworlds Ai Plans Pricing
  plan_count: 1
  slug: augworlds-ai-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Augworlds Ai Rate Limits
  slug: augworlds-ai-rate-limits
scopes:
- name: Augworlds Ai Scopes
  scope_count: 0
  slug: augworlds-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 68.5
    operational_transparency: 0.0
  previous_composite: 24.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Augworlds Ai Authentication
  slug: augworlds-ai-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Augworlds Ai Domain Security
  slug: augworlds-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: augworlds-ai
tags:
- Company
- Travel
- Flights
- Hotels
- Travel Agent
- MCP
- A2A
- AI Agents
- Authentication
- Marketplace
website: https://augworlds.ai/
---
