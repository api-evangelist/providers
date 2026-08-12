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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 67
  human_in_the_loop: 8
  name: Websphere Agentic Access
  operation_count: 154
  slug: websphere-agentic-access
  summary_line: 154 operations · 67 acting · 8 human-in-the-loop
api_count: 35
apis:
- description: Java Management Extensions (JMX) API for programmatic management and monitoring of WebSphere Application Server. Provides MBean access for server configuration, performance monitoring, and resource ma
  name: WebSphere Application Server JMX API
  slug: websphere-jmx-api
- description: Application deployment and lifecycle management
  name: IBM WebSphere Applications API
  slug: websphere-applications-api
- description: Authentication and authorization
  name: IBM WebSphere Authentication API
  slug: websphere-authentication-api
- description: Jakarta Batch job management
  name: IBM WebSphere Batch API
  slug: websphere-batch-api
- description: Channel administration
  name: IBM WebSphere Channels API
  slug: websphere-channels-api
- description: Cluster management operations
  name: IBM WebSphere Clusters API
  slug: websphere-clusters-api
- description: Compliance and configuration drift detection
  name: IBM WebSphere Compliance API
  slug: websphere-compliance-api
- description: Server configuration API
  name: IBM WebSphere Config API
  slug: websphere-config-api
- description: Server configuration management
  name: IBM WebSphere Configuration API
  slug: websphere-configuration-api
- description: Collective controller operations
  name: IBM WebSphere Controller API
  slug: websphere-controller-api
- description: Liberty feature management
  name: IBM WebSphere Features API
  slug: websphere-features-api
- description: File upload and download operations
  name: IBM WebSphere File Transfer API
  slug: websphere-file-transfer-api
- description: Fix management and automated patching
  name: IBM WebSphere Fixes API
  slug: websphere-fixes-api
- description: MicroProfile Health Check API
  name: IBM WebSphere Health API
  slug: websphere-health-api
- description: Host management
  name: IBM WebSphere Hosts API
  slug: websphere-hosts-api
- description: Log access and configuration
  name: IBM WebSphere Logging API
  slug: websphere-logging-api
- description: JMX MBean operations and attribute access
  name: IBM WebSphere MBeans API
  slug: websphere-mbeans-api
- description: Collective member management
  name: IBM WebSphere Members API
  slug: websphere-members-api
- description: Message operations - send and receive
  name: IBM WebSphere Messages API
  slug: websphere-messages-api
- description: MicroProfile Metrics API
  name: IBM WebSphere Metrics API
  slug: websphere-metrics-api
- description: Performance monitoring and health checks
  name: IBM WebSphere Monitoring API
  slug: websphere-monitoring-api
- description: Node management operations
  name: IBM WebSphere Nodes API
  slug: websphere-nodes-api
- description: Alert and notification management
  name: IBM WebSphere Notifications API
  slug: websphere-notifications-api
- description: MicroProfile OpenAPI documentation endpoints
  name: IBM WebSphere OpenAPI API
  slug: websphere-openapi-api
- description: Queue manager administration
  name: IBM WebSphere Queue Manager API
  slug: websphere-queue-manager-api
- description: Queue administration and management
  name: IBM WebSphere Queues API
  slug: websphere-queues-api
- description: Shared configuration repository management
  name: IBM WebSphere Repositories API
  slug: websphere-repositories-api
- description: Resource management including data sources and JMS
  name: IBM WebSphere Resources API
  slug: websphere-resources-api
- description: Scaling policy and auto-scaling management
  name: IBM WebSphere Scaling API
  slug: websphere-scaling-api
- description: Security configuration and management
  name: IBM WebSphere Security API
  slug: websphere-security-api
- description: Server runtime management
  name: IBM WebSphere Server API
  slug: websphere-server-api
- description: Server configuration and management
  name: IBM WebSphere Servers API
  slug: websphere-servers-api
- description: Subscription management
  name: IBM WebSphere Subscriptions API
  slug: websphere-subscriptions-api
- description: Topic administration for publish/subscribe
  name: IBM WebSphere Topics API
  slug: websphere-topics-api
- description: Security vulnerability tracking and remediation
  name: IBM WebSphere Vulnerabilities API
  slug: websphere-vulnerabilities-api
arazzos:
- description: Deploy an application archive, confirm it installed, and start it.
  name: WebSphere Deploy and Start Application
  slug: websphere-application-deploy-workflow
- description: Find a cluster, stop all its members, and start them again.
  name: WebSphere Cluster Controlled Restart
  slug: websphere-cluster-restart-workflow
- description: Find stopped collective members, inspect one, and start it.
  name: Liberty Collective Member Recovery
  slug: websphere-collective-member-recovery-workflow
- description: Find a JDBC data source, read its configuration, and test its connection.
  name: WebSphere Data Source Connectivity Check
  slug: websphere-datasource-connectivity-check-workflow
- description: Restart a Liberty application, capture a server dump, and verify health.
  name: Liberty Application Restart with Diagnostics
  slug: websphere-liberty-app-restart-diagnostic-workflow
- description: Read the Liberty server configuration, update it, and confirm the server runtime.
  name: Liberty Server Configuration Update
  slug: websphere-liberty-config-update-workflow
- description: Authenticate, confirm the target queue, send a message, and verify queue depth increased.
  name: IBM MQ Send Message and Verify Depth
  slug: websphere-mq-send-and-verify-workflow
- description: Find an application server, stop it, and start it again to apply pending changes.
  name: WebSphere Server Controlled Restart
  slug: websphere-server-restart-workflow
- description: Find an open critical vulnerability, inspect it, and apply a fix.
  name: WebSphere Automation Vulnerability Remediation
  slug: websphere-vulnerability-remediation-workflow
artifact_total: 480
collections:
- collection_type: postman
  name: Open Liberty APIs
  slug: postman-open-liberty-apis
- collection_type: postman
  name: WebSphere Application Server Admin REST API
  slug: postman-websphere-admin-rest-api
- collection_type: postman
  name: WebSphere Automation REST API
  slug: postman-websphere-automation-rest-api
- collection_type: postman
  name: WebSphere Liberty Admin REST API
  slug: postman-websphere-liberty-admin-rest-api
- collection_type: postman
  name: WebSphere Liberty Collective Controller REST API
  slug: postman-websphere-liberty-collective-controller-rest-api
- collection_type: postman
  name: WebSphere Liberty REST Connector API
  slug: postman-websphere-liberty-rest-connector-api
- collection_type: postman
  name: IBM MQ REST API
  slug: postman-websphere-mq-rest-api
- collection_type: open
  name: Open Liberty APIs
  slug: open-open-liberty-apis
