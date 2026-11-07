---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 95
  human_in_the_loop: 6
  name: Anaconda Agentic Access
  operation_count: 235
  slug: anaconda-agentic-access
  summary_line: 235 operations · 95 acting · 6 human-in-the-loop
api_count: 5
apis:
- description: The public REST API behind anaconda.org — the community package repository that serves conda and PyPI artifacts. Exposes user/organization profiles, packages, releases, files, labels and channels, and
  name: Anaconda.org Repository API
  slug: anaconda-org-api
- description: Anaconda's Model Context Protocol surface for AI coding agents. `anaconda-mcp` is a unified local gateway that composes conda-aware MCP servers, giving Claude Desktop, Claude Code, Cursor, VS Code, Op
  name: Anaconda MCP
  slug: mcp
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: User account actions
  name: Anaconda Account API
  slug: anaconda-account-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: The AI Navigator API API from Anaconda — 1 operation(s) for ai navigator api.
  name: Anaconda AI Navigator API
  slug: anaconda-ai-navigator-api-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: Artifact endpoints - search, retrieve, mirror
  name: Anaconda Artifacts API
  slug: anaconda-artifacts-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: The Audit Logs API from Anaconda — 5 operation(s) for audit logs.
  name: Anaconda Audit Logs API
  slug: anaconda-audit-logs-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: Authentication endpoints
  name: Anaconda Auth API
  slug: anaconda-auth-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: Channel management endpoints
  name: Anaconda Channels API
  slug: anaconda-channels-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: The diagnosis API from Anaconda — 1 operation(s) for diagnosis.
  name: Anaconda Diagnosis API
  slug: anaconda-diagnosis-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: The docs API from Anaconda — 1 operation(s) for docs.
  name: Anaconda Docs API
  slug: anaconda-docs-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: The Files API from Anaconda — 2 operation(s) for files.
  name: Anaconda Files API
  slug: anaconda-files-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: Group management endpoints
  name: Anaconda Groups API
  slug: anaconda-groups-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: The installers API from Anaconda — 2 operation(s) for installers.
  name: Anaconda Installers API
  slug: anaconda-installers-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: The mirrors API from Anaconda — 1 operation(s) for mirrors.
  name: Anaconda Mirrors API
  slug: anaconda-mirrors-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: The Models API from Anaconda — 5 operation(s) for models.
  name: Anaconda Models API
  slug: anaconda-models-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: The organizations API from Anaconda — 9 operation(s) for organizations.
  name: Anaconda Organizations API
  slug: anaconda-organizations-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: The Repo API from Anaconda — 2 operation(s) for repo.
  name: Anaconda Repo API
  slug: anaconda-repo-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: The reports API from Anaconda — 1 operation(s) for reports.
  name: Anaconda Reports API
  slug: anaconda-reports-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: The Servers API from Anaconda — 3 operation(s) for servers.
  name: Anaconda Servers API
  slug: anaconda-servers-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: System endpoints - version, health, etc.
  name: Anaconda System API
  slug: anaconda-system-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: User role management endpoints (CRUD is managed separately)
  name: Anaconda Users API
  slug: anaconda-users-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: The VectorDB API from Anaconda — 4 operation(s) for vectordb.
  name: Anaconda Vector DB API
  slug: anaconda-vectordb-api
- baseURL: https://api.anaconda.cloud/api
  baseurl_source: declared
  description: The websocket API from Anaconda — 3 operation(s) for websocket.
  name: Anaconda Websocket API
  slug: anaconda-websocket-api
- baseURL: https://api.anaconda.org
  baseurl_source: declared
  description: The cves API from Anaconda — 20 operation(s) for cves.
  name: Anaconda Cves API
  slug: anaconda-cves-api
artifact_total: 63
asyncapis:
- description: ''
  name: Anaconda Events
  slug: anaconda-events
collections:
- collection_type: open
  name: Anaconda Server Account API
  slug: open-anaconda-account-api
- collection_type: open
  name: AI Navigator AI Navigator API API
  slug: open-anaconda-ai-navigator-api-api
- collection_type: open
  name: Anaconda Server Artifacts API
  slug: open-anaconda-artifacts-api
