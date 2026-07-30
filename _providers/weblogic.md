---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 38
  human_in_the_loop: 4
  name: Weblogic Agentic Access
  operation_count: 95
  slug: weblogic-agentic-access
  summary_line: 95 operations · 38 acting · 4 human-in-the-loop
api_count: 19
apis:
- description: Python-based scripting interface for automating WebLogic Server administration tasks. Supports online (connected) and offline modes for configuring, deploying, and managing WebLogic domains programmat
  name: WebLogic WLST (WebLogic Scripting Tool) API
  slug: weblogic-wlst-weblogic-scripting-tool-api
- description: Java Management Extensions API for programmatic access to WebLogic Server MBeans. Provides the same management capabilities as the REST API via JMX connections, suitable for Java-based management clie
  name: WebLogic JMX API
  slug: weblogic-jmx-api
- description: Deploy, undeploy, redeploy, and manage application configurations using the edit tree
  name: Oracle WebLogic Server APIs Application Deployments API
  slug: weblogic-application-deployments-api
- description: Application deployment monitoring
  name: Oracle WebLogic Server APIs Applications API
  slug: weblogic-applications-api
- description: Cluster-level monitoring information
  name: Oracle WebLogic Server APIs Clusters API
  slug: weblogic-clusters-api
- description: JDBC data source monitoring and metrics
  name: Oracle WebLogic Server APIs Data Sources API
  slug: weblogic-data-sources-api
- description: Runtime deployment operations using the domain runtime deployment manager
  name: Oracle WebLogic Server APIs Deployment Operations API
  slug: weblogic-deployment-operations-api
- description: WebLogic Diagnostic Framework (WLDF) resources
  name: Oracle WebLogic Server APIs Diagnostics API
  slug: weblogic-diagnostics-api
- description: Read-only access to the domain-level configuration MBean tree including servers, clusters, data sources, JMS resources, and security realms.
  name: Oracle WebLogic Server APIs Domain Configuration API
  slug: weblogic-domain-configuration-api
- description: Access to domain-level runtime MBeans including server lifecycle operations, deployment operations, and domain-wide monitoring data.
  name: Oracle WebLogic Server APIs Domain Runtime API
  slug: weblogic-domain-runtime-api
- description: Configuration editing operations. An edit session must be started before making changes to the domain configuration. Changes are staged and then activated.
  name: Oracle WebLogic Server APIs Edit API
  slug: weblogic-edit-api
- description: Server and subsystem health checks
  name: Oracle WebLogic Server APIs Health API
  slug: weblogic-health-api
- description: JMS subsystem monitoring
  name: Oracle WebLogic Server APIs JMS API
  slug: weblogic-jms-api
- description: Deploy and manage shared libraries
  name: Oracle WebLogic Server APIs Library Deployments API
  slug: weblogic-library-deployments-api
- description: Server lifecycle management operations including starting, stopping, suspending, and resuming servers.
  name: Oracle WebLogic Server APIs Lifecycle API
  slug: weblogic-lifecycle-api
- description: Read-only access to the server-level configuration MBean tree for individual managed servers.
  name: Oracle WebLogic Server APIs Server Configuration API
  slug: weblogic-server-configuration-api
- description: Access to server-level runtime MBeans providing monitoring data for individual server instances including thread pools, JDBC, JMS, and application runtimes.
  name: Oracle WebLogic Server APIs Server Runtime API
  slug: weblogic-server-runtime-api
- description: Server-level monitoring and health information
  name: Oracle WebLogic Server APIs Servers API
  slug: weblogic-servers-api
- description: Upload application archives to the administration server
  name: Oracle WebLogic Server APIs Upload API
  slug: weblogic-upload-api
artifact_total: 84
collections:
- collection_type: open
  name: Oracle WebLogic Server APIs Oracle WebLogic Server Deployment API
  slug: open-weblogic-deployment
- collection_type: open
  name: Oracle WebLogic Server APIs Oracle WebLogic Server Monitoring and Diagnostics API
  slug: open-weblogic-monitoring-diagnostics
