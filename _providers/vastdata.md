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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Active Directory is supported as an external authorization and authentication provider. Active Directory may store and provide user and group attributes used by both NFS and SMB protocols. Active Dire
  name: VAST Data activedirectory API
  slug: vastdata-activedirectory-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Alarms can be raised by events.
  name: VAST Data alarms API
  slug: vastdata-alarms-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: API tokens are tokens created by VMS that enable VMS users to securely authenticate REST API requests.
  name: VAST Data apitokens API
  slug: vastdata-apitokens-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: This endpoint provides basic settings for users that do not have permissions to access any security realm."
  name: VAST Data basicsettings API
  slug: vastdata-basicsettings-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: BGP Configs are Border Gateway Protocol (BGP) configurations. You can configure a virtual IP pool to use layer 3 connectivity, instead of the default layer 2 connectivity, by attaching a BGP configura
  name: VAST Data bgpconfigs API
  slug: vastdata-bgpconfigs-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The Blob Expansions API from VAST Data — 5 operation(s) for blob expansions.
  name: VAST Data Blob Expansions API
  slug: vastdata-blob-expansions-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The Block Hosts API from VAST Data — 1 operation(s) for block hosts.
  name: VAST Data Block Hosts API
  slug: vastdata-block-hosts-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Block Hosts are block storage client hosts. They must be added to VMS in order to enable block storage volumes to be made available to them.
  name: VAST Data blockhosts API
  slug: vastdata-blockhosts-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Block Mappings are mappings of Blockhosts to Volumes. They make block storage volumes available to block storage hosts.
  name: VAST Data blockmappings API
  slug: vastdata-blockmappings-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The callhomeconfigs path provides access to the cluster's Call Home configuration. Call Home is a service that sends non-sensitive data from your VAST Cluster to our central support server to enable u
  name: VAST Data callhomeconfigs API
  slug: vastdata-callhomeconfigs-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: This endpoint enables you to query capacity details of any path on any tenant and its direct child paths."
  name: VAST Data capacity API
  slug: vastdata-capacity-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Carriers represent DBox slots that house SSDs and NVRAMs.
  name: VAST Data carriers API
  slug: vastdata-carriers-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: A CBox is a server chassis containing four CNodes. The cboxes path represents the CBoxes in the cluster, exposes information about the cBoxes and maintenance operations.
  name: VAST Data cboxes API
  slug: vastdata-cboxes-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The Certificates API from VAST Data — 3 operation(s) for certificates.
  name: VAST Data Certificates API
  slug: vastdata-certificates-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Challenge tokens are used to unlock the cluster's indestructibility mechanism.
  name: VAST Data challengetokens API
  slug: vastdata-challengetokens-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: VMS manages configuration of a single VAST cluster. The clusters path provides access to many configurations and settings that apply to the cluster.
  name: VAST Data clusters API
  slug: vastdata-clusters-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: CNode groups are groups of CNodes that managed applications can run on. See also Managed Applications.
  name: VAST Data cnodegroups API
  slug: vastdata-cnodegroups-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The Cnodes API from VAST Data — 8 operation(s) for cnodes.
  name: VAST Data Cnodes API
  slug: vastdata-cnodes-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The columns endpoint enables you to manage the columns in tables in a schema in a VAST database.
  name: VAST Data columns API
  slug: vastdata-columns-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The Compute Clusters API from VAST Data — 23 operation(s) for compute clusters.
  name: VAST Data Compute Clusters API
  slug: vastdata-compute-clusters-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The config API from VAST Data — 3 operation(s) for config.
  name: VAST Data config API
  slug: vastdata-config-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The dataspace API from VAST Data — 2 operation(s) for dataspace.
  name: VAST Data dataspace API
  slug: vastdata-dataspace-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: A DBox is an NVMe-oF JBOF, otherwise known as a VAST enclosure, or an enclosure containing NVMe-oF controller cards and flash SSDs. The dboxes path represents the DBoxes in the cluster, exposes inform
  name: VAST Data dboxes API
  slug: vastdata-dboxes-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The delta API from VAST Data — 2 operation(s) for delta.
  name: VAST Data delta API
  slug: vastdata-delta-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: A DNode is an NVMe-oF controller card in a DBox. The dnodes path represents the DNodes in the cluster, exposes information about the DNodes and maintenance operations.
  name: VAST Data dnodes API
  slug: vastdata-dnodes-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The DNS path represents a VAST Cluster DNS service. You can create one VAST Cluster DNS service per cluster. The VAST Cluster DNS service can distribute incoming DNS requests to specific VIP pools, ac
  name: VAST Data dns API
  slug: vastdata-dns-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: A DTray is a component of the CERES DBox. It is a canister that has two DNodes installed within. The DTray is a component of the CERES DBox. There are two Dtrays in each CERES DBox.
  name: VAST Data dtrays API
  slug: vastdata-dtrays-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: An EBox is a VAST enclosure that contains a server and SSDs. The server runs a CNode and two DNodes in containers.
  name: VAST Data eboxes API
  slug: vastdata-eboxes-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: An encrypted path is a path that is encrypted with a dedicated encryption group which is a subgroup of the encryption group of the tenant on which the path resides. Encrypted paths can be created on a
  name: VAST Data encryptedpaths API
  slug: vastdata-encryptedpaths-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: When data encryption is enabled on a VAST cluster with keys managed by an external key manager, each tenant must belong to an encryption group. Multiple tenants can belong to the same encryption group
  name: VAST Data encryptiongroups API
  slug: vastdata-encryptiongroups-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The envs API from VAST Data — 2 operation(s) for envs.
  name: VAST Data envs API
  slug: vastdata-envs-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The eventdefinitionconfigs path exposes event definition configurations that affect event definitions and quotas. These include default actions that apply globally to event definitions and are overrid
  name: VAST Data eventdefinitionconfigs API
  slug: vastdata-eventdefinitionconfigs-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Event definitions define the conditions that trigger events, the raising of alarms, alarm severity, and which actions are triggered on events, such as email notifications, webhooks and sending to sysl
  name: VAST Data eventdefinitions API
  slug: vastdata-eventdefinitions-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: VMS logs system driven events, such as changes to object states and properties, and user driven events, such as the creation, modification or deletion of any object in the system.
  name: VAST Data events API
  slug: vastdata-events-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Fans represent fans on the CBoxes and DBoxes
  name: VAST Data fans API
  slug: vastdata-fans-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The filesystem API from VAST Data — 1 operation(s) for filesystem.
  name: VAST Data filesystem API
  slug: vastdata-filesystem-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The folders endpoint enables the ability to manage directories and to set and get a directory's owner user and group attributes.
  name: VAST Data folders API
  slug: vastdata-folders-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: 'Global snapshot streams create instantly writable directories cloned from snapshots. Clones can be created from any snapshot residing on the cluster itself or on a cluster that has a replication peer '
  name: VAST Data globalsnapstreams API
  slug: vastdata-globalsnapstreams-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: 'Groups are user groups that can be authorized to access any data on the cluster via any supported client protocol. The groups path provides: management of groups on the cluster''s local provider, query'
  name: VAST Data groups API
  slug: vastdata-groups-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The Health API from VAST Data — 1 operation(s) for health.
  name: VAST Data Health API
  slug: vastdata-health-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Hosts are network discoverable CNodes and DNodes that can be included in a new cluster configuration.
  name: VAST Data hosts API
  slug: vastdata-hosts-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The iamroles API from VAST Data — 4 operation(s) for iamroles.
  name: VAST Data iamroles API
  slug: vastdata-iamroles-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: 'VAST Cluster enables you to create and maintain immutable backups using a feature called Indestructibility. Snapshots and protection policies can be flagged indestructible and they are then protected '
  name: VAST Data indestructibility API
  slug: vastdata-indestructibility-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The injections API from VAST Data — 1 operation(s) for injections.
  name: VAST Data injections API
  slug: vastdata-injections-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The iodata path provides data flow analytics.
  name: VAST Data iodata API
  slug: vastdata-iodata-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The issues API from VAST Data — 2 operation(s) for issues.
  name: VAST Data issues API
  slug: vastdata-issues-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Kafka Broker is the VAST Event Broker. Event publishing is available for S3 bucket views. In the context of event publishing, an event is a change that has occurred for an element in VAST Element Stor
  name: VAST Data kafkabroker API
  slug: vastdata-kafkabroker-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The Kerberos API from VAST Data — 4 operation(s) for kerberos.
  name: VAST Data Kerberos API
  slug: vastdata-kerberos-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Lightweight Directory Access Protocol (LDAP)-based directory servers may store and provide POSIX user and group attributes, as used by the NFS client access protocol. Up to two LDAP configurations are
  name: VAST Data ldaps API
  slug: vastdata-ldaps-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: A license entitles the VAST Cluster operator to an amount of storage capacity for a given period from a given start time. Licenses can be aggregated to increase the licensed capacity. Operating a VAST
  name: VAST Data licenses API
  slug: vastdata-licenses-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Local Providers are providers configured on the cluster, to which you can add users for authorizing access to the cluster or tenants of the cluster.
  name: VAST Data localproviders API
  slug: vastdata-localproviders-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Local S3 Keys are S3 access keys created for and owned by users on local providers.
  name: VAST Data locals3keys API
  slug: vastdata-locals3keys-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: NLMv4 locks help NFSv3 clients protect NFS files from data consistency conflicts. NFS client applications can acquire read or write NLM locks on byte ranges or on whole files. VAST Cluster uses NSM to
  name: VAST Data locks API
  slug: vastdata-locks-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The login path is used to log into VMS.
  name: VAST Data login API
  slug: vastdata-login-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The logout path is used to log out of VMS.
  name: VAST Data logout API
  slug: vastdata-logout-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Managed applications is a feature that enables you to run 3D applications on CNodes by distributing an image across a group of CNodes.
  name: VAST Data managedapplications API
  slug: vastdata-managedapplications-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: VAST Management System (VMS) users are called managers. A manager has login credentials and must be assigned at least one role in order to have any VMS permissions. A manager can have multiple roles.
  name: VAST Data managers API
  slug: vastdata-managers-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Metrics available to be included in analytics reports (using the /monitors/ endpoint) can be listed using either the /metrics/ endpoint or the /analytics/ endpoint.
  name: VAST Data metrics API
  slug: vastdata-metrics-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The modules API from VAST Data — 2 operation(s) for modules.
  name: VAST Data modules API
  slug: vastdata-modules-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Monitors are analytics reports that can provide insight into capacity utilization and cluster performance. Top performer analytics are performance metrics of the n most active client users, views, cli
  name: VAST Data monitors API
  slug: vastdata-monitors-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: A replication peer is a remote cluster configured as a peer for async replication. A replication peer also represents a configured and mirrored async replication relationship between two clusters.
  name: VAST Data nativereplicationremotetargets API
  slug: vastdata-nativereplicationremotetargets-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The nicports API from VAST Data — 3 operation(s) for nicports.
  name: VAST Data nicports API
  slug: vastdata-nicports-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: NICs represent interfaces on Network Interface Cards (NICs) in the CNodes and DNodes.
  name: VAST Data nics API
  slug: vastdata-nics-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: NIS is a supported external authorization provider. NIS can be used for authorizing user access to files and directories via NFS. NIS netgroups can be used to specify NFS hosts in view policies when c
  name: VAST Data nis API
  slug: vastdata-nis-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: NVRAMs represent flash SSDs resident in DBoxes that are deployed as SCM devices, formerly known as NVRAM devices.
  name: VAST Data nvrams API
  slug: vastdata-nvrams-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Object permissions reflect the access types, permission realms and managers associated with each object type. They can be listed but not modified.
  name: VAST Data objectpermissions API
  slug: vastdata-objectpermissions-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The oidcs API from VAST Data — 3 operation(s) for oidcs.
  name: VAST Data oidcs API
  slug: vastdata-oidcs-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The openfilehandles API from VAST Data — 2 operation(s) for openfilehandles.
  name: VAST Data openfilehandles API
  slug: vastdata-openfilehandles-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The openfiles API from VAST Data — 3 operation(s) for openfiles.
  name: VAST Data openfiles API
  slug: vastdata-openfiles-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The openfilesqueries API from VAST Data — 2 operation(s) for openfilesqueries.
  name: VAST Data openfilesqueries API
  slug: vastdata-openfilesqueries-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The permissions endpoint returns permissions that can be assigned to VMS managers and roles. VMS Each permission enables a type of permission, such as create or read permission, on a realm. Each realm
  name: VAST Data permissions API
  slug: vastdata-permissions-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Ports represent switch ports.
  name: VAST Data ports API
  slug: vastdata-ports-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Projection columns are columns that are included in a projection, either as the columns used to sort the projection or as additional columns included in a projection.
  name: VAST Data projectioncolumns API
  slug: vastdata-projectioncolumns-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Projections are subsets of a full table in the VAST Database that allow for optimized queries that use only the columns included in the projection.
  name: VAST Data projections API
  slug: vastdata-projections-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: prometheusmetrics is VAST's Prometheus exporter resource. Prometheus is an open-source systems monitoring and alerting toolkit that provides a data model for describing and recording metrics over time
  name: VAST Data prometheusmetrics API
  slug: vastdata-prometheusmetrics-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: A protected path is a data path in the Element Store (file/object system) that is protected by snapshots which may be replicated to an S3 replication peer or to an async replication peer. Scheduling a
  name: VAST Data protectedpaths API
  slug: vastdata-protectedpaths-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: A protection policy is a reusable configuration that defines a schedule for taking snapshots and optionally replicating them to a specified async replication peer or S3 replication peer. It defines ho
  name: VAST Data protectionpolicies API
  slug: vastdata-protectionpolicies-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: PSUs represent power supply units on the CBoxes and DBoxes.
  name: VAST Data psus API
  slug: vastdata-psus-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The QoS Policies API from VAST Data — 1 operation(s) for qos policies.
  name: VAST Data QoS Policies API
  slug: vastdata-qos-policies-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Quality of Service policies enable you to define quality of service per view. Quality of service policies can set maximum limits on read and write bandwidth and IOPS per view.
  name: VAST Data qospolicies API
  slug: vastdata-qospolicies-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: QuotaEntityInfo objects contain details of all users and groups that wrote to quota directories. Provides VAST-internal ID from the VAST Cluster user database and email address.
  name: VAST Data quotaentityinfos API
  slug: vastdata-quotaentityinfos-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The quotagroups API from VAST Data — 5 operation(s) for quotagroups.
  name: VAST Data quotagroups API
  slug: vastdata-quotagroups-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: A quota limits the amount of storage and/or the number of files or objects and directories that can be contained in a specified directory. A quota can include default limits on usage per user and grou
  name: VAST Data quotas API
  slug: vastdata-quotas-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The Racks API from VAST Data — 6 operation(s) for racks.
  name: VAST Data Racks API
  slug: vastdata-racks-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Realms are user defined customized permission realms for VMS manager users. They define sets of object types and can be granted to managers and roles for VMS permissions.
  name: VAST Data realms API
  slug: vastdata-realms-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The replicationpolicies API from VAST Data — 2 operation(s) for replicationpolicies.
  name: VAST Data replicationpolicies API
  slug: vastdata-replicationpolicies-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: A replication restore point is a location to which a snapshot was replicated and from which files can be restored.A restore point may reside on an S3 replication peer or on an async replication peer.
  name: VAST Data replicationrestorepoints API
  slug: vastdata-replicationrestorepoints-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: This path enables you to manage replication streams. Note that for the general case, replication streams belong to protected paths and are managed as part of protected path management. However, for th
  name: VAST Data replicationstreams API
  slug: vastdata-replicationstreams-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: 'An S3 replication peer represents a specific S3 destination to which snapshots can be replicated or were replicated. S3 replication peers can be configured in order to enable replication of data to a '
  name: VAST Data replicationtargets API
  slug: vastdata-replicationtargets-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Roles are sets of VMS permissions. They can specify one or more LDAP groups. Mapping roles to LDAP groups gives LDAP group members the ability to log into VMS and be authorized with the aggregate of p
  name: VAST Data roles API
  slug: vastdata-roles-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The s3keys endpoint enables users to manage their own S3 access key pairs.
  name: VAST Data S3 Keys API
  slug: vastdata-s3-keys-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: 'An S3 Lifecycle configuration is a set of rules that define actions that an S3 service applies to a group of objects. VAST Cluster supports S3 Lifecycle configurations that define expiration actions. '
  name: VAST Data s3lifecyclerules API
  slug: vastdata-s3lifecyclerules-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Identity policies comprise statements that grant or deny permissions for any combination of specific actions on any combination of specified resources. They are the primary access control method avail
  name: VAST Data s3policies API
  slug: vastdata-s3policies-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The schemas endpoint enables you to manage the schemas in a VAST database.
  name: VAST Data schemas API
  slug: vastdata-schemas-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The settingsdiff API from VAST Data — 1 operation(s) for settingsdiff.
  name: VAST Data settingsdiff API
  slug: vastdata-settingsdiff-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The snapshotpolicies API from VAST Data — 2 operation(s) for snapshotpolicies.
  name: VAST Data snapshotpolicies API
  slug: vastdata-snapshotpolicies-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: A snapshot is an image of the data existing at a point in time under a specific Element Store path. Snapshots can be created on a one off basis or scheduled using a protected path. Scheduled snapshots
  name: VAST Data snapshots API
  slug: vastdata-snapshots-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: SSDs represent flash SSDs resident in the cluster's DBoxes.
  name: VAST Data ssds API
  slug: vastdata-ssds-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The subnetmanager monitors an OpenSM service. Clusters operating in larger IB networks must have an OpenSM service configured on some of the CNodes in the cluster. The OpenSM services running on those
  name: VAST Data subnetmanager API
  slug: vastdata-subnetmanager-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The Support Bundles API from VAST Data — 2 operation(s) for support bundles.
  name: VAST Data Support Bundles API
  slug: vastdata-support-bundles-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: A support bundle is a compressed file consisting of logs that are extracted from the VAST Cluster. Support bundles can be sent to VAST Support for troubleshooting purposes. They can also be downloaded
  name: VAST Data supportbundles API
  slug: vastdata-supportbundles-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The supporteddrives API from VAST Data — 2 operation(s) for supporteddrives.
  name: VAST Data supporteddrives API
  slug: vastdata-supporteddrives-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Switches represent switches in the cluster.
  name: VAST Data switches API
  slug: vastdata-switches-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: With VAST Database you can store, access and manage tabular data on a VAST cluster. The tables endpoint enables you to interface with the VAST Database tables. You can create tables, filter data, perf
  name: VAST Data tables API
  slug: vastdata-tables-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The Tenants API from VAST Data — 21 operation(s) for tenants.
  name: VAST Data Tenants API
  slug: vastdata-tenants-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The tlscertificates API from VAST Data — 4 operation(s) for tlscertificates.
  name: VAST Data tlscertificates API
  slug: vastdata-tlscertificates-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Tokens are JSON Web Tokens (JWTs), which can be used instead of Apitokens to authenticate requests to the VMS REST API.
  name: VAST Data token API
  slug: vastdata-token-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Topics store categories of events collected by VAST Event Broker.
  name: VAST Data topics API
  slug: vastdata-topics-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: A userquota object defines a user or group quota. A user or group quota limits the capacity and number of files or directories that a specified user or group can own within a directory. A userquota ob
  name: VAST Data userquotas API
  slug: vastdata-userquotas-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Users who can be authorized to access any data on the cluster via any supported client protocol can be created on a local provider. They are more typically stored on external authorization providers (
  name: VAST Data users API
  slug: vastdata-users-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: 'The VAST audit log is a database that can store VAST cluster protocol audits. If protocol auditing is enabled and configured to be logged to VAST audit log, the endpoint can be used to query the VAST '
  name: VAST Data vastauditlog API
  slug: vastdata-vastauditlog-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The bigcatalogconfig endpoint enables you to manage the configuration of VAST Catalog and to query the VAST Catalog. VAST Catalog is a database that indexes metadata attributes of all data on the clus
  name: VAST Data vastcatalogconfig API
  slug: vastdata-vastcatalogconfig-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The bigcatalogindexedcolumns endpoint enables you to add columns to the VAST Catalog table for S3 tags and S3 metadata attributes.
  name: VAST Data vastcatalogindexedcolumns API
  slug: vastdata-vastcatalogindexedcolumns-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The vastdb API from VAST Data — 1 operation(s) for vastdb.
  name: VAST Data vastdb API
  slug: vastdata-vastdb-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The cluster platform and VMS software is installed and upgraded via packages that have a version number per release and a software build number. The versions path exposes the cluster's version history
  name: VAST Data versions API
  slug: vastdata-versions-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: A view policy specifies view configuration parameters. A view policy can be used by multiple views. Every view is attached to one view policy.
  name: VAST Data viewpolicies API
  slug: vastdata-viewpolicies-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The Views API from VAST Data — 10 operation(s) for views.
  name: VAST Data Views API
  slug: vastdata-views-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: 'A VIP pool is a pool of virtual IP operations (VIPs). VAST Cluster listens on VIPs for requests from data traffic. Each VIP pool is dedicated to one of two roles: PROTOCOLS or REPLICATION. Protocols V'
  name: VAST Data vippools API
  slug: vastdata-vippools-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: A VIP is a virtual IP address that belongs to a VIP pool.
  name: VAST Data vips API
  slug: vastdata-vips-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Virtual machines can include EBox hosts and virtual machine hosts that comprise VAST on Cloud (VoC) clusters. Each virtual machine runs CNodes and DNodes in containers. Both EBoxes and GCP VoC virtual
  name: VAST Data vm API
  slug: vastdata-vm-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The VMS path represents VMS settings, such as the management VIP used to access the VMS interfaces, login banner text for the VMS CLI and Web UI, access token lifetimes for the REST API and more.
  name: VAST Data vms API
  slug: vastdata-vms-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The Volumes API from VAST Data — 7 operation(s) for volumes.
  name: VAST Data Volumes API
  slug: vastdata-volumes-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The vpntunnels API from VAST Data — 3 operation(s) for vpntunnels.
  name: VAST Data vpntunnels API
  slug: vastdata-vpntunnels-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The vsettings API from VAST Data — 1 operation(s) for vsettings.
  name: VAST Data vsettings API
  slug: vastdata-vsettings-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: The vtasks API from VAST Data — 3 operation(s) for vtasks.
  name: VAST Data vtasks API
  slug: vastdata-vtasks-api
- baseURL: https://{vms-host}/api
  baseurl_source: declared
  description: Webhooks send event information to external applications. Once defined, you can set them to be triggered by specific events.
  name: VAST Data webhooks API
  slug: vastdata-webhooks-api
artifact_total: 256
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VAST API Swagger Schema activedirectory API
  slug: open-vastdata-activedirectory-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory alarms API
  slug: open-vastdata-alarms-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory apitokens API
  slug: open-vastdata-apitokens-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory basicsettings API
  slug: open-vastdata-basicsettings-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory bgpconfigs API
  slug: open-vastdata-bgpconfigs-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory Blob Expansions API
  slug: open-vastdata-blob-expansions-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory Block Hosts API
  slug: open-vastdata-block-hosts-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory blockhosts API
  slug: open-vastdata-blockhosts-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory blockmappings API
  slug: open-vastdata-blockmappings-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory callhomeconfigs API
  slug: open-vastdata-callhomeconfigs-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory capacity API
  slug: open-vastdata-capacity-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory carriers API
  slug: open-vastdata-carriers-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory cboxes API
  slug: open-vastdata-cboxes-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory Certificates API
  slug: open-vastdata-certificates-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory challengetokens API
  slug: open-vastdata-challengetokens-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory clusters API
  slug: open-vastdata-clusters-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory cnodegroups API
  slug: open-vastdata-cnodegroups-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory Cnodes API
  slug: open-vastdata-cnodes-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory columns API
  slug: open-vastdata-columns-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory Compute Clusters API
  slug: open-vastdata-compute-clusters-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory config API
  slug: open-vastdata-config-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory dataspace API
  slug: open-vastdata-dataspace-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory dboxes API
  slug: open-vastdata-dboxes-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory delta API
  slug: open-vastdata-delta-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory dnodes API
  slug: open-vastdata-dnodes-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory dns API
  slug: open-vastdata-dns-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory dtrays API
  slug: open-vastdata-dtrays-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory eboxes API
  slug: open-vastdata-eboxes-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory encryptedpaths API
  slug: open-vastdata-encryptedpaths-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory encryptiongroups API
  slug: open-vastdata-encryptiongroups-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory envs API
  slug: open-vastdata-envs-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory eventdefinitionconfigs API
  slug: open-vastdata-eventdefinitionconfigs-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory eventdefinitions API
  slug: open-vastdata-eventdefinitions-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory events API
  slug: open-vastdata-events-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory fans API
  slug: open-vastdata-fans-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory filesystem API
  slug: open-vastdata-filesystem-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory folders API
  slug: open-vastdata-folders-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory globalsnapstreams API
  slug: open-vastdata-globalsnapstreams-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory groups API
  slug: open-vastdata-groups-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory Health API
  slug: open-vastdata-health-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory hosts API
  slug: open-vastdata-hosts-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory iamroles API
  slug: open-vastdata-iamroles-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory indestructibility API
  slug: open-vastdata-indestructibility-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory injections API
  slug: open-vastdata-injections-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory iodata API
  slug: open-vastdata-iodata-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory issues API
  slug: open-vastdata-issues-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory kafkabroker API
  slug: open-vastdata-kafkabroker-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory Kerberos API
  slug: open-vastdata-kerberos-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory ldaps API
  slug: open-vastdata-ldaps-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory licenses API
  slug: open-vastdata-licenses-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory localproviders API
  slug: open-vastdata-localproviders-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory locals3keys API
  slug: open-vastdata-locals3keys-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory locks API
  slug: open-vastdata-locks-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory login API
  slug: open-vastdata-login-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory logout API
  slug: open-vastdata-logout-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory managedapplications API
  slug: open-vastdata-managedapplications-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory managers API
  slug: open-vastdata-managers-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory metrics API
  slug: open-vastdata-metrics-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory modules API
  slug: open-vastdata-modules-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory monitors API
  slug: open-vastdata-monitors-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory nativereplicationremotetargets API
  slug: open-vastdata-nativereplicationremotetargets-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory nicports API
  slug: open-vastdata-nicports-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory nics API
  slug: open-vastdata-nics-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory nis API
  slug: open-vastdata-nis-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory nvrams API
  slug: open-vastdata-nvrams-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory objectpermissions API
  slug: open-vastdata-objectpermissions-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory oidcs API
  slug: open-vastdata-oidcs-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory openfilehandles API
  slug: open-vastdata-openfilehandles-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory openfiles API
  slug: open-vastdata-openfiles-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory openfilesqueries API
  slug: open-vastdata-openfilesqueries-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory permissions API
  slug: open-vastdata-permissions-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory ports API
  slug: open-vastdata-ports-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory projectioncolumns API
  slug: open-vastdata-projectioncolumns-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory projections API
  slug: open-vastdata-projections-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory prometheusmetrics API
  slug: open-vastdata-prometheusmetrics-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory protectedpaths API
  slug: open-vastdata-protectedpaths-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory protectionpolicies API
  slug: open-vastdata-protectionpolicies-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory psus API
  slug: open-vastdata-psus-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory QoS Policies API
  slug: open-vastdata-qos-policies-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory qospolicies API
  slug: open-vastdata-qospolicies-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory quotaentityinfos API
  slug: open-vastdata-quotaentityinfos-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory quotagroups API
  slug: open-vastdata-quotagroups-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory quotas API
  slug: open-vastdata-quotas-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory Racks API
  slug: open-vastdata-racks-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory realms API
  slug: open-vastdata-realms-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory replicationpolicies API
  slug: open-vastdata-replicationpolicies-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory replicationrestorepoints API
  slug: open-vastdata-replicationrestorepoints-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory replicationstreams API
  slug: open-vastdata-replicationstreams-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory replicationtargets API
  slug: open-vastdata-replicationtargets-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory roles API
  slug: open-vastdata-roles-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory S3 Keys API
  slug: open-vastdata-s3-keys-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory s3lifecyclerules API
  slug: open-vastdata-s3lifecyclerules-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory s3policies API
  slug: open-vastdata-s3policies-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory schemas API
  slug: open-vastdata-schemas-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory settingsdiff API
  slug: open-vastdata-settingsdiff-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory snapshotpolicies API
  slug: open-vastdata-snapshotpolicies-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory snapshots API
  slug: open-vastdata-snapshots-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory ssds API
  slug: open-vastdata-ssds-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory subnetmanager API
  slug: open-vastdata-subnetmanager-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory Support Bundles API
  slug: open-vastdata-support-bundles-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory supportbundles API
  slug: open-vastdata-supportbundles-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory supporteddrives API
  slug: open-vastdata-supporteddrives-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory switches API
  slug: open-vastdata-switches-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory tables API
  slug: open-vastdata-tables-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory Tenants API
  slug: open-vastdata-tenants-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory tlscertificates API
  slug: open-vastdata-tlscertificates-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory token API
  slug: open-vastdata-token-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory topics API
  slug: open-vastdata-topics-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory userquotas API
  slug: open-vastdata-userquotas-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory users API
  slug: open-vastdata-users-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory vastauditlog API
  slug: open-vastdata-vastauditlog-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory vastcatalogconfig API
  slug: open-vastdata-vastcatalogconfig-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory vastcatalogindexedcolumns API
  slug: open-vastdata-vastcatalogindexedcolumns-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory vastdb API
  slug: open-vastdata-vastdb-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory versions API
  slug: open-vastdata-versions-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory viewpolicies API
  slug: open-vastdata-viewpolicies-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory Views API
  slug: open-vastdata-views-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory vippools API
  slug: open-vastdata-vippools-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory vips API
  slug: open-vastdata-vips-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory vm API
  slug: open-vastdata-vm-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory vms API
  slug: open-vastdata-vms-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory Volumes API
  slug: open-vastdata-volumes-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory vpntunnels API
  slug: open-vastdata-vpntunnels-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory vsettings API
  slug: open-vastdata-vsettings-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory vtasks API
  slug: open-vastdata-vtasks-api
- collection_type: open
  name: VAST API Swagger Schema activedirectory webhooks API
  slug: open-vastdata-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/vastdata-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://vastdata.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.vastdata.com/platform/developers
- group: docs
  title: ''
  type: Documentation
  url: https://support.vastdata.com/s/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/vast-data/cosmos-labs
- group: operate
  title: ''
  type: Support
  url: https://community.vastdata.com/
- group: company
  title: ''
  type: Blog
  url: https://www.vastdata.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vast-data
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vastdata.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vastdata.com/legal/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/vastdata-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vastdata-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/vastdata-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vastdata-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/vastdata-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vastdata-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vastdata-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vastdata-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vastdata-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vastdata-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vastdata-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vastdata-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vastdata-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/vastdata-vms-overlay.yaml
created: '2026-07-17'
description: VAST Data is an enterprise AI infrastructure company building a unified data platform for AI. Its VAST AI Operating System combines the VAST DataStore (all-flash file, object, and block storage over NFS, SMB, S3, and CSI), VAST DataBase (structured data, vectors, and streams), VAST DataSpace (a global namespace across on-prem, cloud, and edge), and VAST DataEngine (serverless functions, event triggers, and a Kafka-compatible broker). Everything is managed through the VAST Management System (VMS) REST API — an OpenAPI-documented surface with 770+ operations — plus official Python and Go SDKs, a Terraform provider, the vastde DataEngine CLI, an official MCP server for cluster administration, and published agent skills.
image: https://github.com/vast-data.png
layout: provider
mcp_servers:
- description: 'Official VAST Admin MCP Server — a Model Context Protocol server for VAST Data cluster administration. Gives AI assistants tools to monitor, list, and manage VAST clusters (views, tenants, snapshots, '
  name: VAST Data MCP Server
  slug: vast-data-mcp-server
modified: '2026-07-21'
name: VAST Data
nav: Providers
network: true
overview: 'VAST Data publishes 126 APIs on the [APIs.io](https://apis.io/) network, including activedirectory API, alarms API, apitokens API, and 123 more. Tagged areas include Company, Infrastructure, Storage, Data, and Artificial Intelligence.


  VAST Data''s developer surface includes documentation, getting-started guide, support, engineering blog, authentication, CLI, and 19 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 24.0
    catalog_earned_first_party: 0.0
    catalog_gap: 91.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 50.2
    developer_ergonomics: 71.4
    discoverability: 51.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 37.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 126
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vastdata/refs/heads/main/screenshots/vastdata-2026-09-02T165457.png
security:
- kind: authentication
  name: Vastdata Authentication
  slug: vastdata-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Vastdata Domain Security
  slug: vastdata-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: vastdata
tags:
- Company
- Infrastructure
- Storage
- Data
- Artificial Intelligence
- Database
- Kubernetes
- HPC
website: https://vastdata.com
---
