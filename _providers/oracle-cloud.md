---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 770
  human_in_the_loop: 45
  name: Oracle Cloud Agentic Access
  operation_count: 1309
  slug: oracle-cloud-agentic-access
  summary_line: 1309 operations · 770 acting · 45 human-in-the-loop
api_count: 9
apis:
- baseURL: https://telemetry.{region}.oraclecloud.com
  baseurl_source: declared
  description: The Alarms API from Oracle Cloud Infrastructure — 2 operation(s) for alarms.
  name: Oracle Cloud Infrastructure Alarms API
  phrasing_intents:
  - id: listAlarms
    intent: List monitoring alarms in a compartment
    question: What monitoring alarms are set up in my compartment?
  - id: createAlarm
    intent: Create a monitoring alarm
    question: How do I create an alarm that fires when a metric query crosses a threshold?
  - id: getAlarm
    intent: Get an alarm's definition
    question: What query and severity does a particular alarm use?
  - id: updateAlarm
    intent: Change an alarm's query, severity or status
    question: How do I disable an alarm without deleting it?
  - id: deleteAlarm
    intent: Delete a monitoring alarm
    question: How do I permanently remove an alarm?
  phrasing_ops: 5
  slug: oracle-cloud-alarms-api
- baseURL: https://objectstorage.{region}.oraclecloud.com
  baseurl_source: declared
  description: The Buckets API from Oracle Cloud Infrastructure — 2 operation(s) for buckets.
  name: Oracle Cloud Infrastructure Buckets API
  phrasing_intents:
  - id: listBuckets
    intent: List the buckets in a compartment
    question: Which storage buckets are in a given Oracle Cloud compartment?
  - id: createBucket
    intent: Create a new storage bucket
    question: How do I make a new bucket to store files?
  - id: getBucket
    intent: Get a bucket's details
    question: What are the current settings of a specific bucket?
  - id: updateBucket
    intent: Update a bucket's settings
    question: Can I rename a bucket or move it to another compartment after creating it?
  - id: deleteBucket
    intent: Delete an empty bucket
    question: Can I delete a bucket that still contains objects?
  phrasing_ops: 5
  slug: oracle-cloud-buckets-api
- baseURL: https://identity.{region}.oraclecloud.com
  baseurl_source: declared
  description: The Compartments API from Oracle Cloud Infrastructure — 1 operation(s) for compartments.
  name: Oracle Cloud Infrastructure Compartments API
  phrasing_intents:
  - id: listCompartments
    intent: List the compartments in a tenancy
    question: What compartments are set up in my Oracle Cloud tenancy?
  phrasing_ops: 1
  slug: oracle-cloud-compartments-api
- baseURL: https://identity.{region}.oraclecloud.com
  baseurl_source: declared
  description: The Groups API from Oracle Cloud Infrastructure — 1 operation(s) for groups.
  name: Oracle Cloud Infrastructure Groups API
  phrasing_intents:
  - id: listGroups
    intent: List IAM groups in the tenancy
    question: What user groups exist in my Oracle Cloud tenancy?
  - id: createGroup
    intent: Create an IAM group
    question: How do I create a new group to organize users for access policies?
  phrasing_ops: 2
  slug: oracle-cloud-groups-api
- baseURL: https://iaas.{region}.oraclecloud.com
  baseurl_source: declared
  description: The Images API from Oracle Cloud Infrastructure — 2 operation(s) for images.
  name: Oracle Cloud Infrastructure Images API
  phrasing_intents:
  - id: listImages
    intent: List available compute images
    question: Which OS images can I use to launch instances in my compartment?
  - id: getImage
    intent: Get details of a compute image
    question: What operating system and version does a specific image contain?
  phrasing_ops: 2
  slug: oracle-cloud-images-api
- baseURL: https://iaas.{region}.oraclecloud.com
  baseurl_source: declared
  description: The Instances API from Oracle Cloud Infrastructure — 3 operation(s) for instances.
  name: Oracle Cloud Infrastructure Instances API
  phrasing_intents:
  - id: listInstances
    intent: List compute instances in a compartment
    question: What virtual machines are running in my Oracle Cloud compartment?
  - id: launchInstance
    intent: Launch a new compute instance
    question: How do I create a new virtual machine?
  - id: getInstance
    intent: Get details of a compute instance
    question: What shape and state is a specific instance in?
  - id: updateInstance
    intent: Rename or resize a compute instance
    question: Can I change an existing instance's shape to give it more CPU or memory?
  - id: terminateInstance
    intent: Terminate a compute instance
    question: How do I permanently delete a virtual machine?
  - id: instanceAction
    intent: Start, stop or reset a compute instance
    question: How do I stop or restart a single virtual machine?
  phrasing_ops: 6
  slug: oracle-cloud-instances-api
- baseURL: https://telemetry.{region}.oraclecloud.com
  baseurl_source: declared
  description: The Metrics API from Oracle Cloud Infrastructure — 2 operation(s) for metrics.
  name: Oracle Cloud Infrastructure Metrics API
  phrasing_intents:
  - id: summarizeMetricsData
    intent: Get aggregated metric data for a query
    question: How can I pull aggregated CPU or memory metrics for my resources over a time range?
  - id: listMetrics
    intent: List available metric definitions
    question: What metrics can I query for resources in my compartment?
  phrasing_ops: 2
  slug: oracle-cloud-metrics-api
- baseURL: https://objectstorage.{region}.oraclecloud.com
  baseurl_source: declared
  description: The Namespaces API from Oracle Cloud Infrastructure — 1 operation(s) for namespaces.
  name: Oracle Cloud Infrastructure Namespaces API
  phrasing_intents:
  - id: getNamespace
    intent: Get my Object Storage namespace name
    question: What is the Object Storage namespace for my Oracle Cloud account?
  phrasing_ops: 1
  slug: oracle-cloud-namespaces-api
- baseURL: https://objectstorage.{region}.oraclecloud.com
  baseurl_source: declared
  description: The Objects API from Oracle Cloud Infrastructure — 2 operation(s) for objects.
  name: Oracle Cloud Infrastructure Objects API
  phrasing_intents:
  - id: listObjects
    intent: List objects in a storage bucket
    question: What files are stored in my Object Storage bucket?
  - id: getObject
    intent: Download an object from a bucket
    question: How do I download a file from an Object Storage bucket?
  - id: putObject
    intent: Upload or overwrite an object in a bucket
    question: How do I upload a file to an Object Storage bucket?
  - id: deleteObject
    intent: Delete an object from a bucket
    question: How do I delete a file from an Object Storage bucket?
  phrasing_ops: 4
  slug: oracle-cloud-objects-api
- baseURL: https://identity.{region}.oraclecloud.com
  baseurl_source: declared
  description: The Policies API from Oracle Cloud Infrastructure — 1 operation(s) for policies.
  name: Oracle Cloud Infrastructure Policies API
  phrasing_intents:
  - id: listPolicies
    intent: List IAM policies in a compartment
    question: What IAM policies are attached to my compartment?
  - id: createPolicy
    intent: Create an IAM policy
    question: How do I grant a group permissions with a new IAM policy?
  phrasing_ops: 2
  slug: oracle-cloud-policies-api
- baseURL: https://objectstorage.{region}.oraclecloud.com
  baseurl_source: declared
  description: The Preauthenticated Requests API from Oracle Cloud Infrastructure — 1 operation(s) for preauthenticated requests.
  name: Oracle Cloud Infrastructure Preauthenticated Requests API
  phrasing_intents:
  - id: listPreauthenticatedRequests
    intent: List pre-authenticated requests on a bucket
    question: Which pre-authenticated links are currently open on my storage bucket?
  - id: createPreauthenticatedRequest
    intent: Create a pre-authenticated request for a bucket
    question: How do I share an object in Object Storage without giving someone credentials?
  phrasing_ops: 2
  slug: oracle-cloud-preauthenticated-requests-api
- baseURL: https://iaas.{region}.oraclecloud.com
  baseurl_source: declared
  description: The Shapes API from Oracle Cloud Infrastructure — 1 operation(s) for shapes.
  name: Oracle Cloud Infrastructure Shapes API
  phrasing_intents:
  - id: listShapes
    intent: List compute shapes available for instances
    question: Which compute shapes can I launch an instance with in my compartment?
  phrasing_ops: 1
  slug: oracle-cloud-shapes-api
- baseURL: https://identity.{region}.oraclecloud.com
  baseurl_source: declared
  description: The Users API from Oracle Cloud Infrastructure — 2 operation(s) for users.
  name: Oracle Cloud Infrastructure Users API
  phrasing_intents:
  - id: listUsers
    intent: List users in the tenancy
    question: Who are the IAM users in my Oracle Cloud tenancy?
  - id: createUser
    intent: Create an IAM user
    question: How do I add a new user to my tenancy?
  - id: getUser
    intent: Get an IAM user
    question: What details are stored for a specific user?
  - id: updateUser
    intent: Update a user's email or description
    question: How do I change the email address on a user account?
  - id: deleteUser
    intent: Delete an IAM user
    question: How do I remove a user who has left the organization?
  phrasing_ops: 5
  slug: oracle-cloud-users-api
- baseURL: https://iaas.{region}.oraclecloud.com
  baseurl_source: declared
  description: The Volume Attachments API from Oracle Cloud Infrastructure — 2 operation(s) for volume attachments.
  name: Oracle Cloud Infrastructure Volume Attachments API
  phrasing_intents:
  - id: listVolumeAttachments
    intent: List block volume attachments in a compartment
    question: Which block volumes are attached to instances in my compartment?
  - id: attachVolume
    intent: Attach a block volume to an instance
    question: How do I attach a block storage volume to a compute instance in Oracle Cloud?
  - id: detachVolume
    intent: Detach a block volume from an instance
    question: How do I disconnect a block volume from its instance?
  phrasing_ops: 3
  slug: oracle-cloud-volume-attachments-api
- baseURL: https://telemetry.{region}.oraclecloud.com
  baseurl_source: declared
  description: The blockstorage API from Oracle Cloud Infrastructure — 33 operation(s) for blockstorage.
  name: Oracle Cloud Infrastructure Blockstorage API
  phrasing_intents:
  - id: ListBlockVolumeReplicas
    intent: List block volume replicas in an availability domain
    question: Which cross-region replicas of my block volumes exist in this availability domain?
  - id: GetBlockVolumeReplica
    intent: Get details of one block volume replica
    question: What is the status of a specific block volume replica?
  - id: ListBootVolumeBackups
    intent: List boot volume backups in a compartment
    question: What backups exist of my instance boot volumes in a compartment?
  - id: CreateBootVolumeBackup
    intent: Back up a boot volume
    question: How do I take a backup of an instance's boot volume?
  - id: DeleteBootVolumeBackup
    intent: Delete a boot volume backup
    question: How do I remove an old boot volume backup I no longer need?
  - id: GetBootVolumeBackup
    intent: Get details of a boot volume backup
    question: What size and state is a specific boot volume backup in?
  - id: UpdateBootVolumeBackup
    intent: Rename or retag a boot volume backup
    question: How do I rename an existing boot volume backup?
  - id: ChangeBootVolumeBackupCompartment
    intent: Move a boot volume backup to another compartment
    question: How do I move a boot volume backup into a different compartment?
  phrasing_ops: 60
  slug: oracle-cloud-blockstorage-api
