---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 93
  human_in_the_loop: 3
  name: Teradata Agentic Access
  operation_count: 170
  slug: teradata-agentic-access
  summary_line: 170 operations · 93 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: The API Info API from Teradata — 1 operation(s) for api info.
  name: Teradata API Info API
  slug: teradata-api-info-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: The Configuration API from Teradata — 8 operation(s) for configuration.
  name: Teradata Configuration API
  slug: teradata-configuration-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: The Issues API from Teradata — 1 operation(s) for issues.
  name: Teradata Issues API
  slug: teradata-issues-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: The Managers API from Teradata — 1 operation(s) for managers.
  name: Teradata Managers API
  slug: teradata-managers-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: The Nodes API from Teradata — 1 operation(s) for nodes.
  name: Teradata Nodes API
  slug: teradata-nodes-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: The Operations API from Teradata — 3 operation(s) for operations.
  name: Teradata Operations API
  slug: teradata-operations-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: The Queries API from Teradata — 2 operation(s) for queries.
  name: Teradata Queries API
  slug: teradata-queries-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: The Sessions API from Teradata — 2 operation(s) for sessions.
  name: Teradata Sessions API
  slug: teradata-sessions-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: The Software API from Teradata — 1 operation(s) for software.
  name: Teradata Software API
  slug: teradata-software-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: The Systems API from Teradata — 1 operation(s) for systems.
  name: Teradata Systems API
  slug: teradata-systems-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: The Users API from Teradata — 1 operation(s) for users.
  name: Teradata Users API
  slug: teradata-users-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Manage bridges used for routing QueryGrid communication between systems without direct connectivity
  name: Teradata Config - Bridges API
  slug: teradata-config-bridges-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Manage communication policies that define how data is transferred between systems
  name: Teradata Config - Communication Policies API
  slug: teradata-config-communication-policies-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Manage connectors that connect data sources to the QueryGrid Fabric
  name: Teradata Config - Connectors API
  slug: teradata-config-connectors-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Manage data centers (a.k.a regions) where QueryGrid software is deployed
  name: Teradata Config - Data Centers API
  slug: teradata-config-data-centers-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Manage fabrics responsible for QueryGrid inter-node communication
  name: Teradata Config - Fabrics API
  slug: teradata-config-fabrics-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Manage links that enable connectivity between connectors
  name: Teradata Config - Links API
  slug: teradata-config-links-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Manage network rules that determine the network interfaces to use for communications
  name: Teradata Config - Networks API
  slug: teradata-config-networks-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Manage virtual IPs associated with nodes
  name: Teradata Config - Node Virtual IPs API
  slug: teradata-config-node-virtual-ips-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Manage the systems or platforms associated with QueryGrid connectors
  name: Teradata Config - Systems API
  slug: teradata-config-systems-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Map initiator user and roles to target user and roles
  name: Teradata Config - User/Role Mappings API
  slug: teradata-config-user-role-mappings-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Register a new data source to QueryGrid Manager
  name: Teradata Operations - Add Data Source API
  slug: teradata-operations-add-data-source-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Bulk delete nodes or issues
  name: Teradata Operations - Bulk Delete API
  slug: teradata-operations-bulk-delete-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Create a foreign server for a given link
  name: Teradata Operations - Create Foreign Server API
  slug: teradata-operations-create-foreign-server-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Generate node registration zip file for a given datasource
  name: Teradata Operations - Data Source Registration File API
  slug: teradata-operations-data-source-registration-file-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Start and monitor diagnostic check and connector install operations
  name: Teradata Operations - Diagnostic Checks / Connector Install API
  slug: teradata-operations-diagnostic-checks-connector-install-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Disable system alerts for a specific system and issue type
  name: Teradata Operations - Disable System Alerts API
  slug: teradata-operations-disable-system-alerts-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Import a system from a different QueryGrid Manager cluster
  name: Teradata Operations - Import System API
  slug: teradata-operations-import-system-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Automate install and registration of nodes with QueryGrid Manager
  name: Teradata Operations - Nodes Auto Install API
  slug: teradata-operations-nodes-auto-install-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Download config file needed for manual install and registration of nodes with QueryGrid Manager
  name: Teradata Operations - Nodes Manual Install API
  slug: teradata-operations-nodes-manual-install-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Generate private link template file for a given cloud platform
  name: Teradata Operations - Private Link Template API
  slug: teradata-operations-private-link-template-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Register current system nodes to remote lake system
  name: Teradata Operations - Register Remote Lake System API
  slug: teradata-operations-register-remote-lake-system-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Estimate memory needed for QueryGrid operations
  name: Teradata Operations - Shared Memory Estimator API
  slug: teradata-operations-shared-memory-estimator-api