- collection_type: open
  name: Oracle WebLogic Server APIs Oracle WebLogic Server RESTful Management Services API
  slug: open-weblogic-restful-management-services
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weblogic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weblogic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/weblogic-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/intro/
- group: other
  title: ''
  type: Downloads
  url: https://www.oracle.com/middleware/technologies/weblogic-server-downloads.html
- group: operate
  title: ''
  type: Support
  url: https://support.oracle.com
- group: operate
  title: ''
  type: Community
  url: https://community.oracle.com/tech/developers/categories/weblogic-server
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/weblogicserver/
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/middleware/technologies/weblogic.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/weblogic
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@OracleDevelopers
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/weblogic-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/weblogic-rules.yml
created: '2024'
description: Collection of APIs and resources for Oracle WebLogic Server administration and management. WebLogic Server is Oracle's enterprise-grade Java EE application server providing high availability, scalability, and comprehensive management capabilities through RESTful management APIs, monitoring and diagnostics, and deployment services.
examples:
- key_count: 4
  name: Weblogic Deploy Application Example
  slug: weblogic-deploy-application-example
- key_count: 4
  name: Weblogic Start Server Example
  slug: weblogic-start-server-example
finops:
- name: Weblogic Finops
  service_category: Application Server / Middleware
  slug: weblogic-finops
image: https://www.oracle.com/a/ocom/img/weblogic-server.png
json_schemas:
- name: ActivationStatus
  property_count: 2
  slug: weblogic-activationstatus
- name: AppDeployment
  property_count: 11
  slug: weblogic-appdeployment
- name: AppDeploymentCreate
  property_count: 9
  slug: weblogic-appdeploymentcreate
- name: AppDeploymentUpdate
  property_count: 6
  slug: weblogic-appdeploymentupdate
- name: WebLogic Application Deployment
  property_count: 16
  slug: weblogic-application-deployment
- name: ApplicationRuntime
  property_count: 6
  slug: weblogic-applicationruntime
- name: ChangeManagerStatus
  property_count: 4
  slug: weblogic-changemanagerstatus
- name: WebLogic Cluster Configuration
  property_count: 18
  slug: weblogic-cluster-configuration
- name: ClusterConfiguration
  property_count: 11
  slug: weblogic-clusterconfiguration
- name: ClusterMonitoring
  property_count: 6
  slug: weblogic-clustermonitoring
- name: DataAccessRuntime
  property_count: 2
  slug: weblogic-dataaccessruntime
- name: WebLogic JDBC Data Source Configuration
  property_count: 4
  slug: weblogic-datasource-configuration
- name: DataSourceMetrics
  property_count: 16
  slug: weblogic-datasourcemetrics
- name: DeploymentMetrics
  property_count: 6
  slug: weblogic-deploymentmetrics
- name: DeploymentProgress
  property_count: 6
  slug: weblogic-deploymentprogress
- name: DeploymentTaskStatus
  property_count: 7
  slug: weblogic-deploymenttaskstatus
- name: DiagnosticQueryResult
  property_count: 4
  slug: weblogic-diagnosticqueryresult
- name: WebLogic Domain Configuration
  property_count: 17
  slug: weblogic-domain-configuration
- name: DomainConfiguration
  property_count: 6
  slug: weblogic-domainconfiguration
- name: DomainRuntime
  property_count: 3
  slug: weblogic-domainruntime
- name: EditRoot
  property_count: 3
  slug: weblogic-editroot
- name: Error
  property_count: 4
  slug: weblogic-error
- name: JDBCDataSourceRuntime
  property_count: 19
  slug: weblogic-jdbcdatasourceruntime
- name: JDBCServiceRuntime
  property_count: 2
  slug: weblogic-jdbcserviceruntime
- name: JDBCSystemResource
  property_count: 5
  slug: weblogic-jdbcsystemresource
- name: JMSDestinationMetrics
  property_count: 11
  slug: weblogic-jmsdestinationmetrics
