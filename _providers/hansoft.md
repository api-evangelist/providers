---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-08-03'
api_count: 3
apis:
- description: GraphQL API service for P4 Plan (Hansoft) exposing 60+ queries, 100+ mutations, and 50+ subscriptions across projects, items (tasks, bugs, backlog), users and groups, sprints, timesheets, reports, das
  name: P4 Plan (Hansoft) GraphQL API
  slug: p4-plan-hansoft-graphql-api
- description: Native P4 Plan (Hansoft) SDK with C, C++, Java, and .NET wrappers auto-generated from C headers. Provides session management, resource and project operations, workflow configuration, custom columns/fi
  name: P4 Plan (Hansoft) SDK
  slug: p4-plan-hansoft-sdk
- description: Web service exposing a limited set of data and tasks over the DDP protocol via a WebSocket connection.
  name: P4 Plan (Hansoft) Web API
  slug: p4-plan-hansoft-web-api
artifact_total: 7
asyncapis:
- description: ''
  name: Hansoft Webhooks
  slug: hansoft-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hansoft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.perforce.com/products/hansoft
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.perforce.com/hansoft/
- group: docs
  title: ''
  type: Documentation
  url: https://help.perforce.com/hansoft/
- group: docs
  title: ''
  type: APIReference
  url: https://help.perforce.com/hansoft/current/Content/hansoftapi/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://help.perforce.com/p4-plan/current/Content/hansoftapi/installing-hansoft-api-service.htm
- group: operate
  title: ''
  type: Support
  url: https://www.perforce.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.perforce.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.perforce.com/products/hansoft/free-agile-planning-tool
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.perforce.com/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.perforce.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.perforce.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.perforce.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.perforce.com/company/security-compliance-policies
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.perforce.com/hansoft/current/Content/whats-new/2026_1.htm
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hansoft-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hansoft-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hansoft-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hansoft-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hansoft-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hansoft-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/hansoft-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hansoft-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hansoft-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hansoft-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hansoft-lifecycle.yml
created: '2026-07-17'
description: Hansoft, now branded P4 Plan by Perforce, is a real-time agile project planning and portfolio management tool for software, game, and hardware teams. It lets multiple teams work in their preferred methodology simultaneously (Scrum, Kanban, and Gantt) within a single backlog, with field-level permissions, capacity and resource planning, sprint and burndown reporting, and tight integration with Perforce version control (P4 changelists). For developers it exposes a GraphQL API service (queries, mutations, and subscriptions), a native SDK with C, C++, Java, and .NET wrappers, a WebSocket Web API, and outbound webhooks for integrations such as Jira. Hansoft is deployed on-premises for security-conscious organizations, so its API and SDK run against a customer-hosted P4 Plan server.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hansoft.png
layout: provider
modified: '2026-07-19'
name: Hansoft
nav: Providers
network: true
overview: 'Hansoft publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Project Management, Agile, Planning, and Software Development.


  The Hansoft catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hansoft''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 20 more developer resources.'
random_paper: 90
score:
  band: developing
  composite: 48.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 60.3
    discoverability: 83.3
    governance: 3.1
    operational_transparency: 39.5
  previous_composite: 48.8
  provenance:
    conformance: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hansoft/refs/heads/main/screenshots/hansoft-2026-07-25T220633.png
security:
- kind: authentication
  name: Hansoft Authentication
  slug: hansoft-authentication
  summary_line: session · 2 schemes
- kind: domain-security
  name: Hansoft Domain Security
  slug: hansoft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Hansoft Trust Center
  slug: hansoft-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, ISO 42001
slug: hansoft
tags:
- Company
- Project Management
- Agile
- Planning
- Software Development
- GraphQL
- SDK
- Webhooks
- DevOps
website: https://www.perforce.com/products/hansoft
---
