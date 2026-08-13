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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 66.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Monaco Agentic Access
  operation_count: 37
  slug: monaco-agentic-access
  summary_line: 37 operations · 24 acting
api_count: 11
apis:
- description: The Accounts API from Monaco — 3 operation(s) for accounts.
  name: Monaco Accounts API
  slug: monaco-accounts-api
- description: The Auth API from Monaco — 1 operation(s) for auth.
  name: Monaco Auth API
  slug: monaco-auth-api
- description: The Contacts API from Monaco — 3 operation(s) for contacts.
  name: Monaco Contacts API
  slug: monaco-contacts-api
- description: The Meetings API from Monaco — 2 operation(s) for meetings.
  name: Monaco Meetings API
  slug: monaco-meetings-api
- description: The Opportunities API from Monaco — 3 operation(s) for opportunities.
  name: Monaco Opportunities API
  slug: monaco-opportunities-api
- description: The Schemas API from Monaco — 1 operation(s) for schemas.
  name: Monaco Schemas API
  slug: monaco-schemas-api
- description: The Sequence Templates API from Monaco — 2 operation(s) for sequence templates.
  name: Monaco Sequence Templates API
  slug: monaco-sequence-templates-api
- description: The Sequences API from Monaco — 2 operation(s) for sequences.
  name: Monaco Sequences API
  slug: monaco-sequences-api
- description: The Tags API from Monaco — 2 operation(s) for tags.
  name: Monaco Tags API
  slug: monaco-tags-api
- description: The Tasks API from Monaco — 3 operation(s) for tasks.
  name: Monaco Tasks API
  slug: monaco-tasks-api
- description: The Users API from Monaco — 1 operation(s) for users.
  name: Monaco Users API
  slug: monaco-users-api
artifact_total: 17
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/monaco-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.monaco.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.monaco.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.monaco.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.monaco.com/auth
- group: company
  title: ''
  type: Website
  url: https://www.monaco.com
- group: company
  title: ''
  type: Blog
  url: https://www.monaco.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.monaco.com/login
- group: start
  title: ''
  type: Login
  url: https://app.monaco.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.monaco.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.monaco.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.monaco.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.monaco.com
- group: auth
  title: ''
  type: Security
  url: https://www.monaco.com/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/monaco-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monaco-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/monaco-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/monaco-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/monaco-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/monaco-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/monaco-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/monaco-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/monaco-agentic-access.yml
created: '2026-07-17'
description: Monaco is an AI-native revenue platform for startups that replaces legacy CRM systems and disparate sales point solutions with a single revenue engine. It unifies a contacts/accounts database, buying signals, sequences, pipeline and opportunity tracking, meeting/call recording with AI summaries, and CRO copilot coaching. Monaco exposes a public REST API (api.monaco.com) covering contacts, accounts, opportunities, tasks, tags, meetings, sequences, and sequence templates, plus a hosted, OAuth-secured MCP server (mcp.monaco.com) and shipped Agent Skills so AI agents can query and act on revenue data in natural language. Founded by Sam Blond and backed by Founders Fund; the API and MCP surface are currently in Beta.
image: https://www.monaco.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: monaco-mcp.yml
  slug: monaco-mcpyml
modified: '2026-07-20'
name: Monaco
nav: Providers
network: true
overview: 'Monaco publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Auth API, Contacts API, and 8 more. Tagged areas include Company, CRM, Sales, Revenue Operations, and Artificial Intelligence.


  Monaco''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, and 18 more developer resources.'
random_paper: 37
rate_limits:
- limit_count: 0
  name: Monaco Rate Limits
  slug: monaco-rate-limits
score:
  band: developing
  composite: 48.4
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 57.1
    developer_ergonomics: 58.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monaco/refs/heads/main/screenshots/monaco-2026-08-07T184130.png
security:
- kind: authentication
  name: Monaco Authentication
  slug: monaco-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Monaco Domain Security
  slug: monaco-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Monaco Vulnerability Disclosure
  slug: monaco-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: monaco
tags:
- Company
- CRM
- Sales
- Revenue Operations
- Artificial Intelligence
- Contacts
- Accounts
- Opportunities
- Pipeline
- Go To Market
- MCP
website: https://www.monaco.com
---
