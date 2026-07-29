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
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Hex Agentic Access
  operation_count: 52
  slug: hex-agentic-access
  summary_line: 52 operations · 29 acting
api_count: 11
apis:
- description: The Cells API from Hex — 4 operation(s) for cells.
  name: Hex Cells API
  slug: hex-cells-api
- description: The Collections API from Hex — 2 operation(s) for collections.
  name: Hex Collections API
  slug: hex-collections-api
- description: The Context API from Hex — 1 operation(s) for context.
  name: Hex Context API
  slug: hex-context-api
- description: The Data Connections API from Hex — 3 operation(s) for data connections.
  name: Hex Data Connections API
  slug: hex-data-connections-api
- description: The Embedding API from Hex — 1 operation(s) for embedding.
  name: Hex Embedding API
  slug: hex-embedding-api
- description: The Groups API from Hex — 2 operation(s) for groups.
  name: Hex Groups API
  slug: hex-groups-api
- description: The Guides API from Hex — 4 operation(s) for guides.
  name: Hex Guides API
  slug: hex-guides-api
- description: The Projects API from Hex — 11 operation(s) for projects.
  name: Hex Projects API
  slug: hex-projects-api
- description: The Semantic (projects|models) API from Hex — 2 operation(s) for semantic (projects|models).
  name: Hex Semantic (projects|models) API
  slug: hex-semantic-projects-models-api
- description: The Threads API from Hex — 4 operation(s) for threads.
  name: Hex Threads API
  slug: hex-threads-api
- description: The Users API from Hex — 3 operation(s) for users.
  name: Hex Users API
  slug: hex-users-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hex-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.hex.tech/docs
- group: docs
  title: ''
  type: Documentation
  url: https://learn.hex.tech/docs
- group: docs
  title: ''
  type: APIReference
  url: https://learn.hex.tech/docs/api-integrations/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.hex.tech/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://hex.tech/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://hex.tech/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.hex.tech/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://learn.hex.tech/docs/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://learn.hex.tech/docs/trust/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hex-inc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hex.tech/
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.hex.tech/changelog
- group: build
  title: ''
  type: Packages
  url: packages/hex-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hex-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/hex-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hex-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hex-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hex-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/hex-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hex-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hex-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hex-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hex-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/hex-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/hex-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/hex-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hex-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hex-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hex-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hex-problem-types.yml
created: '2026-07-17'
description: Hex is an AI-powered analytics platform that combines agentic notebooks, interactive data apps, and conversational self-serve analytics so teams can go from ad-hoc exploration to published, governed data apps. The Hex External API (bearer-token authenticated, base https://app.hex.tech/api/v1) lets you programmatically run and schedule projects, manage projects, collections, groups, cells, and data connections, ingest semantic models, drive AI agent Threads (create, continue, read messages), export projects, and administer workspace users. Hex also ships a first-party CLI, a hosted remote MCP server, Airflow and Dagster integrations, and published Claude Agent Skills. Surfaced as an a16z portfolio company and enriched with its real public developer surface.
image: https://cdn.sanity.io/images/e92memrj/production/57eeccd836f0d6188862a55186ab48521fe1034b-1200x630.png
layout: provider
mcp_servers:
- description: ''
  name: hex-mcp.yml
  slug: hex-mcpyml
modified: '2026-07-19'
name: Hex
nav: Providers
network: true
overview: 'Hex publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Cells API, Collections API, Context API, and 8 more. Tagged areas include Company, Analytics, Data Science, Notebooks, and Business Intelligence.


  Hex''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 25 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 55.8
  delta: -0.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 50.5
    developer_ergonomics: 71.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 56.0
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hex/refs/heads/main/screenshots/hex-2026-07-25T221110.png
security:
- kind: authentication
  name: Hex Authentication
  slug: hex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hex Domain Security
  slug: hex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hex Vulnerability Disclosure
  slug: hex-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Hex Trust Center
  slug: hex-trust-center
  summary_line: SOC 2 Type II, HIPAA, PCI, GDPR, CCPA, EU-US Data Privacy Framework, Swiss-US Data Privacy Framework, UK-US Data Privacy Framework
slug: hex
tags:
- Company
- Analytics
- Data Science
- Notebooks
- Business Intelligence
- Data Apps
- AI
- Agents
- Semantic Layer
- Developer Tools
website: https://learn.hex.tech/docs
---
