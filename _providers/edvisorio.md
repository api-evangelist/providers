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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Single GraphQL API for the Edvisor.io education-recruitment platform, covering students, quotes, school offerings, enrollments, invoices, and agency/school company management. Bearer API-key authentic
  name: Edvisor.io GraphQL API
  slug: edvisorio-graphql-api
artifact_total: 5
asyncapis:
- description: ''
  name: Edvisorio Webhooks
  slug: edvisorio-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edvisorio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://edvisor.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.edvisor.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.edvisor.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.edvisor.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.edvisor.io/
- group: docs
  title: ''
  type: GraphQL
  url: graphql/edvisorio-api-v2-graphql.graphql
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/edvisorio-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/edvisorio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/edvisorio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/edvisorio-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/edvisorio-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/edvisorio-packages.yml
- group: design
  title: ''
  type: Components
  url: components/edvisorio-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/edvisorio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/edvisorio-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/edvisorio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/edvisorio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://edvisor.io/privacy
- group: start
  title: ''
  type: Sandbox
  url: sandbox/edvisorio-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edvisor-io
- group: company
  title: ''
  type: Blog
  url: https://blog.edvisor.io
- group: commercial
  title: ''
  type: Pricing
  url: https://edvisor.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://edvisor.io/pricing#agencies
- group: start
  title: ''
  type: Login
  url: https://app.edvisor.io
- group: operate
  title: ''
  type: Support
  url: mailto:support@edvisor.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://edvisor.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://edvisor.io/privacy
created: '2026-07-17'
description: Edvisor.io is a B2B international-education recruitment platform that connects education agencies with 700+ partner schools across 80+ countries. Agencies browse school portfolios with live pricing, build and send student quotes, manage the student journey from inquiry through enrollment, and track commissions and invoices; schools distribute programs to 5,000+ active agencies, grow and manage their agency network, and analyze their enrollment pipeline. The platform has processed over $2B in tuition. Edvisor exposes a GraphQL API at api-v2.edvisor.io/graphql (226 queries, 203 mutations, Bearer API-key auth) plus webhooks for two-way synchronization with external CRM and back-office systems.
image: https://www.edvisor.io/images/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: edvisorio-mcp.yml
  slug: edvisorio-mcpyml
modified: '2026-07-19'
name: Edvisor.io
nav: Providers
network: true
overview: 'Edvisor.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Student Recruitment, International Education, and EdTech.


  The Edvisor.io catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Edvisor.io''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, engineering blog, pricing, and 22 more developer resources.'
random_paper: 32
score:
  band: developing
  composite: 48.3
  delta: 6.4
  facets:
    commercial_clarity: 52.6
    contract_quality: 58.0
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 13.2
  previous_composite: 41.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/edvisorio/refs/heads/main/screenshots/edvisorio-2026-07-25T212910.png
security:
- kind: authentication
  name: Edvisorio Authentication
  slug: edvisorio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Edvisorio Domain Security
  slug: edvisorio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: edvisorio
tags:
- Company
- Education
- Student Recruitment
- International Education
- EdTech
- GraphQL
- Marketplace
- Webhooks
website: https://edvisor.io/
---