- name: JMSRuntime
  property_count: 8
  slug: weblogic-jmsruntime
- name: JMSServerMetrics
  property_count: 11
  slug: weblogic-jmsservermetrics
- name: JMSServerRuntime
  property_count: 12
  slug: weblogic-jmsserverruntime
- name: JMSSystemResource
  property_count: 4
  slug: weblogic-jmssystemresource
- name: JVMMetrics
  property_count: 9
  slug: weblogic-jvmmetrics
- name: JVMRuntime
  property_count: 10
  slug: weblogic-jvmruntime
- name: LibraryDeployment
  property_count: 9
  slug: weblogic-librarydeployment
- name: LibraryDeploymentCreate
  property_count: 6
  slug: weblogic-librarydeploymentcreate
- name: Link
  property_count: 3
  slug: weblogic-link
- name: SecurityConfiguration
  property_count: 4
  slug: weblogic-securityconfiguration
- name: WebLogic Server Configuration
  property_count: 22
  slug: weblogic-server-configuration
- name: WebLogic Server Runtime
  property_count: 19
  slug: weblogic-server-runtime
- name: ServerConfiguration
  property_count: 14
  slug: weblogic-serverconfiguration
- name: ServerHealth
  property_count: 3
  slug: weblogic-serverhealth
- name: ServerLifecycleRuntime
  property_count: 4
  slug: weblogic-serverlifecycleruntime
- name: ServerMonitoring
  property_count: 12
  slug: weblogic-servermonitoring
- name: ServerRuntime
  property_count: 12
  slug: weblogic-serverruntime
- name: ServletMetrics
  property_count: 8
  slug: weblogic-servletmetrics
- name: TaskStatus
  property_count: 3
  slug: weblogic-taskstatus
- name: ThreadPoolMetrics
  property_count: 8
  slug: weblogic-threadpoolmetrics
- name: ThreadPoolRuntime
  property_count: 12
  slug: weblogic-threadpoolruntime
- name: WLDFSystemResource
  property_count: 5
  slug: weblogic-wldfsystemresource
- name: WorkManagerMetrics
  property_count: 4
  slug: weblogic-workmanagermetrics
json_structures:
- name: Weblogic Server Configuration Structure
  property_count: 0
  slug: weblogic-server-configuration-structure
- name: Weblogic Structure
  property_count: 0
  slug: weblogic-structure
jsonld:
- class_count: 0
  name: Weblogic Context
  property_count: 9
  slug: weblogic-context
layout: provider
modified: '2026-05-19'
name: Oracle WebLogic Server APIs
nav: Providers
network: true
overview: 'Oracle WebLogic Server APIs publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Application Deployments API, Applications API, Clusters API, and 14 more. Tagged areas include Application Server, Enterprise, Java EE, Middleware, and Oracle.


  The Oracle WebLogic Server APIs catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Oracle WebLogic Server APIs'' developer surface includes authentication, developer portal, getting-started guide, support, engineering blog, Stack Overflow tag, YouTube channel, and 11 more developer resources.'
plans:
- name: Weblogic Plans Pricing
  plan_count: 1
  slug: weblogic-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 1
  name: Weblogic Rate Limits
  slug: weblogic-rate-limits
rules:
- name: Oracle WebLogic Server APIs API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: weblogic-jsonschema-spectral-rules
- name: Oracle WebLogic Server APIs API Rules
  rule_count: 13
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 11
  slug: weblogic-rules
score:
  band: developing
  composite: 55.0
  delta: -4.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 70.3
    developer_ergonomics: 37.0
    discoverability: 63.0
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 59.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/weblogic/refs/heads/main/screenshots/weblogic-2026-06-20T201334.png
security:
- kind: authentication
  name: Weblogic Authentication
  slug: weblogic-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Weblogic Domain Security
  slug: weblogic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: weblogic
tags:
- Application Server
- Enterprise
- Java EE
- Middleware
- Oracle
- WebLogic
website: https://www.oracle.com/middleware/technologies/weblogic.html
---
