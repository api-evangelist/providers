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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.3
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 414
  human_in_the_loop: 3
  name: Canonical Agentic Access
  operation_count: 812
  slug: canonical-agentic-access
  summary_line: 812 operations · 414 acting · 3 human-in-the-loop
api_count: 13
apis:
- description: The public Snap Store Device API (api.snapcraft.io) serves information about snaps, revisions, channels, tracks, assertions, and refresh state to snap clients. The Snapcraft Dashboard API (dashboard.s
  name: Snap Store API
  slug: snap-store-api
- description: Developer-facing REST API for Charmhub, Canonical's marketplace for charms (Kubernetes and machine operators). Supports charm discovery, publishing, release channels, and token exchange — macaroons is
  name: Charmhub API
  slug: charmhub-api
- description: The RESTful API for MAAS (Metal as a Service). Everything the MAAS UI can do — commissioning, allocation, deployment, DHCP/DNS, tags, zones, pools, users, machines — is available through the API, maki
  name: MAAS API
  slug: maas-api
- description: Juju is Canonical's open-source orchestration engine for deploying, integrating, scaling, and managing applications on clouds, MAAS, LXD, and Kubernetes via charms. Juju clients communicate with a con
  name: Juju Client / Controller API
  slug: juju-api
- description: Launchpad exposes a RESTful Web Services API over its project hosting, bug tracking, code, builds, translations, and distribution data. The API is authenticated with OAuth; anonymous access gives read
  name: Launchpad Web Services API
  slug: launchpad-api
- description: The Ubuntu Pro client exposes a local API/CLI for managing Ubuntu Pro subscription services on a host — enabling, disabling, and inspecting Extended Security Maintenance (ESM), Livepatch, FIPS, compli
  name: Ubuntu Pro Client API
  slug: ubuntu-pro-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Assertions API from Canonical — 1 operation(s) for assertions.
  name: Canonical Assertions API
  slug: canonical-assertions-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Search API from Canonical — 1 operation(s) for search.
  name: Canonical Search API
  slug: canonical-search-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Snaps API from Canonical — 10 operation(s) for snaps.
  name: Canonical Snaps API
  slug: canonical-snaps-api
- description: MicroCeph is Canonical's opinionated, snap-delivered Ceph distribution. It publishes a small OpenAPI 3.1.0 contract for its cluster REST surface. Recorded here because it is a real published first-par
  name: MicroCeph REST API
  slug: microceph-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The AppAuthorizationService API from Canonical — 3 operation(s) for appauthorizationservice.
  name: Canonical App Authorization Service API
  slug: canonical-appauthorizationservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The application API from Canonical — 1 operation(s) for application.
  name: Canonical Application API
  slug: canonical-application-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The applications API from Canonical — 20 operation(s) for applications.
  name: Canonical Applications API
  slug: canonical-applications-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Apps API from Canonical — 2 operation(s) for apps.
  name: Canonical Apps API
  slug: canonical-apps-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The artefact-builds API from Canonical — 1 operation(s) for artefact-builds.
  name: Canonical Artefact Builds API
  slug: canonical-artefact-builds-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The artefact-matching-rules API from Canonical — 2 operation(s) for artefact-matching-rules.
  name: Canonical Artefact Matching Rules API
  slug: canonical-artefact-matching-rules-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The artefacts API from Canonical — 8 operation(s) for artefacts.
  name: Canonical Artefacts API
  slug: canonical-artefacts-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: Return the reference to a change that will occur in the background.
  name: Canonical Asynchronous API
  slug: canonical-asynchronous-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The auth_groups API from Canonical — 3 operation(s) for auth_groups.
  name: Canonical Auth Groups API
  slug: canonical-auth-groups-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The authentication API from Canonical — 4 operation(s) for authentication.
  name: Canonical Authentication API
  slug: canonical-authentication-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: Access is restricted to the root user.
  name: Canonical Authentication Required API
  slug: canonical-authenticationrequired-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The AuthzGroupsService API from Canonical — 5 operation(s) for authzgroupsservice.
  name: Canonical Authz Groups Service API
  slug: canonical-authzgroupsservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The certificates API from Canonical — 4 operation(s) for certificates.
  name: Canonical Certificates API
  slug: canonical-certificates-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The certification API from Canonical — 1 operation(s) for certification.
  name: Canonical Certification API
  slug: canonical-certification-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The changes and tasks API from Canonical — 4 operation(s) for changes and tasks.
  name: Canonical changes and tasks API
  slug: canonical-changes-and-tasks-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The checks API from Canonical — 2 operation(s) for checks.
  name: Canonical Checks API
  slug: canonical-checks-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The ClientsService API from Canonical — 2 operation(s) for clientsservice.
  name: Canonical Clients Service API
  slug: canonical-clientsservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The cluster API from Canonical — 7 operation(s) for cluster.
  name: Canonical Cluster API
  slug: canonical-cluster-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The cluster-groups API from Canonical — 3 operation(s) for cluster-groups.
  name: Canonical Cluster Groups API
  slug: canonical-cluster-groups-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The cluster-links API from Canonical — 4 operation(s) for cluster-links.
  name: Canonical Cluster Links API
  slug: canonical-cluster-links-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The config API from Canonical — 1 operation(s) for config.
  name: Canonical Config API
  slug: canonical-config-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The containers API from Canonical — 6 operation(s) for containers.
  name: Canonical Containers API
  slug: canonical-containers-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The devices API from Canonical — 3 operation(s) for devices.
  name: Canonical Devices API
  slug: canonical-devices-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The environment-reviews API from Canonical — 2 operation(s) for environment-reviews.
  name: Canonical Environment Reviews API
  slug: canonical-environment-reviews-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The environments API from Canonical — 3 operation(s) for environments.
  name: Canonical Environments API
  slug: canonical-environments-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The events API from Canonical — 1 operation(s) for events.
  name: Canonical Events API
  slug: canonical-events-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The exec API from Canonical — 1 operation(s) for exec.
  name: Canonical Exec API
  slug: canonical-exec-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The execution-metadata API from Canonical — 1 operation(s) for execution-metadata.
  name: Canonical Execution Metadata API
  slug: canonical-execution-metadata-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: Interact with experimental features.
  name: Canonical Experimental API
  slug: canonical-experimental-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The files API from Canonical — 1 operation(s) for files.
  name: Canonical Files API
  slug: canonical-files-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The GroupsService API from Canonical — 8 operation(s) for groupsservice.
  name: Canonical Groups Service API
  slug: canonical-groupsservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Hardware API (hwapi) API from Canonical — 1 operation(s) for hardware api (hwapi).
  name: Canonical Hardware API (hwapi) API
  slug: canonical-hardware-api-hwapi-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The health API from Canonical — 4 operation(s) for health.
  name: Canonical Health API
  slug: canonical-health-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The identities API from Canonical — 15 operation(s) for identities.
  name: Canonical Identities API
  slug: canonical-identities-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The IdentitiesService API from Canonical — 2 operation(s) for identitiesservice.
  name: Canonical Identities Service API
  slug: canonical-identitiesservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The identity_provider_groups API from Canonical — 3 operation(s) for identity_provider_groups.
  name: Canonical Identity Provider Groups API
  slug: canonical-identity-provider-groups-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The IdpsService API from Canonical — 2 operation(s) for idpsservice.
  name: Canonical Idps Service API
  slug: canonical-idpsservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The images API from Canonical — 19 operation(s) for images.
  name: Canonical Images API
  slug: canonical-images-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The instances API from Canonical — 29 operation(s) for instances.
  name: Canonical Instances API
  slug: canonical-instances-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: Display and manage interactions between snaps.
  name: Canonical Interfaces API
  slug: canonical-interfaces-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The internal API from Canonical — 1 operation(s) for internal.
  name: Canonical Internal API
  slug: canonical-internal-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The issues API from Canonical — 6 operation(s) for issues.
  name: Canonical Issues API
  slug: canonical-issues-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The layers API from Canonical — 1 operation(s) for layers.
  name: Canonical Layers API
  slug: canonical-layers-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: Manages local repositories.
  name: Canonical Local Service API
  slug: canonical-localservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The logs API from Canonical — 1 operation(s) for logs.
  name: Canonical Logs API
  slug: canonical-logs-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Metadata API from Canonical — 1 operation(s) for metadata.
  name: Canonical Metadata API
  slug: canonical-metadata-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The metrics API from Canonical — 2 operation(s) for metrics.
  name: Canonical Metrics API
  slug: canonical-metrics-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The MetricsService API from Canonical — 1 operation(s) for metricsservice.
  name: Canonical Metrics Service API
  slug: canonical-metricsservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: Methods for managing repository mirrors.
  name: Canonical Mirror Service API
  slug: canonical-mirrorservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The network-acls API from Canonical — 4 operation(s) for network-acls.
  name: Canonical Network Acls API
  slug: canonical-network-acls-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The network-allocations API from Canonical — 1 operation(s) for network-allocations.
  name: Canonical Network Allocations API
  slug: canonical-network-allocations-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The network-forwards API from Canonical — 3 operation(s) for network-forwards.
  name: Canonical Network Forwards API
  slug: canonical-network-forwards-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The network-load-balancer-pools API from Canonical — 3 operation(s) for network-load-balancer-pools.
  name: Canonical Network Load Balancer Pools API
  slug: canonical-network-load-balancer-pools-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The network-load-balancers API from Canonical — 3 operation(s) for network-load-balancers.
  name: Canonical Network Load Balancers API
  slug: canonical-network-load-balancers-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The network-peers API from Canonical — 3 operation(s) for network-peers.
  name: Canonical Network Peers API
  slug: canonical-network-peers-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The network-zones API from Canonical — 6 operation(s) for network-zones.
  name: Canonical Network Zones API
  slug: canonical-network-zones-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The networks API from Canonical — 5 operation(s) for networks.
  name: Canonical Networks API
  slug: canonical-networks-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The nodes API from Canonical — 3 operation(s) for nodes.
  name: Canonical Nodes API
  slug: canonical-nodes-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The notices API from Canonical — 4 operation(s) for notices.
  name: Canonical Notices API
  slug: canonical-notices-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The notifications API from Canonical — 6 operation(s) for notifications.
  name: Canonical Notifications API
  slug: canonical-notifications-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Oidc_Api API from Canonical — 2 operation(s) for oidc_api.
  name: Canonical Oidc API
  slug: canonical-oidc-api-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The oidc_sessions API from Canonical — 3 operation(s) for oidc_sessions.
  name: Canonical Oidc Sessions API
  slug: canonical-oidc-sessions-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The operations API from Canonical — 10 operation(s) for operations.
  name: Canonical Operations API
  slug: canonical-operations-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: Manages long-running operations.
  name: Canonical Operation Service API
  slug: canonical-operationservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The permissions API from Canonical — 3 operation(s) for permissions.
  name: Canonical Permissions API
  slug: canonical-permissions-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The placement-groups API from Canonical — 3 operation(s) for placement-groups.
  name: Canonical Placement Groups API
  slug: canonical-placement-groups-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The plan API from Canonical — 1 operation(s) for plan.
  name: Canonical Plan API
  slug: canonical-plan-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The profiles API from Canonical — 3 operation(s) for profiles.
  name: Canonical Profiles API
  slug: canonical-profiles-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The projects API from Canonical — 4 operation(s) for projects.
  name: Canonical Projects API
  slug: canonical-projects-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: Manages the publication of Debian artifacts.
  name: Canonical Publication Service API
  slug: canonical-publicationservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: Manages the storage destinations for publishing Debian archives.
  name: Canonical Publication Target Service API
  slug: canonical-publicationtargetservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The region API from Canonical — 1 operation(s) for region.
  name: Canonical Region API
  slug: canonical-region-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The replicators API from Canonical — 4 operation(s) for replicators.
  name: Canonical Replicators API
  slug: canonical-replicators-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The reports API from Canonical — 2 operation(s) for reports.
  name: Canonical Reports API
  slug: canonical-reports-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The RolesService API from Canonical — 5 operation(s) for rolesservice.
  name: Canonical Roles Service API
  slug: canonical-rolesservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: Requires the user to authenticate with root access.
  name: Canonical Root API
  slug: canonical-root-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The schema API from Canonical — 1 operation(s) for schema.
  name: Canonical Schema API
  slug: canonical-schema-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The SchemasService API from Canonical — 3 operation(s) for schemasservice.
  name: Canonical Schemas Service API
  slug: canonical-schemasservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Security API from Canonical — 15 operation(s) for security.
  name: Canonical Security API
  slug: canonical-security-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Sentry Debug API from Canonical — 1 operation(s) for sentry debug.
  name: Canonical Sentry Debug API
  slug: canonical-sentry-debug-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The server API from Canonical — 5 operation(s) for server.
  name: Canonical Server API
  slug: canonical-server-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The service API from Canonical — 2 operation(s) for service.
  name: Canonical Service API
  slug: canonical-service-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The services API from Canonical — 1 operation(s) for services.
  name: Canonical Services API
  slug: canonical-services-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The session API from Canonical — 8 operation(s) for session.
  name: Canonical Session API
  slug: canonical-session-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The signals API from Canonical — 1 operation(s) for signals.
  name: Canonical Signals API
  slug: canonical-signals-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The status API from Canonical — 1 operation(s) for status.
  name: Canonical Status API
  slug: canonical-status-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The StatusService API from Canonical — 2 operation(s) for statusservice.
  name: Canonical Status Service API
  slug: canonical-statusservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The storage API from Canonical — 29 operation(s) for storage.
  name: Canonical Storage API
  slug: canonical-storage-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The system info API from Canonical — 1 operation(s) for system info.
  name: Canonical system info API
  slug: canonical-system-info-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The tasks API from Canonical — 1 operation(s) for tasks.
  name: Canonical Tasks API
  slug: canonical-tasks-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The teams API from Canonical — 3 operation(s) for teams.
  name: Canonical Teams API
  slug: canonical-teams-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The TenantService API from Canonical — 8 operation(s) for tenantservice.
  name: Canonical Tenant Service API
  slug: canonical-tenantservice-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The test-cases API from Canonical — 3 operation(s) for test-cases.
  name: Canonical Test Cases API
  slug: canonical-test-cases-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The test-executions API from Canonical — 10 operation(s) for test-executions.
  name: Canonical Test Executions API
  slug: canonical-test-executions-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Test Observer API from Canonical — 1 operation(s) for test observer.
  name: Canonical Test Observer API
  slug: canonical-test-observer-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The test-plans API from Canonical — 1 operation(s) for test-plans.
  name: Canonical Test Plans API
  slug: canonical-test-plans-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The test-results API from Canonical — 1 operation(s) for test-results.
  name: Canonical Test Results API
  slug: canonical-test-results-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The users API from Canonical — 3 operation(s) for users.
  name: Canonical Users API
  slug: canonical-users-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The V1 API from Canonical — 29 operation(s) for v1.
  name: Canonical V1 API
  slug: canonical-v1-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Version API from Canonical — 1 operation(s) for version.
  name: Canonical Version API
  slug: canonical-version-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The warnings API from Canonical — 3 operation(s) for warnings.
  name: Canonical Warnings API
  slug: canonical-warnings-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Add Ons API from Canonical — 4 operation(s) for add ons.
  name: Canonical Add Ons API
  slug: canonical-add-ons-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Authentication Service API from Canonical — 4 operation(s) for authentication service.
  name: Canonical Authentication Service API
  slug: canonical-authentication-service-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: Do not require the user to authenticate.
  name: Canonical Open Access API
  slug: canonical-open-access-api
artifact_total: 129
asyncapis:
- description: ''
  name: Canonical Launchpad Webhooks
  slug: canonical-launchpad-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Canonical Snap Store Device Assertions API
  slug: open-canonical-assertions-api
- collection_type: open
  name: Canonical Snap Store Device Assertions Search API
  slug: open-canonical-search-api
- collection_type: open
  name: Canonical Snap Store Device Assertions Snaps API
  slug: open-canonical-snaps-api
- collection_type: open
  name: Canonical Snap Store Device API
  slug: open-canonical
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/skills/canonical-snapd-manage-snap.md
  title: ''
  type: AgentSkill
  url: skills/canonical-snapd-manage-snap.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/overlays/canonical-lxd-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-lxd-rest-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/skills/canonical-lxd-provision-instance.md
  title: ''
  type: AgentSkill
  url: skills/canonical-lxd-provision-instance.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/overlays/canonical-ubuntu-security-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-ubuntu-security-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/skills/canonical-ubuntu-security-cve-lookup.md
  title: ''
  type: AgentSkill
  url: skills/canonical-ubuntu-security-cve-lookup.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/overlays/canonical-pebble-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-pebble-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/overlays/canonical-testflinger-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-testflinger-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/overlays/canonical-hardware-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-hardware-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/overlays/canonical-identity-platform-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-identity-platform-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/overlays/canonical-test-observer-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-test-observer-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/overlays/canonical-anbox-cloud-ams-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-anbox-cloud-ams-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/overlays/canonical-anbox-stream-gateway-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-anbox-stream-gateway-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/overlays/canonical-cos-registration-server-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-cos-registration-server-api-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/scopes/canonical-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/canonical-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/authentication/canonical-authentication.yml
  title: ''
  type: Authentication
  url: authentication/canonical-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/agentic-access/canonical-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/canonical-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/security/canonical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canonical-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/canonical
- group: company
  title: ''
  type: Website
  url: https://canonical.com/
- group: company
  title: ''
  type: UbuntuWebsite
  url: https://ubuntu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.ubuntu.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/canonical
- group: other
  title: ''
  type: SnapStore
  url: https://snapcraft.io/
- group: other
  title: ''
  type: Charmhub
  url: https://charmhub.io/
- group: other
  title: ''
  type: Launchpad
  url: https://launchpad.net/
- group: learn
  title: ''
  type: DiscourseForum
  url: https://discourse.ubuntu.com/
- group: commercial
  title: ''
  type: DataPrivacy
  url: https://ubuntu.com/legal/data-privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ubuntu.com/legal/terms
- group: company
  title: ''
  type: Blog
  url: https://canonical.com/blog/feed/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/packages/canonical-packages.yml
  title: ''
  type: Packages
  url: packages/canonical-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/packages/canonical-packages.yml
  title: ''
  type: SDKs
  url: packages/canonical-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/cli/canonical-cli.yml
  title: ''
  type: CLI
  url: cli/canonical-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/components/canonical-components.yml
  title: ''
  type: Components
  url: components/canonical-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/conventions/canonical-conventions.yml
  title: ''
  type: Conventions
  url: conventions/canonical-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/conventions/canonical-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/canonical-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/errors/canonical-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/canonical-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/data-model/canonical-data-model.yml
  title: ''
  type: DataModel
  url: data-model/canonical-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/lifecycle/canonical-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/canonical-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/lifecycle/canonical-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/canonical-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.canonical.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/changelog/canonical-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/canonical-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/conformance/canonical-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canonical-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/security/canonical-trust-center.yml
  title: ''
  type: Compliance
  url: security/canonical-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/security/canonical-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/canonical-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/security/canonical-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/canonical-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/security/canonical-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/canonical-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/well-known/canonical-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canonical-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/well-known/canonical-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/canonical-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/llms/canonical-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canonical-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/asyncapi/canonical-launchpad-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/canonical-launchpad-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/overlays/canonical-landscape-debarchive-provider-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canonical-landscape-debarchive-provider-overlay.yaml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/plans/canonical-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/canonical-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/rate-limits/canonical-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/canonical-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://ubuntu.com/pricing/pro
- group: start
  title: ''
  type: SignUp
  url: https://ubuntu.com/pro/subscribe
- group: start
  title: ''
  type: Login
  url: https://login.ubuntu.com/
- group: operate
  title: ''
  type: Support
  url: https://ubuntu.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ubuntu.com/legal/data-privacy
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.ubuntu.com/lxd/latest/rest-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://ubuntu.com/tutorials
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/canonical
created: '2026-03-16'
description: Canonical is the company behind Ubuntu, the world's most popular open source operating system for cloud, servers, desktops, IoT, and Kubernetes. Canonical publishes a broad set of developer APIs spanning the Ubuntu and Canonical ecosystem — the Snap Store and Snapcraft, the Charmhub charm marketplace, LXD system containers, MAAS bare-metal provisioning, Juju orchestration, Launchpad project hosting, Ubuntu Pro subscription services, and Landscape systems management — most of which are RESTful, open, and well documented.
finops:
- name: Canonical Finops
  service_category: API
  slug: canonical-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canonical.png
layout: provider
modified: '2026-09-05'
name: Canonical
nav: Providers
network: true
overview: 'Canonical publishes 108 APIs on the [APIs.io](https://apis.io/) network, including Assertions API, Search API, Snaps API, and 105 more. Tagged areas include Cloud, Linux, Open-Source, Ubuntu, and Containers.


  The Canonical catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Canonical''s developer surface includes authentication, documentation, engineering blog, CLI, changelog, pricing, signup flow, and 55 more developer resources.'
plans:
- name: Canonical Plans Pricing
  plan_count: 4
  slug: canonical-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Canonical Rate Limits
  slug: canonical-rate-limits
scopes:
- name: Canonical Scopes
  scope_count: 3
  slug: canonical-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: exemplar
  composite: 67.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.9
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 57.8
    developer_ergonomics: 73.2
    discoverability: 66.7
    operational_transparency: 60.5
  previous_composite: 64.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 4.6
      derived: 2
      marker_coverage: 1.9
      total: 108
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/screenshots/canonical-2026-06-20T173927.png
security:
- kind: authentication
  name: Canonical Authentication
  slug: canonical-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Canonical Domain Security
  slug: canonical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Canonical Vulnerability Disclosure
  slug: canonical-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Canonical Trust Center
  slug: canonical-trust-center
  summary_line: trust center published
slug: canonical
tags:
- Cloud
- Linux
- Open-Source
- Ubuntu
- Containers
- Bare Metal
- Charms
- Identity
website: https://canonical.com/
---
