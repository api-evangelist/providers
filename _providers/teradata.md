---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Teradata Agentic Access
  operation_count: 33
  slug: teradata-agentic-access
  summary_line: 33 operations · 15 acting
api_count: 11
apis:
- description: The API Info API from Teradata — 1 operation(s) for api info.
  name: Teradata API Info API
  slug: teradata-api-info-api
- description: The Configuration API from Teradata — 8 operation(s) for configuration.
  name: Teradata Configuration API
  slug: teradata-configuration-api
- description: The Issues API from Teradata — 1 operation(s) for issues.
  name: Teradata Issues API
  slug: teradata-issues-api
- description: The Managers API from Teradata — 1 operation(s) for managers.
  name: Teradata Managers API
  slug: teradata-managers-api
- description: The Nodes API from Teradata — 1 operation(s) for nodes.
  name: Teradata Nodes API
  slug: teradata-nodes-api
- description: The Operations API from Teradata — 3 operation(s) for operations.
  name: Teradata Operations API
  slug: teradata-operations-api
- description: The Queries API from Teradata — 2 operation(s) for queries.
  name: Teradata Queries API
  slug: teradata-queries-api
- description: The Sessions API from Teradata — 2 operation(s) for sessions.
  name: Teradata Sessions API
  slug: teradata-sessions-api
- description: The Software API from Teradata — 1 operation(s) for software.
  name: Teradata Software API
  slug: teradata-software-api
- description: The Systems API from Teradata — 1 operation(s) for systems.
  name: Teradata Systems API
  slug: teradata-systems-api
- description: The Users API from Teradata — 1 operation(s) for users.
  name: Teradata Users API
  slug: teradata-users-api
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
artifact_total: 77
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/teradata-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teradata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/teradata-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/teradata/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/teradata-auto-install-node-software-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/teradata-build-data-fabric-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/teradata-cancel-running-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/teradata-import-and-verify-system-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/teradata-poll-query-results-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/teradata-provision-cross-system-link-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/teradata-register-system-in-datacenter-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/teradata-review-environment-health-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/teradata-run-connectivity-diagnostic-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/teradata-run-query-session-workflow.yml
- group: design
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
- group: company
  title: ''
  type: Blog
  url: https://www.teradata.com/blog
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
  title: ''
  type: SpectralRules
  url: rules/teradata-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/teradata-vocabulary.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Teradata/teradata-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.teradata.com/llms.txt
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
overview: 'Teradata publishes 11 APIs on the [APIs.io](https://apis.io/) network, including API Info API, Configuration API, Issues API, and 8 more. Tagged areas include Analytics, Cloud, Data Management, Data Warehousing, and Database.


  The Teradata catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Teradata''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, engineering blog, training material, and 31 more developer resources.'
plans:
- name: Teradata Plans Pricing
  plan_count: 3
  slug: teradata-plans-pricing
press:
- date: '2026-05-25'
  title: Teradata
  url: https://www.facebook.com/Teradata/posts/teradata-is-recognized-as-a-leader-in-nucleus-research-dsml-platforms-value-matr/1382241110599967/
- date: '2026-05-25'
  title: Teradata Enables AI Agents to Autonomously Process Text ...
  url: https://www.prnewswire.com/news-releases/teradata-enables-ai-agents-to-autonomously-process-text-images-and-audio-at-enterprise-scale-302707423.html
- date: '2026-05-25'
  title: Teradata launches AI Factory
  url: https://www.teradata.com/press-releases/2025/teradata-launches-ai-factory
- date: '2026-05-25'
  title: Teradata Enables AI Agents
  url: https://www.teradata.com/press-releases/2026/teradata-enables-ai-agents
- date: '2026-05-25'
  title: AI/ML
  url: https://www.teradata.com/insights/ai-and-machine-learning
- date: '2026-05-19'
  title: Teradata Delivers Autonomous Knowledge and Data Sovereignty Without Compromise
  url: https://www.teradata.com/press-releases/2026/autonomous-knowledge-and-data-sovereignty
- date: '2026-05-12'
  title: Teradata Recognized as Exemplary Across Seven Categories in 2026 ISG Buyers Guides™ for AI and Data Platforms
  url: https://www.teradata.com/press-releases/2026/teradata-recognized-2026-isg-buyers-guides
- date: '2026-05-07'
  title: Introducing the Teradata Autonomous Knowledge Platform
  url: https://www.teradata.com/press-releases/2026/introducing-the-autonomous-knowledge-platform
random_paper: 19
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
  band: developing
  composite: 41.5
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.8
    contract_quality: 21.6
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
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
slug: teradata
tags:
- Analytics
- Cloud
- Data Management
- Data Warehousing
- Database
- Enterprise
- Machine-Learning
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
website: https://developer.teradata.com
---
