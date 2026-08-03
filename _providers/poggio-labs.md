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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Versioned REST API (v2) exposing Poggio account intelligence, context search, account digests, the superagent chat, Salesforce account-plan writeback, and third-party integration registration. Secured
  name: Poggio REST API v2
  slug: poggio-rest-api-v2
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/poggio-labs-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://poggio.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://poggio.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://poggio.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://poggio.io/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://poggio.io/docs
- group: company
  title: ''
  type: Blog
  url: https://poggio.io/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://poggio.io/pricing
- group: start
  title: ''
  type: Login
  url: https://poggio.io/app/sign-in
- group: operate
  title: ''
  type: Support
  url: mailto:hello@poggio.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://poggio.io/docs/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://poggio.io/docs/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.poggio.io/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.poggio.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/poggiolabs
- group: agent
  title: ''
  type: MCPServer
  url: mcp/poggio-labs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/poggio-labs-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/poggio-labs-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/poggio-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/poggio-labs-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/poggio-labs-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/poggio-labs-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/poggio-labs-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Poggio (Poggio Labs) is an AI revenue intelligence platform for enterprise sales teams — a "Revenue Superagent" that unlocks Salesforce investment by combining deep-research AI agents with a unified context engine connecting CRM, call recordings (Gong), documents, and real-time web intelligence to arm sellers with always-current account knowledge, prioritization, relationship maps, and automated account plans. Poggio exposes its intelligence programmatically through a versioned REST API (v2) and a hosted Model Context Protocol (MCP) server, both secured with OAuth 2.0 (authorization code, client credentials, refresh token) and dynamic client registration, plus native Slack, Salesforce/Agentforce, Highspot, and Gong integrations. Backed by Accel.
image: https://poggio.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: poggio-labs-mcp.yml
  slug: poggio-labs-mcpyml
modified: '2026-07-20'
name: Poggio Labs
nav: Providers
network: true
overview: 'Poggio Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, Revenue Intelligence, Sales, and Account Intelligence.


  Poggio Labs'' developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, authentication, and 17 more developer resources.'
random_paper: 63
score:
  band: thin
  composite: 37.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 37.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Poggio Labs Authentication
  slug: poggio-labs-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Poggio Labs Domain Security
  slug: poggio-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Poggio Labs Trust Center
  slug: poggio-labs-trust-center
  summary_line: SOC 2, ISO 27001
slug: poggio-labs
tags:
- Company
- Ai
- Revenue Intelligence
- Sales
- Account Intelligence
- CRM
- Salesforce
- MCP
- AI Agents
- Enterprise
website: https://poggio.io/
---