- collection_type: open
  name: WebSphere Application Server Admin REST API
  slug: open-websphere-admin-rest-api
- collection_type: open
  name: WebSphere Automation REST API
  slug: open-websphere-automation-rest-api
- collection_type: open
  name: WebSphere Liberty Admin REST API
  slug: open-websphere-liberty-admin-rest-api
- collection_type: open
  name: WebSphere Liberty Collective Controller REST API
  slug: open-websphere-liberty-collective-controller-rest-api
- collection_type: open
  name: WebSphere Liberty REST Connector API
  slug: open-websphere-liberty-rest-connector-api
- collection_type: open
  name: IBM MQ REST API
  slug: open-websphere-mq-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/websphere-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/websphere-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/websphere-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/websphere-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ibm-websphere/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/websphere-application-deploy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/websphere-cluster-restart-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/websphere-collective-member-recovery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/websphere-datasource-connectivity-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/websphere-liberty-app-restart-diagnostic-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/websphere-liberty-config-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/websphere-mq-send-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/websphere-server-restart-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/websphere-vulnerability-remediation-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.ibm.com/wasdev/
- group: operate
  title: ''
  type: Support
  url: https://www.ibm.com/mysupport
- group: docs
  title: ''
  type: Documentation
  url: https://www.ibm.com/docs/en/was
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ibm.com/support/pages/websphere-liberty-developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.ibm.com/support/pages/recommended-updates-websphere-application-server
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ibm.com/products/websphere-hybrid-edition/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ibm.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ibm.com/us-en/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://cloud.ibm.com/status
- group: company
  title: ''
  type: Blog
  url: https://openliberty.io/blog/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/websphere
- group: start
  title: ''
  type: Signup
  url: https://cloud.ibm.com/registration
- group: start
  title: ''
  type: Console
  url: https://www.ibm.com/products/liberty
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WASdev
- group: build
  title: ''
  type: SDKs
  url: https://github.com/WASdev/sample.batch.bonuspayout
created: '2024-01-15'
description: IBM WebSphere is a family of enterprise software products that provide middleware and application server capabilities for building, deploying, and managing enterprise applications.
examples:
- key_count: 11
  name: Open Libertys Batch Job Execution Example
  slug: open-libertys-batch-job-execution-example
- key_count: 9
  name: Open Libertys Batch Job Instance Example
  slug: open-libertys-batch-job-instance-example
- key_count: 2
  name: Open Libertys Error Example
  slug: open-libertys-error-example
- key_count: 2
  name: Open Libertys Health Check Response Example
  slug: open-libertys-health-check-response-example
- key_count: 0
  name: Open Libertys Metrics Response Example
  slug: open-libertys-metrics-response-example
- key_count: 3
  name: Open Libertys Server Config Example
  slug: open-libertys-server-config-example
- key_count: 6
  name: Websphere Addclustermember Example
  slug: websphere-addclustermember-example
- key_count: 6
  name: Websphere Admin Rest Application Example
  slug: websphere-admin-rest-application-example
- key_count: 3
  name: Websphere Admin Rest Application Status Example
  slug: websphere-admin-rest-application-status-example
- key_count: 4
  name: Websphere Admin Rest Cluster Example
  slug: websphere-admin-rest-cluster-example
- key_count: 5
  name: Websphere Admin Rest Cluster Status Example
  slug: websphere-admin-rest-cluster-status-example
- key_count: 5
  name: Websphere Admin Rest Config Resource Example
  slug: websphere-admin-rest-config-resource-example
- key_count: 6
  name: Websphere Admin Rest Data Source Example
  slug: websphere-admin-rest-data-source-example
- key_count: 3
  name: Websphere Admin Rest Error Example
  slug: websphere-admin-rest-error-example
- key_count: 4
  name: Websphere Admin Rest Health Status Example
  slug: websphere-admin-rest-health-status-example
- key_count: 5
  name: Websphere Admin Rest Node Example
  slug: websphere-admin-rest-node-example
- key_count: 3
  name: Websphere Admin Rest Performance Data Example
  slug: websphere-admin-rest-performance-data-example
- key_count: 3
  name: Websphere Admin Rest Resource Type Example
  slug: websphere-admin-rest-resource-type-example
- key_count: 4
  name: Websphere Admin Rest Security Role Example
  slug: websphere-admin-rest-security-role-example
- key_count: 7
  name: Websphere Admin Rest Server Example
  slug: websphere-admin-rest-server-example
- key_count: 3
  name: Websphere Admin Rest Server Status Example
  slug: websphere-admin-rest-server-status-example
- key_count: 4
  name: Websphere Admin Rest User Example
  slug: websphere-admin-rest-user-example
- key_count: 6
  name: Websphere Applyfix Example
  slug: websphere-applyfix-example
- key_count: 5
  name: Websphere Automation Rest Compliance Report Example
  slug: websphere-automation-rest-compliance-report-example
- key_count: 2
  name: Websphere Automation Rest Error Example
  slug: websphere-automation-rest-error-example
- key_count: 9
  name: Websphere Automation Rest Fix Example
  slug: websphere-automation-rest-fix-example
- key_count: 11
  name: Websphere Automation Rest Managed Server Example
  slug: websphere-automation-rest-managed-server-example
- key_count: 8
  name: Websphere Automation Rest Notification Example
  slug: websphere-automation-rest-notification-example
- key_count: 7
  name: Websphere Automation Rest Overall Health Example
  slug: websphere-automation-rest-overall-health-example
- key_count: 9
  name: Websphere Automation Rest Server Health Example
  slug: websphere-automation-rest-server-health-example
- key_count: 10
  name: Websphere Automation Rest Vulnerability Example
  slug: websphere-automation-rest-vulnerability-example
- key_count: 6
  name: Websphere Browsemessages Example
  slug: websphere-browsemessages-example
- key_count: 6
  name: Websphere Createchannel Example
  slug: websphere-createchannel-example
- key_count: 6
  name: Websphere Createcluster Example
  slug: websphere-createcluster-example
- key_count: 6
  name: Websphere Createconfigelement Example
  slug: websphere-createconfigelement-example
- key_count: 6
  name: Websphere Createconfigresource Example
  slug: websphere-createconfigresource-example
- key_count: 6
  name: Websphere Createjavadump Example
  slug: websphere-createjavadump-example
- key_count: 6
  name: Websphere Createnotificationsubscription Example
  slug: websphere-createnotificationsubscription-example
- key_count: 6
  name: Websphere Createqueue Example
  slug: websphere-createqueue-example
- key_count: 6
  name: Websphere Createscalingpolicy Example
  slug: websphere-createscalingpolicy-example
- key_count: 6
  name: Websphere Createserverdump Example
  slug: websphere-createserverdump-example
