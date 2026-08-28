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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 137
  human_in_the_loop: 7
  name: Oracle Goldengate Agentic Access
  operation_count: 281
  slug: oracle-goldengate-agentic-access
  summary_line: 281 operations · 137 acting · 7 human-in-the-loop
api_count: 37
apis:
- description: Import and export GGSA artifacts
  name: Oracle GoldenGate Artifacts API
  slug: oracle-goldengate-artifacts-api
- description: Manage AsyncAPI specifications for data streams
  name: Oracle GoldenGate AsyncAPI API
  slug: oracle-goldengate-asyncapi-api
- description: Manage SSL certificates for deployments
  name: Oracle GoldenGate Certificates API
  slug: oracle-goldengate-certificates-api
- description: Execute GoldenGate commands
  name: Oracle GoldenGate Commands API
  slug: oracle-goldengate-commands-api
- description: Manage compare pairs within groups
  name: Oracle GoldenGate Compare Pairs API
  slug: oracle-goldengate-compare-pairs-api
- description: Configuration files and settings for big data handlers
  name: Oracle GoldenGate Configuration API
  slug: oracle-goldengate-configuration-api
- description: Manage connection-to-deployment assignments
  name: Oracle GoldenGate Connection Assignments API
  slug: oracle-goldengate-connection-assignments-api
- description: Manage database and service connections
  name: Oracle GoldenGate Connections API
  slug: oracle-goldengate-connections-api
- description: Manage credential store for big data target connections
  name: Oracle GoldenGate Credentials API
  slug: oracle-goldengate-credentials-api
- description: Manage data stream configurations
  name: Oracle GoldenGate Data Streams API
  slug: oracle-goldengate-data-streams-api
- description: Manage big data target type configurations
  name: Oracle GoldenGate Data Targets API
  slug: oracle-goldengate-data-targets-api
- description: Manage registered source and target databases
  name: Oracle GoldenGate Database Registrations API
  slug: oracle-goldengate-database-registrations-api
- description: Manage deployment backups
  name: Oracle GoldenGate Deployment Backups API
  slug: oracle-goldengate-deployment-backups-api
- description: Query available deployment versions
  name: Oracle GoldenGate Deployment Versions API
  slug: oracle-goldengate-deployment-versions-api
- description: Manage GoldenGate deployment instances
  name: Oracle GoldenGate Deployments API
  slug: oracle-goldengate-deployments-api
- description: Distribution paths for trail data delivery
  name: Oracle GoldenGate Distribution API
  slug: oracle-goldengate-distribution-api
- description: Manage encryption keys and profiles
  name: Oracle GoldenGate Encryption API
  slug: oracle-goldengate-encryption-api
- description: Run and stop comparison jobs
  name: Oracle GoldenGate Execution API
  slug: oracle-goldengate-execution-api
- description: Manage Extract processes for source data capture
  name: Oracle GoldenGate Extracts API
  slug: oracle-goldengate-extracts-api
- description: Manage compare groups
  name: Oracle GoldenGate Groups API
  slug: oracle-goldengate-groups-api
- description: Manage heartbeat tables for lag monitoring
  name: Oracle GoldenGate Heartbeat API
  slug: oracle-goldengate-heartbeat-api
- description: Import and export Veridata configurations
  name: Oracle GoldenGate Import/Export API
  slug: oracle-goldengate-import-export-api
- description: Manage and execute comparison jobs
  name: Oracle GoldenGate Jobs API
  slug: oracle-goldengate-jobs-api
- description: Access service and process logs
  name: Oracle GoldenGate Logs API
  slug: oracle-goldengate-logs-api
- description: Performance metrics and process monitoring
  name: Oracle GoldenGate Monitoring API
  slug: oracle-goldengate-monitoring-api
- description: Manage data replication pipelines
  name: Oracle GoldenGate Pipelines API
  slug: oracle-goldengate-pipelines-api
- description: Manage comparison profiles
  name: Oracle GoldenGate Profiles API
  slug: oracle-goldengate-profiles-api
- description: Manage receiver/collector paths
  name: Oracle GoldenGate Receiver API
  slug: oracle-goldengate-receiver-api
- description: Repair out-of-sync data
  name: Oracle GoldenGate Repair API
  slug: oracle-goldengate-repair-api
- description: Manage Replicat processes targeting big data systems
  name: Oracle GoldenGate Replicats API
  slug: oracle-goldengate-replicats-api
- description: Server information and configuration
  name: Oracle GoldenGate Server API
  slug: oracle-goldengate-server-api
- description: The Services API from Oracle GoldenGate — 2 operation(s) for services.
  name: Oracle GoldenGate Services API
  slug: oracle-goldengate-services-api
- description: Manage automated tasks
  name: Oracle GoldenGate Tasks API
  slug: oracle-goldengate-tasks-api
- description: Trail file management
  name: Oracle GoldenGate Trails API
  slug: oracle-goldengate-trails-api
- description: User management and authorization
  name: Oracle GoldenGate Users API
  slug: oracle-goldengate-users-api
- description: Validate connections and configurations
  name: Oracle GoldenGate Validation API
  slug: oracle-goldengate-validation-api
- description: Track asynchronous operations
  name: Oracle GoldenGate Work Requests API
  slug: oracle-goldengate-work-requests-api
arazzos:
- description: Create a credential alias, create a Replicat with a checkpoint table, and start it.
  name: Oracle GoldenGate Create and Start Replicat With Checkpoint
  slug: oracle-goldengate-create-and-start-replicat-with-checkpoint-workflow
- description: Create a credential alias, validate it can connect, and create an Extract that uses it.
  name: Oracle GoldenGate Validate Credential Then Create Extract
  slug: oracle-goldengate-credential-validate-then-extract-workflow
- description: Run a service health check, then list all Extract and Replicat processes.
  name: Oracle GoldenGate Health Check and Process Inventory
  slug: oracle-goldengate-health-check-and-inventory-workflow
- description: Create a GoldenGate deployment and poll until it reports running.
  name: Oracle GoldenGate Provision Deployment
  slug: oracle-goldengate-provision-deployment-workflow
- description: Create a distribution path, confirm it, and poll its statistics until data flows.
  name: Oracle GoldenGate Provision Distribution Path
  slug: oracle-goldengate-provision-distribution-path-workflow
- description: Create a credential alias, create an Extract process, start it, and poll until running.
  name: Oracle GoldenGate Provision Extract Pipeline
  slug: oracle-goldengate-provision-extract-pipeline-workflow
- description: Create a Replicat process, start it, and poll until it reports running.
  name: Oracle GoldenGate Provision Replicat Pipeline
  slug: oracle-goldengate-provision-replicat-pipeline-workflow
- description: Inspect an Extract's status and restart it only when it has abended.
  name: Oracle GoldenGate Restart Abended Extract
  slug: oracle-goldengate-restart-abended-extract-workflow
- description: Create a database connection, enable table supplemental logging, and list databases.
  name: Oracle GoldenGate Set Up Source Connection
  slug: oracle-goldengate-setup-source-connection-workflow
- description: Confirm an Extract exists, start it, and poll until it is running.
  name: Oracle GoldenGate Start Extract and Verify
  slug: oracle-goldengate-start-extract-and-verify-workflow
- description: Confirm a Replicat exists, start it, and poll until it is running.
  name: Oracle GoldenGate Start Replicat and Verify
  slug: oracle-goldengate-start-replicat-and-verify-workflow
- description: Capture an Extract's status, issue a STOP command, and poll until stopped.
  name: Oracle GoldenGate Stop Extract Gracefully
  slug: oracle-goldengate-stop-extract-gracefully-workflow
- description: Capture a Replicat's status, issue a STOP command, and poll until stopped.
  name: Oracle GoldenGate Stop Replicat Gracefully
  slug: oracle-goldengate-stop-replicat-gracefully-workflow
- description: Stop an Extract, wait until it is stopped, then delete it.
  name: Oracle GoldenGate Tear Down Extract
  slug: oracle-goldengate-teardown-extract-workflow
artifact_total: 1328
collections:
- collection_type: postman
  name: Oracle GoldenGate for Big Data REST API
  slug: postman-oracle-goldengate-big-data-rest-api
- collection_type: postman
  name: Oracle GoldenGate Cloud Service API
  slug: postman-oracle-goldengate-cloud-service-api
- collection_type: postman
  name: Oracle GoldenGate Data Streams REST API
  slug: postman-oracle-goldengate-data-streams-rest-api
- collection_type: postman
  name: Oracle GoldenGate REST API
  slug: postman-oracle-goldengate-rest-api
- collection_type: postman
  name: Oracle GoldenGate Stream Analytics REST API
  slug: postman-oracle-goldengate-stream-analytics-rest-api
- collection_type: postman
  name: Oracle GoldenGate Veridata REST API
  slug: postman-oracle-goldengate-veridata-rest-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts API
  slug: open-oracle-goldengate-artifacts-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts AsyncAPI API
  slug: open-oracle-goldengate-asyncapi-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST API
  slug: open-oracle-goldengate-big-data-rest-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Certificates API
  slug: open-oracle-goldengate-certificates-api
- collection_type: open
  name: Oracle GoldenGate Cloud Service API
  slug: open-oracle-goldengate-cloud-service-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Commands API
  slug: open-oracle-goldengate-commands-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Compare Pairs API
  slug: open-oracle-goldengate-compare-pairs-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Configuration API
  slug: open-oracle-goldengate-configuration-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Connection Assignments API
  slug: open-oracle-goldengate-connection-assignments-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Connections API
  slug: open-oracle-goldengate-connections-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Credentials API
  slug: open-oracle-goldengate-credentials-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Data Streams API
  slug: open-oracle-goldengate-data-streams-api
- collection_type: open
  name: Oracle GoldenGate Data Streams REST API
  slug: open-oracle-goldengate-data-streams-rest-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Data Targets API
  slug: open-oracle-goldengate-data-targets-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Database Registrations API
  slug: open-oracle-goldengate-database-registrations-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Deployment Backups API
  slug: open-oracle-goldengate-deployment-backups-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Deployment Versions API
  slug: open-oracle-goldengate-deployment-versions-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Deployments API
  slug: open-oracle-goldengate-deployments-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Distribution API
  slug: open-oracle-goldengate-distribution-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Encryption API
  slug: open-oracle-goldengate-encryption-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Execution API
  slug: open-oracle-goldengate-execution-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Extracts API
  slug: open-oracle-goldengate-extracts-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Groups API
  slug: open-oracle-goldengate-groups-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Heartbeat API
  slug: open-oracle-goldengate-heartbeat-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Import/Export API
  slug: open-oracle-goldengate-import-export-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Jobs API
  slug: open-oracle-goldengate-jobs-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Logs API
  slug: open-oracle-goldengate-logs-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Monitoring API
  slug: open-oracle-goldengate-monitoring-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Pipelines API
  slug: open-oracle-goldengate-pipelines-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Profiles API
  slug: open-oracle-goldengate-profiles-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Receiver API
  slug: open-oracle-goldengate-receiver-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Repair API
  slug: open-oracle-goldengate-repair-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Replicats API
  slug: open-oracle-goldengate-replicats-api
- collection_type: open
  name: Oracle GoldenGate REST API
  slug: open-oracle-goldengate-rest-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Server API
  slug: open-oracle-goldengate-server-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Services API
  slug: open-oracle-goldengate-services-api
- collection_type: open
  name: Oracle GoldenGate Stream Analytics REST API
  slug: open-oracle-goldengate-stream-analytics-rest-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Tasks API
  slug: open-oracle-goldengate-tasks-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Trails API
  slug: open-oracle-goldengate-trails-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Users API
  slug: open-oracle-goldengate-users-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Validation API
  slug: open-oracle-goldengate-validation-api
- collection_type: open
  name: Oracle GoldenGate Veridata REST API
  slug: open-oracle-goldengate-veridata-rest-api
- collection_type: open
  name: Oracle GoldenGate for Big Data REST Artifacts Work Requests API
  slug: open-oracle-goldengate-work-requests-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/oracle/docker-images/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-goldengate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-goldengate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-goldengate-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/oracle-goldengate/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-goldengate-create-and-start-replicat-with-checkpoint-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-goldengate-credential-validate-then-extract-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-goldengate-health-check-and-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-goldengate-provision-deployment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-goldengate-provision-distribution-path-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-goldengate-provision-extract-pipeline-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-goldengate-provision-replicat-pipeline-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-goldengate-restart-abended-extract-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-goldengate-setup-source-connection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-goldengate-start-extract-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-goldengate-start-replicat-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-goldengate-stop-extract-gracefully-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-goldengate-stop-replicat-gracefully-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-goldengate-teardown-extract-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.oracle.com/integration/goldengate/
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/dataintegration/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/integration/goldengate/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/middleware/goldengate/core/21.3/index.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/cloud/paas/goldengate-service/docs.html
- group: start
  title: ''
  type: Signup
  url: https://www.oracle.com/cloud/free/
- group: start
  title: ''
  type: Login
  url: https://cloud.oracle.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- group: operate
  title: ''
  type: Support
  url: https://support.oracle.com
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://www.oracle.com/integration/goldengate/knowledge-hub/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/oracle/docker-images/tree/main/OracleGoldenGate
- group: learn
  title: ''
  type: Training
  url: https://education.oracle.com/data-integration/goldengate/product_148
- group: learn
  title: ''
  type: Tutorials
  url: https://docs.oracle.com/en/cloud/paas/goldengate-service/tutorials.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.oracle.com/en/database/goldengate/core/26/release-notes/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/oracle-goldengate-deployment-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/oracle-goldengate-context.jsonld
created: '2024-01-15'
description: Oracle GoldenGate enables real-time data integration and replication in heterogeneous IT environments. These APIs provide programmatic access to manage and monitor GoldenGate deployments, processes, and configurations.
examples:
- key_count: 1
  name: Oracle Goldengate Big Data Rest Command Response Example
  slug: oracle-goldengate-big-data-rest-command-response-example
- key_count: 1
  name: Oracle Goldengate Big Data Rest Config File Content Example
  slug: oracle-goldengate-big-data-rest-config-file-content-example
- key_count: 2
  name: Oracle Goldengate Big Data Rest Config File Example
  slug: oracle-goldengate-big-data-rest-config-file-example
- key_count: 1
  name: Oracle Goldengate Big Data Rest Config File List Example
  slug: oracle-goldengate-big-data-rest-config-file-list-example
- key_count: 2
  name: Oracle Goldengate Big Data Rest Create Credential Request Example
  slug: oracle-goldengate-big-data-rest-create-credential-request-example
- key_count: 2
  name: Oracle Goldengate Big Data Rest Create Distribution Path Request Example
  slug: oracle-goldengate-big-data-rest-create-distribution-path-request-example
- key_count: 4
  name: Oracle Goldengate Big Data Rest Create Extract Request Example
  slug: oracle-goldengate-big-data-rest-create-extract-request-example
- key_count: 5
  name: Oracle Goldengate Big Data Rest Create Replicat Request Example
  slug: oracle-goldengate-big-data-rest-create-replicat-request-example
- key_count: 3
  name: Oracle Goldengate Big Data Rest Credential Alias Example
  slug: oracle-goldengate-big-data-rest-credential-alias-example
- key_count: 1
  name: Oracle Goldengate Big Data Rest Credential Domain List Example
  slug: oracle-goldengate-big-data-rest-credential-domain-list-example
- key_count: 1
  name: Oracle Goldengate Big Data Rest Data Target Type List Example
  slug: oracle-goldengate-big-data-rest-data-target-type-list-example
- key_count: 2
  name: Oracle Goldengate Big Data Rest Data Target Type Schema Example
  slug: oracle-goldengate-big-data-rest-data-target-type-schema-example
- key_count: 4
  name: Oracle Goldengate Big Data Rest Distribution Path Example
  slug: oracle-goldengate-big-data-rest-distribution-path-example
- key_count: 1
  name: Oracle Goldengate Big Data Rest Distribution Path List Example
  slug: oracle-goldengate-big-data-rest-distribution-path-list-example
- key_count: 4
  name: Oracle Goldengate Big Data Rest Distribution Path Summary Example
  slug: oracle-goldengate-big-data-rest-distribution-path-summary-example
- key_count: 3
  name: Oracle Goldengate Big Data Rest Error Response Example
  slug: oracle-goldengate-big-data-rest-error-response-example
- key_count: 1
  name: Oracle Goldengate Big Data Rest Execute Command Request Example
  slug: oracle-goldengate-big-data-rest-execute-command-request-example
- key_count: 5
  name: Oracle Goldengate Big Data Rest Extract Example
  slug: oracle-goldengate-big-data-rest-extract-example
- key_count: 1
  name: Oracle Goldengate Big Data Rest Extract List Example
  slug: oracle-goldengate-big-data-rest-extract-list-example
- key_count: 3
  name: Oracle Goldengate Big Data Rest Extract Summary Example
  slug: oracle-goldengate-big-data-rest-extract-summary-example
- key_count: 1
  name: Oracle Goldengate Big Data Rest Process Command Example
  slug: oracle-goldengate-big-data-rest-process-command-example
- key_count: 1
  name: Oracle Goldengate Big Data Rest Process Metrics List Example
  slug: oracle-goldengate-big-data-rest-process-metrics-list-example
- key_count: 4
  name: Oracle Goldengate Big Data Rest Process Status Example
  slug: oracle-goldengate-big-data-rest-process-status-example
- key_count: 7
  name: Oracle Goldengate Big Data Rest Replicat Example
  slug: oracle-goldengate-big-data-rest-replicat-example
- key_count: 1
  name: Oracle Goldengate Big Data Rest Replicat List Example
  slug: oracle-goldengate-big-data-rest-replicat-list-example
- key_count: 6
  name: Oracle Goldengate Big Data Rest Replicat Statistics Example
  slug: oracle-goldengate-big-data-rest-replicat-statistics-example
- key_count: 4
  name: Oracle Goldengate Big Data Rest Replicat Summary Example
  slug: oracle-goldengate-big-data-rest-replicat-summary-example
- key_count: 2
  name: Oracle Goldengate Big Data Rest Service Health Example
  slug: oracle-goldengate-big-data-rest-service-health-example
- key_count: 1
  name: Oracle Goldengate Big Data Rest Trail List Example
  slug: oracle-goldengate-big-data-rest-trail-list-example
- key_count: 2
  name: Oracle Goldengate Big Data Rest Update Extract Request Example
  slug: oracle-goldengate-big-data-rest-update-extract-request-example
- key_count: 2
  name: Oracle Goldengate Big Data Rest Update Replicat Request Example
  slug: oracle-goldengate-big-data-rest-update-replicat-request-example
- key_count: 6
  name: Oracle Goldengate Bulkcreateusers Example
  slug: oracle-goldengate-bulkcreateusers-example
- key_count: 6
  name: Oracle Goldengate Changedeploymentcompartment Example
  slug: oracle-goldengate-changedeploymentcompartment-example
- key_count: 6
  name: Oracle Goldengate Clonegroup Example
  slug: oracle-goldengate-clonegroup-example
- key_count: 1
  name: Oracle Goldengate Cloud Service Certificate Collection Example
  slug: oracle-goldengate-cloud-service-certificate-collection-example
- key_count: 13
  name: Oracle Goldengate Cloud Service Certificate Example
  slug: oracle-goldengate-cloud-service-certificate-example
- key_count: 4
  name: Oracle Goldengate Cloud Service Certificate Summary Example
  slug: oracle-goldengate-cloud-service-certificate-summary-example
- key_count: 1
  name: Oracle Goldengate Cloud Service Change Compartment Details Example
  slug: oracle-goldengate-cloud-service-change-compartment-details-example
- key_count: 3
  name: Oracle Goldengate Cloud Service Collect Diagnostics Details Example
  slug: oracle-goldengate-cloud-service-collect-diagnostics-details-example
- key_count: 1
  name: Oracle Goldengate Cloud Service Connection Assignment Collection Example
  slug: oracle-goldengate-cloud-service-connection-assignment-collection-example
- key_count: 7
  name: Oracle Goldengate Cloud Service Connection Assignment Example
  slug: oracle-goldengate-cloud-service-connection-assignment-example
- key_count: 4
  name: Oracle Goldengate Cloud Service Connection Assignment Summary Example
  slug: oracle-goldengate-cloud-service-connection-assignment-summary-example
- key_count: 1
  name: Oracle Goldengate Cloud Service Connection Collection Example
  slug: oracle-goldengate-cloud-service-connection-collection-example
- key_count: 10
  name: Oracle Goldengate Cloud Service Connection Example
  slug: oracle-goldengate-cloud-service-connection-example
- key_count: 5
  name: Oracle Goldengate Cloud Service Connection Summary Example
  slug: oracle-goldengate-cloud-service-connection-summary-example
- key_count: 2
  name: Oracle Goldengate Cloud Service Create Certificate Details Example
  slug: oracle-goldengate-cloud-service-create-certificate-details-example
- key_count: 2
  name: Oracle Goldengate Cloud Service Create Connection Assignment Details Example
  slug: oracle-goldengate-cloud-service-create-connection-assignment-details-example
