---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 137
  human_in_the_loop: 3
  name: Jfrog Agentic Access
  operation_count: 260
  slug: jfrog-agentic-access
  summary_line: 260 operations · 137 acting · 3 human-in-the-loop
api_count: 53
apis:
- description: Token creation and management
  name: JFrog Access Tokens API
  slug: jfrog-access-tokens-api
- description: Deploy, retrieve, copy, move, and delete artifacts
  name: JFrog Artifacts & Storage API
  slug: jfrog-artifacts-storage-api
- description: Curation audit and activity logs
  name: JFrog Audit API
  slug: jfrog-audit-api
- description: Build information and promotion
  name: JFrog Builds API
  slug: jfrog-builds-api
- description: Remote command execution on devices
  name: JFrog Commands API
  slug: jfrog-commands-api
- description: Component details and vulnerability information
  name: JFrog Components API
  slug: jfrog-components-api
- description: Model deployment and serving
  name: JFrog Deployments API
  slug: jfrog-deployments-api
- description: Logical grouping of devices
  name: JFrog Device Groups API
  slug: jfrog-device-groups-api
- description: Device management and monitoring
  name: JFrog Devices API
  slug: jfrog-devices-api
- description: Distribute release bundles to edge nodes
  name: JFrog Distribution API
  slug: jfrog-distribution-api
- description: Create and manage evidence attestations
  name: JFrog Evidence API
  slug: jfrog-evidence-api
- description: Worker testing and execution
  name: JFrog Execution API
  slug: jfrog-execution-api
- description: ML experiment tracking
  name: JFrog Experiments API
  slug: jfrog-experiments-api
- description: GraphQL query interface for package and CVE data
  name: JFrog GraphQL API
  slug: jfrog-graphql-api
- description: User group management
  name: JFrog Groups API
  slug: jfrog-groups-api
- description: Rules for ignoring specific vulnerabilities
  name: JFrog Ignore Rules API
  slug: jfrog-ignore-rules-api
- description: External service integrations
  name: JFrog Integrations API
  slug: jfrog-integrations-api
- description: JFrog Platform Deployment management
  name: JFrog JPDs API
  slug: jfrog-jpds-api
- description: Custom label management for packages
  name: JFrog Labels API
  slug: jfrog-labels-api
- description: License management across instances
  name: JFrog Licenses API
  slug: jfrog-licenses-api
- description: Model version management
  name: JFrog Model Versions API
  slug: jfrog-model-versions-api
- description: ML model registry and management
  name: JFrog Models API
  slug: jfrog-models-api
- description: Build node pool management
  name: JFrog Node Pools API
  slug: jfrog-node-pools-api
- description: Package metadata search and retrieval
  name: JFrog Packages API
  slug: jfrog-packages-api
- description: Permission target management
  name: JFrog Permissions API
  slug: jfrog-permissions-api
- description: Manage pipeline source configurations
  name: JFrog Pipeline Sources API
  slug: jfrog-pipeline-sources-api
- description: Pipeline definitions and management
  name: JFrog Pipelines API
  slug: jfrog-pipelines-api
- description: Curation policy management
  name: JFrog Policies API
  slug: jfrog-policies-api
- description: Project administration
  name: JFrog Projects API
  slug: jfrog-projects-api
- description: Promote release bundles through environments
  name: JFrog Promotion API
  slug: jfrog-promotion-api
- description: Set, update, and delete artifact properties
  name: JFrog Properties API
  slug: jfrog-properties-api
- description: Create and manage release bundles (v1)
  name: JFrog Release Bundles V1 API
  slug: jfrog-release-bundles-v1-api
- description: Create and manage release bundles v2
  name: JFrog Release Bundles V2 API
  slug: jfrog-release-bundles-v2-api
- description: Push and pull replication configuration
  name: JFrog Replication API
  slug: jfrog-replication-api
- description: Vulnerability and compliance reports
  name: JFrog Reports API
  slug: jfrog-reports-api
- description: Create, read, update, and delete repositories
  name: JFrog Repositories API
  slug: jfrog-repositories-api
- description: Pipeline run execution and monitoring
  name: JFrog Runs API
  slug: jfrog-runs-api
- description: On-demand scanning operations
  name: JFrog Scanning API
  slug: jfrog-scanning-api
- description: Remote execution scripts
  name: JFrog Scripts API
  slug: jfrog-scripts-api
