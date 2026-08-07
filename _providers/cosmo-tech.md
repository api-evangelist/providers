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
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 56
  human_in_the_loop: 16
  name: Cosmo Tech Agentic Access
  operation_count: 101
  slug: cosmo-tech-agentic-access
  summary_line: 101 operations · 56 acting · 16 human-in-the-loop
api_count: 7
apis:
- description: Dataset Management
  name: Cosmo Tech dataset API
  slug: cosmo-tech-dataset-api
- description: Meta Management
  name: Cosmo Tech meta API
  slug: cosmo-tech-meta-api
- description: Organization Management
  name: Cosmo Tech organization API
  slug: cosmo-tech-organization-api
- description: Run Management
  name: Cosmo Tech run API
  slug: cosmo-tech-run-api
- description: Runner Management
  name: Cosmo Tech runner API
  slug: cosmo-tech-runner-api
- description: Solution Management
  name: Cosmo Tech solution API
  slug: cosmo-tech-solution-api
- description: Workspace Management
  name: Cosmo Tech workspace API
  slug: cosmo-tech-workspace-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://cosmotech.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.cosmotech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Cosmo-Tech/cosmotech-api
- group: docs
  title: ''
  type: APIReference
  url: https://dev.api.cosmotech.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cosmo-Tech
- group: start
  title: ''
  type: Login
  url: https://portal.cosmotech.com/
- group: operate
  title: ''
  type: Support
  url: https://cosmotech.com/solutions/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cosmotech.com/legal-information/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cosmotech.com/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cosmotech.com/
- group: build
  title: ''
  type: Packages
  url: packages/cosmo-tech-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cosmo-tech-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cosmo-tech-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cosmo-tech-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cosmo-tech-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/cosmo-tech-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cosmo-tech-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cosmo-tech-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cosmo-tech-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cosmo-tech-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cosmo-tech-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cosmo-tech-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cosmo-tech-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cosmo-tech-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cosmo-tech-domain-security.yml
created: '2026-07-17'
description: Cosmo Tech is a predictive and prescriptive AI-simulation (digital twin) platform for industry, based in Lyon, France and backed by Insight Partners. Its open-source Cosmo Tech Cloud Platform API (Kotlin, MIT) lets teams model organizations, workspaces, solutions, datasets, runners and runs, then configure and execute large-scale what-if simulations across supply chains, asset investment planning and enterprise operations. The API is modular across seven service specs (organization, workspace, solution, dataset, runner, run, meta), authenticates via OAuth2 / OpenID Connect (Keycloak), and ships auto-generated TypeScript and Python clients plus the Babylon CLI.
image: https://avatars.githubusercontent.com/u/9283409?v=4
layout: provider
mcp_servers:
- description: ''
  name: cosmo-tech-mcp.yml
  slug: cosmo-tech-mcpyml
modified: '2026-07-18'
name: Cosmo Tech
nav: Providers
network: true
overview: 'Cosmo Tech publishes 7 APIs on the [APIs.io](https://apis.io/) network, including dataset API, meta API, organization API, and 4 more. Tagged areas include Company, Simulation, Digital Twin, Artificial Intelligence, and Supply Chain.


  Cosmo Tech''s developer surface includes documentation, API reference, support, CLI, authentication, changelog, and 20 more developer resources.'
random_paper: 106
scopes:
- name: Cosmo Tech Scopes
  scope_count: 0
  slug: cosmo-tech-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.3
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 49.5
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 44.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cosmo-tech/refs/heads/main/screenshots/cosmo-tech-2026-07-25T210455.png
security:
- kind: authentication
  name: Cosmo Tech Authentication
  slug: cosmo-tech-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cosmo Tech Domain Security
  slug: cosmo-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cosmo-tech
tags:
- Company
- Simulation
- Digital Twin
- Artificial Intelligence
- Supply Chain
- Predictive Analytics
- Industrial
website: https://cosmotech.com/
---