- baseURL: https://telemetry.{region}.oraclecloud.com
  baseurl_source: declared
  description: The compute API from Oracle Cloud Infrastructure — 82 operation(s) for compute.
  name: Oracle Cloud Infrastructure Compute API
  phrasing_intents:
  - id: ListAppCatalogListings
    intent: Browse published App Catalog listings
    question: What images and apps are published in the Oracle Cloud App Catalog?
  - id: GetAppCatalogListing
    intent: Get one App Catalog listing
    question: Where can I see the details of a single App Catalog listing?
  - id: ListAppCatalogListingResourceVersions
    intent: List versions of an App Catalog listing
    question: Which resource versions are available for an App Catalog listing?
  - id: GetAppCatalogListingResourceVersion
    intent: Get one version of an App Catalog listing
    question: What details are recorded for a specific version of a catalog listing?
  - id: GetAppCatalogListingAgreements
    intent: Retrieve the agreements for a listing version
    question: What terms do I have to accept before subscribing to an App Catalog listing version?
  - id: DeleteAppCatalogSubscription
    intent: Remove an App Catalog subscription
    question: How do I unsubscribe a compartment from an App Catalog listing version?
  - id: ListAppCatalogSubscriptions
    intent: List App Catalog subscriptions in a compartment
    question: Which App Catalog listings is my compartment subscribed to?
  - id: CreateAppCatalogSubscription
    intent: Subscribe a compartment to a catalog listing version
    question: How do I subscribe my compartment to an App Catalog image so I can launch it?
  phrasing_ops: 130
  slug: oracle-cloud-compute-api
- baseURL: https://telemetry.{region}.oraclecloud.com
  baseurl_source: declared
  description: The computeManagement API from Oracle Cloud Infrastructure — 23 operation(s) for computemanagement.
  name: Oracle Cloud Infrastructure Compute Management API
  phrasing_intents:
  - id: ListClusterNetworks
    intent: List cluster networks in a compartment
    question: Which RDMA cluster networks with instance pools do I have in my compartment?
  - id: CreateClusterNetwork
    intent: Create an RDMA cluster network with instance pools
    question: How do I set up a low-latency RDMA network of GPU or HPC bare metal instances?
  - id: TerminateClusterNetwork
    intent: Terminate a cluster network and its instances
    question: What gets deleted when I terminate a cluster network?
  - id: GetClusterNetwork
    intent: Get details of a cluster network
    question: What instance pools and state does my cluster network have?
  - id: UpdateClusterNetwork
    intent: Update a cluster network
    question: Can I resize the instance pools inside an existing cluster network?
  - id: ChangeClusterNetworkCompartment
    intent: Move a cluster network to another compartment
    question: Can I move a cluster network into a different compartment in the same tenancy?
  - id: ListClusterNetworkInstances
    intent: List instances in a cluster network
    question: Which compute instances belong to my cluster network?
  - id: ListInstanceConfigurations
    intent: List instance configurations in a compartment
    question: What instance configuration templates do I have saved in my compartment?
  phrasing_ops: 33
  slug: oracle-cloud-computemanagement-api
- baseURL: https://telemetry.{region}.oraclecloud.com
  baseurl_source: declared
  description: API operations for working with the container engine service.
  name: Oracle Cloud Infrastructure Container Engine API
  phrasing_intents:
  - id: ListAddonOptions
    intent: List add-ons supported for a Kubernetes version
    question: Which cluster add-ons are available for a given Kubernetes version on OKE?
  - id: GetClusterOptions
    intent: Get the options available for creating clusters
    question: What Kubernetes versions and settings can I choose when creating a new cluster?
  - id: ListClusters
    intent: List Kubernetes clusters in a compartment
    question: What Kubernetes clusters are running in my compartment?
  - id: CreateCluster
    intent: Create a Kubernetes cluster
    question: How do I spin up a new managed Kubernetes cluster in Oracle Cloud?
  - id: DeleteCluster
    intent: Delete a Kubernetes cluster
    question: How do I tear down a Kubernetes cluster I no longer need?
  - id: GetCluster
    intent: Get details of a Kubernetes cluster
    question: What version and state is my Kubernetes cluster in right now?
  - id: UpdateCluster
    intent: Update a Kubernetes cluster's settings
    question: How do I upgrade the Kubernetes version of an existing cluster?
  - id: CompleteCredentialRotation
    intent: Finish a cluster credential rotation
    question: How do I retire the old credentials after rotating my cluster's certificates?
  phrasing_ops: 50
  slug: oracle-cloud-containerengine-api
- baseURL: https://telemetry.{region}.oraclecloud.com
  baseurl_source: declared
  description: The database API from Oracle Cloud Infrastructure — 319 operation(s) for database.
  name: Oracle Cloud Infrastructure Database API
  phrasing_intents:
  - id: ListApplicationVips
    intent: List application VIPs on a cloud VM cluster
    question: Which application virtual IP addresses are assigned to my cloud VM cluster?
  - id: CreateApplicationVip
    intent: Create an application VIP on a cloud VM cluster
    question: How do I add a new application virtual IP address to an Oracle cloud VM cluster?
  - id: DeleteApplicationVip
    intent: Delete an application VIP
    question: How can I remove and deregister an application VIP I no longer need?
  - id: GetApplicationVip
    intent: Get details of an application VIP
    question: What IP address and hostname does a specific application VIP have?
  - id: ListAutonomousContainerDatabaseBackups
    intent: List Autonomous Container Database backups
    question: Where can I see the backups taken of an Autonomous Container Database?
  - id: ListAutonomousContainerDatabaseVersions
    intent: List supported Autonomous Container Database versions
    question: Which database versions can I choose when creating an Autonomous Container Database?
  - id: ListAutonomousContainerDatabases
    intent: List Autonomous Container Databases in a compartment
    question: What Autonomous Container Databases exist in my compartment?
  - id: CreateAutonomousContainerDatabase
    intent: Create an Autonomous Container Database
    question: How do I create a new Autonomous Container Database on dedicated Exadata infrastructure?
  phrasing_ops: 444
  slug: oracle-cloud-database-api
- baseURL: https://telemetry.{region}.oraclecloud.com
  baseurl_source: declared
  description: The events API from Oracle Cloud Infrastructure — 3 operation(s) for events.
  name: Oracle Cloud Infrastructure Events API
  phrasing_intents:
  - id: ListRules
    intent: List event rules in a compartment
    question: What event rules are set up in my compartment?
  - id: CreateRule
    intent: Create an event rule
    question: How do I trigger a notification or function when a resource event happens in Oracle Cloud?
  - id: DeleteRule
    intent: Delete an event rule
    question: How do I delete an event rule I no longer need?
  - id: GetRule
    intent: Get an event rule
    question: Which events does a particular rule match and what does it do?
  - id: UpdateRule
    intent: Update or disable an event rule
    question: Can I temporarily disable an event rule without deleting it?
  - id: ChangeRuleCompartment
    intent: Move an event rule to another compartment
    question: Can I move an event rule into a different compartment?
  phrasing_ops: 6
  slug: oracle-cloud-events-api
- baseURL: https://telemetry.{region}.oraclecloud.com
  baseurl_source: declared
  description: The functionsInvoke API from Oracle Cloud Infrastructure — 1 operation(s) for functionsinvoke.
  name: Oracle Cloud Infrastructure Functions Invoke API
  phrasing_intents:
  - id: InvokeFunction
    intent: Invoke a serverless function
    question: How do I call an OCI Function and get its result back?
  phrasing_ops: 1
  slug: oracle-cloud-functionsinvoke-api
- baseURL: https://telemetry.{region}.oraclecloud.com
  baseurl_source: declared
  description: The functionsManagement API from Oracle Cloud Infrastructure — 10 operation(s) for functionsmanagement.
  name: Oracle Cloud Infrastructure Functions Management API
  phrasing_intents:
  - id: ListApplications
    intent: List function applications in a compartment
    question: Which Functions applications exist in my compartment?
  - id: CreateApplication
    intent: Create a Functions application
    question: How do I create an application to hold my Oracle Cloud Functions?
  - id: DeleteApplication
    intent: Delete a Functions application
    question: How do I remove a Functions application I no longer need?
  - id: GetApplication
    intent: Get the details of a Functions application
    question: What configuration and subnets does a particular Functions application use?
  - id: UpdateApplication
    intent: Update a Functions application's configuration
    question: Can I change the shared config variables on an existing Functions application?
  - id: ChangeApplicationCompartment
    intent: Move a Functions application to another compartment
    question: Can I move a Functions application to a different compartment in my tenancy?
  - id: ListFunctions
    intent: List the functions in an application
    question: Which functions are deployed inside one application?
  - id: CreateFunction
    intent: Deploy a new function in an application
    question: How do I deploy a new serverless function from a container image?
  phrasing_ops: 16
  slug: oracle-cloud-functionsmanagement-api
- baseURL: https://telemetry.{region}.oraclecloud.com
  baseurl_source: declared
  description: The identity API from Oracle Cloud Infrastructure — 93 operation(s) for identity.
  name: Oracle Cloud Infrastructure Identity API
  phrasing_intents:
  - id: ListAllowedDomainLicenseTypes
    intent: List license types allowed for identity domains
    question: Which license types can I pick when creating an OCI identity domain?
  - id: GetAuthenticationPolicy
    intent: Get the tenancy's authentication policy
    question: What password rules and network restrictions apply to sign-ins in my tenancy?
  - id: UpdateAuthenticationPolicy
    intent: Update the tenancy's authentication policy
    question: Can I tighten the password requirements for local users in my tenancy?
  - id: ListAvailabilityDomains
    intent: List availability domains in the tenancy
    question: Which availability domains does my tenancy have in this region?
  - id: ListCompartments
    intent: List compartments inside a compartment
    question: What compartments sit under my root compartment?
  - id: CreateCompartment
    intent: Create a compartment
    question: How do I create a new compartment to organize cloud resources?
  - id: ListBulkActionResourceTypes
    intent: List resource types supported by bulk actions
    question: Which resource types can I bulk move or bulk delete from a compartment?
  - id: DeleteCompartment
    intent: Delete an empty compartment
    question: How do I delete a compartment I no longer use?
  phrasing_ops: 148
  slug: oracle-cloud-identity-api
