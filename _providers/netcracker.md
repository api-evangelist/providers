---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 137
  human_in_the_loop: 36
  name: Netcracker Agentic Access
  operation_count: 276
  slug: netcracker-agentic-access
  summary_line: 276 operations · 137 acting · 36 human-in-the-loop
api_count: 4
apis:
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: APIs for technical administration.
  name: Netcracker Admin API
  slug: netcracker-admin-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: The Aggregated Database Administration No Namespace Controller V 3 API from Netcracker — 3 operation(s) for aggregated database administration no namespace controller v 3.
  name: Netcracker Aggregated Database Administration No Namespace Controller V 3 API
  slug: netcracker-aggregated-database-administration-no-namespace-controller-v-3-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: APIs for AI chat assistant. Each user has their own chat list; chats are persisted on the server with a configurable TTL and pinning support. Conversations support streaming responses (SSE) and automa
  name: Netcracker AI Chat API
  slug: netcracker-ai-chat-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: Providing API version info
  name: Netcracker API version controller API
  slug: netcracker-api-version-controller-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: APIs for auth integrations.
  name: Netcracker Auth API
  slug: netcracker-auth-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: Backup & Restore operations for DBaaS
  name: Netcracker Backup & Restore API
  slug: netcracker-backup-restore-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: Allows to get list of available backups, trigger backup collector and restore some specific backup. All backup management is per namespace.
  name: Netcracker Backups administration API
  slug: netcracker-backups-administration-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: Allows to configure a logic of balancing logical databases over physical.
  name: Netcracker Balancing Rules Administration V3 API
  slug: netcracker-balancing-rules-administration-v3-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: The Blue Green Controller V 1 API from Netcracker — 12 operation(s) for blue green controller v 1.
  name: Netcracker Blue Green Controller V 1 API
  slug: netcracker-blue-green-controller-v-1-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: Changes APIs.
  name: Netcracker Changes API
  slug: netcracker-changes-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: The Composite Controller API from Netcracker — 3 operation(s) for composite controller.
  name: Netcracker Composite Controller API
  slug: netcracker-composite-controller-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: The Config Controller V 1 API from Netcracker — 4 operation(s) for config controller v 1.
  name: Netcracker Config Controller V 1 API
  slug: netcracker-config-controller-v-1-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: DDL and MCP contract APIs.
  name: Netcracker Contracts API
  slug: netcracker-contracts-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: Allows to create, access and drop databases. This API uses classifier as a key to create and retrieve databases. Classifier is an abstract key that could be any JSON object mapping to (String -> Objec
  name: Netcracker Controller Database administration API
  slug: netcracker-controller-database-administration-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: The Controller for debug operations API from Netcracker — 5 operation(s) for controller for debug operations.
  name: Netcracker Controller for debug operations API
  slug: netcracker-controller-for-debug-operations-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: Custom APIs.
  name: Netcracker Custom API
  slug: netcracker-custom-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: This controller contains API for operations with already created databases, users.
  name: Netcracker Database operation controller v3 API
  slug: netcracker-database-operation-controller-v3-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: This controller contains API for operations with database users.
  name: Netcracker Database users controller v3 API
  slug: netcracker-database-users-controller-v3-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: The Declarative Controller API from Netcracker — 2 operation(s) for declarative controller.
  name: Netcracker Declarative Controller API
  slug: netcracker-declarative-controller-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: Documents APIs.
  name: Netcracker Documents API
  slug: netcracker-documents-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: APIs for short-lived file downloads. Files are stored temporarily on the server and accessed via signed tokens embedded in producer responses (e.g. AI chat assistant markdown links).
  name: Netcracker Ephemeral Files API
  slug: netcracker-ephemeral-files-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: Export API documentation.
  name: Netcracker Export API
  slug: netcracker-export-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: This controller provides APIs for performing operations on existing databases and users without requiring a specific namespace in the endpoints.
  name: Netcracker Global Database Operation Controller v3 API
  slug: netcracker-global-database-operation-controller-v3-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: APIs for internal documents management.
  name: Netcracker Internal Documents API
  slug: netcracker-internal-documents-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: This controller contains APIs based on microservice value.
  name: Netcracker Microservice controller v3 API
  slug: netcracker-microservice-controller-v3-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: 'Provides API to migrate: database registration from another source, database passwords to external system.'
  name: Netcracker Migration controller API
  slug: netcracker-migration-controller-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: Operation groups
  name: Netcracker Operation groups API
  slug: netcracker-operation-groups-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: Operations APIs.
  name: Netcracker Operations API
  slug: netcracker-operations-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: APIs for the package management.
  name: Netcracker Packages API
  slug: netcracker-packages-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: Provides API to register new physical databases
  name: Netcracker Physical databases registration controller API
  slug: netcracker-physical-databases-registration-controller-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: Publish version API
  name: Netcracker Publish API
  slug: netcracker-publish-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: APIs for role management.
  name: Netcracker Roles API
  slug: netcracker-roles-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: Search functions.
  name: Netcracker Search API
  slug: netcracker-search-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: Operations to move packages
  name: Netcracker Transition API
  slug: netcracker-transition-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: API for 'try it' functionality
  name: Netcracker Try It API
  slug: netcracker-tryit-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: APIs for user's personal settings.
  name: Netcracker User profile API
  slug: netcracker-user-profile-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: APIs for the user operations.
  name: Netcracker Users API
  slug: netcracker-users-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: The V1 API from Netcracker — 22 operation(s) for v1.
  name: Netcracker V1 API
  slug: netcracker-v1-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: The V2 API from Netcracker — 13 operation(s) for v2.
  name: Netcracker V2 API
  slug: netcracker-v2-api
- baseURL: https://{apihub}.qubership.org
  baseurl_source: declared
  description: Published package versions API.
  name: Netcracker Versions API
  slug: netcracker-versions-api
artifact_total: 50
collections:
- collection_type: open
  name: APIHUB system administrators API – External
  slug: open-netcracker-qubership-apihub-admin
- collection_type: open
  name: APIHUB Registry – External API
  slug: open-netcracker-qubership-apihub-registry
- collection_type: open
  name: DBaaS Aggregator API
  slug: open-netcracker-qubership-dbaas
- collection_type: open
  name: Maas Service API
  slug: open-netcracker-qubership-maas-swagger
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/netcracker-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/netcracker-qubership-apihub-registry-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/netcracker-qubership-apihub-admin-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/netcracker-qubership-maas-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/netcracker-qubership-dbaas-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Netcracker/qubership-apihub-backend/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Netcracker/qubership-apihub-backend/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Netcracker/qubership-apihub-backend/blob/develop/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Netcracker/qubership-apihub-backend/blob/develop/CODE-OF-CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Netcracker/qubership-apihub-backend/blob/develop/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Netcracker/qubership-apihub-backend/blob/develop/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/netcracker-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netcracker-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/netcracker-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/netcracker-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/netcracker-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/netcracker-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/netcracker-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/netcracker-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/netcracker-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/netcracker-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/netcracker-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/netcracker-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/netcracker-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/netcracker-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://netcracker.github.io/apihub/releases/
- group: design
  title: ''
  type: Conformance
  url: conformance/netcracker-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.netcracker.com/portfolio/services/netcracker-cybersecurity
- group: auth
  title: ''
  type: TrustCenter
  url: security/netcracker-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/netcracker-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/Netcracker/qubership-apihub/blob/main/SECURITY.md
- group: build
  title: ''
  type: CLI
  url: cli/netcracker-cli.yml
- group: design
  title: ''
  type: Components
  url: components/netcracker-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/netcracker-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/netcracker-sandbox.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/netcracker-qubership-control-plane-bus.proto
- group: company
  title: ''
  type: Website
  url: https://www.netcracker.com/
- group: docs
  title: ''
  type: Documentation
  url: https://netcracker.github.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://netcracker.github.io/apihub/deploy/
- group: operate
  title: ''
  type: Support
  url: https://github.com/Netcracker/qubership-apihub/issues
- group: build
  title: ''
  type: Postman
  url: https://github.com/Netcracker/qubership-apihub-postman-collections
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.netcracker.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.netcracker.com/privacy-notice
- group: operate
  title: ''
  type: ContactUs
  url: https://www.netcracker.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Netcracker
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netcracker-technology
- group: company
  title: ''
  type: Blog
  url: https://www.netcracker.com/blog
- group: operate
  title: ''
  type: PressReleases
  url: https://www.netcracker.com/news/press-releases
- group: other
  title: ''
  type: ProductPage
  url: https://www.netcracker.com/portfolio/products/netcracker-api-management-integration
- group: other
  title: ''
  type: Portfolio
  url: https://www.netcracker.com/portfolio
created: '2026-07-25'
description: 'Netcracker Technology is a Waltham, Massachusetts-based BSS/OSS and digital business software vendor and a wholly owned subsidiary of NEC Corporation. It sells cloud BSS, digital commerce and monetization, convergent charging, service and network orchestration, and API management and integration software to communications service providers worldwide — it is a supplier to carriers rather than a carrier itself, sitting one layer behind the operator in the telecom value chain and never touching a public developer directly. Netcracker is a long-standing TM Forum participant, claims the TM Forum Platinum Badge for Open API and "Ready for ODA" certification for its BSS/OSS portfolio, and contributed conformance toolkits to the TM Forum Open API program. Its API posture toward the outside world is honestly partner-gated: netcracker.com publishes no developer portal (developer., developers., docs., api. subdomains do not resolve; /developer, /developers and /api all return 404), no
  product OpenAPI is downloadable, and every commercial API — the TM Forum Open APIs its products implement — reaches integrators only through a customer or partner engagement. The one genuinely public, self-serve API surface Netcracker publishes is Qubership, its open-source cloud platform at github.com/Netcracker and netcracker.github.io, which ships real, downloadable OpenAPI contracts for its APIHUB API registry, integration, messaging and database services. On CAMARA, Netcracker names the standard in product marketing alongside TM Forum, MEF, ETSI, 3GPP and O-RAN and says CSPs can monetize "plug and play developer APIs, such as those from CAMARA" — but no CAMARA API is implemented, specified or callable anywhere in its public surface. That is a positioning statement, not an implementation.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Netcracker MCP Server
  slug: netcracker-mcp-server
modified: '2026-07-25'
name: Netcracker
nav: Providers
network: true
overview: 'Netcracker publishes 40 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Aggregated Database Administration No Namespace Controller V 3 API, AI Chat API, and 37 more. Tagged areas include Telecommunications, United States, BSS, OSS, and Network Vendor.


  Netcracker''s developer surface includes authentication, changelog, CLI, sandbox, documentation, getting-started guide, support, and 44 more developer resources.'
random_paper: 8
score:
  band: strong
  composite: 58.9
  coverage:
    artifact_dirs: 24
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 57.2
    developer_ergonomics: 75.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 100.0
  previous_composite: 58.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 52.5
      derived: 0
      marker_coverage: 0.0
      total: 40
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 58.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netcracker/refs/heads/main/screenshots/netcracker-2026-08-07T184931.png
security:
- kind: authentication
  name: Netcracker Authentication
  slug: netcracker-authentication
  summary_line: apiKey/http · 6 schemes
- kind: domain-security
  name: Netcracker Domain Security
  slug: netcracker-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Netcracker Vulnerability Disclosure
  slug: netcracker-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Netcracker Trust Center
  slug: netcracker-trust-center
  summary_line: PCI DSS, ISO 27001, ISO 27018, ISO 22301, SOC reporting
slug: netcracker
tags:
- Telecommunications
- United States
- BSS
- OSS
- Network Vendor
- API Management
- TM Forum
- OpenAPI
- CAMARA
- Standards
- Orchestration
- Monetization
- Open-Source
website: https://www.netcracker.com/
---
