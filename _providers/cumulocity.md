---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 72
  human_in_the_loop: 10
  name: Cumulocity Agentic Access
  operation_count: 128
  slug: cumulocity-agentic-access
  summary_line: 128 operations · 72 acting · 10 human-in-the-loop
api_count: 4
apis:
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: Constrained-device MQTT broker fronting the Cumulocity REST API with a CSV-based SmartREST 2.0 payload format that saves up to 80% of mobile traffic versus JSON. Supports static templates for common o
  name: Cumulocity MQTT and SmartREST API
  slug: cumulocity-mqtt-api
- baseURL: mqtts://mqtt.{tenant}.cumulocity.com:8883
  baseurl_source: declared
  description: Standards-compliant, multi-tenant MQTT broker for application-level messaging that does not need Cumulocity's domain model. Topics are tenant-scoped, persistent, and bridgeable to the Cumulocity domai
  name: Cumulocity MQTT Service API
  slug: cumulocity-mqtt-service-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Alarms API from Cumulocity — 2 operation(s) for alarms.
  name: Cumulocity Alarms API
  phrasing_intents:
  - id: postAlarmCollectionResource
    intent: Raise a new alarm for a device
    question: How can I raise an alarm against a device from my own code?
  - id: getAlarmCollectionResource
    intent: List alarms raised on devices
    question: Which alarms are currently active on my Cumulocity devices?
  - id: putAlarmCollectionResource
    intent: Update many alarms at once by filter
    question: How do I acknowledge every active alarm on a device in one call?
  - id: deleteAlarmCollectionResource
    intent: Delete alarms matching a filter
    question: Is there a way to purge a whole batch of old alarms by filter?
  - id: getAlarmResource
    intent: Look up a single alarm by ID
    question: How do I fetch the full details of one alarm by its ID?
  - id: putAlarmResource
    intent: Change the status or text of one alarm
    question: How do I acknowledge or clear one specific alarm?
  phrasing_ops: 6
  slug: cumulocity-alarms-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Application Binaries API from Cumulocity — 1 operation(s) for application binaries.
  name: Cumulocity Application Binaries API
  phrasing_intents:
  - id: postBinaryApplicationContentResource
    intent: Upload a build for an application
    question: How do I deploy a new zip of my web app or microservice?
  - id: getBinaryApplicationContentResource
    intent: List an application's uploaded builds
    question: Which build archives have been uploaded for an application?
  phrasing_ops: 2
  slug: cumulocity-application-binaries-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Applications API from Cumulocity — 2 operation(s) for applications.
  name: Cumulocity Applications API
  phrasing_intents:
  - id: postApplicationCollectionResource
    intent: Register a new application
    question: How do I register a new web app or microservice in Cumulocity?
  - id: getAbstractApplicationCollectionResource
    intent: List applications in the tenant
    question: Which applications and microservices are available in my tenant?
  - id: getApplicationResource
    intent: Look up one application by ID
    question: How do I get the details of a specific application?
  - id: putApplicationResource
    intent: Change an application's settings
    question: Can I rename an existing application or change its availability?
  - id: deleteApplicationResource
    intent: Delete an application
    question: How do I remove an application from my tenant entirely?
  phrasing_ops: 5
  slug: cumulocity-applications-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Asset Instances API from Cumulocity — 2 operation(s) for asset instances.
  name: Cumulocity Asset Instances API
  phrasing_intents:
  - id: listAssetInstances
    intent: List digital twin asset instances
    question: Which asset instances exist in my digital twin model?
  - id: createAssetInstance
    intent: Create an asset instance from a model
    question: How do I create a new asset from an asset model in the digital twin manager?
  - id: getAssetInstance
    intent: Look up one asset instance
    question: How do I see the properties and children of a single asset instance?
  - id: updateAssetInstance
    intent: Change an asset instance
    question: Can I rename an asset instance or move it under a different parent?
  - id: deleteAssetInstance
    intent: Delete an asset instance
    question: How do I remove an asset instance from the digital twin?
  phrasing_ops: 5
  slug: cumulocity-asset-instances-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Asset Models API from Cumulocity — 2 operation(s) for asset models.
  name: Cumulocity Asset Models API
  phrasing_intents:
  - id: listAssetModels
    intent: List digital twin asset models
    question: What asset models are defined in my digital twin manager?
  - id: createAssetModel
    intent: Define a new asset model
    question: How do I define a new asset type with its own properties?
  - id: getAssetModel
    intent: Look up one asset model
    question: How do I see the property definitions of one asset model?
  - id: updateAssetModel
    intent: Change an asset model definition
    question: Can I add properties to an asset model that already exists?
  - id: deleteAssetModel
    intent: Delete an asset model
    question: How do I remove an asset model I no longer need?
  phrasing_ops: 5
  slug: cumulocity-asset-models-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: Binary attachments associated with managed objects.
  name: Cumulocity Binaries API
  phrasing_intents:
  - id: postBinariesCollectionResource
    intent: Upload a file to the inventory
    question: How do I upload a firmware image or config file?
  - id: getBinariesCollectionResource
    intent: List stored files
    question: What files are stored in the inventory binary repository?
  - id: getBinariesResource
    intent: Download a stored file
    question: How do I download a file I uploaded earlier?
  - id: deleteBinariesResource
    intent: Delete a stored file
    question: How do I delete an old firmware file from storage?
  phrasing_ops: 4
  slug: cumulocity-binaries-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Bulk Operations API from Cumulocity — 2 operation(s) for bulk operations.
  name: Cumulocity Bulk Operations API
  phrasing_intents:
  - id: postBulkOperationCollectionResource
    intent: Send one operation to a whole device group
    question: How do I send the same command to every device in a group?
  - id: getBulkOperationCollectionResource
    intent: List bulk device operations
    question: Which bulk operations have been scheduled across device groups?
  - id: getBulkOperationResource
    intent: Look up one bulk operation
    question: How do I check the progress of a single bulk operation?
  - id: putBulkOperationResource
    intent: Reschedule or change a bulk operation
    question: Can I change the start date of a bulk operation that hasn't run yet?
  - id: deleteBulkOperationResource
    intent: Delete a bulk operation
    question: How do I cancel and remove a scheduled bulk operation?
  phrasing_ops: 5
  slug: cumulocity-bulk-operations-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Cloud Sync API from Cumulocity — 1 operation(s) for cloud sync.
  name: Cumulocity Cloud Sync API
  phrasing_intents:
  - id: getCloudSyncConfiguration
    intent: Read the Edge cloud sync settings
    question: Is my Edge installation syncing data to the cloud tenant?
  - id: updateCloudSyncConfiguration
    intent: Change the Edge cloud sync settings
    question: How do I point my Edge to a cloud tenant for data sync?
  phrasing_ops: 2
  slug: cumulocity-cloud-sync-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Current User API from Cumulocity — 1 operation(s) for current user.
  name: Cumulocity Current User API
  phrasing_intents:
  - id: getCurrentUserResource
    intent: Show the signed-in user's profile
    question: Who am I logged in as, and what roles do I have?
  - id: putCurrentUserResource
    intent: Update my own user profile
    question: How do I change my own password or email?
  phrasing_ops: 2
  slug: cumulocity-current-user-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Device Credentials API from Cumulocity — 1 operation(s) for device credentials.
  name: Cumulocity Device Credentials API
  phrasing_intents:
  - id: postDeviceCredentialsCollectionResource
    intent: Request credentials for a new device
    question: How does an unprovisioned device poll for its credentials?
  phrasing_ops: 1
  slug: cumulocity-device-credentials-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Events API from Cumulocity — 2 operation(s) for events.
  name: Cumulocity Events API
  phrasing_intents:
  - id: postEventCollectionResource
    intent: Record a new event for a device
    question: How do I log a custom event for a device in Cumulocity?
  - id: getEventCollectionResource
    intent: List events recorded for devices
    question: What events has a particular device reported recently?
  - id: deleteEventCollectionResource
    intent: Delete events matching a filter
    question: Can I bulk delete a set of events by filter?
  - id: getEventResource
    intent: Look up a single event by ID
    question: How do I read the details of one event by its ID?
  - id: putEventResource
    intent: Change the text or details of an event
    question: Can I edit the text of an event that was already recorded?
  - id: deleteEventResource
    intent: Delete one event by ID
    question: How do I remove a single event that was logged by mistake?
  phrasing_ops: 6
  slug: cumulocity-events-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The External IDs API from Cumulocity — 2 operation(s) for external ids.
  name: Cumulocity External IDs API
  phrasing_intents:
  - id: postExternalIDCollectionResource
    intent: Link an external ID to a device
    question: How do I register a device's serial number as an external ID?
  - id: getExternalIDCollectionResource
    intent: List all external IDs of a device
    question: What serial numbers and other identifiers are linked to one device?
  - id: getExternalIDResource
    intent: Find a device by its external ID
    question: How do I find a device using its serial number or IMEI?
  - id: deleteExternalIDResource
    intent: Remove an external ID mapping
    question: How do I unlink a serial number from a device?
  phrasing_ops: 4
  slug: cumulocity-external-ids-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Groups API from Cumulocity — 2 operation(s) for groups.
  name: Cumulocity Groups API
  phrasing_intents:
  - id: postGroupCollectionResource
    intent: Create a user group
    question: How do I create a new user group with its own roles?
  - id: getGroupCollectionResource
    intent: List user groups in a tenant
    question: Which user groups exist in my tenant?
  - id: getGroupByIdResource
    intent: Look up one user group
    question: How do I see which roles and users belong to one group?
  - id: putGroupByIdResource
    intent: Change a user group
    question: Can I rename a user group or change its description?
  - id: deleteGroupByIdResource
    intent: Delete a user group
    question: How do I delete a user group that is no longer used?
  phrasing_ops: 5
  slug: cumulocity-groups-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: Inventory documents representing devices, assets, groups, and digital twins.
  name: Cumulocity Managed Objects API
  phrasing_intents:
  - id: postManagedObjectCollectionResource
    intent: Register a device or asset in the inventory
    question: How do I register a new device in the inventory?
  - id: getManagedObjectCollectionResource
    intent: Search the device and asset inventory
    question: How do I list all devices in my Cumulocity inventory?
  - id: getManagedObjectResource
    intent: Look up one device or asset
    question: How do I fetch one device's inventory record by ID?
  - id: putManagedObjectResource
    intent: Change a device or asset record
    question: How do I rename a device in the inventory?
  - id: deleteManagedObjectResource
    intent: Delete a device or asset
    question: How do I remove a device from the inventory?
  phrasing_ops: 5
  slug: cumulocity-managed-objects-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Measurements API from Cumulocity — 2 operation(s) for measurements.
  name: Cumulocity Measurements API
  phrasing_intents:
  - id: postMeasurementCollectionResource
    intent: Send a new measurement reading
    question: How do I push a sensor reading into Cumulocity?
  - id: getMeasurementCollectionResource
    intent: List sensor measurements
    question: What temperature readings did a device send yesterday?
  - id: deleteMeasurementCollectionResource
    intent: Delete measurements matching a filter
    question: Can I delete all measurements from a device for a date range?
  - id: getMeasurementResource
    intent: Look up one measurement
    question: How do I read a single measurement by its ID?
  - id: deleteMeasurementResource
    intent: Delete one measurement
    question: How do I remove one bad sensor reading?
  phrasing_ops: 5
  slug: cumulocity-measurements-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The New Device Requests API from Cumulocity — 2 operation(s) for new device requests.
  name: Cumulocity New Device Requests API
  phrasing_intents:
  - id: postNewDeviceRequestCollectionResource
    intent: Start registering a new device
    question: How do I start registering a device by its serial ID?
  - id: getNewDeviceRequestCollectionResource
    intent: List pending device registrations
    question: Which devices are waiting for registration approval?
  phrasing_ops: 2
  slug: cumulocity-new-device-requests-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Offload Configurations API from Cumulocity — 2 operation(s) for offload configurations.
  name: Cumulocity Offload Configurations API
  phrasing_intents:
  - id: listOffloadConfigurations
    intent: List DataHub offload configurations
    question: Which DataHub offloading pipelines are configured?
  - id: createOffloadConfiguration
    intent: Set up a new DataHub offload pipeline
    question: How do I start offloading alarms or measurements to the data lake?
  - id: getOffloadConfiguration
    intent: Look up one offload configuration
    question: How do I see the filter and schedule of one offload pipeline?
  - id: updateOffloadConfiguration
    intent: Change an offload pipeline
    question: Can I change the schedule of an existing offload pipeline?
  - id: deleteOffloadConfiguration
    intent: Delete an offload pipeline
    question: How do I remove an offload pipeline I no longer need?
  phrasing_ops: 5
  slug: cumulocity-offload-configurations-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Offload Jobs API from Cumulocity — 1 operation(s) for offload jobs.
  name: Cumulocity Offload Jobs API
  phrasing_intents:
  - id: listOffloadJobs
    intent: List runs of an offload pipeline
    question: Did my DataHub offload pipeline run successfully last night?
  - id: startOffloadJob
    intent: Run an offload pipeline now
    question: Can I trigger an offload run manually instead of waiting for the schedule?
  phrasing_ops: 2
  slug: cumulocity-offload-jobs-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Operations API from Cumulocity — 2 operation(s) for operations.
  name: Cumulocity Operations API
  phrasing_intents:
  - id: postOperationCollectionResource
    intent: Send a command to a device
    question: How do I send a restart command to a device remotely?
  - id: getOperationCollectionResource
    intent: List device operations
    question: Which commands are still pending for a particular device?
  - id: deleteOperationCollectionResource
    intent: Delete operations matching a filter
    question: Can I clear out a batch of old device operations at once?
  - id: getOperationResource
    intent: Look up one device operation
    question: How do I check whether a command I sent has succeeded?
  - id: putOperationResource
    intent: Report progress on a device operation
    question: How does a device agent mark an operation as executing or successful?
  phrasing_ops: 5
  slug: cumulocity-operations-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Queries API from Cumulocity — 1 operation(s) for queries.
  name: Cumulocity Queries API
  phrasing_intents:
  - id: runQuery
    intent: Run a SQL query over offloaded data
    question: Can I run SQL against data offloaded to DataHub?
  phrasing_ops: 1
  slug: cumulocity-queries-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Retention Rules API from Cumulocity — 2 operation(s) for retention rules.
  name: Cumulocity Retention Rules API
  phrasing_intents:
  - id: postRetentionRuleCollectionResource
    intent: Add a data retention rule
    question: How do I make old measurements expire after a number of days?
  - id: getRetentionRuleCollectionResource
    intent: List data retention rules
    question: What data retention rules are set on my tenant?
  - id: getRetentionRuleResource
    intent: Look up one retention rule
    question: How do I see the details of one retention rule?
  - id: putRetentionRuleResource
    intent: Change a data retention rule
    question: Can I change how many days an existing retention rule keeps data?
  - id: deleteRetentionRuleResource
    intent: Delete a data retention rule
    question: How do I remove a retention rule so data is no longer auto-deleted by it?
  phrasing_ops: 5
  slug: cumulocity-retention-rules-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Roles API from Cumulocity — 1 operation(s) for roles.
  name: Cumulocity Roles API
  phrasing_intents:
  - id: getRoleCollectionResource
    intent: List global user roles
    question: Which roles can I assign to users and groups?
  phrasing_ops: 1
  slug: cumulocity-roles-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Software Updates API from Cumulocity — 1 operation(s) for software updates.
  name: Cumulocity Software Updates API
  phrasing_intents:
  - id: listEdgeUpdates
    intent: List available Edge updates
    question: Are there new versions available for my Edge installation?
  - id: installEdgeUpdate
    intent: Install an Edge update
    question: How do I upgrade my Edge installation to a newer version?
  phrasing_ops: 2
  slug: cumulocity-software-updates-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Subscriptions API from Cumulocity — 2 operation(s) for subscriptions.
  name: Cumulocity Subscriptions API
  phrasing_intents:
  - id: postNotificationSubscriptionResource
    intent: Subscribe to device or tenant notifications
    question: How do I subscribe to real-time notifications for a device?
  - id: getNotificationSubscriptionCollectionResource
    intent: List Notification 2.0 subscriptions
    question: Which notification subscriptions exist for my devices?
  - id: deleteNotificationSubscriptionBySourceResource
    intent: Delete subscriptions matching a filter
    question: Can I remove all my notification subscriptions in one go?
  - id: getNotificationSubscriptionResource
    intent: Look up one notification subscription
    question: How do I see the filter and context of one subscription?
  - id: deleteNotificationSubscriptionResource
    intent: Delete one notification subscription
    question: How do I stop one notification subscription?
  phrasing_ops: 5
  slug: cumulocity-subscriptions-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The System API from Cumulocity — 2 operation(s) for system.
  name: Cumulocity System API
  phrasing_intents:
  - id: getEdgeSystemStatus
    intent: Check the Edge system status
    question: Is my Edge system healthy right now?
  - id: restartEdge
    intent: Restart the Edge system
    question: How do I restart my Edge system remotely?
  phrasing_ops: 2
  slug: cumulocity-system-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Tenants API from Cumulocity — 2 operation(s) for tenants.
  name: Cumulocity Tenants API
  phrasing_intents:
  - id: postTenantCollectionResource
    intent: Create a subtenant
    question: How do I create a new customer tenant with its own admin?
  - id: getTenantCollectionResource
    intent: List subtenants
    question: Which subtenants exist under my enterprise tenant?
  - id: getTenantResource
    intent: Look up one tenant
    question: How do I see the details of one subtenant?
  - id: putTenantResource
    intent: Change a tenant's details
    question: Can I suspend a subtenant or change its contact details?
  - id: deleteTenantResource
    intent: Delete a tenant
    question: How do I permanently remove a subtenant?
  phrasing_ops: 5
  slug: cumulocity-tenants-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Tokens API from Cumulocity — 2 operation(s) for tokens.
  name: Cumulocity Tokens API
  phrasing_intents:
  - id: postNotificationTokenResource
    intent: Get a token to consume a subscription
    question: How do I get a token to connect to a notification subscription?
  - id: postNotificationTokenUnsubscribeResource
    intent: Invalidate a subscription token
    question: How do I unsubscribe a consumer and invalidate its token?
  phrasing_ops: 2
  slug: cumulocity-tokens-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Users API from Cumulocity — 2 operation(s) for users.
  name: Cumulocity Users API
  phrasing_intents:
  - id: postUserCollectionResource
    intent: Create a user account
    question: How do I add a new user to my tenant?
  - id: getUserCollectionResource
    intent: List users in a tenant
    question: Who are all the users in my tenant?
  - id: getUserResource
    intent: Look up one user
    question: How do I see a user's roles and groups?
  - id: putUserResource
    intent: Change another user's account
    question: Can I disable a user account without deleting it?
  - id: deleteUserResource
    intent: Delete a user account
    question: How do I remove a user who has left the company?
  phrasing_ops: 5
  slug: cumulocity-users-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: The alarm API resource returns URIs and URI templates to collections of alarms, so that all alarms or alarms of a specified source device and/or status can be retrieved.
  name: Cumulocity Alarm API
  slug: cumulocity-alarm-api-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: The application API resource returns URIs and URI templates to collections of applications so that all applications with a particular name and all applications owned by particular tenant can be querie
  name: Cumulocity Application API
  slug: cumulocity-application-api-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: API methods to retrieve, create, update and delete application versions.
  name: Cumulocity Application versions API
  slug: cumulocity-application-versions-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: It is possible to store, retrieve and delete binaries for events. Each event can have only one binary attached.
  name: Cumulocity Attachments API
  slug: cumulocity-attachments-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: The audit API resource returns URIs and URI templates to collections of audit records, so that they can be retrieved by criteria such as “all records from a particular user”, or “all records from a pa
  name: Cumulocity Audit API
  slug: cumulocity-audit-api-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: An audit log stores events that are security-relevant and should be stored for auditing. For example, an audit log should be generated when a user logs into a gateway. An audit log extends an event th
  name: Cumulocity Audits API
  slug: cumulocity-audits-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: API methods to retrieve the bootstrap user of an application.
  name: Cumulocity Bootstrap user API
  slug: cumulocity-bootstrap-user-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: API to create a new CA certificate for tenant in Cumulocity.
  name: Cumulocity Certificate authority API
  slug: cumulocity-certificate-authority-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: Managed objects can contain collections of references to child devices, additions and assets. > **&#9432; Info:** The Accept header should be provided in all POST requests, otherwise an empty response
  name: Cumulocity Child operations API
  slug: cumulocity-child-operations-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: API methods to retrieve and update the current application and to retrieve its subscribers. It is the authenticated microservice user's application.
  name: Cumulocity Current application API
  slug: cumulocity-current-application-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: The device control API resource returns URIs and URI templates to collections of operations so that they can be retrieved. > **&#9432; Info:** In order to create/retrieve/update an operation for a dev
  name: Cumulocity Device control API
  slug: cumulocity-device-control-api-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: Device enroll API to be used by a device to issue an X509 certificate signed by tenant's [certificate authority](#operation/postBulkNewDeviceRequestCollectionResource). The identifier and enrollment O
  name: Cumulocity Device enrollment API
  slug: cumulocity-device-enrollment-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: API methods to retrieve and update device permissions assignments. Device permissions enable users to access and manipulate devices. The device permission structure is **[API:fragment_name:permission]
  name: Cumulocity Device Permissions API
  slug: cumulocity-device-permissions-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: Device statistics are collected for each inventory object with at least one measurement, event or alarm. There are no additional checks if the inventory object is marked as device using the `c8y_IsDev
  name: Cumulocity Device statistics API
  slug: cumulocity-device-statistics-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: The event API resource returns URIs and URI templates to collections of events, so that all events or events of a specified type and/or source device can be retrieved.
  name: Cumulocity Event API
  slug: cumulocity-event-api-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: The Feature toggles API API from Cumulocity — 4 operation(s) for feature toggles api.
  name: Cumulocity Feature toggles API
  slug: cumulocity-feature-toggles-api-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: Cumulocity can associate devices and assets with multiple external identities. For instance, devices can often be identified by the IMEI of their modem, by a micro-controller serial number or by an as
  name: Cumulocity Identity API
  slug: cumulocity-identity-api-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: The inventory stores all master data related to devices, their configuration and their connections. It also contains all related assets (for example, vehicles, machines, buildings) and their structure
  name: Cumulocity Inventory API
  slug: cumulocity-inventory-api-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: API methods to create, retrieve, update and delete inventory roles. > **&#9432; Info:** The Accept header should be provided in all POST/PUT requests, otherwise an empty response body will be returned
  name: Cumulocity Inventory Roles API
  slug: cumulocity-inventory-roles-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: API methods to retrieve the login options configured in the tenant. More detailed information about the parameters and their meaning can be found in [Platform administration > Authentication](https://
  name: Cumulocity Login options API
  slug: cumulocity-login-options-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: API methods to obtain access tokens to the Cumulocity platform in case of OAI-Secure or SSO authentication.
  name: Cumulocity Login tokens API
  slug: cumulocity-login-tokens-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: The measurement API resource returns URIs and URI templates to collections of measurements, so that all measurements can be filtered and retrieved. Querying without filters can be slow, hence it is re
  name: Cumulocity Measurement API
  slug: cumulocity-measurement-api-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: The notification 2.0 API resource returns URIs and URI templates to collections of notifications, so that all notifications or notifications of a specified context and/or source device can be retrieve
  name: Cumulocity Notification 2.0 API
  slug: cumulocity-notification-2-0-api-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: API methods to retrieve the options configured in the tenant. > **&#9432; Info:** The Accept header should be provided in all POST/PUT requests, otherwise an empty response body will be returned.
  name: Cumulocity Options API
  slug: cumulocity-options-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: To discover the URIs of the various interfaces of Cumulocity, a platform interface is provided. This interface aggregates all the underlying API resources.
  name: Cumulocity Platform API
  slug: cumulocity-platform-api-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: '# Real-time operations Real-time notification services of Cumulocity have their own subscription channel name format and URL. The real-time notifications are available for [Alarms](#tag/Alarm-notifica'
  name: Cumulocity Real-time notification API
  slug: cumulocity-real-time-notification-api-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: API methods to retrieve the read-only properties predefined in the platform's configuration. For security reasons, a few system options are considered secured, which means the user must have the requi
  name: Cumulocity System options API
  slug: cumulocity-system-options-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: The tenant API resource returns URIs and URI templates to collections of tenants, so that all tenants can be filtered and retrieved.
  name: Cumulocity Tenant API
  slug: cumulocity-tenant-api-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: References to the tenant subscribed applications. > **&#9432; Info:** The Accept header should be provided in all POST requests, otherwise an empty response body will be returned.
  name: Cumulocity Tenant applications API
  slug: cumulocity-tenant-applications-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: API methods for managing trusted certificates used to establish device connections via MQTT. More detailed information about trusted certificates and their role can be found in [Device management > De
  name: Cumulocity Trusted certificates API
  slug: cumulocity-trusted-certificates-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: Days are counted according to server timezone, so be aware that the tenant usage statistics displaying/filtering may not work correctly when the client is not in the same timezone as the server. Howev
  name: Cumulocity Usage statistics API
  slug: cumulocity-usage-statistics-api
- baseURL: mqtt://{tenant}.cumulocity.com:1883
  baseurl_source: declared
  description: The user API resource returns URIs and URI templates to collections of users, groups, and roles, so that they can be queried.
  name: Cumulocity User API
  slug: cumulocity-user-api-api
artifact_total: 209
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
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cumulocity.com/pricing/
- group: company
  title: ''
  type: Website
  url: https://www.cumulocity.com/
- group: other
  href: https://artifacts.apis.io/cumulocity/capabilities/cumulocity-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cumulocity-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cumulocity/overview
- group: agent
  href: https://artifacts.apis.io/cumulocity/agentic-access/cumulocity-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cumulocity-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cumulocity/security/cumulocity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cumulocity-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cumulocity/authentication/cumulocity-authentication.yml
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
  href: https://artifacts.apis.io/cumulocity/plans/cumulocity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cumulocity-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cumulocity/rate-limits/cumulocity-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cumulocity-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cumulocity/finops/cumulocity-finops.yml
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
- has_sources: true
  method: derived
  name: Cumulocity Finops
  primary_unit: subscription
  service_category: ''
  slug: cumulocity-finops
  template: false
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
overview: 'Cumulocity publishes 62 API contracts indexed on the [APIs.io](https://apis.io/) network, including MQTT and SmartREST API, MQTT Service API, Alarms API, and 59 more. Tagged areas include IoT, Industrial IoT, AIoT, Device Management, and Digital Twin.


  The Cumulocity catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Cumulocity''s developer surface includes pricing, authentication, developer portal, documentation, getting-started guide, changelog, support, and 65 more developer resources.'
plans:
- name: Cumulocity Plans Pricing
  plan_count: 5
  slug: cumulocity-plans-pricing
- name: Cumulocity Price Estimates
  plan_count: 0
  slug: cumulocity-price-estimates
random_paper: 22
rate_limits:
- limit_count: 0
  name: Cumulocity Rate Limits
  slug: cumulocity-rate-limits
rules:
- authorship: generated
  effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Cumulocity — asyncapi rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: cumulocity-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Cumulocity — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cumulocity-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 53
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
  band: exemplar
  composite: 70.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 79.5
    catalog_earned_first_party: 12.0
    catalog_gap: 35.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 86.8
    contract_governance: 13.6
    contract_quality: 73.1
    developer_ergonomics: 63.1
    discoverability: 73.2
    operational_transparency: 47.4
  previous_composite: 71.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 46.6
      derived: 0
      marker_coverage: 50.5
      total: 103
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/cumulocity/cumulocity-2026-06-20T175331.png
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
- Industrial IoT
- AIoT
- Device Management
- Digital Twin
- MQTT
- Edge Computing
- Streaming Analytics
- Data Lake
- Real-Time
website: https://www.cumulocity.com/
---