- key_count: 6
  name: Oracle Goldengate Cloud Service Create Connection Details Example
  slug: oracle-goldengate-cloud-service-create-connection-details-example
- key_count: 8
  name: Oracle Goldengate Cloud Service Create Database Registration Details Example
  slug: oracle-goldengate-cloud-service-create-database-registration-details-example
- key_count: 6
  name: Oracle Goldengate Cloud Service Create Deployment Backup Details Example
  slug: oracle-goldengate-cloud-service-create-deployment-backup-details-example
- key_count: 12
  name: Oracle Goldengate Cloud Service Create Deployment Details Example
  slug: oracle-goldengate-cloud-service-create-deployment-details-example
- key_count: 5
  name: Oracle Goldengate Cloud Service Create Pipeline Details Example
  slug: oracle-goldengate-cloud-service-create-pipeline-details-example
- key_count: 1
  name: Oracle Goldengate Cloud Service Database Registration Collection Example
  slug: oracle-goldengate-cloud-service-database-registration-collection-example
- key_count: 10
  name: Oracle Goldengate Cloud Service Database Registration Example
  slug: oracle-goldengate-cloud-service-database-registration-example
- key_count: 4
  name: Oracle Goldengate Cloud Service Database Registration Summary Example
  slug: oracle-goldengate-cloud-service-database-registration-summary-example
- key_count: 1
  name: Oracle Goldengate Cloud Service Deployment Backup Collection Example
  slug: oracle-goldengate-cloud-service-deployment-backup-collection-example
- key_count: 9
  name: Oracle Goldengate Cloud Service Deployment Backup Example
  slug: oracle-goldengate-cloud-service-deployment-backup-example
- key_count: 5
  name: Oracle Goldengate Cloud Service Deployment Backup Summary Example
  slug: oracle-goldengate-cloud-service-deployment-backup-summary-example
- key_count: 1
  name: Oracle Goldengate Cloud Service Deployment Collection Example
  slug: oracle-goldengate-cloud-service-deployment-collection-example
- key_count: 19
  name: Oracle Goldengate Cloud Service Deployment Example
  slug: oracle-goldengate-cloud-service-deployment-example
- key_count: 6
  name: Oracle Goldengate Cloud Service Deployment Summary Example
  slug: oracle-goldengate-cloud-service-deployment-summary-example
- key_count: 1
  name: Oracle Goldengate Cloud Service Deployment Version Collection Example
  slug: oracle-goldengate-cloud-service-deployment-version-collection-example
- key_count: 2
  name: Oracle Goldengate Cloud Service Error Example
  slug: oracle-goldengate-cloud-service-error-example
- key_count: 1
  name: Oracle Goldengate Cloud Service Pipeline Collection Example
  slug: oracle-goldengate-cloud-service-pipeline-collection-example
- key_count: 9
  name: Oracle Goldengate Cloud Service Pipeline Example
  slug: oracle-goldengate-cloud-service-pipeline-example
- key_count: 4
  name: Oracle Goldengate Cloud Service Pipeline Summary Example
  slug: oracle-goldengate-cloud-service-pipeline-summary-example
- key_count: 1
  name: Oracle Goldengate Cloud Service Restore Deployment Details Example
  slug: oracle-goldengate-cloud-service-restore-deployment-details-example
- key_count: 1
  name: Oracle Goldengate Cloud Service Start Deployment Details Example
  slug: oracle-goldengate-cloud-service-start-deployment-details-example
- key_count: 1
  name: Oracle Goldengate Cloud Service Stop Deployment Details Example
  slug: oracle-goldengate-cloud-service-stop-deployment-details-example
- key_count: 3
  name: Oracle Goldengate Cloud Service Update Connection Details Example
  slug: oracle-goldengate-cloud-service-update-connection-details-example
- key_count: 6
  name: Oracle Goldengate Cloud Service Update Database Registration Details Example
  slug: oracle-goldengate-cloud-service-update-database-registration-details-example
- key_count: 7
  name: Oracle Goldengate Cloud Service Update Deployment Details Example
  slug: oracle-goldengate-cloud-service-update-deployment-details-example
- key_count: 2
  name: Oracle Goldengate Cloud Service Update Pipeline Details Example
  slug: oracle-goldengate-cloud-service-update-pipeline-details-example
- key_count: 2
  name: Oracle Goldengate Cloud Service Upgrade Deployment Details Example
  slug: oracle-goldengate-cloud-service-upgrade-deployment-details-example
- key_count: 1
  name: Oracle Goldengate Cloud Service Work Request Collection Example
  slug: oracle-goldengate-cloud-service-work-request-collection-example
- key_count: 1
  name: Oracle Goldengate Cloud Service Work Request Error Collection Example
  slug: oracle-goldengate-cloud-service-work-request-error-collection-example
- key_count: 8
  name: Oracle Goldengate Cloud Service Work Request Example
  slug: oracle-goldengate-cloud-service-work-request-example
- key_count: 1
  name: Oracle Goldengate Cloud Service Work Request Log Entry Collection Example
  slug: oracle-goldengate-cloud-service-work-request-log-entry-collection-example
- key_count: 5
  name: Oracle Goldengate Cloud Service Work Request Summary Example
  slug: oracle-goldengate-cloud-service-work-request-summary-example
- key_count: 6
  name: Oracle Goldengate Collectdeploymentdiagnostics Example
  slug: oracle-goldengate-collectdeploymentdiagnostics-example
- key_count: 6
  name: Oracle Goldengate Createcertificate Example
  slug: oracle-goldengate-createcertificate-example
- key_count: 6
  name: Oracle Goldengate Createcollectorpath Example
  slug: oracle-goldengate-createcollectorpath-example
- key_count: 6
  name: Oracle Goldengate Createcomparepairs Example
  slug: oracle-goldengate-createcomparepairs-example
- key_count: 6
  name: Oracle Goldengate Createconfigfile Example
  slug: oracle-goldengate-createconfigfile-example
- key_count: 6
  name: Oracle Goldengate Createconnection Example
  slug: oracle-goldengate-createconnection-example
- key_count: 6
  name: Oracle Goldengate Createconnectionassignment Example
  slug: oracle-goldengate-createconnectionassignment-example
- key_count: 6
  name: Oracle Goldengate Createcredentialalias Example
  slug: oracle-goldengate-createcredentialalias-example
- key_count: 6
  name: Oracle Goldengate Createdatabaseregistration Example
  slug: oracle-goldengate-createdatabaseregistration-example
- key_count: 6
  name: Oracle Goldengate Createdatastream Example
  slug: oracle-goldengate-createdatastream-example
- key_count: 6
  name: Oracle Goldengate Createdeployment Example
  slug: oracle-goldengate-createdeployment-example
- key_count: 6
  name: Oracle Goldengate Createdeploymentbackup Example
  slug: oracle-goldengate-createdeploymentbackup-example
- key_count: 6
  name: Oracle Goldengate Createdistributionpath Example
  slug: oracle-goldengate-createdistributionpath-example
- key_count: 6
  name: Oracle Goldengate Createencryptionkey Example
  slug: oracle-goldengate-createencryptionkey-example
- key_count: 6
  name: Oracle Goldengate Createextract Example
  slug: oracle-goldengate-createextract-example
- key_count: 6
  name: Oracle Goldengate Creategroup Example
  slug: oracle-goldengate-creategroup-example
- key_count: 6
  name: Oracle Goldengate Createheartbeattable Example
  slug: oracle-goldengate-createheartbeattable-example
- key_count: 6
  name: Oracle Goldengate Createjob Example
  slug: oracle-goldengate-createjob-example
- key_count: 6
  name: Oracle Goldengate Createmasterkeyversion Example
  slug: oracle-goldengate-createmasterkeyversion-example
- key_count: 6
  name: Oracle Goldengate Createpipeline Example
  slug: oracle-goldengate-createpipeline-example
- key_count: 6
  name: Oracle Goldengate Createprofile Example
  slug: oracle-goldengate-createprofile-example
- key_count: 6
  name: Oracle Goldengate Createreplicat Example
  slug: oracle-goldengate-createreplicat-example
- key_count: 6
  name: Oracle Goldengate Createservice Example
  slug: oracle-goldengate-createservice-example
- key_count: 6
  name: Oracle Goldengate Createtask Example
  slug: oracle-goldengate-createtask-example
- key_count: 6
  name: Oracle Goldengate Createuser Example
  slug: oracle-goldengate-createuser-example
- key_count: 6
  name: Oracle Goldengate Createusergroup Example
  slug: oracle-goldengate-createusergroup-example
- key_count: 4
  name: Oracle Goldengate Data Streams Rest Create Data Stream Request Example
  slug: oracle-goldengate-data-streams-rest-create-data-stream-request-example
- key_count: 9
  name: Oracle Goldengate Data Streams Rest Data Stream Example
  slug: oracle-goldengate-data-streams-rest-data-stream-example
- key_count: 1
  name: Oracle Goldengate Data Streams Rest Data Stream List Example
  slug: oracle-goldengate-data-streams-rest-data-stream-list-example
- key_count: 3
  name: Oracle Goldengate Data Streams Rest Data Stream Summary Example
  slug: oracle-goldengate-data-streams-rest-data-stream-summary-example
- key_count: 2
  name: Oracle Goldengate Data Streams Rest Error Response Example
  slug: oracle-goldengate-data-streams-rest-error-response-example
- key_count: 4
  name: Oracle Goldengate Data Streams Rest Update Data Stream Request Example
  slug: oracle-goldengate-data-streams-rest-update-data-stream-request-example
- key_count: 6
  name: Oracle Goldengate Describeapiversion Example
  slug: oracle-goldengate-describeapiversion-example
- key_count: 6
  name: Oracle Goldengate Executecommand Example
  slug: oracle-goldengate-executecommand-example
- key_count: 6
  name: Oracle Goldengate Exportconfiguration Example
  slug: oracle-goldengate-exportconfiguration-example
- key_count: 6
  name: Oracle Goldengate Exportpipeline Example
  slug: oracle-goldengate-exportpipeline-example
- key_count: 6
  name: Oracle Goldengate Generatecolumnmappings Example
  slug: oracle-goldengate-generatecolumnmappings-example
- key_count: 6
  name: Oracle Goldengate Generatemappingobjects Example
  slug: oracle-goldengate-generatemappingobjects-example
- key_count: 6
  name: Oracle Goldengate Getapiversions Example
  slug: oracle-goldengate-getapiversions-example
- key_count: 6
  name: Oracle Goldengate Getasyncapispec Example
  slug: oracle-goldengate-getasyncapispec-example
- key_count: 6
  name: Oracle Goldengate Getcachestatistics Example
  slug: oracle-goldengate-getcachestatistics-example
- key_count: 6
  name: Oracle Goldengate Getcertificate Example
  slug: oracle-goldengate-getcertificate-example
- key_count: 6
  name: Oracle Goldengate Getcollectorpath Example
  slug: oracle-goldengate-getcollectorpath-example
- key_count: 6
  name: Oracle Goldengate Getcomparepair Example
  slug: oracle-goldengate-getcomparepair-example
- key_count: 6
  name: Oracle Goldengate Getcomparepairstatistics Example
  slug: oracle-goldengate-getcomparepairstatistics-example
- key_count: 6
  name: Oracle Goldengate Getcomparisonreport Example
  slug: oracle-goldengate-getcomparisonreport-example
- key_count: 6
  name: Oracle Goldengate Getconfigfile Example
  slug: oracle-goldengate-getconfigfile-example
- key_count: 6
  name: Oracle Goldengate Getconfigsummary Example
  slug: oracle-goldengate-getconfigsummary-example
- key_count: 6
  name: Oracle Goldengate Getconnection Example
  slug: oracle-goldengate-getconnection-example
- key_count: 6
  name: Oracle Goldengate Getconnectionassignment Example
  slug: oracle-goldengate-getconnectionassignment-example
- key_count: 6
  name: Oracle Goldengate Getconnectionmetadata Example
  slug: oracle-goldengate-getconnectionmetadata-example
- key_count: 6
  name: Oracle Goldengate Getconnectionstatus Example
  slug: oracle-goldengate-getconnectionstatus-example
- key_count: 6
  name: Oracle Goldengate Getcredentialalias Example
  slug: oracle-goldengate-getcredentialalias-example
- key_count: 6
  name: Oracle Goldengate Getcriticalevents Example
  slug: oracle-goldengate-getcriticalevents-example
- key_count: 6
  name: Oracle Goldengate Getcurrentuser Example
  slug: oracle-goldengate-getcurrentuser-example
- key_count: 6
  name: Oracle Goldengate Getdatabasenames Example
  slug: oracle-goldengate-getdatabasenames-example
- key_count: 6
  name: Oracle Goldengate Getdatabaseregistration Example
  slug: oracle-goldengate-getdatabaseregistration-example
- key_count: 6
  name: Oracle Goldengate Getdatabasetables Example
  slug: oracle-goldengate-getdatabasetables-example
- key_count: 6
  name: Oracle Goldengate Getdatastream Example
  slug: oracle-goldengate-getdatastream-example
- key_count: 6
  name: Oracle Goldengate Getdatatargettypeschema Example
  slug: oracle-goldengate-getdatatargettypeschema-example
- key_count: 6
  name: Oracle Goldengate Getdeployment Example
  slug: oracle-goldengate-getdeployment-example
- key_count: 6
  name: Oracle Goldengate Getdeploymentbackup Example
  slug: oracle-goldengate-getdeploymentbackup-example
- key_count: 6
  name: Oracle Goldengate Getdistributionpath Example
  slug: oracle-goldengate-getdistributionpath-example
- key_count: 6
  name: Oracle Goldengate Getdistributionpathstats Example
  slug: oracle-goldengate-getdistributionpathstats-example
- key_count: 6
  name: Oracle Goldengate Getencryptionkey Example
  slug: oracle-goldengate-getencryptionkey-example
- key_count: 6
  name: Oracle Goldengate Getextract Example
  slug: oracle-goldengate-getextract-example
- key_count: 6
  name: Oracle Goldengate Getextractcheckpoints Example
  slug: oracle-goldengate-getextractcheckpoints-example
- key_count: 6
  name: Oracle Goldengate Getextractdatabasestats Example
  slug: oracle-goldengate-getextractdatabasestats-example
- key_count: 6
  name: Oracle Goldengate Getextracthistory Example
  slug: oracle-goldengate-getextracthistory-example
- key_count: 6
  name: Oracle Goldengate Getextractreport Example
  slug: oracle-goldengate-getextractreport-example
- key_count: 6
  name: Oracle Goldengate Getextractstatus Example
  slug: oracle-goldengate-getextractstatus-example
- key_count: 6
  name: Oracle Goldengate Getgroup Example
  slug: oracle-goldengate-getgroup-example
- key_count: 6
  name: Oracle Goldengate Getheartbeatentries Example
  slug: oracle-goldengate-getheartbeatentries-example
- key_count: 6
  name: Oracle Goldengate Getheartbeatmetrics Example
  slug: oracle-goldengate-getheartbeatmetrics-example
- key_count: 6
  name: Oracle Goldengate Getheartbeattable Example
  slug: oracle-goldengate-getheartbeattable-example
- key_count: 6
  name: Oracle Goldengate Getjob Example
  slug: oracle-goldengate-getjob-example
- key_count: 6
  name: Oracle Goldengate Getjobstatistics Example
  slug: oracle-goldengate-getjobstatistics-example
- key_count: 6
  name: Oracle Goldengate Getlog Example
  slug: oracle-goldengate-getlog-example
- key_count: 6
  name: Oracle Goldengate Getmessageexplanation Example
  slug: oracle-goldengate-getmessageexplanation-example
- key_count: 6
  name: Oracle Goldengate Getoutofsyncdata Example
  slug: oracle-goldengate-getoutofsyncdata-example
- key_count: 6
  name: Oracle Goldengate Getparameterinfo Example
  slug: oracle-goldengate-getparameterinfo-example
- key_count: 6
  name: Oracle Goldengate Getpipeline Example
  slug: oracle-goldengate-getpipeline-example
- key_count: 6
  name: Oracle Goldengate Getprocessmetrics Example
  slug: oracle-goldengate-getprocessmetrics-example
- key_count: 6
  name: Oracle Goldengate Getprocessperformance Example
  slug: oracle-goldengate-getprocessperformance-example
- key_count: 6
  name: Oracle Goldengate Getprofile Example
  slug: oracle-goldengate-getprofile-example
- key_count: 6
  name: Oracle Goldengate Getrepairedrowdetails Example
  slug: oracle-goldengate-getrepairedrowdetails-example
- key_count: 6
  name: Oracle Goldengate Getrepairreport Example
  slug: oracle-goldengate-getrepairreport-example
- key_count: 6
  name: Oracle Goldengate Getrepairstatistics Example
  slug: oracle-goldengate-getrepairstatistics-example
- key_count: 6
  name: Oracle Goldengate Getreplicat Example
  slug: oracle-goldengate-getreplicat-example
- key_count: 6
  name: Oracle Goldengate Getreplicatcheckpoints Example
  slug: oracle-goldengate-getreplicatcheckpoints-example
- key_count: 6
  name: Oracle Goldengate Getreplicatdatabasestats Example
  slug: oracle-goldengate-getreplicatdatabasestats-example
- key_count: 6
  name: Oracle Goldengate Getreplicathistory Example
  slug: oracle-goldengate-getreplicathistory-example
- key_count: 6
  name: Oracle Goldengate Getreplicatstats Example
  slug: oracle-goldengate-getreplicatstats-example
- key_count: 6
  name: Oracle Goldengate Getreplicatstatus Example
  slug: oracle-goldengate-getreplicatstatus-example
- key_count: 6
  name: Oracle Goldengate Getrequeststatus Example
  slug: oracle-goldengate-getrequeststatus-example
- key_count: 6
  name: Oracle Goldengate Getserverconfiguration Example
  slug: oracle-goldengate-getserverconfiguration-example
- key_count: 6
  name: Oracle Goldengate Getserverinfo Example
  slug: oracle-goldengate-getserverinfo-example
- key_count: 6
  name: Oracle Goldengate Getserverlogs Example
  slug: oracle-goldengate-getserverlogs-example
- key_count: 6
  name: Oracle Goldengate Getservice Example
  slug: oracle-goldengate-getservice-example
- key_count: 6
  name: Oracle Goldengate Getservicehealth Example
  slug: oracle-goldengate-getservicehealth-example
- key_count: 6
  name: Oracle Goldengate Getservicehealthcheck Example
  slug: oracle-goldengate-getservicehealthcheck-example
- key_count: 6
  name: Oracle Goldengate Getservicehealthdetails Example
  slug: oracle-goldengate-getservicehealthdetails-example
- key_count: 6
  name: Oracle Goldengate Gettask Example
  slug: oracle-goldengate-gettask-example
- key_count: 6
  name: Oracle Goldengate Getuser Example
  slug: oracle-goldengate-getuser-example
- key_count: 6
  name: Oracle Goldengate Getusergroup Example
  slug: oracle-goldengate-getusergroup-example
- key_count: 6
  name: Oracle Goldengate Getworkrequest Example
  slug: oracle-goldengate-getworkrequest-example
- key_count: 6
  name: Oracle Goldengate Importartifacts Example
  slug: oracle-goldengate-importartifacts-example
- key_count: 6
  name: Oracle Goldengate Importconfiguration Example
  slug: oracle-goldengate-importconfiguration-example
- key_count: 6
  name: Oracle Goldengate Importgoldengateparameterfile Example
  slug: oracle-goldengate-importgoldengateparameterfile-example
- key_count: 6
  name: Oracle Goldengate Issueextractcommand Example
  slug: oracle-goldengate-issueextractcommand-example
- key_count: 6
  name: Oracle Goldengate Issuereplicatcommand Example
  slug: oracle-goldengate-issuereplicatcommand-example
- key_count: 6
  name: Oracle Goldengate Listbackgroundrequests Example
  slug: oracle-goldengate-listbackgroundrequests-example
- key_count: 6
  name: Oracle Goldengate Listcertificates Example
  slug: oracle-goldengate-listcertificates-example
- key_count: 6
  name: Oracle Goldengate Listcertificatetypes Example
  slug: oracle-goldengate-listcertificatetypes-example
- key_count: 6
  name: Oracle Goldengate Listcollectorpaths Example
  slug: oracle-goldengate-listcollectorpaths-example
- key_count: 6
  name: Oracle Goldengate Listconfigfiles Example
  slug: oracle-goldengate-listconfigfiles-example
- key_count: 6
  name: Oracle Goldengate Listconfigtypes Example
  slug: oracle-goldengate-listconfigtypes-example
- key_count: 6
  name: Oracle Goldengate Listconnectionassignments Example
  slug: oracle-goldengate-listconnectionassignments-example
- key_count: 6
  name: Oracle Goldengate Listconnections Example
  slug: oracle-goldengate-listconnections-example
- key_count: 6
  name: Oracle Goldengate Listcredentialdomains Example
  slug: oracle-goldengate-listcredentialdomains-example
- key_count: 6
  name: Oracle Goldengate Listdatabaseregistrations Example
  slug: oracle-goldengate-listdatabaseregistrations-example
