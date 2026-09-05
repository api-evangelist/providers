---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: REST API for Warmly's agent-tools surface — discover available tools, execute read tools (warm visitors, warm accounts, third-party intent signals, credit balance) and async write tools (push contacts
  name: Warmly REST API
  slug: warmly-rest-api
- description: Hosted, remote Model Context Protocol server exposing Warmly's agent-tools registry to MCP-capable agents (Claude Desktop, Claude Code, Cursor, Zed). Documented read tools cover identified website vis
  name: Warmly MCP Server
  slug: warmly-mcp-server
artifact_total: 11
asyncapis:
- description: ''
  name: Warmly Webhooks
  slug: warmly-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://warmly.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.warmly.ai/en/collections/5275235549-mcp_api
- group: docs
  title: ''
  type: Documentation
  url: https://help.warmly.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://help.warmly.ai/articles/9641856032-warmly-technical-documentation-rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.warmly.ai/articles/4646691220-warmly-technical-documentation-mcp-server
- group: operate
  title: ''
  type: Support
  url: https://help.warmly.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.warmly.ai/p/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.warmly.ai/p/pricing
- group: start
  title: ''
  type: SignUp
  url: https://opps.getwarmly.com/login/?signup=free
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.warmly.ai/p/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.warmly.ai/p/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/warmly-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/warmly-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/warmly-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/warmly-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/warmly-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/warmly-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.warmly.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/warmly-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/warmly-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/warmly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://security.warmly.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/warmly-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/warmly-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/warmly-scopes.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/warmly-tool-crosswalk.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/warmly-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/warmly-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/warmly-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/warmly-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/warmly-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/warmly-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getwarmly.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/warmly-changelog.yml
- group: operate
  title: ''
  type: Releases
  url: https://www.warmly.ai/p/resources/launches
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Warmly is a signal-based revenue orchestration and AI go-to-market platform that de-anonymizes website visitors down to the individual person, unifies first-, second-, and third-party intent signals in a unified Context Graph, and runs two autonomous agents — an Inbound Agent that converts on-site visitors through AI chat and an outbound TAM Agent that orchestrates prospecting across email, LinkedIn, and ads. Warmly exposes a REST API and a hosted, OAuth-authenticated MCP server (both live at opps-api.getwarmly.com) that let agents list warm visitors and accounts, look up third-party intent signals, check credit balances, and push identified contacts into HubSpot, Salesforce, and sequences — with outbound webhooks reporting agent-tool execution status and delivering intent signals to downstream automations.
image: https://logo.clearbit.com/warmly.ai
layout: provider
mcp_servers:
- description: ''
  name: Warmly MCP Server
  slug: warmly-mcp-server
modified: '2026-08-13'
name: Warmly
nav: Providers
network: true
overview: 'Warmly publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Marketing, Intent Data, and Revenue Orchestration.


  The Warmly catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Warmly''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Warmly Plans Pricing
  plan_count: 5
  slug: warmly-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Warmly Rate Limits
  slug: warmly-rate-limits
scopes:
- name: Warmly Scopes
  scope_count: 4
  slug: warmly-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode/refreshToken/clientCredentials
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 71.1
  previous_composite: 55.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/warmly/refs/heads/main/screenshots/warmly-2026-08-17T082842.png
security:
- kind: authentication
  name: Warmly Authentication
  slug: warmly-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Warmly Domain Security
  slug: warmly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Warmly Vulnerability Disclosure
  slug: warmly-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Warmly Trust Center
  slug: warmly-trust-center
  summary_line: SOC 2, GDPR, CCPA, EU Data Act
slug: warmly
tags:
- Company
- Sales
- Marketing
- Intent Data
- Revenue Orchestration
- Website Visitor Identification
- AI Agents
- Go-To-Market
- MCP
- Lead Generation
- CRM
website: https://warmly.ai
---
