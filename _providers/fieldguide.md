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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Fieldguide Agentic Access
  operation_count: 56
  slug: fieldguide-agentic-access
  summary_line: 56 operations · 19 acting
api_count: 15
apis:
- description: Endpoints used to interact with the Fieldguide API platform
  name: Fieldguide api API
  slug: fieldguide-api-api
- description: Endpoints used to interact with Fieldguide Comments
  name: Fieldguide comments API
  slug: fieldguide-comments-api
- description: Endpoints used to interact with Fieldguide Companies
  name: Fieldguide companies API
  slug: fieldguide-companies-api
- description: Endpoints used to interact with Fieldguide Controls
  name: Fieldguide controls API
  slug: fieldguide-controls-api
- description: Endpoints used to interact with Fieldguide Engagements
  name: Fieldguide engagements API
  slug: fieldguide-engagements-api
- description: Endpoints used to interact with Fieldguide Files
  name: Fieldguide files API
  slug: fieldguide-files-api
- description: Endpoints used to interact with Fieldguide Insights
  name: Fieldguide insights API
  slug: fieldguide-insights-api
- description: Endpoints used to interact with long-running processes (Jobs) in the Fieldguide API
  name: Fieldguide jobs API
  slug: fieldguide-jobs-api
- description: Endpoints used to interact with Fieldguide Milestones
  name: Fieldguide milestones API
  slug: fieldguide-milestones-api
- description: Endpoints used to interact with Fieldguide Requests
  name: Fieldguide requests API
  slug: fieldguide-requests-api
- description: Endpoints used to interact with Fieldguide Sheet Columns
  name: Fieldguide sheet-columns API
  slug: fieldguide-sheet-columns-api
- description: Endpoints used to interact with Fieldguide Sheet Rows
  name: Fieldguide sheet-rows API
  slug: fieldguide-sheet-rows-api
- description: Endpoints used to interact with Fieldguide Sheets
  name: Fieldguide sheets API
  slug: fieldguide-sheets-api
- description: Endpoints used to interact with Fieldguide Users
  name: Fieldguide users API
  slug: fieldguide-users-api
- description: Endpoints used to interact with Fieldguide Webhooks
  name: Fieldguide webhooks API
  slug: fieldguide-webhooks-api
artifact_total: 22
asyncapis:
- description: ''
  name: Fieldguide Webhooks
  slug: fieldguide-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/fieldguide-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fieldguide-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fieldguide-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fieldguide-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.fieldguide.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.fieldguide.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://fieldguide.notion.site/Fieldguide-API-Documentation-650f03765dc0402c96ccb750ecd70eda
- group: docs
  title: ''
  type: APIReference
  url: https://api.fieldguide.io/api
- group: company
  title: ''
  type: Blog
  url: https://www.fieldguide.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.fieldguide.io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fieldguide.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fieldguide.io/demo
- group: start
  title: ''
  type: SignUp
  url: https://app.fieldguide.io
- group: start
  title: ''
  type: Login
  url: https://app.fieldguide.io
- group: operate
  title: ''
  type: Support
  url: mailto:support@fieldguide.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fieldguide.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fieldguide.io/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.fieldguide.io/trust
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fieldguide-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fieldguide-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fieldguide-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fieldguide-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fieldguide-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fieldguide-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/fieldguide-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/fieldguide-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fieldguide-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fieldguide-data-model.yml
created: '2026-07-17'
description: Fieldguide is an AI-native platform for audit and advisory firms, providing professional-grade "Field Agents" that plan, execute, and document engagement work end-to-end across financial audit, SOC audits, IT audit, risk advisory, tax, cybersecurity, and regulatory compliance engagements. The platform pairs engagement management, document management, insights and analytics, and a client hub with an open REST API (api.fieldguide.io) that exposes companies, engagements, requests, sheets, files, comments, milestones, users, insights, and webhook subscriptions. Fieldguide is used by half of the top 100 firms, is SOC 2 Type 2 and ISO/IEC 42001 certified, and is backed by 8VC and Bessemer Venture Partners.
image: https://app.fieldguide.io/img/logo192.png
layout: provider
mcp_servers:
- description: ''
  name: fieldguide-mcp.yml
  slug: fieldguide-mcpyml
modified: '2026-07-19'
name: Fieldguide
nav: Providers
network: true
overview: 'Fieldguide publishes 15 APIs on the [APIs.io](https://apis.io/) network, including api API, comments API, companies API, and 12 more. Tagged areas include Company, Audit, Advisory, Accounting, and Compliance.


  The Fieldguide catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fieldguide''s developer surface includes authentication, documentation, API reference, engineering blog, changelog, pricing, signup flow, and 22 more developer resources.'
random_paper: 25
scopes:
- name: Fieldguide Scopes
  scope_count: 21
  slug: fieldguide-scopes
  summary_line: 21 scopes
score:
  band: developing
  composite: 52.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 66.8
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fieldguide/refs/heads/main/screenshots/fieldguide-2026-07-25T214434.png
security:
- kind: authentication
  name: Fieldguide Authentication
  slug: fieldguide-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fieldguide Domain Security
  slug: fieldguide-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fieldguide Trust Center
  slug: fieldguide-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA
slug: fieldguide
tags:
- Company
- Audit
- Advisory
- Accounting
- Compliance
- Risk
- Engagement Management
- Artificial Intelligence
- Agents
- Webhooks
website: https://www.fieldguide.io
---