- key_count: 6
  name: Websphere Createsharedconfig Example
  slug: websphere-createsharedconfig-example
- key_count: 6
  name: Websphere Createtopic Example
  slug: websphere-createtopic-example
- key_count: 6
  name: Websphere Deployapplication Example
  slug: websphere-deployapplication-example
- key_count: 6
  name: Websphere Downloadfile Example
  slug: websphere-downloadfile-example
- key_count: 6
  name: Websphere Getallmetrics Example
  slug: websphere-getallmetrics-example
- key_count: 6
  name: Websphere Getapiexplorer Example
  slug: websphere-getapiexplorer-example
- key_count: 6
  name: Websphere Getapplication Example
  slug: websphere-getapplication-example
- key_count: 6
  name: Websphere Getapplicationmetrics Example
  slug: websphere-getapplicationmetrics-example
- key_count: 6
  name: Websphere Getbasemetrics Example
  slug: websphere-getbasemetrics-example
- key_count: 6
  name: Websphere Getbatchjobexecution Example
  slug: websphere-getbatchjobexecution-example
- key_count: 6
  name: Websphere Getbatchjobinstance Example
  slug: websphere-getbatchjobinstance-example
- key_count: 6
  name: Websphere Getchannel Example
  slug: websphere-getchannel-example
- key_count: 6
  name: Websphere Getcluster Example
  slug: websphere-getcluster-example
- key_count: 6
  name: Websphere Getcompliancereport Example
  slug: websphere-getcompliancereport-example
- key_count: 6
  name: Websphere Getconfigelement Example
  slug: websphere-getconfigelement-example
- key_count: 6
  name: Websphere Getconfigelementbyid Example
  slug: websphere-getconfigelementbyid-example
- key_count: 6
  name: Websphere Getconfigresource Example
  slug: websphere-getconfigresource-example
- key_count: 6
  name: Websphere Getconfigresources Example
  slug: websphere-getconfigresources-example
- key_count: 6
  name: Websphere Getcontrollerinfo Example
  slug: websphere-getcontrollerinfo-example
- key_count: 6
  name: Websphere Getdatasource Example
  slug: websphere-getdatasource-example
- key_count: 6
  name: Websphere Getfeature Example
  slug: websphere-getfeature-example
- key_count: 6
  name: Websphere Getfix Example
  slug: websphere-getfix-example
- key_count: 6
  name: Websphere Gethealth Example
  slug: websphere-gethealth-example
- key_count: 6
  name: Websphere Gethealthstatus Example
  slug: websphere-gethealthstatus-example
- key_count: 6
  name: Websphere Gethost Example
  slug: websphere-gethost-example
- key_count: 6
  name: Websphere Getliveness Example
  slug: websphere-getliveness-example
- key_count: 6
  name: Websphere Getlogconfig Example
  slug: websphere-getlogconfig-example
- key_count: 6
  name: Websphere Getlogmessages Example
  slug: websphere-getlogmessages-example
- key_count: 6
  name: Websphere Getmanagedserver Example
  slug: websphere-getmanagedserver-example
- key_count: 6
  name: Websphere Getmbeanattribute Example
  slug: websphere-getmbeanattribute-example
- key_count: 6
  name: Websphere Getmbeanattributes Example
  slug: websphere-getmbeanattributes-example
- key_count: 6
  name: Websphere Getmbeaninfo Example
  slug: websphere-getmbeaninfo-example
- key_count: 6
  name: Websphere Getmember Example
  slug: websphere-getmember-example
- key_count: 6
  name: Websphere Getmetrics Example
  slug: websphere-getmetrics-example
- key_count: 6
  name: Websphere Getnode Example
  slug: websphere-getnode-example
- key_count: 6
  name: Websphere Getnotifications Example
  slug: websphere-getnotifications-example
- key_count: 6
  name: Websphere Getopenapidocument Example
  slug: websphere-getopenapidocument-example
- key_count: 6
  name: Websphere Getopenapiui Example
  slug: websphere-getopenapiui-example
- key_count: 6
  name: Websphere Getoverallhealth Example
  slug: websphere-getoverallhealth-example
- key_count: 6
  name: Websphere Getperformancedata Example
  slug: websphere-getperformancedata-example
- key_count: 6
  name: Websphere Getqueue Example
  slug: websphere-getqueue-example
- key_count: 6
  name: Websphere Getqueuemanager Example
  slug: websphere-getqueuemanager-example
- key_count: 6
  name: Websphere Getreadiness Example
  slug: websphere-getreadiness-example
- key_count: 6
  name: Websphere Getscalingpolicy Example
  slug: websphere-getscalingpolicy-example
- key_count: 6
  name: Websphere Getserver Example
  slug: websphere-getserver-example
- key_count: 6
  name: Websphere Getserverconfig Example
  slug: websphere-getserverconfig-example
- key_count: 6
  name: Websphere Getserverhealth Example
  slug: websphere-getserverhealth-example
- key_count: 6
  name: Websphere Getserverinfo Example
  slug: websphere-getserverinfo-example
- key_count: 6
  name: Websphere Getstarted Example
  slug: websphere-getstarted-example
- key_count: 6
  name: Websphere Getsubscription Example
  slug: websphere-getsubscription-example
- key_count: 6
  name: Websphere Gettopic Example
  slug: websphere-gettopic-example
- key_count: 6
  name: Websphere Getvendormetrics Example
  slug: websphere-getvendormetrics-example
- key_count: 6
  name: Websphere Getvulnerability Example
  slug: websphere-getvulnerability-example
- key_count: 6
  name: Websphere Invokembeanoperation Example
  slug: websphere-invokembeanoperation-example
- key_count: 2
  name: Websphere Liberty Admin Rest Config Element Example
  slug: websphere-liberty-admin-rest-config-element-example
- key_count: 3
  name: Websphere Liberty Admin Rest Error Example
  slug: websphere-liberty-admin-rest-error-example
- key_count: 6
  name: Websphere Liberty Admin Rest Feature Example
  slug: websphere-liberty-admin-rest-feature-example
- key_count: 2
  name: Websphere Liberty Admin Rest Health Check Example
  slug: websphere-liberty-admin-rest-health-check-example
- key_count: 6
  name: Websphere Liberty Admin Rest Liberty Application Example
  slug: websphere-liberty-admin-rest-liberty-application-example
- key_count: 3
  name: Websphere Liberty Admin Rest Liberty Application Status Example
  slug: websphere-liberty-admin-rest-liberty-application-status-example
- key_count: 9
  name: Websphere Liberty Admin Rest Liberty Server Example
  slug: websphere-liberty-admin-rest-liberty-server-example
