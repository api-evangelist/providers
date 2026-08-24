---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 78
  human_in_the_loop: 1
  name: Aptible Agentic Access
  operation_count: 225
  slug: aptible-agentic-access
  summary_line: 225 operations · 78 acting · 1 human-in-the-loop
api_count: 51
apis:
- description: The Aptible authentication and identity service at auth.aptible.com. A HAL+JSON API exposing organizations, sessions, tokens, OAuth clients, users, U2F trusted facets and SSH key pre-authorizations, p
  name: Aptible Auth API
  slug: auth
- description: The Accounts API from Aptible — 4 operation(s) for accounts.
  name: Aptible Accounts API
  slug: aptible-accounts-api
- description: The actions API from Aptible — 2 operation(s) for actions.
  name: Aptible Actions API
  slug: aptible-actions-api
- description: The ActivityReports API from Aptible — 3 operation(s) for activityreports.
  name: Aptible Activity Reports API
  slug: aptible-activityreports-api
- description: The Apps API from Aptible — 5 operation(s) for apps.
  name: Aptible Apps API
  slug: aptible-apps-api
- description: The assets API from Aptible — 2 operation(s) for assets.
  name: Aptible Assets API
  slug: aptible-assets-api
- description: The BackupRetentionPolicies API from Aptible — 2 operation(s) for backupretentionpolicies.
  name: Aptible Backup Retention Policies API
  slug: aptible-backupretentionpolicies-api
- description: The Backups API from Aptible — 5 operation(s) for backups.
  name: Aptible Backups API
  slug: aptible-backups-api
- description: The Certificates API from Aptible — 2 operation(s) for certificates.
  name: Aptible Certificates API
  slug: aptible-certificates-api
- description: The Claims API from Aptible — 3 operation(s) for claims.
  name: Aptible Claims API
  slug: aptible-claims-api
- description: The CodeScanResults API from Aptible — 2 operation(s) for codescanresults.
  name: Aptible Code Scan Results API
  slug: aptible-codescanresults-api
- description: The Configurations API from Aptible — 3 operation(s) for configurations.
  name: Aptible Configurations API
  slug: aptible-configurations-api
- description: The connections API from Aptible — 2 operation(s) for connections.
  name: Aptible Connections API
  slug: aptible-connections-api
- description: The Containers API from Aptible — 4 operation(s) for containers.
  name: Aptible Containers API
  slug: aptible-containers-api
- description: The DatabaseCredentials API from Aptible — 2 operation(s) for databasecredentials.
  name: Aptible Database Credentials API
  slug: aptible-databasecredentials-api
- description: The Databases API from Aptible — 5 operation(s) for databases.
  name: Aptible Databases API
  slug: aptible-databases-api
- description: The Deployments API from Aptible — 3 operation(s) for deployments.
  name: Aptible Deployments API
  slug: aptible-deployments-api
- description: The DiskAttachments API from Aptible — 5 operation(s) for diskattachments.
  name: Aptible Disk Attachments API
  slug: aptible-diskattachments-api
- description: The Disks API from Aptible — 2 operation(s) for disks.
  name: Aptible Disks API
  slug: aptible-disks-api
- description: The environments API from Aptible — 5 operation(s) for environments.
  name: Aptible Environments API
  slug: aptible-environments-api
- description: The EphemeralContainers API from Aptible — 3 operation(s) for ephemeralcontainers.
  name: Aptible Ephemeral Containers API
  slug: aptible-ephemeralcontainers-api
- description: The EphemeralSessions API from Aptible — 3 operation(s) for ephemeralsessions.
  name: Aptible Ephemeral Sessions API
  slug: aptible-ephemeralsessions-api
- description: The Images API from Aptible — 4 operation(s) for images.
  name: Aptible Images API
  slug: aptible-images-api
- description: The IntrusionDetectionReports API from Aptible — 4 operation(s) for intrusiondetectionreports.
  name: Aptible Intrusion Detection Reports API
  slug: aptible-intrusiondetectionreports-api
- description: The LlmGatewayConfigurations API from Aptible — 2 operation(s) for llmgatewayconfigurations.
  name: Aptible Llm Gateway Configurations API
  slug: aptible-llmgatewayconfigurations-api