- key_count: 6
  name: Oracle Goldengate Listdatastreams Example
  slug: oracle-goldengate-listdatastreams-example
- key_count: 6
  name: Oracle Goldengate Listdatatargettypes Example
  slug: oracle-goldengate-listdatatargettypes-example
- key_count: 6
  name: Oracle Goldengate Listdeploymentbackups Example
  slug: oracle-goldengate-listdeploymentbackups-example
- key_count: 6
  name: Oracle Goldengate Listdeployments Example
  slug: oracle-goldengate-listdeployments-example
- key_count: 6
  name: Oracle Goldengate Listdeploymentversions Example
  slug: oracle-goldengate-listdeploymentversions-example
- key_count: 6
  name: Oracle Goldengate Listdistributionpaths Example
  slug: oracle-goldengate-listdistributionpaths-example
- key_count: 6
  name: Oracle Goldengate Listdomainaliases Example
  slug: oracle-goldengate-listdomainaliases-example
- key_count: 6
  name: Oracle Goldengate Listencryptionkeys Example
  slug: oracle-goldengate-listencryptionkeys-example
- key_count: 6
  name: Oracle Goldengate Listextractlogs Example
  slug: oracle-goldengate-listextractlogs-example
- key_count: 6
  name: Oracle Goldengate Listextractreports Example
  slug: oracle-goldengate-listextractreports-example
- key_count: 6
  name: Oracle Goldengate Listextracts Example
  slug: oracle-goldengate-listextracts-example
- key_count: 6
  name: Oracle Goldengate Listextracttrails Example
  slug: oracle-goldengate-listextracttrails-example
- key_count: 6
  name: Oracle Goldengate Listgroups Example
  slug: oracle-goldengate-listgroups-example
- key_count: 6
  name: Oracle Goldengate Listjobs Example
  slug: oracle-goldengate-listjobs-example
- key_count: 6
  name: Oracle Goldengate Listlogs Example
  slug: oracle-goldengate-listlogs-example
- key_count: 6
  name: Oracle Goldengate Listmasterkeyversions Example
  slug: oracle-goldengate-listmasterkeyversions-example
- key_count: 6
  name: Oracle Goldengate Listmessagecodes Example
  slug: oracle-goldengate-listmessagecodes-example
- key_count: 6
  name: Oracle Goldengate Listmessages Example
  slug: oracle-goldengate-listmessages-example
- key_count: 6
  name: Oracle Goldengate Listmonitoringmessages Example
  slug: oracle-goldengate-listmonitoringmessages-example
- key_count: 6
  name: Oracle Goldengate Listparameters Example
  slug: oracle-goldengate-listparameters-example
- key_count: 6
  name: Oracle Goldengate Listpipelines Example
  slug: oracle-goldengate-listpipelines-example
- key_count: 6
  name: Oracle Goldengate Listprocessmetrics Example
  slug: oracle-goldengate-listprocessmetrics-example
- key_count: 6
  name: Oracle Goldengate Listprofiles Example
  slug: oracle-goldengate-listprofiles-example
- key_count: 6
  name: Oracle Goldengate Listreplicatreports Example
  slug: oracle-goldengate-listreplicatreports-example
- key_count: 6
  name: Oracle Goldengate Listreplicats Example
  slug: oracle-goldengate-listreplicats-example
- key_count: 6
  name: Oracle Goldengate Listservices Example
  slug: oracle-goldengate-listservices-example
- key_count: 6
  name: Oracle Goldengate Liststatuschanges Example
  slug: oracle-goldengate-liststatuschanges-example
- key_count: 6
  name: Oracle Goldengate Listtasks Example
  slug: oracle-goldengate-listtasks-example
- key_count: 6
  name: Oracle Goldengate Listtrails Example
  slug: oracle-goldengate-listtrails-example
- key_count: 6
  name: Oracle Goldengate Listusergroups Example
  slug: oracle-goldengate-listusergroups-example
- key_count: 6
  name: Oracle Goldengate Listuserroles Example
  slug: oracle-goldengate-listuserroles-example
- key_count: 6
  name: Oracle Goldengate Listusers Example
  slug: oracle-goldengate-listusers-example
- key_count: 6
  name: Oracle Goldengate Listworkrequesterrors Example
  slug: oracle-goldengate-listworkrequesterrors-example
- key_count: 6
  name: Oracle Goldengate Listworkrequestlogs Example
  slug: oracle-goldengate-listworkrequestlogs-example
- key_count: 6
  name: Oracle Goldengate Listworkrequests Example
  slug: oracle-goldengate-listworkrequests-example
- key_count: 6
  name: Oracle Goldengate Login Example
  slug: oracle-goldengate-login-example
- key_count: 6
  name: Oracle Goldengate Manageschemasupplementallogging Example
  slug: oracle-goldengate-manageschemasupplementallogging-example
- key_count: 6
  name: Oracle Goldengate Managetablesupplementallogging Example
  slug: oracle-goldengate-managetablesupplementallogging-example
- key_count: 6
  name: Oracle Goldengate Modifylogproperties Example
  slug: oracle-goldengate-modifylogproperties-example
- key_count: 6
  name: Oracle Goldengate Publishpipeline Example
  slug: oracle-goldengate-publishpipeline-example
- key_count: 6
  name: Oracle Goldengate Repairjob Example
  slug: oracle-goldengate-repairjob-example
- key_count: 6
  name: Oracle Goldengate Replacecomparepair Example
  slug: oracle-goldengate-replacecomparepair-example
- key_count: 6
  name: Oracle Goldengate Replaceconfigfile Example
  slug: oracle-goldengate-replaceconfigfile-example
- key_count: 6
  name: Oracle Goldengate Replaceconnection Example
  slug: oracle-goldengate-replaceconnection-example
- key_count: 6
  name: Oracle Goldengate Replacecredentialalias Example
  slug: oracle-goldengate-replacecredentialalias-example
- key_count: 6
  name: Oracle Goldengate Replacejob Example
  slug: oracle-goldengate-replacejob-example
- key_count: 6
  name: Oracle Goldengate Replaceuser Example
  slug: oracle-goldengate-replaceuser-example
- key_count: 6
  name: Oracle Goldengate Replaceusergroup Example
  slug: oracle-goldengate-replaceusergroup-example
- key_count: 6
  name: Oracle Goldengate Resetprofile Example
  slug: oracle-goldengate-resetprofile-example
- key_count: 6
  name: Oracle Goldengate Resetserverconfiguration Example
  slug: oracle-goldengate-resetserverconfiguration-example
- key_count: 4
  name: Oracle Goldengate Rest Api Version Details Example
  slug: oracle-goldengate-rest-api-version-details-example
- key_count: 1
  name: Oracle Goldengate Rest Api Version List Example
  slug: oracle-goldengate-rest-api-version-list-example
- key_count: 1
  name: Oracle Goldengate Rest Bulk Create Users Request Example
  slug: oracle-goldengate-rest-bulk-create-users-request-example
- key_count: 4
  name: Oracle Goldengate Rest Cache Statistics Example
  slug: oracle-goldengate-rest-cache-statistics-example
- key_count: 6
  name: Oracle Goldengate Rest Certificate Example
  slug: oracle-goldengate-rest-certificate-example
- key_count: 1
  name: Oracle Goldengate Rest Certificate Name List Example
  slug: oracle-goldengate-rest-certificate-name-list-example
- key_count: 1
  name: Oracle Goldengate Rest Certificate Type List Example
  slug: oracle-goldengate-rest-certificate-type-list-example
- key_count: 3
  name: Oracle Goldengate Rest Checkpoints Example
  slug: oracle-goldengate-rest-checkpoints-example
- key_count: 4
  name: Oracle Goldengate Rest Collector Path Example
  slug: oracle-goldengate-rest-collector-path-example
- key_count: 1
  name: Oracle Goldengate Rest Collector Path List Example
  slug: oracle-goldengate-rest-collector-path-list-example
- key_count: 2
  name: Oracle Goldengate Rest Collector Path Summary Example
  slug: oracle-goldengate-rest-collector-path-summary-example
- key_count: 1
  name: Oracle Goldengate Rest Command Response Example
  slug: oracle-goldengate-rest-command-response-example
- key_count: 1
  name: Oracle Goldengate Rest Config File Content Example
  slug: oracle-goldengate-rest-config-file-content-example
- key_count: 3
  name: Oracle Goldengate Rest Config File Example
  slug: oracle-goldengate-rest-config-file-example
- key_count: 1
  name: Oracle Goldengate Rest Config File List Example
  slug: oracle-goldengate-rest-config-file-list-example
- key_count: 5
  name: Oracle Goldengate Rest Config Summary Example
  slug: oracle-goldengate-rest-config-summary-example
- key_count: 1
  name: Oracle Goldengate Rest Config Type List Example
  slug: oracle-goldengate-rest-config-type-list-example
- key_count: 1
  name: Oracle Goldengate Rest Connection List Example
  slug: oracle-goldengate-rest-connection-list-example
- key_count: 2
  name: Oracle Goldengate Rest Create Collector Path Request Example
  slug: oracle-goldengate-rest-create-collector-path-request-example
- key_count: 3
  name: Oracle Goldengate Rest Create Connection Request Example
  slug: oracle-goldengate-rest-create-connection-request-example
- key_count: 2
  name: Oracle Goldengate Rest Create Credential Alias Request Example
  slug: oracle-goldengate-rest-create-credential-alias-request-example
- key_count: 4
  name: Oracle Goldengate Rest Create Deployment Request Example
  slug: oracle-goldengate-rest-create-deployment-request-example
- key_count: 4
  name: Oracle Goldengate Rest Create Distribution Path Request Example
  slug: oracle-goldengate-rest-create-distribution-path-request-example
- key_count: 8
  name: Oracle Goldengate Rest Create Extract Request Example
  slug: oracle-goldengate-rest-create-extract-request-example
- key_count: 4
  name: Oracle Goldengate Rest Create Heartbeat Table Request Example
  slug: oracle-goldengate-rest-create-heartbeat-table-request-example
- key_count: 7
  name: Oracle Goldengate Rest Create Replicat Request Example
  slug: oracle-goldengate-rest-create-replicat-request-example
- key_count: 3
  name: Oracle Goldengate Rest Create Service Request Example
  slug: oracle-goldengate-rest-create-service-request-example
- key_count: 3
  name: Oracle Goldengate Rest Create Task Request Example
  slug: oracle-goldengate-rest-create-task-request-example
- key_count: 2
  name: Oracle Goldengate Rest Create User Request Example
  slug: oracle-goldengate-rest-create-user-request-example
- key_count: 3
  name: Oracle Goldengate Rest Credential Alias Example
  slug: oracle-goldengate-rest-credential-alias-example
- key_count: 1
  name: Oracle Goldengate Rest Credential Alias List Example
  slug: oracle-goldengate-rest-credential-alias-list-example
- key_count: 1
  name: Oracle Goldengate Rest Credential Domain List Example
  slug: oracle-goldengate-rest-credential-domain-list-example
- key_count: 4
  name: Oracle Goldengate Rest Database Connection Example
  slug: oracle-goldengate-rest-database-connection-example
- key_count: 1
  name: Oracle Goldengate Rest Database Name List Example
  slug: oracle-goldengate-rest-database-name-list-example
- key_count: 6
  name: Oracle Goldengate Rest Database Statistics Example
  slug: oracle-goldengate-rest-database-statistics-example
- key_count: 7
  name: Oracle Goldengate Rest Deployment Example
  slug: oracle-goldengate-rest-deployment-example
- key_count: 1
  name: Oracle Goldengate Rest Deployment List Example
  slug: oracle-goldengate-rest-deployment-list-example
- key_count: 3
  name: Oracle Goldengate Rest Deployment Summary Example
  slug: oracle-goldengate-rest-deployment-summary-example
- key_count: 6
  name: Oracle Goldengate Rest Distribution Path Example
  slug: oracle-goldengate-rest-distribution-path-example
- key_count: 1
  name: Oracle Goldengate Rest Distribution Path List Example
  slug: oracle-goldengate-rest-distribution-path-list-example
- key_count: 4
  name: Oracle Goldengate Rest Distribution Path Summary Example
  slug: oracle-goldengate-rest-distribution-path-summary-example
- key_count: 3
  name: Oracle Goldengate Rest Encryption Key Example
  slug: oracle-goldengate-rest-encryption-key-example
- key_count: 1
  name: Oracle Goldengate Rest Encryption Key List Example
  slug: oracle-goldengate-rest-encryption-key-list-example
- key_count: 3
  name: Oracle Goldengate Rest Error Response Example
  slug: oracle-goldengate-rest-error-response-example
- key_count: 1
  name: Oracle Goldengate Rest Event List Example
  slug: oracle-goldengate-rest-event-list-example
- key_count: 1
  name: Oracle Goldengate Rest Execute Command Request Example
  slug: oracle-goldengate-rest-execute-command-request-example
- key_count: 10
  name: Oracle Goldengate Rest Extract Example
  slug: oracle-goldengate-rest-extract-example
- key_count: 1
  name: Oracle Goldengate Rest Extract List Example
  slug: oracle-goldengate-rest-extract-list-example
- key_count: 4
  name: Oracle Goldengate Rest Extract Summary Example
  slug: oracle-goldengate-rest-extract-summary-example
- key_count: 1
  name: Oracle Goldengate Rest Extract Trail List Example
  slug: oracle-goldengate-rest-extract-trail-list-example
- key_count: 3
  name: Oracle Goldengate Rest Health Check Summary Example
  slug: oracle-goldengate-rest-health-check-summary-example
- key_count: 1
  name: Oracle Goldengate Rest Heartbeat Entries Example
  slug: oracle-goldengate-rest-heartbeat-entries-example
- key_count: 3
  name: Oracle Goldengate Rest Heartbeat Metrics Example
  slug: oracle-goldengate-rest-heartbeat-metrics-example
- key_count: 5
  name: Oracle Goldengate Rest Heartbeat Table Example
  slug: oracle-goldengate-rest-heartbeat-table-example
- key_count: 3
  name: Oracle Goldengate Rest Link Example
  slug: oracle-goldengate-rest-link-example
- key_count: 3
  name: Oracle Goldengate Rest Log Content Example
  slug: oracle-goldengate-rest-log-content-example
- key_count: 1
  name: Oracle Goldengate Rest Log List Example
  slug: oracle-goldengate-rest-log-list-example
- key_count: 3
  name: Oracle Goldengate Rest Master Key Version Example
  slug: oracle-goldengate-rest-master-key-version-example
- key_count: 1
  name: Oracle Goldengate Rest Master Key Version List Example
  slug: oracle-goldengate-rest-master-key-version-list-example
- key_count: 1
  name: Oracle Goldengate Rest Message Code List Example
  slug: oracle-goldengate-rest-message-code-list-example
- key_count: 4
  name: Oracle Goldengate Rest Message Explanation Example
  slug: oracle-goldengate-rest-message-explanation-example
- key_count: 1
  name: Oracle Goldengate Rest Message List Example
  slug: oracle-goldengate-rest-message-list-example
- key_count: 1
  name: Oracle Goldengate Rest Modify Log Request Example
  slug: oracle-goldengate-rest-modify-log-request-example
- key_count: 1
  name: Oracle Goldengate Rest Monitoring Message List Example
  slug: oracle-goldengate-rest-monitoring-message-list-example
- key_count: 5
  name: Oracle Goldengate Rest Parameter Info Example
  slug: oracle-goldengate-rest-parameter-info-example
- key_count: 1
  name: Oracle Goldengate Rest Parameter Name List Example
  slug: oracle-goldengate-rest-parameter-name-list-example
- key_count: 4
  name: Oracle Goldengate Rest Path Statistics Example
  slug: oracle-goldengate-rest-path-statistics-example
- key_count: 2
  name: Oracle Goldengate Rest Process Command Example
  slug: oracle-goldengate-rest-process-command-example
- key_count: 2
  name: Oracle Goldengate Rest Process History Example
  slug: oracle-goldengate-rest-process-history-example
- key_count: 8
  name: Oracle Goldengate Rest Process Metrics Example
  slug: oracle-goldengate-rest-process-metrics-example
- key_count: 1
  name: Oracle Goldengate Rest Process Metrics List Example
  slug: oracle-goldengate-rest-process-metrics-list-example
- key_count: 4
  name: Oracle Goldengate Rest Process Performance Example
  slug: oracle-goldengate-rest-process-performance-example
- key_count: 5
  name: Oracle Goldengate Rest Process Status Example
  slug: oracle-goldengate-rest-process-status-example
- key_count: 8
  name: Oracle Goldengate Rest Replicat Example
  slug: oracle-goldengate-rest-replicat-example
- key_count: 1
  name: Oracle Goldengate Rest Replicat List Example
  slug: oracle-goldengate-rest-replicat-list-example
- key_count: 3
  name: Oracle Goldengate Rest Replicat Summary Example
  slug: oracle-goldengate-rest-replicat-summary-example
- key_count: 2
  name: Oracle Goldengate Rest Report Example
  slug: oracle-goldengate-rest-report-example
- key_count: 1
  name: Oracle Goldengate Rest Report List Example
  slug: oracle-goldengate-rest-report-list-example
- key_count: 1
  name: Oracle Goldengate Rest Request List Example
  slug: oracle-goldengate-rest-request-list-example
- key_count: 5
  name: Oracle Goldengate Rest Request Status Example
  slug: oracle-goldengate-rest-request-status-example
- key_count: 1
  name: Oracle Goldengate Rest Role List Example
  slug: oracle-goldengate-rest-role-list-example
- key_count: 5
  name: Oracle Goldengate Rest Service Example
  slug: oracle-goldengate-rest-service-example
- key_count: 2
  name: Oracle Goldengate Rest Service Health Details Example
  slug: oracle-goldengate-rest-service-health-details-example
- key_count: 1
  name: Oracle Goldengate Rest Service List Example
  slug: oracle-goldengate-rest-service-list-example
- key_count: 4
  name: Oracle Goldengate Rest Service Summary Example
  slug: oracle-goldengate-rest-service-summary-example
- key_count: 1
  name: Oracle Goldengate Rest Status Change List Example
  slug: oracle-goldengate-rest-status-change-list-example
- key_count: 1
  name: Oracle Goldengate Rest Table List Example
  slug: oracle-goldengate-rest-table-list-example
- key_count: 5
  name: Oracle Goldengate Rest Task Example
  slug: oracle-goldengate-rest-task-example
- key_count: 1
  name: Oracle Goldengate Rest Task List Example
  slug: oracle-goldengate-rest-task-list-example
- key_count: 3
  name: Oracle Goldengate Rest Task Summary Example
  slug: oracle-goldengate-rest-task-summary-example
- key_count: 1
  name: Oracle Goldengate Rest Trail List Example
  slug: oracle-goldengate-rest-trail-list-example
- key_count: 2
  name: Oracle Goldengate Rest Trandata Request Example
  slug: oracle-goldengate-rest-trandata-request-example
- key_count: 2
  name: Oracle Goldengate Rest Trandata Response Example
  slug: oracle-goldengate-rest-trandata-response-example
- key_count: 3
  name: Oracle Goldengate Rest Update Collector Path Request Example
  slug: oracle-goldengate-rest-update-collector-path-request-example
- key_count: 3
  name: Oracle Goldengate Rest Update Deployment Request Example
  slug: oracle-goldengate-rest-update-deployment-request-example
- key_count: 3
  name: Oracle Goldengate Rest Update Distribution Path Request Example
  slug: oracle-goldengate-rest-update-distribution-path-request-example
- key_count: 5
  name: Oracle Goldengate Rest Update Extract Request Example
  slug: oracle-goldengate-rest-update-extract-request-example
- key_count: 3
  name: Oracle Goldengate Rest Update Heartbeat Table Request Example
  slug: oracle-goldengate-rest-update-heartbeat-table-request-example
- key_count: 5
  name: Oracle Goldengate Rest Update Replicat Request Example
  slug: oracle-goldengate-rest-update-replicat-request-example
- key_count: 3
  name: Oracle Goldengate Rest Update Service Request Example
  slug: oracle-goldengate-rest-update-service-request-example
- key_count: 3
  name: Oracle Goldengate Rest Update Task Request Example
  slug: oracle-goldengate-rest-update-task-request-example
- key_count: 2
  name: Oracle Goldengate Rest Update User Request Example
  slug: oracle-goldengate-rest-update-user-request-example
- key_count: 3
  name: Oracle Goldengate Rest User Example
  slug: oracle-goldengate-rest-user-example
- key_count: 1
  name: Oracle Goldengate Rest User List Example
  slug: oracle-goldengate-rest-user-list-example
- key_count: 2
  name: Oracle Goldengate Rest Validation Result Example
  slug: oracle-goldengate-rest-validation-result-example
- key_count: 6
  name: Oracle Goldengate Restoredeployment Example
  slug: oracle-goldengate-restoredeployment-example
- key_count: 6
  name: Oracle Goldengate Runjob Example
  slug: oracle-goldengate-runjob-example
- key_count: 6
  name: Oracle Goldengate Startdeployment Example
  slug: oracle-goldengate-startdeployment-example