- description: Search for artifacts using various criteria
  name: JFrog Searches API
  slug: jfrog-searches-api
- description: Users, groups, permissions, and access tokens
  name: JFrog Security API
  slug: jfrog-security-api
- description: Pipeline step execution details
  name: JFrog Steps API
  slug: jfrog-steps-api
- description: Artifact and build vulnerability summaries
  name: JFrog Summary API
  slug: jfrog-summary-api
- description: Access service system information
  name: JFrog System API
  slug: jfrog-system-api
- description: System health, configuration, and version information
  name: JFrog System & Configuration API
  slug: jfrog-system-configuration-api
- description: Access token creation, management, and revocation
  name: JFrog Tokens API
  slug: jfrog-tokens-api
- description: OTA software update deployments
  name: JFrog Updates API
  slug: jfrog-updates-api
- description: Platform user management
  name: JFrog Users API
  slug: jfrog-users-api
- description: Verify evidence and retrieve verification status
  name: JFrog Verification API
  slug: jfrog-verification-api
- description: Policy violations management
  name: JFrog Violations API
  slug: jfrog-violations-api
- description: Watch policies for monitoring artifacts
  name: JFrog Watches API
  slug: jfrog-watches-api
- description: Webhook configuration
  name: JFrog Webhooks API
  slug: jfrog-webhooks-api
- description: Worker lifecycle management
  name: JFrog Workers API
  slug: jfrog-workers-api
arazzos:
- description: Create a group then a user in that group via the Access service.
  name: JFrog Access Create User With Group
  slug: jfrog-access-create-user-with-group-workflow
- description: Create a project, add a user to it, and confirm the project.
  name: JFrog Access Provision Project
  slug: jfrog-access-provision-project-workflow
- description: Create signed evidence for a build then verify its signature.
  name: JFrog Attach Build Evidence
  slug: jfrog-attach-build-evidence-workflow
- description: Run an AQL search for stale artifacts and delete the first match.
  name: JFrog Cleanup Stale Artifacts
  slug: jfrog-cleanup-stale-artifacts-workflow
- description: Confirm a repository exists then configure push replication for it.
  name: JFrog Configure Repository Replication
  slug: jfrog-configure-repository-replication-workflow
- description: Create a curation policy then review its audit log.
  name: JFrog Curation Policy Setup
  slug: jfrog-curation-policy-setup-workflow
- description: Deploy an artifact to a repository and confirm its storage metadata.
  name: JFrog Deploy and Verify Artifact
  slug: jfrog-deploy-and-verify-artifact-workflow
- description: Create a release bundle, sign it, distribute it, and poll for status.
  name: JFrog Distribution Release Bundle
  slug: jfrog-distribution-release-bundle-workflow
- description: Create a permission target granting a group access to a repository.
  name: JFrog Grant Repository Permission
  slug: jfrog-grant-repository-permission-workflow
- description: Register an ML model then publish a version of it.
  name: JFrog ML Register Model Version
  slug: jfrog-ml-register-model-version-workflow
- description: Trigger a pipeline run, find the new run, and poll until it finishes.
  name: JFrog Pipelines Trigger and Monitor
  slug: jfrog-pipelines-trigger-and-monitor-workflow
- description: Create a platform webhook subscription and confirm it.
  name: JFrog Platform Register Webhook
  slug: jfrog-platform-register-webhook-workflow
- description: Issue a fresh platform token then revoke a superseded one.
  name: JFrog Platform Rotate Access Token
  slug: jfrog-platform-rotate-access-token-workflow
- description: Find an artifact by its checksum and copy it to a release repository.
  name: JFrog Promote Artifact by Checksum
  slug: jfrog-promote-artifact-by-checksum-workflow
- description: Resolve a build run and promote it to a target repository.
  name: JFrog Promote Build
  slug: jfrog-promote-build-workflow
- description: Create a local Artifactory repository and confirm its configuration.
  name: JFrog Provision Local Repository
  slug: jfrog-provision-local-repository-workflow
- description: Create a v2 release bundle from a build and promote it to an environment.
  name: JFrog Release Bundle v2 Promote
  slug: jfrog-release-bundle-v2-promote-workflow
- description: Deploy an artifact then immediately scan it with Xray for issues.
  name: JFrog Secure Publish Artifact
  slug: jfrog-secure-publish-artifact-workflow