- description: The LlmKeys API from Aptible — 5 operation(s) for llmkeys.
  name: Aptible Llm Keys API
  slug: aptible-llmkeys-api
- description: The LlmPolicies API from Aptible — 5 operation(s) for llmpolicies.
  name: Aptible Llm Policies API
  slug: aptible-llmpolicies-api
- description: The LogDrains API from Aptible — 2 operation(s) for logdrains.
  name: Aptible Log Drains API
  slug: aptible-logdrains-api
- description: The Maintenances API from Aptible — 2 operation(s) for maintenances.
  name: Aptible Maintenances API
  slug: aptible-maintenances-api
- description: The MetricDrains API from Aptible — 2 operation(s) for metricdrains.
  name: Aptible Metric Drains API
  slug: aptible-metricdrains-api
- description: The operations API from Aptible — 18 operation(s) for operations.
  name: Aptible Operations API
  slug: aptible-operations-api
- description: The organizations API from Aptible — 4 operation(s) for organizations.
  name: Aptible Organizations API
  slug: aptible-organizations-api
- description: The Permissions API from Aptible — 3 operation(s) for permissions.
  name: Aptible Permissions API
  slug: aptible-permissions-api
- description: The PersistentDisks API from Aptible — 2 operation(s) for persistentdisks.
  name: Aptible Persistent Disks API
  slug: aptible-persistentdisks-api
- description: The Plans API from Aptible — 2 operation(s) for plans.
  name: Aptible Plans API
  slug: aptible-plans-api
- description: The Releases API from Aptible — 2 operation(s) for releases.
  name: Aptible Releases API
  slug: aptible-releases-api
- description: The Root API from Aptible — 1 operation(s) for root.
  name: Aptible Root API
  slug: aptible-root-api
- description: The Services API from Aptible — 3 operation(s) for services.
  name: Aptible Services API
  slug: aptible-services-api
- description: The ServiceSizingPolicies API from Aptible — 4 operation(s) for servicesizingpolicies.
  name: Aptible Service Sizing Policies API
  slug: aptible-servicesizingpolicies-api
- description: The Settings API from Aptible — 5 operation(s) for settings.
  name: Aptible Settings API
  slug: aptible-settings-api
- description: The Sources API from Aptible — 4 operation(s) for sources.
  name: Aptible Sources API
  slug: aptible-sources-api
- description: The SshPortalConnections API from Aptible — 2 operation(s) for sshportalconnections.
  name: Aptible Ssh Portal Connections API
  slug: aptible-sshportalconnections-api
- description: The Stacks API from Aptible — 2 operation(s) for stacks.
  name: Aptible Stacks API
  slug: aptible-stacks-api
- description: The System API from Aptible — 1 operation(s) for system.
  name: Aptible System API
  slug: aptible-system-api
- description: The Tool API from Aptible — 1 operation(s) for tool.
  name: Aptible Tool API
  slug: aptible-tool-api
- description: The Tools API from Aptible — 1 operation(s) for tools.
  name: Aptible Tools API
  slug: aptible-tools-api
- description: The utilities API from Aptible — 2 operation(s) for utilities.
  name: Aptible Utilities API
  slug: aptible-utilities-api
- description: The Vhosts API from Aptible — 5 operation(s) for vhosts.
  name: Aptible Vhosts API
  slug: aptible-vhosts-api
- description: The VpcPeers API from Aptible — 2 operation(s) for vpcpeers.
  name: Aptible Vpc Peers API
  slug: aptible-vpcpeers-api
- description: The VpnTunnels API from Aptible — 2 operation(s) for vpntunnels.
  name: Aptible Vpn Tunnels API
  slug: aptible-vpntunnels-api
- description: The worker API from Aptible — 1 operation(s) for worker.
  name: Aptible Worker API
  slug: aptible-worker-api
artifact_total: 108
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Aptible API v1 Accounts API
  slug: open-aptible-accounts-api
- collection_type: open
  name: Cloud Actions API
  slug: open-aptible-actions-api
- collection_type: open
  name: Aptible API v1 Activity Reports API
  slug: open-aptible-activityreports-api
- collection_type: open
  name: Aptible API v1 Apps API
  slug: open-aptible-apps-api