- key_count: 6
  name: Oracle Goldengate Stopdeployment Example
  slug: oracle-goldengate-stopdeployment-example
- key_count: 6
  name: Oracle Goldengate Stopjob Example
  slug: oracle-goldengate-stopjob-example
- key_count: 3
  name: Oracle Goldengate Stream Analytics Rest Artifact Import Example
  slug: oracle-goldengate-stream-analytics-rest-artifact-import-example
- key_count: 2
  name: Oracle Goldengate Stream Analytics Rest Create User Request Example
  slug: oracle-goldengate-stream-analytics-rest-create-user-request-example
- key_count: 2
  name: Oracle Goldengate Stream Analytics Rest Error Response Example
  slug: oracle-goldengate-stream-analytics-rest-error-response-example
- key_count: 3
  name: Oracle Goldengate Stream Analytics Rest Import Result Example
  slug: oracle-goldengate-stream-analytics-rest-import-result-example
- key_count: 10
  name: Oracle Goldengate Stream Analytics Rest Pipeline Example
  slug: oracle-goldengate-stream-analytics-rest-pipeline-example
- key_count: 3
  name: Oracle Goldengate Stream Analytics Rest Pipeline Export Example
  slug: oracle-goldengate-stream-analytics-rest-pipeline-export-example
- key_count: 1
  name: Oracle Goldengate Stream Analytics Rest Pipeline List Example
  slug: oracle-goldengate-stream-analytics-rest-pipeline-list-example
- key_count: 4
  name: Oracle Goldengate Stream Analytics Rest Pipeline Source Example
  slug: oracle-goldengate-stream-analytics-rest-pipeline-source-example
- key_count: 4
  name: Oracle Goldengate Stream Analytics Rest Pipeline Stage Example
  slug: oracle-goldengate-stream-analytics-rest-pipeline-stage-example
- key_count: 4
  name: Oracle Goldengate Stream Analytics Rest Pipeline Target Example
  slug: oracle-goldengate-stream-analytics-rest-pipeline-target-example
- key_count: 1
  name: Oracle Goldengate Stream Analytics Rest Publish Pipeline Request Example
  slug: oracle-goldengate-stream-analytics-rest-publish-pipeline-request-example
- key_count: 2
  name: Oracle Goldengate Stream Analytics Rest Update User Request Example
  slug: oracle-goldengate-stream-analytics-rest-update-user-request-example
- key_count: 3
  name: Oracle Goldengate Stream Analytics Rest User Example
  slug: oracle-goldengate-stream-analytics-rest-user-example
- key_count: 1
  name: Oracle Goldengate Stream Analytics Rest User List Example
  slug: oracle-goldengate-stream-analytics-rest-user-list-example
- key_count: 6
  name: Oracle Goldengate Unpublishpipeline Example
  slug: oracle-goldengate-unpublishpipeline-example
- key_count: 6
  name: Oracle Goldengate Updateasyncapispec Example
  slug: oracle-goldengate-updateasyncapispec-example
- key_count: 6
  name: Oracle Goldengate Updatecollectorpath Example
  slug: oracle-goldengate-updatecollectorpath-example
- key_count: 6
  name: Oracle Goldengate Updateconnection Example
  slug: oracle-goldengate-updateconnection-example
- key_count: 6
  name: Oracle Goldengate Updatedatabaseregistration Example
  slug: oracle-goldengate-updatedatabaseregistration-example
- key_count: 6
  name: Oracle Goldengate Updatedatastream Example
  slug: oracle-goldengate-updatedatastream-example
- key_count: 6
  name: Oracle Goldengate Updatedeployment Example
  slug: oracle-goldengate-updatedeployment-example
- key_count: 6
  name: Oracle Goldengate Updatedistributionpath Example
  slug: oracle-goldengate-updatedistributionpath-example
- key_count: 6
  name: Oracle Goldengate Updateextract Example
  slug: oracle-goldengate-updateextract-example
- key_count: 6
  name: Oracle Goldengate Updategroup Example
  slug: oracle-goldengate-updategroup-example
- key_count: 6
  name: Oracle Goldengate Updateheartbeattable Example
  slug: oracle-goldengate-updateheartbeattable-example
- key_count: 6
  name: Oracle Goldengate Updatepipeline Example
  slug: oracle-goldengate-updatepipeline-example
- key_count: 6
  name: Oracle Goldengate Updateprofile Example
  slug: oracle-goldengate-updateprofile-example
- key_count: 6
  name: Oracle Goldengate Updatereplicat Example
  slug: oracle-goldengate-updatereplicat-example
- key_count: 6
  name: Oracle Goldengate Updateserverconfiguration Example
  slug: oracle-goldengate-updateserverconfiguration-example
- key_count: 6
  name: Oracle Goldengate Updateservice Example
  slug: oracle-goldengate-updateservice-example
- key_count: 6
  name: Oracle Goldengate Updatetask Example
  slug: oracle-goldengate-updatetask-example
- key_count: 6
  name: Oracle Goldengate Updateuser Example
  slug: oracle-goldengate-updateuser-example
- key_count: 6
  name: Oracle Goldengate Upgradedeployment Example
  slug: oracle-goldengate-upgradedeployment-example
- key_count: 6
  name: Oracle Goldengate Validateagentconnection Example
  slug: oracle-goldengate-validateagentconnection-example
- key_count: 6
  name: Oracle Goldengate Validatecomparepair Example
  slug: oracle-goldengate-validatecomparepair-example
- key_count: 6
  name: Oracle Goldengate Validatecredentialalias Example
  slug: oracle-goldengate-validatecredentialalias-example
- key_count: 6
  name: Oracle Goldengate Validatedatabaseconnection Example
  slug: oracle-goldengate-validatedatabaseconnection-example
- key_count: 6
  name: Oracle Goldengate Validategroup Example
  slug: oracle-goldengate-validategroup-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest Clone Group Request Example
  slug: oracle-goldengate-veridata-rest-clone-group-request-example
- key_count: 3
  name: Oracle Goldengate Veridata Rest Column Mapping Example
  slug: oracle-goldengate-veridata-rest-column-mapping-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest Column Mapping List Example
  slug: oracle-goldengate-veridata-rest-column-mapping-list-example
- key_count: 8
  name: Oracle Goldengate Veridata Rest Compare Pair Example
  slug: oracle-goldengate-veridata-rest-compare-pair-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest Compare Pair List Example
  slug: oracle-goldengate-veridata-rest-compare-pair-list-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest Compare Pair Statistics List Example
  slug: oracle-goldengate-veridata-rest-compare-pair-statistics-list-example
- key_count: 6
  name: Oracle Goldengate Veridata Rest Comparison Report Example
  slug: oracle-goldengate-veridata-rest-comparison-report-example
- key_count: 10
  name: Oracle Goldengate Veridata Rest Connection Example
  slug: oracle-goldengate-veridata-rest-connection-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest Connection List Example
  slug: oracle-goldengate-veridata-rest-connection-list-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest Connection Metadata Example
  slug: oracle-goldengate-veridata-rest-connection-metadata-example
- key_count: 3
  name: Oracle Goldengate Veridata Rest Connection Status Example
  slug: oracle-goldengate-veridata-rest-connection-status-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest Create Compare Pairs Request Example
  slug: oracle-goldengate-veridata-rest-create-compare-pairs-request-example
- key_count: 11
  name: Oracle Goldengate Veridata Rest Create Connection Request Example
  slug: oracle-goldengate-veridata-rest-create-connection-request-example
- key_count: 5
  name: Oracle Goldengate Veridata Rest Create Group Request Example
  slug: oracle-goldengate-veridata-rest-create-group-request-example
- key_count: 4
  name: Oracle Goldengate Veridata Rest Create Job Request Example
  slug: oracle-goldengate-veridata-rest-create-job-request-example
- key_count: 5
  name: Oracle Goldengate Veridata Rest Create Profile Request Example
  slug: oracle-goldengate-veridata-rest-create-profile-request-example
- key_count: 3
  name: Oracle Goldengate Veridata Rest Create User Group Request Example
  slug: oracle-goldengate-veridata-rest-create-user-group-request-example
- key_count: 7
  name: Oracle Goldengate Veridata Rest Create User Request Example
  slug: oracle-goldengate-veridata-rest-create-user-request-example
- key_count: 2
  name: Oracle Goldengate Veridata Rest Error Response Example
  slug: oracle-goldengate-veridata-rest-error-response-example
- key_count: 7
  name: Oracle Goldengate Veridata Rest Group Example
  slug: oracle-goldengate-veridata-rest-group-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest Group List Example
  slug: oracle-goldengate-veridata-rest-group-list-example
- key_count: 3
  name: Oracle Goldengate Veridata Rest Import Result Example
  slug: oracle-goldengate-veridata-rest-import-result-example
- key_count: 6
  name: Oracle Goldengate Veridata Rest Job Example
  slug: oracle-goldengate-veridata-rest-job-example
- key_count: 5
  name: Oracle Goldengate Veridata Rest Job Execution Example
  slug: oracle-goldengate-veridata-rest-job-execution-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest Job List Example
  slug: oracle-goldengate-veridata-rest-job-list-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest Job Statistics List Example
  slug: oracle-goldengate-veridata-rest-job-statistics-list-example
- key_count: 3
  name: Oracle Goldengate Veridata Rest Login Response Example
  slug: oracle-goldengate-veridata-rest-login-response-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest Mapping Object List Example
  slug: oracle-goldengate-veridata-rest-mapping-object-list-example
- key_count: 3
  name: Oracle Goldengate Veridata Rest Mapping Rules Request Example
  slug: oracle-goldengate-veridata-rest-mapping-rules-request-example
- key_count: 2
  name: Oracle Goldengate Veridata Rest Metadata Request Example
  slug: oracle-goldengate-veridata-rest-metadata-request-example
- key_count: 2
  name: Oracle Goldengate Veridata Rest Out Of Sync Data Example
  slug: oracle-goldengate-veridata-rest-out-of-sync-data-example
- key_count: 7
  name: Oracle Goldengate Veridata Rest Profile Example
  slug: oracle-goldengate-veridata-rest-profile-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest Profile List Example
  slug: oracle-goldengate-veridata-rest-profile-list-example
- key_count: 3
  name: Oracle Goldengate Veridata Rest Repair Execution Example
  slug: oracle-goldengate-veridata-rest-repair-execution-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest Repair Job Request Example
  slug: oracle-goldengate-veridata-rest-repair-job-request-example
- key_count: 6
  name: Oracle Goldengate Veridata Rest Repair Report Example
  slug: oracle-goldengate-veridata-rest-repair-report-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest Repair Statistics List Example
  slug: oracle-goldengate-veridata-rest-repair-statistics-list-example
- key_count: 2
  name: Oracle Goldengate Veridata Rest Repaired Row Details Example
  slug: oracle-goldengate-veridata-rest-repaired-row-details-example
- key_count: 5
  name: Oracle Goldengate Veridata Rest Replace Compare Pair Request Example
  slug: oracle-goldengate-veridata-rest-replace-compare-pair-request-example
- key_count: 4
  name: Oracle Goldengate Veridata Rest Replace Job Request Example
  slug: oracle-goldengate-veridata-rest-replace-job-request-example
- key_count: 3
  name: Oracle Goldengate Veridata Rest Replace User Group Request Example
  slug: oracle-goldengate-veridata-rest-replace-user-group-request-example
- key_count: 5
  name: Oracle Goldengate Veridata Rest Replace User Request Example
  slug: oracle-goldengate-veridata-rest-replace-user-request-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest Run Job Request Example
  slug: oracle-goldengate-veridata-rest-run-job-request-example
- key_count: 4
  name: Oracle Goldengate Veridata Rest Server Configuration Example
  slug: oracle-goldengate-veridata-rest-server-configuration-example
- key_count: 4
  name: Oracle Goldengate Veridata Rest Server Info Example
  slug: oracle-goldengate-veridata-rest-server-info-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest Server Logs Example
  slug: oracle-goldengate-veridata-rest-server-logs-example
- key_count: 6
  name: Oracle Goldengate Veridata Rest Update Connection Request Example
  slug: oracle-goldengate-veridata-rest-update-connection-request-example
- key_count: 3
  name: Oracle Goldengate Veridata Rest Update Group Request Example
  slug: oracle-goldengate-veridata-rest-update-group-request-example
- key_count: 4
  name: Oracle Goldengate Veridata Rest Update Profile Request Example
  slug: oracle-goldengate-veridata-rest-update-profile-request-example
- key_count: 3
  name: Oracle Goldengate Veridata Rest Update Server Configuration Request Example
  slug: oracle-goldengate-veridata-rest-update-server-configuration-request-example
- key_count: 7
  name: Oracle Goldengate Veridata Rest User Example
  slug: oracle-goldengate-veridata-rest-user-example
- key_count: 4
  name: Oracle Goldengate Veridata Rest User Group Example
  slug: oracle-goldengate-veridata-rest-user-group-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest User Group List Example
  slug: oracle-goldengate-veridata-rest-user-group-list-example
- key_count: 1
  name: Oracle Goldengate Veridata Rest User List Example
  slug: oracle-goldengate-veridata-rest-user-list-example
- key_count: 2
  name: Oracle Goldengate Veridata Rest Validate Connection Request Example
  slug: oracle-goldengate-veridata-rest-validate-connection-request-example
- key_count: 6
  name: Oracle Goldengate Veridata Rest Validate Database Request Example
  slug: oracle-goldengate-veridata-rest-validate-database-request-example
- key_count: 2
  name: Oracle Goldengate Veridata Rest Validation Result Example
  slug: oracle-goldengate-veridata-rest-validation-result-example
features:
- Real-time data replication across heterogeneous databases
- Change data capture (CDC) with minimal impact on source systems
- Zero-downtime migration and database upgrades
- Multi-cloud and hybrid cloud data integration
- Bidirectional replication for active-active architectures
- Stream analytics for real-time event processing
- Data verification and repair with Veridata
- Big data target support including Kafka, HDFS, and MongoDB
finops:
- name: Oracle Goldengate Finops
  service_category: Data Integration
  slug: oracle-goldengate-finops
image: /assets/icons/oracle-goldengate.png
integrations:
- Oracle Database
- MySQL
- PostgreSQL
- SQL Server
- MongoDB
- Apache Kafka
- Apache Hadoop / HDFS
- Elasticsearch
- Google BigQuery
- Amazon Kinesis
- Snowflake
- Oracle Cloud Infrastructure
json_schemas:
- name: ApiVersionDetails
  property_count: 4
  slug: oracle-goldengate-apiversiondetails
- name: ApiVersionList
  property_count: 1
  slug: oracle-goldengate-apiversionlist
- name: ArtifactImport
  property_count: 3
  slug: oracle-goldengate-artifactimport
- name: CommandResponse
  property_count: 1
  slug: oracle-goldengate-big-data-rest-command-response
- name: ConfigFileContent
  property_count: 1
  slug: oracle-goldengate-big-data-rest-config-file-content
- name: ConfigFileList
  property_count: 1
  slug: oracle-goldengate-big-data-rest-config-file-list
- name: ConfigFile
  property_count: 2
  slug: oracle-goldengate-big-data-rest-config-file
- name: CreateCredentialRequest
  property_count: 2
  slug: oracle-goldengate-big-data-rest-create-credential-request
- name: CreateDistributionPathRequest
  property_count: 2
  slug: oracle-goldengate-big-data-rest-create-distribution-path-request
- name: CreateExtractRequest
  property_count: 4
  slug: oracle-goldengate-big-data-rest-create-extract-request
- name: CreateReplicatRequest
  property_count: 5
  slug: oracle-goldengate-big-data-rest-create-replicat-request
- name: CredentialAlias
  property_count: 3
  slug: oracle-goldengate-big-data-rest-credential-alias
- name: CredentialDomainList
  property_count: 1
  slug: oracle-goldengate-big-data-rest-credential-domain-list
- name: DataTargetTypeList
  property_count: 1
  slug: oracle-goldengate-big-data-rest-data-target-type-list
- name: DataTargetTypeSchema
  property_count: 2
  slug: oracle-goldengate-big-data-rest-data-target-type-schema
- name: DistributionPathList
  property_count: 1
  slug: oracle-goldengate-big-data-rest-distribution-path-list
- name: DistributionPath
  property_count: 4
  slug: oracle-goldengate-big-data-rest-distribution-path
- name: DistributionPathSummary
  property_count: 4
  slug: oracle-goldengate-big-data-rest-distribution-path-summary
- name: ErrorResponse
  property_count: 3
  slug: oracle-goldengate-big-data-rest-error-response
- name: ExecuteCommandRequest
  property_count: 1
  slug: oracle-goldengate-big-data-rest-execute-command-request
- name: ExtractList
  property_count: 1
  slug: oracle-goldengate-big-data-rest-extract-list
- name: Extract
  property_count: 5
  slug: oracle-goldengate-big-data-rest-extract
- name: ExtractSummary
  property_count: 3
  slug: oracle-goldengate-big-data-rest-extract-summary
- name: ProcessCommand
  property_count: 1
  slug: oracle-goldengate-big-data-rest-process-command
- name: ProcessMetricsList
  property_count: 1
  slug: oracle-goldengate-big-data-rest-process-metrics-list
- name: ProcessStatus
  property_count: 4
  slug: oracle-goldengate-big-data-rest-process-status
- name: ReplicatList
  property_count: 1
  slug: oracle-goldengate-big-data-rest-replicat-list
- name: Replicat
  property_count: 7
  slug: oracle-goldengate-big-data-rest-replicat
- name: ReplicatStatistics
  property_count: 6
  slug: oracle-goldengate-big-data-rest-replicat-statistics
- name: ReplicatSummary
  property_count: 4
  slug: oracle-goldengate-big-data-rest-replicat-summary
- name: ServiceHealth
  property_count: 2
  slug: oracle-goldengate-big-data-rest-service-health
- name: TrailList
  property_count: 1
  slug: oracle-goldengate-big-data-rest-trail-list
- name: UpdateExtractRequest
  property_count: 2
  slug: oracle-goldengate-big-data-rest-update-extract-request
- name: UpdateReplicatRequest
  property_count: 2
  slug: oracle-goldengate-big-data-rest-update-replicat-request
- name: BulkCreateUsersRequest
  property_count: 1
  slug: oracle-goldengate-bulkcreateusersrequest
- name: CacheStatistics
  property_count: 4
  slug: oracle-goldengate-cachestatistics
- name: Certificate
  property_count: 13
  slug: oracle-goldengate-certificate
- name: CertificateCollection
  property_count: 1
  slug: oracle-goldengate-certificatecollection
- name: CertificateNameList
  property_count: 1
  slug: oracle-goldengate-certificatenamelist
- name: CertificateSummary
  property_count: 4
  slug: oracle-goldengate-certificatesummary
- name: CertificateTypeList
  property_count: 1
  slug: oracle-goldengate-certificatetypelist
- name: ChangeCompartmentDetails
  property_count: 1
  slug: oracle-goldengate-changecompartmentdetails
- name: Checkpoints
  property_count: 3
  slug: oracle-goldengate-checkpoints
- name: CloneGroupRequest
  property_count: 1
  slug: oracle-goldengate-clonegrouprequest
- name: CertificateCollection
  property_count: 1
  slug: oracle-goldengate-cloud-service-certificate-collection
- name: Certificate
  property_count: 13
  slug: oracle-goldengate-cloud-service-certificate
- name: CertificateSummary
  property_count: 4
  slug: oracle-goldengate-cloud-service-certificate-summary
- name: ChangeCompartmentDetails
  property_count: 1
  slug: oracle-goldengate-cloud-service-change-compartment-details
- name: CollectDiagnosticsDetails
  property_count: 3
  slug: oracle-goldengate-cloud-service-collect-diagnostics-details
- name: ConnectionAssignmentCollection
  property_count: 1
  slug: oracle-goldengate-cloud-service-connection-assignment-collection
- name: ConnectionAssignment
  property_count: 7
  slug: oracle-goldengate-cloud-service-connection-assignment
- name: ConnectionAssignmentSummary
  property_count: 4
  slug: oracle-goldengate-cloud-service-connection-assignment-summary
- name: ConnectionCollection
  property_count: 1
  slug: oracle-goldengate-cloud-service-connection-collection
- name: Connection
  property_count: 10
  slug: oracle-goldengate-cloud-service-connection
- name: ConnectionSummary
  property_count: 5
  slug: oracle-goldengate-cloud-service-connection-summary
- name: CreateCertificateDetails
  property_count: 2
  slug: oracle-goldengate-cloud-service-create-certificate-details
- name: CreateConnectionAssignmentDetails
  property_count: 2
  slug: oracle-goldengate-cloud-service-create-connection-assignment-details
- name: CreateConnectionDetails
  property_count: 6
  slug: oracle-goldengate-cloud-service-create-connection-details
- name: CreateDatabaseRegistrationDetails
  property_count: 8
  slug: oracle-goldengate-cloud-service-create-database-registration-details
- name: CreateDeploymentBackupDetails
  property_count: 6
  slug: oracle-goldengate-cloud-service-create-deployment-backup-details
