---
access_model:
  confidence: medium
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 129
  human_in_the_loop: 7
  name: Portainer Agentic Access
  operation_count: 240
  slug: portainer-agentic-access
  summary_line: 240 operations · 129 acting · 7 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Authenticate against Portainer HTTP API
  name: Portainer Auth API
  slug: portainer-auth-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage backups
  name: Portainer Backup API
  slug: portainer-backup-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Custom Templates
  name: Portainer Custom Templates API
  slug: portainer-custom-templates-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Docker resources
  name: Portainer Docker API
  slug: portainer-docker-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Edge related environment(endpoint) settings
  name: Portainer Edge API
  slug: portainer-edge-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Edge Groups
  name: Portainer Edge Groups API
  slug: portainer-edge-groups-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Edge Jobs
  name: Portainer Edge Jobs API
  slug: portainer-edge-jobs-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Edge Stacks
  name: Portainer Edge Stacks API
  slug: portainer-edge-stacks-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage environment(endpoint) groups
  name: Portainer Endpoint Groups API
  slug: portainer-endpoint-groups-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Docker environments(endpoints)
  name: Portainer Endpoints API
  slug: portainer-endpoints-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Helm charts
  name: Portainer Helm API
  slug: portainer-helm-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Intel AMT settings
  name: Portainer Intel API
  slug: portainer-intel-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Kubernetes cluster
  name: Portainer Kubernetes API
  slug: portainer-kubernetes-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage LDAP settings
  name: Portainer Ldap API
  slug: portainer-ldap-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Fetch the message of the day
  name: Portainer Motd API
  slug: portainer-motd-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Docker registries
  name: Portainer Registries API
  slug: portainer-registries-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage access control on Docker resources
  name: Portainer Resource Controls API
  slug: portainer-resource-controls-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage roles
  name: Portainer Roles API
  slug: portainer-roles-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Portainer settings
  name: Portainer Settings API
  slug: portainer-settings-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage ssl settings
  name: Portainer Ssl API
  slug: portainer-ssl-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage stacks
  name: Portainer Stacks API
  slug: portainer-stacks-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Information about the Portainer instance
  name: Portainer Status API
  slug: portainer-status-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage Portainer system
  name: Portainer System API
  slug: portainer-system-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage tags
  name: Portainer Tags API
  slug: portainer-tags-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage team memberships
  name: Portainer Team Memberships API
  slug: portainer-team-memberships-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage teams
  name: Portainer Teams API
  slug: portainer-teams-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage App Templates
  name: Portainer Templates API
  slug: portainer-templates-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Upload files
  name: Portainer Upload API
  slug: portainer-upload-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage users
  name: Portainer Users API
  slug: portainer-users-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Manage webhooks
  name: Portainer Webhooks API
  slug: portainer-webhooks-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Create exec sessions using websockets
  name: Portainer Websocket API
  slug: portainer-websocket-api
- baseURL: https://api-docs.portainer.io
  baseurl_source: declared
  description: Operate git repository
  name: Portainer Git Ops API
  slug: portainer-git-ops-api
artifact_total: 174
collections:
- collection_type: open
  name: PortainerCE auth API
  slug: open-portainer-auth-api
- collection_type: open
  name: PortainerCE auth backup API
  slug: open-portainer-backup-api
- collection_type: open
  name: PortainerCE auth custom_templates API
  slug: open-portainer-custom-templates-api
- collection_type: open
  name: PortainerCE auth docker API
  slug: open-portainer-docker-api
- collection_type: open
  name: PortainerCE auth edge API
  slug: open-portainer-edge-api
- collection_type: open
  name: PortainerCE auth edge_groups API
  slug: open-portainer-edge-groups-api
- collection_type: open
  name: PortainerCE auth edge_jobs API
  slug: open-portainer-edge-jobs-api
- collection_type: open
  name: PortainerCE auth edge_stacks API
  slug: open-portainer-edge-stacks-api
- collection_type: open
  name: PortainerCE auth endpoint_groups API
  slug: open-portainer-endpoint-groups-api
- collection_type: open
  name: PortainerCE auth endpoints API
  slug: open-portainer-endpoints-api
- collection_type: open
  name: PortainerCE auth gitops API
  slug: open-portainer-gitops-api
- collection_type: open
  name: PortainerCE auth helm API
  slug: open-portainer-helm-api
- collection_type: open
  name: PortainerCE auth intel API
  slug: open-portainer-intel-api
- collection_type: open
  name: PortainerCE auth kubernetes API
  slug: open-portainer-kubernetes-api