- collection_type: open
  name: Cloud Assets API
  slug: open-aptible-assets-api
- collection_type: open
  name: Aptible API v1 Backup Retention Policies API
  slug: open-aptible-backupretentionpolicies-api
- collection_type: open
  name: Aptible API v1 Backups API
  slug: open-aptible-backups-api
- collection_type: open
  name: Aptible API v1 Certificates API
  slug: open-aptible-certificates-api
- collection_type: open
  name: Aptible API v1 Claims API
  slug: open-aptible-claims-api
- collection_type: open
  name: Aptible API v1 Code Scan Results API
  slug: open-aptible-codescanresults-api
- collection_type: open
  name: Aptible API v1 Configurations API
  slug: open-aptible-configurations-api
- collection_type: open
  name: Cloud Connections API
  slug: open-aptible-connections-api
- collection_type: open
  name: Aptible API v1 Containers API
  slug: open-aptible-containers-api
- collection_type: open
  name: Aptible API v1 Database Credentials API
  slug: open-aptible-databasecredentials-api
- collection_type: open
  name: Aptible API v1 Databases API
  slug: open-aptible-databases-api
- collection_type: open
  name: Aptible API v1 Deployments API
  slug: open-aptible-deployments-api
- collection_type: open
  name: Aptible API v1 Disk Attachments API
  slug: open-aptible-diskattachments-api
- collection_type: open
  name: Aptible API v1 Disks API
  slug: open-aptible-disks-api
- collection_type: open
  name: Cloud Environments API
  slug: open-aptible-environments-api
- collection_type: open
  name: Aptible API v1 Ephemeral Containers API
  slug: open-aptible-ephemeralcontainers-api
- collection_type: open
  name: Aptible API v1 Ephemeral Sessions API
  slug: open-aptible-ephemeralsessions-api
- collection_type: open
  name: Aptible API v1 Images API
  slug: open-aptible-images-api
- collection_type: open
  name: Aptible API v1 Intrusion Detection Reports API
  slug: open-aptible-intrusiondetectionreports-api
- collection_type: open
  name: Aptible API v1 Llm Gateway Configurations API
  slug: open-aptible-llmgatewayconfigurations-api
- collection_type: open
  name: Aptible API v1 Llm Keys API
  slug: open-aptible-llmkeys-api
- collection_type: open
  name: Aptible API v1 Llm Policies API
  slug: open-aptible-llmpolicies-api
- collection_type: open
  name: Aptible API v1 Log Drains API
  slug: open-aptible-logdrains-api
- collection_type: open
  name: Aptible API v1 Maintenances API
  slug: open-aptible-maintenances-api
- collection_type: open
  name: Aptible API v1 Metric Drains API
  slug: open-aptible-metricdrains-api
- collection_type: open
  name: Aptible Operations API
  slug: open-aptible-operations-api
- collection_type: open
  name: Cloud Organizations API
  slug: open-aptible-organizations-api
- collection_type: open
  name: Aptible API v1 Permissions API
  slug: open-aptible-permissions-api
- collection_type: open
  name: Aptible API v1 Persistent Disks API
  slug: open-aptible-persistentdisks-api
- collection_type: open
  name: Aptible API v1 Plans API
  slug: open-aptible-plans-api
- collection_type: open
  name: Aptible API v1 Releases API
  slug: open-aptible-releases-api
- collection_type: open
  name: Aptible API v1 Root API
  slug: open-aptible-root-api
- collection_type: open
  name: Aptible API v1 Services API
  slug: open-aptible-services-api
- collection_type: open
  name: Aptible API v1 Service Sizing Policies API
  slug: open-aptible-servicesizingpolicies-api
- collection_type: open
  name: Aptible API v1 Settings API
  slug: open-aptible-settings-api
- collection_type: open
  name: Aptible API v1 Sources API
  slug: open-aptible-sources-api
- collection_type: open
  name: Aptible API v1 Ssh Portal Connections API
  slug: open-aptible-sshportalconnections-api
- collection_type: open
  name: Aptible API v1 Stacks API
  slug: open-aptible-stacks-api
- collection_type: open
  name: Cloud System API
  slug: open-aptible-system-api
- collection_type: open
  name: Tool API
  slug: open-aptible-tool-api
