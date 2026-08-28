---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 72
  human_in_the_loop: 10
  name: Cumulocity Agentic Access
  operation_count: 128
  slug: cumulocity-agentic-access
  summary_line: 128 operations · 72 acting · 10 human-in-the-loop
api_count: 39
apis:
- description: Constrained-device MQTT broker fronting the Cumulocity REST API with a CSV-based SmartREST 2.0 payload format that saves up to 80% of mobile traffic versus JSON. Supports static templates for common o
  name: Cumulocity MQTT and SmartREST API
  slug: cumulocity-mqtt-api
- description: Standards-compliant, multi-tenant MQTT broker for application-level messaging that does not need Cumulocity's domain model. Topics are tenant-scoped, persistent, and bridgeable to the Cumulocity domai
  name: Cumulocity MQTT Service API
  slug: cumulocity-mqtt-service-api
- description: The Alarms API from Cumulocity — 2 operation(s) for alarms.
  name: Cumulocity Alarms API
  slug: cumulocity-alarms-api
- description: The Application Binaries API from Cumulocity — 1 operation(s) for application binaries.
  name: Cumulocity Application Binaries API
  slug: cumulocity-application-binaries-api
- description: The Applications API from Cumulocity — 2 operation(s) for applications.
  name: Cumulocity Applications API
  slug: cumulocity-applications-api
- description: The Asset Instances API from Cumulocity — 2 operation(s) for asset instances.
  name: Cumulocity Asset Instances API
  slug: cumulocity-asset-instances-api
- description: The Asset Models API from Cumulocity — 2 operation(s) for asset models.
  name: Cumulocity Asset Models API
  slug: cumulocity-asset-models-api
- description: The Audit Records API from Cumulocity — 2 operation(s) for audit records.
  name: Cumulocity Audit Records API
  slug: cumulocity-audit-records-api
- description: The Bayeux Handshake API from Cumulocity — 1 operation(s) for bayeux handshake.
  name: Cumulocity Bayeux Handshake API
  slug: cumulocity-bayeux-handshake-api
- description: Binary attachments associated with managed objects.
  name: Cumulocity Binaries API
  slug: cumulocity-binaries-api
- description: The Bootstrap Users API from Cumulocity — 1 operation(s) for bootstrap users.
  name: Cumulocity Bootstrap Users API
  slug: cumulocity-bootstrap-users-api
- description: The Bulk Operations API from Cumulocity — 2 operation(s) for bulk operations.
  name: Cumulocity Bulk Operations API
  slug: cumulocity-bulk-operations-api
- description: Hierarchical relationships between managed objects.
  name: Cumulocity Child References API
  slug: cumulocity-child-references-api
- description: The Cloud Sync API from Cumulocity — 1 operation(s) for cloud sync.
  name: Cumulocity Cloud Sync API
  slug: cumulocity-cloud-sync-api
- description: The Current User API from Cumulocity — 1 operation(s) for current user.
  name: Cumulocity Current User API
  slug: cumulocity-current-user-api
- description: The Device Credentials API from Cumulocity — 1 operation(s) for device credentials.
  name: Cumulocity Device Credentials API
  slug: cumulocity-device-credentials-api
- description: The Event Binaries API from Cumulocity — 1 operation(s) for event binaries.
  name: Cumulocity Event Binaries API
  slug: cumulocity-event-binaries-api
- description: The Events API from Cumulocity — 2 operation(s) for events.
  name: Cumulocity Events API
  slug: cumulocity-events-api
- description: The External IDs API from Cumulocity — 2 operation(s) for external ids.
  name: Cumulocity External IDs API
  slug: cumulocity-external-ids-api
- description: The Groups API from Cumulocity — 2 operation(s) for groups.
  name: Cumulocity Groups API
  slug: cumulocity-groups-api
- description: Inventory documents representing devices, assets, groups, and digital twins.
  name: Cumulocity Managed Objects API
  slug: cumulocity-managed-objects-api