- baseURL: https://telemetry.{region}.oraclecloud.com
  baseurl_source: declared
  description: The monitoring API from Oracle Cloud Infrastructure — 13 operation(s) for monitoring.
  name: Oracle Cloud Infrastructure Monitoring API
  phrasing_intents:
  - id: ListAlarmSuppressions
    intent: List suppressions on an alarm
    question: Which suppressions are currently muting notifications for a given alarm?
  - id: CreateAlarmSuppression
    intent: Suppress an alarm's notifications for a time window
    question: How do I silence alarm notifications during a planned maintenance window?
  - id: DeleteAlarmSuppression
    intent: Delete a specific alarm suppression
    question: How do I end one suppression early by its ID?
  - id: GetAlarmSuppression
    intent: Get the details of one alarm suppression
    question: When does a particular alarm suppression start and end?
  - id: ListAlarms
    intent: List the alarms in a compartment
    question: What monitoring alarms are defined in my compartment?
  - id: CreateAlarm
    intent: Create a monitoring alarm on a metric query
    question: How do I get notified when CPU utilization goes above a threshold in Oracle Cloud?
  - id: ListAlarmsStatus
    intent: See which alarms are firing in a compartment
    question: Which of my alarms are currently firing?
  - id: DeleteAlarm
    intent: Delete an alarm
    question: How do I permanently remove an alarm I no longer need?
  phrasing_ops: 18
  slug: oracle-cloud-monitoring-api
- baseURL: https://telemetry.{region}.oraclecloud.com
  baseurl_source: declared
  description: The notificationControlPlane API from Oracle Cloud Infrastructure — 13 operation(s) for notificationcontrolplane.
  name: Oracle Cloud Infrastructure Notification Control Plane API
  phrasing_intents:
  - id: ListPublisherMapGroups
    intent: List publisher map groups in a compartment
    question: Which publisher map groups are set up in my compartment?
  - id: CreatePublisherMapGroup
    intent: Create a publisher map group
    question: How do I bundle several publisher maps into one group for notifications?
  - id: DeletePublisherMapGroup
    intent: Delete a publisher map group
    question: How do I remove a publisher map group I no longer use?
  - id: GetPublisherMapGroup
    intent: Get a publisher map group's configuration
    question: Which publisher maps are included in a particular publisher map group?
  - id: UpdatePublisherMapGroup
    intent: Change the maps in a publisher map group
    question: How do I change which publisher maps belong to a group?
  - id: AddPublisherMapGroupLock
    intent: Lock a publisher map group
    question: How do I protect a publisher map group from being changed or deleted?
  - id: RemovePublisherMapGroupLock
    intent: Unlock a publisher map group
    question: How do I take the lock off a publisher map group?
  - id: ListPublisherMaps
    intent: List publisher maps in a compartment
    question: What publisher maps exist in my compartment?
  phrasing_ops: 22
  slug: oracle-cloud-notificationcontrolplane-api
- baseURL: https://telemetry.{region}.oraclecloud.com
  baseurl_source: declared
  description: The notificationDataPlane API from Oracle Cloud Infrastructure — 9 operation(s) for notificationdataplane.
  name: Oracle Cloud Infrastructure Notification Data Plane API
  phrasing_intents:
  - id: ListSmsNumbers
    intent: List SMS numbers for an SMS provider
    question: Which SMS numbers are registered with my SMS provider?
  - id: ListSubscriptions
    intent: List subscriptions for a compartment or topic
    question: Who is subscribed to my notification topic?
  - id: CreateSubscription
    intent: Subscribe an endpoint to a topic
    question: How do I subscribe an email address to a notification topic?
  - id: GetConfirmSubscription
    intent: Get a subscription's confirmation result
    question: How do I check the confirmation details of a subscription using its token?
  - id: ResendSubscriptionConfirmation
    intent: Resend a subscription confirmation
    question: How do I resend the confirmation link for a pending subscription?
  - id: GetUnsubscription
    intent: Unsubscribe a subscription from its topic
    question: How do I unsubscribe an endpoint from a topic with its unsubscribe token?
  - id: DeleteSubscription
    intent: Delete a subscription
    question: How do I delete a subscription as the topic administrator?
  - id: GetSubscription
    intent: Get a subscription's configuration
    question: Is a particular subscription confirmed or still pending?
  phrasing_ops: 12
  slug: oracle-cloud-notificationdataplane-api
- baseURL: https://telemetry.{region}.oraclecloud.com
  baseurl_source: declared
  description: The virtualNetwork API from Oracle Cloud Infrastructure — 176 operation(s) for virtualnetwork.
  name: Oracle Cloud Infrastructure Virtual Network API
  phrasing_intents:
  - id: ListAllowedPeerRegionsForRemotePeering
    intent: List regions allowed for remote VCN peering
    question: Which OCI regions can I peer my VCN with across regions?
  - id: ListByoasns
    intent: List BYOASN resources in a compartment
    question: What bring-your-own ASNs have I imported into this compartment?
  - id: CreateByoasn
    intent: Import your own autonomous system number
    question: How do I bring my own ASN into Oracle Cloud?
  - id: DeleteByoasn
    intent: Delete a BYOASN resource
    question: How do I remove an ASN I imported that I no longer need?
  - id: GetByoasn
    intent: Get a BYOASN resource
    question: Where can I see the details and state of one imported ASN?
  - id: UpdateByoasn
    intent: Rename or retag a BYOASN resource
    question: Can I change the display name of a BYOASN after importing it?
  - id: ChangeByoasnCompartment
    intent: Move a BYOASN to another compartment
    question: Can I move an imported ASN resource into a different compartment?
  - id: ValidateByoasn
    intent: Submit a BYOASN for validation
    question: How do I get my imported ASN validated by Oracle?
  phrasing_ops: 267
  slug: oracle-cloud-virtualnetwork-api
- baseURL: https://telemetry.{region}.oraclecloud.com
  baseurl_source: declared
  description: The Object Storage API from Oracle Cloud Infrastructure — 33 operation(s) for object storage.
  name: Oracle Cloud Infrastructure Object Storage API
  phrasing_intents:
  - id: GetNamespace
    intent: Look up my tenancy's Object Storage namespace name
    question: What is the Object Storage namespace string assigned to my Oracle Cloud tenancy?
  - id: GetNamespaceMetadata
    intent: View the default S3 and Swift compartments of a namespace
    question: Which compartment do buckets created through the S3 compatibility API land in by default?
  - id: UpdateNamespaceMetadata
    intent: Change the default compartments for S3 and Swift buckets
    question: How do I stop S3-compatible buckets from being created in the root compartment?
  - id: ListBuckets
    intent: List the buckets in a compartment
    question: Which Object Storage buckets exist in a given compartment?
  - id: CreateBucket
    intent: Create a new Object Storage bucket
    question: How do I create a bucket in Oracle Cloud Object Storage?
  - id: DeleteBucket
    intent: Delete an empty bucket
    question: Why can't I delete a bucket that still has objects in it?
  - id: GetBucket
    intent: Get the full details of a bucket
    question: What settings, tags and metadata does one specific bucket have?
  - id: HeadBucket
    intent: Check whether a bucket exists and get its ETag
    question: Is there a quick way to test if a bucket exists without fetching all its details?
  phrasing_ops: 61
  slug: oracle-cloud-object-storage-api
arazzos:
- description: Resolve a VCN's route table and security list, then create a subnet wired to both.
  name: Oracle Cloud Add Secured Subnet
  slug: oracle-cloud-add-secured-subnet-workflow
- description: Resolve the namespace, create a bucket, upload an object, then confirm it is listed.
  name: Oracle Cloud Create Bucket And Upload Object
  slug: oracle-cloud-create-bucket-and-upload-object-workflow
- description: Discover a metric in a namespace, create an alarm on it, then confirm the alarm.
  name: Oracle Cloud Create Metric Alarm
  slug: oracle-cloud-create-metric-alarm-workflow
- description: Create a Functions application, create a function in it, then invoke the function.
  name: Oracle Cloud Deploy And Invoke Function
  slug: oracle-cloud-deploy-and-invoke-function-workflow
- description: Pick a compatible shape and image in a compartment, then launch an instance with them.
  name: Oracle Cloud Find Image And Launch Instance
  slug: oracle-cloud-find-image-and-launch-instance-workflow
- description: Launch a compute instance, poll until it is running, then attach a block volume.
  name: Oracle Cloud Launch Instance With Attached Volume
  slug: oracle-cloud-launch-instance-with-volume-workflow
- description: Create an IAM group, create a user, then create a policy granting the group access.
  name: Oracle Cloud Onboard IAM User
  slug: oracle-cloud-onboard-iam-user-workflow
- description: Create an Autonomous Database and poll until it is AVAILABLE with connection URLs.
  name: Oracle Cloud Provision Autonomous Database
  slug: oracle-cloud-provision-autonomous-database-workflow
- description: Create a Kubernetes cluster, poll until active, then add a node pool to it.
  name: Oracle Cloud Provision OKE Cluster With Node Pool
  slug: oracle-cloud-provision-oke-cluster-workflow
- description: Create a VCN, poll until available, add an internet gateway, and create a public subnet.
  name: Oracle Cloud Provision VCN Network
  slug: oracle-cloud-provision-vcn-network-workflow
- description: Stop an instance, update its flexible shape configuration, then start it back up.
  name: Oracle Cloud Resize Instance Shape
  slug: oracle-cloud-resize-instance-shape-workflow
- description: Stop an Autonomous Database, confirm it stopped, then start it again.
  name: Oracle Cloud Restart Autonomous Database
  slug: oracle-cloud-restart-autonomous-database-workflow
- description: Resolve the namespace, confirm an object exists, then mint a read-only pre-authenticated URL.
  name: Oracle Cloud Share Object Via Preauthenticated Request
  slug: oracle-cloud-share-object-via-par-workflow
- description: Gracefully stop a running instance, confirm it stopped, then terminate it.
  name: Oracle Cloud Stop And Terminate Instance
  slug: oracle-cloud-stop-and-terminate-instance-workflow
- description: Confirm a running instance, then query summarized CPU metrics for its compartment.
  name: Oracle Cloud Summarize Instance CPU Metrics
  slug: oracle-cloud-summarize-instance-cpu-metrics-workflow
- description: List functions in an application, delete the first function, then delete the application.
  name: Oracle Cloud Teardown Functions Application
  slug: oracle-cloud-teardown-functions-application-workflow
- description: List a cluster's node pools, delete the first node pool, then delete the cluster.
  name: Oracle Cloud Teardown OKE Cluster
  slug: oracle-cloud-teardown-oke-cluster-workflow
- description: List subnets in a VCN, delete the first subnet, then delete the VCN itself.
  name: Oracle Cloud Teardown VCN Network
  slug: oracle-cloud-teardown-vcn-network-workflow
artifact_total: 472
asyncapis:
- description: ''
  name: Oracle Cloud Events Webhooks
  slug: oracle-cloud-events-webhooks
collections:
- collection_type: postman
  name: Oracle Cloud Compute API
  slug: postman-oracle-cloud-compute
- collection_type: postman
  name: Oracle Cloud Database API
  slug: postman-oracle-cloud-database
- collection_type: postman
  name: Oracle Cloud Functions API
  slug: postman-oracle-cloud-functions
- collection_type: postman
  name: Oracle Cloud Identity and Access Management API
  slug: postman-oracle-cloud-iam
- collection_type: postman
  name: Oracle Cloud Monitoring API
  slug: postman-oracle-cloud-monitoring
- collection_type: postman
  name: Oracle Cloud Networking API
  slug: postman-oracle-cloud-networking
- collection_type: postman
  name: Oracle Cloud Object Storage API
  slug: postman-oracle-cloud-object-storage