- key_count: 6
  name: Websphere Liberty Admin Rest Log Message Example
  slug: websphere-liberty-admin-rest-log-message-example
- key_count: 7
  name: Websphere Liberty Admin Rest Logging Config Example
  slug: websphere-liberty-admin-rest-logging-config-example
- key_count: 2
  name: Websphere Liberty Admin Rest Metrics Example
  slug: websphere-liberty-admin-rest-metrics-example
- key_count: 4
  name: Websphere Liberty Admin Rest Server Config Example
  slug: websphere-liberty-admin-rest-server-config-example
- key_count: 4
  name: Websphere Liberty Collective Controller Rest Cluster Status Example
  slug: websphere-liberty-collective-controller-rest-cluster-status-example
- key_count: 5
  name: Websphere Liberty Collective Controller Rest Collective Cluster Example
  slug: websphere-liberty-collective-controller-rest-collective-cluster-example
- key_count: 8
  name: Websphere Liberty Collective Controller Rest Collective Member Example
  slug: websphere-liberty-collective-controller-rest-collective-member-example
- key_count: 7
  name: Websphere Liberty Collective Controller Rest Controller Info Example
  slug: websphere-liberty-collective-controller-rest-controller-info-example
- key_count: 2
  name: Websphere Liberty Collective Controller Rest Error Example
  slug: websphere-liberty-collective-controller-rest-error-example
- key_count: 5
  name: Websphere Liberty Collective Controller Rest Host Example
  slug: websphere-liberty-collective-controller-rest-host-example
- key_count: 3
  name: Websphere Liberty Collective Controller Rest Member Status Example
  slug: websphere-liberty-collective-controller-rest-member-status-example
- key_count: 8
  name: Websphere Liberty Collective Controller Rest Scaling Policy Example
  slug: websphere-liberty-collective-controller-rest-scaling-policy-example
- key_count: 4
  name: Websphere Liberty Collective Controller Rest Shared Config Example
  slug: websphere-liberty-collective-controller-rest-shared-config-example
- key_count: 3
  name: Websphere Liberty Rest Connector Attribute Value Example
  slug: websphere-liberty-rest-connector-attribute-value-example
- key_count: 2
  name: Websphere Liberty Rest Connector Error Example
  slug: websphere-liberty-rest-connector-error-example
- key_count: 6
  name: Websphere Liberty Rest Connector M Bean Detail Example
  slug: websphere-liberty-rest-connector-m-bean-detail-example
- key_count: 4
  name: Websphere Liberty Rest Connector M Bean Info Example
  slug: websphere-liberty-rest-connector-m-bean-info-example
- key_count: 6
  name: Websphere Liberty Rest Connector Notification Example
  slug: websphere-liberty-rest-connector-notification-example
- key_count: 4
  name: Websphere Liberty Rest Connector Notification Subscription Example
  slug: websphere-liberty-rest-connector-notification-subscription-example
- key_count: 6
  name: Websphere Listapplications Example
  slug: websphere-listapplications-example
- key_count: 6
  name: Websphere Listbatchjobexecutions Example
  slug: websphere-listbatchjobexecutions-example
- key_count: 6
  name: Websphere Listbatchjobinstances Example
  slug: websphere-listbatchjobinstances-example
- key_count: 6
  name: Websphere Listchannels Example
  slug: websphere-listchannels-example
- key_count: 6
  name: Websphere Listclustermembers Example
  slug: websphere-listclustermembers-example
- key_count: 6
  name: Websphere Listclusters Example
  slug: websphere-listclusters-example
- key_count: 6
  name: Websphere Listcompliancereports Example
  slug: websphere-listcompliancereports-example
- key_count: 6
  name: Websphere Listconfigresources Example
  slug: websphere-listconfigresources-example
- key_count: 6
  name: Websphere Listdatasources Example
  slug: websphere-listdatasources-example
- key_count: 6
  name: Websphere Listfeatures Example
  slug: websphere-listfeatures-example
- key_count: 6
  name: Websphere Listfixes Example
  slug: websphere-listfixes-example
- key_count: 6
  name: Websphere Listhosts Example
  slug: websphere-listhosts-example
- key_count: 6
  name: Websphere Listmanagedservers Example
  slug: websphere-listmanagedservers-example
- key_count: 6
  name: Websphere Listmbeans Example
  slug: websphere-listmbeans-example
- key_count: 6
  name: Websphere Listmembers Example
  slug: websphere-listmembers-example
- key_count: 6
  name: Websphere Listnodes Example
  slug: websphere-listnodes-example
- key_count: 6
  name: Websphere Listnotifications Example
  slug: websphere-listnotifications-example
- key_count: 6
  name: Websphere Listnotificationsubscriptions Example
  slug: websphere-listnotificationsubscriptions-example
- key_count: 6
  name: Websphere Listqueuemanagers Example
  slug: websphere-listqueuemanagers-example
- key_count: 6
  name: Websphere Listqueues Example
  slug: websphere-listqueues-example
- key_count: 6
  name: Websphere Listroles Example
  slug: websphere-listroles-example
- key_count: 6
  name: Websphere Listscalingpolicies Example
  slug: websphere-listscalingpolicies-example
- key_count: 6
  name: Websphere Listservers Example
  slug: websphere-listservers-example
- key_count: 6
  name: Websphere Listsharedconfigs Example
  slug: websphere-listsharedconfigs-example
- key_count: 6
  name: Websphere Listsubscriptions Example
  slug: websphere-listsubscriptions-example
- key_count: 6
  name: Websphere Listtopics Example
  slug: websphere-listtopics-example
- key_count: 6
  name: Websphere Listusers Example
  slug: websphere-listusers-example
- key_count: 6
  name: Websphere Listvulnerabilities Example
  slug: websphere-listvulnerabilities-example
- key_count: 6
  name: Websphere Login Example
  slug: websphere-login-example
- key_count: 5
  name: Websphere Mq Rest Channel Create Example
  slug: websphere-mq-rest-channel-create-example
- key_count: 6
  name: Websphere Mq Rest Channel Example
  slug: websphere-mq-rest-channel-example
- key_count: 1
  name: Websphere Mq Rest Error Example
  slug: websphere-mq-rest-error-example
- key_count: 9
  name: Websphere Mq Rest Message Example
  slug: websphere-mq-rest-message-example
- key_count: 6
  name: Websphere Mq Rest Queue Create Example
  slug: websphere-mq-rest-queue-create-example
- key_count: 11
  name: Websphere Mq Rest Queue Example
  slug: websphere-mq-rest-queue-example
- key_count: 8
  name: Websphere Mq Rest Queue Manager Example
  slug: websphere-mq-rest-queue-manager-example
