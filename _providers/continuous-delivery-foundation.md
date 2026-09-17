---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: templated
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.1
  scored_at: '2026-09-16'
api_count: 7
apis:
- description: CDEvents is a common specification for Continuous Delivery events that enables interoperability across CI/CD systems. It extends the CloudEvents specification and defines event vocabularies for source
  name: CDEvents Specification
  slug: cdevents
- description: Ortelius is an open source supply chain evidence store that aggregates continuous security intelligence across the software delivery lifecycle. It exposes APIs for tracking microservice components, SB
  name: Ortelius
  slug: ortelius
- description: The Continuous Delivery Foundation publishes a machine-readable index of its own website content. The foundation serves an RFC 9727 API catalog at /.well-known/api-catalog which anchors https://cd.fou
  name: CD Foundation Content API
  slug: content-api
- description: Tekton is a Kubernetes-native open source framework for creating CI/CD systems. It defines Custom Resource Definitions for Pipelines, Tasks, PipelineRuns, and TaskRuns and was originally hosted at the
  name: Tekton
  slug: tekton
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The admin-controller API from Continuous Delivery Foundation — 3 operation(s) for admin-controller.
  name: Continuous Delivery Foundation Admin Controller API
  slug: continuous-delivery-foundation-admin-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The amazon-infrastructure-controller API from Continuous Delivery Foundation — 6 operation(s) for amazon-infrastructure-controller.
  name: Continuous Delivery Foundation Amazon Infrastructure Controller API
  slug: continuous-delivery-foundation-amazon-infrastructure-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The api-extension-controller API from Continuous Delivery Foundation — 1 operation(s) for api-extension-controller.
  name: Continuous Delivery Foundation API Extension Controller API
  slug: continuous-delivery-foundation-api-extension-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The application-controller API from Continuous Delivery Foundation — 13 operation(s) for application-controller.
  name: Continuous Delivery Foundation Application Controller API
  slug: continuous-delivery-foundation-application-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The artifact-controller API from Continuous Delivery Foundation — 7 operation(s) for artifact-controller.
  name: Continuous Delivery Foundation Artifact Controller API
  slug: continuous-delivery-foundation-artifact-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The artifactory-controller API from Continuous Delivery Foundation — 1 operation(s) for artifactory-controller.
  name: Continuous Delivery Foundation Artifactory Controller API
  slug: continuous-delivery-foundation-artifactory-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The auth-controller API from Continuous Delivery Foundation — 6 operation(s) for auth-controller.
  name: Continuous Delivery Foundation Auth Controller API
  slug: continuous-delivery-foundation-auth-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The bake-controller API from Continuous Delivery Foundation — 3 operation(s) for bake-controller.
  name: Continuous Delivery Foundation Bake Controller API
  slug: continuous-delivery-foundation-bake-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The batch-entity-tags-controller API from Continuous Delivery Foundation — 1 operation(s) for batch-entity-tags-controller.
  name: Continuous Delivery Foundation Batch Entity Tags Controller API
  slug: continuous-delivery-foundation-batch-entity-tags-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The build-controller API from Continuous Delivery Foundation — 10 operation(s) for build-controller.
  name: Continuous Delivery Foundation Build Controller API
  slug: continuous-delivery-foundation-build-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The capabilities-controller API from Continuous Delivery Foundation — 3 operation(s) for capabilities-controller.
  name: Continuous Delivery Foundation Capabilities Controller API
  slug: continuous-delivery-foundation-capabilities-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The certificate-controller API from Continuous Delivery Foundation — 2 operation(s) for certificate-controller.
  name: Continuous Delivery Foundation Certificate Controller API
  slug: continuous-delivery-foundation-certificate-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The chart-image-controller API from Continuous Delivery Foundation — 3 operation(s) for chart-image-controller.
  name: Continuous Delivery Foundation Chart Image Controller API
  slug: continuous-delivery-foundation-chart-image-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The ci-controller API from Continuous Delivery Foundation — 2 operation(s) for ci-controller.
  name: Continuous Delivery Foundation Ci Controller API
  slug: continuous-delivery-foundation-ci-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The cleanup-controller API from Continuous Delivery Foundation — 4 operation(s) for cleanup-controller.
  name: Continuous Delivery Foundation Cleanup Controller API
  slug: continuous-delivery-foundation-cleanup-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The cloud-metric-controller API from Continuous Delivery Foundation — 2 operation(s) for cloud-metric-controller.
  name: Continuous Delivery Foundation Cloud Metric Controller API
  slug: continuous-delivery-foundation-cloud-metric-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The cluster-controller API from Continuous Delivery Foundation — 8 operation(s) for cluster-controller.
  name: Continuous Delivery Foundation Cluster Controller API
  slug: continuous-delivery-foundation-cluster-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The concourse-controller API from Continuous Delivery Foundation — 5 operation(s) for concourse-controller.
  name: Continuous Delivery Foundation Concourse Controller API
  slug: continuous-delivery-foundation-concourse-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The credentials-controller API from Continuous Delivery Foundation — 4 operation(s) for credentials-controller.
  name: Continuous Delivery Foundation Credentials Controller API
  slug: continuous-delivery-foundation-credentials-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The cron-controller API from Continuous Delivery Foundation — 1 operation(s) for cron-controller.
  name: Continuous Delivery Foundation Cron Controller API
  slug: continuous-delivery-foundation-cron-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The data-controller API from Continuous Delivery Foundation — 2 operation(s) for data-controller.
  name: Continuous Delivery Foundation Data Controller API
  slug: continuous-delivery-foundation-data-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The deck-plugins-controller API from Continuous Delivery Foundation — 2 operation(s) for deck-plugins-controller.
  name: Continuous Delivery Foundation Deck Plugins Controller API
  slug: continuous-delivery-foundation-deck-plugins-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The ecs-cloud-metric-controller API from Continuous Delivery Foundation — 1 operation(s) for ecs-cloud-metric-controller.
  name: Continuous Delivery Foundation Ecs Cloud Metric Controller API
  slug: continuous-delivery-foundation-ecs-cloud-metric-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The ecs-cluster-controller API from Continuous Delivery Foundation — 2 operation(s) for ecs-cluster-controller.
  name: Continuous Delivery Foundation Ecs Cluster Controller API
  slug: continuous-delivery-foundation-ecs-cluster-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The ecs-secret-controller API from Continuous Delivery Foundation — 1 operation(s) for ecs-secret-controller.
  name: Continuous Delivery Foundation Ecs Secret Controller API
  slug: continuous-delivery-foundation-ecs-secret-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The ecs-server-group-events-controller API from Continuous Delivery Foundation — 1 operation(s) for ecs-server-group-events-controller.
  name: Continuous Delivery Foundation Ecs Server Group Events Controller API
  slug: continuous-delivery-foundation-ecs-server-group-events-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The ecs-service-discovery-controller API from Continuous Delivery Foundation — 1 operation(s) for ecs-service-discovery-controller.
  name: Continuous Delivery Foundation Ecs Service Discovery Controller API
  slug: continuous-delivery-foundation-ecs-service-discovery-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The entity-tags-controller API from Continuous Delivery Foundation — 3 operation(s) for entity-tags-controller.
  name: Continuous Delivery Foundation Entity Tags Controller API
  slug: continuous-delivery-foundation-entity-tags-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The executions-controller API from Continuous Delivery Foundation — 3 operation(s) for executions-controller.
  name: Continuous Delivery Foundation Executions Controller API
  slug: continuous-delivery-foundation-executions-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The firewall-controller API from Continuous Delivery Foundation — 4 operation(s) for firewall-controller.
  name: Continuous Delivery Foundation Firewall Controller API
  slug: continuous-delivery-foundation-firewall-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The generic-error-controller API from Continuous Delivery Foundation — 1 operation(s) for generic-error-controller.
  name: Continuous Delivery Foundation Generic Error Controller API
  slug: continuous-delivery-foundation-generic-error-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The history-controller API from Continuous Delivery Foundation — 1 operation(s) for history-controller.
  name: Continuous Delivery Foundation History Controller API
  slug: continuous-delivery-foundation-history-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The image-controller API from Continuous Delivery Foundation — 3 operation(s) for image-controller.
  name: Continuous Delivery Foundation Image Controller API
  slug: continuous-delivery-foundation-image-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The instance-controller API from Continuous Delivery Foundation — 2 operation(s) for instance-controller.
  name: Continuous Delivery Foundation Instance Controller API
  slug: continuous-delivery-foundation-instance-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The job-controller API from Continuous Delivery Foundation — 2 operation(s) for job-controller.
  name: Continuous Delivery Foundation Job Controller API
  slug: continuous-delivery-foundation-job-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The load-balancer-controller API from Continuous Delivery Foundation — 4 operation(s) for load-balancer-controller.
  name: Continuous Delivery Foundation Load Balancer Controller API
  slug: continuous-delivery-foundation-load-balancer-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The managed-controller API from Continuous Delivery Foundation — 32 operation(s) for managed-controller.
  name: Continuous Delivery Foundation Managed Controller API
  slug: continuous-delivery-foundation-managed-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The manifest-controller API from Continuous Delivery Foundation — 1 operation(s) for manifest-controller.
  name: Continuous Delivery Foundation Manifest Controller API
  slug: continuous-delivery-foundation-manifest-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: APIs for viewing multiple pipeline runs
  name: Continuous Delivery Foundation Multi-Pipeline Graph API
  slug: continuous-delivery-foundation-multi-pipeline-graph-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The network-controller API from Continuous Delivery Foundation — 2 operation(s) for network-controller.
  name: Continuous Delivery Foundation Network Controller API
  slug: continuous-delivery-foundation-network-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The nexus-controller API from Continuous Delivery Foundation — 1 operation(s) for nexus-controller.
  name: Continuous Delivery Foundation Nexus Controller API
  slug: continuous-delivery-foundation-nexus-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The notification-controller API from Continuous Delivery Foundation — 3 operation(s) for notification-controller.
  name: Continuous Delivery Foundation Notification Controller API
  slug: continuous-delivery-foundation-notification-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The pipeline-config-controller API from Continuous Delivery Foundation — 3 operation(s) for pipeline-config-controller.
  name: Continuous Delivery Foundation Pipeline Config Controller API
  slug: continuous-delivery-foundation-pipeline-config-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The pipeline-controller API from Continuous Delivery Foundation — 16 operation(s) for pipeline-controller.
  name: Continuous Delivery Foundation Pipeline Controller API
  slug: continuous-delivery-foundation-pipeline-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: APIs for individual pipeline run visualization and control
  name: Continuous Delivery Foundation Pipeline Overview API
  slug: continuous-delivery-foundation-pipeline-overview-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The pipeline-templates-controller API from Continuous Delivery Foundation — 4 operation(s) for pipeline-templates-controller.
  name: Continuous Delivery Foundation Pipeline Templates Controller API
  slug: continuous-delivery-foundation-pipeline-templates-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The plugin-info-controller API from Continuous Delivery Foundation — 2 operation(s) for plugin-info-controller.
  name: Continuous Delivery Foundation Plugin Info Controller API
  slug: continuous-delivery-foundation-plugin-info-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The plugin-publish-controller API from Continuous Delivery Foundation — 1 operation(s) for plugin-publish-controller.
  name: Continuous Delivery Foundation Plugin Publish Controller API
  slug: continuous-delivery-foundation-plugin-publish-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The plugins-installed-controller API from Continuous Delivery Foundation — 1 operation(s) for plugins-installed-controller.
  name: Continuous Delivery Foundation Plugins Installed Controller API
  slug: continuous-delivery-foundation-plugins-installed-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The project-controller API from Continuous Delivery Foundation — 4 operation(s) for project-controller.
  name: Continuous Delivery Foundation Project Controller API
  slug: continuous-delivery-foundation-project-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The proxy-controller API from Continuous Delivery Foundation — 2 operation(s) for proxy-controller.
  name: Continuous Delivery Foundation Proxy Controller API
  slug: continuous-delivery-foundation-proxy-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The pubsub-subscription-controller API from Continuous Delivery Foundation — 1 operation(s) for pubsub-subscription-controller.
  name: Continuous Delivery Foundation Pubsub Subscription Controller API
  slug: continuous-delivery-foundation-pubsub-subscription-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The raw-resource-controller API from Continuous Delivery Foundation — 1 operation(s) for raw-resource-controller.
  name: Continuous Delivery Foundation Raw Resource Controller API
  slug: continuous-delivery-foundation-raw-resource-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The reorder-pipelines-controller API from Continuous Delivery Foundation — 2 operation(s) for reorder-pipelines-controller.
  name: Continuous Delivery Foundation Reorder Pipelines Controller API
  slug: continuous-delivery-foundation-reorder-pipelines-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The role-controller API from Continuous Delivery Foundation — 1 operation(s) for role-controller.
  name: Continuous Delivery Foundation Role Controller API
  slug: continuous-delivery-foundation-role-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The root-controller API from Continuous Delivery Foundation — 1 operation(s) for root-controller.
  name: Continuous Delivery Foundation Root Controller API
  slug: continuous-delivery-foundation-root-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The search-controller API from Continuous Delivery Foundation — 1 operation(s) for search-controller.
  name: Continuous Delivery Foundation Search Controller API
  slug: continuous-delivery-foundation-search-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The security-group-controller API from Continuous Delivery Foundation — 3 operation(s) for security-group-controller.
  name: Continuous Delivery Foundation Security Group Controller API
  slug: continuous-delivery-foundation-security-group-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The server-group-controller API from Continuous Delivery Foundation — 3 operation(s) for server-group-controller.
  name: Continuous Delivery Foundation Server Group Controller API
  slug: continuous-delivery-foundation-server-group-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The server-group-manager-controller API from Continuous Delivery Foundation — 1 operation(s) for server-group-manager-controller.
  name: Continuous Delivery Foundation Server Group Manager Controller API
  slug: continuous-delivery-foundation-server-group-manager-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The service-broker-controller API from Continuous Delivery Foundation — 2 operation(s) for service-broker-controller.
  name: Continuous Delivery Foundation Service Broker Controller API
  slug: continuous-delivery-foundation-service-broker-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The snapshot-controller API from Continuous Delivery Foundation — 2 operation(s) for snapshot-controller.
  name: Continuous Delivery Foundation Snapshot Controller API
  slug: continuous-delivery-foundation-snapshot-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The storage-account-controller API from Continuous Delivery Foundation — 1 operation(s) for storage-account-controller.
  name: Continuous Delivery Foundation Storage Account Controller API
  slug: continuous-delivery-foundation-storage-account-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The strategy-config-controller API from Continuous Delivery Foundation — 2 operation(s) for strategy-config-controller.
  name: Continuous Delivery Foundation Strategy Config Controller API
  slug: continuous-delivery-foundation-strategy-config-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The strategy-controller API from Continuous Delivery Foundation — 4 operation(s) for strategy-controller.
  name: Continuous Delivery Foundation Strategy Controller API
  slug: continuous-delivery-foundation-strategy-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The subnet-controller API from Continuous Delivery Foundation — 1 operation(s) for subnet-controller.
  name: Continuous Delivery Foundation Subnet Controller API
  slug: continuous-delivery-foundation-subnet-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The task-controller API from Continuous Delivery Foundation — 5 operation(s) for task-controller.
  name: Continuous Delivery Foundation Task Controller API
  slug: continuous-delivery-foundation-task-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The test-controller API from Continuous Delivery Foundation — 2 operation(s) for test-controller.
  name: Continuous Delivery Foundation Test Controller API
  slug: continuous-delivery-foundation-test-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The v-2-canary-config-controller API from Continuous Delivery Foundation — 2 operation(s) for v-2-canary-config-controller.
  name: Continuous Delivery Foundation V 2 Canary Config Controller API
  slug: continuous-delivery-foundation-v-2-canary-config-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The v-2-canary-controller API from Continuous Delivery Foundation — 9 operation(s) for v-2-canary-controller.
  name: Continuous Delivery Foundation V 2 Canary Controller API
  slug: continuous-delivery-foundation-v-2-canary-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The v-2-pipeline-templates-controller API from Continuous Delivery Foundation — 7 operation(s) for v-2-pipeline-templates-controller.
  name: Continuous Delivery Foundation V 2 Pipeline Templates Controller API
  slug: continuous-delivery-foundation-v-2-pipeline-templates-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The v4 API from Continuous Delivery Foundation — 119 operation(s) for v4.
  name: Continuous Delivery Foundation V4 API
  slug: continuous-delivery-foundation-v4-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The version-controller API from Continuous Delivery Foundation — 1 operation(s) for version-controller.
  name: Continuous Delivery Foundation Version Controller API
  slug: continuous-delivery-foundation-version-controller-api
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: The webhook-controller API from Continuous Delivery Foundation — 3 operation(s) for webhook-controller.
  name: Continuous Delivery Foundation Webhook Controller API
  slug: continuous-delivery-foundation-webhook-controller-api