- description: The Measurements API from Cumulocity — 2 operation(s) for measurements.
  name: Cumulocity Measurements API
  slug: cumulocity-measurements-api
- description: The New Device Requests API from Cumulocity — 2 operation(s) for new device requests.
  name: Cumulocity New Device Requests API
  slug: cumulocity-new-device-requests-api
- description: The Offload Configurations API from Cumulocity — 2 operation(s) for offload configurations.
  name: Cumulocity Offload Configurations API
  slug: cumulocity-offload-configurations-api
- description: The Offload Jobs API from Cumulocity — 1 operation(s) for offload jobs.
  name: Cumulocity Offload Jobs API
  slug: cumulocity-offload-jobs-api
- description: The Operations API from Cumulocity — 2 operation(s) for operations.
  name: Cumulocity Operations API
  slug: cumulocity-operations-api
- description: The Queries API from Cumulocity — 1 operation(s) for queries.
  name: Cumulocity Queries API
  slug: cumulocity-queries-api
- description: The Retention Rules API from Cumulocity — 2 operation(s) for retention rules.
  name: Cumulocity Retention Rules API
  slug: cumulocity-retention-rules-api
- description: The Roles API from Cumulocity — 1 operation(s) for roles.
  name: Cumulocity Roles API
  slug: cumulocity-roles-api
- description: The Series API from Cumulocity — 1 operation(s) for series.
  name: Cumulocity Series API
  slug: cumulocity-series-api
- description: The Software Updates API from Cumulocity — 1 operation(s) for software updates.
  name: Cumulocity Software Updates API
  slug: cumulocity-software-updates-api
- description: The Subscriptions API from Cumulocity — 2 operation(s) for subscriptions.
  name: Cumulocity Subscriptions API
  slug: cumulocity-subscriptions-api
- description: Discover the measurement types reported against a managed object.
  name: Cumulocity Supported Measurements API
  slug: cumulocity-supported-measurements-api
- description: The System API from Cumulocity — 2 operation(s) for system.
  name: Cumulocity System API
  slug: cumulocity-system-api
- description: The Tenant Options API from Cumulocity — 2 operation(s) for tenant options.
  name: Cumulocity Tenant Options API
  slug: cumulocity-tenant-options-api
- description: The Tenant Statistics API from Cumulocity — 1 operation(s) for tenant statistics.
  name: Cumulocity Tenant Statistics API
  slug: cumulocity-tenant-statistics-api
- description: The Tenants API from Cumulocity — 2 operation(s) for tenants.
  name: Cumulocity Tenants API
  slug: cumulocity-tenants-api
- description: The Tokens API from Cumulocity — 2 operation(s) for tokens.
  name: Cumulocity Tokens API
  slug: cumulocity-tokens-api
- description: The Users API from Cumulocity — 2 operation(s) for users.
  name: Cumulocity Users API
  slug: cumulocity-users-api
artifact_total: 186
asyncapis:
- description: Constrained-device MQTT broker fronting the Cumulocity REST API with a CSV-based SmartREST 2.0 payload format that saves up to 80% of mobile traffic versus JSON. Supports static templates for common o
  name: Cumulocity MQTT and SmartREST API
  slug: cumulocity-mqtt-asyncapi
- description: Standards-compliant, multi-tenant MQTT broker for application-level messaging that does not need Cumulocity's domain model. Topics are tenant-scoped, persistent, and bridgeable to the Cumulocity domai
  name: Cumulocity MQTT Service
  slug: cumulocity-mqtt-service-asyncapi
- description: WebSocket consumer endpoint for Notification 2.0. After creating a Subscription and exchanging it for a short-lived JWT token via POST /notification2/token, connect to this WebSocket to consume ordere
  name: Cumulocity Notification 2.0 WebSocket
  slug: cumulocity-notification2-asyncapi