- name: CreateDeploymentDetails
  property_count: 12
  slug: oracle-goldengate-cloud-service-create-deployment-details
- name: CreatePipelineDetails
  property_count: 5
  slug: oracle-goldengate-cloud-service-create-pipeline-details
- name: DatabaseRegistrationCollection
  property_count: 1
  slug: oracle-goldengate-cloud-service-database-registration-collection
- name: DatabaseRegistration
  property_count: 10
  slug: oracle-goldengate-cloud-service-database-registration
- name: DatabaseRegistrationSummary
  property_count: 4
  slug: oracle-goldengate-cloud-service-database-registration-summary
- name: DeploymentBackupCollection
  property_count: 1
  slug: oracle-goldengate-cloud-service-deployment-backup-collection
- name: DeploymentBackup
  property_count: 9
  slug: oracle-goldengate-cloud-service-deployment-backup
- name: DeploymentBackupSummary
  property_count: 5
  slug: oracle-goldengate-cloud-service-deployment-backup-summary
- name: DeploymentCollection
  property_count: 1
  slug: oracle-goldengate-cloud-service-deployment-collection
- name: Deployment
  property_count: 19
  slug: oracle-goldengate-cloud-service-deployment
- name: DeploymentSummary
  property_count: 6
  slug: oracle-goldengate-cloud-service-deployment-summary
- name: DeploymentVersionCollection
  property_count: 1
  slug: oracle-goldengate-cloud-service-deployment-version-collection
- name: Error
  property_count: 2
  slug: oracle-goldengate-cloud-service-error
- name: PipelineCollection
  property_count: 1
  slug: oracle-goldengate-cloud-service-pipeline-collection
- name: Pipeline
  property_count: 9
  slug: oracle-goldengate-cloud-service-pipeline
- name: PipelineSummary
  property_count: 4
  slug: oracle-goldengate-cloud-service-pipeline-summary
- name: RestoreDeploymentDetails
  property_count: 1
  slug: oracle-goldengate-cloud-service-restore-deployment-details
- name: StartDeploymentDetails
  property_count: 1
  slug: oracle-goldengate-cloud-service-start-deployment-details
- name: StopDeploymentDetails
  property_count: 1
  slug: oracle-goldengate-cloud-service-stop-deployment-details
- name: UpdateConnectionDetails
  property_count: 3
  slug: oracle-goldengate-cloud-service-update-connection-details
- name: UpdateDatabaseRegistrationDetails
  property_count: 6
  slug: oracle-goldengate-cloud-service-update-database-registration-details
- name: UpdateDeploymentDetails
  property_count: 7
  slug: oracle-goldengate-cloud-service-update-deployment-details
- name: UpdatePipelineDetails
  property_count: 2
  slug: oracle-goldengate-cloud-service-update-pipeline-details
- name: UpgradeDeploymentDetails
  property_count: 2
  slug: oracle-goldengate-cloud-service-upgrade-deployment-details
- name: WorkRequestCollection
  property_count: 1
  slug: oracle-goldengate-cloud-service-work-request-collection
- name: WorkRequestErrorCollection
  property_count: 1
  slug: oracle-goldengate-cloud-service-work-request-error-collection
- name: WorkRequestLogEntryCollection
  property_count: 1
  slug: oracle-goldengate-cloud-service-work-request-log-entry-collection
- name: WorkRequest
  property_count: 8
  slug: oracle-goldengate-cloud-service-work-request
- name: WorkRequestSummary
  property_count: 5
  slug: oracle-goldengate-cloud-service-work-request-summary
- name: CollectDiagnosticsDetails
  property_count: 3
  slug: oracle-goldengate-collectdiagnosticsdetails
- name: CollectorPath
  property_count: 4
  slug: oracle-goldengate-collectorpath
- name: CollectorPathList
  property_count: 1
  slug: oracle-goldengate-collectorpathlist
- name: CollectorPathSummary
  property_count: 2
  slug: oracle-goldengate-collectorpathsummary
- name: ColumnMapping
  property_count: 3
  slug: oracle-goldengate-columnmapping
- name: ColumnMappingList
  property_count: 1
  slug: oracle-goldengate-columnmappinglist
- name: CommandResponse
  property_count: 1
  slug: oracle-goldengate-commandresponse
- name: ComparePair
  property_count: 8
  slug: oracle-goldengate-comparepair
- name: ComparePairList
  property_count: 1
  slug: oracle-goldengate-comparepairlist
- name: ComparePairStatisticsList
  property_count: 1
  slug: oracle-goldengate-comparepairstatisticslist
- name: ComparisonReport
  property_count: 6
  slug: oracle-goldengate-comparisonreport
- name: ConfigFile
  property_count: 2
  slug: oracle-goldengate-configfile
- name: ConfigFileContent
  property_count: 1
  slug: oracle-goldengate-configfilecontent
- name: ConfigFileList
  property_count: 1
  slug: oracle-goldengate-configfilelist
- name: ConfigSummary
  property_count: 5
  slug: oracle-goldengate-configsummary
- name: ConfigTypeList
  property_count: 1
  slug: oracle-goldengate-configtypelist
- name: Connection
  property_count: 10
  slug: oracle-goldengate-connection
- name: ConnectionAssignment
  property_count: 7
  slug: oracle-goldengate-connectionassignment
- name: ConnectionAssignmentCollection
  property_count: 1
  slug: oracle-goldengate-connectionassignmentcollection
- name: ConnectionAssignmentSummary
  property_count: 4
  slug: oracle-goldengate-connectionassignmentsummary
- name: ConnectionCollection
  property_count: 1
  slug: oracle-goldengate-connectioncollection
- name: ConnectionList
  property_count: 1
  slug: oracle-goldengate-connectionlist
- name: ConnectionMetadata
  property_count: 1
  slug: oracle-goldengate-connectionmetadata
- name: ConnectionStatus
  property_count: 3
  slug: oracle-goldengate-connectionstatus
- name: ConnectionSummary
  property_count: 5
  slug: oracle-goldengate-connectionsummary
- name: CreateCertificateDetails
  property_count: 2
  slug: oracle-goldengate-createcertificatedetails
- name: CreateCollectorPathRequest
  property_count: 2
  slug: oracle-goldengate-createcollectorpathrequest
- name: CreateComparePairsRequest
  property_count: 1
  slug: oracle-goldengate-createcomparepairsrequest
- name: CreateConnectionAssignmentDetails
  property_count: 2
  slug: oracle-goldengate-createconnectionassignmentdetails
- name: CreateConnectionDetails
  property_count: 6
  slug: oracle-goldengate-createconnectiondetails
- name: CreateConnectionRequest
  property_count: 3
  slug: oracle-goldengate-createconnectionrequest
- name: CreateCredentialAliasRequest
  property_count: 2
  slug: oracle-goldengate-createcredentialaliasrequest
- name: CreateCredentialRequest
  property_count: 2
  slug: oracle-goldengate-createcredentialrequest
- name: CreateDatabaseRegistrationDetails
  property_count: 8
  slug: oracle-goldengate-createdatabaseregistrationdetails
- name: CreateDataStreamRequest
  property_count: 4
  slug: oracle-goldengate-createdatastreamrequest
- name: CreateDeploymentBackupDetails
  property_count: 6
  slug: oracle-goldengate-createdeploymentbackupdetails
- name: CreateDeploymentDetails
  property_count: 12
  slug: oracle-goldengate-createdeploymentdetails
- name: CreateDeploymentRequest
  property_count: 4
  slug: oracle-goldengate-createdeploymentrequest
- name: CreateDistributionPathRequest
  property_count: 2
  slug: oracle-goldengate-createdistributionpathrequest
- name: CreateExtractRequest
  property_count: 4
  slug: oracle-goldengate-createextractrequest
- name: CreateGroupRequest
  property_count: 5
  slug: oracle-goldengate-creategrouprequest
- name: CreateHeartbeatTableRequest
  property_count: 4
  slug: oracle-goldengate-createheartbeattablerequest
- name: CreateJobRequest
  property_count: 4
  slug: oracle-goldengate-createjobrequest
- name: CreatePipelineDetails
  property_count: 5
  slug: oracle-goldengate-createpipelinedetails
- name: CreateProfileRequest
  property_count: 5
  slug: oracle-goldengate-createprofilerequest
- name: CreateReplicatRequest
  property_count: 5
  slug: oracle-goldengate-createreplicatrequest
- name: CreateServiceRequest
  property_count: 3
  slug: oracle-goldengate-createservicerequest
- name: CreateTaskRequest
  property_count: 3
  slug: oracle-goldengate-createtaskrequest
- name: CreateUserGroupRequest
  property_count: 3
  slug: oracle-goldengate-createusergrouprequest
- name: CreateUserRequest
  property_count: 2
  slug: oracle-goldengate-createuserrequest
- name: CredentialAlias
  property_count: 3
  slug: oracle-goldengate-credentialalias
- name: CredentialAliasList
  property_count: 1
  slug: oracle-goldengate-credentialaliaslist
- name: CredentialDomainList
  property_count: 1
  slug: oracle-goldengate-credentialdomainlist
- name: CreateDataStreamRequest
  property_count: 4
  slug: oracle-goldengate-data-streams-rest-create-data-stream-request
- name: DataStreamList
  property_count: 1
  slug: oracle-goldengate-data-streams-rest-data-stream-list
- name: DataStream
  property_count: 9
  slug: oracle-goldengate-data-streams-rest-data-stream
- name: DataStreamSummary
  property_count: 3
  slug: oracle-goldengate-data-streams-rest-data-stream-summary
- name: ErrorResponse
  property_count: 2
  slug: oracle-goldengate-data-streams-rest-error-response
- name: UpdateDataStreamRequest
  property_count: 4
  slug: oracle-goldengate-data-streams-rest-update-data-stream-request
- name: DatabaseConnection
  property_count: 4
  slug: oracle-goldengate-databaseconnection
- name: DatabaseNameList
  property_count: 1
  slug: oracle-goldengate-databasenamelist
- name: DatabaseRegistration
  property_count: 10
  slug: oracle-goldengate-databaseregistration
- name: DatabaseRegistrationCollection
  property_count: 1
  slug: oracle-goldengate-databaseregistrationcollection
- name: DatabaseRegistrationSummary
  property_count: 4
  slug: oracle-goldengate-databaseregistrationsummary
- name: DatabaseStatistics
  property_count: 6
  slug: oracle-goldengate-databasestatistics
- name: DataStream
  property_count: 9
  slug: oracle-goldengate-datastream
- name: DataStreamList
  property_count: 1
  slug: oracle-goldengate-datastreamlist
- name: DataStreamSummary
  property_count: 3
  slug: oracle-goldengate-datastreamsummary
- name: DataTargetTypeList
  property_count: 1
  slug: oracle-goldengate-datatargettypelist
- name: DataTargetTypeSchema
  property_count: 2
  slug: oracle-goldengate-datatargettypeschema
- name: Oracle GoldenGate Deployment
  property_count: 10
  slug: oracle-goldengate-deployment
- name: DeploymentBackup
  property_count: 9
  slug: oracle-goldengate-deploymentbackup
- name: DeploymentBackupCollection
  property_count: 1
  slug: oracle-goldengate-deploymentbackupcollection
- name: DeploymentBackupSummary
  property_count: 5
  slug: oracle-goldengate-deploymentbackupsummary
- name: DeploymentCollection
  property_count: 1
  slug: oracle-goldengate-deploymentcollection
- name: DeploymentList
  property_count: 1
  slug: oracle-goldengate-deploymentlist
- name: DeploymentSummary
  property_count: 6
  slug: oracle-goldengate-deploymentsummary
- name: DeploymentVersionCollection
  property_count: 1
  slug: oracle-goldengate-deploymentversioncollection
- name: DistributionPath
  property_count: 4
  slug: oracle-goldengate-distributionpath
- name: DistributionPathList
  property_count: 1
  slug: oracle-goldengate-distributionpathlist
- name: DistributionPathSummary
  property_count: 4
  slug: oracle-goldengate-distributionpathsummary
- name: EncryptionKey
  property_count: 3
  slug: oracle-goldengate-encryptionkey
- name: EncryptionKeyList
  property_count: 1
  slug: oracle-goldengate-encryptionkeylist
- name: Error
  property_count: 2
  slug: oracle-goldengate-error
- name: ErrorResponse
  property_count: 3
  slug: oracle-goldengate-errorresponse
- name: EventList
  property_count: 1
  slug: oracle-goldengate-eventlist
- name: ExecuteCommandRequest
  property_count: 1
  slug: oracle-goldengate-executecommandrequest
- name: Extract
  property_count: 5
  slug: oracle-goldengate-extract
- name: ExtractList
  property_count: 1
  slug: oracle-goldengate-extractlist
- name: ExtractSummary
  property_count: 3
  slug: oracle-goldengate-extractsummary
- name: ExtractTrailList
  property_count: 1
  slug: oracle-goldengate-extracttraillist
- name: Group
  property_count: 7
  slug: oracle-goldengate-group
- name: GroupList
  property_count: 1
  slug: oracle-goldengate-grouplist
- name: HealthCheckSummary
  property_count: 3
  slug: oracle-goldengate-healthchecksummary
- name: HeartbeatEntries
  property_count: 1
  slug: oracle-goldengate-heartbeatentries
- name: HeartbeatMetrics
  property_count: 3
  slug: oracle-goldengate-heartbeatmetrics
- name: HeartbeatTable
  property_count: 5
  slug: oracle-goldengate-heartbeattable
- name: ImportResult
  property_count: 3
  slug: oracle-goldengate-importresult
- name: Job
  property_count: 6
  slug: oracle-goldengate-job
- name: JobExecution
  property_count: 5
  slug: oracle-goldengate-jobexecution
- name: JobList
  property_count: 1
  slug: oracle-goldengate-joblist
- name: JobStatisticsList
  property_count: 1
  slug: oracle-goldengate-jobstatisticslist
- name: Link
  property_count: 3
  slug: oracle-goldengate-link
- name: LogContent
  property_count: 3
  slug: oracle-goldengate-logcontent
- name: LoginResponse
  property_count: 3
  slug: oracle-goldengate-loginresponse
- name: LogList
  property_count: 1
  slug: oracle-goldengate-loglist
- name: MappingObjectList
  property_count: 1
  slug: oracle-goldengate-mappingobjectlist
- name: MappingRulesRequest
  property_count: 3
  slug: oracle-goldengate-mappingrulesrequest
- name: MasterKeyVersion
  property_count: 3
  slug: oracle-goldengate-masterkeyversion
- name: MasterKeyVersionList
  property_count: 1
  slug: oracle-goldengate-masterkeyversionlist
- name: MessageCodeList
  property_count: 1
  slug: oracle-goldengate-messagecodelist
- name: MessageExplanation
  property_count: 4
  slug: oracle-goldengate-messageexplanation
- name: MessageList
  property_count: 1
  slug: oracle-goldengate-messagelist
- name: MetadataRequest
  property_count: 2
  slug: oracle-goldengate-metadatarequest
- name: ModifyLogRequest
  property_count: 1
  slug: oracle-goldengate-modifylogrequest
- name: MonitoringMessageList
  property_count: 1
  slug: oracle-goldengate-monitoringmessagelist
- name: OutOfSyncData
  property_count: 2
  slug: oracle-goldengate-outofsyncdata
- name: ParameterInfo
  property_count: 5
  slug: oracle-goldengate-parameterinfo
- name: ParameterNameList
  property_count: 1
  slug: oracle-goldengate-parameternamelist
- name: PathStatistics
  property_count: 4
  slug: oracle-goldengate-pathstatistics
- name: Pipeline
  property_count: 9
  slug: oracle-goldengate-pipeline
- name: PipelineCollection
  property_count: 1
  slug: oracle-goldengate-pipelinecollection
- name: PipelineExport
  property_count: 4
  slug: oracle-goldengate-pipelineexport
- name: PipelineList
  property_count: 1
  slug: oracle-goldengate-pipelinelist
- name: PipelineSource
  property_count: 4
  slug: oracle-goldengate-pipelinesource
- name: PipelineStage
  property_count: 4
  slug: oracle-goldengate-pipelinestage
- name: PipelineSummary
  property_count: 4
  slug: oracle-goldengate-pipelinesummary
- name: PipelineTarget
  property_count: 4
  slug: oracle-goldengate-pipelinetarget
- name: ProcessCommand
  property_count: 1
  slug: oracle-goldengate-processcommand
- name: ProcessHistory
  property_count: 2
  slug: oracle-goldengate-processhistory
- name: ProcessMetrics
  property_count: 8
  slug: oracle-goldengate-processmetrics
- name: ProcessMetricsList
  property_count: 1
  slug: oracle-goldengate-processmetricslist
- name: ProcessPerformance
  property_count: 4
  slug: oracle-goldengate-processperformance
- name: ProcessStatus
  property_count: 4
  slug: oracle-goldengate-processstatus
- name: Profile
  property_count: 7
  slug: oracle-goldengate-profile
- name: ProfileList
  property_count: 1
  slug: oracle-goldengate-profilelist
- name: PublishPipelineRequest
  property_count: 1
  slug: oracle-goldengate-publishpipelinerequest
- name: RepairedRowDetails
  property_count: 2
  slug: oracle-goldengate-repairedrowdetails
- name: RepairExecution
  property_count: 3
  slug: oracle-goldengate-repairexecution
- name: RepairJobRequest
  property_count: 1
  slug: oracle-goldengate-repairjobrequest
- name: RepairReport
  property_count: 6
  slug: oracle-goldengate-repairreport
- name: RepairStatisticsList
  property_count: 1
  slug: oracle-goldengate-repairstatisticslist
- name: ReplaceComparePairRequest
  property_count: 5
  slug: oracle-goldengate-replacecomparepairrequest
- name: ReplaceJobRequest
  property_count: 4
  slug: oracle-goldengate-replacejobrequest
- name: ReplaceUserGroupRequest
  property_count: 3
  slug: oracle-goldengate-replaceusergrouprequest
- name: ReplaceUserRequest
  property_count: 5
  slug: oracle-goldengate-replaceuserrequest
- name: Replicat
  property_count: 7
  slug: oracle-goldengate-replicat
- name: ReplicatList
  property_count: 1
  slug: oracle-goldengate-replicatlist
- name: ReplicatStatistics
  property_count: 6
  slug: oracle-goldengate-replicatstatistics
- name: ReplicatSummary
  property_count: 4
  slug: oracle-goldengate-replicatsummary
- name: Report
  property_count: 2
  slug: oracle-goldengate-report
- name: ReportList
  property_count: 1
  slug: oracle-goldengate-reportlist
- name: RequestList
  property_count: 1
  slug: oracle-goldengate-requestlist
- name: RequestStatus
  property_count: 5
  slug: oracle-goldengate-requeststatus
- name: ApiVersionDetails
  property_count: 4
  slug: oracle-goldengate-rest-api-version-details
- name: ApiVersionList
  property_count: 1
  slug: oracle-goldengate-rest-api-version-list
- name: BulkCreateUsersRequest
  property_count: 1
  slug: oracle-goldengate-rest-bulk-create-users-request
- name: CacheStatistics
  property_count: 4
  slug: oracle-goldengate-rest-cache-statistics
- name: CertificateNameList
  property_count: 1
  slug: oracle-goldengate-rest-certificate-name-list
- name: Certificate
  property_count: 6
  slug: oracle-goldengate-rest-certificate
- name: CertificateTypeList
  property_count: 1
  slug: oracle-goldengate-rest-certificate-type-list
- name: Checkpoints
  property_count: 3
  slug: oracle-goldengate-rest-checkpoints
- name: CollectorPathList
  property_count: 1
  slug: oracle-goldengate-rest-collector-path-list
- name: CollectorPath
  property_count: 4
  slug: oracle-goldengate-rest-collector-path
- name: CollectorPathSummary
  property_count: 2
  slug: oracle-goldengate-rest-collector-path-summary
- name: CommandResponse
  property_count: 1
  slug: oracle-goldengate-rest-command-response
- name: ConfigFileContent
  property_count: 1
  slug: oracle-goldengate-rest-config-file-content
- name: ConfigFileList
  property_count: 1
  slug: oracle-goldengate-rest-config-file-list
- name: ConfigFile
  property_count: 3
  slug: oracle-goldengate-rest-config-file
- name: ConfigSummary
  property_count: 5
  slug: oracle-goldengate-rest-config-summary
- name: ConfigTypeList
  property_count: 1
  slug: oracle-goldengate-rest-config-type-list
- name: ConnectionList
  property_count: 1
  slug: oracle-goldengate-rest-connection-list
- name: CreateCollectorPathRequest
  property_count: 2
  slug: oracle-goldengate-rest-create-collector-path-request
- name: CreateConnectionRequest
  property_count: 3
  slug: oracle-goldengate-rest-create-connection-request
- name: CreateCredentialAliasRequest
  property_count: 2
  slug: oracle-goldengate-rest-create-credential-alias-request
- name: CreateDeploymentRequest
  property_count: 4
  slug: oracle-goldengate-rest-create-deployment-request
- name: CreateDistributionPathRequest
  property_count: 4
  slug: oracle-goldengate-rest-create-distribution-path-request
