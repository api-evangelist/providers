---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
  schema_version: '0.2'
  score: 22.1
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 72
  human_in_the_loop: 10
  name: Cumulocity Agentic Access
  operation_count: 128
  slug: cumulocity-agentic-access
  summary_line: 128 operations · 72 acting · 10 human-in-the-loop
api_count: 17
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
  - id: listAlarms
    intent: List alarms raised on devices
    question: Which alarms are currently active on my Cumulocity devices?
  - id: createAlarm
    intent: Raise a new alarm for a device
    question: How can I raise an alarm against a device from my own code?
  - id: bulkUpdateAlarms
    intent: Update many alarms at once by filter
    question: How do I acknowledge every active alarm on a device in one call?
  - id: deleteAlarms
    intent: Delete alarms matching a filter
    question: Is there a way to purge a whole batch of old alarms by filter?
  - id: getAlarm
    intent: Look up a single alarm by ID
    question: How do I fetch the full details of one alarm by its ID?
  - id: updateAlarm
    intent: Change the status or text of one alarm
    question: How do I acknowledge or clear one specific alarm?
  phrasing_ops: 6
  slug: cumulocity-alarms-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Application Binaries API from Cumulocity — 1 operation(s) for application binaries.
  name: Cumulocity Application Binaries API
  phrasing_intents:
  - id: listApplicationBinaries
    intent: List an application's uploaded builds
    question: Which build archives have been uploaded for an application?
  - id: uploadApplicationBinary
    intent: Upload a build for an application
    question: How do I deploy a new zip of my web app or microservice?
  phrasing_ops: 2
  slug: cumulocity-application-binaries-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Applications API from Cumulocity — 2 operation(s) for applications.
  name: Cumulocity Applications API
  phrasing_intents:
  - id: listApplications
    intent: List applications in the tenant
    question: Which applications and microservices are available in my tenant?
  - id: createApplication
    intent: Register a new application
    question: How do I register a new web app or microservice in Cumulocity?
  - id: getApplication
    intent: Look up one application by ID
    question: How do I get the details of a specific application?
  - id: updateApplication
    intent: Change an application's settings
    question: Can I rename an existing application or change its availability?
  - id: deleteApplication
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
  description: The Audit Records API from Cumulocity — 2 operation(s) for audit records.
  name: Cumulocity Audit Records API
  phrasing_intents:
  - id: listAuditRecords
    intent: List audit log records
    question: Who changed what in my tenant last week?
  - id: createAuditRecord
    intent: Write a custom audit log entry
    question: How do I write my own entry into the audit log?
  - id: getAuditRecord
    intent: Look up one audit record
    question: How do I see the full details of one audit entry?
  phrasing_ops: 3
  slug: cumulocity-audit-records-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Bayeux Handshake API from Cumulocity — 1 operation(s) for bayeux handshake.
  name: Cumulocity Bayeux Handshake API
  phrasing_intents:
  - id: bayeuxChannelEndpoint
    intent: Exchange real-time Bayeux messages
    question: How do I start a real-time CometD session with a handshake?
  phrasing_ops: 1
  slug: cumulocity-bayeux-handshake-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: Binary attachments associated with managed objects.
  name: Cumulocity Binaries API
  phrasing_intents:
  - id: listBinaries
    intent: List stored files
    question: What files are stored in the inventory binary repository?
  - id: uploadBinary
    intent: Upload a file to the inventory
    question: How do I upload a firmware image or config file?
  - id: getBinary
    intent: Download a stored file
    question: How do I download a file I uploaded earlier?
  - id: deleteBinary
    intent: Delete a stored file
    question: How do I delete an old firmware file from storage?
  phrasing_ops: 4
  slug: cumulocity-binaries-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Bootstrap Users API from Cumulocity — 1 operation(s) for bootstrap users.
  name: Cumulocity Bootstrap Users API
  phrasing_intents:
  - id: getBootstrapUser
    intent: Get a microservice's bootstrap credentials
    question: How does my microservice get its bootstrap user credentials?
  phrasing_ops: 1
  slug: cumulocity-bootstrap-users-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Bulk Operations API from Cumulocity — 2 operation(s) for bulk operations.
  name: Cumulocity Bulk Operations API
  phrasing_intents:
  - id: listBulkOperations
    intent: List bulk device operations
    question: Which bulk operations have been scheduled across device groups?
  - id: createBulkOperation
    intent: Send one operation to a whole device group
    question: How do I send the same command to every device in a group?
  - id: getBulkOperation
    intent: Look up one bulk operation
    question: How do I check the progress of a single bulk operation?
  - id: updateBulkOperation
    intent: Reschedule or change a bulk operation
    question: Can I change the start date of a bulk operation that hasn't run yet?
  - id: deleteBulkOperation
    intent: Delete a bulk operation
    question: How do I cancel and remove a scheduled bulk operation?
  phrasing_ops: 5
  slug: cumulocity-bulk-operations-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: Hierarchical relationships between managed objects.
  name: Cumulocity Child References API
  phrasing_intents:
  - id: listChildDevices
    intent: List a device's child devices
    question: Which child devices are connected under a gateway?
  - id: addChildDevice
    intent: Attach a child device to a parent
    question: How do I put a device under a gateway or group?
  - id: listChildAssets
    intent: List a managed object's child assets
    question: What assets sit under a particular asset or group in the hierarchy?
  - id: listChildAdditions
    intent: List a managed object's child additions
    question: What child additions are attached to a managed object?
  phrasing_ops: 4
  slug: cumulocity-child-references-api
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
  - id: getCurrentUser
    intent: Show the signed-in user's profile
    question: Who am I logged in as, and what roles do I have?
  - id: updateCurrentUser
    intent: Update my own user profile
    question: How do I change my own password or email?
  phrasing_ops: 2
  slug: cumulocity-current-user-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Device Credentials API from Cumulocity — 1 operation(s) for device credentials.
  name: Cumulocity Device Credentials API
  phrasing_intents:
  - id: requestDeviceCredentials
    intent: Request credentials for a new device
    question: How does an unprovisioned device poll for its credentials?
  phrasing_ops: 1
  slug: cumulocity-device-credentials-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Event Binaries API from Cumulocity — 1 operation(s) for event binaries.
  name: Cumulocity Event Binaries API
  phrasing_intents:
  - id: getEventBinary
    intent: Download a file attached to an event
    question: How do I download the file attached to an event?
  - id: attachEventBinary
    intent: Attach a file to an event
    question: How do I attach a photo or log file to an event?
  - id: deleteEventBinary
    intent: Remove the file attached to an event
    question: How do I remove the attachment from an event but keep the event?
  phrasing_ops: 3
  slug: cumulocity-event-binaries-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Events API from Cumulocity — 2 operation(s) for events.
  name: Cumulocity Events API
  phrasing_intents:
  - id: listEvents
    intent: List events recorded for devices
    question: What events has a particular device reported recently?
  - id: createEvent
    intent: Record a new event for a device
    question: How do I log a custom event for a device in Cumulocity?
  - id: deleteEvents
    intent: Delete events matching a filter
    question: Can I bulk delete a set of events by filter?
  - id: getEvent
    intent: Look up a single event by ID
    question: How do I read the details of one event by its ID?
  - id: updateEvent
    intent: Change the text or details of an event
    question: Can I edit the text of an event that was already recorded?
  - id: deleteEvent
    intent: Delete one event by ID
    question: How do I remove a single event that was logged by mistake?
  phrasing_ops: 6
  slug: cumulocity-events-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The External IDs API from Cumulocity — 2 operation(s) for external ids.
  name: Cumulocity External IDs API
  phrasing_intents:
  - id: getExternalId
    intent: Find a device by its external ID
    question: How do I find a device using its serial number or IMEI?
  - id: deleteExternalId
    intent: Remove an external ID mapping
    question: How do I unlink a serial number from a device?
  - id: listExternalIdsForGlobalId
    intent: List all external IDs of a device
    question: What serial numbers and other identifiers are linked to one device?
  - id: createExternalId
    intent: Link an external ID to a device
    question: How do I register a device's serial number as an external ID?
  phrasing_ops: 4
  slug: cumulocity-external-ids-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Groups API from Cumulocity — 2 operation(s) for groups.
  name: Cumulocity Groups API
  phrasing_intents:
  - id: listGroups
    intent: List user groups in a tenant
    question: Which user groups exist in my tenant?
  - id: createGroup
    intent: Create a user group
    question: How do I create a new user group with its own roles?
  - id: getGroup
    intent: Look up one user group
    question: How do I see which roles and users belong to one group?
  - id: updateGroup
    intent: Change a user group
    question: Can I rename a user group or change its description?
  - id: deleteGroup
    intent: Delete a user group
    question: How do I delete a user group that is no longer used?
  phrasing_ops: 5
  slug: cumulocity-groups-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: Inventory documents representing devices, assets, groups, and digital twins.
  name: Cumulocity Managed Objects API
  phrasing_intents:
  - id: listManagedObjects
    intent: Search the device and asset inventory
    question: How do I list all devices in my Cumulocity inventory?
  - id: createManagedObject
    intent: Register a device or asset in the inventory
    question: How do I register a new device in the inventory?
  - id: getManagedObject
    intent: Look up one device or asset
    question: How do I fetch one device's inventory record by ID?
  - id: updateManagedObject
    intent: Change a device or asset record
    question: How do I rename a device in the inventory?
  - id: deleteManagedObject
    intent: Delete a device or asset
    question: How do I remove a device from the inventory?
  phrasing_ops: 5
  slug: cumulocity-managed-objects-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Measurements API from Cumulocity — 2 operation(s) for measurements.
  name: Cumulocity Measurements API
  phrasing_intents:
  - id: listMeasurements
    intent: List sensor measurements
    question: What temperature readings did a device send yesterday?
  - id: createMeasurement
    intent: Send a new measurement reading
    question: How do I push a sensor reading into Cumulocity?
  - id: deleteMeasurements
    intent: Delete measurements matching a filter
    question: Can I delete all measurements from a device for a date range?
  - id: getMeasurement
    intent: Look up one measurement
    question: How do I read a single measurement by its ID?
  - id: deleteMeasurement
    intent: Delete one measurement
    question: How do I remove one bad sensor reading?
  phrasing_ops: 5
  slug: cumulocity-measurements-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The New Device Requests API from Cumulocity — 2 operation(s) for new device requests.
  name: Cumulocity New Device Requests API
  phrasing_intents:
  - id: listNewDeviceRequests
    intent: List pending device registrations
    question: Which devices are waiting for registration approval?
  - id: createNewDeviceRequest
    intent: Start registering a new device
    question: How do I start registering a device by its serial ID?
  - id: getNewDeviceRequest
    intent: Check one device registration request
    question: What is the status of a particular device registration request?
  - id: updateNewDeviceRequest
    intent: Accept or reject a device registration
    question: How do I accept a device that's waiting to be registered?
  - id: deleteNewDeviceRequest
    intent: Delete a device registration request
    question: How do I cancel a device registration I started?
  phrasing_ops: 5
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
  - id: listOperations
    intent: List device operations
    question: Which commands are still pending for a particular device?
  - id: createOperation
    intent: Send a command to a device
    question: How do I send a restart command to a device remotely?
  - id: deleteOperations
    intent: Delete operations matching a filter
    question: Can I clear out a batch of old device operations at once?
  - id: getOperation
    intent: Look up one device operation
    question: How do I check whether a command I sent has succeeded?
  - id: updateOperation
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
  - id: listRetentionRules
    intent: List data retention rules
    question: What data retention rules are set on my tenant?
  - id: createRetentionRule
    intent: Add a data retention rule
    question: How do I make old measurements expire after a number of days?
  - id: getRetentionRule
    intent: Look up one retention rule
    question: How do I see the details of one retention rule?
  - id: updateRetentionRule
    intent: Change a data retention rule
    question: Can I change how many days an existing retention rule keeps data?
  - id: deleteRetentionRule
    intent: Delete a data retention rule
    question: How do I remove a retention rule so data is no longer auto-deleted by it?
  phrasing_ops: 5
  slug: cumulocity-retention-rules-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Roles API from Cumulocity — 1 operation(s) for roles.
  name: Cumulocity Roles API
  phrasing_intents:
  - id: listRoles
    intent: List global user roles
    question: Which roles can I assign to users and groups?
  phrasing_ops: 1
  slug: cumulocity-roles-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Series API from Cumulocity — 1 operation(s) for series.
  name: Cumulocity Series API
  phrasing_intents:
  - id: getSeries
    intent: Get aggregated measurement series
    question: How do I get hourly or daily averages of a sensor series?
  phrasing_ops: 1
  slug: cumulocity-series-api
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
  - id: listSubscriptions
    intent: List Notification 2.0 subscriptions
    question: Which notification subscriptions exist for my devices?
  - id: createSubscription
    intent: Subscribe to device or tenant notifications
    question: How do I subscribe to real-time notifications for a device?
  - id: deleteSubscriptions
    intent: Delete subscriptions matching a filter
    question: Can I remove all my notification subscriptions in one go?
  - id: getSubscription
    intent: Look up one notification subscription
    question: How do I see the filter and context of one subscription?
  - id: deleteSubscription
    intent: Delete one notification subscription
    question: How do I stop one notification subscription?
  phrasing_ops: 5
  slug: cumulocity-subscriptions-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: Discover the measurement types reported against a managed object.
  name: Cumulocity Supported Measurements API
  phrasing_intents:
  - id: listSupportedMeasurements
    intent: List measurement types a device reports
    question: What kinds of measurements does a device send?
  - id: listSupportedSeries
    intent: List measurement series a device reports
    question: Which measurement series can I chart for a device?
  phrasing_ops: 2
  slug: cumulocity-supported-measurements-api
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
  description: The Tenant Options API from Cumulocity — 2 operation(s) for tenant options.
  name: Cumulocity Tenant Options API
  phrasing_intents:
  - id: listTenantOptions
    intent: List tenant configuration options
    question: What configuration options are set on my tenant?
  - id: createTenantOption
    intent: Add a tenant configuration option
    question: How do I store a new configuration value on my tenant?
  - id: getTenantOption
    intent: Read one tenant option
    question: What value is a specific tenant option set to?
  - id: updateTenantOption
    intent: Change a tenant option value
    question: How do I change the value of an existing tenant option?
  - id: deleteTenantOption
    intent: Delete a tenant option
    question: How do I remove a tenant option I no longer use?
  phrasing_ops: 5
  slug: cumulocity-tenant-options-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Tenant Statistics API from Cumulocity — 1 operation(s) for tenant statistics.
  name: Cumulocity Tenant Statistics API
  phrasing_intents:
  - id: listTenantStatistics
    intent: Report tenant usage statistics
    question: How much storage and how many requests has my tenant used this month?
  phrasing_ops: 1
  slug: cumulocity-tenant-statistics-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Tenants API from Cumulocity — 2 operation(s) for tenants.
  name: Cumulocity Tenants API
  phrasing_intents:
  - id: listTenants
    intent: List subtenants
    question: Which subtenants exist under my enterprise tenant?
  - id: createTenant
    intent: Create a subtenant
    question: How do I create a new customer tenant with its own admin?
  - id: getTenant
    intent: Look up one tenant
    question: How do I see the details of one subtenant?
  - id: updateTenant
    intent: Change a tenant's details
    question: Can I suspend a subtenant or change its contact details?
  - id: deleteTenant
    intent: Delete a tenant
    question: How do I permanently remove a subtenant?
  phrasing_ops: 5
  slug: cumulocity-tenants-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Tokens API from Cumulocity — 2 operation(s) for tokens.
  name: Cumulocity Tokens API
  phrasing_intents:
  - id: createToken
    intent: Get a token to consume a subscription
    question: How do I get a token to connect to a notification subscription?
  - id: unsubscribeToken
    intent: Invalidate a subscription token
    question: How do I unsubscribe a consumer and invalidate its token?
  phrasing_ops: 2
  slug: cumulocity-tokens-api