- collection_type: postman
  name: Oracle Cloud Container Engine for Kubernetes API
  slug: postman-oracle-cloud-oke
- collection_type: open
  name: Oracle Cloud Compute Alarms API
  slug: open-oracle-cloud-alarms-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Applications API
  slug: open-oracle-cloud-applications-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Autonomous Databases API
  slug: open-oracle-cloud-autonomous-databases-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Buckets API
  slug: open-oracle-cloud-buckets-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Clusters API
  slug: open-oracle-cloud-clusters-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Compartments API
  slug: open-oracle-cloud-compartments-api
- collection_type: open
  name: Oracle Cloud Compute Alarms DB Systems API
  slug: open-oracle-cloud-db-systems-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Functions API
  slug: open-oracle-cloud-functions-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Groups API
  slug: open-oracle-cloud-groups-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Images API
  slug: open-oracle-cloud-images-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Instances API
  slug: open-oracle-cloud-instances-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Internet Gateways API
  slug: open-oracle-cloud-internet-gateways-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Metrics API
  slug: open-oracle-cloud-metrics-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Namespaces API
  slug: open-oracle-cloud-namespaces-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Node Pools API
  slug: open-oracle-cloud-node-pools-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Objects API
  slug: open-oracle-cloud-objects-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Policies API
  slug: open-oracle-cloud-policies-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Preauthenticated Requests API
  slug: open-oracle-cloud-preauthenticated-requests-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Route Tables API
  slug: open-oracle-cloud-route-tables-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Security Lists API
  slug: open-oracle-cloud-security-lists-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Shapes API
  slug: open-oracle-cloud-shapes-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Subnets API
  slug: open-oracle-cloud-subnets-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Users API
  slug: open-oracle-cloud-users-api
- collection_type: open
  name: Oracle Cloud Compute Alarms VCNs API
  slug: open-oracle-cloud-vcns-api
- collection_type: open
  name: Oracle Cloud Compute Alarms Volume Attachments API
  slug: open-oracle-cloud-volume-attachments-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://www.oracle.com/
- group: commercial
  href: https://artifacts.apis.io/oracle-cloud/plans/oracle-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/oracle-cloud-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/oracle-cloud/rate-limits/oracle-cloud-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/oracle-cloud-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/oracle-cloud/finops/oracle-cloud-finops.yml
  title: ''
  type: FinOps
  url: finops/oracle-cloud-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/cloud/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/oracle/oci-cli/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/oracle/oci-cli/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/oracle/oci-cli/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/oracle/oci-cli/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/oracle/oci-cli/blob/master/CONTRIBUTING.md
- group: agent
  href: https://artifacts.apis.io/oracle-cloud/agentic-access/oracle-cloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-cloud-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/oracle-cloud/security/oracle-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oracle-cloud-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/oracle-cloud/authentication/oracle-cloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/oracle-cloud-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/oracle-cloud-infrastructure/overview
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-add-secured-subnet-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-add-secured-subnet-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-create-bucket-and-upload-object-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-create-bucket-and-upload-object-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-create-metric-alarm-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-create-metric-alarm-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-deploy-and-invoke-function-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-deploy-and-invoke-function-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-find-image-and-launch-instance-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-find-image-and-launch-instance-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-launch-instance-with-volume-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-launch-instance-with-volume-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-onboard-iam-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-onboard-iam-user-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-provision-autonomous-database-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-provision-autonomous-database-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-provision-oke-cluster-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-provision-oke-cluster-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-provision-vcn-network-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-provision-vcn-network-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-resize-instance-shape-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-resize-instance-shape-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-restart-autonomous-database-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-restart-autonomous-database-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-share-object-via-par-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-share-object-via-par-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-stop-and-terminate-instance-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-stop-and-terminate-instance-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-summarize-instance-cpu-metrics-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-summarize-instance-cpu-metrics-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-teardown-functions-application-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-teardown-functions-application-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-teardown-oke-cluster-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-teardown-oke-cluster-workflow.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/arazzo/oracle-cloud-teardown-vcn-network-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/oracle-cloud-teardown-vcn-network-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/oracle-cloud
- group: start
  title: ''
  type: Portal
  url: https://cloud.oracle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en-us/iaas/Content/home.htm
- group: auth
  title: ''
  type: Authentication
  url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm
- group: build
  title: ''
  type: SDKs
  url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm
- group: build
  title: ''
  type: CLI
  url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- group: operate
  title: ''
  type: Support
  url: https://www.oracle.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/cloud/price-list.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en-us/iaas/Content/GSG/Concepts/baremetalintro.htm
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/cloud-infrastructure/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.oracle.com/en-us/iaas/releasenotes/index.htm
- group: start
  title: ''
  type: Signup
  url: https://www.oracle.com/cloud/free/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.oracle.com/en-us/iaas/Content/servicechanges.htm
- group: build
  title: Java SDK
  type: SDKs
  url: https://github.com/oracle/oci-java-sdk
- group: build
  title: Python SDK
  type: SDKs
  url: https://github.com/oracle/oci-python-sdk
- group: build
  title: TypeScript SDK
  type: SDKs
  url: https://github.com/oracle/oci-typescript-sdk
- group: build
  title: .NET SDK
  type: SDKs
  url: https://github.com/oracle/oci-dotnet-sdk
- group: build
  title: Go SDK
  type: SDKs
  url: https://github.com/oracle/oci-go-sdk
- group: build
  title: Ruby SDK
  type: SDKs
  url: https://github.com/oracle/oci-ruby-sdk
- group: build
  title: PowerShell Modules
  type: SDKs
  url: https://github.com/oracle/oci-powershell-modules
- group: build
  title: OCI CLI Repository
  type: GitHubRepository
  url: https://github.com/oracle/oci-cli
- group: build
  title: Terraform Provider
  type: GitHubRepository
  url: https://github.com/oracle/terraform-provider-oci
- group: design
  href: https://artifacts.apis.io/oracle-cloud/rules/oracle-cloud-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/oracle-cloud-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/vocabulary/oracle-cloud-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/oracle-cloud-vocabulary.yaml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-iam-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-iam-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-database-create-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-database-create-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-monitoring-summarize-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-monitoring-summarize-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-iam-update-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-iam-update-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-oke-create-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-oke-create-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-oke-node-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-oke-node-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-functions-function-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-functions-function-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-networking-update-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-networking-update-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-database-db-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-database-db-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-functions-application-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-functions-application-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-functions-create-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-functions-create-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-object-storage-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-object-storage-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-compute-update-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-compute-update-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-database-autonomous-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-database-autonomous-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-oke-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-oke-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-monitoring-update-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-monitoring-update-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-networking-route-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-networking-route-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-compute-launch-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-compute-launch-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-compute-volume-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-compute-volume-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-monitoring-create-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-monitoring-create-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-monitoring-metric-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-monitoring-metric-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-compute-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-compute-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-functions-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-functions-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-oke-cluster-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-oke-cluster-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-networking-internet-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-networking-internet-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-monitoring-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-monitoring-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-compute-attach-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-compute-attach-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-iam-create-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-iam-create-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-database-update-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-database-update-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-networking-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-networking-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-networking-create-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-networking-create-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-oke-update-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-oke-update-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-networking-security-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-networking-security-context.jsonld
- group: design
  href: https://artifacts.apis.io/oracle-cloud/json-ld/oracle-cloud-monitoring-alarm-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oracle-cloud-monitoring-alarm-context.jsonld
- group: docs
  href: https://artifacts.apis.io/oracle-cloud/openapi/_original/oracle-cloud-core-services-openapi.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/oracle-cloud-core-services-openapi.yaml
- group: docs
  href: https://artifacts.apis.io/oracle-cloud/openapi/_original/oracle-cloud-identity-openapi.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/oracle-cloud-identity-openapi.yaml
- group: docs
  href: https://artifacts.apis.io/oracle-cloud/openapi/_original/oracle-cloud-object-storage-openapi.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/oracle-cloud-object-storage-openapi.yaml
- group: docs
  href: https://artifacts.apis.io/oracle-cloud/openapi/_original/oracle-cloud-database-openapi.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/oracle-cloud-database-openapi.yaml
- group: docs
  href: https://artifacts.apis.io/oracle-cloud/openapi/_original/oracle-cloud-kubernetes-engine-openapi.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/oracle-cloud-kubernetes-engine-openapi.yaml
- group: docs
  href: https://artifacts.apis.io/oracle-cloud/openapi/_original/oracle-cloud-monitoring-openapi.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/oracle-cloud-monitoring-openapi.yaml
- group: docs
  href: https://artifacts.apis.io/oracle-cloud/openapi/_original/oracle-cloud-functions-openapi.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/oracle-cloud-functions-openapi.yaml
- group: docs
  href: https://artifacts.apis.io/oracle-cloud/openapi/_original/oracle-cloud-events-openapi.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/oracle-cloud-events-openapi.yaml
- group: docs
  href: https://artifacts.apis.io/oracle-cloud/openapi/_original/oracle-cloud-notifications-openapi.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/oracle-cloud-notifications-openapi.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oracle.com/en-us/iaas/api/
- group: start
  title: ''
  type: SignUp
  url: https://www.oracle.com/cloud/free/
- group: build
  href: https://artifacts.apis.io/oracle-cloud/packages/oracle-cloud-packages.yml
  title: ''
  type: Packages
  url: packages/oracle-cloud-packages.yml
- group: build
  href: https://artifacts.apis.io/oracle-cloud/packages/oracle-cloud-packages.yml
  title: ''
  type: SDKs
  url: packages/oracle-cloud-packages.yml
- group: agent
  href: https://artifacts.apis.io/oracle-cloud/mcp/oracle-cloud-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/oracle-cloud-mcp.yml
- group: build
  href: https://artifacts.apis.io/oracle-cloud/mcp/oracle-cloud-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/oracle-cloud-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/oracle-cloud/llms/oracle-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/oracle-cloud-llms.txt
- group: agent
  href: https://artifacts.apis.io/oracle-cloud/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/conventions/oracle-cloud-conventions.yml
  title: ''
  type: Conventions
  url: conventions/oracle-cloud-conventions.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/conventions/oracle-cloud-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/oracle-cloud-conventions.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/errors/oracle-cloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/oracle-cloud-problem-types.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/lifecycle/oracle-cloud-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/oracle-cloud-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/oracle-cloud/lifecycle/oracle-cloud-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/oracle-cloud-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/oracle-cloud/changelog/oracle-cloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/oracle-cloud-changelog.yml
- group: build
  href: https://artifacts.apis.io/oracle-cloud/cli/oracle-cloud-cli.yml
  title: ''
  type: CLI
  url: cli/oracle-cloud-cli.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/data-model/oracle-cloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/oracle-cloud-data-model.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/asyncapi/oracle-cloud-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/oracle-cloud-events-webhooks.yml
- group: design
  href: https://artifacts.apis.io/oracle-cloud/conformance/oracle-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/oracle-cloud-conformance.yml
- group: auth
  href: https://artifacts.apis.io/oracle-cloud/conformance/oracle-cloud-conformance.yml
  title: ''
  type: Compliance
  url: conformance/oracle-cloud-conformance.yml
