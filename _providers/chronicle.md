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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 29.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Workspace-scoped REST API to list templates, create presentations from templates, generate presentations from a prompt (asynchronous, poll-to-complete), upload reference files to ground generation, fe
  name: Chronicle API
  slug: chronicle-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/chronicle-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chronicle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chroniclehq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.chroniclehq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chroniclehq.com/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chroniclehq.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.chroniclehq.com/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://chroniclehq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.chroniclehq.com/start
- group: start
  title: ''
  type: Login
  url: https://app.chroniclehq.com
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/chroniclehqfaq/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.chroniclehq.com/get-help
- group: company
  title: ''
  type: Blog
  url: https://chroniclehq.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chroniclehq.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chroniclehq.com/privacy-policy-2
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chroniclehq
- group: auth
  title: ''
  type: Compliance
  url: https://security.chroniclehq.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/chronicle-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chronicle-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/chronicle-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/chronicle-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/chronicle-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/chronicle-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chronicle-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chronicle-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chronicle-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/chronicle-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chronicle-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/chronicle-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chronicle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/chronicle-security.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Chronicle is an AI presentation platform (chroniclehq.com) that turns documents, notes, data, and business context into beautiful, fully editable, on-brand presentations, using templates from designers at Apple, McKinsey, BCG, and IDEO. Beyond the web app, Chronicle ships a developer surface: a workspace-scoped REST API at api.chroniclehq.com/api/v1 for listing templates, creating and generating presentations, uploading reference files, and polling asynchronous generation jobs; and a hosted, OAuth-secured MCP server at mcp.chroniclehq.com that lets AI agents (Claude, ChatGPT, Gemini) create presentations directly. Chronicle is used by teams including OpenAI, Ramp, Vercel, Notion, Figma, and Meta, and is backed by Accel.'
image: https://cms.chroniclehq.com/wp-content/uploads/2026/02/og.jpg
layout: provider
mcp_servers:
- description: ''
  name: Chronicle MCP Server
  slug: chronicle-mcp-server
modified: '2026-07-18'
name: Chronicle
nav: Providers
network: true
overview: 'Chronicle publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud Saas, Presentations, Artificial Intelligence, and Productivity.


  Chronicle''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 25 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 1
  name: Chronicle Rate Limits
  slug: chronicle-rate-limits
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 38.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chronicle/refs/heads/main/screenshots/chronicle-2026-07-25T205309.png
security:
- kind: authentication
  name: Chronicle Authentication
  slug: chronicle-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Chronicle Domain Security
  slug: chronicle-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Chronicle Vulnerability Disclosure
  slug: chronicle-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Chronicle Trust Center
  slug: chronicle-trust-center
  summary_line: SOC 2, ISO 27001
slug: chronicle
tags:
- Company
- Cloud Saas
- Presentations
- Artificial Intelligence
- Productivity
- Content Generation
- Agents
- MCP
- Developer API
website: https://chroniclehq.com/
---