- name: CreateExtractRequest
  property_count: 8
  slug: oracle-goldengate-rest-create-extract-request
- name: CreateHeartbeatTableRequest
  property_count: 4
  slug: oracle-goldengate-rest-create-heartbeat-table-request
- name: CreateReplicatRequest
  property_count: 7
  slug: oracle-goldengate-rest-create-replicat-request
- name: CreateServiceRequest
  property_count: 3
  slug: oracle-goldengate-rest-create-service-request
- name: CreateTaskRequest
  property_count: 3
  slug: oracle-goldengate-rest-create-task-request
- name: CreateUserRequest
  property_count: 2
  slug: oracle-goldengate-rest-create-user-request
- name: CredentialAliasList
  property_count: 1
  slug: oracle-goldengate-rest-credential-alias-list
- name: CredentialAlias
  property_count: 3
  slug: oracle-goldengate-rest-credential-alias
- name: CredentialDomainList
  property_count: 1
  slug: oracle-goldengate-rest-credential-domain-list
- name: DatabaseConnection
  property_count: 4
  slug: oracle-goldengate-rest-database-connection
- name: DatabaseNameList
  property_count: 1
  slug: oracle-goldengate-rest-database-name-list
- name: DatabaseStatistics
  property_count: 6
  slug: oracle-goldengate-rest-database-statistics
- name: DeploymentList
  property_count: 1
  slug: oracle-goldengate-rest-deployment-list
- name: Deployment
  property_count: 7
  slug: oracle-goldengate-rest-deployment
- name: DeploymentSummary
  property_count: 3
  slug: oracle-goldengate-rest-deployment-summary
- name: DistributionPathList
  property_count: 1
  slug: oracle-goldengate-rest-distribution-path-list
- name: DistributionPath
  property_count: 6
  slug: oracle-goldengate-rest-distribution-path
- name: DistributionPathSummary
  property_count: 4
  slug: oracle-goldengate-rest-distribution-path-summary
- name: EncryptionKeyList
  property_count: 1
  slug: oracle-goldengate-rest-encryption-key-list
- name: EncryptionKey
  property_count: 3
  slug: oracle-goldengate-rest-encryption-key
- name: ErrorResponse
  property_count: 3
  slug: oracle-goldengate-rest-error-response
- name: EventList
  property_count: 1
  slug: oracle-goldengate-rest-event-list
- name: ExecuteCommandRequest
  property_count: 1
  slug: oracle-goldengate-rest-execute-command-request
- name: ExtractList
  property_count: 1
  slug: oracle-goldengate-rest-extract-list
- name: Extract
  property_count: 10
  slug: oracle-goldengate-rest-extract
- name: ExtractSummary
  property_count: 4
  slug: oracle-goldengate-rest-extract-summary
- name: ExtractTrailList
  property_count: 1
  slug: oracle-goldengate-rest-extract-trail-list
- name: HealthCheckSummary
  property_count: 3
  slug: oracle-goldengate-rest-health-check-summary
- name: HeartbeatEntries
  property_count: 1
  slug: oracle-goldengate-rest-heartbeat-entries
- name: HeartbeatMetrics
  property_count: 3
  slug: oracle-goldengate-rest-heartbeat-metrics
- name: HeartbeatTable
  property_count: 5
  slug: oracle-goldengate-rest-heartbeat-table
- name: Link
  property_count: 3
  slug: oracle-goldengate-rest-link
- name: LogContent
  property_count: 3
  slug: oracle-goldengate-rest-log-content
- name: LogList
  property_count: 1
  slug: oracle-goldengate-rest-log-list
- name: MasterKeyVersionList
  property_count: 1
  slug: oracle-goldengate-rest-master-key-version-list
- name: MasterKeyVersion
  property_count: 3
  slug: oracle-goldengate-rest-master-key-version
- name: MessageCodeList
  property_count: 1
  slug: oracle-goldengate-rest-message-code-list
- name: MessageExplanation
  property_count: 4
  slug: oracle-goldengate-rest-message-explanation
- name: MessageList
  property_count: 1
  slug: oracle-goldengate-rest-message-list
- name: ModifyLogRequest
  property_count: 1
  slug: oracle-goldengate-rest-modify-log-request
- name: MonitoringMessageList
  property_count: 1
  slug: oracle-goldengate-rest-monitoring-message-list
- name: ParameterInfo
  property_count: 5
  slug: oracle-goldengate-rest-parameter-info
- name: ParameterNameList
  property_count: 1
  slug: oracle-goldengate-rest-parameter-name-list
- name: PathStatistics
  property_count: 4
  slug: oracle-goldengate-rest-path-statistics
- name: ProcessCommand
  property_count: 2
  slug: oracle-goldengate-rest-process-command
- name: ProcessHistory
  property_count: 2
  slug: oracle-goldengate-rest-process-history
- name: ProcessMetricsList
  property_count: 1
  slug: oracle-goldengate-rest-process-metrics-list
- name: ProcessMetrics
  property_count: 8
  slug: oracle-goldengate-rest-process-metrics
- name: ProcessPerformance
  property_count: 4
  slug: oracle-goldengate-rest-process-performance
- name: ProcessStatus
  property_count: 5
  slug: oracle-goldengate-rest-process-status
- name: ReplicatList
  property_count: 1
  slug: oracle-goldengate-rest-replicat-list
- name: Replicat
  property_count: 8
  slug: oracle-goldengate-rest-replicat
- name: ReplicatSummary
  property_count: 3
  slug: oracle-goldengate-rest-replicat-summary
- name: ReportList
  property_count: 1
  slug: oracle-goldengate-rest-report-list
- name: Report
  property_count: 2
  slug: oracle-goldengate-rest-report
- name: RequestList
  property_count: 1
  slug: oracle-goldengate-rest-request-list
- name: RequestStatus
  property_count: 5
  slug: oracle-goldengate-rest-request-status
- name: RoleList
  property_count: 1
  slug: oracle-goldengate-rest-role-list
- name: ServiceHealthDetails
  property_count: 2
  slug: oracle-goldengate-rest-service-health-details
- name: ServiceList
  property_count: 1
  slug: oracle-goldengate-rest-service-list
- name: Service
  property_count: 5
  slug: oracle-goldengate-rest-service
- name: ServiceSummary
  property_count: 4
  slug: oracle-goldengate-rest-service-summary
- name: StatusChangeList
  property_count: 1
  slug: oracle-goldengate-rest-status-change-list
- name: TableList
  property_count: 1
  slug: oracle-goldengate-rest-table-list
- name: TaskList
  property_count: 1
  slug: oracle-goldengate-rest-task-list
- name: Task
  property_count: 5
  slug: oracle-goldengate-rest-task
- name: TaskSummary
  property_count: 3
  slug: oracle-goldengate-rest-task-summary
- name: TrailList
  property_count: 1
  slug: oracle-goldengate-rest-trail-list
- name: TrandataRequest
  property_count: 2
  slug: oracle-goldengate-rest-trandata-request
- name: TrandataResponse
  property_count: 2
  slug: oracle-goldengate-rest-trandata-response
- name: UpdateCollectorPathRequest
  property_count: 3
  slug: oracle-goldengate-rest-update-collector-path-request
- name: UpdateDeploymentRequest
  property_count: 3
  slug: oracle-goldengate-rest-update-deployment-request
- name: UpdateDistributionPathRequest
  property_count: 3
  slug: oracle-goldengate-rest-update-distribution-path-request
- name: UpdateExtractRequest
  property_count: 5
  slug: oracle-goldengate-rest-update-extract-request
- name: UpdateHeartbeatTableRequest
  property_count: 3
  slug: oracle-goldengate-rest-update-heartbeat-table-request
- name: UpdateReplicatRequest
  property_count: 5
  slug: oracle-goldengate-rest-update-replicat-request
- name: UpdateServiceRequest
  property_count: 3
  slug: oracle-goldengate-rest-update-service-request
- name: UpdateTaskRequest
  property_count: 3
  slug: oracle-goldengate-rest-update-task-request
- name: UpdateUserRequest
  property_count: 2
  slug: oracle-goldengate-rest-update-user-request
- name: UserList
  property_count: 1
  slug: oracle-goldengate-rest-user-list
- name: User
  property_count: 3
  slug: oracle-goldengate-rest-user
- name: ValidationResult
  property_count: 2
  slug: oracle-goldengate-rest-validation-result
- name: RestoreDeploymentDetails
  property_count: 1
  slug: oracle-goldengate-restoredeploymentdetails
- name: RoleList
  property_count: 1
  slug: oracle-goldengate-rolelist
- name: RunJobRequest
  property_count: 1
  slug: oracle-goldengate-runjobrequest
- name: ServerConfiguration
  property_count: 4
  slug: oracle-goldengate-serverconfiguration
- name: ServerInfo
  property_count: 4
  slug: oracle-goldengate-serverinfo
- name: ServerLogs
  property_count: 1
  slug: oracle-goldengate-serverlogs
- name: Service
  property_count: 5
  slug: oracle-goldengate-service
- name: ServiceHealth
  property_count: 2
  slug: oracle-goldengate-servicehealth
- name: ServiceHealthDetails
  property_count: 2
  slug: oracle-goldengate-servicehealthdetails
- name: ServiceList
  property_count: 1
  slug: oracle-goldengate-servicelist
- name: ServiceSummary
  property_count: 4
  slug: oracle-goldengate-servicesummary
- name: StartDeploymentDetails
  property_count: 1
  slug: oracle-goldengate-startdeploymentdetails
- name: StatusChangeList
  property_count: 1
  slug: oracle-goldengate-statuschangelist
- name: StopDeploymentDetails
  property_count: 1
  slug: oracle-goldengate-stopdeploymentdetails
- name: ArtifactImport
  property_count: 3
  slug: oracle-goldengate-stream-analytics-rest-artifact-import
- name: CreateUserRequest
  property_count: 2
  slug: oracle-goldengate-stream-analytics-rest-create-user-request
- name: ErrorResponse
  property_count: 2
  slug: oracle-goldengate-stream-analytics-rest-error-response
- name: ImportResult
  property_count: 3
  slug: oracle-goldengate-stream-analytics-rest-import-result
- name: PipelineExport
  property_count: 3
  slug: oracle-goldengate-stream-analytics-rest-pipeline-export
- name: PipelineList
  property_count: 1
  slug: oracle-goldengate-stream-analytics-rest-pipeline-list
- name: Pipeline
  property_count: 10
  slug: oracle-goldengate-stream-analytics-rest-pipeline
- name: PipelineSource
  property_count: 4
  slug: oracle-goldengate-stream-analytics-rest-pipeline-source
- name: PipelineStage
  property_count: 4
  slug: oracle-goldengate-stream-analytics-rest-pipeline-stage
- name: PipelineTarget
  property_count: 4
  slug: oracle-goldengate-stream-analytics-rest-pipeline-target
- name: PublishPipelineRequest
  property_count: 1
  slug: oracle-goldengate-stream-analytics-rest-publish-pipeline-request
- name: UpdateUserRequest
  property_count: 2
  slug: oracle-goldengate-stream-analytics-rest-update-user-request
- name: UserList
  property_count: 1
  slug: oracle-goldengate-stream-analytics-rest-user-list
- name: User
  property_count: 3
  slug: oracle-goldengate-stream-analytics-rest-user
- name: TableList
  property_count: 1
  slug: oracle-goldengate-tablelist
- name: Task
  property_count: 5
  slug: oracle-goldengate-task
- name: TaskList
  property_count: 1
  slug: oracle-goldengate-tasklist
- name: TaskSummary
  property_count: 3
  slug: oracle-goldengate-tasksummary
- name: TrailList
  property_count: 1
  slug: oracle-goldengate-traillist
- name: TrandataRequest
  property_count: 2
  slug: oracle-goldengate-trandatarequest
- name: TrandataResponse
  property_count: 2
  slug: oracle-goldengate-trandataresponse
- name: UpdateCollectorPathRequest
  property_count: 3
  slug: oracle-goldengate-updatecollectorpathrequest
- name: UpdateConnectionDetails
  property_count: 3
  slug: oracle-goldengate-updateconnectiondetails
- name: UpdateConnectionRequest
  property_count: 6
  slug: oracle-goldengate-updateconnectionrequest
- name: UpdateDatabaseRegistrationDetails
  property_count: 6
  slug: oracle-goldengate-updatedatabaseregistrationdetails
- name: UpdateDataStreamRequest
  property_count: 4
  slug: oracle-goldengate-updatedatastreamrequest
- name: UpdateDeploymentDetails
  property_count: 7
  slug: oracle-goldengate-updatedeploymentdetails
- name: UpdateDeploymentRequest
  property_count: 3
  slug: oracle-goldengate-updatedeploymentrequest
- name: UpdateDistributionPathRequest
  property_count: 3
  slug: oracle-goldengate-updatedistributionpathrequest
- name: UpdateExtractRequest
  property_count: 2
  slug: oracle-goldengate-updateextractrequest
- name: UpdateGroupRequest
  property_count: 3
  slug: oracle-goldengate-updategrouprequest
- name: UpdateHeartbeatTableRequest
  property_count: 3
  slug: oracle-goldengate-updateheartbeattablerequest
- name: UpdatePipelineDetails
  property_count: 2
  slug: oracle-goldengate-updatepipelinedetails
- name: UpdateProfileRequest
  property_count: 4
  slug: oracle-goldengate-updateprofilerequest
- name: UpdateReplicatRequest
  property_count: 2
  slug: oracle-goldengate-updatereplicatrequest
- name: UpdateServerConfigurationRequest
  property_count: 3
  slug: oracle-goldengate-updateserverconfigurationrequest
- name: UpdateServiceRequest
  property_count: 3
  slug: oracle-goldengate-updateservicerequest
- name: UpdateTaskRequest
  property_count: 3
  slug: oracle-goldengate-updatetaskrequest
- name: UpdateUserRequest
  property_count: 2
  slug: oracle-goldengate-updateuserrequest
- name: UpgradeDeploymentDetails
  property_count: 2
  slug: oracle-goldengate-upgradedeploymentdetails
- name: User
  property_count: 3
  slug: oracle-goldengate-user
- name: UserGroup
  property_count: 4
  slug: oracle-goldengate-usergroup
- name: UserGroupList
  property_count: 1
  slug: oracle-goldengate-usergrouplist
- name: UserList
  property_count: 1
  slug: oracle-goldengate-userlist
- name: ValidateConnectionRequest
  property_count: 2
  slug: oracle-goldengate-validateconnectionrequest
- name: ValidateDatabaseRequest
  property_count: 6
  slug: oracle-goldengate-validatedatabaserequest
- name: ValidationResult
  property_count: 2
  slug: oracle-goldengate-validationresult
- name: CloneGroupRequest
  property_count: 1
  slug: oracle-goldengate-veridata-rest-clone-group-request
- name: ColumnMappingList
  property_count: 1
  slug: oracle-goldengate-veridata-rest-column-mapping-list
- name: ColumnMapping
  property_count: 3
  slug: oracle-goldengate-veridata-rest-column-mapping
- name: ComparePairList
  property_count: 1
  slug: oracle-goldengate-veridata-rest-compare-pair-list
- name: ComparePair
  property_count: 8
  slug: oracle-goldengate-veridata-rest-compare-pair
- name: ComparePairStatisticsList
  property_count: 1
  slug: oracle-goldengate-veridata-rest-compare-pair-statistics-list
- name: ComparisonReport
  property_count: 6
  slug: oracle-goldengate-veridata-rest-comparison-report
- name: ConnectionList
  property_count: 1
  slug: oracle-goldengate-veridata-rest-connection-list
- name: ConnectionMetadata
  property_count: 1
  slug: oracle-goldengate-veridata-rest-connection-metadata
- name: Connection
  property_count: 10
  slug: oracle-goldengate-veridata-rest-connection
- name: ConnectionStatus
  property_count: 3
  slug: oracle-goldengate-veridata-rest-connection-status
- name: CreateComparePairsRequest
  property_count: 1
  slug: oracle-goldengate-veridata-rest-create-compare-pairs-request
- name: CreateConnectionRequest
  property_count: 11
  slug: oracle-goldengate-veridata-rest-create-connection-request
- name: CreateGroupRequest
  property_count: 5
  slug: oracle-goldengate-veridata-rest-create-group-request
- name: CreateJobRequest
  property_count: 4
  slug: oracle-goldengate-veridata-rest-create-job-request
- name: CreateProfileRequest
  property_count: 5
  slug: oracle-goldengate-veridata-rest-create-profile-request
- name: CreateUserGroupRequest
  property_count: 3
  slug: oracle-goldengate-veridata-rest-create-user-group-request
- name: CreateUserRequest
  property_count: 7
  slug: oracle-goldengate-veridata-rest-create-user-request
- name: ErrorResponse
  property_count: 2
  slug: oracle-goldengate-veridata-rest-error-response
- name: GroupList
  property_count: 1
  slug: oracle-goldengate-veridata-rest-group-list
- name: Group
  property_count: 7
  slug: oracle-goldengate-veridata-rest-group
- name: ImportResult
  property_count: 3
  slug: oracle-goldengate-veridata-rest-import-result
- name: JobExecution
  property_count: 5
  slug: oracle-goldengate-veridata-rest-job-execution
- name: JobList
  property_count: 1
  slug: oracle-goldengate-veridata-rest-job-list
- name: Job
  property_count: 6
  slug: oracle-goldengate-veridata-rest-job
- name: JobStatisticsList
  property_count: 1
  slug: oracle-goldengate-veridata-rest-job-statistics-list
- name: LoginResponse
  property_count: 3
  slug: oracle-goldengate-veridata-rest-login-response
- name: MappingObjectList
  property_count: 1
  slug: oracle-goldengate-veridata-rest-mapping-object-list
- name: MappingRulesRequest
  property_count: 3
  slug: oracle-goldengate-veridata-rest-mapping-rules-request
- name: MetadataRequest
  property_count: 2
  slug: oracle-goldengate-veridata-rest-metadata-request
- name: OutOfSyncData
  property_count: 2
  slug: oracle-goldengate-veridata-rest-out-of-sync-data
- name: ProfileList
  property_count: 1
  slug: oracle-goldengate-veridata-rest-profile-list
- name: Profile
  property_count: 7
  slug: oracle-goldengate-veridata-rest-profile
- name: RepairExecution
  property_count: 3
  slug: oracle-goldengate-veridata-rest-repair-execution
- name: RepairJobRequest
  property_count: 1
  slug: oracle-goldengate-veridata-rest-repair-job-request
- name: RepairReport
  property_count: 6
  slug: oracle-goldengate-veridata-rest-repair-report
- name: RepairStatisticsList
  property_count: 1
  slug: oracle-goldengate-veridata-rest-repair-statistics-list
- name: RepairedRowDetails
  property_count: 2
  slug: oracle-goldengate-veridata-rest-repaired-row-details
- name: ReplaceComparePairRequest
  property_count: 5
  slug: oracle-goldengate-veridata-rest-replace-compare-pair-request
- name: ReplaceJobRequest
  property_count: 4
  slug: oracle-goldengate-veridata-rest-replace-job-request
- name: ReplaceUserGroupRequest
  property_count: 3
  slug: oracle-goldengate-veridata-rest-replace-user-group-request
- name: ReplaceUserRequest
  property_count: 5
  slug: oracle-goldengate-veridata-rest-replace-user-request
- name: RunJobRequest
  property_count: 1
  slug: oracle-goldengate-veridata-rest-run-job-request
- name: ServerConfiguration
  property_count: 4
  slug: oracle-goldengate-veridata-rest-server-configuration
- name: ServerInfo
  property_count: 4
  slug: oracle-goldengate-veridata-rest-server-info
- name: ServerLogs
  property_count: 1
  slug: oracle-goldengate-veridata-rest-server-logs
- name: UpdateConnectionRequest
  property_count: 6
  slug: oracle-goldengate-veridata-rest-update-connection-request
- name: UpdateGroupRequest
  property_count: 3
  slug: oracle-goldengate-veridata-rest-update-group-request
- name: UpdateProfileRequest
  property_count: 4
  slug: oracle-goldengate-veridata-rest-update-profile-request
- name: UpdateServerConfigurationRequest
  property_count: 3
  slug: oracle-goldengate-veridata-rest-update-server-configuration-request
- name: UserGroupList
  property_count: 1
  slug: oracle-goldengate-veridata-rest-user-group-list
- name: UserGroup
  property_count: 4
  slug: oracle-goldengate-veridata-rest-user-group
- name: UserList
  property_count: 1
  slug: oracle-goldengate-veridata-rest-user-list
- name: User
  property_count: 7
  slug: oracle-goldengate-veridata-rest-user
- name: ValidateConnectionRequest
  property_count: 2
  slug: oracle-goldengate-veridata-rest-validate-connection-request
- name: ValidateDatabaseRequest
  property_count: 6
  slug: oracle-goldengate-veridata-rest-validate-database-request
- name: ValidationResult
  property_count: 2
  slug: oracle-goldengate-veridata-rest-validation-result
- name: WorkRequest
  property_count: 8
  slug: oracle-goldengate-workrequest