artifact_total: 86
asyncapis:
- description: ''
  name: Continuous Delivery Foundation Cdevents Events
  slug: continuous-delivery-foundation-cdevents-events
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/overlays/continuous-delivery-foundation-jenkins-pipeline-graph-view-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/continuous-delivery-foundation-jenkins-pipeline-graph-view-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/overlays/continuous-delivery-foundation-spinnaker-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/continuous-delivery-foundation-spinnaker-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/overlays/continuous-delivery-foundation-screwdriver-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/continuous-delivery-foundation-screwdriver-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/overlays/continuous-delivery-foundation-jayex-jx-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/continuous-delivery-foundation-jayex-jx-api-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/security/continuous-delivery-foundation-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/continuous-delivery-foundation-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/authentication/continuous-delivery-foundation-authentication.yml
  title: ''
  type: Authentication
  url: authentication/continuous-delivery-foundation-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/security/continuous-delivery-foundation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/continuous-delivery-foundation-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cdeliveryfdn
- group: company
  title: ''
  type: Website
  url: https://cd.foundation/
- group: other
  title: ''
  type: Projects
  url: https://cd.foundation/projects/
- group: docs
  title: ''
  type: Documentation
  url: https://cd.foundation/projects/
- group: company
  title: ''
  type: Blog
  url: https://cd.foundation/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://cd.foundation/news/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/cdfoundation