- group: auth
  href: https://artifacts.apis.io/oracle-cloud/security/oracle-cloud-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/oracle-cloud-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/oracle-cloud/security/oracle-cloud-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/oracle-cloud-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/oracle-cloud/security/oracle-cloud-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/oracle-cloud-trust-center.yml
- group: other
  href: https://artifacts.apis.io/oracle-cloud/overlays/oracle-cloud-core-services-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-cloud-core-services-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-cloud/overlays/oracle-cloud-identity-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-cloud-identity-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-cloud/overlays/oracle-cloud-object-storage-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-cloud-object-storage-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-cloud/overlays/oracle-cloud-database-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-cloud-database-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-cloud/overlays/oracle-cloud-kubernetes-engine-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-cloud-kubernetes-engine-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-cloud/overlays/oracle-cloud-monitoring-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-cloud-monitoring-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-cloud/overlays/oracle-cloud-functions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-cloud-functions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-cloud/overlays/oracle-cloud-events-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-cloud-events-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-cloud/overlays/oracle-cloud-notifications-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-cloud-notifications-overlay.yaml
created: '2024-01-01'
description: Oracle Cloud Infrastructure (OCI) is Oracle's public cloud, exposed as a REST control plane of 159 service APIs covering compute, virtual cloud networking, block and object storage, identity and access management, Autonomous Database, Kubernetes Engine, Functions, monitoring, events and notifications. Every request is signed with an RSA API signing key rather than a bearer token, every service is versioned by a YYYYMMDD segment in the URL path, and Oracle publishes a first-party Swagger 2.0 contract for each service from a single machine-readable index at docs.oracle.com/en-us/iaas/api/specs/. Client SDKs ship for Python, Java, TypeScript, Go, Ruby, .NET and PowerShell alongside the OCI CLI, a Terraform provider, and a repository of 27 reference MCP servers for agent access.
examples:
- key_count: 5
  name: Compute Attach Volume Details Example
  slug: compute-attach-volume-details-example
- key_count: 8
  name: Compute Image Example
  slug: compute-image-example
- key_count: 11
  name: Compute Instance Example
  slug: compute-instance-example
- key_count: 8
  name: Compute Launch Instance Details Example
  slug: compute-launch-instance-details-example
- key_count: 7
  name: Compute Shape Example
  slug: compute-shape-example
- key_count: 4
  name: Compute Update Instance Details Example
  slug: compute-update-instance-details-example
- key_count: 7
  name: Compute Volume Attachment Example
  slug: compute-volume-attachment-example
- key_count: 13
  name: Database Autonomous Database Example
  slug: database-autonomous-database-example
- key_count: 10
  name: Database Autonomous Database Summary Example
  slug: database-autonomous-database-summary-example
- key_count: 9
  name: Database Create Autonomous Database Details Example
  slug: database-create-autonomous-database-details-example
- key_count: 11
  name: Database Db System Example
  slug: database-db-system-example
- key_count: 6
  name: Database Db System Summary Example
  slug: database-db-system-summary-example
- key_count: 5
  name: Database Update Autonomous Database Details Example
  slug: database-update-autonomous-database-details-example
- key_count: 7
  name: Functions Application Example
  slug: functions-application-example
- key_count: 5
  name: Functions Application Summary Example
  slug: functions-application-summary-example
- key_count: 4
  name: Functions Create Application Details Example
  slug: functions-create-application-details-example
- key_count: 6
  name: Functions Create Function Details Example
  slug: functions-create-function-details-example
- key_count: 11
  name: Functions Function Example
  slug: functions-function-example
- key_count: 7
  name: Functions Function Summary Example
  slug: functions-function-summary-example
- key_count: 6
  name: Iam Compartment Example
  slug: iam-compartment-example
- key_count: 3
  name: Iam Create Group Details Example
  slug: iam-create-group-details-example
- key_count: 4
  name: Iam Create Policy Details Example
  slug: iam-create-policy-details-example
- key_count: 4
  name: Iam Create User Details Example
  slug: iam-create-user-details-example
- key_count: 6
  name: Iam Group Example
  slug: iam-group-example
- key_count: 7
  name: Iam Policy Example
  slug: iam-policy-example
- key_count: 2
  name: Iam Update User Details Example
  slug: iam-update-user-details-example
- key_count: 8
  name: Iam User Example
  slug: iam-user-example
- key_count: 11
  name: Monitoring Alarm Example
  slug: monitoring-alarm-example
- key_count: 5
  name: Monitoring Alarm Summary Example
  slug: monitoring-alarm-summary-example
- key_count: 8
  name: Monitoring Create Alarm Details Example
  slug: monitoring-create-alarm-details-example
- key_count: 5
  name: Monitoring Metric Data Example
  slug: monitoring-metric-data-example
- key_count: 4
  name: Monitoring Metric Example
  slug: monitoring-metric-example
- key_count: 5
  name: Monitoring Summarize Metrics Data Details Example
  slug: monitoring-summarize-metrics-data-details-example
- key_count: 4
  name: Monitoring Update Alarm Details Example
  slug: monitoring-update-alarm-details-example
- key_count: 4
  name: Networking Create Internet Gateway Details Example
  slug: networking-create-internet-gateway-details-example
- key_count: 8
  name: Networking Create Subnet Details Example
  slug: networking-create-subnet-details-example
- key_count: 5
  name: Networking Create Vcn Details Example
  slug: networking-create-vcn-details-example
- key_count: 7
  name: Networking Internet Gateway Example
  slug: networking-internet-gateway-example
- key_count: 7
  name: Networking Route Table Example
  slug: networking-route-table-example
- key_count: 8
  name: Networking Security List Example
  slug: networking-security-list-example
- key_count: 12
  name: Networking Subnet Example
  slug: networking-subnet-example
- key_count: 2
  name: Networking Update Vcn Details Example
  slug: networking-update-vcn-details-example
- key_count: 12
  name: Networking Vcn Example
  slug: networking-vcn-example
- key_count: 14
  name: Object Storage Bucket Example
  slug: object-storage-bucket-example
- key_count: 6
  name: Object Storage Bucket Summary Example
  slug: object-storage-bucket-summary-example
- key_count: 7
  name: Object Storage Create Bucket Details Example
  slug: object-storage-create-bucket-details-example
- key_count: 4
  name: Object Storage Create Preauthenticated Request Details Example
  slug: object-storage-create-preauthenticated-request-details-example
- key_count: 3
  name: Object Storage List Objects Example
  slug: object-storage-list-objects-example
- key_count: 6
  name: Object Storage Object Summary Example
  slug: object-storage-object-summary-example
- key_count: 7
  name: Object Storage Preauthenticated Request Example
  slug: object-storage-preauthenticated-request-example
- key_count: 6
  name: Object Storage Preauthenticated Request Summary Example
  slug: object-storage-preauthenticated-request-summary-example
- key_count: 7
  name: Object Storage Update Bucket Details Example
  slug: object-storage-update-bucket-details-example
- key_count: 8
  name: Oke Cluster Example
  slug: oke-cluster-example
- key_count: 6
  name: Oke Cluster Summary Example
  slug: oke-cluster-summary-example
- key_count: 4
  name: Oke Create Cluster Details Example
  slug: oke-create-cluster-details-example
- key_count: 6
  name: Oke Create Node Pool Details Example
  slug: oke-create-node-pool-details-example
- key_count: 9
  name: Oke Node Pool Example
  slug: oke-node-pool-example
- key_count: 6
  name: Oke Node Pool Summary Example
  slug: oke-node-pool-summary-example
- key_count: 2
  name: Oke Update Cluster Details Example
  slug: oke-update-cluster-details-example
- key_count: 6
  name: Oracle Cloud Attachvolume Example
  slug: oracle-cloud-attachvolume-example
- key_count: 6
  name: Oracle Cloud Createalarm Example
  slug: oracle-cloud-createalarm-example
- key_count: 6
  name: Oracle Cloud Createapplication Example
  slug: oracle-cloud-createapplication-example
- key_count: 6
  name: Oracle Cloud Createautonomousdatabase Example
  slug: oracle-cloud-createautonomousdatabase-example
- key_count: 6
  name: Oracle Cloud Createbucket Example
  slug: oracle-cloud-createbucket-example
- key_count: 6
  name: Oracle Cloud Createcluster Example
  slug: oracle-cloud-createcluster-example
- key_count: 6
  name: Oracle Cloud Createfunction Example
  slug: oracle-cloud-createfunction-example
- key_count: 6
  name: Oracle Cloud Creategroup Example
  slug: oracle-cloud-creategroup-example
- key_count: 6
  name: Oracle Cloud Createinternetgateway Example
  slug: oracle-cloud-createinternetgateway-example
- key_count: 6
  name: Oracle Cloud Createnodepool Example
  slug: oracle-cloud-createnodepool-example
- key_count: 6
  name: Oracle Cloud Createpolicy Example
  slug: oracle-cloud-createpolicy-example
- key_count: 6
  name: Oracle Cloud Createpreauthenticatedrequest Example
  slug: oracle-cloud-createpreauthenticatedrequest-example
- key_count: 6
  name: Oracle Cloud Createsubnet Example
  slug: oracle-cloud-createsubnet-example
- key_count: 6
  name: Oracle Cloud Createuser Example
  slug: oracle-cloud-createuser-example
- key_count: 6
  name: Oracle Cloud Createvcn Example
  slug: oracle-cloud-createvcn-example
- key_count: 6
  name: Oracle Cloud Deletebucket Example
  slug: oracle-cloud-deletebucket-example
- key_count: 6
  name: Oracle Cloud Deleteobject Example
  slug: oracle-cloud-deleteobject-example
- key_count: 6
  name: Oracle Cloud Getalarm Example
  slug: oracle-cloud-getalarm-example
- key_count: 6
  name: Oracle Cloud Getapplication Example
  slug: oracle-cloud-getapplication-example
- key_count: 6
  name: Oracle Cloud Getautonomousdatabase Example
  slug: oracle-cloud-getautonomousdatabase-example
- key_count: 6
  name: Oracle Cloud Getbucket Example
  slug: oracle-cloud-getbucket-example
- key_count: 6
  name: Oracle Cloud Getcluster Example
  slug: oracle-cloud-getcluster-example
- key_count: 6
  name: Oracle Cloud Getdbsystem Example
  slug: oracle-cloud-getdbsystem-example
- key_count: 6
  name: Oracle Cloud Getfunction Example
  slug: oracle-cloud-getfunction-example
- key_count: 6
  name: Oracle Cloud Getimage Example
  slug: oracle-cloud-getimage-example
- key_count: 6
  name: Oracle Cloud Getinstance Example
  slug: oracle-cloud-getinstance-example
- key_count: 6
  name: Oracle Cloud Getnamespace Example
  slug: oracle-cloud-getnamespace-example
- key_count: 6
  name: Oracle Cloud Getnodepool Example
  slug: oracle-cloud-getnodepool-example
- key_count: 6
  name: Oracle Cloud Getobject Example
  slug: oracle-cloud-getobject-example
- key_count: 6
  name: Oracle Cloud Getsubnet Example
  slug: oracle-cloud-getsubnet-example