collections:
- collection_type: postman
  name: Cumulocity Alarm Alarms API
  slug: postman-cumulocity-alarms-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Application Binaries API
  slug: postman-cumulocity-application-binaries-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Applications API
  slug: postman-cumulocity-applications-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Asset Instances API
  slug: postman-cumulocity-asset-instances-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Asset Models API
  slug: postman-cumulocity-asset-models-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Audit Records API
  slug: postman-cumulocity-audit-records-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Bayeux Handshake API
  slug: postman-cumulocity-bayeux-handshake-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Binaries API
  slug: postman-cumulocity-binaries-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Bootstrap Users API
  slug: postman-cumulocity-bootstrap-users-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Bulk Operations API
  slug: postman-cumulocity-bulk-operations-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Child References API
  slug: postman-cumulocity-child-references-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Cloud Sync API
  slug: postman-cumulocity-cloud-sync-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Current User API
  slug: postman-cumulocity-current-user-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Device Credentials API
  slug: postman-cumulocity-device-credentials-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Event Binaries API
  slug: postman-cumulocity-event-binaries-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Events API
  slug: postman-cumulocity-events-api
- collection_type: postman
  name: Cumulocity Alarm Alarms External IDs API
  slug: postman-cumulocity-external-ids-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Groups API
  slug: postman-cumulocity-groups-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Managed Objects API
  slug: postman-cumulocity-managed-objects-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Measurements API
  slug: postman-cumulocity-measurements-api
- collection_type: postman
  name: Cumulocity Alarm Alarms New Device Requests API
  slug: postman-cumulocity-new-device-requests-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Offload Configurations API
  slug: postman-cumulocity-offload-configurations-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Offload Jobs API
  slug: postman-cumulocity-offload-jobs-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Operations API
  slug: postman-cumulocity-operations-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Queries API
  slug: postman-cumulocity-queries-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Retention Rules API
  slug: postman-cumulocity-retention-rules-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Roles API
  slug: postman-cumulocity-roles-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Series API
  slug: postman-cumulocity-series-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Software Updates API
  slug: postman-cumulocity-software-updates-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Subscriptions API
  slug: postman-cumulocity-subscriptions-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Supported Measurements API
  slug: postman-cumulocity-supported-measurements-api
- collection_type: postman
  name: Cumulocity Alarm Alarms System API
  slug: postman-cumulocity-system-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Tenant Options API
  slug: postman-cumulocity-tenant-options-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Tenant Statistics API
  slug: postman-cumulocity-tenant-statistics-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Tenants API
  slug: postman-cumulocity-tenants-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Tokens API
  slug: postman-cumulocity-tokens-api
- collection_type: postman
  name: Cumulocity Alarm Alarms Users API
  slug: postman-cumulocity-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cumulocity Alarm API
  slug: open-cumulocity-alarm-api
- collection_type: open
  name: Cumulocity Alarm Alarms API
  slug: open-cumulocity-alarms-api
- collection_type: open
  name: Cumulocity Application API
  slug: open-cumulocity-application-api
- collection_type: open
  name: Cumulocity Alarm Alarms Application Binaries API
  slug: open-cumulocity-application-binaries-api
- collection_type: open
  name: Cumulocity Alarm Alarms Applications API
  slug: open-cumulocity-applications-api
- collection_type: open
  name: Cumulocity Alarm Alarms Asset Instances API
  slug: open-cumulocity-asset-instances-api
- collection_type: open
  name: Cumulocity Alarm Alarms Asset Models API
  slug: open-cumulocity-asset-models-api
- collection_type: open
  name: Cumulocity Audit API
  slug: open-cumulocity-audit-api
- collection_type: open
  name: Cumulocity Alarm Alarms Audit Records API
  slug: open-cumulocity-audit-records-api
- collection_type: open
  name: Cumulocity Alarm Alarms Bayeux Handshake API
  slug: open-cumulocity-bayeux-handshake-api
- collection_type: open
  name: Cumulocity Alarm Alarms Binaries API
  slug: open-cumulocity-binaries-api
- collection_type: open
  name: Cumulocity Alarm Alarms Bootstrap Users API
  slug: open-cumulocity-bootstrap-users-api