- description: Create a worker, run a test payload, then enable it on success.
  name: JFrog Worker Deploy and Test
  slug: jfrog-worker-deploy-and-test-workflow
- description: Look up component details then confirm via the catalog version data.
  name: JFrog Xray Component License Check
  slug: jfrog-xray-component-license-check-workflow
- description: Create a security policy then a watch that assigns it to a repository.
  name: JFrog Xray Policy and Watch
  slug: jfrog-xray-policy-and-watch-workflow
- description: Trigger an Xray scan for an artifact then pull its security summary.
  name: JFrog Xray Scan Artifact
  slug: jfrog-xray-scan-artifact-workflow
- description: Trigger an Xray CI build scan then read the build security summary.
  name: JFrog Xray Scan Build
  slug: jfrog-xray-scan-build-workflow
- description: Query Xray violations and create an ignore rule when any are found.
  name: JFrog Xray Triage Violation
  slug: jfrog-xray-triage-violation-workflow
- description: Generate a vulnerability report and poll until it completes.
  name: JFrog Xray Vulnerability Report
  slug: jfrog-xray-vulnerability-report-workflow
artifact_total: 284
collections:
- collection_type: postman
  name: JFrog Access REST API
  slug: postman-jfrog-access
- collection_type: postman
  name: JFrog Artifactory REST API
  slug: postman-jfrog-artifactory
- collection_type: postman
  name: JFrog Catalog REST API
  slug: postman-jfrog-catalog
- collection_type: postman
  name: JFrog Connect REST API
  slug: postman-jfrog-connect
- collection_type: postman
  name: JFrog Curation REST API
  slug: postman-jfrog-curation
- collection_type: postman
  name: JFrog Distribution REST API
  slug: postman-jfrog-distribution
- collection_type: postman
  name: JFrog Evidence REST API
  slug: postman-jfrog-evidence
- collection_type: postman
  name: JFrog Mission Control REST API
  slug: postman-jfrog-mission-control
- collection_type: postman
  name: JFrog ML REST API
  slug: postman-jfrog-ml
- collection_type: postman
  name: JFrog Pipelines REST API
  slug: postman-jfrog-pipelines
- collection_type: postman
  name: JFrog Platform REST API
  slug: postman-jfrog-platform
- collection_type: postman
  name: JFrog Release Lifecycle Management REST API
  slug: postman-jfrog-release-lifecycle
- collection_type: postman
  name: JFrog Workers REST API
  slug: postman-jfrog-workers
- collection_type: postman
  name: JFrog Xray REST API
  slug: postman-jfrog-xray
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: JFrog Access REST Access Tokens API
  slug: open-jfrog-access-tokens-api
- collection_type: open
  name: JFrog Access REST API
  slug: open-jfrog-access
- collection_type: open
  name: JFrog Artifactory REST API
  slug: open-jfrog-artifactory
- collection_type: open
  name: JFrog Access REST Access Tokens Artifacts & Storage API
  slug: open-jfrog-artifacts-storage-api
- collection_type: open
  name: JFrog Access REST Access Tokens Audit API
  slug: open-jfrog-audit-api
- collection_type: open
  name: JFrog Access REST Access Tokens Builds API
  slug: open-jfrog-builds-api
- collection_type: open
  name: JFrog Catalog REST API
  slug: open-jfrog-catalog
- collection_type: open
  name: JFrog Access REST Access Tokens Commands API
  slug: open-jfrog-commands-api
- collection_type: open
  name: JFrog Access REST Access Tokens Components API
  slug: open-jfrog-components-api
- collection_type: open
  name: JFrog Connect REST API
  slug: open-jfrog-connect
- collection_type: open
  name: JFrog Curation REST API
  slug: open-jfrog-curation
- collection_type: open
  name: JFrog Access REST Access Tokens Deployments API
  slug: open-jfrog-deployments-api
- collection_type: open
  name: JFrog Access REST Access Tokens Device Groups API
  slug: open-jfrog-device-groups-api
- collection_type: open
  name: JFrog Access REST Access Tokens Devices API
  slug: open-jfrog-devices-api
- collection_type: open
  name: JFrog Access REST Access Tokens Distribution API
  slug: open-jfrog-distribution-api
- collection_type: open
  name: JFrog Distribution REST API
  slug: open-jfrog-distribution
