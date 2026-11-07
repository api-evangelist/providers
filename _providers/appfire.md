---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 27
  human_in_the_loop: 2
  name: Appfire Agentic Access
  operation_count: 41
  slug: appfire-agentic-access
  summary_line: 41 operations · 27 acting · 2 human-in-the-loop
api_count: 3
apis:
- description: Public REST API for BigPicture, BigGantt and BigTemplate on Atlassian Cloud (Appfire's portfolio and project-management suite). Exposes boxes, box types, tasks, teams, team memberships, resources, ski
  name: BigPicture Cloud Public API
  slug: bigpicture-cloud-public-api
- baseURL: https://timehubjra.7pace.com
  baseurl_source: declared
  description: 'Retrieve objectives, key results, updates, and comments. Use **expand** to include related entities (teams, periods, labels, etc.) instead of IDs only. Authenticate with the **API-Token** header. For '
  name: Appfire API query methods API
  slug: appfire-api-query-methods-api
- baseURL: https://timehubjra.7pace.com
  baseurl_source: declared
  description: '**POST** with a JSON body. Send **Content-Type: application/json** and the **API-Token** header. Creates update records that set current status (and key-result progress where applicable).'
  name: Appfire API update methods API
  slug: appfire-api-update-methods-api
- baseURL: https://timehubjra.7pace.com
  baseurl_source: declared
  description: The Settings API from Appfire — 16 operation(s) for settings.
  name: Appfire Settings API
  slug: appfire-settings-api
- baseURL: https://timehubjra.7pace.com
  baseurl_source: declared
  description: The Worklogs API from Appfire — 10 operation(s) for worklogs.
  name: Appfire Worklogs API
  slug: appfire-worklogs-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The activity-resource API from Appfire — 3 operation(s) for activity-resource.
  name: Appfire Activity Resource API
  slug: appfire-activity-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The addon-descriptor-controller API from Appfire — 1 operation(s) for addon-descriptor-controller.
  name: Appfire Addon Descriptor Controller API
  slug: appfire-addon-descriptor-controller-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The ai-resource API from Appfire — 1 operation(s) for ai-resource.
  name: Appfire AI Resource API
  slug: appfire-ai-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The ai-settings-resource API from Appfire — 1 operation(s) for ai-settings-resource.
  name: Appfire AI Settings Resource API
  slug: appfire-ai-settings-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The aikr-resource API from Appfire — 1 operation(s) for aikr-resource.
  name: Appfire Aikr Resource API
  slug: appfire-aikr-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The alignment-resource API from Appfire — 6 operation(s) for alignment-resource.
  name: Appfire Alignment Resource API
  slug: appfire-alignment-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The api-token-resource API from Appfire — 5 operation(s) for api-token-resource.
  name: Appfire API Token Resource API
  slug: appfire-api-token-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The atlassian-connect-error-controller API from Appfire — 1 operation(s) for atlassian-connect-error-controller.
  name: Appfire Atlassian Connect Error Controller API
  slug: appfire-atlassian-connect-error-controller-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The auto-kr-index-resource API from Appfire — 2 operation(s) for auto-kr-index-resource.
  name: Appfire Auto Kr Index Resource API
  slug: appfire-auto-kr-index-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The auto-kr-resource API from Appfire — 4 operation(s) for auto-kr-resource.
  name: Appfire Auto Kr Resource API
  slug: appfire-auto-kr-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The child-okr-filter-resource API from Appfire — 1 operation(s) for child-okr-filter-resource.
  name: Appfire Child Okr Filter Resource API
  slug: appfire-child-okr-filter-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The comments-resource API from Appfire — 3 operation(s) for comments-resource.
  name: Appfire Comments Resource API
  slug: appfire-comments-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: Manage custom field definitions for Objectives and Key Results. Custom fields allow workspace administrators to attach additional structured data to OKRs — for example a "Risk level" dropdown, a "Budg
  name: Appfire Custom Fields API
  slug: appfire-custom-fields-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: 'Manage data residency migrations for SPM tenants. Follows the standard Appfire migration lifecycle: schedule → start → status → commit/rollback.'
  name: Appfire Data Residency Migration API
  slug: appfire-data-residency-migration-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: Appfire Data Retention Service (DRS) v2 integration. Handles tenant data cleanup when a tenant's data retention period expires after license expiration or app uninstall.
  name: Appfire Data Retention API
  slug: appfire-data-retention-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The dynamic-module-manual-registration-resource API from Appfire — 2 operation(s) for dynamic-module-manual-registration-resource.
  name: Appfire Dynamic Module Manual Registration Resource API
  slug: appfire-dynamic-module-manual-registration-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The entity-bulk-resource API from Appfire — 1 operation(s) for entity-bulk-resource.
  name: Appfire Entity Bulk Resource API
  slug: appfire-entity-bulk-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The export-resource API from Appfire — 1 operation(s) for export-resource.
  name: Appfire Export Resource API
  slug: appfire-export-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The external-link-resource API from Appfire — 2 operation(s) for external-link-resource.
  name: Appfire External Link Resource API
  slug: appfire-external-link-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The feature-flag-resource API from Appfire — 2 operation(s) for feature-flag-resource.
  name: Appfire Feature Flag Resource API
  slug: appfire-feature-flag-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The filtered-okr-resource API from Appfire — 1 operation(s) for filtered-okr-resource.
  name: Appfire Filtered Okr Resource API
  slug: appfire-filtered-okr-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The heap-dump-resource API from Appfire — 1 operation(s) for heap-dump-resource.
  name: Appfire Heap Dump Resource API
  slug: appfire-heap-dump-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The host-info-resource API from Appfire — 1 operation(s) for host-info-resource.
  name: Appfire Host Info Resource API
  slug: appfire-host-info-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The impact-resource API from Appfire — 3 operation(s) for impact-resource.
  name: Appfire Impact Resource API
  slug: appfire-impact-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The import-okr-resource API from Appfire — 1 operation(s) for import-okr-resource.
  name: Appfire Import Okr Resource API
  slug: appfire-import-okr-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The jql-function-resource API from Appfire — 2 operation(s) for jql-function-resource.
  name: Appfire Jql Function Resource API
  slug: appfire-jql-function-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: Manage links between OKR key results and BigPicture boxes. Linked entities contribute to auto key result progress calculation.
  name: Appfire Key Result Linking API
  slug: appfire-key-result-linking-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The key-result-resource-2 API from Appfire — 27 operation(s) for key-result-resource-2.
  name: Appfire Key Result Resource 2 API
  slug: appfire-key-result-resource-2-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The label-resource API from Appfire — 3 operation(s) for label-resource.
  name: Appfire Label Resource API
  slug: appfire-label-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: SPM app lifecycle event handlers for Connect-based installations. Called by the Appfire platform when an app is installed or uninstalled.
  name: Appfire Lifecycle API
  slug: appfire-lifecycle-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The migrate-tenant-resource API from Appfire — 1 operation(s) for migrate-tenant-resource.
  name: Appfire Migrate Tenant Resource API
  slug: appfire-migrate-tenant-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The migrations-resource API from Appfire — 3 operation(s) for migrations-resource.
  name: Appfire Migrations Resource API
  slug: appfire-migrations-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The milestone-resource API from Appfire — 2 operation(s) for milestone-resource.
  name: Appfire Milestone Resource API
  slug: appfire-milestone-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The notification-settings-resource API from Appfire — 2 operation(s) for notification-settings-resource.
  name: Appfire Notification Settings Resource API
  slug: appfire-notification-settings-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The objective-type-resource API from Appfire — 6 operation(s) for objective-type-resource.
  name: Appfire Objective Type Resource API
  slug: appfire-objective-type-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: Bulk alignment link lookup for objectives and key results, for M2M consumers (PPM), keyed by installation ID.
  name: Appfire OKR alignment (internal) API
  slug: appfire-okr-alignment-internal-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: Objective types, labels, teams, and period aliases for M2M consumers (PPM), keyed by installation ID.
  name: Appfire OKR metadata (internal) API
  slug: appfire-okr-metadata-internal-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The okr-query-resource API from Appfire — 1 operation(s) for okr-query-resource.
  name: Appfire Okr Query Resource API
  slug: appfire-okr-query-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The okr-resource API from Appfire — 28 operation(s) for okr-resource.
  name: Appfire Okr Resource API
  slug: appfire-okr-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: Retrieve and update OKR objectives and key results. Used by BigPicture for cross-product OKR synchronization.
  name: Appfire OKRs API
  slug: appfire-okrs-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The one-installation-descriptor-views API from Appfire — 1 operation(s) for one-installation-descriptor-views.
  name: Appfire One Installation Descriptor Views API
  slug: appfire-one-installation-descriptor-views-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The outgoing-mail-resource API from Appfire — 2 operation(s) for outgoing-mail-resource.
  name: Appfire Outgoing Mail Resource API
  slug: appfire-outgoing-mail-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The period-alias-resource API from Appfire — 5 operation(s) for period-alias-resource.
  name: Appfire Period Alias Resource API
  slug: appfire-period-alias-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: Query OKR time periods. Periods define the time boundaries for OKR cycles, such as quarters or custom date ranges.
  name: Appfire Periods API
  slug: appfire-periods-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The permission-debug-resource API from Appfire — 1 operation(s) for permission-debug-resource.
  name: Appfire Permission Debug Resource API
  slug: appfire-permission-debug-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: Check user permissions on OKR objectives and key results. Returns the granted permissions (VIEW, EDIT) for each requested entity based on the user's access restrictions.
  name: Appfire Permissions API
  slug: appfire-permissions-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: Invalidate OKR's cached UPS permission answers for a tenant. Called by BigPicture when OKR global permissions change so the change takes effect immediately instead of after cache expiry.
  name: Appfire Permissions Cache API
  slug: appfire-permissions-cache-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The permissions-resource API from Appfire — 9 operation(s) for permissions-resource.
  name: Appfire Permissions Resource API
  slug: appfire-permissions-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The queue-tasks-consumers API from Appfire — 2 operation(s) for queue-tasks-consumers.
  name: Appfire Queue Tasks Consumers API
  slug: appfire-queue-tasks-consumers-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: Read and set a tenant's OKR Restriction mode. Used by BigPicture's Security page; the M2M scope is the authorization and no user identity is exchanged.
  name: Appfire Restriction mode API
  slug: appfire-restriction-mode-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The restriction-resource API from Appfire — 1 operation(s) for restriction-resource.
  name: Appfire Restriction Resource API
  slug: appfire-restriction-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The restrictions-feature-settings-resource API from Appfire — 1 operation(s) for restrictions-feature-settings-resource.
  name: Appfire Restrictions Feature Settings Resource API
  slug: appfire-restrictions-feature-settings-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The saved-view-resource API from Appfire — 3 operation(s) for saved-view-resource.
  name: Appfire Saved View Resource API
  slug: appfire-saved-view-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The schedule-kr-update-reminder-email-job API from Appfire — 1 operation(s) for schedule-kr-update-reminder-email-job.
  name: Appfire Schedule Kr Update Reminder Email Job API
  slug: appfire-schedule-kr-update-reminder-email-job-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The send-email-job API from Appfire — 1 operation(s) for send-email-job.
  name: Appfire Send Email Job API
  slug: appfire-send-email-job-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The shortened-link-resource API from Appfire — 2 operation(s) for shortened-link-resource.
  name: Appfire Shortened Link Resource API
  slug: appfire-shortened-link-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The spm-context-resource API from Appfire — 1 operation(s) for spm-context-resource.
  name: Appfire Spm Context Resource API
  slug: appfire-spm-context-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The statistics-resource API from Appfire — 3 operation(s) for statistics-resource.
  name: Appfire Statistics Resource API
  slug: appfire-statistics-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: Background migration of local teams to the external Team Service.
  name: Appfire Team migration (internal) API
  slug: appfire-team-migration-internal-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The team-resource API from Appfire — 2 operation(s) for team-resource.
  name: Appfire Team Resource API
  slug: appfire-team-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The team-sync-resource API from Appfire — 2 operation(s) for team-sync-resource.
  name: Appfire Team Sync Resource API
  slug: appfire-team-sync-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The tenant-data-removal-service API from Appfire — 1 operation(s) for tenant-data-removal-service.
  name: Appfire Tenant Data Removal Service API
  slug: appfire-tenant-data-removal-service-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The tenant-license-sync-service API from Appfire — 1 operation(s) for tenant-license-sync-service.
  name: Appfire Tenant License Sync Service API
  slug: appfire-tenant-license-sync-service-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The tenants-synchronization-service API from Appfire — 4 operation(s) for tenants-synchronization-service.
  name: Appfire Tenants Synchronization Service API
  slug: appfire-tenants-synchronization-service-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The test-setup-resource API from Appfire — 6 operation(s) for test-setup-resource.
  name: Appfire Test Setup Resource API
  slug: appfire-test-setup-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The trigger-mail-send-resource API from Appfire — 3 operation(s) for trigger-mail-send-resource.
  name: Appfire Trigger Mail Send Resource API
  slug: appfire-trigger-mail-send-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: Batch backfill of ADMIN/VIEWER role assignments to UPS.
  name: Appfire UPS global role seed (internal) API
  slug: appfire-ups-global-role-seed-internal-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The user-permissions-bean API from Appfire — 1 operation(s) for user-permissions-bean.
  name: Appfire User Permissions Bean API
  slug: appfire-user-permissions-bean-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The user-permissions-resource API from Appfire — 1 operation(s) for user-permissions-resource.
  name: Appfire User Permissions Resource API
  slug: appfire-user-permissions-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The user-resource API from Appfire — 5 operation(s) for user-resource.
  name: Appfire User Resource API
  slug: appfire-user-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: The user-setting-resource API from Appfire — 2 operation(s) for user-setting-resource.
  name: Appfire User Setting Resource API
  slug: appfire-user-setting-resource-api
- baseURL: https://api.bigpicture.one/public/bigpicture/rest
  baseurl_source: declared
  description: Configure webhook target URLs for receiving OKR change notifications. Used by BigPicture to register its callback endpoint for real-time OKR synchronization.
  name: Appfire Webhook Configuration API
  slug: appfire-webhook-configuration-api
artifact_total: 89
collections:
- collection_type: open
  name: OKR API query methods API
  slug: open-appfire-api-query-methods-api
- collection_type: open
  name: OKR API update methods API
  slug: open-appfire-api-update-methods-api
- collection_type: open
  name: Appfire Settings API
  slug: open-appfire-settings-api
- collection_type: open
  name: Appfire Worklogs API
  slug: open-appfire-worklogs-api
common:
- group: other
  href: https://artifacts.apis.io/appfire/capabilities/appfire-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/appfire-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/appfire/mcp/appfire-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/appfire-mcp.yml
- group: agent
  href: https://artifacts.apis.io/appfire/agentic-access/appfire-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/appfire-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/appfire/security/appfire-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/appfire-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/appfire/security/appfire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appfire-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/appfire/authentication/appfire-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appfire-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://appfire.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bigpicture.one/
- group: docs
  title: ''
  type: Documentation
  url: https://appfire.atlassian.net/wiki/spaces/APPFIRE/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.bigpicture.one/reference/whatisbigpicture
- group: operate
  title: ''
  type: Support
  url: https://support.appfire.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.appfire.com/
- group: company
  title: ''
  type: Blog
  url: https://appfire.com/resources/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appfire.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appfire.com/eula
- group: auth
  title: ''
  type: Compliance
  url: https://trust.appfire.com/
- group: build
  href: https://artifacts.apis.io/appfire/packages/appfire-packages.yml
  title: ''
  type: Packages
  url: packages/appfire-packages.yml
- group: build
  href: https://artifacts.apis.io/appfire/packages/appfire-packages.yml
  title: ''
  type: SDKs
  url: packages/appfire-packages.yml
- group: build
  href: https://artifacts.apis.io/appfire/cli/appfire-cli.yml
  title: ''
  type: CLI
  url: cli/appfire-cli.yml
- group: design
  href: https://artifacts.apis.io/appfire/conventions/appfire-conventions.yml
  title: ''
  type: Conventions
  url: conventions/appfire-conventions.yml
- group: design
  href: https://artifacts.apis.io/appfire/errors/appfire-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/appfire-problem-types.yml
- group: design
  href: https://artifacts.apis.io/appfire/lifecycle/appfire-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/appfire-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/appfire/changelog/appfire-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/appfire-changelog.yml
- group: design
  href: https://artifacts.apis.io/appfire/conformance/appfire-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appfire-conformance.yml
- group: design
  href: https://artifacts.apis.io/appfire/data-model/appfire-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appfire-data-model.yml
- group: agent
  href: https://artifacts.apis.io/appfire/llms/appfire-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appfire-llms.txt
- group: agent
  href: https://artifacts.apis.io/appfire/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/appfire/overlays/appfire-okr-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appfire-okr-overlay.yaml
- group: other
  href: https://artifacts.apis.io/appfire/overlays/appfire-7pace-timetracker-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appfire-7pace-timetracker-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/appfire/overlays/appfire-7pace-timetracker-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appfire-7pace-timetracker-v1-overlay.yaml
created: '2026-08-06'
description: 'Appfire is a global software company that builds, acquires, and operates a large portfolio of apps that enhance, extend, and connect the platforms enterprise teams already run on — principally Atlassian Jira, Confluence and Jira Service Management (Cloud and Data Center), plus Microsoft Azure DevOps, monday.com and Salesforce. Its product families cover portfolio and project management (BigPicture, BigGantt, BigTemplate), goal setting (OKR for Jira), time tracking (7pace Timetracker for Jira and for Azure DevOps), document workflow and approvals (Comala Document Management), workflow automation and scripting (Jira Misc Workflow Extensions, Power Scripts), and administration tooling (the Appfire/Atlassian Command Line Interface). Public, machine-readable API surface is per-product rather than company-wide: 7pace Timetracker for Jira publishes OpenAPI 3.0 for its v1 and v2 REST APIs, the OKR app serves an OpenAPI 3.1 document for its public export/update API, and BigPicture publishes
  a hosted API reference for its Cloud and Data Center REST APIs.'
layout: provider
modified: '2026-08-06'
name: Appfire
nav: Providers
network: true
overview: 'Appfire publishes 77 API contracts indexed on the [APIs.io](https://apis.io/) network, including API query methods API, API update methods API, Settings API, and 74 more. Tagged areas include Atlassian, Jira, Confluence, Project Portfolio Management, and Work Management.


  The Appfire catalog on APIs.io includes 1 Spectral governance ruleset.


  Appfire''s developer surface includes authentication, documentation, API reference, support, engineering blog, CLI, changelog, and 23 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Appfire API Rules
  rule_count: 49
  severity_counts:
    error: 31
    hint: 0
    info: 6
    warn: 12
  slug: appfire-rules
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.6
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 60.1
    discoverability: 75.0
    operational_transparency: 31.6
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 97.4
      derived: 0
      marker_coverage: 94.9
      total: 78
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/appfire/appfire-2026-08-07T161502.png
security:
- kind: authentication
  name: Appfire Authentication
  slug: appfire-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Appfire Domain Security
  slug: appfire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Appfire Trust Center
  slug: appfire-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, HIPAA, GDPR
skill_count: 3
skills:
- name: Sync 7pace Timetracker worklogs
  slug: appfire-7pace-worklog-sync
- name: Export Appfire OKR objectives, key results and check-ins
  slug: appfire-okr-export-progress
- name: Post an OKR check-in to Appfire OKR for Jira
  slug: appfire-okr-post-checkin
slug: appfire
tags:
- Atlassian
- Jira
- Confluence
- Project Portfolio Management
- Work Management
- Time Tracking
- OKRs
- Workflow Automation
- Azure DevOps
- Marketplace Apps
- Document Workflow
- Enterprise Software
website: https://appfire.com
---