- collection_type: open
  name: Cumulocity Alarm Alarms Bulk Operations API
  slug: open-cumulocity-bulk-operations-api
- collection_type: open
  name: Cumulocity Alarm Alarms Child References API
  slug: open-cumulocity-child-references-api
- collection_type: open
  name: Cumulocity Alarm Alarms Cloud Sync API
  slug: open-cumulocity-cloud-sync-api
- collection_type: open
  name: Cumulocity Alarm Alarms Current User API
  slug: open-cumulocity-current-user-api
- collection_type: open
  name: Cumulocity DataHub API
  slug: open-cumulocity-datahub-api
- collection_type: open
  name: Cumulocity Device Bootstrap API
  slug: open-cumulocity-device-bootstrap-api
- collection_type: open
  name: Cumulocity Device Control API
  slug: open-cumulocity-device-control-api
- collection_type: open
  name: Cumulocity Alarm Alarms Device Credentials API
  slug: open-cumulocity-device-credentials-api
- collection_type: open
  name: Cumulocity Digital Twin Manager API
  slug: open-cumulocity-dtm-api
- collection_type: open
  name: Cumulocity Edge API
  slug: open-cumulocity-edge-api
- collection_type: open
  name: Cumulocity Event API
  slug: open-cumulocity-event-api
- collection_type: open
  name: Cumulocity Alarm Alarms Event Binaries API
  slug: open-cumulocity-event-binaries-api
- collection_type: open
  name: Cumulocity Alarm Alarms Events API
  slug: open-cumulocity-events-api
- collection_type: open
  name: Cumulocity Alarm Alarms External IDs API
  slug: open-cumulocity-external-ids-api
- collection_type: open
  name: Cumulocity Alarm Alarms Groups API
  slug: open-cumulocity-groups-api
- collection_type: open
  name: Cumulocity Identity API
  slug: open-cumulocity-identity-api
- collection_type: open
  name: Cumulocity Inventory API
  slug: open-cumulocity-inventory-api
- collection_type: open
  name: Cumulocity Alarm Alarms Managed Objects API
  slug: open-cumulocity-managed-objects-api
- collection_type: open
  name: Cumulocity Measurement API
  slug: open-cumulocity-measurement-api
- collection_type: open
  name: Cumulocity Alarm Alarms Measurements API
  slug: open-cumulocity-measurements-api
- collection_type: open
  name: Cumulocity Alarm Alarms New Device Requests API
  slug: open-cumulocity-new-device-requests-api
- collection_type: open
  name: Cumulocity Notification 2.0 API
  slug: open-cumulocity-notification2-api
- collection_type: open
  name: Cumulocity Alarm Alarms Offload Configurations API
  slug: open-cumulocity-offload-configurations-api
- collection_type: open
  name: Cumulocity Alarm Alarms Offload Jobs API
  slug: open-cumulocity-offload-jobs-api
- collection_type: open
  name: Cumulocity Alarm Alarms Operations API
  slug: open-cumulocity-operations-api
- collection_type: open
  name: Cumulocity Alarm Alarms Queries API
  slug: open-cumulocity-queries-api
- collection_type: open
  name: Cumulocity Real-Time Notifications API
  slug: open-cumulocity-real-time-api
- collection_type: open
  name: Cumulocity Retention Rules API
  slug: open-cumulocity-retention-api
- collection_type: open
  name: Cumulocity Alarm Alarms Retention Rules API
  slug: open-cumulocity-retention-rules-api
- collection_type: open
  name: Cumulocity Alarm Alarms Roles API
  slug: open-cumulocity-roles-api
- collection_type: open
  name: Cumulocity Alarm Alarms Series API
  slug: open-cumulocity-series-api
- collection_type: open
  name: Cumulocity Alarm Alarms Software Updates API
  slug: open-cumulocity-software-updates-api
- collection_type: open
  name: Cumulocity Alarm Alarms Subscriptions API
  slug: open-cumulocity-subscriptions-api