- group: operate
  title: ''
  type: Community
  url: https://cd.foundation/community/
- group: other
  title: ''
  type: Events
  url: https://cd.foundation/events/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/well-known/continuous-delivery-foundation-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/continuous-delivery-foundation-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/well-known/continuous-delivery-foundation-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/continuous-delivery-foundation-api-catalog.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/well-known/continuous-delivery-foundation-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/continuous-delivery-foundation-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.jenkins.io/security/reporting/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/llms/continuous-delivery-foundation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/continuous-delivery-foundation-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/mcp/continuous-delivery-foundation-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/continuous-delivery-foundation-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/mcp/continuous-delivery-foundation-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/continuous-delivery-foundation-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/packages/continuous-delivery-foundation-packages.yml
  title: ''
  type: Packages
  url: packages/continuous-delivery-foundation-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/packages/continuous-delivery-foundation-packages.yml
  title: ''
  type: SDKs
  url: packages/continuous-delivery-foundation-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/cli/continuous-delivery-foundation-cli.yml
  title: ''
  type: CLI
  url: cli/continuous-delivery-foundation-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/conformance/continuous-delivery-foundation-conformance.yml
  title: ''
  type: Conformance
  url: conformance/continuous-delivery-foundation-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/errors/continuous-delivery-foundation-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/continuous-delivery-foundation-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/lifecycle/continuous-delivery-foundation-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/continuous-delivery-foundation-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jenkins.io/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/conventions/continuous-delivery-foundation-conventions.yml
  title: ''
  type: Conventions
  url: conventions/continuous-delivery-foundation-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/changelog/continuous-delivery-foundation-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/continuous-delivery-foundation-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/data-model/continuous-delivery-foundation-data-model.yml
  title: ''
  type: DataModel
  url: data-model/continuous-delivery-foundation-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/asyncapi/continuous-delivery-foundation-cdevents-events.yml
  title: ''
  type: Webhooks
  url: asyncapi/continuous-delivery-foundation-cdevents-events.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/json-schema/continuous-delivery-foundation-cdevents-schemas.yml
  title: ''
  type: JSONSchema
  url: json-schema/continuous-delivery-foundation-cdevents-schemas.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/plans/continuous-delivery-foundation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/continuous-delivery-foundation-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/rate-limits/continuous-delivery-foundation-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/continuous-delivery-foundation-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/finops/continuous-delivery-foundation-finops.yml
  title: ''
  type: FinOps
  url: finops/continuous-delivery-foundation-finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linuxfoundation.org/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linuxfoundation.org/legal/privacy-policy
