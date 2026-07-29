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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 49
  human_in_the_loop: 2
  name: Elementum Agentic Access
  operation_count: 72
  slug: elementum-agentic-access
  summary_line: 72 operations · 49 acting · 2 human-in-the-loop
api_count: 18
apis:
- description: Manage access tokens using OAuth 2.0 standards
  name: Elementum Access Token API
  slug: elementum-access-token-api
- description: Manage AI agents
  name: Elementum Agents API
  slug: elementum-agents-api
- description: Compose and manage apps
  name: Elementum Apps API
  slug: elementum-apps-api
- description: Manage the attachments of a record
  name: Elementum Attachments API
  slug: elementum-attachments-api
- description: Manage automations
  name: Elementum Automations API
  slug: elementum-automations-api
- description: Manage the conversation of a record
  name: Elementum Comments API
  slug: elementum-comments-api
- description: Manage organization domains
  name: Elementum Domains API
  slug: elementum-domains-api
- description: Manage elements imported from connected cloud sources
  name: Elementum Elements API
  slug: elementum-elements-api
- description: Manage flows
  name: Elementum Flows API
  slug: elementum-flows-api
- description: Manage groups and group membership
  name: Elementum Groups API
  slug: elementum-groups-api
- description: Manage your records
  name: Elementum Records API
  slug: elementum-records-api
- description: Manage the related items of a record
  name: Elementum Related-items API
  slug: elementum-related-items-api
- description: Manage search tables (snowflake and linked)
  name: Elementum Search Tables API
  slug: elementum-search-tables-api
- description: Manage agent skills
  name: Elementum Skills API
  slug: elementum-skills-api
- description: 'Manage tables: schemas, fields, joins, and join mappings'
  name: Elementum Tables API
  slug: elementum-tables-api
- description: Manage users in your organization
  name: Elementum Users API
  slug: elementum-users-api
- description: Manage app views
  name: Elementum Views API
  slug: elementum-views-api
- description: Manage the watchers of a record
  name: Elementum Watchers API
  slug: elementum-watchers-api
artifact_total: 22
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.elementum.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.elementum.io/getting-started/welcome-to-elementum
- group: docs
  title: ''
  type: APIReference
  url: https://docs.elementum.io/api-reference/api-introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.elementum.io/getting-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.elementum.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.elementum.io/support/resources
- group: start
  title: ''
  type: SignUp
  url: https://app.elementum.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elementum.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elementum.ai/privacy
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.elementum.io/release-notes/upcoming-features
- group: operate
  title: ''
  type: StatusPage
  url: https://status.elementum.io/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/elementum-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elementum-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elementum-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/elementum-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/elementum-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/elementum-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/elementum-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/elementum-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elementum-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/elementum-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elementum-domain-security.yml
created: '2026-07-17'
description: Elementum is an AI-native process automation and orchestration platform that lets enterprises build custom business workflows that coordinate people, rules, LLMs, and AI agents without moving data out of the customer's own data warehouse (its "Zero Persistence" / CloudLink model, with first-class Snowflake integration). Originally a multi-enterprise supply chain orchestration vendor, Elementum pivoted to general enterprise AI orchestration spanning supply chain, finance, healthcare, and compliance. It exposes a versioned REST API (v1, US and EU regions) secured with OAuth 2.0 client-credentials for records, apps, elements, tasks, attachments, comments, watchers, related items, agents, automations, flows, skills, tables, views, groups, and users, plus a public documentation MCP server, SAML SSO/SCIM provisioning, and service accounts for agents and automations. Elementum is backed by Lightspeed Venture Partners, Snowflake Ventures, and others.
image: https://www.elementum.ai/opengraph-image-12jlf3?57ba9092a8cf43dd
layout: provider
mcp_servers:
- description: ''
  name: elementum-mcp.yml
  slug: elementum-mcpyml
modified: '2026-07-19'
name: Elementum
nav: Providers
network: true
overview: 'Elementum publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Access Token API, Agents API, Apps API, and 15 more. Tagged areas include Company, AI, Automation, Workflow, and Orchestration.


  Elementum''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 16 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 45.5
  delta: -2.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 47.3
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elementum/refs/heads/main/screenshots/elementum-2026-07-25T213131.png
security:
- kind: authentication
  name: Elementum Authentication
  slug: elementum-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Elementum Domain Security
  slug: elementum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elementum
tags:
- Company
- AI
- Automation
- Workflow
- Orchestration
- Agents
- Supply Chain
- No-Code
- Enterprise
- Snowflake
website: https://docs.elementum.io/
---