- collection_type: open
  name: Cumulocity Alarm Alarms Supported Measurements API
  slug: open-cumulocity-supported-measurements-api
- collection_type: open
  name: Cumulocity Alarm Alarms System API
  slug: open-cumulocity-system-api
- collection_type: open
  name: Cumulocity Tenant API
  slug: open-cumulocity-tenant-api
- collection_type: open
  name: Cumulocity Alarm Alarms Tenant Options API
  slug: open-cumulocity-tenant-options-api
- collection_type: open
  name: Cumulocity Alarm Alarms Tenant Statistics API
  slug: open-cumulocity-tenant-statistics-api
- collection_type: open
  name: Cumulocity Alarm Alarms Tenants API
  slug: open-cumulocity-tenants-api
- collection_type: open
  name: Cumulocity Alarm Alarms Tokens API
  slug: open-cumulocity-tokens-api
- collection_type: open
  name: Cumulocity User API
  slug: open-cumulocity-user-api
- collection_type: open
  name: Cumulocity Alarm Alarms Users API
  slug: open-cumulocity-users-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cumulocity/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cumulocity-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cumulocity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cumulocity-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.cumulocity.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.cumulocity.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/api/core/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/api/datahub/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/api/dtm/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/api/edge/
- group: start
  title: ''
  type: GettingStarted
  url: https://cumulocity.com/docs/welcome/quickstart/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/docs/concepts/introduction/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/docs/concepts/domain-model/
- group: auth
  title: ''
  type: Authentication
  url: https://cumulocity.com/docs/authentication/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/docs/reference/general-aspects/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/docs/reference/rest-conventions/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/docs/reference/notifications/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/docs/device-integration/mqtt/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/docs/smartrest/smartrest-two/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/docs/microservice-sdk/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/docs/web-sdk/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/docs/web-sdk/web-sdk-overview/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/docs/streaming-analytics/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/docs/datahub/datahub-overview/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/docs/digital-twin-manager/dtm-overview/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/docs/edge/edge-overview/
- group: operate
  title: ''
  type: ChangeLog
  url: https://cumulocity.com/docs/release-notes/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cumulocity.com
- group: operate
  title: ''
  type: Forums
  url: https://community.cumulocity.com
- group: operate
  title: ''
  type: Support
  url: https://cumulocity.com/contact-support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cumulocity.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cumulocity.com/legal/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://cumulocity.com/legal/dpa/
- group: auth
  title: ''
  type: TrustCenter
  url: https://cumulocity.com/trust-center/
- group: auth
  title: ''
  type: Security
  url: https://cumulocity.com/security/
- group: commercial
  title: ''
  type: Pricing
  url: https://cumulocity.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://cumulocity.com/free-trial/
- group: company
  title: ''
  type: Blog
  url: https://cumulocity.com/blog/
- group: company
  title: ''
  type: Press
  url: https://cumulocity.com/press-releases/
- group: other
  title: ''
  type: CaseStudies
  url: https://cumulocity.com/case-studies/
- group: other
  title: ''
  type: Events
  url: https://cumulocity.com/events/
- group: learn
  title: ''
  type: Video
  url: https://www.youtube.com/@CumulocityIoT
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cumulocity/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cumulocity-IoT
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SoftwareAG
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Cumulocity-IoT/cumulocity-clients-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Cumulocity-IoT/cumulocity-python-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Cumulocity-IoT/cumulocity-sdk-dotnet
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@c8y/client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Cumulocity-IoT/cumulocity-ui-toolkit
- group: build
  title: ''
  type: CLI
  url: https://github.com/reubenmiller/go-c8y-cli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/reubenmiller/go-c8y
- group: build
  title: ''
  type: Tools
  url: https://github.com/Cumulocity-IoT/cumulocity-microservice-archetype
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Cumulocity-IoT/cumulocity-examples
- group: build
  title: ''
  type: Tools
  url: https://github.com/Cumulocity-IoT/cumulocity-dynamic-mapper
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Cumulocity-IoT/cumulocity-devicemanagement-agent
- group: build
  title: ''
  type: Tools
  url: https://github.com/Cumulocity-IoT/cumulocity-mcp-server