- baseURL: https://querygrid.teradata.com/api/v1
  baseurl_source: declared
  description: Generate support archive for a Manager, System, Node, Query, or Bandwidth Tests issues
  name: Teradata Support Archive API
  slug: teradata-support-archive-api
arazzos:
- description: Pick a software version, trigger an automated node install, then verify the nodes.
  name: Teradata Auto-Install Node Software
  slug: teradata-auto-install-node-software-workflow
- description: Create a data fabric, attach a network, and apply a communication policy.
  name: Teradata Build a Data Fabric
  slug: teradata-build-data-fabric-workflow
- description: Submit a query, check whether it is still running, and cancel it if so.
  name: Teradata Cancel a Running Query
  slug: teradata-cancel-running-query-workflow
- description: Import a system from a remote QueryGrid manager, confirm it landed, and diagnose its connectivity.
  name: Teradata Import and Verify a Remote System
  slug: teradata-import-and-verify-system-workflow
- description: Submit a SQL query, poll its status until it completes, then branch on success or failure.
  name: Teradata Submit Query and Poll for Results
  slug: teradata-poll-query-results-workflow
- description: Register a system, create a connector for it, then link it into a fabric.
  name: Teradata Provision a Cross-System Link
  slug: teradata-provision-cross-system-link-workflow
- description: Create a data center, register a system inside it, then bridge it to an existing system.
  name: Teradata Register a System in a New Data Center
  slug: teradata-register-system-in-datacenter-workflow
- description: Confirm the manager API is running, list open issues, and branch to inspect managers when issues exist.
  name: Teradata Review QueryGrid Environment Health
  slug: teradata-review-environment-health-workflow
- description: List configured systems, run a connectivity diagnostic, then branch on the result.
  name: Teradata Run a Connectivity Diagnostic
  slug: teradata-run-connectivity-diagnostic-workflow
- description: Pick an available Vantage system, open a session, run a SQL query, and close the session.
  name: Teradata Run Query in a Session
  slug: teradata-run-query-session-workflow
- description: Create a query session, verify it is active, then close it.
  name: Teradata Session Lifecycle
  slug: teradata-session-lifecycle-workflow
artifact_total: 130
collections:
- collection_type: postman
  name: Teradata Query Service API
  slug: postman-teradata-query-service-api
- collection_type: postman
  name: Teradata QueryGrid Manager API
  slug: postman-teradata-querygrid-manager-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Teradata Query Service API Info API
  slug: open-teradata-api-info-api
- collection_type: open
  name: Teradata Query Service API Info Configuration API
  slug: open-teradata-configuration-api
- collection_type: open
  name: Teradata Query Service API Info Issues API
  slug: open-teradata-issues-api
- collection_type: open
  name: Teradata Query Service API Info Managers API
  slug: open-teradata-managers-api
- collection_type: open
  name: Teradata Query Service API Info Nodes API
  slug: open-teradata-nodes-api
- collection_type: open
  name: Teradata Query Service API Info Operations API
  slug: open-teradata-operations-api
- collection_type: open
  name: Teradata Query Service API Info Queries API
  slug: open-teradata-queries-api
- collection_type: open
  name: Teradata Query Service API Info Sessions API
  slug: open-teradata-sessions-api
- collection_type: open
  name: Teradata Query Service API Info Software API
  slug: open-teradata-software-api
- collection_type: open
  name: Teradata Query Service API Info Systems API
  slug: open-teradata-systems-api
- collection_type: open
  name: Teradata Query Service API Info Users API
  slug: open-teradata-users-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/finops/teradata-finops.yml
  title: ''
  type: FinOps
  url: finops/teradata-finops.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/rate-limits/teradata-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/teradata-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/plans/teradata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/teradata-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/rules/teradata-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/teradata-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/rules/teradata-rules.yml
  title: ''
  type: Spectral
  url: rules/teradata-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/rules/teradata-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/teradata-jsonschema-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/json-ld/teradata-querygrid-manager-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/teradata-querygrid-manager-api-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/json-ld/teradata-query-service-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/teradata-query-service-api-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/json-ld/teradata-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/teradata-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/vocabulary/teradata-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/teradata-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/data-model/teradata-data-model.yml
  title: ''
  type: DataModel
  url: data-model/teradata-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://www.teradata.com/trust-security-center/data-security/vulnerability-disclosure-policy
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/errors/teradata-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/teradata-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/conformance/teradata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/teradata-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/well-known/teradata-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/teradata-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/well-known/teradata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/teradata-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/hosts/teradata-hosts.yml
  title: ''
  type: Hosts
  url: hosts/teradata-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/vendors/teradata-vendors.yml
  title: ''
  type: Vendors
  url: vendors/teradata-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/packages/teradata-packages.yml
  title: ''
  type: Packages
  url: packages/teradata-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.teradata.com/university/academics/register