- key_count: 6
  name: Oracle Cloud Getuser Example
  slug: oracle-cloud-getuser-example
- key_count: 6
  name: Oracle Cloud Getvcn Example
  slug: oracle-cloud-getvcn-example
- key_count: 6
  name: Oracle Cloud Instanceaction Example
  slug: oracle-cloud-instanceaction-example
- key_count: 6
  name: Oracle Cloud Launchinstance Example
  slug: oracle-cloud-launchinstance-example
- key_count: 6
  name: Oracle Cloud Listalarms Example
  slug: oracle-cloud-listalarms-example
- key_count: 6
  name: Oracle Cloud Listapplications Example
  slug: oracle-cloud-listapplications-example
- key_count: 6
  name: Oracle Cloud Listautonomousdatabases Example
  slug: oracle-cloud-listautonomousdatabases-example
- key_count: 6
  name: Oracle Cloud Listbuckets Example
  slug: oracle-cloud-listbuckets-example
- key_count: 6
  name: Oracle Cloud Listclusters Example
  slug: oracle-cloud-listclusters-example
- key_count: 6
  name: Oracle Cloud Listcompartments Example
  slug: oracle-cloud-listcompartments-example
- key_count: 6
  name: Oracle Cloud Listdbsystems Example
  slug: oracle-cloud-listdbsystems-example
- key_count: 6
  name: Oracle Cloud Listfunctions Example
  slug: oracle-cloud-listfunctions-example
- key_count: 6
  name: Oracle Cloud Listgroups Example
  slug: oracle-cloud-listgroups-example
- key_count: 6
  name: Oracle Cloud Listimages Example
  slug: oracle-cloud-listimages-example
- key_count: 6
  name: Oracle Cloud Listinstances Example
  slug: oracle-cloud-listinstances-example
- key_count: 6
  name: Oracle Cloud Listinternetgateways Example
  slug: oracle-cloud-listinternetgateways-example
- key_count: 6
  name: Oracle Cloud Listmetrics Example
  slug: oracle-cloud-listmetrics-example
- key_count: 6
  name: Oracle Cloud Listnodepools Example
  slug: oracle-cloud-listnodepools-example
- key_count: 6
  name: Oracle Cloud Listobjects Example
  slug: oracle-cloud-listobjects-example
- key_count: 6
  name: Oracle Cloud Listpolicies Example
  slug: oracle-cloud-listpolicies-example
- key_count: 6
  name: Oracle Cloud Listpreauthenticatedrequests Example
  slug: oracle-cloud-listpreauthenticatedrequests-example
- key_count: 6
  name: Oracle Cloud Listroutetables Example
  slug: oracle-cloud-listroutetables-example
- key_count: 6
  name: Oracle Cloud Listsecuritylists Example
  slug: oracle-cloud-listsecuritylists-example
- key_count: 6
  name: Oracle Cloud Listshapes Example
  slug: oracle-cloud-listshapes-example
- key_count: 6
  name: Oracle Cloud Listsubnets Example
  slug: oracle-cloud-listsubnets-example
- key_count: 6
  name: Oracle Cloud Listusers Example
  slug: oracle-cloud-listusers-example
- key_count: 6
  name: Oracle Cloud Listvcns Example
  slug: oracle-cloud-listvcns-example
- key_count: 6
  name: Oracle Cloud Listvolumeattachments Example
  slug: oracle-cloud-listvolumeattachments-example
- key_count: 6
  name: Oracle Cloud Startautonomousdatabase Example
  slug: oracle-cloud-startautonomousdatabase-example
- key_count: 6
  name: Oracle Cloud Stopautonomousdatabase Example
  slug: oracle-cloud-stopautonomousdatabase-example
- key_count: 6
  name: Oracle Cloud Summarizemetricsdata Example
  slug: oracle-cloud-summarizemetricsdata-example
- key_count: 6
  name: Oracle Cloud Terminateinstance Example
  slug: oracle-cloud-terminateinstance-example
- key_count: 6
  name: Oracle Cloud Updatealarm Example
  slug: oracle-cloud-updatealarm-example
- key_count: 6
  name: Oracle Cloud Updateautonomousdatabase Example
  slug: oracle-cloud-updateautonomousdatabase-example
- key_count: 6
  name: Oracle Cloud Updatebucket Example
  slug: oracle-cloud-updatebucket-example
- key_count: 6
  name: Oracle Cloud Updatecluster Example
  slug: oracle-cloud-updatecluster-example
- key_count: 6
  name: Oracle Cloud Updateinstance Example
  slug: oracle-cloud-updateinstance-example
- key_count: 6
  name: Oracle Cloud Updateuser Example
  slug: oracle-cloud-updateuser-example
- key_count: 6
  name: Oracle Cloud Updatevcn Example
  slug: oracle-cloud-updatevcn-example
features:
- description: Bare metal, virtual machine, and GPU compute instances with flexible shapes and autoscaling
  name: Compute
- description: Highly durable and scalable object storage for unstructured data with S3 compatibility
  name: Object Storage
- description: Self-driving, self-securing, self-repairing database with automated patching and tuning
  name: Autonomous Database
- description: Managed Kubernetes service for deploying and managing containerized applications
  name: Container Engine for Kubernetes
- description: Software-defined networking with private subnets, security lists, and network security groups
  name: Virtual Cloud Networks
- description: Fine-grained access control with policies, compartments, and identity federation
  name: Identity and Access Management
- description: Event-driven serverless compute platform based on Fn Project
  name: Serverless Functions
- description: Layer 4 and Layer 7 load balancing with SSL termination and health checks
  name: Load Balancing
- description: Real-time metrics collection, dashboards, and automated alarm notifications
  name: Monitoring and Alarms
- description: Automated security monitoring and threat detection across OCI resources
  name: Cloud Guard
- description: Hardware security module-backed encryption key management and secret storage
  name: Vault and Key Management
- description: Automated disaster recovery orchestration for complex multi-tier applications
  name: Disaster Recovery
- description: Large language model hosting and inference with customizable foundation models
  name: Generative AI
- description: Managed Jupyter notebooks and ML model lifecycle management platform
  name: Data Science
finops:
- has_sources: true
  method: derived
  name: Oracle Cloud Finops
  primary_unit: function invocation
  service_category: ''
  slug: oracle-cloud-finops
  template: false
image: /assets/icons/oracle-cloud.png
integrations:
- description: Infrastructure as Code provisioning with the OCI Terraform Provider
  name: Terraform
- description: Configuration management and automation with OCI Ansible Collection
  name: Ansible
- description: Metrics visualization with the OCI Grafana Plugin for Monitoring data
  name: Grafana
- description: Container orchestration with managed OKE clusters and Helm chart support
  name: Kubernetes
- description: IDE integration with OCI Tools for Visual Studio
  name: Visual Studio
- description: IDE integration with OCI Toolkit for Visual Studio Code
  name: VS Code
- description: IDE integration with OCI Toolkit for Eclipse
  name: Eclipse
- description: CI/CD automation with OCI GitHub Actions for deployment pipelines
  name: GitHub Actions
- description: Pre-built connectors for SaaS and on-premises application integration
  name: Oracle Integration Cloud
- description: Oracle Database@Azure for running Oracle databases on Azure infrastructure
  name: Microsoft Azure
json_schemas:
- name: AttachVolumeDetails
  property_count: 5
  slug: compute-attach-volume-details
- name: Image
  property_count: 8
  slug: compute-image
- name: Instance
  property_count: 11
  slug: compute-instance
- name: LaunchInstanceDetails
  property_count: 8
  slug: compute-launch-instance-details
- name: Shape
  property_count: 7
  slug: compute-shape
- name: UpdateInstanceDetails
  property_count: 4
  slug: compute-update-instance-details
- name: VolumeAttachment
  property_count: 7
  slug: compute-volume-attachment
- name: AutonomousDatabase
  property_count: 13
  slug: database-autonomous-database
- name: AutonomousDatabaseSummary
  property_count: 10
  slug: database-autonomous-database-summary
- name: CreateAutonomousDatabaseDetails
  property_count: 9
  slug: database-create-autonomous-database-details
- name: DbSystem
  property_count: 11
  slug: database-db-system
- name: DbSystemSummary
  property_count: 6
  slug: database-db-system-summary
- name: UpdateAutonomousDatabaseDetails
  property_count: 5
  slug: database-update-autonomous-database-details
- name: Application
  property_count: 7
  slug: functions-application
- name: ApplicationSummary
  property_count: 5
  slug: functions-application-summary
- name: CreateApplicationDetails
  property_count: 4
  slug: functions-create-application-details
- name: CreateFunctionDetails
  property_count: 6
  slug: functions-create-function-details
- name: Function
  property_count: 11
  slug: functions-function
- name: FunctionSummary
  property_count: 7
  slug: functions-function-summary
- name: Compartment
  property_count: 6
  slug: iam-compartment
- name: CreateGroupDetails
  property_count: 3
  slug: iam-create-group-details
- name: CreatePolicyDetails
  property_count: 4
  slug: iam-create-policy-details
- name: CreateUserDetails
  property_count: 4
  slug: iam-create-user-details
- name: Group
  property_count: 6
  slug: iam-group
- name: Policy
  property_count: 7
  slug: iam-policy
- name: UpdateUserDetails
  property_count: 2
  slug: iam-update-user-details
- name: User
  property_count: 8
  slug: iam-user
- name: Alarm
  property_count: 11
  slug: monitoring-alarm
- name: AlarmSummary
  property_count: 5
  slug: monitoring-alarm-summary
- name: CreateAlarmDetails
  property_count: 8
  slug: monitoring-create-alarm-details
- name: MetricData
  property_count: 5
  slug: monitoring-metric-data
- name: Metric
  property_count: 4
  slug: monitoring-metric
- name: SummarizeMetricsDataDetails
  property_count: 5
  slug: monitoring-summarize-metrics-data-details
- name: UpdateAlarmDetails
  property_count: 4
  slug: monitoring-update-alarm-details
- name: CreateInternetGatewayDetails
  property_count: 4
  slug: networking-create-internet-gateway-details
- name: CreateSubnetDetails
  property_count: 8
  slug: networking-create-subnet-details
- name: CreateVcnDetails
  property_count: 5
  slug: networking-create-vcn-details
- name: InternetGateway
  property_count: 7
  slug: networking-internet-gateway
- name: RouteTable
  property_count: 7
  slug: networking-route-table
- name: SecurityList
  property_count: 8
  slug: networking-security-list
- name: Subnet
  property_count: 12
  slug: networking-subnet
- name: UpdateVcnDetails
  property_count: 2
  slug: networking-update-vcn-details
- name: Vcn
  property_count: 12
  slug: networking-vcn
- name: Bucket
  property_count: 14
  slug: object-storage-bucket
- name: BucketSummary
  property_count: 6
  slug: object-storage-bucket-summary
- name: CreateBucketDetails
  property_count: 7
  slug: object-storage-create-bucket-details
- name: CreatePreauthenticatedRequestDetails
  property_count: 4
  slug: object-storage-create-preauthenticated-request-details