- collection_type: open
  name: Tool Tools API
  slug: open-aptible-tools-api
- collection_type: open
  name: Cloud Utilities API
  slug: open-aptible-utilities-api
- collection_type: open
  name: Aptible API v1 Vhosts API
  slug: open-aptible-vhosts-api
- collection_type: open
  name: Aptible API v1 Vpc Peers API
  slug: open-aptible-vpcpeers-api
- collection_type: open
  name: Aptible API v1 Vpn Tunnels API
  slug: open-aptible-vpntunnels-api
- collection_type: open
  name: Cloud Worker API
  slug: open-aptible-worker-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/aptible-cloud-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/aptible/cloud-api-clients/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/aptible/cloud-api-clients/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/aptible/cloud-api-clients/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aptible-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aptible-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aptible-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aptible-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.aptible.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aptible.com/docs/getting-started/home
- group: docs
  title: ''
  type: Documentation
  url: https://www.aptible.com/docs/getting-started/home
- group: docs
  title: ''
  type: APIReference
  url: https://www.aptible.com/docs/reference/aptible-cli/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aptible.com/docs/getting-started/deploy-starter-template/overview
- group: operate
  title: ''
  type: Support
  url: https://app.aptible.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.aptible.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aptible
- group: operate
  title: ''
  type: Roadmap
  url: https://portal.productboard.com/aptible/2-aptible-roadmap-portal/tabs/10-in-progress
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aptible.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.aptible.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.aptible.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aptible.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aptible.com/legal/privacy-statement
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aptible.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.aptible.com/docs/core-concepts/security-compliance/overview
- group: auth
  title: ''
  type: Security
  url: https://www.aptible.com/legal/responsible-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aptible-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.aptible.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aptible-changelog.yml
- group: operate
  title: ''
  type: SLA
  url: https://www.aptible.com/legal/service-level-agreement
- group: build
  title: ''
  type: Packages
  url: packages/aptible-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aptible-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/aptible-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aptible-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/aptible-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aptible-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/aptible-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aptible-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aptible-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aptible-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aptible-data-model.yml
created: '2026-08-06'
description: Aptible is a Platform as a Service (PaaS) built for teams that have to prove security and compliance, not just ship. It deploys web apps, managed databases (PostgreSQL, MySQL, Redis, Elasticsearch, InfluxDB, RabbitMQ, SFTP) and AI workloads onto isolated, dedicated AWS infrastructure with encryption, host hardening, DDoS protection, managed host intrusion detection and vulnerability scanning enforced by default. Aptible ships HIPAA Business Associate Agreements, HITRUST R2 inheritance, SOC 2, PCI DSS and PIPEDA support alongside a Security & Compliance Dashboard, and more recently an LLM Gateway (400+ models behind one compliant API, with audit logging, spend limits and model access policies) and an MCP Gateway that governs how teams and agents reach MCP servers. The platform is driven by a public HAL+JSON REST API at api.aptible.com, an auth service at auth.aptible.com, a Ruby CLI, a Terraform provider, and generated Go/Ruby/Python client libraries.
image: https://framerusercontent.com/assets/sM8ECTApfoCzQMGmPJrKL9qxMFo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Aptible MCP Server
  slug: aptible-mcp-server
modified: '2026-08-06'
name: Aptible
nav: Providers
network: true
overview: 'Aptible publishes 50 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Actions API, Activity Reports API, and 47 more. Tagged areas include Company, Platform-as-a-Service, Cloud Infrastructure, Deployment, and Managed Databases.


  Aptible''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 34 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 54.2
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 16.7
    contract_quality: 52.3
    developer_ergonomics: 68.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 50.0
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 53
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aptible/refs/heads/main/screenshots/aptible-2026-08-07T161518.png
security:
- kind: authentication
  name: Aptible Authentication
  slug: aptible-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Aptible Domain Security
  slug: aptible-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aptible Vulnerability Disclosure
  slug: aptible-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aptible Trust Center
  slug: aptible-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: aptible
tags:
- Company
- Platform-as-a-Service
- Cloud Infrastructure
- Deployment
- Managed Databases
- Security
- Compliance
- HIPAA
- DevOps
- AI Gateway
- MCP
website: https://www.aptible.com/
---