- name: WorkRequestCollection
  property_count: 1
  slug: oracle-goldengate-workrequestcollection
- name: WorkRequestErrorCollection
  property_count: 1
  slug: oracle-goldengate-workrequesterrorcollection
- name: WorkRequestLogEntryCollection
  property_count: 1
  slug: oracle-goldengate-workrequestlogentrycollection
- name: WorkRequestSummary
  property_count: 5
  slug: oracle-goldengate-workrequestsummary
json_structures:
- name: Oracle Goldengate Big Data Rest Command Response Structure
  property_count: 1
  slug: oracle-goldengate-big-data-rest-command-response-structure
- name: Oracle Goldengate Big Data Rest Config File Content Structure
  property_count: 1
  slug: oracle-goldengate-big-data-rest-config-file-content-structure
- name: Oracle Goldengate Big Data Rest Config File List Structure
  property_count: 1
  slug: oracle-goldengate-big-data-rest-config-file-list-structure
- name: Oracle Goldengate Big Data Rest Config File Structure
  property_count: 2
  slug: oracle-goldengate-big-data-rest-config-file-structure
- name: Oracle Goldengate Big Data Rest Create Credential Request Structure
  property_count: 2
  slug: oracle-goldengate-big-data-rest-create-credential-request-structure
- name: Oracle Goldengate Big Data Rest Create Distribution Path Request Structure
  property_count: 2
  slug: oracle-goldengate-big-data-rest-create-distribution-path-request-structure
- name: Oracle Goldengate Big Data Rest Create Extract Request Structure
  property_count: 4
  slug: oracle-goldengate-big-data-rest-create-extract-request-structure
- name: Oracle Goldengate Big Data Rest Create Replicat Request Structure
  property_count: 5
  slug: oracle-goldengate-big-data-rest-create-replicat-request-structure
- name: Oracle Goldengate Big Data Rest Credential Alias Structure
  property_count: 3
  slug: oracle-goldengate-big-data-rest-credential-alias-structure
- name: Oracle Goldengate Big Data Rest Credential Domain List Structure
  property_count: 1
  slug: oracle-goldengate-big-data-rest-credential-domain-list-structure
- name: Oracle Goldengate Big Data Rest Data Target Type List Structure
  property_count: 1
  slug: oracle-goldengate-big-data-rest-data-target-type-list-structure
- name: Oracle Goldengate Big Data Rest Data Target Type Schema Structure
  property_count: 2
  slug: oracle-goldengate-big-data-rest-data-target-type-schema-structure
- name: Oracle Goldengate Big Data Rest Distribution Path List Structure
  property_count: 1
  slug: oracle-goldengate-big-data-rest-distribution-path-list-structure
- name: Oracle Goldengate Big Data Rest Distribution Path Structure
  property_count: 4
  slug: oracle-goldengate-big-data-rest-distribution-path-structure
- name: Oracle Goldengate Big Data Rest Distribution Path Summary Structure
  property_count: 4
  slug: oracle-goldengate-big-data-rest-distribution-path-summary-structure
- name: Oracle Goldengate Big Data Rest Error Response Structure
  property_count: 3
  slug: oracle-goldengate-big-data-rest-error-response-structure
- name: Oracle Goldengate Big Data Rest Execute Command Request Structure
  property_count: 1
  slug: oracle-goldengate-big-data-rest-execute-command-request-structure
- name: Oracle Goldengate Big Data Rest Extract List Structure
  property_count: 1
  slug: oracle-goldengate-big-data-rest-extract-list-structure
- name: Oracle Goldengate Big Data Rest Extract Structure
  property_count: 5
  slug: oracle-goldengate-big-data-rest-extract-structure
- name: Oracle Goldengate Big Data Rest Extract Summary Structure
  property_count: 3
  slug: oracle-goldengate-big-data-rest-extract-summary-structure
- name: Oracle Goldengate Big Data Rest Process Command Structure
  property_count: 1
  slug: oracle-goldengate-big-data-rest-process-command-structure
- name: Oracle Goldengate Big Data Rest Process Metrics List Structure
  property_count: 1
  slug: oracle-goldengate-big-data-rest-process-metrics-list-structure
- name: Oracle Goldengate Big Data Rest Process Status Structure
  property_count: 4
  slug: oracle-goldengate-big-data-rest-process-status-structure
- name: Oracle Goldengate Big Data Rest Replicat List Structure
  property_count: 1
  slug: oracle-goldengate-big-data-rest-replicat-list-structure
- name: Oracle Goldengate Big Data Rest Replicat Statistics Structure
  property_count: 6
  slug: oracle-goldengate-big-data-rest-replicat-statistics-structure
- name: Oracle Goldengate Big Data Rest Replicat Structure
  property_count: 7
  slug: oracle-goldengate-big-data-rest-replicat-structure
- name: Oracle Goldengate Big Data Rest Replicat Summary Structure
  property_count: 4
  slug: oracle-goldengate-big-data-rest-replicat-summary-structure
- name: Oracle Goldengate Big Data Rest Service Health Structure
  property_count: 2
  slug: oracle-goldengate-big-data-rest-service-health-structure
- name: Oracle Goldengate Big Data Rest Trail List Structure
  property_count: 1
  slug: oracle-goldengate-big-data-rest-trail-list-structure
- name: Oracle Goldengate Big Data Rest Update Extract Request Structure
  property_count: 2
  slug: oracle-goldengate-big-data-rest-update-extract-request-structure
- name: Oracle Goldengate Big Data Rest Update Replicat Request Structure
  property_count: 2
  slug: oracle-goldengate-big-data-rest-update-replicat-request-structure
- name: Oracle Goldengate Cloud Service Certificate Collection Structure
  property_count: 1
  slug: oracle-goldengate-cloud-service-certificate-collection-structure
- name: Oracle Goldengate Cloud Service Certificate Structure
  property_count: 13
  slug: oracle-goldengate-cloud-service-certificate-structure
- name: Oracle Goldengate Cloud Service Certificate Summary Structure
  property_count: 4
  slug: oracle-goldengate-cloud-service-certificate-summary-structure
- name: Oracle Goldengate Cloud Service Change Compartment Details Structure
  property_count: 1
  slug: oracle-goldengate-cloud-service-change-compartment-details-structure
- name: Oracle Goldengate Cloud Service Collect Diagnostics Details Structure
  property_count: 3
  slug: oracle-goldengate-cloud-service-collect-diagnostics-details-structure
- name: Oracle Goldengate Cloud Service Connection Assignment Collection Structure
  property_count: 1
  slug: oracle-goldengate-cloud-service-connection-assignment-collection-structure
- name: Oracle Goldengate Cloud Service Connection Assignment Structure
  property_count: 7
  slug: oracle-goldengate-cloud-service-connection-assignment-structure
- name: Oracle Goldengate Cloud Service Connection Assignment Summary Structure
  property_count: 4
  slug: oracle-goldengate-cloud-service-connection-assignment-summary-structure
- name: Oracle Goldengate Cloud Service Connection Collection Structure
  property_count: 1
  slug: oracle-goldengate-cloud-service-connection-collection-structure
- name: Oracle Goldengate Cloud Service Connection Structure
  property_count: 10
  slug: oracle-goldengate-cloud-service-connection-structure
- name: Oracle Goldengate Cloud Service Connection Summary Structure
  property_count: 5
  slug: oracle-goldengate-cloud-service-connection-summary-structure
- name: Oracle Goldengate Cloud Service Create Certificate Details Structure
  property_count: 2
  slug: oracle-goldengate-cloud-service-create-certificate-details-structure
- name: Oracle Goldengate Cloud Service Create Connection Assignment Details Structure
  property_count: 2
  slug: oracle-goldengate-cloud-service-create-connection-assignment-details-structure
- name: Oracle Goldengate Cloud Service Create Connection Details Structure
  property_count: 6
  slug: oracle-goldengate-cloud-service-create-connection-details-structure
- name: Oracle Goldengate Cloud Service Create Database Registration Details Structure
  property_count: 8
  slug: oracle-goldengate-cloud-service-create-database-registration-details-structure
- name: Oracle Goldengate Cloud Service Create Deployment Backup Details Structure
  property_count: 6
  slug: oracle-goldengate-cloud-service-create-deployment-backup-details-structure
- name: Oracle Goldengate Cloud Service Create Deployment Details Structure
  property_count: 12
  slug: oracle-goldengate-cloud-service-create-deployment-details-structure
- name: Oracle Goldengate Cloud Service Create Pipeline Details Structure
  property_count: 5
  slug: oracle-goldengate-cloud-service-create-pipeline-details-structure
- name: Oracle Goldengate Cloud Service Database Registration Collection Structure
  property_count: 1
  slug: oracle-goldengate-cloud-service-database-registration-collection-structure
- name: Oracle Goldengate Cloud Service Database Registration Structure
  property_count: 10
  slug: oracle-goldengate-cloud-service-database-registration-structure
- name: Oracle Goldengate Cloud Service Database Registration Summary Structure
  property_count: 4
  slug: oracle-goldengate-cloud-service-database-registration-summary-structure
- name: Oracle Goldengate Cloud Service Deployment Backup Collection Structure
  property_count: 1
  slug: oracle-goldengate-cloud-service-deployment-backup-collection-structure
- name: Oracle Goldengate Cloud Service Deployment Backup Structure
  property_count: 9
  slug: oracle-goldengate-cloud-service-deployment-backup-structure
- name: Oracle Goldengate Cloud Service Deployment Backup Summary Structure
  property_count: 5
  slug: oracle-goldengate-cloud-service-deployment-backup-summary-structure
- name: Oracle Goldengate Cloud Service Deployment Collection Structure
  property_count: 1
  slug: oracle-goldengate-cloud-service-deployment-collection-structure
- name: Oracle Goldengate Cloud Service Deployment Structure
  property_count: 19
  slug: oracle-goldengate-cloud-service-deployment-structure
- name: Oracle Goldengate Cloud Service Deployment Summary Structure
  property_count: 6
  slug: oracle-goldengate-cloud-service-deployment-summary-structure
- name: Oracle Goldengate Cloud Service Deployment Version Collection Structure
  property_count: 1
  slug: oracle-goldengate-cloud-service-deployment-version-collection-structure
- name: Oracle Goldengate Cloud Service Error Structure
  property_count: 2
  slug: oracle-goldengate-cloud-service-error-structure
- name: Oracle Goldengate Cloud Service Pipeline Collection Structure
  property_count: 1
  slug: oracle-goldengate-cloud-service-pipeline-collection-structure
- name: Oracle Goldengate Cloud Service Pipeline Structure
  property_count: 9
  slug: oracle-goldengate-cloud-service-pipeline-structure
- name: Oracle Goldengate Cloud Service Pipeline Summary Structure
  property_count: 4
  slug: oracle-goldengate-cloud-service-pipeline-summary-structure
- name: Oracle Goldengate Cloud Service Restore Deployment Details Structure
  property_count: 1
  slug: oracle-goldengate-cloud-service-restore-deployment-details-structure
- name: Oracle Goldengate Cloud Service Start Deployment Details Structure
  property_count: 1
  slug: oracle-goldengate-cloud-service-start-deployment-details-structure
- name: Oracle Goldengate Cloud Service Stop Deployment Details Structure
  property_count: 1
  slug: oracle-goldengate-cloud-service-stop-deployment-details-structure
- name: Oracle Goldengate Cloud Service Update Connection Details Structure
  property_count: 3
  slug: oracle-goldengate-cloud-service-update-connection-details-structure
- name: Oracle Goldengate Cloud Service Update Database Registration Details Structure
  property_count: 6
  slug: oracle-goldengate-cloud-service-update-database-registration-details-structure
- name: Oracle Goldengate Cloud Service Update Deployment Details Structure
  property_count: 7
  slug: oracle-goldengate-cloud-service-update-deployment-details-structure
- name: Oracle Goldengate Cloud Service Update Pipeline Details Structure
  property_count: 2
  slug: oracle-goldengate-cloud-service-update-pipeline-details-structure
- name: Oracle Goldengate Cloud Service Upgrade Deployment Details Structure
  property_count: 2
  slug: oracle-goldengate-cloud-service-upgrade-deployment-details-structure
- name: Oracle Goldengate Cloud Service Work Request Collection Structure
  property_count: 1
  slug: oracle-goldengate-cloud-service-work-request-collection-structure
- name: Oracle Goldengate Cloud Service Work Request Error Collection Structure
  property_count: 1
  slug: oracle-goldengate-cloud-service-work-request-error-collection-structure
- name: Oracle Goldengate Cloud Service Work Request Log Entry Collection Structure
  property_count: 1
  slug: oracle-goldengate-cloud-service-work-request-log-entry-collection-structure
- name: Oracle Goldengate Cloud Service Work Request Structure
  property_count: 8
  slug: oracle-goldengate-cloud-service-work-request-structure
- name: Oracle Goldengate Cloud Service Work Request Summary Structure
  property_count: 5
  slug: oracle-goldengate-cloud-service-work-request-summary-structure
- name: Oracle Goldengate Data Streams Rest Create Data Stream Request Structure
  property_count: 4
  slug: oracle-goldengate-data-streams-rest-create-data-stream-request-structure
- name: Oracle Goldengate Data Streams Rest Data Stream List Structure
  property_count: 1
  slug: oracle-goldengate-data-streams-rest-data-stream-list-structure
- name: Oracle Goldengate Data Streams Rest Data Stream Structure
  property_count: 9
  slug: oracle-goldengate-data-streams-rest-data-stream-structure
- name: Oracle Goldengate Data Streams Rest Data Stream Summary Structure
  property_count: 3
  slug: oracle-goldengate-data-streams-rest-data-stream-summary-structure
- name: Oracle Goldengate Data Streams Rest Error Response Structure
  property_count: 2
  slug: oracle-goldengate-data-streams-rest-error-response-structure
- name: Oracle Goldengate Data Streams Rest Update Data Stream Request Structure
  property_count: 4
  slug: oracle-goldengate-data-streams-rest-update-data-stream-request-structure
- name: Oracle Goldengate Rest Api Version Details Structure
  property_count: 4
  slug: oracle-goldengate-rest-api-version-details-structure
- name: Oracle Goldengate Rest Api Version List Structure
  property_count: 1
  slug: oracle-goldengate-rest-api-version-list-structure
- name: Oracle Goldengate Rest Bulk Create Users Request Structure
  property_count: 1
  slug: oracle-goldengate-rest-bulk-create-users-request-structure
- name: Oracle Goldengate Rest Cache Statistics Structure
  property_count: 4
  slug: oracle-goldengate-rest-cache-statistics-structure
- name: Oracle Goldengate Rest Certificate Name List Structure
  property_count: 1
  slug: oracle-goldengate-rest-certificate-name-list-structure
- name: Oracle Goldengate Rest Certificate Structure
  property_count: 6
  slug: oracle-goldengate-rest-certificate-structure
- name: Oracle Goldengate Rest Certificate Type List Structure
  property_count: 1
  slug: oracle-goldengate-rest-certificate-type-list-structure
- name: Oracle Goldengate Rest Checkpoints Structure
  property_count: 3
  slug: oracle-goldengate-rest-checkpoints-structure
- name: Oracle Goldengate Rest Collector Path List Structure
  property_count: 1
  slug: oracle-goldengate-rest-collector-path-list-structure
- name: Oracle Goldengate Rest Collector Path Structure
  property_count: 4
  slug: oracle-goldengate-rest-collector-path-structure
- name: Oracle Goldengate Rest Collector Path Summary Structure
  property_count: 2
  slug: oracle-goldengate-rest-collector-path-summary-structure
- name: Oracle Goldengate Rest Command Response Structure
  property_count: 1
  slug: oracle-goldengate-rest-command-response-structure
- name: Oracle Goldengate Rest Config File Content Structure
  property_count: 1
  slug: oracle-goldengate-rest-config-file-content-structure
- name: Oracle Goldengate Rest Config File List Structure
  property_count: 1
  slug: oracle-goldengate-rest-config-file-list-structure
- name: Oracle Goldengate Rest Config File Structure
  property_count: 3
  slug: oracle-goldengate-rest-config-file-structure
- name: Oracle Goldengate Rest Config Summary Structure
  property_count: 5
  slug: oracle-goldengate-rest-config-summary-structure
- name: Oracle Goldengate Rest Config Type List Structure
  property_count: 1
  slug: oracle-goldengate-rest-config-type-list-structure
- name: Oracle Goldengate Rest Connection List Structure
  property_count: 1
  slug: oracle-goldengate-rest-connection-list-structure
- name: Oracle Goldengate Rest Create Collector Path Request Structure
  property_count: 2
  slug: oracle-goldengate-rest-create-collector-path-request-structure
- name: Oracle Goldengate Rest Create Connection Request Structure
  property_count: 3
  slug: oracle-goldengate-rest-create-connection-request-structure
- name: Oracle Goldengate Rest Create Credential Alias Request Structure
  property_count: 2
  slug: oracle-goldengate-rest-create-credential-alias-request-structure
- name: Oracle Goldengate Rest Create Deployment Request Structure
  property_count: 4
  slug: oracle-goldengate-rest-create-deployment-request-structure
- name: Oracle Goldengate Rest Create Distribution Path Request Structure
  property_count: 4
  slug: oracle-goldengate-rest-create-distribution-path-request-structure
- name: Oracle Goldengate Rest Create Extract Request Structure
  property_count: 8
  slug: oracle-goldengate-rest-create-extract-request-structure
- name: Oracle Goldengate Rest Create Heartbeat Table Request Structure
  property_count: 4
  slug: oracle-goldengate-rest-create-heartbeat-table-request-structure
- name: Oracle Goldengate Rest Create Replicat Request Structure
  property_count: 7
  slug: oracle-goldengate-rest-create-replicat-request-structure
- name: Oracle Goldengate Rest Create Service Request Structure
  property_count: 3
  slug: oracle-goldengate-rest-create-service-request-structure
- name: Oracle Goldengate Rest Create Task Request Structure
  property_count: 3
  slug: oracle-goldengate-rest-create-task-request-structure
- name: Oracle Goldengate Rest Create User Request Structure
  property_count: 2
  slug: oracle-goldengate-rest-create-user-request-structure
- name: Oracle Goldengate Rest Credential Alias List Structure
  property_count: 1
  slug: oracle-goldengate-rest-credential-alias-list-structure
- name: Oracle Goldengate Rest Credential Alias Structure
  property_count: 3
  slug: oracle-goldengate-rest-credential-alias-structure
- name: Oracle Goldengate Rest Credential Domain List Structure
  property_count: 1
  slug: oracle-goldengate-rest-credential-domain-list-structure
- name: Oracle Goldengate Rest Database Connection Structure
  property_count: 4
  slug: oracle-goldengate-rest-database-connection-structure
- name: Oracle Goldengate Rest Database Name List Structure
  property_count: 1
  slug: oracle-goldengate-rest-database-name-list-structure
- name: Oracle Goldengate Rest Database Statistics Structure
  property_count: 6
  slug: oracle-goldengate-rest-database-statistics-structure
- name: Oracle Goldengate Rest Deployment List Structure
  property_count: 1
  slug: oracle-goldengate-rest-deployment-list-structure
- name: Oracle Goldengate Rest Deployment Structure
  property_count: 7
  slug: oracle-goldengate-rest-deployment-structure
- name: Oracle Goldengate Rest Deployment Summary Structure
  property_count: 3
  slug: oracle-goldengate-rest-deployment-summary-structure
- name: Oracle Goldengate Rest Distribution Path List Structure
  property_count: 1
  slug: oracle-goldengate-rest-distribution-path-list-structure
- name: Oracle Goldengate Rest Distribution Path Structure
  property_count: 6
  slug: oracle-goldengate-rest-distribution-path-structure
- name: Oracle Goldengate Rest Distribution Path Summary Structure
  property_count: 4
  slug: oracle-goldengate-rest-distribution-path-summary-structure
- name: Oracle Goldengate Rest Encryption Key List Structure
  property_count: 1
  slug: oracle-goldengate-rest-encryption-key-list-structure
- name: Oracle Goldengate Rest Encryption Key Structure
  property_count: 3
  slug: oracle-goldengate-rest-encryption-key-structure
- name: Oracle Goldengate Rest Error Response Structure
  property_count: 3
  slug: oracle-goldengate-rest-error-response-structure
- name: Oracle Goldengate Rest Event List Structure
  property_count: 1
  slug: oracle-goldengate-rest-event-list-structure
- name: Oracle Goldengate Rest Execute Command Request Structure
  property_count: 1
  slug: oracle-goldengate-rest-execute-command-request-structure
- name: Oracle Goldengate Rest Extract List Structure
  property_count: 1
  slug: oracle-goldengate-rest-extract-list-structure
- name: Oracle Goldengate Rest Extract Structure
  property_count: 10
  slug: oracle-goldengate-rest-extract-structure
- name: Oracle Goldengate Rest Extract Summary Structure
  property_count: 4
  slug: oracle-goldengate-rest-extract-summary-structure
- name: Oracle Goldengate Rest Extract Trail List Structure
  property_count: 1
  slug: oracle-goldengate-rest-extract-trail-list-structure