- collection_type: open
  name: Audit Logs API
  slug: open-anaconda-audit-logs-api
- collection_type: open
  name: Anaconda Server Auth API
  slug: open-anaconda-auth-api
- collection_type: open
  name: Anaconda Server Channels API
  slug: open-anaconda-channels-api
- collection_type: open
  name: Anaconda Server Cves API
  slug: open-anaconda-cves-api
- collection_type: open
  name: Anaconda Server Diagnosis API
  slug: open-anaconda-diagnosis-api
- collection_type: open
  name: Anaconda Server Docs API
  slug: open-anaconda-docs-api
- collection_type: open
  name: Anaconda Files API
  slug: open-anaconda-files-api
- collection_type: open
  name: Anaconda Server Groups API
  slug: open-anaconda-groups-api
- collection_type: open
  name: Anaconda Server Installers API
  slug: open-anaconda-installers-api
- collection_type: open
  name: Anaconda Server Mirrors API
  slug: open-anaconda-mirrors-api
- collection_type: open
  name: Anaconda Models API
  slug: open-anaconda-models-api
- collection_type: open
  name: Organization Management Organizations API
  slug: open-anaconda-organizations-api
- collection_type: open
  name: Anaconda Server Repo API
  slug: open-anaconda-repo-api
- collection_type: open
  name: Anaconda Server Reports API
  slug: open-anaconda-reports-api
- collection_type: open
  name: Anaconda Servers API
  slug: open-anaconda-servers-api
- collection_type: open
  name: Anaconda Server System API
  slug: open-anaconda-system-api
- collection_type: open
  name: Anaconda Server Users API
  slug: open-anaconda-users-api
- collection_type: open
  name: AI Navigator Vector DB API
  slug: open-anaconda-vectordb-api
- collection_type: open
  name: Anaconda Server Websocket API
  slug: open-anaconda-websocket-api
common:
- group: commercial
  href: https://artifacts.apis.io/anaconda/plans/anaconda-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anaconda-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/anaconda/capabilities/anaconda-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/anaconda-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/anaconda/agentic-access/anaconda-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anaconda-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/anaconda/security/anaconda-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/anaconda-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/anaconda/security/anaconda-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/anaconda-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/anaconda/security/anaconda-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anaconda-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/anaconda/authentication/anaconda-authentication.yml
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
  href: https://artifacts.apis.io/anaconda/llms/anaconda-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anaconda-llms.txt
- group: agent
  href: https://artifacts.apis.io/anaconda/well-known/anaconda-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anaconda-well-known.yml
- group: auth
  href: https://artifacts.apis.io/anaconda/well-known/anaconda-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anaconda-security.txt
- group: other
  href: https://artifacts.apis.io/anaconda/well-known/anaconda-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/anaconda-openid-configuration.json
- group: build
  href: https://artifacts.apis.io/anaconda/packages/anaconda-packages.yml
  title: ''
  type: Packages
  url: packages/anaconda-packages.yml
- group: build
  href: https://artifacts.apis.io/anaconda/packages/anaconda-packages.yml
  title: ''
  type: SDKs
  url: packages/anaconda-packages.yml
- group: build
  href: https://artifacts.apis.io/anaconda/cli/anaconda-cli.yml
  title: ''
  type: CLI
  url: cli/anaconda-cli.yml
- group: agent
  href: https://artifacts.apis.io/anaconda/mcp/anaconda-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anaconda-mcp.yml
- group: build
  href: https://artifacts.apis.io/anaconda/mcp/anaconda-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/anaconda-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/anaconda/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/anaconda/scopes/anaconda-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/anaconda-scopes.yml
- group: design
  href: https://artifacts.apis.io/anaconda/conventions/anaconda-conventions.yml
  title: ''
  type: Conventions
  url: conventions/anaconda-conventions.yml
- group: design
  href: https://artifacts.apis.io/anaconda/errors/anaconda-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anaconda-problem-types.yml
- group: design
  href: https://artifacts.apis.io/anaconda/lifecycle/anaconda-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/anaconda-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://anaconda.statuspage.io
- group: operate
  href: https://artifacts.apis.io/anaconda/changelog/anaconda-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/anaconda-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://anaconda.com/docs/anaconda-org/release-notes