- collection_type: open
  name: JFrog Access REST Access Tokens Evidence API
  slug: open-jfrog-evidence-api
- collection_type: open
  name: JFrog Evidence REST API
  slug: open-jfrog-evidence
- collection_type: open
  name: JFrog Access REST Access Tokens Execution API
  slug: open-jfrog-execution-api
- collection_type: open
  name: JFrog Access REST Access Tokens Experiments API
  slug: open-jfrog-experiments-api
- collection_type: open
  name: JFrog Access REST Access Tokens GraphQL API
  slug: open-jfrog-graphql-api
- collection_type: open
  name: JFrog Access REST Access Tokens Groups API
  slug: open-jfrog-groups-api
- collection_type: open
  name: JFrog Access REST Access Tokens Ignore Rules API
  slug: open-jfrog-ignore-rules-api
- collection_type: open
  name: JFrog Access REST Access Tokens Integrations API
  slug: open-jfrog-integrations-api
- collection_type: open
  name: JFrog Access REST Access Tokens JPDs API
  slug: open-jfrog-jpds-api
- collection_type: open
  name: JFrog Access REST Access Tokens Labels API
  slug: open-jfrog-labels-api
- collection_type: open
  name: JFrog Access REST Access Tokens Licenses API
  slug: open-jfrog-licenses-api
- collection_type: open
  name: JFrog Mission Control REST API
  slug: open-jfrog-mission-control
- collection_type: open
  name: JFrog ML REST API
  slug: open-jfrog-ml
- collection_type: open
  name: JFrog Access REST Access Tokens Model Versions API
  slug: open-jfrog-model-versions-api
- collection_type: open
  name: JFrog Access REST Access Tokens Models API
  slug: open-jfrog-models-api
- collection_type: open
  name: JFrog Access REST Access Tokens Node Pools API
  slug: open-jfrog-node-pools-api
- collection_type: open
  name: JFrog Access REST Access Tokens Packages API
  slug: open-jfrog-packages-api
- collection_type: open
  name: JFrog Access REST Access Tokens Permissions API
  slug: open-jfrog-permissions-api
- collection_type: open
  name: JFrog Access REST Access Tokens Pipeline Sources API
  slug: open-jfrog-pipeline-sources-api
- collection_type: open
  name: JFrog Access REST Access Tokens Pipelines API
  slug: open-jfrog-pipelines-api
- collection_type: open
  name: JFrog Pipelines REST API
  slug: open-jfrog-pipelines
- collection_type: open
  name: JFrog Platform REST API
  slug: open-jfrog-platform
- collection_type: open
  name: JFrog Access REST Access Tokens Policies API
  slug: open-jfrog-policies-api
- collection_type: open
  name: JFrog Access REST Access Tokens Projects API
  slug: open-jfrog-projects-api
- collection_type: open
  name: JFrog Access REST Access Tokens Promotion API
  slug: open-jfrog-promotion-api
- collection_type: open
  name: JFrog Access REST Access Tokens Properties API
  slug: open-jfrog-properties-api
- collection_type: open
  name: JFrog Access REST Access Tokens Release Bundles V1 API
  slug: open-jfrog-release-bundles-v1-api
- collection_type: open
  name: JFrog Access REST Access Tokens Release Bundles V2 API
  slug: open-jfrog-release-bundles-v2-api
- collection_type: open
  name: JFrog Release Lifecycle Management REST API
  slug: open-jfrog-release-lifecycle
- collection_type: open
  name: JFrog Access REST Access Tokens Replication API
  slug: open-jfrog-replication-api
- collection_type: open
  name: JFrog Access REST Access Tokens Reports API
  slug: open-jfrog-reports-api
- collection_type: open
  name: JFrog Access REST Access Tokens Repositories API
  slug: open-jfrog-repositories-api
- collection_type: open
  name: JFrog Access REST Access Tokens Runs API
  slug: open-jfrog-runs-api
- collection_type: open
  name: JFrog Access REST Access Tokens Scanning API
  slug: open-jfrog-scanning-api
- collection_type: open
  name: JFrog Access REST Access Tokens Scripts API
  slug: open-jfrog-scripts-api
- collection_type: open
  name: JFrog Access REST Access Tokens Searches API
  slug: open-jfrog-searches-api