- key_count: 5
  name: Websphere Mq Rest Queue Update Example
  slug: websphere-mq-rest-queue-update-example
- key_count: 6
  name: Websphere Mq Rest Subscription Example
  slug: websphere-mq-rest-subscription-example
- key_count: 4
  name: Websphere Mq Rest Topic Create Example
  slug: websphere-mq-rest-topic-create-example
- key_count: 7
  name: Websphere Mq Rest Topic Example
  slug: websphere-mq-rest-topic-example
- key_count: 6
  name: Websphere Publishmessage Example
  slug: websphere-publishmessage-example
- key_count: 6
  name: Websphere Receivemessage Example
  slug: websphere-receivemessage-example
- key_count: 6
  name: Websphere Registerserver Example
  slug: websphere-registerserver-example
- key_count: 6
  name: Websphere Resolvevulnerability Example
  slug: websphere-resolvevulnerability-example
- key_count: 6
  name: Websphere Restartapplication Example
  slug: websphere-restartapplication-example
- key_count: 6
  name: Websphere Restartbatchjobexecution Example
  slug: websphere-restartbatchjobexecution-example
- key_count: 6
  name: Websphere Sendmessage Example
  slug: websphere-sendmessage-example
- key_count: 6
  name: Websphere Setmbeanattribute Example
  slug: websphere-setmbeanattribute-example
- key_count: 6
  name: Websphere Startapplication Example
  slug: websphere-startapplication-example
- key_count: 6
  name: Websphere Startcluster Example
  slug: websphere-startcluster-example
- key_count: 6
  name: Websphere Startmember Example
  slug: websphere-startmember-example
- key_count: 6
  name: Websphere Startserver Example
  slug: websphere-startserver-example
- key_count: 6
  name: Websphere Stopapplication Example
  slug: websphere-stopapplication-example
- key_count: 6
  name: Websphere Stopbatchjobexecution Example
  slug: websphere-stopbatchjobexecution-example
- key_count: 6
  name: Websphere Stopcluster Example
  slug: websphere-stopcluster-example
- key_count: 6
  name: Websphere Stopmember Example
  slug: websphere-stopmember-example
- key_count: 6
  name: Websphere Stopserver Example
  slug: websphere-stopserver-example
- key_count: 6
  name: Websphere Syncnode Example
  slug: websphere-syncnode-example
- key_count: 6
  name: Websphere Testdatasourceconnection Example
  slug: websphere-testdatasourceconnection-example
- key_count: 6
  name: Websphere Transferfiles Example
  slug: websphere-transferfiles-example
- key_count: 6
  name: Websphere Updateapplication Example
  slug: websphere-updateapplication-example
- key_count: 6
  name: Websphere Updateconfigelement Example
  slug: websphere-updateconfigelement-example
- key_count: 6
  name: Websphere Updateconfigresource Example
  slug: websphere-updateconfigresource-example
- key_count: 6
  name: Websphere Updatelogconfig Example
  slug: websphere-updatelogconfig-example
- key_count: 6
  name: Websphere Updatequeue Example
  slug: websphere-updatequeue-example
- key_count: 6
  name: Websphere Updatescalingpolicy Example
  slug: websphere-updatescalingpolicy-example
- key_count: 6
  name: Websphere Updateserverconfig Example
  slug: websphere-updateserverconfig-example
- key_count: 6
  name: Websphere Uploadfile Example
  slug: websphere-uploadfile-example
features:
- Enterprise Java Application Hosting
- Cloud-Native Deployment with Liberty
- Centralized Server Management
- Auto-Scaling and Clustering
- JMX Remote Administration
- IBM MQ Integration
- Automated Vulnerability Patching
- Jakarta EE and MicroProfile Support
finops:
- name: Websphere Finops
  service_category: Application Server / Middleware
  slug: websphere-finops
image: https://www.ibm.com/brand/experience-guides/developer/b1db1ae501d522a1a4b49613fe07c9f4/01_8-bar-positive.svg
integrations:
- IBM MQ
- IBM Cloud
- OpenShift Container Platform
- Jenkins CI/CD
- IBM Db2
- Oracle Database
- LDAP / Active Directory
- Prometheus and Grafana
json_schemas:
- name: WebSphere Application
  property_count: 19
  slug: application
- name: WebSphere Cluster
  property_count: 18
  slug: cluster
- name: IBM MQ Message Queue
  property_count: 25
  slug: message-queue
- name: BatchJobExecution
  property_count: 11
  slug: open-libertys-batch-job-execution
- name: BatchJobInstance
  property_count: 9
  slug: open-libertys-batch-job-instance
- name: Error
  property_count: 2
  slug: open-libertys-error
- name: HealthCheckResponse
  property_count: 2
  slug: open-libertys-health-check-response
- name: MetricsResponse
  property_count: 0
  slug: open-libertys-metrics-response
- name: ServerConfig
  property_count: 3
  slug: open-libertys-server-config
- name: WebSphere Server
  property_count: 25
  slug: server
- name: Application
  property_count: 6
  slug: websphere-admin-rest-application
- name: ApplicationStatus
  property_count: 3
  slug: websphere-admin-rest-application-status
- name: Cluster
  property_count: 4
  slug: websphere-admin-rest-cluster
- name: ClusterStatus
  property_count: 5
  slug: websphere-admin-rest-cluster-status
- name: ConfigResource
  property_count: 5
  slug: websphere-admin-rest-config-resource
- name: DataSource
  property_count: 6
  slug: websphere-admin-rest-data-source
- name: Error
  property_count: 3
  slug: websphere-admin-rest-error
- name: HealthStatus
  property_count: 4
  slug: websphere-admin-rest-health-status
- name: Node
  property_count: 5
  slug: websphere-admin-rest-node
- name: PerformanceData
  property_count: 3
  slug: websphere-admin-rest-performance-data
- name: ResourceType
  property_count: 3
  slug: websphere-admin-rest-resource-type
- name: SecurityRole
  property_count: 4
  slug: websphere-admin-rest-security-role
- name: Server
  property_count: 7
  slug: websphere-admin-rest-server
- name: ServerStatus
  property_count: 3
  slug: websphere-admin-rest-server-status
- name: User
  property_count: 4
  slug: websphere-admin-rest-user
- name: Application
  property_count: 6
  slug: websphere-application
- name: ApplicationStatus
  property_count: 3
  slug: websphere-applicationstatus
- name: AttributeValue
  property_count: 3
  slug: websphere-attributevalue
- name: ComplianceReport
  property_count: 5
  slug: websphere-automation-rest-compliance-report
- name: Error
  property_count: 2
  slug: websphere-automation-rest-error