- name: ListObjects
  property_count: 3
  slug: object-storage-list-objects
- name: ObjectSummary
  property_count: 6
  slug: object-storage-object-summary
- name: PreauthenticatedRequest
  property_count: 7
  slug: object-storage-preauthenticated-request
- name: PreauthenticatedRequestSummary
  property_count: 6
  slug: object-storage-preauthenticated-request-summary
- name: UpdateBucketDetails
  property_count: 7
  slug: object-storage-update-bucket-details
- name: Cluster
  property_count: 8
  slug: oke-cluster
- name: ClusterSummary
  property_count: 6
  slug: oke-cluster-summary
- name: CreateClusterDetails
  property_count: 4
  slug: oke-create-cluster-details
- name: CreateNodePoolDetails
  property_count: 6
  slug: oke-create-node-pool-details
- name: NodePool
  property_count: 9
  slug: oke-node-pool
- name: NodePoolSummary
  property_count: 6
  slug: oke-node-pool-summary
- name: UpdateClusterDetails
  property_count: 2
  slug: oke-update-cluster-details
- name: Alarm
  property_count: 11
  slug: oracle-cloud-alarm
- name: AlarmSummary
  property_count: 5
  slug: oracle-cloud-alarmsummary
- name: Application
  property_count: 7
  slug: oracle-cloud-application
- name: ApplicationSummary
  property_count: 5
  slug: oracle-cloud-applicationsummary
- name: AttachVolumeDetails
  property_count: 5
  slug: oracle-cloud-attachvolumedetails
- name: AutonomousDatabase
  property_count: 13
  slug: oracle-cloud-autonomousdatabase
- name: AutonomousDatabaseSummary
  property_count: 10
  slug: oracle-cloud-autonomousdatabasesummary
- name: Bucket
  property_count: 14
  slug: oracle-cloud-bucket
- name: BucketSummary
  property_count: 6
  slug: oracle-cloud-bucketsummary
- name: Cluster
  property_count: 8
  slug: oracle-cloud-cluster
- name: ClusterSummary
  property_count: 6
  slug: oracle-cloud-clustersummary
- name: Compartment
  property_count: 6
  slug: oracle-cloud-compartment
- name: CreateAlarmDetails
  property_count: 8
  slug: oracle-cloud-createalarmdetails
- name: CreateApplicationDetails
  property_count: 4
  slug: oracle-cloud-createapplicationdetails
- name: CreateAutonomousDatabaseDetails
  property_count: 9
  slug: oracle-cloud-createautonomousdatabasedetails
- name: CreateBucketDetails
  property_count: 7
  slug: oracle-cloud-createbucketdetails
- name: CreateClusterDetails
  property_count: 4
  slug: oracle-cloud-createclusterdetails
- name: CreateFunctionDetails
  property_count: 6
  slug: oracle-cloud-createfunctiondetails
- name: CreateGroupDetails
  property_count: 3
  slug: oracle-cloud-creategroupdetails
- name: CreateInternetGatewayDetails
  property_count: 4
  slug: oracle-cloud-createinternetgatewaydetails
- name: CreateNodePoolDetails
  property_count: 6
  slug: oracle-cloud-createnodepooldetails
- name: CreatePolicyDetails
  property_count: 4
  slug: oracle-cloud-createpolicydetails
- name: CreatePreauthenticatedRequestDetails
  property_count: 4
  slug: oracle-cloud-createpreauthenticatedrequestdetails
- name: CreateSubnetDetails
  property_count: 8
  slug: oracle-cloud-createsubnetdetails
- name: CreateUserDetails
  property_count: 4
  slug: oracle-cloud-createuserdetails
- name: CreateVcnDetails
  property_count: 5
  slug: oracle-cloud-createvcndetails
- name: DbSystem
  property_count: 11
  slug: oracle-cloud-dbsystem
- name: DbSystemSummary
  property_count: 6
  slug: oracle-cloud-dbsystemsummary
- name: Error
  property_count: 3
  slug: oracle-cloud-error
- name: Function
  property_count: 11
  slug: oracle-cloud-function
- name: FunctionSummary
  property_count: 7
  slug: oracle-cloud-functionsummary
- name: Group
  property_count: 6
  slug: oracle-cloud-group
- name: Image
  property_count: 8
  slug: oracle-cloud-image
- name: Instance
  property_count: 11
  slug: oracle-cloud-instance
- name: InternetGateway
  property_count: 7
  slug: oracle-cloud-internetgateway
- name: LaunchInstanceDetails
  property_count: 8
  slug: oracle-cloud-launchinstancedetails
- name: ListObjects
  property_count: 3
  slug: oracle-cloud-listobjects
- name: Metric
  property_count: 4
  slug: oracle-cloud-metric
- name: MetricData
  property_count: 5
  slug: oracle-cloud-metricdata
- name: NodePool
  property_count: 9
  slug: oracle-cloud-nodepool
- name: NodePoolSummary
  property_count: 6
  slug: oracle-cloud-nodepoolsummary
- name: ObjectSummary
  property_count: 6
  slug: oracle-cloud-objectsummary
- name: Policy
  property_count: 7
  slug: oracle-cloud-policy
- name: PreauthenticatedRequest
  property_count: 7
  slug: oracle-cloud-preauthenticatedrequest
- name: PreauthenticatedRequestSummary
  property_count: 6
  slug: oracle-cloud-preauthenticatedrequestsummary
- name: RouteTable
  property_count: 7
  slug: oracle-cloud-routetable
- name: SecurityList
  property_count: 8
  slug: oracle-cloud-securitylist
- name: Shape
  property_count: 7
  slug: oracle-cloud-shape
- name: Subnet
  property_count: 12
  slug: oracle-cloud-subnet
- name: SummarizeMetricsDataDetails
  property_count: 5
  slug: oracle-cloud-summarizemetricsdatadetails
- name: UpdateAlarmDetails
  property_count: 4
  slug: oracle-cloud-updatealarmdetails
- name: UpdateAutonomousDatabaseDetails
  property_count: 5
  slug: oracle-cloud-updateautonomousdatabasedetails
- name: UpdateBucketDetails
  property_count: 7
  slug: oracle-cloud-updatebucketdetails
- name: UpdateClusterDetails
  property_count: 2
  slug: oracle-cloud-updateclusterdetails
- name: UpdateInstanceDetails
  property_count: 4
  slug: oracle-cloud-updateinstancedetails
- name: UpdateUserDetails
  property_count: 2
  slug: oracle-cloud-updateuserdetails
- name: UpdateVcnDetails
  property_count: 2
  slug: oracle-cloud-updatevcndetails
- name: User
  property_count: 8
  slug: oracle-cloud-user
- name: Vcn
  property_count: 12
  slug: oracle-cloud-vcn
- name: VolumeAttachment
  property_count: 7
  slug: oracle-cloud-volumeattachment
json_structures:
- name: Compute Attach Volume Details Structure
  property_count: 5
  slug: compute-attach-volume-details-structure
- name: Compute Image Structure
  property_count: 8
  slug: compute-image-structure
- name: Compute Instance Structure
  property_count: 11
  slug: compute-instance-structure
- name: Compute Launch Instance Details Structure
  property_count: 8
  slug: compute-launch-instance-details-structure
- name: Compute Shape Structure
  property_count: 7
  slug: compute-shape-structure
- name: Compute Update Instance Details Structure
  property_count: 4
  slug: compute-update-instance-details-structure
- name: Compute Volume Attachment Structure
  property_count: 7
  slug: compute-volume-attachment-structure
- name: Database Autonomous Database Structure
  property_count: 13
  slug: database-autonomous-database-structure
- name: Database Autonomous Database Summary Structure
  property_count: 10
  slug: database-autonomous-database-summary-structure
- name: Database Create Autonomous Database Details Structure
  property_count: 9
  slug: database-create-autonomous-database-details-structure
- name: Database Db System Structure
  property_count: 11
  slug: database-db-system-structure
- name: Database Db System Summary Structure
  property_count: 6
  slug: database-db-system-summary-structure
- name: Database Update Autonomous Database Details Structure
  property_count: 5
  slug: database-update-autonomous-database-details-structure
- name: Functions Application Structure
  property_count: 7
  slug: functions-application-structure
- name: Functions Application Summary Structure
  property_count: 5
  slug: functions-application-summary-structure
- name: Functions Create Application Details Structure
  property_count: 4
  slug: functions-create-application-details-structure
- name: Functions Create Function Details Structure
  property_count: 6
  slug: functions-create-function-details-structure
- name: Functions Function Structure
  property_count: 11
  slug: functions-function-structure
- name: Functions Function Summary Structure
  property_count: 7
  slug: functions-function-summary-structure
- name: Iam Compartment Structure
  property_count: 6
  slug: iam-compartment-structure
- name: Iam Create Group Details Structure
  property_count: 3
  slug: iam-create-group-details-structure
- name: Iam Create Policy Details Structure
  property_count: 4
  slug: iam-create-policy-details-structure
- name: Iam Create User Details Structure
  property_count: 4
  slug: iam-create-user-details-structure
- name: Iam Group Structure
  property_count: 6
  slug: iam-group-structure
- name: Iam Policy Structure
  property_count: 7
  slug: iam-policy-structure
- name: Iam Update User Details Structure
  property_count: 2
  slug: iam-update-user-details-structure
- name: Iam User Structure
  property_count: 8
  slug: iam-user-structure
- name: Monitoring Alarm Structure
  property_count: 11
  slug: monitoring-alarm-structure
- name: Monitoring Alarm Summary Structure
  property_count: 5
  slug: monitoring-alarm-summary-structure
- name: Monitoring Create Alarm Details Structure
  property_count: 8
  slug: monitoring-create-alarm-details-structure
- name: Monitoring Metric Data Structure
  property_count: 5
  slug: monitoring-metric-data-structure
- name: Monitoring Metric Structure
  property_count: 4
  slug: monitoring-metric-structure
- name: Monitoring Summarize Metrics Data Details Structure
  property_count: 5
  slug: monitoring-summarize-metrics-data-details-structure
- name: Monitoring Update Alarm Details Structure
  property_count: 4
  slug: monitoring-update-alarm-details-structure
- name: Networking Create Internet Gateway Details Structure
  property_count: 4
  slug: networking-create-internet-gateway-details-structure
- name: Networking Create Subnet Details Structure
  property_count: 8
  slug: networking-create-subnet-details-structure
- name: Networking Create Vcn Details Structure
  property_count: 5
  slug: networking-create-vcn-details-structure
- name: Networking Internet Gateway Structure
  property_count: 7
  slug: networking-internet-gateway-structure
- name: Networking Route Table Structure
  property_count: 7
  slug: networking-route-table-structure
- name: Networking Security List Structure
  property_count: 8
  slug: networking-security-list-structure
- name: Networking Subnet Structure
  property_count: 12
  slug: networking-subnet-structure
- name: Networking Update Vcn Details Structure
  property_count: 2
  slug: networking-update-vcn-details-structure
- name: Networking Vcn Structure
  property_count: 12
  slug: networking-vcn-structure
