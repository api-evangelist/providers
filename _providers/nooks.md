---
access_model:
  confidence: medium
  label: Public API, sales-gated pricing
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://developer.nooks.in/
  - https://www.nooks.ai/pricing
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Nooks Agentic Access
  operation_count: 37
  slug: nooks-agentic-access
  summary_line: 37 operations · 13 acting
api_count: 2
apis:
- description: The Nooks Sequencing API (also published as the "Nooks External API") provides programmatic access to sequences, sequence steps, sequence states (enrollments), prospects, accounts, notes, tasks, calls
  name: Nooks Sequencing API
  slug: nooks-sequencing-api
- description: Nooks operates a hosted, remote Model Context Protocol server at https://mcp.nooks.in/. It is OAuth-protected — an anonymous `tools/list` returns HTTP 401 `invalid_token` — and publishes RFC 9728 prot
  name: Nooks MCP Server
  slug: nooks-mcp-server
artifact_total: 12
asyncapis:
- description: ''
  name: Nooks Webhooks
  slug: nooks-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.nooks.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.nooks.in/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nooks.in/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.nooks.in/
- group: operate
  title: ''
  type: Support
  url: https://nooks.help.usepylon.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://nooks.help.usepylon.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NooksApp
- group: start
  title: ''
  type: Login
  url: https://app.nooks.in
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nooks.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.nooks.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nooks.ai/terms-of-services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nooks.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nooks.in/
- group: auth
  title: ''
  type: TrustCenter
  url: security/nooks-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.nooks.ai/
- group: auth
  title: ''
  type: Security
  url: https://www.nooks.ai/responsible-disclosure-process
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nooks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nooks-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nooks-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nooks-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/nooks-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nooks-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nooks-agentic-access.yml
created: '2026-07-17'
description: Nooks is an AI-native revenue/sales engagement platform positioned as "The Agent Workspace for Intelligent Outbound," where sales representatives and AI agents collaborate on prospecting, sequencing, dialing, and coaching inside a single workspace. Its products include an AI Parallel Dialer, AI Sequencing, AI Coaching, Signals Intelligence, and a Virtual Salesfloor, aimed at helping revenue and SDR teams build more pipeline with less manual work. Nooks publishes a public Nooks Sequencing API (the "Nooks External API") documented with a Scalar-rendered OpenAPI 3.1.0 contract at developer.nooks.in, served from partner-api.nooks.in/v1, covering sequences, sequence steps, sequence states, prospects, accounts, notes, tasks, calls, call dispositions, emails, email templates, mailboxes, and users. Authentication accepts either a workspace-scoped `nooks-api-` API key or an OAuth 2.0 authorization-code + PKCE access token from oauth.nooks.in, with 24 published scopes, RFC 8414 authorization-server
  metadata, and a JWKS endpoint. Nooks also operates an OAuth-protected remote MCP server at mcp.nooks.in, a signed `call.logged` webhook, an Atlassian Statuspage at status.nooks.in, and a SafeBase trust center with SOC 2 Type 2, SOC 3, ISO/IEC 27001:2022, GDPR, CCPA, and EU-US DPF coverage plus a Bugcrowd responsible-disclosure program. Nooks is backed by Kleiner Perkins and runs its application at app.nooks.in.
image: https://cdn.prod.website-files.com/697107c16c913fd77cf0aacd/69b2e1b1625a9e823d1edf5f_6995c9952aa828323555083c_OG%20Image%20(1).png
layout: provider
mcp_servers:
- description: ''
  name: nooks-mcp.yml
  slug: nooks-mcpyml
modified: '2026-08-14'
name: Nooks
nav: Providers
network: true
overview: 'Nooks publishes 1 API on the [APIs.io](https://apis.io/) network: Sequencing API. Tagged areas include Company, AI, Sales Engagement, Sales Dialer, and AI SDR.


  The Nooks catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nooks'' developer surface includes documentation, API reference, support, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Nooks Plans Pricing
  plan_count: 0
  slug: nooks-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 8
  name: Nooks Rate Limits
  slug: nooks-rate-limits
scopes:
- name: Nooks Scopes
  scope_count: 24
  slug: nooks-scopes
  summary_line: 24 scopes · authorizationCode
score:
  band: strong
  composite: 55.4
  delta: -1.6
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 16.7
    contract_quality: 76.1
    developer_ergonomics: 35.1
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 60.5
  previous_composite: 57.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nooks/refs/heads/main/screenshots/nooks-2026-08-07T185457.png
security:
- kind: authentication
  name: Nooks Authentication
  slug: nooks-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Nooks Domain Security
  slug: nooks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nooks Vulnerability Disclosure
  slug: nooks-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
- kind: trust-center
  name: Nooks Trust Center
  slug: nooks-trust-center
  summary_line: SOC 2 Type 2, SOC 3, ISO/IEC 27001:2022, GDPR, CCPA, EU-US DPF
slug: nooks
tags:
- Company
- AI
- Sales Engagement
- Sales Dialer
- AI SDR
- Outbound Sales
- Sales Coaching
- Revenue Operations
- Sales Sequencing
- CRM Integration
- Agents
- MCP
website: https://www.nooks.ai
---