- collection_type: open
  name: PortainerCE auth ldap API
  slug: open-portainer-ldap-api
- collection_type: open
  name: PortainerCE auth motd API
  slug: open-portainer-motd-api
- collection_type: open
  name: PortainerCE auth registries API
  slug: open-portainer-registries-api
- collection_type: open
  name: PortainerCE auth resource_controls API
  slug: open-portainer-resource-controls-api
- collection_type: open
  name: PortainerCE auth roles API
  slug: open-portainer-roles-api
- collection_type: open
  name: PortainerCE auth settings API
  slug: open-portainer-settings-api
- collection_type: open
  name: PortainerCE auth ssl API
  slug: open-portainer-ssl-api
- collection_type: open
  name: PortainerCE auth stacks API
  slug: open-portainer-stacks-api
- collection_type: open
  name: PortainerCE auth status API
  slug: open-portainer-status-api
- collection_type: open
  name: PortainerCE auth system API
  slug: open-portainer-system-api
- collection_type: open
  name: PortainerCE auth tags API
  slug: open-portainer-tags-api
- collection_type: open
  name: PortainerCE auth team_memberships API
  slug: open-portainer-team-memberships-api
- collection_type: open
  name: PortainerCE auth teams API
  slug: open-portainer-teams-api
- collection_type: open
  name: PortainerCE auth templates API
  slug: open-portainer-templates-api
- collection_type: open
  name: PortainerCE auth upload API
  slug: open-portainer-upload-api
- collection_type: open
  name: PortainerCE auth users API
  slug: open-portainer-users-api
- collection_type: open
  name: PortainerCE auth webhooks API
  slug: open-portainer-webhooks-api
- collection_type: open
  name: PortainerCE auth websocket API
  slug: open-portainer-websocket-api
- collection_type: open
  name: PortainerCE API
  slug: open-portainer
common:
- group: other
  href: https://artifacts.apis.io/portainer/capabilities/portainer-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/portainer-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/portainer/mcp/portainer-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/portainer-mcp.yml
- group: commercial
  href: https://artifacts.apis.io/portainer/finops/portainer-finops.yml
  title: ''
  type: FinOps
  url: finops/portainer-finops.yml
- group: operate
  href: https://artifacts.apis.io/portainer/rate-limits/portainer-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/portainer-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/portainer/plans/portainer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/portainer-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/portainer/rules/portainer-rules.yml
  title: ''
  type: Spectral
  url: rules/portainer-rules.yml
- group: design
  href: https://artifacts.apis.io/portainer/json-ld/portainer-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/portainer-context.jsonld
- group: design
  href: https://artifacts.apis.io/portainer/vocabulary/portainer-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/portainer-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/portainer/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/portainer/data-model/portainer-data-model.yml
  title: ''
  type: DataModel
  url: data-model/portainer-data-model.yml
- group: design
  href: https://artifacts.apis.io/portainer/errors/portainer-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/portainer-problem-types.yml
- group: design
  href: https://artifacts.apis.io/portainer/conformance/portainer-conformance.yml
  title: ''
  type: Conformance
  url: conformance/portainer-conformance.yml
- group: agent
  href: https://artifacts.apis.io/portainer/llms/portainer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/portainer-llms.txt
- group: agent
  href: https://artifacts.apis.io/portainer/well-known/portainer-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/portainer-well-known.yml
- group: other
  href: https://artifacts.apis.io/portainer/hosts/portainer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/portainer-hosts.yml
- group: other
  href: https://artifacts.apis.io/portainer/vendors/portainer-vendors.yml
  title: ''
  type: Vendors
  url: vendors/portainer-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.portainer.io/terms-and-license-agreements
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.portainer.io/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.portainer.io/start/install/server/setup
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/portainer/portainer/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/portainer/portainer/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/portainer/portainer/blob/develop/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/portainer/portainer/blob/develop/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/portainer/portainer/blob/develop/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/portainer/portainer/blob/develop/LICENSE
- group: agent
  href: https://artifacts.apis.io/portainer/agentic-access/portainer-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/portainer-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/portainer/security/portainer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/portainer-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/portainer/authentication/portainer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/portainer-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/portainer
- group: company
  title: ''
  type: Website
  url: https://www.portainer.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.portainer.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.portainer.io/
- group: company
  title: ''
  type: Blog
  url: https://www.portainer.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.portainer.io/pricing
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/portainer
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/portainer/portainer
- group: operate
  title: ''
  type: Community
  url: https://www.portainer.io/community