- name: Fix
  property_count: 9
  slug: websphere-automation-rest-fix
- name: ManagedServer
  property_count: 11
  slug: websphere-automation-rest-managed-server
- name: Notification
  property_count: 8
  slug: websphere-automation-rest-notification
- name: OverallHealth
  property_count: 7
  slug: websphere-automation-rest-overall-health
- name: ServerHealth
  property_count: 9
  slug: websphere-automation-rest-server-health
- name: Vulnerability
  property_count: 10
  slug: websphere-automation-rest-vulnerability
- name: BatchJobExecution
  property_count: 11
  slug: websphere-batchjobexecution
- name: BatchJobInstance
  property_count: 9
  slug: websphere-batchjobinstance
- name: Channel
  property_count: 6
  slug: websphere-channel
- name: ChannelCreate
  property_count: 5
  slug: websphere-channelcreate
- name: Cluster
  property_count: 4
  slug: websphere-cluster
- name: ClusterStatus
  property_count: 5
  slug: websphere-clusterstatus
- name: CollectiveCluster
  property_count: 5
  slug: websphere-collectivecluster
- name: CollectiveMember
  property_count: 8
  slug: websphere-collectivemember
- name: ComplianceReport
  property_count: 5
  slug: websphere-compliancereport
- name: ConfigElement
  property_count: 2
  slug: websphere-configelement
- name: ConfigResource
  property_count: 5
  slug: websphere-configresource
- name: ControllerInfo
  property_count: 7
  slug: websphere-controllerinfo
- name: DataSource
  property_count: 6
  slug: websphere-datasource
- name: Error
  property_count: 2
  slug: websphere-error
- name: Feature
  property_count: 6
  slug: websphere-feature
- name: Fix
  property_count: 9
  slug: websphere-fix
- name: HealthCheck
  property_count: 2
  slug: websphere-healthcheck
- name: HealthCheckResponse
  property_count: 2
  slug: websphere-healthcheckresponse
- name: HealthStatus
  property_count: 4
  slug: websphere-healthstatus
- name: Host
  property_count: 5
  slug: websphere-host
- name: ConfigElement
  property_count: 2
  slug: websphere-liberty-admin-rest-config-element
- name: Error
  property_count: 3
  slug: websphere-liberty-admin-rest-error
- name: Feature
  property_count: 6
  slug: websphere-liberty-admin-rest-feature
- name: HealthCheck
  property_count: 2
  slug: websphere-liberty-admin-rest-health-check
- name: LibertyApplication
  property_count: 6
  slug: websphere-liberty-admin-rest-liberty-application
- name: LibertyApplicationStatus
  property_count: 3
  slug: websphere-liberty-admin-rest-liberty-application-status
- name: LibertyServer
  property_count: 9
  slug: websphere-liberty-admin-rest-liberty-server
- name: LogMessage
  property_count: 6
  slug: websphere-liberty-admin-rest-log-message
- name: LoggingConfig
  property_count: 7
  slug: websphere-liberty-admin-rest-logging-config
- name: Metrics
  property_count: 2
  slug: websphere-liberty-admin-rest-metrics
- name: ServerConfig
  property_count: 4
  slug: websphere-liberty-admin-rest-server-config
- name: ClusterStatus
  property_count: 4
  slug: websphere-liberty-collective-controller-rest-cluster-status
- name: CollectiveCluster
  property_count: 5
  slug: websphere-liberty-collective-controller-rest-collective-cluster
- name: CollectiveMember
  property_count: 8
  slug: websphere-liberty-collective-controller-rest-collective-member
- name: ControllerInfo
  property_count: 7
  slug: websphere-liberty-collective-controller-rest-controller-info
- name: Error
  property_count: 2
  slug: websphere-liberty-collective-controller-rest-error
- name: Host
  property_count: 5
  slug: websphere-liberty-collective-controller-rest-host
- name: MemberStatus
  property_count: 3
  slug: websphere-liberty-collective-controller-rest-member-status
- name: ScalingPolicy
  property_count: 8
  slug: websphere-liberty-collective-controller-rest-scaling-policy
- name: SharedConfig
  property_count: 4
  slug: websphere-liberty-collective-controller-rest-shared-config
- name: AttributeValue
  property_count: 3
  slug: websphere-liberty-rest-connector-attribute-value
- name: Error
  property_count: 2
  slug: websphere-liberty-rest-connector-error
- name: MBeanDetail
  property_count: 6
  slug: websphere-liberty-rest-connector-m-bean-detail
- name: MBeanInfo
  property_count: 4
  slug: websphere-liberty-rest-connector-m-bean-info
- name: Notification
  property_count: 6
  slug: websphere-liberty-rest-connector-notification
- name: NotificationSubscription
  property_count: 4
  slug: websphere-liberty-rest-connector-notification-subscription
- name: LibertyApplication
  property_count: 6
  slug: websphere-libertyapplication
- name: LibertyApplicationStatus
  property_count: 3
  slug: websphere-libertyapplicationstatus
- name: LibertyServer
  property_count: 9
  slug: websphere-libertyserver
- name: LoggingConfig
  property_count: 7
  slug: websphere-loggingconfig
- name: LogMessage
  property_count: 6
  slug: websphere-logmessage
- name: ManagedServer
  property_count: 11
  slug: websphere-managedserver
- name: MBeanDetail
  property_count: 6
  slug: websphere-mbeandetail
- name: MBeanInfo
  property_count: 4
  slug: websphere-mbeaninfo
- name: MemberStatus
  property_count: 3
  slug: websphere-memberstatus
- name: Message
  property_count: 9
  slug: websphere-message
- name: Metrics
  property_count: 2
  slug: websphere-metrics
- name: MetricsResponse
  property_count: 0
  slug: websphere-metricsresponse
- name: ChannelCreate
  property_count: 5
  slug: websphere-mq-rest-channel-create
- name: Channel
  property_count: 6
  slug: websphere-mq-rest-channel
- name: Error
  property_count: 1
  slug: websphere-mq-rest-error
- name: Message
  property_count: 9
  slug: websphere-mq-rest-message
- name: QueueCreate
  property_count: 6
  slug: websphere-mq-rest-queue-create
- name: QueueManager
  property_count: 8
  slug: websphere-mq-rest-queue-manager
- name: Queue
  property_count: 11
  slug: websphere-mq-rest-queue
- name: QueueUpdate
  property_count: 5
  slug: websphere-mq-rest-queue-update
- name: Subscription
  property_count: 6
  slug: websphere-mq-rest-subscription
- name: TopicCreate
  property_count: 4
  slug: websphere-mq-rest-topic-create
- name: Topic
  property_count: 7
  slug: websphere-mq-rest-topic
