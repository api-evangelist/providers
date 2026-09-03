---
access_model:
  confidence: high
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.actively.ai/sitemap.xml
  - https://www.actively.ai/pricing
  - https://app.actively.ai/
  - https://www.actively.ai/products/api-platform
  trial: false
  try_now: false
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
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Actively's hosted (remote) Model Context Protocol server, which connects its Per-Account Agents — per-account research, strategy and persistent memory — into external AI clients such as ChatGPT, Claud
  name: Actively Intelligence MCP
  slug: actively-intelligence-mcp
artifact_total: 9
common:
- group: design
  title: ''
  type: Conformance
  url: conformance/actively-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/actively-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/actively-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/actively-llms.txt
- group: auth
  title: ''
  type: Security
  url: security/actively-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/actively-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/actively-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/actively-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/actively-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/actively-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/actively-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/actively-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/actively-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/actively-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/actively-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.actively.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/actively-ai
- group: start
  title: ''
  type: SignUp
  url: https://app.actively.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.actively.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.actively.ai/privacy
- group: company
  title: ''
  type: Website
  url: https://www.actively.ai/
created: '2026-07-17'
description: Actively AI delivers "Intelligence-Led Revenue" — an AI revenue-intelligence platform whose Per-Account Agents work every prospect and customer account 24/7, surfacing next-best-actions and helping go-to-market teams execute them across the full lifecycle. The product spans an Agent Inbox, an Assistant, Watchtower, an API for embedding GTM intelligence into internal tools and workflows, and a hosted MCP server that connects its per-account agents into ChatGPT, Claude, and Cowork. Actively is backed by Bain Capital Ventures.
image: https://framerusercontent.com/images/rYdlvukOk7Ivrd88T13uZVYfc.png
layout: provider
mcp_servers:
- description: ''
  name: Actively Intelligence MCP
  slug: actively-intelligence-mcp
modified: '2026-08-13'
name: Actively
nav: Providers
network: true
overview: 'Actively publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Apps, AI Agents, Revenue Intelligence, and Sales.


  Actively''s developer surface includes authentication, engineering blog, signup flow, and 18 more developer resources.'
plans:
- name: Actively Plans Pricing
  plan_count: 0
  slug: actively-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Actively Rate Limits
  slug: actively-rate-limits
scopes:
- name: Actively Scopes
  scope_count: 0
  slug: actively-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 24.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/actively/refs/heads/main/screenshots/actively-2026-07-25T181529.png
security:
- kind: authentication
  name: Actively Authentication
  slug: actively-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Actively Domain Security
  slug: actively-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Actively Vulnerability Disclosure
  slug: actively-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Actively Trust Center
  slug: actively-trust-center
  summary_line: SOC 2 Type II, ISO 27001, HITRUST, GDPR, CCPA
slug: actively
tags:
- Company
- Ai Apps
- AI Agents
- Revenue Intelligence
- Sales
- Go-To-Market
- MCP
- Authentication
- Sales Intelligence
- Enterprise Software
website: https://www.actively.ai/
---
