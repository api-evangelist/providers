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
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 72.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Aptly Agentic Access
  operation_count: 51
  slug: aptly-agentic-access
  summary_line: 51 operations · 24 acting
api_count: 15
apis:
- description: The App API from Aptly — 2 operation(s) for app.
  name: Aptly App API
  slug: aptly-app-api
- description: The Board API from Aptly — 12 operation(s) for board.
  name: Aptly Board API
  slug: aptly-board-api
- description: The Boards API from Aptly — 1 operation(s) for boards.
  name: Aptly Boards API
  slug: aptly-boards-api
- description: The Cards API from Aptly — 6 operation(s) for cards.
  name: Aptly Cards API
  slug: aptly-cards-api
- description: The Company API from Aptly — 1 operation(s) for company.
  name: Aptly Company API
  slug: aptly-company-api
- description: The Contacts API from Aptly — 5 operation(s) for contacts.
  name: Aptly Contacts API
  slug: aptly-contacts-api
- description: The Email API from Aptly — 2 operation(s) for email.
  name: Aptly Email API
  slug: aptly-email-api
- description: The Files API from Aptly — 2 operation(s) for files.
  name: Aptly Files API
  slug: aptly-files-api
- description: The Inboxes API from Aptly — 1 operation(s) for inboxes.
  name: Aptly Inboxes API
  slug: aptly-inboxes-api
- description: The Knowledge API from Aptly — 2 operation(s) for knowledge.
  name: Aptly Knowledge API
  slug: aptly-knowledge-api
- description: The RoutingGroups API from Aptly — 4 operation(s) for routinggroups.
  name: Aptly RoutingGroups API
  slug: aptly-routinggroups-api
- description: The Schema API from Aptly — 1 operation(s) for schema.
  name: Aptly Schema API
  slug: aptly-schema-api
- description: The Tasks API from Aptly — 3 operation(s) for tasks.
  name: Aptly Tasks API
  slug: aptly-tasks-api
- description: The Templates API from Aptly — 2 operation(s) for templates.
  name: Aptly Templates API
  slug: aptly-templates-api
- description: The Users API from Aptly — 2 operation(s) for users.
  name: Aptly Users API
  slug: aptly-users-api
artifact_total: 19
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getaptly.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getaptly.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getaptly.com/api-reference/users/list-users
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getaptly.com/authentication
- group: company
  title: ''
  type: Blog
  url: https://www.getaptly.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getaptly.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.getaptly.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getaptly.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getaptly.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getaptly
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/aptly-openapi-original.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aptly-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aptly-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/aptly-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aptly-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aptly-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: conventions/aptly-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aptly-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aptly-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/aptly-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aptly-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aptly-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/aptly-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aptly-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/aptly-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aptly-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.getaptly.com
created: '2026-07-17'
description: Aptly is the AI operations layer for property management, built by Invisible Apps, Inc. It unifies resident and owner communication (calls, texts, emails, and chat) with board-based workflows, automation, and AI agents that handle leasing inquiries, maintenance requests, and around-the-clock resident communication, and it syncs bidirectionally with property management systems including Yardi, RealPage, Entrata, and AppFolio. The Aptly Core API (https://core-api.getaptly.com) gives external systems and AI agents direct read/write access to boards, cards, contacts, tasks, inboxes, calendars, files, and knowledge documents using a per-company API key, and Aptly ships an official hosted MCP server (https://mcp.getaptly.com/mcp) as the recommended way to connect LLMs. A separate Portal API powers the rental-application screening portal.
image: https://www.getaptly.com/images/aptly-logo-light.png
layout: provider
mcp_servers:
- description: ''
  name: aptly-mcp.yml
  slug: aptly-mcpyml
modified: '2026-07-18'
name: Aptly
nav: Providers
network: true
overview: 'Aptly publishes 15 APIs on the [APIs.io](https://apis.io/) network, including App API, Board API, Boards API, and 12 more. Tagged areas include Company, Cloud Saas, Property Management, Real Estate, and PropTech.


  Aptly''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 21 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 49.7
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 57.5
    developer_ergonomics: 63.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 49.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aptly/refs/heads/main/screenshots/aptly-2026-07-25T200942.png
security:
- kind: authentication
  name: Aptly Authentication
  slug: aptly-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Aptly Domain Security
  slug: aptly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aptly
tags:
- Company
- Cloud Saas
- Property Management
- Real Estate
- PropTech
- CRM
- Workflow Automation
- AI Agents
- Communications
- MCP
website: https://www.getaptly.com
---
