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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'REST + gRPC API for querying features from the Chalk Context Engine — online single-row queries, bulk (feather/Arrow) queries, and asynchronous offline dataset generation — plus deployment of feature '
  name: Chalk API
  slug: chalk-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://chalk.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.chalk.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chalk.ai/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chalk.ai/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.chalk.ai/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://chalk.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chalk-ai
- group: start
  title: ''
  type: Login
  url: https://chalk.ai/login
- group: start
  title: ''
  type: SignUp
  url: https://chalk.ai/book-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chalk.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chalk.ai/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://chalk.statuspage.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.chalk.ai/docs/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/chalk-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chalk-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/chalk-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/chalk-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/chalk-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/chalk-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/chalk-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chalk-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/chalk-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chalk-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chalk-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/chalk-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chalk-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.chalk.ai/docs/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chalk-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chalk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.chalk.ai/docs/security
created: '2026-07-17'
description: 'Chalk is a real-time AI/ML data platform ("Context Engine") that lets teams define features, embeddings, LLM outputs, and prompts once in Python and serve them everywhere — training, real-time inference, and agents — computed on infrastructure the customer controls. Instead of stitching together a feature store, vector database, retrieval and prompt tooling, orchestration, and a sandbox runtime, Chalk unifies them: features are point-in-time correct, served in single-digit milliseconds, and deployed via a branch-based model inside the customer''s own cloud. It exposes a REST API and gRPC client libraries (Python, TypeScript, Go, Java, C#), a first-party CLI, OAuth 2.0 authentication, and MCP-scoped agent access. Backed by Felicis and General Catalyst.'
image: https://chalk.ai/opengraph.png
layout: provider
mcp_servers:
- description: ''
  name: Chalk MCP Server
  slug: chalk-mcp-server
modified: '2026-07-18'
name: Chalk
nav: Providers
network: true
overview: 'Chalk publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Machine-Learning, Feature Store, Artificial Intelligence, and Data Platform.


  Chalk''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, changelog, authentication, and 23 more developer resources.'
random_paper: 11
scopes:
- name: Chalk Scopes
  scope_count: 3
  slug: chalk-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 73.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 38.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chalk/refs/heads/main/screenshots/chalk-2026-07-25T205026.png
security:
- kind: authentication
  name: Chalk Authentication
  slug: chalk-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Chalk Domain Security
  slug: chalk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chalk Vulnerability Disclosure
  slug: chalk-vulnerability-disclosure
  summary_line: contact published
slug: chalk
tags:
- Company
- Machine-Learning
- Feature Store
- Artificial Intelligence
- Data Platform
- MLOps
- Real-Time Data
- LLM
- Agents
- Feature Engineering
website: https://chalk.ai
---