- group: design
  href: https://artifacts.apis.io/anaconda/conformance/anaconda-conformance.yml
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
  href: https://artifacts.apis.io/anaconda/data-model/anaconda-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anaconda-data-model.yml
- group: other
  href: https://artifacts.apis.io/anaconda/asyncapi/anaconda-events.yml
  title: ''
  type: StreamingEndpoint
  url: asyncapi/anaconda-events.yml
- group: other
  href: https://artifacts.apis.io/anaconda/overlays/anaconda-server-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anaconda-server-overlay.yaml
- group: other
  href: https://artifacts.apis.io/anaconda/overlays/anaconda-org-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anaconda-org-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/anaconda/overlays/anaconda-audit-logs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anaconda-audit-logs-overlay.yaml
- group: other
  href: https://artifacts.apis.io/anaconda/overlays/anaconda-ai-navigator-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anaconda-ai-navigator-overlay.yaml
- group: other
  href: https://artifacts.apis.io/anaconda/overlays/anaconda-desktop-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anaconda-desktop-overlay.yaml
created: '2026-08-02'
description: Anaconda, Inc. is the Austin, Texas company behind the Anaconda Distribution of Python and R, the conda package manager ecosystem, and the anaconda.org package repository — the default supply chain for open-source data science and AI packages. Its commercial Anaconda Platform (formerly Anaconda Cloud / Anaconda Server) adds a curated, security-scanned package repository with CVE metadata, private channels, mirroring, organization and seat management, audit logging, an on-premises repository server, Anaconda Desktop and AI Navigator for running local models and vector databases, and Agent Studio. Anaconda publishes machine-readable OpenAPI for the Anaconda Server repository API, the Organization Management API, the Audit Logs API, and the local Desktop and AI Navigator APIs, ships first-party Python client libraries and a plugin-based `anaconda` CLI, and operates conda-aware MCP servers for AI coding agents.
finops:
- has_sources: true
  method: derived
  name: Anaconda Finops
  primary_unit: user
  service_category: ''
  slug: anaconda-finops
  template: false
image: https://www.anaconda.com/wp-content/uploads/2024/07/anaconda-logo.svg
layout: provider
mcp_servers:
- description: Remote MCP server at anaconda.com.
  name: Anaconda MCP Server
  slug: anaconda-mcp-yml
modified: '2026-09-16'
name: Anaconda
nav: Providers
network: true
overview: 'Anaconda publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, AI Navigator API, Artifacts API, and 21 more. Tagged areas include Company, Data Science, Machine Learning, Artificial Intelligence, and Package Management.


  The Anaconda catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Anaconda''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 42 more developer resources.'
plans:
- name: Anaconda Plans Pricing
  plan_count: 17
  slug: anaconda-plans-pricing
- name: Anaconda Price Estimates
  plan_count: 0
  slug: anaconda-price-estimates
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Anaconda API Rules
  rule_count: 47
  severity_counts:
    error: 29
    hint: 0
    info: 5
    warn: 13
  slug: anaconda-rules
scopes:
- name: Anaconda Scopes
  scope_count: 3
  slug: anaconda-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials/deviceCode/password/refreshToken
score:
  band: strong
  composite: 64.3
  coverage:
    artifact_dirs: 33
    catalog_earned: 54.5
    catalog_earned_first_party: 12.0
    catalog_gap: 60.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 61.0
    developer_ergonomics: 73.2
    discoverability: 71.7
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 63.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 77.3
      derived: 0
      marker_coverage: 68.2
      total: 22
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/anaconda/anaconda-2026-08-07T161352.png
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
skill_count: 5
skills:
- name: Audit an Anaconda channel for CVEs
  slug: anaconda-audit-channel-cves
- name: Export Anaconda audit logs
  slug: anaconda-export-audit-logs
- name: Create a channel and manage its artifacts
  slug: anaconda-manage-channels-and-artifacts
- name: Onboard users into an Anaconda organization
  slug: anaconda-onboard-org-users
- name: Run a local model and vector database with Anaconda AI
  slug: anaconda-run-local-models
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