- group: learn
  title: ''
  type: Training
  url: https://cd.foundation/training/
- group: company
  title: ''
  type: Newsletter
  url: https://cd.foundation/newsletter/
created: '2026-03-16'
description: The Continuous Delivery Foundation (CDF) is a Linux Foundation project that hosts vendor-neutral open source projects for continuous integration, continuous delivery, and DevOps. It is the home of CDEvents, Jenkins, Spinnaker, Screwdriver, Ortelius, JayeX, and was previously the home of Tekton (now a CNCF graduated project) and other CD-focused tooling.
finops:
- name: Continuous Delivery Foundation Finops
  service_category: API
  slug: continuous-delivery-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/continuous-delivery-foundation.png
layout: provider
mcp_servers:
- description: ''
  name: Continuous Delivery Foundation MCP Server
  slug: continuous-delivery-foundation-mcp-server
modified: '2026-09-05'
name: Continuous Delivery Foundation
nav: Providers
network: true
overview: 'Continuous Delivery Foundation publishes 74 APIs on the [APIs.io](https://apis.io/) network, including Admin Controller API, Amazon Infrastructure Controller API, API Extension Controller API, and 71 more. Tagged areas include Automation, CI/CD, DevOps, Linux Foundation, and Open-Source.


  The Continuous Delivery Foundation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Continuous Delivery Foundation''s developer surface includes authentication, documentation, engineering blog, CLI, changelog, training material, and 37 more developer resources.'
plans:
- name: Continuous Delivery Foundation Plans Pricing
  plan_count: 0
  slug: continuous-delivery-foundation-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Continuous Delivery Foundation Rate Limits
  slug: continuous-delivery-foundation-rate-limits
score:
  band: developing
  composite: 51.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.0
    catalog_earned_first_party: 6.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 58.9
    developer_ergonomics: 61.3
    discoverability: 66.7
    operational_transparency: 55.3
  previous_composite: 53.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 74
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/screenshots/continuous-delivery-foundation-2026-06-20T174948.png
security:
- kind: authentication
  name: Continuous Delivery Foundation Authentication
  slug: continuous-delivery-foundation-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Continuous Delivery Foundation Domain Security
  slug: continuous-delivery-foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Continuous Delivery Foundation Vulnerability Disclosure
  slug: continuous-delivery-foundation-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: continuous-delivery-foundation
tags:
- Automation
- CI/CD
- DevOps
- Linux Foundation
- Open-Source
website: https://cd.foundation/
---