- group: commercial
  title: ''
  type: Pricing
  url: https://www.teradata.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.teradata.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.teradata.com/about-us/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/security/teradata-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/teradata-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.teradata.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/agentic-access/teradata-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/teradata-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/security/teradata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/teradata-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/authentication/teradata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/teradata-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/teradata/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/arazzo/teradata-auto-install-node-software-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/teradata-auto-install-node-software-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/arazzo/teradata-build-data-fabric-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/teradata-build-data-fabric-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/arazzo/teradata-cancel-running-query-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/teradata-cancel-running-query-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/arazzo/teradata-import-and-verify-system-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/teradata-import-and-verify-system-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/arazzo/teradata-poll-query-results-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/teradata-poll-query-results-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/arazzo/teradata-provision-cross-system-link-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/teradata-provision-cross-system-link-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/arazzo/teradata-register-system-in-datacenter-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/teradata-register-system-in-datacenter-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/arazzo/teradata-review-environment-health-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/teradata-review-environment-health-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/arazzo/teradata-run-connectivity-diagnostic-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/teradata-run-connectivity-diagnostic-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/arazzo/teradata-run-query-session-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/teradata-run-query-session-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/arazzo/teradata-session-lifecycle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/teradata-session-lifecycle-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teradata
- group: start
  title: ''
  type: Portal
  url: https://developer.teradata.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.teradata.com
- group: start
  title: ''
  type: GettingStarted
  url: https://quickstarts.teradata.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Teradata
- group: operate
  title: ''
  type: Support
  url: https://support.teradata.com
- group: learn
  title: ''
  type: Training
  url: https://www.teradata.com/University
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teradata.com/Legal/Terms-of-Use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teradata.com/Legal/Privacy
- group: build
  title: Python SQL Driver
  type: SDKs
  url: https://pypi.org/project/teradatasql/
- group: build
  title: Node.js SQL Driver
  type: SDKs
  url: https://www.npmjs.com/package/teradatasql
- group: build
  title: R SQL Driver
  type: SDKs
  url: https://github.com/Teradata/r-driver
- group: build
  title: Rust API
  type: SDKs
  url: https://github.com/Teradata/teradatarustapi
- group: build
  title: Go SQL Driver
  type: SDKs
  url: https://github.com/Teradata/gosql-driver
- group: build
  title: JDBC Driver
  type: SDKs
  url: https://github.com/Teradata/jdbc-driver
- group: build
  title: VS Code SQL Extension
  type: CLI
  url: https://github.com/Teradata/teradata-vscode-sql-extension
- group: build
  title: MCP Server
  type: Tools
  url: https://github.com/Teradata/teradata-mcp-server
- group: build
  title: QueryGrid MCP Server
  type: Tools
  url: https://github.com/Teradata/teradata-qg-mcp-server
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/rules/teradata-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/teradata-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/vocabulary/teradata-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/teradata-vocabulary.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Teradata/teradata-mcp-server
created: '2026-04-18'
description: Teradata provides enterprise analytics and data management solutions. The Teradata VantageCloud platform delivers connected multi-cloud data analytics with capabilities for data warehousing, advanced analytics, and machine learning at scale. Teradata offers REST APIs for managing QueryGrid data fabric connections, running SQL queries, and administering platform resources.
examples:
- key_count: 5
  name: Query Service Api Query Result Example
  slug: query-service-api-query-result-example
- key_count: 5
  name: Query Service Api Session Example
  slug: query-service-api-session-example
- key_count: 5
  name: Querygrid Manager Api Issue Example
  slug: querygrid-manager-api-issue-example
- key_count: 6
  name: Querygrid Manager Api Node Example
  slug: querygrid-manager-api-node-example
- key_count: 6
  name: Querygrid Manager Api System Example
  slug: querygrid-manager-api-system-example