- collection_type: open
  name: JFrog Access REST Access Tokens Security API
  slug: open-jfrog-security-api
- collection_type: open
  name: JFrog Access REST Access Tokens Steps API
  slug: open-jfrog-steps-api
- collection_type: open
  name: JFrog Access REST Access Tokens Summary API
  slug: open-jfrog-summary-api
- collection_type: open
  name: JFrog Access REST Access Tokens System API
  slug: open-jfrog-system-api
- collection_type: open
  name: JFrog Access REST Access Tokens System & Configuration API
  slug: open-jfrog-system-configuration-api
- collection_type: open
  name: JFrog Access REST Access Tokens API
  slug: open-jfrog-tokens-api
- collection_type: open
  name: JFrog Access REST Access Tokens Updates API
  slug: open-jfrog-updates-api
- collection_type: open
  name: JFrog Access REST Access Tokens Users API
  slug: open-jfrog-users-api
- collection_type: open
  name: JFrog Access REST Access Tokens Verification API
  slug: open-jfrog-verification-api
- collection_type: open
  name: JFrog Access REST Access Tokens Violations API
  slug: open-jfrog-violations-api
- collection_type: open
  name: JFrog Access REST Access Tokens Watches API
  slug: open-jfrog-watches-api
- collection_type: open
  name: JFrog Access REST Access Tokens Webhooks API
  slug: open-jfrog-webhooks-api
- collection_type: open
  name: JFrog Access REST Access Tokens Workers API
  slug: open-jfrog-workers-api
- collection_type: open
  name: JFrog Workers REST API
  slug: open-jfrog-workers
- collection_type: open
  name: JFrog Xray REST API
  slug: open-jfrog-xray
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jfrog-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jfrog-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jfrog-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jfrog-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/jfrog/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-access-create-user-with-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-access-provision-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-attach-build-evidence-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-cleanup-stale-artifacts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-configure-repository-replication-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-curation-policy-setup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-deploy-and-verify-artifact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-distribution-release-bundle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-grant-repository-permission-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-ml-register-model-version-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-pipelines-trigger-and-monitor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-platform-register-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-platform-rotate-access-token-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-promote-artifact-by-checksum-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-promote-build-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-provision-local-repository-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-release-bundle-v2-promote-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-secure-publish-artifact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-worker-deploy-and-test-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-xray-component-license-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-xray-policy-and-watch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-xray-scan-artifact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-xray-scan-build-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-xray-triage-violation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jfrog-xray-vulnerability-report-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://jfrog.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://jfrog.com/help/r/jfrog-rest-apis/jfrog-rest-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://jfrog.com/artifactory/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-tokens
- group: company
  title: ''
  type: Blog
  url: https://jfrog.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jfrog.io/
- group: operate
  title: ''
  type: Support
  url: https://jfrog.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jfrog.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jfrog.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jfrog
- group: operate
  title: ''
  type: Community
  url: https://jfrog.com/community/
- group: company
  title: ''
  type: Website
  url: https://jfrog.com/
- group: start
  title: ''
  type: Login
  url: https://my.jfrog.com/login/
- group: start
  title: ''
  type: Signup
  url: https://jfrog.com/start-free/
- group: commercial
  title: ''
  type: Pricing
  url: https://jfrog.com/pricing/
- group: build
  title: ''
  type: CLI
  url: https://jfrog.com/getcli/
- group: operate
  title: ''
  type: ChangeLog
  url: https://jfrog.com/help/r/jfrog-release-information/jfrog-release-notes
- group: build
  title: ''
  type: SDKs
  url: https://github.com/jfrog/jfrog-client-go
- group: build
  title: ''
  type: Java SDK
  url: https://github.com/jfrog/artifactory-client-java
- group: build
  title: ''
  type: JavaScript SDK
  url: https://github.com/jfrog/jfrog-client-js
- group: learn
  title: ''
  type: Academy
  url: https://academy.jfrog.com/
- group: design
  title: ''
  type: Webhooks
  url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/webhooks
- group: other
  title: ''
  type: Terraform Provider
  url: https://registry.terraform.io/providers/jfrog/platform/latest/docs
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@jfrog
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/jfrog
- group: operate
  title: ''
  type: RateLimits
  url: https://jfrog.com/help/r/jfrog-rest-apis/usage-and-rate-limits
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/api-evangelist/jfrog/documentation/zgmorin/jfrog-rest-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jfrog-ltd
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/jfrog-context.jsonld
- group: docs
  title: ''
  type: JSON Schema - Artifact
  url: json-schema/jfrog-artifact-schema.json
