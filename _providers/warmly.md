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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: REST API for Warmly's agent-tools surface — discover available tools, execute read tools (warm visitors, warm accounts, third-party intent signals, credit balance) and async write tools (push contacts
  name: Warmly REST API
  slug: warmly-rest-api
artifact_total: 7
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
created: '2026-07-17'
description: Warmly is a signal-based revenue orchestration and AI go-to-market platform that de-anonymizes website visitors down to the individual person, unifies first-, second-, and third-party intent signals in a unified Context Graph, and runs two autonomous agents — an Inbound Agent that converts on-site visitors through AI chat and an outbound TAM Agent that orchestrates prospecting across email, LinkedIn, and ads. Warmly exposes a REST API and a hosted, OAuth-authenticated MCP server (both live at opps-api.getwarmly.com) that let agents list warm visitors and accounts, look up third-party intent signals, check credit balances, and push identified contacts into HubSpot, Salesforce, and sequences — with outbound webhooks reporting agent-tool execution status and delivering intent signals to downstream automations.
image: https://logo.clearbit.com/warmly.ai
layout: provider
mcp_servers:
- description: ''
  name: warmly-mcp.yml
  slug: warmly-mcpyml
modified: '2026-07-21'
name: Warmly
nav: Providers
network: true
overview: 'Warmly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Marketing, Intent Data, and Revenue Orchestration.


  The Warmly catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Warmly''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 88
score:
  band: developing
  composite: 48.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 18.4
  previous_composite: 48.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
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
- Go To Market
- MCP
- Lead Generation
- CRM
website: https://warmly.ai
---