- baseURL: https://{tenant}.cumulocity.com/inventory
  baseurl_source: declared
  description: The Users API from Cumulocity — 2 operation(s) for users.
  name: Cumulocity Users API
  phrasing_intents:
  - id: listUsers
    intent: List users in a tenant
    question: Who are all the users in my tenant?
  - id: createUser
    intent: Create a user account
    question: How do I add a new user to my tenant?
  - id: getUser
    intent: Look up one user
    question: How do I see a user's roles and groups?
  - id: updateUser
    intent: Change another user's account
    question: Can I disable a user account without deleting it?
  - id: deleteUser
    intent: Delete a user account
    question: How do I remove a user who has left the company?
  phrasing_ops: 5
  slug: cumulocity-users-api
artifact_total: 187
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
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cumulocity.com/pricing/
- group: company
  title: ''
  type: Website
  url: https://www.cumulocity.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cumulocity/refs/heads/main/capabilities/cumulocity-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cumulocity-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cumulocity/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cumulocity/refs/heads/main/agentic-access/cumulocity-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cumulocity-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cumulocity/refs/heads/main/security/cumulocity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cumulocity-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cumulocity/refs/heads/main/authentication/cumulocity-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/cumulocity/refs/heads/main/plans/cumulocity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cumulocity-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cumulocity/refs/heads/main/rate-limits/cumulocity-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cumulocity-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cumulocity/refs/heads/main/finops/cumulocity-finops.yml
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
overview: 'Cumulocity publishes 39 APIs on the [APIs.io](https://apis.io/) network, including MQTT and SmartREST API, MQTT Service API, Alarms API, and 36 more. Tagged areas include IoT, Industrial IoT, AIoT, Device Management, and Digital Twin.


  The Cumulocity catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Cumulocity''s developer surface includes pricing, authentication, developer portal, documentation, getting-started guide, changelog, support, and 65 more developer resources.'
plans:
- name: Cumulocity Plans Pricing
  plan_count: 5
  slug: cumulocity-plans-pricing
- name: Cumulocity Price Estimates
  plan_count: 0
  slug: cumulocity-price-estimates
random_paper: 2
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
  band: exemplar
  composite: 67.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 79.5
    catalog_earned_first_party: 12.0
    catalog_gap: 35.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 92.1
    contract_governance: 13.6
    contract_quality: 68.8
    developer_ergonomics: 63.1
    discoverability: 73.2
    operational_transparency: 47.4
  previous_composite: 67.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 91.9
      derived: 0
      marker_coverage: 0.0
      total: 37
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 27.8
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