- group: docs
  title: ''
  type: JSON Schema - Repository
  url: json-schema/jfrog-repository-schema.json
- group: docs
  title: ''
  type: JSON Schema - Build Info
  url: json-schema/jfrog-build-info-schema.json
- group: docs
  title: ''
  type: JSON Schema - Release Bundle
  url: json-schema/jfrog-release-bundle-schema.json
- group: docs
  title: ''
  type: JSON Schema - Security Vulnerability
  url: json-schema/jfrog-security-vulnerability-schema.json
- group: docs
  title: ''
  type: JSON Schema - User
  url: json-schema/jfrog-user-schema.json
- group: docs
  title: ''
  type: JSON Schema - Permission
  url: json-schema/jfrog-permission-schema.json
- group: docs
  title: ''
  type: JSON Schema - Pipeline
  url: json-schema/jfrog-pipeline-schema.json
- group: docs
  title: ''
  type: JSON Schema - Worker
  url: json-schema/jfrog-worker-schema.json
- group: docs
  title: ''
  type: JSON Schema - Curation Policy
  url: json-schema/jfrog-curation-policy-schema.json
- group: docs
  title: ''
  type: JSON Schema - Evidence
  url: json-schema/jfrog-evidence-schema.json
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/jfrog/mcp-jfrog
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/jfrog/jfrog-skills
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.connect.jfrog.io/llms.txt
created: '2024'
description: JFrog provides universal DevOps solutions for software supply chain automation and security, offering a unified platform for managing binaries, securing the software supply chain, and automating DevOps workflows.
finops:
- name: Jfrog Finops
  service_category: DevOps / Software Supply Chain
  slug: jfrog-finops
graphqls:
- description: ''
  name: JFrog GraphQL API
  slug: jfrog-graphql
image: https://jfrog.com/brand/jfrog-logo.png
json_schemas:
- name: AccessToken
  property_count: 5
  slug: jfrog-accesstoken
- name: AqlSearchResult
  property_count: 2
  slug: jfrog-aqlsearchresult
- name: JFrog Artifact
  property_count: 16
  slug: jfrog-artifact
- name: ArtifactSummary
  property_count: 1
  slug: jfrog-artifactsummary
- name: AuditEntry
  property_count: 9
  slug: jfrog-auditentry
- name: JFrog Build Info
  property_count: 16
  slug: jfrog-build-info
- name: BuildInfo
  property_count: 1
  slug: jfrog-buildinfo
- name: BuildPromotion
  property_count: 11
  slug: jfrog-buildpromotion
- name: BuildRuns
  property_count: 2
  slug: jfrog-buildruns
- name: BuildsList
  property_count: 1
  slug: jfrog-buildslist
- name: BuildSummary
  property_count: 2
  slug: jfrog-buildsummary
- name: CatalogVulnerability
  property_count: 9
  slug: jfrog-catalogvulnerability
- name: Checksums
  property_count: 3
  slug: jfrog-checksums
- name: CommandRequest
  property_count: 4
  slug: jfrog-commandrequest
- name: ComponentDetail
  property_count: 6
  slug: jfrog-componentdetail
- name: CreateEvidenceRequest
  property_count: 6
  slug: jfrog-createevidencerequest
- name: CreateTokenRequest
  property_count: 8
  slug: jfrog-createtokenrequest
- name: CreateUserRequest
  property_count: 7
  slug: jfrog-createuserrequest
- name: JFrog Curation Policy
  property_count: 10
  slug: jfrog-curation-policy
- name: CurationPolicy
  property_count: 10
  slug: jfrog-curationpolicy
- name: CurationPolicyRequest
  property_count: 8
  slug: jfrog-curationpolicyrequest
- name: Deployment
  property_count: 9
  slug: jfrog-deployment
- name: DeploymentRequest
  property_count: 5
  slug: jfrog-deploymentrequest
- name: DeployResponse
  property_count: 10
  slug: jfrog-deployresponse
- name: Device
  property_count: 13
  slug: jfrog-device
- name: DeviceGroup
  property_count: 5
  slug: jfrog-devicegroup