- name: Node
  property_count: 5
  slug: websphere-node
- name: Notification
  property_count: 8
  slug: websphere-notification
- name: NotificationSubscription
  property_count: 4
  slug: websphere-notificationsubscription
- name: OverallHealth
  property_count: 7
  slug: websphere-overallhealth
- name: PerformanceData
  property_count: 3
  slug: websphere-performancedata
- name: Queue
  property_count: 11
  slug: websphere-queue
- name: QueueCreate
  property_count: 6
  slug: websphere-queuecreate
- name: QueueManager
  property_count: 8
  slug: websphere-queuemanager
- name: QueueUpdate
  property_count: 5
  slug: websphere-queueupdate
- name: ResourceType
  property_count: 3
  slug: websphere-resourcetype
- name: ScalingPolicy
  property_count: 8
  slug: websphere-scalingpolicy
- name: SecurityRole
  property_count: 4
  slug: websphere-securityrole
- name: Server
  property_count: 7
  slug: websphere-server
- name: ServerConfig
  property_count: 3
  slug: websphere-serverconfig
- name: ServerHealth
  property_count: 9
  slug: websphere-serverhealth
- name: ServerStatus
  property_count: 3
  slug: websphere-serverstatus
- name: SharedConfig
  property_count: 4
  slug: websphere-sharedconfig
- name: Subscription
  property_count: 6
  slug: websphere-subscription
- name: Topic
  property_count: 7
  slug: websphere-topic
- name: TopicCreate
  property_count: 4
  slug: websphere-topiccreate
- name: User
  property_count: 4
  slug: websphere-user
- name: Vulnerability
  property_count: 10
  slug: websphere-vulnerability
json_structures:
- name: Open Libertys Batch Job Execution Structure
  property_count: 11
  slug: open-libertys-batch-job-execution-structure
- name: Open Libertys Batch Job Instance Structure
  property_count: 9
  slug: open-libertys-batch-job-instance-structure
- name: Open Libertys Error Structure
  property_count: 2
  slug: open-libertys-error-structure
- name: Open Libertys Health Check Response Structure
  property_count: 2
  slug: open-libertys-health-check-response-structure
- name: Open Libertys Metrics Response Structure
  property_count: 0
  slug: open-libertys-metrics-response-structure
- name: Open Libertys Server Config Structure
  property_count: 3
  slug: open-libertys-server-config-structure
- name: Websphere Admin Rest Application Status Structure
  property_count: 3
  slug: websphere-admin-rest-application-status-structure
- name: Websphere Admin Rest Application Structure
  property_count: 6
  slug: websphere-admin-rest-application-structure
- name: Websphere Admin Rest Cluster Status Structure
  property_count: 5
  slug: websphere-admin-rest-cluster-status-structure
- name: Websphere Admin Rest Cluster Structure
  property_count: 4
  slug: websphere-admin-rest-cluster-structure
- name: Websphere Admin Rest Config Resource Structure
  property_count: 5
  slug: websphere-admin-rest-config-resource-structure
- name: Websphere Admin Rest Data Source Structure
  property_count: 6
  slug: websphere-admin-rest-data-source-structure
- name: Websphere Admin Rest Error Structure
  property_count: 3
  slug: websphere-admin-rest-error-structure
- name: Websphere Admin Rest Health Status Structure
  property_count: 4
  slug: websphere-admin-rest-health-status-structure
- name: Websphere Admin Rest Node Structure
  property_count: 5
  slug: websphere-admin-rest-node-structure
- name: Websphere Admin Rest Performance Data Structure
  property_count: 3
  slug: websphere-admin-rest-performance-data-structure
- name: Websphere Admin Rest Resource Type Structure
  property_count: 3
  slug: websphere-admin-rest-resource-type-structure
- name: Websphere Admin Rest Security Role Structure
  property_count: 4
  slug: websphere-admin-rest-security-role-structure
- name: Websphere Admin Rest Server Status Structure
  property_count: 3
  slug: websphere-admin-rest-server-status-structure
- name: Websphere Admin Rest Server Structure
  property_count: 7
  slug: websphere-admin-rest-server-structure
- name: Websphere Admin Rest User Structure
  property_count: 4
  slug: websphere-admin-rest-user-structure
- name: Websphere Automation Rest Compliance Report Structure
  property_count: 5
  slug: websphere-automation-rest-compliance-report-structure
- name: Websphere Automation Rest Error Structure
  property_count: 2
  slug: websphere-automation-rest-error-structure
- name: Websphere Automation Rest Fix Structure
  property_count: 9
  slug: websphere-automation-rest-fix-structure
- name: Websphere Automation Rest Managed Server Structure
  property_count: 11
  slug: websphere-automation-rest-managed-server-structure
- name: Websphere Automation Rest Notification Structure
  property_count: 8
  slug: websphere-automation-rest-notification-structure
- name: Websphere Automation Rest Overall Health Structure
  property_count: 7
  slug: websphere-automation-rest-overall-health-structure
- name: Websphere Automation Rest Server Health Structure
  property_count: 9
  slug: websphere-automation-rest-server-health-structure
- name: Websphere Automation Rest Vulnerability Structure
  property_count: 10
  slug: websphere-automation-rest-vulnerability-structure
- name: Websphere Liberty Admin Rest Config Element Structure
  property_count: 2
  slug: websphere-liberty-admin-rest-config-element-structure
- name: Websphere Liberty Admin Rest Error Structure
  property_count: 3
  slug: websphere-liberty-admin-rest-error-structure
- name: Websphere Liberty Admin Rest Feature Structure
  property_count: 6
  slug: websphere-liberty-admin-rest-feature-structure
- name: Websphere Liberty Admin Rest Health Check Structure
  property_count: 2
  slug: websphere-liberty-admin-rest-health-check-structure
- name: Websphere Liberty Admin Rest Liberty Application Status Structure
  property_count: 3
  slug: websphere-liberty-admin-rest-liberty-application-status-structure
- name: Websphere Liberty Admin Rest Liberty Application Structure
  property_count: 6
  slug: websphere-liberty-admin-rest-liberty-application-structure
- name: Websphere Liberty Admin Rest Liberty Server Structure
  property_count: 9
  slug: websphere-liberty-admin-rest-liberty-server-structure
- name: Websphere Liberty Admin Rest Log Message Structure
  property_count: 6
  slug: websphere-liberty-admin-rest-log-message-structure
- name: Websphere Liberty Admin Rest Logging Config Structure
  property_count: 7
  slug: websphere-liberty-admin-rest-logging-config-structure
- name: Websphere Liberty Admin Rest Metrics Structure
  property_count: 2
  slug: websphere-liberty-admin-rest-metrics-structure
