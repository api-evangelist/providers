---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 97
  human_in_the_loop: 7
  name: Anaconda Agentic Access
  operation_count: 223
  slug: anaconda-agentic-access
  summary_line: 223 operations · 97 acting · 7 human-in-the-loop
api_count: 7
apis:
- description: The repository API behind the Anaconda Platform and the on-premises Anaconda Server — channels, artifacts (conda, PyPI, CRAN), subchannels, mirrors, installers, CVE and vulnerability metadata, account
  name: Anaconda Server API
  slug: server-api
- description: Administrative API for Anaconda Platform organizations — create and delete service accounts, add and remove users, assign and revoke subscription seats, onboard users in bulk, and create, update, list
  name: Anaconda Organization Management API
  slug: org-management-api
- description: Read and export organization audit events from the Anaconda Platform. Supports listing audit logs with limit/offset/sort pagination, retrieving a single event, and creating asynchronous bulk export jo
  name: Anaconda Audit Logs API
  slug: audit-logs-api
- description: Local HTTP API exposed by Anaconda AI Navigator for managing curated local models, model files, inference servers, and an embedded vector database — list and download models, start and stop model serv
  name: Anaconda AI Navigator API
  slug: ai-navigator-api
- description: Local HTTP API exposed by Anaconda Desktop for model and inference-server management — list the model catalog, inspect and delete model files, track download status, and create, start, stop and delete
  name: Anaconda Desktop API
  slug: desktop-api
- description: The public REST API behind anaconda.org — the community package repository that serves conda and PyPI artifacts. Exposes user/organization profiles, packages, releases, files, labels and channels, and
  name: Anaconda.org Repository API
  slug: anaconda-org-api
- description: Anaconda's Model Context Protocol surface for AI coding agents. `anaconda-mcp` is a unified local gateway that composes conda-aware MCP servers, giving Claude Desktop, Claude Code, Cursor, VS Code, Op
  name: Anaconda MCP
  slug: mcp
artifact_total: 15
asyncapis:
- description: ''
  name: Anaconda Events
  slug: anaconda-events
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/anaconda-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/anaconda-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anaconda-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anaconda-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anaconda-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.anaconda.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://anaconda.com/docs/main
- group: docs
  title: ''
  type: Documentation
  url: https://anaconda.com/docs/main
- group: docs
  title: ''
  type: APIReference
  url: https://anaconda.com/docs/api-reference/get-api
- group: start
  title: ''
  type: GettingStarted
  url: https://anaconda.com/docs/getting-started/main
- group: operate
  title: ''
  type: Support
  url: https://www.anaconda.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.anaconda.cloud/
- group: company
  title: ''
  type: Blog
  url: https://www.anaconda.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anaconda
- group: commercial
  title: ''
  type: Pricing
  url: https://www.anaconda.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.anaconda.com/app/signup
- group: start
  title: ''
  type: Login
  url: https://auth.anaconda.com/ui/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anaconda.com/legal/terms/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.anaconda.com/policies/en/?name=privacy-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/anaconda_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anaconda-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anaconda-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/anaconda-security.txt
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/anaconda-openid-configuration.json
- group: build
  title: ''
  type: Packages
  url: packages/anaconda-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/anaconda-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/anaconda-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/anaconda-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/anaconda-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/anaconda-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anaconda-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/anaconda-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anaconda-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://anaconda.statuspage.io
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/anaconda-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://anaconda.com/docs/anaconda-org/release-notes
- group: design
  title: ''
  type: Conformance
  url: conformance/anaconda-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.anaconda.com/security-compliance
- group: auth
  title: ''
  type: Security
  url: https://app.intigriti.com/programs/anacondainc/anacondavdp/detail
- group: design
  title: ''
  type: DataModel
  url: data-model/anaconda-data-model.yml
- group: other
  title: ''
  type: StreamingEndpoint
  url: asyncapi/anaconda-events.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/anaconda-server-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/anaconda-org-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/anaconda-audit-logs-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/anaconda-ai-navigator-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/anaconda-desktop-overlay.yaml
created: '2026-08-02'
description: Anaconda, Inc. is the Austin, Texas company behind the Anaconda Distribution of Python and R, the conda package manager ecosystem, and the anaconda.org package repository — the default supply chain for open-source data science and AI packages. Its commercial Anaconda Platform (formerly Anaconda Cloud / Anaconda Server) adds a curated, security-scanned package repository with CVE metadata, private channels, mirroring, organization and seat management, audit logging, an on-premises repository server, Anaconda Desktop and AI Navigator for running local models and vector databases, and Agent Studio. Anaconda publishes machine-readable OpenAPI for the Anaconda Server repository API, the Organization Management API, the Audit Logs API, and the local Desktop and AI Navigator APIs, ships first-party Python client libraries and a plugin-based `anaconda` CLI, and operates conda-aware MCP servers for AI coding agents.
image: https://www.anaconda.com/wp-content/uploads/2024/07/anaconda-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: anaconda-mcp.yml
  slug: anaconda-mcpyml
modified: '2026-08-02'
name: Anaconda
nav: Providers
network: true
overview: 'Anaconda publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Server API, Organization Management API, Audit Logs API, and 2 more. Tagged areas include Company, Data Science, Machine Learning, Artificial Intelligence, and Package Management.


  The Anaconda catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Anaconda''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 40 more developer resources.'
random_paper: 30
scopes:
- name: Anaconda Scopes
  scope_count: 3
  slug: anaconda-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials/deviceCode/password/refreshToken
score:
  band: strong
  composite: 58.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 62.3
    developer_ergonomics: 75.5
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 58.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Anaconda Authentication
  slug: anaconda-authentication
  summary_line: http/apiKey/openIdConnect · 6 schemes
- kind: domain-security
  name: Anaconda Domain Security
  slug: anaconda-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Anaconda Vulnerability Disclosure
  slug: anaconda-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
- kind: trust-center
  name: Anaconda Trust Center
  slug: anaconda-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: anaconda
tags:
- Company
- Data Science
- Machine Learning
- Artificial Intelligence
- Package Management
- Python
- Developer Tools
- Software Supply Chain
- Repository
- Package Registry
- Conda
- MCP
website: https://www.anaconda.com/
---