- name: DeviceGroupRequest
  property_count: 3
  slug: jfrog-devicegrouprequest
- name: DistributeRequest
  property_count: 2
  slug: jfrog-distributerequest
- name: DistributionRequest
  property_count: 3
  slug: jfrog-distributionrequest
- name: JFrog Evidence
  property_count: 11
  slug: jfrog-evidence
- name: EvidenceRequest
  property_count: 6
  slug: jfrog-evidencerequest
- name: EvidenceSearchRequest
  property_count: 7
  slug: jfrog-evidencesearchrequest
- name: Experiment
  property_count: 10
  slug: jfrog-experiment
- name: ExperimentRequest
  property_count: 4
  slug: jfrog-experimentrequest
- name: FileInfo
  property_count: 13
  slug: jfrog-fileinfo
- name: FolderInfo
  property_count: 9
  slug: jfrog-folderinfo
- name: GraphQLRequest
  property_count: 3
  slug: jfrog-graphqlrequest
- name: GraphQLResponse
  property_count: 2
  slug: jfrog-graphqlresponse
- name: Group
  property_count: 7
  slug: jfrog-group
- name: GroupSummary
  property_count: 2
  slug: jfrog-groupsummary
- name: IgnoreRule
  property_count: 10
  slug: jfrog-ignorerule
- name: Integration
  property_count: 7
  slug: jfrog-integration
- name: IntegrationRequest
  property_count: 5
  slug: jfrog-integrationrequest
- name: Issue
  property_count: 9
  slug: jfrog-issue
- name: ItemProperties
  property_count: 2
  slug: jfrog-itemproperties
- name: JPD
  property_count: 7
  slug: jfrog-jpd
- name: JPDRequest
  property_count: 4
  slug: jfrog-jpdrequest
- name: Label
  property_count: 6
  slug: jfrog-label
- name: LabelRequest
  property_count: 3
  slug: jfrog-labelrequest
- name: LicenseBucket
  property_count: 6
  slug: jfrog-licensebucket
- name: LicenseInfo
  property_count: 3
  slug: jfrog-licenseinfo
- name: Model
  property_count: 11
  slug: jfrog-model
- name: ModelRequest
  property_count: 5
  slug: jfrog-modelrequest
- name: ModelVersion
  property_count: 10
  slug: jfrog-modelversion
- name: ModelVersionRequest
  property_count: 6
  slug: jfrog-modelversionrequest
- name: MoveOrCopyResponse
  property_count: 1
  slug: jfrog-moveorcopyresponse
- name: NodePool
  property_count: 9
  slug: jfrog-nodepool
- name: NodePoolRequest
  property_count: 6
  slug: jfrog-nodepoolrequest
- name: PackageDetail
  property_count: 10
  slug: jfrog-packagedetail
- name: PackageSearchRequest
  property_count: 7
  slug: jfrog-packagesearchrequest
- name: PackageSearchResponse
  property_count: 2
  slug: jfrog-packagesearchresponse
- name: PackageSummary
  property_count: 7
  slug: jfrog-packagesummary
- name: PackageVersion
  property_count: 7
  slug: jfrog-packageversion
- name: JFrog Permission Target
  property_count: 2
  slug: jfrog-permission
- name: PermissionTarget
  property_count: 3
  slug: jfrog-permissiontarget
- name: PermissionTargetSummary
  property_count: 2
  slug: jfrog-permissiontargetsummary
- name: JFrog Pipeline
  property_count: 9
  slug: jfrog-pipeline
- name: PipelineSource
  property_count: 9
  slug: jfrog-pipelinesource
- name: PipelineSourceRequest
  property_count: 6
  slug: jfrog-pipelinesourcerequest
- name: PlatformGroup
  property_count: 7
  slug: jfrog-platformgroup
- name: PlatformUser
  property_count: 8
  slug: jfrog-platformuser
- name: Policy
  property_count: 4
  slug: jfrog-policy
- name: Project
  property_count: 8
  slug: jfrog-project
- name: ProjectRequest
  property_count: 5
  slug: jfrog-projectrequest
- name: PromotionRequest
  property_count: 5
  slug: jfrog-promotionrequest
- name: PromotionStatus
  property_count: 4
  slug: jfrog-promotionstatus
- name: JFrog Release Bundle
  property_count: 13
  slug: jfrog-release-bundle