- name: Object Storage Bucket Structure
  property_count: 14
  slug: object-storage-bucket-structure
- name: Object Storage Bucket Summary Structure
  property_count: 6
  slug: object-storage-bucket-summary-structure
- name: Object Storage Create Bucket Details Structure
  property_count: 7
  slug: object-storage-create-bucket-details-structure
- name: Object Storage Create Preauthenticated Request Details Structure
  property_count: 4
  slug: object-storage-create-preauthenticated-request-details-structure
- name: Object Storage List Objects Structure
  property_count: 3
  slug: object-storage-list-objects-structure
- name: Object Storage Object Summary Structure
  property_count: 6
  slug: object-storage-object-summary-structure
- name: Object Storage Preauthenticated Request Structure
  property_count: 7
  slug: object-storage-preauthenticated-request-structure
- name: Object Storage Preauthenticated Request Summary Structure
  property_count: 6
  slug: object-storage-preauthenticated-request-summary-structure
- name: Object Storage Update Bucket Details Structure
  property_count: 7
  slug: object-storage-update-bucket-details-structure
- name: Oke Cluster Structure
  property_count: 8
  slug: oke-cluster-structure
- name: Oke Cluster Summary Structure
  property_count: 6
  slug: oke-cluster-summary-structure
- name: Oke Create Cluster Details Structure
  property_count: 4
  slug: oke-create-cluster-details-structure
- name: Oke Create Node Pool Details Structure
  property_count: 6
  slug: oke-create-node-pool-details-structure
- name: Oke Node Pool Structure
  property_count: 9
  slug: oke-node-pool-structure
- name: Oke Node Pool Summary Structure
  property_count: 6
  slug: oke-node-pool-summary-structure
- name: Oke Update Cluster Details Structure
  property_count: 2
  slug: oke-update-cluster-details-structure
- name: Oracle Cloud Structure
  property_count: 0
  slug: oracle-cloud-structure
jsonld:
- class_count: 1
  name: Oracle Cloud Compute Attach Context
  property_count: 5
  slug: oracle-cloud-compute-attach-context
- class_count: 3
  name: Oracle Cloud Compute Context
  property_count: 20
  slug: oracle-cloud-compute-context
- class_count: 1
  name: Oracle Cloud Compute Launch Context
  property_count: 8
  slug: oracle-cloud-compute-launch-context
- class_count: 1
  name: Oracle Cloud Compute Update Context
  property_count: 4
  slug: oracle-cloud-compute-update-context
- class_count: 1
  name: Oracle Cloud Compute Volume Context
  property_count: 7
  slug: oracle-cloud-compute-volume-context
- class_count: 2
  name: Oracle Cloud Database Autonomous Context
  property_count: 13
  slug: oracle-cloud-database-autonomous-context
- class_count: 1
  name: Oracle Cloud Database Create Context
  property_count: 9
  slug: oracle-cloud-database-create-context
- class_count: 2
  name: Oracle Cloud Database Db Context
  property_count: 11
  slug: oracle-cloud-database-db-context
- class_count: 1
  name: Oracle Cloud Database Update Context
  property_count: 5
  slug: oracle-cloud-database-update-context
- class_count: 1
  name: Oracle Cloud Functions Application Context
  property_count: 5
  slug: oracle-cloud-functions-application-context
- class_count: 2
  name: Oracle Cloud Functions Context
  property_count: 12
  slug: oracle-cloud-functions-context
- class_count: 2
  name: Oracle Cloud Functions Create Context
  property_count: 8
  slug: oracle-cloud-functions-create-context
- class_count: 1
  name: Oracle Cloud Functions Function Context
  property_count: 7
  slug: oracle-cloud-functions-function-context
- class_count: 4
  name: Oracle Cloud Iam Context
  property_count: 9
  slug: oracle-cloud-iam-context
- class_count: 3
  name: Oracle Cloud Iam Create Context
  property_count: 5
  slug: oracle-cloud-iam-create-context
- class_count: 1
  name: Oracle Cloud Iam Update Context
  property_count: 2
  slug: oracle-cloud-iam-update-context
- class_count: 1
  name: Oracle Cloud Monitoring Alarm Context
  property_count: 5
  slug: oracle-cloud-monitoring-alarm-context
- class_count: 2
  name: Oracle Cloud Monitoring Context
  property_count: 13
  slug: oracle-cloud-monitoring-context
- class_count: 1
  name: Oracle Cloud Monitoring Create Context
  property_count: 8
  slug: oracle-cloud-monitoring-create-context
- class_count: 1
  name: Oracle Cloud Monitoring Metric Context
  property_count: 5
  slug: oracle-cloud-monitoring-metric-context
- class_count: 1
  name: Oracle Cloud Monitoring Summarize Context
  property_count: 5
  slug: oracle-cloud-monitoring-summarize-context
- class_count: 1
  name: Oracle Cloud Monitoring Update Context
  property_count: 4
  slug: oracle-cloud-monitoring-update-context
- class_count: 2
  name: Oracle Cloud Networking Context
  property_count: 17
  slug: oracle-cloud-networking-context
- class_count: 3
  name: Oracle Cloud Networking Create Context
  property_count: 11
  slug: oracle-cloud-networking-create-context
- class_count: 1
  name: Oracle Cloud Networking Internet Context
  property_count: 7
  slug: oracle-cloud-networking-internet-context
- class_count: 1
  name: Oracle Cloud Networking Route Context
  property_count: 7
  slug: oracle-cloud-networking-route-context
- class_count: 1
  name: Oracle Cloud Networking Security Context
  property_count: 8
  slug: oracle-cloud-networking-security-context
- class_count: 1
  name: Oracle Cloud Networking Update Context
  property_count: 2
  slug: oracle-cloud-networking-update-context
- class_count: 9
  name: Oracle Cloud Object Storage Context
  property_count: 26
  slug: oracle-cloud-object-storage-context
- class_count: 1
  name: Oracle Cloud Oke Cluster Context
  property_count: 6
  slug: oracle-cloud-oke-cluster-context
- class_count: 1
  name: Oracle Cloud Oke Context
  property_count: 8
  slug: oracle-cloud-oke-context
- class_count: 2
  name: Oracle Cloud Oke Create Context
  property_count: 7
  slug: oracle-cloud-oke-create-context
- class_count: 2
  name: Oracle Cloud Oke Node Context
  property_count: 9
  slug: oracle-cloud-oke-node-context
- class_count: 1
  name: Oracle Cloud Oke Update Context
  property_count: 2
  slug: oracle-cloud-oke-update-context
layout: provider
mcp_servers:
- description: Oracle publishes a first-party MCP monorepo at github.com/oracle/mcp containing 32 MCP servers, 27 of which target Oracle Cloud Infrastructure. Two are general-purpose entry points — oci-cloud-mcp-ser
  name: Oracle MCP Servers for OCI
  slug: oracle-mcp-servers-for-oci
modified: '2026-08-29'
name: Oracle Cloud Infrastructure
nav: Providers
network: true
overview: 'Oracle Cloud Infrastructure publishes 28 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alarms API, Buckets API, Compartments API, and 25 more. Tagged areas include Cloud Computing, Enterprise Cloud, Infrastructure-as-a-Service, Oracle, and Platform-as-a-Service.


  The Oracle Cloud Infrastructure catalog on APIs.io includes 1 event-driven AsyncAPI specification, 34 JSON-LD contexts, and 2 Spectral governance rulesets.


  Oracle Cloud Infrastructure''s developer surface includes authentication, developer portal, documentation, CLI, support, pricing, getting-started guide, and 127 more developer resources.'
plans:
- name: Oracle Cloud Plans Pricing
  plan_count: 10
  slug: oracle-cloud-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Oracle Cloud Rate Limits
  slug: oracle-cloud-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Oracle Cloud Infrastructure — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: oracle-cloud-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: Oracle Cloud Infrastructure API Rules
  rule_count: 31
  severity_counts:
    error: 14
    hint: 0
    info: 5
    warn: 12
  slug: oracle-cloud-spectral-rules
score:
  band: exemplar
  composite: 76.9
  coverage:
    artifact_dirs: 36
    catalog_earned: 84.0
    catalog_earned_first_party: 12.0
    catalog_gap: 31.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 54.0
    developer_ergonomics: 83.9
    discoverability: 76.7
    operational_transparency: 60.5
  previous_composite: 76.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 77.4
      derived: 22
      marker_coverage: 61.1
      total: 36
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/oracle-cloud/oracle-cloud-2026-06-20T191120.png
security:
- kind: authentication
  name: Oracle Cloud Authentication
  slug: oracle-cloud-authentication
  summary_line: http-signature · 1 scheme
- kind: domain-security
  name: Oracle Cloud Domain Security
  slug: oracle-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Oracle Cloud Vulnerability Disclosure
  slug: oracle-cloud-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Oracle Cloud Trust Center
  slug: oracle-cloud-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, PCI DSS, HIPAA, HITRUST, FedRAMP, DoD Impact Levels, CJIS, ITAR, IRAP, C5, ENS, HDS, G-Cloud / Cyber Essentials, ISMAP, K-ISMS, MTCS, TISAX, CSA STAR, CSA AI STAR, GDPR, NIST
skill_count: 6
skills:
- name: oracle-cloud-launch-compute-instance
  slug: oracle-cloud-launch-compute-instance
- name: oracle-cloud-monitor-with-alarms
  slug: oracle-cloud-monitor-with-alarms
- name: oracle-cloud-onboard-iam-user
  slug: oracle-cloud-onboard-iam-user
- name: oracle-cloud-provision-autonomous-database
  slug: oracle-cloud-provision-autonomous-database
- name: oracle-cloud-provision-vcn-network
  slug: oracle-cloud-provision-vcn-network
- name: oracle-cloud-store-and-share-object
  slug: oracle-cloud-store-and-share-object
slug: oracle-cloud
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure-as-a-Service
- Oracle
- Platform-as-a-Service
- Compute
- Object Storage
- Database
- Kubernetes
- Serverless
- Monitoring
- Event-Driven
use_cases:
- description: Migrate on-premises workloads to OCI with tools for assessment, planning, and execution
  name: Cloud Migration
- description: Run HPC workloads with bare metal instances, RDMA networking, and cluster networking
  name: High Performance Computing
- description: Build scalable data warehouses with Autonomous Database and integrated analytics
  name: Data Warehousing
- description: Automate build, test, and deployment pipelines with OCI DevOps and Container Engine
  name: DevOps and CI/CD
- description: Implement business continuity with cross-region replication and automated failover
  name: Disaster Recovery
- description: Train and deploy ML models using GPU instances, Data Science, and Generative AI services
  name: AI and Machine Learning
- description: Extend on-premises infrastructure with Cloud@Customer and dedicated regions
  name: Hybrid Cloud
- description: Extend Oracle SaaS applications with custom APIs and integrations on OCI
  name: SaaS Extension
- description: Process IoT data at scale with streaming, functions, and edge infrastructure
  name: IoT and Edge Computing
- description: Connect OCI with AWS, Azure, and Google Cloud using FastConnect and partnerships
  name: Multi-Cloud Networking
website: https://www.oracle.com/cloud/
---