- group: build
  title: ''
  type: Tools
  url: https://github.com/Cumulocity-IoT/c8y-ai-sandbox
- group: build
  title: ''
  type: Tools
  url: https://github.com/Cumulocity-IoT/cumulocity-cypress
- group: build
  title: ''
  type: Tools
  url: https://github.com/Cumulocity-IoT/cumulocity-subtenant-management
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Cumulocity-IoT/apama-analytics-builder-block-sdk
- group: build
  title: ''
  type: Tools
  url: https://github.com/Cumulocity-IoT/apama-eplapps-tools
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Cumulocity-IoT/streaming-analytics-sample-repo-template
- group: build
  title: ''
  type: Tools
  url: https://github.com/Cumulocity-IoT/cumulocity-remote-access-cloud-http-proxy
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Cumulocity-IoT/cumulocity-os-repo-overview
- group: commercial
  title: ''
  type: Plans
  url: plans/cumulocity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cumulocity-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cumulocity-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: Cumulocity is an enterprise AIoT (Artificial Intelligence of Things) platform that connects, manages, and analyzes industrial assets from cloud to edge. Founded inside Software AG and divested via a 2025 management buyout into an independent company (sale announced alongside the IBM acquisition of Software AG's StreamSets and webMethods), Cumulocity provides a full-stack platform — REST and MQTT APIs, device management, digital twin modeling, streaming analytics powered by Apama, DataHub data-lake offload, Cockpit dashboards, and on-prem Edge deployments — validated at 100 million devices and 1 million messages/second across industrial equipment, medical devices, manufacturing, utilities, energy, transport, retail, and telecommunications.
examples:
- key_count: 6
  name: Cumulocity Create Alarm Example
  slug: cumulocity-create-alarm-example
- key_count: 5
  name: Cumulocity Create Event Example
  slug: cumulocity-create-event-example
- key_count: 6
  name: Cumulocity Create Managed Object Example
  slug: cumulocity-create-managed-object-example
- key_count: 4
  name: Cumulocity Create Measurement Example
  slug: cumulocity-create-measurement-example
- key_count: 4
  name: Cumulocity Create Notification2 Subscription Example
  slug: cumulocity-create-notification2-subscription-example
- key_count: 3
  name: Cumulocity Create Operation Example
  slug: cumulocity-create-operation-example
features:
- Core REST API covering inventory, identity, measurements, events, alarms, device control, device bootstrap, tenants, users, applications, audit, retention, and real-time
- Notification 2.0 — high-throughput, ordered, persistent WebSocket streaming with JWT-token auth and per-subscriber buffering
- Bayeux/CometD legacy real-time channel for measurements/events/alarms/operations/inventory subscriptions
- MQTT 3.1.1/5.0 broker with SmartREST 2.0 CSV payload format saving up to 80% mobile traffic vs JSON; 16 KiB max payload
- MQTT Service — multi-tenant standards-compliant broker for application-level messaging independent of the Cumulocity domain model
- Zero-touch device onboarding via bootstrap user + Identity API external-ID lookup
- Microservice SDK with Java/Spring archetype and managed container hosting; bootstrap-user auth model
- Web SDK with Angular plugins, hosted application uploads, and per-tenant subdomain serving
- DataHub — offload operational data to a Parquet/Dremio data lake; query via SQL/JDBC/ODBC/Arrow Flight to Power BI and Tableau
- Digital Twin Manager (DTM) — asset modeling, hierarchies, computed smart functions, custom properties
- Streaming Analytics powered by Apama EPL and the Analytics Builder low-code block editor
- Cockpit dashboards with per-tenant customization, plugins, and the UI Toolkit monorepo
- Edge — single-node on-prem deployment, including air-gapped option, with selective cloud sync
- Multi-tenancy with management tenant, enterprise tenants, and sub-tenants for OEMs/MSPs
- LoRa framework with built-in connectors for TTN, ChirpStack, Kerlink Wanesy, Loriot, Actility, Objenious, Live Objects, Orbiwan
- Dynamic Mapper — zero-code bridge between arbitrary message brokers (Kafka, generic MQTT) and the Cumulocity domain model
- Cloud Remote Access — SSH/VNC/Telnet to devices through the Cumulocity cloud
- Audit API for immutable compliance trail across user actions, operations, and managed-object changes
- Retention rules for per-data-type lifecycle (measurements / events / alarms / audit / operations)
- SSO via SAML and OIDC; SCIM provisioning for enterprise tenants; per-managed-object inventory roles
- Client SDKs: Java, Python, .NET (C#), JavaScript/TypeScript (@c8y/client), Go (community go-c8y)
- go-c8y-cli — community-built feature-complete CLI with SSO (auth-code / device flow), session management, piping, and remote-access support
- Python and TypeScript MCP server implementations for Claude / agentic access to Cumulocity tenants
- Cypress test toolkit for end-to-end UI testing of Cumulocity-based applications
- Sub-tenant management tooling for enterprise/management hierarchies
- thin-edge.io upstream open-source agent for constrained edge devices
- Validated at 100M devices and 1M messages/second; A+ SSL Labs rating
- Five hosted regions: eu-latest, us, emea, apj, cumulocity.com (RoW); Edge for on-prem
- Three cloud plans (Starter EUR 215/mo, Business, Enterprise) plus Edge Connected and Edge Air-Gapped
- 30-day full-feature free trial with up to 10 devices
finops:
- name: Cumulocity Finops
  service_category: Internet of Things
  slug: cumulocity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cumulocity.png
json_schemas:
- name: Cumulocity Alarm
  property_count: 12
  slug: cumulocity-alarm
- name: Cumulocity Event
  property_count: 8
  slug: cumulocity-event
- name: Cumulocity Managed Object
  property_count: 22
  slug: cumulocity-managed-object
- name: Cumulocity Measurement
  property_count: 7
  slug: cumulocity-measurement
json_structures:
- name: Cumulocity Alarm Structure
  property_count: 12
  slug: cumulocity-alarm-structure
- name: Cumulocity Managed Object Structure
  property_count: 13
  slug: cumulocity-managed-object-structure
jsonld:
- class_count: 16
  name: Cumulocity Context
  property_count: 22
  slug: cumulocity-context
layout: provider
modified: '2026-05-25'
name: Cumulocity
nav: Providers
network: true
overview: 'Cumulocity publishes 39 APIs on the [APIs.io](https://apis.io/) network, including MQTT and SmartREST API, MQTT Service API, Alarms API, and 36 more. Tagged areas include IoT, Internet of Things, Industrial IoT, AIoT, and Device Management.


  The Cumulocity catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Cumulocity''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, support, pricing, and 62 more developer resources.'
plans:
- name: Cumulocity Plans Pricing
  plan_count: 6
  slug: cumulocity-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Cumulocity Rate Limits
  slug: cumulocity-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Cumulocity API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: cumulocity-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Cumulocity API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cumulocity-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Cumulocity API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 4
    warn: 4
  slug: cumulocity-rules
score:
  band: strong
  composite: 63.2
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 13.6
    contract_quality: 74.4
    developer_ergonomics: 66.7
    discoverability: 50.0
    governance: 13.6
    operational_transparency: 47.4
  previous_composite: 63.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 37
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cumulocity/refs/heads/main/screenshots/cumulocity-2026-06-20T175331.png
security:
- kind: authentication
  name: Cumulocity Authentication
  slug: cumulocity-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Cumulocity Domain Security
  slug: cumulocity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cumulocity
tags:
- IoT
- Internet of Things
- Industrial IoT
- AIoT
- Device Management
- Digital Twin
- MQTT
- Edge Computing
- Streaming Analytics
- Data Lake
website: https://www.cumulocity.com
---
