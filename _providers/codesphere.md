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
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 50
  human_in_the_loop: 1
  name: Codesphere Agentic Access
  operation_count: 80
  slug: codesphere-agentic-access
  summary_line: 80 operations · 50 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: The clusters API from Codesphere — 2 operation(s) for clusters.
  name: Codesphere clusters API
  slug: codesphere-clusters-api
- description: The domains API from Codesphere — 4 operation(s) for domains.
  name: Codesphere domains API
  slug: codesphere-domains-api
- description: The managed-services API from Codesphere — 5 operation(s) for managed-services.
  name: Codesphere managed-services API
  slug: codesphere-managed-services-api
- description: The metadata API from Codesphere — 3 operation(s) for metadata.
  name: Codesphere metadata API
  slug: codesphere-metadata-api
- description: The organizations API from Codesphere — 5 operation(s) for organizations.
  name: Codesphere organizations API
  slug: codesphere-organizations-api
- description: The ssh API from Codesphere — 1 operation(s) for ssh.
  name: Codesphere ssh API
  slug: codesphere-ssh-api
- description: The teams API from Codesphere — 6 operation(s) for teams.
  name: Codesphere teams API
  slug: codesphere-teams-api
- description: The usage API from Codesphere — 2 operation(s) for usage.
  name: Codesphere usage API
  slug: codesphere-usage-api
- description: The vault API from Codesphere — 8 operation(s) for vault.
  name: Codesphere vault API
  slug: codesphere-vault-api
- description: The workspaces API from Codesphere — 21 operation(s) for workspaces.
  name: Codesphere workspaces API
  slug: codesphere-workspaces-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Create a workspace, run the prepare and run pipeline stages, and confirm it is live.
  name: Deploy an application to a Codesphere workspace
  slug: codesphere-deploy-workspace
- description: Discover providers, create a managed service, and confirm it is running.
  name: Provision a Codesphere managed service
  slug: codesphere-provision-managed-service
artifact_total: 19
common:
- group: company
  title: ''
  type: Website
  url: https://codesphere.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.codesphere.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.codesphere.com
- group: docs
  title: ''
  type: APIReference
  url: https://cloud.codesphere.com/api/swagger-ui
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.codesphere.com/getting-started
- group: operate
  title: ''
  type: Support
  url: mailto:support@codesphere.com
- group: company
  title: ''
  type: Blog
  url: https://codesphere.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codesphere-cloud
- group: operate
  title: ''
  type: StatusPage
  url: https://status.codesphere.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codesphere.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.codesphere.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://cloud.codesphere.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.codesphere.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/codesphere-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/codesphere-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/codesphere-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codesphere-domain-security.yml
- group: build
  title: ''
  type: CLI
  url: cli/codesphere-cli.yml
- group: build
  title: ''
  type: SDKs
  url: packages/codesphere-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/codesphere-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/codesphere-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/codesphere-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/codesphere-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/codesphere-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/codesphere-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/codesphere-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/codesphere-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/codesphere-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/codesphere-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/codesphere-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/codesphere-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/codesphere-llms.txt
- group: design
  title: ''
  type: Arazzo
  url: arazzo/codesphere-deploy-workspace.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/codesphere-provision-managed-service.yml
created: '2026-07-17'
description: Codesphere is a European-built sovereign cloud platform that lets organizations deploy and operate applications across on-premises, hybrid, and public-cloud infrastructure from a single control layer, without Kubernetes expertise or vendor lock-in. Its Public API manages workspaces, CI/deploy pipelines, landscapes, managed services (PostgreSQL, Valkey, OpenSearch, RabbitMQ, DocumentDB, object storage, virtual Kubernetes clusters), custom domains, teams, organizations, secret vaults, SSH keys, and usage. A first-party `cs` CLI, a Go managed-services SDK, a GitHub deploy Action, and a VS Code extension wrap the same REST contract. Codesphere is ISO 27001 certified and SOC 1 & 2 attested. Surfaced as a portfolio company of Creandum and enriched from its own public developer surface.
image: https://avatars.githubusercontent.com/u/66959440?v=4
layout: provider
mcp_servers:
- description: ''
  name: codesphere-mcp.yml
  slug: codesphere-mcpyml
modified: '2026-07-18'
name: Codesphere
nav: Providers
network: true
overview: 'Codesphere publishes 10 APIs on the [APIs.io](https://apis.io/) network, including clusters API, domains API, managed-services API, and 7 more. Tagged areas include Company, Saas, Cloud, Deployment, and Developer Tools.


  Codesphere''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, CLI, and 28 more developer resources.'
random_paper: 74
score:
  band: developing
  composite: 53.8
  delta: -1.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 52.9
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 55.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codesphere/refs/heads/main/screenshots/codesphere-2026-07-25T205930.png
security:
- kind: authentication
  name: Codesphere Authentication
  slug: codesphere-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Codesphere Domain Security
  slug: codesphere-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Codesphere Vulnerability Disclosure
  slug: codesphere-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Codesphere Trust Center
  slug: codesphere-trust-center
  summary_line: SOC 2, ISO 27001
slug: codesphere
tags:
- Company
- Saas
- Cloud
- Deployment
- Developer Tools
- Platform as a Service
- Infrastructure
- Sovereign Cloud
- CI/CD
- Managed Services
website: https://codesphere.com/
---