- group: operate
  title: ''
  type: Slack
  url: https://www.portainer.io/slack
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.portainer.io/llms.txt
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI/AsyncAPI/GraphQL spec found at known endpoints (e.g., https://api.portainer.io/openapi.json returned empty).
  evidence:
  - status: 200
    url: https://api.portainer.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-03-26'
description: Portainer provides a centralized multi‑cluster management platform for Kubernetes, Docker, Swarm and Podman workloads. It offers enterprise identity and access features such as SSO, LDAP and OIDC, as well as GitOps deployment workflows and self‑service guardrails. The product is aimed at engineering teams and enterprises that need to govern containerized applications across on‑premises, cloud and edge environments from a single console.
finops:
- has_sources: true
  method: derived
  name: Portainer Finops
  primary_unit: node tier (5, 10, or 15 nodes)
  service_category: ''
  slug: portainer-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/portainer.png
json_schemas:
- name: auth.authenticatePayload
  property_count: 2
  slug: portainer-auth-authenticate-payload
- name: auth.authenticateResponse
  property_count: 1
  slug: portainer-auth-authenticate-response
- name: auth.oauthPayload
  property_count: 1
  slug: portainer-auth-oauth-payload
- name: backup.backupPayload
  property_count: 1
  slug: portainer-backup-backup-payload
- name: backup.restorePayload
  property_count: 3
  slug: portainer-backup-restore-payload
- name: containers.containerGpusResponse
  property_count: 1
  slug: portainer-containers-container-gpus-response
- name: customtemplates.customTemplateFromFileContentPayload
  property_count: 9
  slug: portainer-customtemplates-custom-template-from-file-content-payload
- name: customtemplates.customTemplateFromGitRepositoryPayload
  property_count: 16
  slug: portainer-customtemplates-custom-template-from-git-repository-payload
- name: customtemplates.customTemplateUpdatePayload
  property_count: 19
  slug: portainer-customtemplates-custom-template-update-payload
- name: customtemplates.fileResponse
  property_count: 1
  slug: portainer-customtemplates-file-response
- name: docker.dashboardResponse
  property_count: 6
  slug: portainer-docker-dashboard-response
- name: edge.StackPayload
  property_count: 24
  slug: portainer-edge-stack-payload
- name: edgegroups.decoratedEdgeGroup
  property_count: 11
  slug: portainer-edgegroups-decorated-edge-group
- name: edgegroups.edgeGroupCreatePayload
  property_count: 5
  slug: portainer-edgegroups-edge-group-create-payload
- name: edgegroups.edgeGroupUpdatePayload
  property_count: 5
  slug: portainer-edgegroups-edge-group-update-payload
- name: edgejobs.edgeJobCreateFromFileContentPayload
  property_count: 6
  slug: portainer-edgejobs-edge-job-create-from-file-content-payload
- name: edgejobs.edgeJobFileResponse
  property_count: 1
  slug: portainer-edgejobs-edge-job-file-response
- name: edgejobs.edgeJobUpdatePayload
  property_count: 6
  slug: portainer-edgejobs-edge-job-update-payload
- name: edgejobs.taskContainer
  property_count: 4
  slug: portainer-edgejobs-task-container
- name: edgestacks.edgeStackFromGitRepositoryPayload
  property_count: 13
  slug: portainer-edgestacks-edge-stack-from-git-repository-payload
- name: edgestacks.edgeStackFromStringPayload
  property_count: 6
  slug: portainer-edgestacks-edge-stack-from-string-payload
- name: edgestacks.updateEdgeStackPayload
  property_count: 5
  slug: portainer-edgestacks-update-edge-stack-payload
- name: edgestacks.updateStatusPayload
  property_count: 5
  slug: portainer-edgestacks-update-status-payload
- name: endpointedge.endpointEdgeStatusInspectResponse
  property_count: 6
  slug: portainer-endpointedge-endpoint-edge-status-inspect-response
- name: endpointgroups.endpointGroupCreatePayload
  property_count: 4
  slug: portainer-endpointgroups-endpoint-group-create-payload
- name: endpointgroups.endpointGroupUpdatePayload
  property_count: 6
  slug: portainer-endpointgroups-endpoint-group-update-payload
- name: endpoints.endpointSettingsUpdatePayload
  property_count: 11
  slug: portainer-endpoints-endpoint-settings-update-payload
- name: endpoints.endpointUpdatePayload
  property_count: 17
  slug: portainer-endpoints-endpoint-update-payload
- name: github_com_portainer_portainer_pkg_libhelm_release.Release
  property_count: 12
  slug: portainer-github-com-portainer-portainer-pkg-libhelm-release-release
- name: gitops.fileResponse
  property_count: 1
  slug: portainer-gitops-file-response
- name: gitops.repositoryFilePreviewPayload
  property_count: 7
  slug: portainer-gitops-repository-file-preview-payload
- name: helm.installChartPayload
  property_count: 7
  slug: portainer-helm-install-chart-payload
- name: images.ImageResponse
  property_count: 6
  slug: portainer-images-image-response
- name: kubernetes.K8sApplication
  property_count: 31
  slug: portainer-kubernetes-k8s-application
- name: kubernetes.K8sServiceInfo
  property_count: 15
  slug: portainer-kubernetes-k8s-service-info
- name: ldap.checkPayload
  property_count: 1
  slug: portainer-ldap-check-payload
- name: motd.motdResponse
  property_count: 5
  slug: portainer-motd-motd-response
- name: openamt.deviceActionPayload
  property_count: 1
  slug: portainer-openamt-device-action-payload
- name: openamt.deviceFeaturesPayload
  property_count: 1
  slug: portainer-openamt-device-features-payload
- name: openamt.openAMTConfigurePayload
  property_count: 8
  slug: portainer-openamt-open-amtconfigure-payload
- name: portainer.APIKey
  property_count: 7
  slug: portainer-portainer-apikey
- name: portainer.CustomTemplate
  property_count: 15
  slug: portainer-portainer-custom-template
- name: portainer.EdgeGroup
  property_count: 7
  slug: portainer-portainer-edge-group
- name: portainer.EdgeJob
  property_count: 10
  slug: portainer-portainer-edge-job
- name: portainer.EdgeStack
  property_count: 14
  slug: portainer-portainer-edge-stack
- name: portainer.EndpointGroup
  property_count: 10
  slug: portainer-portainer-endpoint-group
- name: portainer.Endpoint
  property_count: 37
  slug: portainer-portainer-endpoint
- name: portainer.HelmUserRepository
  property_count: 3
  slug: portainer-portainer-helm-user-repository
- name: portainer.Registry
  property_count: 20
  slug: portainer-portainer-registry
- name: portainer.ResourceControl
  property_count: 11
  slug: portainer-portainer-resource-control
- name: portainer.Role
  property_count: 5
  slug: portainer-portainer-role
- name: portainer.Settings
  property_count: 33
  slug: portainer-portainer-settings
- name: portainer.SSLSettings
  property_count: 4
  slug: portainer-portainer-sslsettings
- name: portainer.Stack
  property_count: 20
  slug: portainer-portainer-stack
- name: portainer.Tag
  property_count: 4
  slug: portainer-portainer-tag
- name: portainer.TeamMembership
  property_count: 4
  slug: portainer-portainer-team-membership
- name: portainer.Team
  property_count: 2
  slug: portainer-portainer-team
- name: portainer.User
  property_count: 9
  slug: portainer-portainer-user
- name: portainer.Webhook
  property_count: 6
  slug: portainer-portainer-webhook
- name: registries.registryConfigurePayload
  property_count: 9
  slug: portainer-registries-registry-configure-payload
- name: registries.registryCreatePayload
  property_count: 11
  slug: portainer-registries-registry-create-payload
- name: registries.registryPingPayload
  property_count: 5
  slug: portainer-registries-registry-ping-payload
- name: registries.registryPingResponse
  property_count: 2
  slug: portainer-registries-registry-ping-response
- name: registries.registryUpdatePayload
  property_count: 9
  slug: portainer-registries-registry-update-payload
- name: release.ReleaseElement
  property_count: 7
  slug: portainer-release-release-element
- name: resourcecontrols.resourceControlCreatePayload
  property_count: 7
  slug: portainer-resourcecontrols-resource-control-create-payload
- name: settings.publicSettingsResponse
  property_count: 13
  slug: portainer-settings-public-settings-response
- name: settings.settingsUpdatePayload
  property_count: 18
  slug: portainer-settings-settings-update-payload
- name: ssl.sslUpdatePayload
  property_count: 3
  slug: portainer-ssl-ssl-update-payload
- name: stacks.composeStackFromGitRepositoryPayload
  property_count: 12
  slug: portainer-stacks-compose-stack-from-git-repository-payload
- name: stacks.stackGitRedployPayload
  property_count: 10
  slug: portainer-stacks-stack-git-redploy-payload
- name: stacks.swarmStackFromFileContentPayload
  property_count: 5
  slug: portainer-stacks-swarm-stack-from-file-content-payload
- name: stacks.swarmStackFromGitRepositoryPayload
  property_count: 13
  slug: portainer-stacks-swarm-stack-from-git-repository-payload
- name: stacks.updateSwarmStackPayload
  property_count: 5
  slug: portainer-stacks-update-swarm-stack-payload
- name: system.nodesCountResponse
  property_count: 1
  slug: portainer-system-nodes-count-response
- name: system.status
  property_count: 2
  slug: portainer-system-status
- name: system.systemInfoResponse
  property_count: 3
  slug: portainer-system-system-info-response
- name: system.versionResponse
  property_count: 9
  slug: portainer-system-version-response
- name: tags.tagCreatePayload
  property_count: 1
  slug: portainer-tags-tag-create-payload
- name: teammemberships.teamMembershipCreatePayload
  property_count: 3
  slug: portainer-teammemberships-team-membership-create-payload
- name: teammemberships.teamMembershipUpdatePayload
  property_count: 3
  slug: portainer-teammemberships-team-membership-update-payload
- name: teams.teamCreatePayload
  property_count: 2
  slug: portainer-teams-team-create-payload
- name: teams.teamUpdatePayload
  property_count: 1
  slug: portainer-teams-team-update-payload
- name: templates.fileResponse
  property_count: 1
  slug: portainer-templates-file-response
- name: templates.listResponse
  property_count: 2
  slug: portainer-templates-list-response
- name: users.addHelmRepoUrlPayload
  property_count: 1
  slug: portainer-users-add-helm-repo-url-payload
- name: users.adminInitPayload
  property_count: 2
  slug: portainer-users-admin-init-payload
- name: users.helmUserRepositoryResponse
  property_count: 2
  slug: portainer-users-helm-user-repository-response
- name: users.userCreatePayload
  property_count: 3
  slug: portainer-users-user-create-payload
- name: users.userUpdatePayload
  property_count: 6
  slug: portainer-users-user-update-payload
- name: v1beta1.NodeMetricsList
  property_count: 4
  slug: portainer-v1beta1-node-metrics-list
- name: v1beta1.NodeMetrics
  property_count: 6
  slug: portainer-v1beta1-node-metrics
- name: v1beta1.PodMetricsList
  property_count: 4
  slug: portainer-v1beta1-pod-metrics-list
- name: v1beta1.PodMetrics
  property_count: 6
  slug: portainer-v1beta1-pod-metrics
- name: webhooks.webhookCreatePayload
  property_count: 4
  slug: portainer-webhooks-webhook-create-payload
- name: webhooks.webhookUpdatePayload
  property_count: 1
  slug: portainer-webhooks-webhook-update-payload
jsonld:
- class_count: 120
  name: Portainer Context
  property_count: 350
  slug: portainer-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.portainer.io over HTTP.
  name: Portainer Documentation MCP Server — GitBook-hosted remote https://docs.portainer.io/~gitbook/mcp
  slug: portainer
modified: '2026-05-19'
name: Portainer
nav: Providers
network: true
overview: 'Portainer publishes 32 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Backup API, Custom Templates API, and 29 more. Tagged areas include Container Management, Containers, Docker, Kubernetes, and Kubernetes Management.


  The Portainer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Portainer''s developer surface includes getting-started guide, authentication, documentation, API reference, engineering blog, pricing, and 33 more developer resources.'
plans:
- name: Portainer Plans Pricing
  plan_count: 4
  slug: portainer-plans-pricing
- name: Portainer Price Estimates
  plan_count: 0
  slug: portainer-price-estimates
random_paper: 20
rate_limits:
- limit_count: 5
  name: Portainer Rate Limits
  slug: portainer-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Portainer API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 4
    warn: 2
  slug: portainer-rules
score:
  band: strong
  composite: 56.0
  coverage:
    artifact_dirs: 31
    catalog_earned: 80.8
    catalog_earned_first_party: 12.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 62.4
    developer_ergonomics: 39.9
    discoverability: 75.0
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 58.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 32
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/portainer/portainer-2026-06-20T191931.png
security:
- kind: authentication
  name: Portainer Authentication
  slug: portainer-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Portainer Domain Security
  slug: portainer-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 3
skills:
- name: portainer-create-user-with-api-key
  slug: portainer-create-user-with-api-key
- name: portainer-team-create-and-inspect
  slug: portainer-team-create-and-inspect
- name: portainer-webhooks-manage
  slug: portainer-webhooks-manage
slug: portainer
tags:
- Container Management
- Containers
- Docker
- Kubernetes
- Kubernetes Management
- Enterprise Identity
- GitOps
website: https://www.portainer.io/
---