features:
- description: Cloud-native analytics platform available on AWS, Azure, and Google Cloud.
  name: VantageCloud
- description: Advanced analytics engine with machine learning, graph analytics, and AI capabilities built into Vantage.
  name: ClearScape Analytics
- description: Data fabric for multi-system analytics enabling queries across Teradata, Hadoop, Spark, and cloud object storage.
  name: QueryGrid
- description: Model lifecycle management for deploying, monitoring, and governing machine learning models.
  name: ModelOps
- description: On-demand AI and ML engine for exploratory analytics without infrastructure management.
  name: AI Unlimited
- description: Support for Apache Iceberg and open table formats for lakehouse analytics.
  name: Open Table Formats
finops:
- name: Teradata Finops
  service_category: API
  slug: teradata-finops
image: /assets/icons/teradata.png
json_schemas:
- name: QueryResult
  property_count: 6
  slug: query-service-api-query-result
- name: Session
  property_count: 5
  slug: query-service-api-session
- name: ApiInfo
  property_count: 3
  slug: querygrid-manager-api-api-info
- name: Bridge
  property_count: 5
  slug: querygrid-manager-api-bridge
- name: Connector
  property_count: 5
  slug: querygrid-manager-api-connector
- name: DataCenter
  property_count: 4
  slug: querygrid-manager-api-data-center
- name: Issue
  property_count: 5
  slug: querygrid-manager-api-issue
- name: Node
  property_count: 6
  slug: querygrid-manager-api-node
- name: System
  property_count: 6
  slug: querygrid-manager-api-system
- name: AutoInstallRequest
  property_count: 2
  slug: teradata-auto-install-request
- name: AutoInstallResponse
  property_count: 3
  slug: teradata-auto-install-response
- name: Bridge
  property_count: 5
  slug: teradata-bridge
- name: CommPolicy
  property_count: 5
  slug: teradata-comm-policy
- name: Connector
  property_count: 5
  slug: teradata-connector
- name: DiagnosticCheckRequest
  property_count: 3
  slug: teradata-diagnostic-check-request
- name: DiagnosticCheckResponse
  property_count: 3
  slug: teradata-diagnostic-check-response
- name: Fabric
  property_count: 4
  slug: teradata-fabric
- name: ImportSystemRequest
  property_count: 2
  slug: teradata-import-system-request
- name: ImportSystemResponse
  property_count: 3
  slug: teradata-import-system-response
- name: Issue
  property_count: 5
  slug: teradata-issue
- name: Link
  property_count: 6
  slug: teradata-link
- name: Manager
  property_count: 5
  slug: teradata-manager
- name: Node
  property_count: 6
  slug: teradata-node
- name: post-datasource
  property_count: 29
  slug: teradata-post-datasource
- name: post-link
  property_count: 19
  slug: teradata-post-link
- name: query-details
  property_count: 0
  slug: teradata-query-details
- name: QueryRequest
  property_count: 4
  slug: teradata-query-request
- name: QueryResult
  property_count: 6
  slug: teradata-query-result
- name: query-summary
  property_count: 0
  slug: teradata-query-summary
- name: QuerySystem
  property_count: 4
  slug: teradata-query-system
- name: SessionRequest
  property_count: 3
  slug: teradata-session-request
- name: Session
  property_count: 5
  slug: teradata-session
- name: Software
  property_count: 3
  slug: teradata-software
- name: system
  property_count: 23
  slug: teradata-system
- name: User
  property_count: 2
  slug: teradata-user
- name: watchdog-heartbeat
  property_count: 15
  slug: teradata-watchdog-heartbeat
json_structures:
- name: Query Service Api Query Result Structure
  property_count: 6
  slug: query-service-api-query-result-structure
- name: Query Service Api Session Structure
  property_count: 5
  slug: query-service-api-session-structure
- name: Querygrid Manager Api Issue Structure
  property_count: 5
  slug: querygrid-manager-api-issue-structure
- name: Querygrid Manager Api Node Structure
  property_count: 6
  slug: querygrid-manager-api-node-structure
- name: Querygrid Manager Api System Structure
  property_count: 6
  slug: querygrid-manager-api-system-structure
jsonld:
- class_count: 120
  name: Teradata Context
  property_count: 282
  slug: teradata-context
- class_count: 4
  name: Teradata Query Service Api Context
  property_count: 13
  slug: teradata-query-service-api-context