- name: Oracle Goldengate Rest Health Check Summary Structure
  property_count: 3
  slug: oracle-goldengate-rest-health-check-summary-structure
- name: Oracle Goldengate Rest Heartbeat Entries Structure
  property_count: 1
  slug: oracle-goldengate-rest-heartbeat-entries-structure
- name: Oracle Goldengate Rest Heartbeat Metrics Structure
  property_count: 3
  slug: oracle-goldengate-rest-heartbeat-metrics-structure
- name: Oracle Goldengate Rest Heartbeat Table Structure
  property_count: 5
  slug: oracle-goldengate-rest-heartbeat-table-structure
- name: Oracle Goldengate Rest Link Structure
  property_count: 3
  slug: oracle-goldengate-rest-link-structure
- name: Oracle Goldengate Rest Log Content Structure
  property_count: 3
  slug: oracle-goldengate-rest-log-content-structure
- name: Oracle Goldengate Rest Log List Structure
  property_count: 1
  slug: oracle-goldengate-rest-log-list-structure
- name: Oracle Goldengate Rest Master Key Version List Structure
  property_count: 1
  slug: oracle-goldengate-rest-master-key-version-list-structure
- name: Oracle Goldengate Rest Master Key Version Structure
  property_count: 3
  slug: oracle-goldengate-rest-master-key-version-structure
- name: Oracle Goldengate Rest Message Code List Structure
  property_count: 1
  slug: oracle-goldengate-rest-message-code-list-structure
- name: Oracle Goldengate Rest Message Explanation Structure
  property_count: 4
  slug: oracle-goldengate-rest-message-explanation-structure
- name: Oracle Goldengate Rest Message List Structure
  property_count: 1
  slug: oracle-goldengate-rest-message-list-structure
- name: Oracle Goldengate Rest Modify Log Request Structure
  property_count: 1
  slug: oracle-goldengate-rest-modify-log-request-structure
- name: Oracle Goldengate Rest Monitoring Message List Structure
  property_count: 1
  slug: oracle-goldengate-rest-monitoring-message-list-structure
- name: Oracle Goldengate Rest Parameter Info Structure
  property_count: 5
  slug: oracle-goldengate-rest-parameter-info-structure
- name: Oracle Goldengate Rest Parameter Name List Structure
  property_count: 1
  slug: oracle-goldengate-rest-parameter-name-list-structure
- name: Oracle Goldengate Rest Path Statistics Structure
  property_count: 4
  slug: oracle-goldengate-rest-path-statistics-structure
- name: Oracle Goldengate Rest Process Command Structure
  property_count: 2
  slug: oracle-goldengate-rest-process-command-structure
- name: Oracle Goldengate Rest Process History Structure
  property_count: 2
  slug: oracle-goldengate-rest-process-history-structure
- name: Oracle Goldengate Rest Process Metrics List Structure
  property_count: 1
  slug: oracle-goldengate-rest-process-metrics-list-structure
- name: Oracle Goldengate Rest Process Metrics Structure
  property_count: 8
  slug: oracle-goldengate-rest-process-metrics-structure
- name: Oracle Goldengate Rest Process Performance Structure
  property_count: 4
  slug: oracle-goldengate-rest-process-performance-structure
- name: Oracle Goldengate Rest Process Status Structure
  property_count: 5
  slug: oracle-goldengate-rest-process-status-structure
- name: Oracle Goldengate Rest Replicat List Structure
  property_count: 1
  slug: oracle-goldengate-rest-replicat-list-structure
- name: Oracle Goldengate Rest Replicat Structure
  property_count: 8
  slug: oracle-goldengate-rest-replicat-structure
- name: Oracle Goldengate Rest Replicat Summary Structure
  property_count: 3
  slug: oracle-goldengate-rest-replicat-summary-structure
- name: Oracle Goldengate Rest Report List Structure
  property_count: 1
  slug: oracle-goldengate-rest-report-list-structure
- name: Oracle Goldengate Rest Report Structure
  property_count: 2
  slug: oracle-goldengate-rest-report-structure
- name: Oracle Goldengate Rest Request List Structure
  property_count: 1
  slug: oracle-goldengate-rest-request-list-structure
- name: Oracle Goldengate Rest Request Status Structure
  property_count: 5
  slug: oracle-goldengate-rest-request-status-structure
- name: Oracle Goldengate Rest Role List Structure
  property_count: 1
  slug: oracle-goldengate-rest-role-list-structure
- name: Oracle Goldengate Rest Service Health Details Structure
  property_count: 2
  slug: oracle-goldengate-rest-service-health-details-structure
- name: Oracle Goldengate Rest Service List Structure
  property_count: 1
  slug: oracle-goldengate-rest-service-list-structure
- name: Oracle Goldengate Rest Service Structure
  property_count: 5
  slug: oracle-goldengate-rest-service-structure
- name: Oracle Goldengate Rest Service Summary Structure
  property_count: 4
  slug: oracle-goldengate-rest-service-summary-structure
- name: Oracle Goldengate Rest Status Change List Structure
  property_count: 1
  slug: oracle-goldengate-rest-status-change-list-structure
- name: Oracle Goldengate Rest Table List Structure
  property_count: 1
  slug: oracle-goldengate-rest-table-list-structure
- name: Oracle Goldengate Rest Task List Structure
  property_count: 1
  slug: oracle-goldengate-rest-task-list-structure
- name: Oracle Goldengate Rest Task Structure
  property_count: 5
  slug: oracle-goldengate-rest-task-structure
- name: Oracle Goldengate Rest Task Summary Structure
  property_count: 3
  slug: oracle-goldengate-rest-task-summary-structure
- name: Oracle Goldengate Rest Trail List Structure
  property_count: 1
  slug: oracle-goldengate-rest-trail-list-structure
- name: Oracle Goldengate Rest Trandata Request Structure
  property_count: 2
  slug: oracle-goldengate-rest-trandata-request-structure
- name: Oracle Goldengate Rest Trandata Response Structure
  property_count: 2
  slug: oracle-goldengate-rest-trandata-response-structure
- name: Oracle Goldengate Rest Update Collector Path Request Structure
  property_count: 3
  slug: oracle-goldengate-rest-update-collector-path-request-structure
- name: Oracle Goldengate Rest Update Deployment Request Structure
  property_count: 3
  slug: oracle-goldengate-rest-update-deployment-request-structure
- name: Oracle Goldengate Rest Update Distribution Path Request Structure
  property_count: 3
  slug: oracle-goldengate-rest-update-distribution-path-request-structure
- name: Oracle Goldengate Rest Update Extract Request Structure
  property_count: 5
  slug: oracle-goldengate-rest-update-extract-request-structure
- name: Oracle Goldengate Rest Update Heartbeat Table Request Structure
  property_count: 3
  slug: oracle-goldengate-rest-update-heartbeat-table-request-structure
- name: Oracle Goldengate Rest Update Replicat Request Structure
  property_count: 5
  slug: oracle-goldengate-rest-update-replicat-request-structure
- name: Oracle Goldengate Rest Update Service Request Structure
  property_count: 3
  slug: oracle-goldengate-rest-update-service-request-structure
- name: Oracle Goldengate Rest Update Task Request Structure
  property_count: 3
  slug: oracle-goldengate-rest-update-task-request-structure
- name: Oracle Goldengate Rest Update User Request Structure
  property_count: 2
  slug: oracle-goldengate-rest-update-user-request-structure
- name: Oracle Goldengate Rest User List Structure
  property_count: 1
  slug: oracle-goldengate-rest-user-list-structure
- name: Oracle Goldengate Rest User Structure
  property_count: 3
  slug: oracle-goldengate-rest-user-structure
- name: Oracle Goldengate Rest Validation Result Structure
  property_count: 2
  slug: oracle-goldengate-rest-validation-result-structure
- name: Oracle Goldengate Stream Analytics Rest Artifact Import Structure
  property_count: 3
  slug: oracle-goldengate-stream-analytics-rest-artifact-import-structure
- name: Oracle Goldengate Stream Analytics Rest Create User Request Structure
  property_count: 2
  slug: oracle-goldengate-stream-analytics-rest-create-user-request-structure
- name: Oracle Goldengate Stream Analytics Rest Error Response Structure
  property_count: 2
  slug: oracle-goldengate-stream-analytics-rest-error-response-structure
- name: Oracle Goldengate Stream Analytics Rest Import Result Structure
  property_count: 3
  slug: oracle-goldengate-stream-analytics-rest-import-result-structure
- name: Oracle Goldengate Stream Analytics Rest Pipeline Export Structure
  property_count: 3
  slug: oracle-goldengate-stream-analytics-rest-pipeline-export-structure
- name: Oracle Goldengate Stream Analytics Rest Pipeline List Structure
  property_count: 1
  slug: oracle-goldengate-stream-analytics-rest-pipeline-list-structure
- name: Oracle Goldengate Stream Analytics Rest Pipeline Source Structure
  property_count: 4
  slug: oracle-goldengate-stream-analytics-rest-pipeline-source-structure
- name: Oracle Goldengate Stream Analytics Rest Pipeline Stage Structure
  property_count: 4
  slug: oracle-goldengate-stream-analytics-rest-pipeline-stage-structure
- name: Oracle Goldengate Stream Analytics Rest Pipeline Structure
  property_count: 10
  slug: oracle-goldengate-stream-analytics-rest-pipeline-structure
- name: Oracle Goldengate Stream Analytics Rest Pipeline Target Structure
  property_count: 4
  slug: oracle-goldengate-stream-analytics-rest-pipeline-target-structure
- name: Oracle Goldengate Stream Analytics Rest Publish Pipeline Request Structure
  property_count: 1
  slug: oracle-goldengate-stream-analytics-rest-publish-pipeline-request-structure
- name: Oracle Goldengate Stream Analytics Rest Update User Request Structure
  property_count: 2
  slug: oracle-goldengate-stream-analytics-rest-update-user-request-structure
- name: Oracle Goldengate Stream Analytics Rest User List Structure
  property_count: 1
  slug: oracle-goldengate-stream-analytics-rest-user-list-structure
- name: Oracle Goldengate Stream Analytics Rest User Structure
  property_count: 3
  slug: oracle-goldengate-stream-analytics-rest-user-structure
- name: Oracle Goldengate Structure
  property_count: 0
  slug: oracle-goldengate-structure
- name: Oracle Goldengate Veridata Rest Clone Group Request Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-clone-group-request-structure
- name: Oracle Goldengate Veridata Rest Column Mapping List Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-column-mapping-list-structure
- name: Oracle Goldengate Veridata Rest Column Mapping Structure
  property_count: 3
  slug: oracle-goldengate-veridata-rest-column-mapping-structure
- name: Oracle Goldengate Veridata Rest Compare Pair List Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-compare-pair-list-structure
- name: Oracle Goldengate Veridata Rest Compare Pair Statistics List Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-compare-pair-statistics-list-structure
- name: Oracle Goldengate Veridata Rest Compare Pair Structure
  property_count: 8
  slug: oracle-goldengate-veridata-rest-compare-pair-structure
- name: Oracle Goldengate Veridata Rest Comparison Report Structure
  property_count: 6
  slug: oracle-goldengate-veridata-rest-comparison-report-structure
- name: Oracle Goldengate Veridata Rest Connection List Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-connection-list-structure
- name: Oracle Goldengate Veridata Rest Connection Metadata Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-connection-metadata-structure
- name: Oracle Goldengate Veridata Rest Connection Status Structure
  property_count: 3
  slug: oracle-goldengate-veridata-rest-connection-status-structure
- name: Oracle Goldengate Veridata Rest Connection Structure
  property_count: 10
  slug: oracle-goldengate-veridata-rest-connection-structure
- name: Oracle Goldengate Veridata Rest Create Compare Pairs Request Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-create-compare-pairs-request-structure
- name: Oracle Goldengate Veridata Rest Create Connection Request Structure
  property_count: 11
  slug: oracle-goldengate-veridata-rest-create-connection-request-structure
- name: Oracle Goldengate Veridata Rest Create Group Request Structure
  property_count: 5
  slug: oracle-goldengate-veridata-rest-create-group-request-structure
- name: Oracle Goldengate Veridata Rest Create Job Request Structure
  property_count: 4
  slug: oracle-goldengate-veridata-rest-create-job-request-structure
- name: Oracle Goldengate Veridata Rest Create Profile Request Structure
  property_count: 5
  slug: oracle-goldengate-veridata-rest-create-profile-request-structure
- name: Oracle Goldengate Veridata Rest Create User Group Request Structure
  property_count: 3
  slug: oracle-goldengate-veridata-rest-create-user-group-request-structure
- name: Oracle Goldengate Veridata Rest Create User Request Structure
  property_count: 7
  slug: oracle-goldengate-veridata-rest-create-user-request-structure
- name: Oracle Goldengate Veridata Rest Error Response Structure
  property_count: 2
  slug: oracle-goldengate-veridata-rest-error-response-structure
- name: Oracle Goldengate Veridata Rest Group List Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-group-list-structure
- name: Oracle Goldengate Veridata Rest Group Structure
  property_count: 7
  slug: oracle-goldengate-veridata-rest-group-structure
- name: Oracle Goldengate Veridata Rest Import Result Structure
  property_count: 3
  slug: oracle-goldengate-veridata-rest-import-result-structure
- name: Oracle Goldengate Veridata Rest Job Execution Structure
  property_count: 5
  slug: oracle-goldengate-veridata-rest-job-execution-structure
- name: Oracle Goldengate Veridata Rest Job List Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-job-list-structure
- name: Oracle Goldengate Veridata Rest Job Statistics List Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-job-statistics-list-structure
- name: Oracle Goldengate Veridata Rest Job Structure
  property_count: 6
  slug: oracle-goldengate-veridata-rest-job-structure
- name: Oracle Goldengate Veridata Rest Login Response Structure
  property_count: 3
  slug: oracle-goldengate-veridata-rest-login-response-structure
- name: Oracle Goldengate Veridata Rest Mapping Object List Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-mapping-object-list-structure
- name: Oracle Goldengate Veridata Rest Mapping Rules Request Structure
  property_count: 3
  slug: oracle-goldengate-veridata-rest-mapping-rules-request-structure
- name: Oracle Goldengate Veridata Rest Metadata Request Structure
  property_count: 2
  slug: oracle-goldengate-veridata-rest-metadata-request-structure
- name: Oracle Goldengate Veridata Rest Out Of Sync Data Structure
  property_count: 2
  slug: oracle-goldengate-veridata-rest-out-of-sync-data-structure
- name: Oracle Goldengate Veridata Rest Profile List Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-profile-list-structure
- name: Oracle Goldengate Veridata Rest Profile Structure
  property_count: 7
  slug: oracle-goldengate-veridata-rest-profile-structure
- name: Oracle Goldengate Veridata Rest Repair Execution Structure
  property_count: 3
  slug: oracle-goldengate-veridata-rest-repair-execution-structure
- name: Oracle Goldengate Veridata Rest Repair Job Request Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-repair-job-request-structure
- name: Oracle Goldengate Veridata Rest Repair Report Structure
  property_count: 6
  slug: oracle-goldengate-veridata-rest-repair-report-structure
- name: Oracle Goldengate Veridata Rest Repair Statistics List Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-repair-statistics-list-structure
- name: Oracle Goldengate Veridata Rest Repaired Row Details Structure
  property_count: 2
  slug: oracle-goldengate-veridata-rest-repaired-row-details-structure
- name: Oracle Goldengate Veridata Rest Replace Compare Pair Request Structure
  property_count: 5
  slug: oracle-goldengate-veridata-rest-replace-compare-pair-request-structure
- name: Oracle Goldengate Veridata Rest Replace Job Request Structure
  property_count: 4
  slug: oracle-goldengate-veridata-rest-replace-job-request-structure
- name: Oracle Goldengate Veridata Rest Replace User Group Request Structure
  property_count: 3
  slug: oracle-goldengate-veridata-rest-replace-user-group-request-structure
- name: Oracle Goldengate Veridata Rest Replace User Request Structure
  property_count: 5
  slug: oracle-goldengate-veridata-rest-replace-user-request-structure
- name: Oracle Goldengate Veridata Rest Run Job Request Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-run-job-request-structure
- name: Oracle Goldengate Veridata Rest Server Configuration Structure
  property_count: 4
  slug: oracle-goldengate-veridata-rest-server-configuration-structure
- name: Oracle Goldengate Veridata Rest Server Info Structure
  property_count: 4
  slug: oracle-goldengate-veridata-rest-server-info-structure
- name: Oracle Goldengate Veridata Rest Server Logs Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-server-logs-structure
- name: Oracle Goldengate Veridata Rest Update Connection Request Structure
  property_count: 6
  slug: oracle-goldengate-veridata-rest-update-connection-request-structure
- name: Oracle Goldengate Veridata Rest Update Group Request Structure
  property_count: 3
  slug: oracle-goldengate-veridata-rest-update-group-request-structure
- name: Oracle Goldengate Veridata Rest Update Profile Request Structure
  property_count: 4
  slug: oracle-goldengate-veridata-rest-update-profile-request-structure
- name: Oracle Goldengate Veridata Rest Update Server Configuration Request Structure
  property_count: 3
  slug: oracle-goldengate-veridata-rest-update-server-configuration-request-structure
- name: Oracle Goldengate Veridata Rest User Group List Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-user-group-list-structure
- name: Oracle Goldengate Veridata Rest User Group Structure
  property_count: 4
  slug: oracle-goldengate-veridata-rest-user-group-structure
- name: Oracle Goldengate Veridata Rest User List Structure
  property_count: 1
  slug: oracle-goldengate-veridata-rest-user-list-structure
- name: Oracle Goldengate Veridata Rest User Structure
  property_count: 7
  slug: oracle-goldengate-veridata-rest-user-structure
- name: Oracle Goldengate Veridata Rest Validate Connection Request Structure
  property_count: 2
  slug: oracle-goldengate-veridata-rest-validate-connection-request-structure
- name: Oracle Goldengate Veridata Rest Validate Database Request Structure
  property_count: 6
  slug: oracle-goldengate-veridata-rest-validate-database-request-structure
- name: Oracle Goldengate Veridata Rest Validation Result Structure
  property_count: 2
  slug: oracle-goldengate-veridata-rest-validation-result-structure
jsonld:
- class_count: 0
  name: Oracle Goldengate Big Data Rest Context
  property_count: 0
  slug: oracle-goldengate-big-data-rest-context
- class_count: 0
  name: Oracle Goldengate Cloud Service Context
  property_count: 0
  slug: oracle-goldengate-cloud-service-context
- class_count: 0
  name: Oracle Goldengate Context
  property_count: 16
  slug: oracle-goldengate-context
- class_count: 0
  name: Oracle Goldengate Data Streams Rest Context
  property_count: 0
  slug: oracle-goldengate-data-streams-rest-context
- class_count: 0
  name: Oracle Goldengate Rest Context
  property_count: 0
  slug: oracle-goldengate-rest-context
- class_count: 0
  name: Oracle Goldengate Stream Analytics Rest Context
  property_count: 0
  slug: oracle-goldengate-stream-analytics-rest-context
- class_count: 0
  name: Oracle Goldengate Veridata Rest Context
  property_count: 0
  slug: oracle-goldengate-veridata-rest-context
layout: provider
modified: '2026-05-19'
name: Oracle GoldenGate
nav: Providers
network: true
overview: 'Oracle GoldenGate publishes 37 APIs on the [APIs.io](https://apis.io/) network, including Artifacts API, AsyncAPI API, Certificates API, and 34 more. Tagged areas include CDC, Data Integration, Data Synchronization, Database, and Enterprise.


  The Oracle GoldenGate catalog on APIs.io includes 7 JSON-LD contexts and 2 Spectral governance rulesets.


  Oracle GoldenGate''s developer surface includes authentication, developer portal, engineering blog, pricing, getting-started guide, documentation, signup flow, and 31 more developer resources.'
plans:
- name: Oracle Goldengate Plans Pricing
  plan_count: 3
  slug: oracle-goldengate-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Oracle Goldengate Rate Limits
  slug: oracle-goldengate-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Oracle GoldenGate API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: oracle-goldengate-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Oracle GoldenGate API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 7
  slug: oracle-goldengate-spectral-rules
score:
  band: strong
  composite: 55.2
  delta: 4.3
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 13.6
    contract_quality: 66.1
    developer_ergonomics: 76.2
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 42.1
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 37
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-goldengate/refs/heads/main/screenshots/oracle-goldengate-2026-06-20T191134.png
security:
- kind: authentication
  name: Oracle Goldengate Authentication
  slug: oracle-goldengate-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Oracle Goldengate Domain Security
  slug: oracle-goldengate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-goldengate
tags:
- CDC
- Data Integration
- Data Synchronization
- Database
- Enterprise
- Real-Time Replication
use_cases:
- Real-time data warehouse loading and synchronization
- Database migration with zero downtime
- Active-active database replication for high availability
- Streaming data to big data platforms (Kafka, Hadoop, Elasticsearch)
- Cloud migration from on-premises Oracle databases to OCI
- Data verification and compliance auditing
- Real-time analytics pipeline construction
website: https://www.oracle.com/integration/goldengate/
---