- name: Websphere Liberty Admin Rest Server Config Structure
  property_count: 4
  slug: websphere-liberty-admin-rest-server-config-structure
- name: Websphere Liberty Collective Controller Rest Cluster Status Structure
  property_count: 4
  slug: websphere-liberty-collective-controller-rest-cluster-status-structure
- name: Websphere Liberty Collective Controller Rest Collective Cluster Structure
  property_count: 5
  slug: websphere-liberty-collective-controller-rest-collective-cluster-structure
- name: Websphere Liberty Collective Controller Rest Collective Member Structure
  property_count: 8
  slug: websphere-liberty-collective-controller-rest-collective-member-structure
- name: Websphere Liberty Collective Controller Rest Controller Info Structure
  property_count: 7
  slug: websphere-liberty-collective-controller-rest-controller-info-structure
- name: Websphere Liberty Collective Controller Rest Error Structure
  property_count: 2
  slug: websphere-liberty-collective-controller-rest-error-structure
- name: Websphere Liberty Collective Controller Rest Host Structure
  property_count: 5
  slug: websphere-liberty-collective-controller-rest-host-structure
- name: Websphere Liberty Collective Controller Rest Member Status Structure
  property_count: 3
  slug: websphere-liberty-collective-controller-rest-member-status-structure
- name: Websphere Liberty Collective Controller Rest Scaling Policy Structure
  property_count: 8
  slug: websphere-liberty-collective-controller-rest-scaling-policy-structure
- name: Websphere Liberty Collective Controller Rest Shared Config Structure
  property_count: 4
  slug: websphere-liberty-collective-controller-rest-shared-config-structure
- name: Websphere Liberty Rest Connector Attribute Value Structure
  property_count: 3
  slug: websphere-liberty-rest-connector-attribute-value-structure
- name: Websphere Liberty Rest Connector Error Structure
  property_count: 2
  slug: websphere-liberty-rest-connector-error-structure
- name: Websphere Liberty Rest Connector M Bean Detail Structure
  property_count: 6
  slug: websphere-liberty-rest-connector-m-bean-detail-structure
- name: Websphere Liberty Rest Connector M Bean Info Structure
  property_count: 4
  slug: websphere-liberty-rest-connector-m-bean-info-structure
- name: Websphere Liberty Rest Connector Notification Structure
  property_count: 6
  slug: websphere-liberty-rest-connector-notification-structure
- name: Websphere Liberty Rest Connector Notification Subscription Structure
  property_count: 4
  slug: websphere-liberty-rest-connector-notification-subscription-structure
- name: Websphere Mq Rest Channel Create Structure
  property_count: 5
  slug: websphere-mq-rest-channel-create-structure
- name: Websphere Mq Rest Channel Structure
  property_count: 6
  slug: websphere-mq-rest-channel-structure
- name: Websphere Mq Rest Error Structure
  property_count: 1
  slug: websphere-mq-rest-error-structure
- name: Websphere Mq Rest Message Structure
  property_count: 9
  slug: websphere-mq-rest-message-structure
- name: Websphere Mq Rest Queue Create Structure
  property_count: 6
  slug: websphere-mq-rest-queue-create-structure
- name: Websphere Mq Rest Queue Manager Structure
  property_count: 8
  slug: websphere-mq-rest-queue-manager-structure
- name: Websphere Mq Rest Queue Structure
  property_count: 11
  slug: websphere-mq-rest-queue-structure
- name: Websphere Mq Rest Queue Update Structure
  property_count: 5
  slug: websphere-mq-rest-queue-update-structure
- name: Websphere Mq Rest Subscription Structure
  property_count: 6
  slug: websphere-mq-rest-subscription-structure
- name: Websphere Mq Rest Topic Create Structure
  property_count: 4
  slug: websphere-mq-rest-topic-create-structure
- name: Websphere Mq Rest Topic Structure
  property_count: 7
  slug: websphere-mq-rest-topic-structure
- name: Websphere Structure
  property_count: 0
  slug: websphere-structure
jsonld:
- class_count: 3
  name: context Context
  property_count: 11
  slug: context
- class_count: 0
  name: Open Libertys Context
  property_count: 0
  slug: open-libertys-context
- class_count: 0
  name: Websphere Admin Rest Context
  property_count: 0
  slug: websphere-admin-rest-context
- class_count: 0
  name: Websphere Automation Rest Context
  property_count: 0
  slug: websphere-automation-rest-context
- class_count: 0
  name: Websphere Liberty Admin Rest Context
  property_count: 0
  slug: websphere-liberty-admin-rest-context
- class_count: 0
  name: Websphere Liberty Collective Controller Rest Context
  property_count: 0
  slug: websphere-liberty-collective-controller-rest-context
- class_count: 0
  name: Websphere Liberty Rest Connector Context
  property_count: 0
  slug: websphere-liberty-rest-connector-context
- class_count: 0
  name: Websphere Mq Rest Context
  property_count: 0
  slug: websphere-mq-rest-context
layout: provider
modified: '2026-05-19'
name: IBM WebSphere
nav: Providers
network: true
overview: 'IBM WebSphere publishes 34 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Authentication API, Batch API, and 31 more. Tagged areas include Application Server, Cloud Native, Enterprise Java, J2EE, and Microservices.


  The IBM WebSphere catalog on APIs.io includes 8 JSON-LD contexts and 2 Spectral governance rulesets.


  IBM WebSphere''s developer surface includes authentication, developer portal, support, documentation, getting-started guide, changelog, pricing, and 22 more developer resources.'
plans:
- name: Websphere Plans Pricing
  plan_count: 1
  slug: websphere-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 1
  name: Websphere Rate Limits
  slug: websphere-rate-limits
rules:
- name: IBM WebSphere API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: websphere-jsonschema-spectral-rules
- name: IBM WebSphere API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 8
  slug: websphere-spectral-rules
score:
  band: strong
  composite: 59.8
  delta: -3.3
  facets:
    commercial_clarity: 57.9
    contract_quality: 72.8
    developer_ergonomics: 63.0
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 63.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 34
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/websphere/refs/heads/main/screenshots/websphere-2026-06-20T201348.png
security:
- kind: authentication
  name: Websphere Authentication
  slug: websphere-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Websphere Domain Security
  slug: websphere-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Websphere Vulnerability Disclosure
  slug: websphere-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: websphere
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
use_cases:
- Enterprise Application Hosting and Deployment
- Microservices Architecture with Liberty
- Message-Driven Integration with IBM MQ
- Automated Compliance and Security Patching
- Batch Processing and Job Management
- Centralized Multi-Server Administration
website: https://developer.ibm.com/wasdev/
---