- class_count: 15
  name: Teradata Querygrid Manager Api Context
  property_count: 23
  slug: teradata-querygrid-manager-api-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Teradata
nav: Providers
network: true
overview: 'Teradata publishes 34 APIs on the [APIs.io](https://apis.io/) network, including API Info API, Configuration API, Issues API, and 31 more. Tagged areas include Analytics, Cloud, Data Management, Data Warehousing, and Database.


  The Teradata catalog on APIs.io includes 3 JSON-LD contexts and 3 Spectral governance rulesets.


  Teradata''s developer surface includes signup flow, pricing, authentication, developer portal, documentation, getting-started guide, support, and 55 more developer resources.'
plans:
- name: Teradata Plans Pricing
  plan_count: 3
  slug: teradata-plans-pricing
press:
- date: ''
  title: Teradata Named a Leader in Data Fabric Platforms, Q4 2025 Analyst Evaluation
  url: https://www.teradata.com/press-releases/2026/leader-in-data-fabric-platforms
- date: ''
  title: Teradata Named a Leader in Nucleus Research 2026 DSML Platform Technology Value Matrix
  url: https://www.teradata.com/press-releases/2026/leader-in-nucleus-research-2026
- date: ''
  title: Teradata to Present at Upcoming Investor Conferences
  url: https://www.teradata.com/press-releases/2025/teradata-investor-conference
- date: ''
  title: Teradata Enables AI Agents to Autonomously Process Text, Images, and Audio at Enterprise Scale
  url: https://www.teradata.com/press-releases/2026/teradata-enables-ai-agents
- date: ''
  title: Teradata Announces 2025 Fourth Quarter and Full-Year Earnings Release Date
  url: https://www.teradata.com/press-releases/2026/teradata-announces-2025-fourth-quarter-and-full-year-earnings-release-date
- date: ''
  title: Teradata AI Services Deliver Production-Ready Agentic Use Cases that Drive Measurable Business Impact
  url: https://www.teradata.com/press-releases/2025/teradata-ai-services-deliver-production-ready-agentic-use-cases
- date: ''
  title: Teradata Delivers Autonomous Knowledge and Data Sovereignty Without Compromise
  url: https://www.teradata.com/press-releases/2026/autonomous-knowledge-and-data-sovereignty
- date: ''
  title: Teradata Accelerates AI Innovation with More than 150 Enterprise AI Engagements in 2025
  url: https://www.teradata.com/press-releases/2026/teradata-accelerates-150-enterprise-ai-engage
random_paper: 2
rate_limits:
- limit_count: 5
  name: Teradata Rate Limits
  slug: teradata-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Teradata API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: teradata-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Teradata API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: teradata-rules
- effective_rule_count: 73
  extends:
  - spectral:oas
  name: Teradata API Rules
  rule_count: 32
  severity_counts:
    error: 13
    hint: 0
    info: 4
    warn: 15
  slug: teradata-spectral-rules
score:
  band: strong
  composite: 59.4
  coverage:
    artifact_dirs: 32
    catalog_earned: 75.0
    catalog_earned_first_party: 0.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.6
  facets:
    access_clarity: 60.5
    contract_governance: 31.8
    contract_quality: 56.1
    developer_ergonomics: 74.4
    discoverability: 83.9
    operational_transparency: 21.1
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 11.1
      derived: 6
      marker_coverage: 16.7
      total: 36
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/teradata/refs/heads/main/screenshots/teradata-2026-06-20T195123.png
security:
- kind: authentication
  name: Teradata Authentication
  slug: teradata-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Teradata Domain Security
  slug: teradata-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Teradata Vulnerability Disclosure
  slug: teradata-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: teradata
tags:
- Analytics
- Cloud
- Data Management
- Data Warehousing
- Database
- Enterprise
- Machine Learning
- SQL
- Fortune 1000
use_cases:
- description: Centralized data warehousing with petabyte-scale analytics for enterprise reporting and BI.
  name: Enterprise Data Warehousing
- description: In-database machine learning, statistical analysis, and predictive modeling at scale.
  name: Advanced Analytics
- description: Connected analytics across AWS, Azure, and Google Cloud with data fabric integration.
  name: Multi-Cloud Analytics
- description: End-to-end machine learning model lifecycle management with ModelOps.
  name: AI and ML Operations
- description: Real-time data ingestion and analytics with QueryGrid cross-system query federation.
  name: Real-Time Data Integration
website: https://www.teradata.com/
---