- name: ReleaseBundle
  property_count: 8
  slug: jfrog-releasebundle
- name: ReleaseBundleRequest
  property_count: 7
  slug: jfrog-releasebundlerequest
- name: ReleaseBundleV2
  property_count: 9
  slug: jfrog-releasebundlev2
- name: ReleaseBundleV2Request
  property_count: 5
  slug: jfrog-releasebundlev2request
- name: ReleaseBundleV2Summary
  property_count: 6
  slug: jfrog-releasebundlev2summary
- name: ReplicationConfig
  property_count: 12
  slug: jfrog-replicationconfig
- name: JFrog Repository
  property_count: 20
  slug: jfrog-repository
- name: RepositoryConfiguration
  property_count: 15
  slug: jfrog-repositoryconfiguration
- name: RepositoryListItem
  property_count: 5
  slug: jfrog-repositorylistitem
- name: Run
  property_count: 10
  slug: jfrog-run
- name: Script
  property_count: 5
  slug: jfrog-script
- name: ScriptRequest
  property_count: 3
  slug: jfrog-scriptrequest
- name: SearchResult
  property_count: 1
  slug: jfrog-searchresult
- name: JFrog Security Vulnerability
  property_count: 16
  slug: jfrog-security-vulnerability
- name: Step
  property_count: 9
  slug: jfrog-step
- name: StorageSummary
  property_count: 3
  slug: jfrog-storagesummary
- name: SystemHealth
  property_count: 2
  slug: jfrog-systemhealth
- name: SystemVersion
  property_count: 4
  slug: jfrog-systemversion
- name: TokenInfo
  property_count: 9
  slug: jfrog-tokeninfo
- name: TokenResponse
  property_count: 7
  slug: jfrog-tokenresponse
- name: Update
  property_count: 10
  slug: jfrog-update
- name: UpdateRequest
  property_count: 12
  slug: jfrog-updaterequest
- name: UpdateUserRequest
  property_count: 7
  slug: jfrog-updateuserrequest
- name: JFrog Platform User
  property_count: 11
  slug: jfrog-user
- name: UserSummary
  property_count: 4
  slug: jfrog-usersummary
- name: VerificationResult
  property_count: 6
  slug: jfrog-verificationresult
- name: ViolationsResponse
  property_count: 2
  slug: jfrog-violationsresponse
- name: Vulnerability
  property_count: 9
  slug: jfrog-vulnerability
- name: Watch
  property_count: 3
  slug: jfrog-watch
- name: Webhook
  property_count: 7
  slug: jfrog-webhook
- name: WebhookRequest
  property_count: 7
  slug: jfrog-webhookrequest
- name: JFrog Worker
  property_count: 9
  slug: jfrog-worker
- name: WorkerRequest
  property_count: 7
  slug: jfrog-workerrequest
json_structures:
- name: Jfrog Structure
  property_count: 0
  slug: jfrog-structure
jsonld:
- class_count: 9
  name: Jfrog Context
  property_count: 13
  slug: jfrog-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: JFrog
nav: Providers
network: true
overview: 'JFrog publishes 53 APIs on the [APIs.io](https://apis.io/) network, including Access Tokens API, Artifacts & Storage API, Audit API, and 50 more. Tagged areas include Artifactory, CI/CD, Container Registry, DevOps, and MLOps.


  The JFrog catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  JFrog''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, signup flow, and 66 more developer resources.'
plans:
- name: Jfrog Plans Pricing
  plan_count: 8
  slug: jfrog-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 3
  name: Jfrog Rate Limits
  slug: jfrog-rate-limits
rules:
- name: JFrog API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: jfrog-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 68.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 68.0
    developer_ergonomics: 87.0
    discoverability: 83.3
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 68.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 53
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jfrog/refs/heads/main/screenshots/jfrog-2026-06-20T183730.png
security:
- kind: authentication
  name: Jfrog Authentication
  slug: jfrog-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Jfrog Domain Security
  slug: jfrog-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jfrog Vulnerability Disclosure
  slug: jfrog-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: jfrog-package-safety-and-download
  slug: jfrog-package-safety-and-download
- name: jfrog
  slug: jfrog
slug: jfrog
tags:
- Artifactory
- CI/CD
- Container Registry
- DevOps
- MLOps
- Package Management
- Security
- Software Supply Chain
website: https://jfrog.com/
---
