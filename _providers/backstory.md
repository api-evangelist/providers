---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
  schema_version: 0.2
  score: 28.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Backstory's hosted, remote Model Context Protocol server. It lets an AI client query a customer's own Backstory revenue-intelligence data — accounts, opportunities, recent activity, engaged people, sc
  name: Backstory MCP
  slug: backstory-mcp
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.backstory.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.backstory.ai/newsroom
- group: start
  title: ''
  type: Login
  url: https://app.people.ai/login/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.backstory.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.backstory.ai/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://www.backstory.ai/pricing
- group: operate
  title: ''
  type: Support
  url: mailto:support@backstory.ai
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.backstory.ai/en/
- group: docs
  title: ''
  type: Documentation
  url: https://help.backstory.ai/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.backstory.ai/en/collections/19646748-get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/people-ai
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.backstory.ai/platform/trust-security
- group: auth
  title: ''
  type: Compliance
  url: https://www.backstory.ai/platform/trust-security
- group: operate
  title: ''
  type: StatusPage
  url: https://status.backstory.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.backstory.ai/en/articles/15252920-new-product-releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/backstory-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/backstory-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/backstory-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/backstory-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/backstory-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/backstory-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/backstory-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/backstory-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/backstory-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/backstory-packages.yml
- group: design
  title: ''
  type: Components
  url: components/backstory-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/backstory-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/backstory-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/backstory-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/backstory-help-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/backstory-domain-security.yml
created: '2026-07-17'
description: 'Backstory (formerly People.ai, rebranded April 2026) is an AI revenue intelligence platform for sales leaders, CROs, and revenue teams. It automatically captures customer interactions across email, meetings, calls, chat, and CRM records, maps that activity to open deals, and reconstructs what is actually happening inside a deal or account — flagging which deals are losing momentum, where decision-makers are missing, whether a forecast is defensible, and the recommended next step. It integrates with Salesforce, Microsoft Dynamics, Oracle, Gmail, Outlook, Zoom, Teams, Webex, and Slack without requiring reps to change their workflow. Backstory''s public developer surface is agent-native rather than REST: it operates a hosted, remote MCP server at https://mcp.people.ai/mcp with thirteen documented tools, protected by OAuth 2.0 with PKCE and dynamic client registration, and documented for Claude, ChatGPT, Microsoft Copilot, Gemini CLI and n8n. A separate REST API exists but is documented
  only as admin-panel API key management, with no published reference or specification. Backstory is backed by ICONIQ Capital, Andreessen Horowitz, and Lightspeed Venture Partners.'
image: https://cdn.prod.website-files.com/69aab19e3344fee750b8721c/69bc218831a2d8ce7c69e9da_ab2eb85cd7fb357375e2a489f3bb519f_Backstory_OG.jpg
layout: provider
mcp_servers:
- description: Backstory MCP is the provider's hosted, remote Model Context Protocol server. It lets AI clients (Claude, ChatGPT, Microsoft Copilot, Google Gemini CLI, n8n AI Agent nodes, or any custom MCP client) q
  name: Backstory MCP
  slug: backstory-mcp
modified: '2026-08-14'
name: Backstory
nav: Providers
network: true
overview: 'Backstory publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Revenue Intelligence, Sales, and CRM.


  Backstory''s developer surface includes engineering blog, pricing, support, documentation, getting-started guide, changelog, authentication, and 25 more developer resources.'
plans:
- name: Backstory Plans Pricing
  plan_count: 0
  slug: backstory-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Backstory Rate Limits
  slug: backstory-rate-limits
scopes:
- name: Backstory Scopes
  scope_count: 1
  slug: backstory-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 33.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/backstory/refs/heads/main/screenshots/backstory-2026-07-25T202235.png
security:
- kind: authentication
  name: Backstory Authentication
  slug: backstory-authentication
  summary_line: oauth2/apiKey/http · 4 schemes
- kind: domain-security
  name: Backstory Domain Security
  slug: backstory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Backstory Trust Center
  slug: backstory-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, GDPR, CSA STAR
slug: backstory
tags:
- Company
- Artificial Intelligence
- Revenue Intelligence
- Sales
- CRM
- Sales Analytics
- Forecasting
- Revenue Operations
- MCP
- AI Agents
website: https://www.backstory.ai/
---
