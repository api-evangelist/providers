---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 756
  human_in_the_loop: 18
  name: Pure Storage Agentic Access
  operation_count: 1309
  slug: pure-storage-agentic-access
  summary_line: 1309 operations · 756 acting · 18 human-in-the-loop
api_count: 130
apis:
- description: Kubernetes-native data services platform from Pure Storage. Portworx exposes its API surface through Custom Resource Definitions managed by the libopenstorage operator and the portworx/apis CRDs, enab
  name: Portworx Kubernetes API
  slug: portworx-kubernetes-api
- description: Active Directory configuration authenticates users for NFS using Kerberos or SMB using Kerberos or New Technology LAN Manager (NTLM). Active Directory is also used to authorize users by mapping identi
  name: Pure Storage Active Directory API
  slug: pure-storage-active-directory-api
- description: The FlashArray has a single default administrative account named pureuser. The administrator can add, delete, and modify administrators on the array. Administrators are assigned management access poli
  name: Pure Storage Administrators API
  slug: pure-storage-administrators-api
- description: Alert watchers receive email notifications when alerts occur on an array.
  name: Pure Storage Alert Watchers API
  slug: pure-storage-alert-watchers-api
- description: Alerts indicate significant events that occur on an array, including whenever a component degrades or the capacity threshold of the component is reached.
  name: Pure Storage Alerts API
  slug: pure-storage-alerts-api
- description: An API client represents an identity type. API clients are created on the array. To create an API client, register and then enable it on the array. After the API client has been created, the user name
  name: Pure Storage API Clients API
  slug: pure-storage-api-clients-api
- description: Apps that extend array functionality can be integrated into the Purity//FA operating system.
  name: Pure Storage Apps API
  slug: pure-storage-apps-api
- description: Manages connections between arrays.
  name: Pure Storage Array Connections API
  slug: pure-storage-array-connections-api
- description: Array features provide the ability to configure settings that affect the operation of the array as a whole and monitor array I/O performance.
  name: Pure Storage Arrays API
  slug: pure-storage-arrays-api
- description: View and manage audit log targets that are filesystems. These are filesystems where audit logs will be stored, and they may be configured in audit policies.
  name: Pure Storage Audit Log Target for File Systems API
  slug: pure-storage-audit-log-target-for-file-systems-api
- description: View and manage audit log targets for object store. These are buckets where audit logs will be stored, and they may be configured in audit policies.
  name: Pure Storage Audit Log Target for Object Store API
  slug: pure-storage-audit-log-target-for-object-store-api
- description: Audit trail records describe administrative actions performed by a user to modify the configuration of an array.
  name: Pure Storage Audits API
  slug: pure-storage-audits-api
- description: Pure Storage uses the OAuth 2.0 Token Exchange authorization grant and JSON Web Tokens (JWTs) to authenticate to the Pure Storage REST API. Before you can exchange the ID token for an access token, cr
  name: Pure Storage Authorization API
  slug: pure-storage-authorization-api
- description: Displays the detailed information of each blade in the array.
  name: Pure Storage Blades API
  slug: pure-storage-blades-api
- description: Object replication requires a replica link that connects a source bucket to a remote bucket. The configuration of a replica link includes remote credentials, bucket names, remote names, replication st
  name: Pure Storage Bucket Replica Links API
  slug: pure-storage-bucket-replica-links-api
- description: Manages the creation, attributes, and deletion of buckets on the array.
  name: Pure Storage Buckets API
  slug: pure-storage-buckets-api
- description: Certificate groups, also known as certificate bundles, are collections of digital certificates. Each certificate can belong to one or more groups in order to serve different purposes.
  name: Pure Storage Certificate Groups API
  slug: pure-storage-certificate-groups-api
- description: Purity//FA creates a self-signed certificate and private key when you start the system for the first time. You can use the default certificate, change the certificate attributes, create a new self-sig
  name: Pure Storage Certificates API
  slug: pure-storage-certificates-api
- description: Displays an NFS client’s performance metrics on the array for read, write, and meta operations.
  name: Pure Storage Clients API
  slug: pure-storage-clients-api
- description: A connection gives hosts access to volumes on the array.
  name: Pure Storage Connections API
  slug: pure-storage-connections-api
- description: 'Default protection is a list of protection groups that are applied to newly created volumes. Volumes can opt out of the default protection at creation. The pod''s `default_protections` defaults to the '
  name: Pure Storage Container Default Protections API
  slug: pure-storage-container-default-protections-api
- description: Controller data includes the name, mode, FlashArray model, Purity//FA software version, and status of each controller in the array.
  name: Pure Storage Controllers API
  slug: pure-storage-controllers-api
- description: Important file system directories should be set up as managed directories. Managed directories can have policies attached to them. Managed directories differ from standard directories in that they pro
  name: Pure Storage Directories API
  slug: pure-storage-directories-api
- description: Managed directory exports are created by adding NFS or SMB export policies to managed directories.
  name: Pure Storage Directory Exports API
  slug: pure-storage-directory-exports-api
- description: Directory quotas provide the ability to set capacity limits on managed directories.
  name: Pure Storage Directory Quotas API
  slug: pure-storage-directory-quotas-api
- description: Manages directory service configurations for integration with LDAP servers (e.g. Active Directory and OpenLDAP) in order to support various array services.
  name: Pure Storage Directory Services API
  slug: pure-storage-directory-services-api
- description: Directory snapshots are created manually or by adding snapshot policies to managed directories. Each snapshot policy can be re-used for multiple directories.
  name: Pure Storage Directory Snapshots API
  slug: pure-storage-directory-snapshots-api
- description: DNS attributes include the domain suffix, static name servers, mode (static or DHCP), and search domain. The configured attributes can be listed.
  name: Pure Storage DNS API
  slug: pure-storage-dns-api
- description: Drive data includes the name, type, status, capacity, protocol and other information for all flash, NVRAM, and cache modules in an array.
  name: Pure Storage Drives API
  slug: pure-storage-drives-api
- description: Manages the creation, attributes, and deletion of file system exports. Exports link either an NFS Export Policy or a SMB Client Policy, a file system, and a server.
  name: Pure Storage File System Exports API
  slug: pure-storage-file-system-exports-api
- description: Manages the creation, and deletion of file system junctions. Junctions link a specific path in the origin file system to the root of a destination file system.
  name: Pure Storage File System Junctions API
  slug: pure-storage-file-system-junctions-api
- description: File system replication requires a replica link that connects a source array to a remote target. The configuration of a replica link includes policies, file system names, remote names, and replication
  name: Pure Storage File System Replica Links API
  slug: pure-storage-file-system-replica-links-api
- description: 'A file system snapshot is a point-in-time copy of a file system. Multiple snapshots of a file system can be copied for different points in time. A snapshot policy can also be applied to a file system '
  name: Pure Storage File System Snapshots API
  slug: pure-storage-file-system-snapshots-api
- description: A FlashArray can contain up to 24 separate file systems, each with a number of directories that can be exported via supported protocols. Clients, using Active Directory or LDAP, can connect and access
  name: Pure Storage File Systems API
  slug: pure-storage-file-systems-api
- description: The Files API from Pure Storage — 1 operation(s) for files.
  name: Pure Storage Files API
  slug: pure-storage-files-api
- description: A fleet is a collection of Arrays.
  name: Pure Storage Fleets API
  slug: pure-storage-fleets-api
- description: Operational status is reported by most of the hardware components in an array, including the chassis, controller, and storage shelf.
  name: Pure Storage Hardware API
  slug: pure-storage-hardware-api
- description: The endpoints are deprecated. Use the endpoints under Network Interfaces instead. Manages the port connector attributes on the array. Lane speeds and port count attributes can be configured.
  name: Pure Storage Hardware Connectors API
  slug: pure-storage-hardware-connectors-api
- description: Host groups implement consistent connections between a set of hosts and one or more volumes. Connections are consistent in the sense that all hosts associated with a host group address a volume connec
  name: Pure Storage Host Groups API
  slug: pure-storage-host-groups-api
- description: Hosts organize the storage network addresses (iSCSI Qualified Names, NVMe qualified names, or Fibre Channel world wide names) of client computers to identify the host's intiators. Hosts also control c
  name: Pure Storage Hosts API
  slug: pure-storage-hosts-api
- description: Provides information about Pure1 subscription invoices.
  name: Pure Storage Invoices API
  slug: pure-storage-invoices-api
- description: Keytab management functionality for Kerberos authentication.
  name: Pure Storage Keytabs API
  slug: pure-storage-keytabs-api
- description: 'The Key Management Interoperability Protocol (KMIP) server is used in combination with the Pure Storage Rapid Data Locking (RDL) feature and EncryptReduce feature to further secure the encrypted data '
  name: Pure Storage KMIP API
  slug: pure-storage-kmip-api
- description: Manages the creation, attributes, and deletion of holds on the array. A hold can be also applied to a path under a file system to mark the entries under the path as immutable.
  name: Pure Storage Legal Holds API
  slug: pure-storage-legal-holds-api
- description: A life cycle rule helps manage the number of copies of a specific bucket. A lifecycle rule can be applied to a bucket with a rule indicating the retention time before it is to be deleted.
  name: Pure Storage Lifecycle Rules API
  slug: pure-storage-lifecycle-rules-api
- description: Manages the link aggregation group (LAG) of Ethernet ports on the array.
  name: Pure Storage Link Aggregation Groups API
  slug: pure-storage-link-aggregation-groups-api
- description: Log Targets to be used to send management or data audit logs.
  name: Pure Storage Log Targets API
  slug: pure-storage-log-targets-api
- description: The array collects a log of command activities that can be used for analysis when the logs are sent to Pure Technical Services.
  name: Pure Storage Logs API
  slug: pure-storage-logs-api
- description: During a maintenance window, alerts are suppressed that are related to connections, paths, ports, and other resources that are down during maintenance.
  name: Pure Storage Maintenance Windows API
  slug: pure-storage-maintenance-windows-api
- description: Provides information about historical metrics for arrays, buckets, directories, file systems, pods, subscription licenses, and volumes.
  name: Pure Storage Metrics API
  slug: pure-storage-metrics-api
- description: Manages the interfaces and the network connection attributes of the array.
  name: Pure Storage Network Interfaces API
  slug: pure-storage-network-interfaces-api
- description: Node Groups can contain one or more nodes for file system creation management.
  name: Pure Storage Node Groups API
  slug: pure-storage-node-groups-api
- description: Manages the nodes for pNFS. These nodes are where the client will read/write to when pNFS is enabled.
  name: Pure Storage Nodes API
  slug: pure-storage-nodes-api
- description: Manages object store access keys. A maximum of two sets of keys can be created for each object store user. A set of keys consists of an access key ID and Secret Access Key.
  name: Pure Storage Object Store Access Keys API
  slug: pure-storage-object-store-access-keys-api
- description: Manages object store account exports. Exports expose accounts and their contained resources to servers.
  name: Pure Storage Object Store Account Exports API
  slug: pure-storage-object-store-account-exports-api
- description: Manages object store accounts. Accounts contain buckets and users. Accounts must be created before an object store user or buckets can be created.
  name: Pure Storage Object Store Accounts API
  slug: pure-storage-object-store-accounts-api
- description: Manages remote credentials for remote objects. Remote credentials contain access information that can be reused for multiple objects.
  name: Pure Storage Object Store Remote Credentials API
  slug: pure-storage-object-store-remote-credentials-api
- description: Manages the roles assumable by external federated entity. Each role is assigned a trust policy that determines which identity provider authorizes the entities and how.
  name: Pure Storage Object Store Roles API
  slug: pure-storage-object-store-roles-api
- description: Manages the object store users attributes. Each user is assigned to an object store account and given an access key.
  name: Pure Storage Object Store Users API
  slug: pure-storage-object-store-users-api
- description: Manages virtual host-style addressing for S3 requests to read or write an object within a bucket on the array.
  name: Pure Storage Object Store Virtual Hosts API
  slug: pure-storage-object-store-virtual-hosts-api
- description: The offload feature enables system administrators to replicate point-in-time volume snapshots from the array to an external storage system for long-term retention. Each offload target represents an ex
  name: Pure Storage Offloads API
  slug: pure-storage-offloads-api
- description: OIDC SSO allows customers to configure settings of OIDC service provider and identity provider. It provides a multi-factor authentication (MFA) mechanism for customers to log in to FlashBlade.
  name: Pure Storage OIDC SSO API
  slug: pure-storage-oidc-sso-api
- description: Pod replica links are created by associating a source pod with a demoted pod, making the demoted pod the target pod of the source pod. The direction of the replica link is from the promoted source pod
  name: Pure Storage Pod Replica Links API
  slug: pure-storage-pod-replica-links-api
- description: Synchronous replication is managed through pods. A pod representing a collection of protection groups and volumes is created on one array and stretched to another array, resulting in fully synchronize
  name: Pure Storage Pods API
  slug: pure-storage-pods-api
- description: Displays general information for all available types of policies and their members.
  name: Pure Storage Policies (All) API
  slug: pure-storage-policies-all-api
- description: Policies are used to create exports (i.e., shares) and schedule snapshots. NFS and SMB policies can be created and have one or more rules applied to them. Each policy can be reused, creating exports f
  name: Pure Storage Policies API
  slug: pure-storage-policies-api
- description: Manages audit policies for filesystems. These policies are composed of log target which contain the destination for audit logs.
  name: Pure Storage Policies - Audit for File Systems API
  slug: pure-storage-policies-audit-for-file-systems-api
- description: Manages audit policies for object store. These policies are composed of log targets which contain the destination for audit logs.
  name: Pure Storage Policies - Audit for Object Store API
  slug: pure-storage-policies-audit-for-object-store-api
- description: Manages file Data Eviction policies. These policies define controls that can be configured and attached to managed data lifecycle independently of the lifecycle of files.
  name: Pure Storage Policies - Data Eviction API
  slug: pure-storage-policies-data-eviction-api
- description: Manages management access policies. These policies are composed of rules which govern an administrative user's permissions when managing resources.
  name: Pure Storage Policies - Management Access API
  slug: pure-storage-policies-management-access-api
- description: Manages management authentication policies. These policies control what authentication factors are required when logging in to different management interfaces (e.g., SSH).
  name: Pure Storage Policies - Management Authentication API
  slug: pure-storage-policies-management-authentication-api
- description: Manages network access policies. These policies are composed of rules which govern a client's ability to access different product interfaces.
  name: Pure Storage Policies - Network Access API
  slug: pure-storage-policies-network-access-api
- description: Manages NFS export policies. These policies are composed of rules which govern a client's ability to access the exported filesystem.
  name: Pure Storage Policies - NFS API
  slug: pure-storage-policies-nfs-api
- description: Manages access policies for object store users. Administrators can assign policies to users for managing buckets and objects.
  name: Pure Storage Policies - Object Store Access API
  slug: pure-storage-policies-object-store-access-api
- description: Manages password policies. These policies define requirements for user passwords complexity and login attempts.
  name: Pure Storage Policies - Password API
  slug: pure-storage-policies-password-api
- description: Manages Quality of Service (QoS) policies. These policies define controls that can be configured and attached to managed objects to guarantee performance of workloads.
  name: Pure Storage Policies - QoS API
  slug: pure-storage-policies-qos-api
- description: Manages S3 export policies for Object Store Account Exports. These policies contain rules which govern which buckets from the account are actually exported to the servers.
  name: Pure Storage Policies - S3 Export API
  slug: pure-storage-policies-s3-export-api
- description: An SMB Client policy manages access to SMB file systems on a per-client basis. These policies can be applied to one or more file systems.
  name: Pure Storage Policies - SMB Client API
  slug: pure-storage-policies-smb-client-api
- description: An SMB Share policy manages access to SMB file systems on a per-user/group basis. These policies can be applied to one or more file systems.
  name: Pure Storage Policies - SMB Share API
  slug: pure-storage-policies-smb-share-api
- description: A snapshot policy manages the creation file system snapshots or it can applied to file system and object replication links for replication. These policies provide the user a way to control the frequen
  name: Pure Storage Policies - Snapshot API
  slug: pure-storage-policies-snapshot-api
- description: An SSH Certificate Authority policy manages the keys that are allowed to sign user SSH certificates for access to the array, as well as the principals that they require be encoded in certificates to a
  name: Pure Storage Policies - SSH Certificate Authority API
  slug: pure-storage-policies-ssh-certificate-authority-api
- description: 'A storage class tiering policy manages the criteria for tiering data within a filesystem from one storage class to another. These policies can be applied to one or more filesystems. Supported storage '
  name: Pure Storage Policies - Storage Class Tiering API
  slug: pure-storage-policies-storage-class-tiering-api
- description: A TLS policy manages the allowed TLS versions and ciphers for incoming network traffic to the system. These policies can be applied at the array level, or to individual network IPs.
  name: Pure Storage Policies - TLS API
  slug: pure-storage-policies-tls-api
- description: A user-group-quota policy manages NFS and SMB quota configuration applicable for file owners in a filesystems. Rules can be set to configure quotas for specific users or groups, user-default and group
  name: Pure Storage Policies - User and Group Quota Policy API
  slug: pure-storage-policies-user-and-group-quota-policy-api
- description: Manages WORM data for file systems. These policies are composed of retention periods, lock type, and auto-commit status.
  name: Pure Storage Policies - WORM Data API
  slug: pure-storage-policies-worm-data-api
- description: The ports on a FlashArray are assigned iSCSI Qualified Names (IQNs), NVMe Qualified Names (NQNs), and Fibre Channel World Wide Names (WWNs).
  name: Pure Storage Ports API
  slug: pure-storage-ports-api
- description: Presets are reusable templates that provision resources.
  name: Pure Storage Presets API
  slug: pure-storage-presets-api
- description: Protection group snapshots capture the content of all volumes on the source array for the specified protection group at a single point in time.
  name: Pure Storage Protection Group Snapshots API
  slug: pure-storage-protection-group-snapshots-api
- description: 'A protection group defines a set of volumes, hosts, or host groups (called members) that are protected together through snapshots with point-in-time consistency across the member volumes. The members '
  name: Pure Storage Protection Groups API
  slug: pure-storage-protection-groups-api
- description: Public Keys can be configured for reference in other configurations as signing keys are used to verify cryptographic signatures.
  name: Pure Storage Public Keys API
  slug: pure-storage-public-keys-api
- description: A quota manages a set amount of space on a file system which a user or group may write to. A quota can be applied to a user or group of a specified file system. Once a user or group reaches their quot
  name: Pure Storage Quotas API
  slug: pure-storage-quotas-api
- description: Displays Rapid Data Locking (RDL) configuration and performs functionality tests of the associated Enterprise Key Management (EKM) servers.
  name: Pure Storage RDL API
  slug: pure-storage-rdl-api
- description: Realm connections enable replication services between different realms in a connected array cluster.
  name: Pure Storage Realm Connections API
  slug: pure-storage-realm-connections-api
- description: A realm is an administrative domain, a data container, and a namespace for pods, hosts, and host groups.
  name: Pure Storage Realms API
  slug: pure-storage-realms-api
- description: Remote arrays provide the ability to list and manage all the remote arrays known to an array.
  name: Pure Storage Remote Arrays API
  slug: pure-storage-remote-arrays-api
- description: A remote pod represents a pod that is on a connected array but not stretched to this array.
  name: Pure Storage Remote Pods API
  slug: pure-storage-remote-pods-api
- description: A remote protection group snapshot represents a protection group snapshot that resides on an offload target with the source side of the remote protection group snapshot being another array that is con
  name: Pure Storage Remote Protection Group Snapshots API
  slug: pure-storage-remote-protection-group-snapshots-api
- description: 'A remote protection group represents a protection group that resides on an offload target with the source side of the remote protection group being another array that is connected to the local array. '
  name: Pure Storage Remote Protection Groups API
  slug: pure-storage-remote-protection-groups-api
- description: A remote realm represents a realm that is on a connected array but not stretched to this array.
  name: Pure Storage Remote Realms API
  slug: pure-storage-remote-realms-api
- description: A remote volume snapshot represents a volume snapshot that resides on an offload target with the source side of the remote volume snapshot being another array that is connected to the local array. The
  name: Pure Storage Remote Volume Snapshots API
  slug: pure-storage-remote-volume-snapshots-api
- description: Resiliency groups display pairs of nodes where HA is enabled.
  name: Pure Storage Resiliency Groups API
  slug: pure-storage-resiliency-groups-api
- description: The Resource Accesses API from Pure Storage — 5 operation(s) for resource accesses.
  name: Pure Storage Resource Accesses API
  slug: pure-storage-resource-accesses-api
- description: Displays role attributes. Each user of the array is assigned to a role and each role has a set of role based access controls (RBAC). The roles (`array_admin`, `storage_admin`, `ops_admin`, `readonly`,
  name: Pure Storage Roles API
  slug: pure-storage-roles-api
- description: SAML2 SSO allows customers to configure settings of SAML2 service provider and identity provider. It provides a multi-factor authentication (MFA) mechanism for customers to log in to FlashArray.
  name: Pure Storage SAML2 SSO API
  slug: pure-storage-saml2-sso-api
- description: The Servers API from Pure Storage — 2 operation(s) for servers.
  name: Pure Storage Servers API
  slug: pure-storage-servers-api
- description: Manages Purity//FA login and user session data.
  name: Pure Storage Sessions API
  slug: pure-storage-sessions-api
- description: Manages the Pure Storage Storage Management Initiative Specification (SMI-S).
  name: Pure Storage SMI-S API
  slug: pure-storage-smi-s-api
- description: Manages Simple Mail Transfer Protocol (SMTP) settings. SMTP allows the array to send email notifications and alerts to recipients.
  name: Pure Storage SMTP API
  slug: pure-storage-smtp-api
- description: Manages connections to Simple Network Management Protocol (SNMP) agents.
  name: Pure Storage SNMP Agents API
  slug: pure-storage-snmp-agents-api
- description: Manages connections to Simple Network Management Protocol (SNMP) managers.
  name: Pure Storage SNMP Managers API
  slug: pure-storage-snmp-managers-api
- description: Software to be installed on the array.
  name: Pure Storage Software API
  slug: pure-storage-software-api
- description: Manages the subnets and VLANs used to organize the network interfaces.
  name: Pure Storage Subnets API
  slug: pure-storage-subnets-api
- description: Provides information about subscription assets.
  name: Pure Storage Subscription Assets API
  slug: pure-storage-subscription-assets-api
- description: Provides information about subscription offerings.
  name: Pure Storage Subscriptions API
  slug: pure-storage-subscriptions-api
- description: Enables Support to fix bugs and help customers solve problems. Support tools include proxy, phonehome, and remote assist.
  name: Pure Storage Support API
  slug: pure-storage-support-api
- description: Manages support diagnostics for the array, including performing diagnostics tasks, running tests, finding problems and giving remediation. The diagnostics tool provides a way to test the array compone
  name: Pure Storage Support Diagnostics API
  slug: pure-storage-support-diagnostics-api
- description: Provides information about energy consumption and sustainability.
  name: Pure Storage Sustainability API
  slug: pure-storage-sustainability-api
- description: Copied to Log Targets/Syslog for more organized way to handle all log targets. Both endpoints are identical. We encourage our users to use Log Targets/Syslog.
  name: Pure Storage Syslog API
  slug: pure-storage-syslog-api
- description: Manages targets for replication, including viewing the performance metrics of active replication operations.
  name: Pure Storage Targets API
  slug: pure-storage-targets-api
- description: Topology groups provide a way to manage sets of arrays. Groups are composed of individual arrays or other topology groups. By nesting groups, customers can express group and array hierarchies. A group
  name: Pure Storage Topology Groups API
  slug: pure-storage-topology-groups-api
- description: Displays the data usage and hard limit quotas for all users and groups on a file system.
  name: Pure Storage Usage API
  slug: pure-storage-usage-api
- description: User Group quotas provide the ability to set capacity limits for users and groups in managed directories.
  name: Pure Storage User Group Quotas API
  slug: pure-storage-user-group-quotas-api
- description: A vchost connection is between a protocol endpoint and vchost. In the context of vchost-connection, the vchost represents a vCenter, and the protocol endpoint is used to represent a storage container.
  name: Pure Storage Vchost Connections API
  slug: pure-storage-vchost-connections-api
- description: The Vchosts API from Pure Storage — 3 operation(s) for vchosts.
  name: Pure Storage Vchosts API
  slug: pure-storage-vchosts-api
- description: Verification keys used by Pure Support to access the array.
  name: Pure Storage Verification Keys API
  slug: pure-storage-verification-keys-api
- description: The Virtual Machines API from Pure Storage — 3 operation(s) for virtual machines.
  name: Pure Storage Virtual Machines API
  slug: pure-storage-virtual-machines-api
- description: 'Volume groups organize volumes into logical groupings. If virtual volumes are configured, each volume group on the FlashArray array represents its associated virtual machine, and inside each of those '
  name: Pure Storage Volume Groups API
  slug: pure-storage-volume-groups-api
- description: Volume snapshots are immutable, point-in-time images of the contents of one or more volumes. There are two types of volume snapshots&#58; volume snapshots and protection group volume snapshots. A volu
  name: Pure Storage Volume Snapshots API
  slug: pure-storage-volume-snapshots-api
- description: 'A volume represents a container that manages the storage space on the array. After a volume has been created, host-volume connections must be established so that the host can read data from and write '
  name: Pure Storage Volumes API
  slug: pure-storage-volumes-api
- description: Workloads organize storage resources (such as volumes) and their related configuration and policy objects into logical groupings. Workloads can be deployed from workload presets.
  name: Pure Storage Workloads API
  slug: pure-storage-workloads-api
artifact_total: 279
collections:
- collection_type: open
  name: FlashArray REST API
  slug: open-flasharray-rest-api
- collection_type: open
  name: FlashBlade REST API
  slug: open-flashblade-rest-api
- collection_type: open
  name: Pure1 Public REST API
  slug: open-pure1-cloud-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pure-storage-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pure-storage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pure-storage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pure-storage-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/purestorage
- group: company
  title: ''
  type: Website
  url: https://www.purestorage.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://code.purestorage.com
- group: docs
  title: ''
  type: Documentation
  url: https://code.purestorage.com
- group: docs
  title: ''
  type: APIReference
  url: https://code.purestorage.com/swagger
- group: build
  title: py-pure-client (Unified Python SDK)
  type: SDKs
  url: https://github.com/PureStorage-OpenConnect/py-pure-client
- group: build
  title: Swagger UI for FA / FB / Pure1
  type: Tools
  url: https://github.com/PureStorage-OpenConnect/swagger
- group: build
  title: FlashBlade MCP Server
  type: Tools
  url: https://github.com/PureStorage-OpenConnect/flashblade-mcp-server
- group: build
  title: px-deploy
  type: CLI
  url: https://github.com/PureStorage-OpenConnect/px-deploy
- group: operate
  title: ''
  type: Support
  url: https://support.purestorage.com
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://supportcenter.purestorage.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PureStorage-OpenConnect
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/purestorage
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/portworx
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/libopenstorage
- group: company
  title: ''
  type: Blog
  url: https://blog.purestorage.com/feed/
- group: design
  title: Pure Storage Spectral Ruleset
  type: SpectralRules
  url: rules/pure-storage-rules.yml
- group: design
  title: Pure Storage Vocabulary
  type: Vocabulary
  url: vocabulary/pure-storage-vocabulary.yml
crds:
- name: pure storage portworx portworxdiag
  url: https://raw.githubusercontent.com/api-evangelist/pure-storage/refs/heads/main/crd/pure-storage-portworx-portworxdiag.yaml
- name: pure storage portworx storagecluster
  url: https://raw.githubusercontent.com/api-evangelist/pure-storage/refs/heads/main/crd/pure-storage-portworx-storagecluster.yaml
- name: pure storage portworx storagenode
  url: https://raw.githubusercontent.com/api-evangelist/pure-storage/refs/heads/main/crd/pure-storage-portworx-storagenode.yaml
- name: pure storage portworx xcopyvolumepopulator
  url: https://raw.githubusercontent.com/api-evangelist/pure-storage/refs/heads/main/crd/pure-storage-portworx-xcopyvolumepopulator.yaml
created: '2026-05-04'
description: Pure Storage is an American publicly traded technology company specializing in all-flash data storage hardware and software products. The company provides enterprise data storage platforms including FlashArray, FlashBlade, and Pure1 fleet management, along with Portworx for Kubernetes data services. Pure Storage offers REST APIs, SDKs, CRDs, and developer tooling that enable programmatic management of storage infrastructure and integration with automation workflows across block, file, and object storage.
examples:
- key_count: 22
  name: Flasharray Rest Api Alert Example
  slug: flasharray-rest-api-alert-example
- key_count: 9
  name: Flasharray Rest Api Api Client Example
  slug: flasharray-rest-api-api-client-example
- key_count: 12
  name: Flasharray Rest Api Directory Example
  slug: flasharray-rest-api-directory-example
- key_count: 18
  name: Flasharray Rest Api Host Example
  slug: flasharray-rest-api-host-example
- key_count: 9
  name: Flasharray Rest Api Host Group Example
  slug: flasharray-rest-api-host-group-example
- key_count: 10
  name: Flasharray Rest Api Network Interface Example
  slug: flasharray-rest-api-network-interface-example
- key_count: 20
  name: Flasharray Rest Api Pod Example
  slug: flasharray-rest-api-pod-example
- key_count: 4
  name: Flasharray Rest Api Policy Example
  slug: flasharray-rest-api-policy-example
- key_count: 20
  name: Flasharray Rest Api Protection Group Example
  slug: flasharray-rest-api-protection-group-example
- key_count: 10
  name: Flasharray Rest Api Volume Example
  slug: flasharray-rest-api-volume-example
- key_count: 13
  name: Flasharray Rest Api Volume Snapshot Example
  slug: flasharray-rest-api-volume-snapshot-example
- key_count: 18
  name: Flashblade Rest Api Alert Example
  slug: flashblade-rest-api-alert-example
- key_count: 9
  name: Flashblade Rest Api Api Client Example
  slug: flashblade-rest-api-api-client-example
- key_count: 18
  name: Flashblade Rest Api Array Example
  slug: flashblade-rest-api-array-example
- key_count: 21
  name: Flashblade Rest Api Bucket Example
  slug: flashblade-rest-api-bucket-example
- key_count: 28
  name: Flashblade Rest Api File System Example
  slug: flashblade-rest-api-file-system-example
- key_count: 12
  name: Flashblade Rest Api File System Snapshot Example
  slug: flashblade-rest-api-file-system-snapshot-example
- key_count: 13
  name: Flashblade Rest Api Network Interface Example
  slug: flashblade-rest-api-network-interface-example
- key_count: 11
  name: Flashblade Rest Api Object Store Account Example
  slug: flashblade-rest-api-object-store-account-example
- key_count: 6
  name: Flashblade Rest Api Object Store User Example
  slug: flashblade-rest-api-object-store-user-example
- key_count: 6
  name: Flashblade Rest Api Object Store Virtual Host Example
  slug: flashblade-rest-api-object-store-virtual-host-example
- key_count: 4
  name: Flashblade Rest Api Policy Example
  slug: flashblade-rest-api-policy-example
- key_count: 16
  name: Pure1 Cloud Api Alert Example
  slug: pure1-cloud-api-alert-example
- key_count: 4
  name: Pure1 Cloud Api Array Example
  slug: pure1-cloud-api-array-example
- key_count: 6
  name: Pure1 Cloud Api Audit Example
  slug: pure1-cloud-api-audit-example
- key_count: 4
  name: Pure1 Cloud Api Blade Example
  slug: pure1-cloud-api-blade-example
- key_count: 5
  name: Pure1 Cloud Api Bucket Example
  slug: pure1-cloud-api-bucket-example
- key_count: 9
  name: Pure1 Cloud Api File System Example
  slug: pure1-cloud-api-file-system-example
- key_count: 5
  name: Pure1 Cloud Api File System Snapshot Example
  slug: pure1-cloud-api-file-system-snapshot-example
- key_count: 4
  name: Pure1 Cloud Api Metric Example
  slug: pure1-cloud-api-metric-example
- key_count: 4
  name: Pure1 Cloud Api Protection Group Snapshot Example
  slug: pure1-cloud-api-protection-group-snapshot-example
- key_count: 10
  name: Pure1 Cloud Api Subscription Example
  slug: pure1-cloud-api-subscription-example
- key_count: 14
  name: Pure1 Cloud Api Subscription License Example
  slug: pure1-cloud-api-subscription-license-example
- key_count: 3
  name: Pure1 Cloud Api Support Contract Example
  slug: pure1-cloud-api-support-contract-example
- key_count: 5
  name: Pure1 Cloud Api Tag Example
  slug: pure1-cloud-api-tag-example
features:
- description: Enterprise all-flash storage hardware (FlashArray, FlashBlade) with consistent low-latency performance.
  name: All-Flash Storage
- description: FlashBlade provides scale-out file and S3-compatible object storage from a single platform.
  name: Unified File and Object Storage
- description: Pure1 SaaS provides telemetry, analytics, alerting, and capacity planning across the entire Pure fleet.
  name: Cross-Array Fleet Management
- description: Portworx delivers persistent storage, data protection, DR, and migration for Kubernetes workloads.
  name: Kubernetes Data Services
- description: Synchronous replication for zero-RPO active-active configurations across data centers.
  name: Active Cluster Replication
- description: Space-efficient snapshots and instant clones for backup, dev/test, and database refresh.
  name: Snapshot and Cloning
- description: Pure1 sustainability metrics expose energy, carbon, and efficiency data per array.
  name: Sustainability Reporting
- description: All Pure Storage REST APIs authenticate via the OAuth 2.0 token-exchange flow with JWT subject tokens.
  name: OAuth 2.0 Token Exchange
finops:
- name: Pure Storage Finops
  service_category: API
  slug: pure-storage-finops
image: https://avatars.githubusercontent.com/u/8324560
integrations:
- description: First-class integration with vSphere via vCenter plugins, vVols, and SRM workflows.
  name: VMware vSphere
- description: Official Ansible collections for FlashArray, FlashBlade, and Pure1 published on Ansible Galaxy.
  name: Ansible
- description: Terraform providers for FlashArray and Cloud Block Store.
  name: Terraform
- description: CSI drivers, the libopenstorage operator, Portworx, Stork, and the Pure Service Orchestrator (PSO).
  name: Kubernetes
- description: Cinder and Manila drivers for FlashArray and FlashBlade.
  name: OpenStack
- description: Splunk apps and TAs ingest Pure Storage telemetry for security and operations dashboards.
  name: Splunk
- description: OpenMetrics exporters for FlashArray and FlashBlade feed Prometheus-based observability stacks.
  name: Prometheus / Grafana
- description: Support and incident integrations through Pure1 alerts and webhooks.
  name: ServiceNow / Jira
json_schemas:
- name: Alert
  property_count: 0
  slug: flasharray-rest-api-alert
- name: ApiClient
  property_count: 9
  slug: flasharray-rest-api-api-client
- name: Directory
  property_count: 0
  slug: flasharray-rest-api-directory
- name: HostGroup
  property_count: 0
  slug: flasharray-rest-api-host-group
- name: Host
  property_count: 0
  slug: flasharray-rest-api-host
- name: NetworkInterface
  property_count: 0
  slug: flasharray-rest-api-network-interface
- name: Pod
  property_count: 0
  slug: flasharray-rest-api-pod
- name: Policy
  property_count: 0
  slug: flasharray-rest-api-policy
- name: ProtectionGroup
  property_count: 0
  slug: flasharray-rest-api-protection-group
- name: Volume
  property_count: 0
  slug: flasharray-rest-api-volume
- name: VolumeSnapshot
  property_count: 0
  slug: flasharray-rest-api-volume-snapshot
- name: Alert
  property_count: 0
  slug: flashblade-rest-api-alert
- name: ApiClient
  property_count: 0
  slug: flashblade-rest-api-api-client
- name: Array
  property_count: 0
  slug: flashblade-rest-api-array
- name: Bucket
  property_count: 0
  slug: flashblade-rest-api-bucket
- name: FileSystem
  property_count: 0
  slug: flashblade-rest-api-file-system
- name: FileSystemSnapshot
  property_count: 0
  slug: flashblade-rest-api-file-system-snapshot
- name: NetworkInterface
  property_count: 0
  slug: flashblade-rest-api-network-interface
- name: ObjectStoreAccount
  property_count: 0
  slug: flashblade-rest-api-object-store-account
- name: ObjectStoreUser
  property_count: 0
  slug: flashblade-rest-api-object-store-user
- name: ObjectStoreVirtualHost
  property_count: 0
  slug: flashblade-rest-api-object-store-virtual-host
- name: Policy
  property_count: 0
  slug: flashblade-rest-api-policy
- name: Alert
  property_count: 0
  slug: pure1-cloud-api-alert
- name: Array
  property_count: 0
  slug: pure1-cloud-api-array
- name: Audit
  property_count: 0
  slug: pure1-cloud-api-audit
- name: Blade
  property_count: 0
  slug: pure1-cloud-api-blade
- name: Bucket
  property_count: 0
  slug: pure1-cloud-api-bucket
- name: FileSystem
  property_count: 0
  slug: pure1-cloud-api-file-system
- name: FileSystemSnapshot
  property_count: 0
  slug: pure1-cloud-api-file-system-snapshot
- name: Metric
  property_count: 0
  slug: pure1-cloud-api-metric
- name: ProtectionGroupSnapshot
  property_count: 0
  slug: pure1-cloud-api-protection-group-snapshot
- name: SubscriptionLicense
  property_count: 0
  slug: pure1-cloud-api-subscription-license
- name: Subscription
  property_count: 0
  slug: pure1-cloud-api-subscription
- name: SupportContract
  property_count: 3
  slug: pure1-cloud-api-support-contract
- name: Tag
  property_count: 5
  slug: pure1-cloud-api-tag
json_structures:
- name: Flasharray Rest Api Alert Structure
  property_count: 0
  slug: flasharray-rest-api-alert-structure
- name: Flasharray Rest Api Api Client Structure
  property_count: 9
  slug: flasharray-rest-api-api-client-structure
- name: Flasharray Rest Api Directory Structure
  property_count: 0
  slug: flasharray-rest-api-directory-structure
- name: Flasharray Rest Api Host Group Structure
  property_count: 0
  slug: flasharray-rest-api-host-group-structure
- name: Flasharray Rest Api Host Structure
  property_count: 0
  slug: flasharray-rest-api-host-structure
- name: Flasharray Rest Api Network Interface Structure
  property_count: 0
  slug: flasharray-rest-api-network-interface-structure
- name: Flasharray Rest Api Pod Structure
  property_count: 0
  slug: flasharray-rest-api-pod-structure
- name: Flasharray Rest Api Policy Structure
  property_count: 0
  slug: flasharray-rest-api-policy-structure
- name: Flasharray Rest Api Protection Group Structure
  property_count: 0
  slug: flasharray-rest-api-protection-group-structure
- name: Flasharray Rest Api Volume Snapshot Structure
  property_count: 0
  slug: flasharray-rest-api-volume-snapshot-structure
- name: Flasharray Rest Api Volume Structure
  property_count: 0
  slug: flasharray-rest-api-volume-structure
- name: Flashblade Rest Api Alert Structure
  property_count: 0
  slug: flashblade-rest-api-alert-structure
- name: Flashblade Rest Api Api Client Structure
  property_count: 0
  slug: flashblade-rest-api-api-client-structure
- name: Flashblade Rest Api Array Structure
  property_count: 0
  slug: flashblade-rest-api-array-structure
- name: Flashblade Rest Api Bucket Structure
  property_count: 0
  slug: flashblade-rest-api-bucket-structure
- name: Flashblade Rest Api File System Snapshot Structure
  property_count: 0
  slug: flashblade-rest-api-file-system-snapshot-structure
- name: Flashblade Rest Api File System Structure
  property_count: 0
  slug: flashblade-rest-api-file-system-structure
- name: Flashblade Rest Api Network Interface Structure
  property_count: 0
  slug: flashblade-rest-api-network-interface-structure
- name: Flashblade Rest Api Object Store Account Structure
  property_count: 0
  slug: flashblade-rest-api-object-store-account-structure
- name: Flashblade Rest Api Object Store User Structure
  property_count: 0
  slug: flashblade-rest-api-object-store-user-structure
- name: Flashblade Rest Api Object Store Virtual Host Structure
  property_count: 0
  slug: flashblade-rest-api-object-store-virtual-host-structure
- name: Flashblade Rest Api Policy Structure
  property_count: 0
  slug: flashblade-rest-api-policy-structure
- name: Pure1 Cloud Api Alert Structure
  property_count: 0
  slug: pure1-cloud-api-alert-structure
- name: Pure1 Cloud Api Array Structure
  property_count: 0
  slug: pure1-cloud-api-array-structure
- name: Pure1 Cloud Api Audit Structure
  property_count: 0
  slug: pure1-cloud-api-audit-structure
- name: Pure1 Cloud Api Blade Structure
  property_count: 0
  slug: pure1-cloud-api-blade-structure
- name: Pure1 Cloud Api Bucket Structure
  property_count: 0
  slug: pure1-cloud-api-bucket-structure
- name: Pure1 Cloud Api File System Snapshot Structure
  property_count: 0
  slug: pure1-cloud-api-file-system-snapshot-structure
- name: Pure1 Cloud Api File System Structure
  property_count: 0
  slug: pure1-cloud-api-file-system-structure
- name: Pure1 Cloud Api Metric Structure
  property_count: 0
  slug: pure1-cloud-api-metric-structure
- name: Pure1 Cloud Api Protection Group Snapshot Structure
  property_count: 0
  slug: pure1-cloud-api-protection-group-snapshot-structure
- name: Pure1 Cloud Api Subscription License Structure
  property_count: 0
  slug: pure1-cloud-api-subscription-license-structure
- name: Pure1 Cloud Api Subscription Structure
  property_count: 0
  slug: pure1-cloud-api-subscription-structure
- name: Pure1 Cloud Api Support Contract Structure
  property_count: 3
  slug: pure1-cloud-api-support-contract-structure
- name: Pure1 Cloud Api Tag Structure
  property_count: 5
  slug: pure1-cloud-api-tag-structure
jsonld:
- class_count: 11
  name: Pure Storage Flasharray Rest Api Context
  property_count: 108
  slug: pure-storage-flasharray-rest-api-context
- class_count: 11
  name: Pure Storage Flashblade Rest Api Context
  property_count: 102
  slug: pure-storage-flashblade-rest-api-context
- class_count: 13
  name: Pure Storage Pure1 Cloud Api Context
  property_count: 78
  slug: pure-storage-pure1-cloud-api-context
layout: provider
modified: '2026-05-19'
name: Pure Storage
nav: Providers
network: true
overview: 'Pure Storage publishes 129 APIs on the [APIs.io](https://apis.io/) network, including Active Directory API, Administrators API, Alert Watchers API, and 126 more. Tagged areas include Storage, Data Storage, Flash Storage, Enterprise Storage, and Cloud Storage.


  The Pure Storage catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  Pure Storage''s developer surface includes authentication, documentation, API reference, tooling, CLI, support, engineering blog, and 15 more developer resources.'
plans:
- name: Pure Storage Plans Pricing
  plan_count: 1
  slug: pure-storage-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 2
  name: Pure Storage Rate Limits
  slug: pure-storage-rate-limits
rules:
- name: Pure Storage API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pure-storage-jsonschema-spectral-rules
- name: Pure Storage API Rules
  rule_count: 26
  severity_counts:
    error: 8
    hint: 0
    info: 4
    warn: 14
  slug: pure-storage-rules
score:
  band: developing
  composite: 48.7
  delta: -5.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 57.7
    developer_ergonomics: 54.3
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 129
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/pure-storage/refs/heads/main/screenshots/pure-storage-2026-06-20T192313.png
security:
- kind: authentication
  name: Pure Storage Authentication
  slug: pure-storage-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Pure Storage Domain Security
  slug: pure-storage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pure Storage Vulnerability Disclosure
  slug: pure-storage-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pure-storage
solutions:
- description: All-flash block storage arrays for tier-1 enterprise workloads.
  name: FlashArray
- description: Unified fast file and object storage for unstructured data and modern analytics.
  name: FlashBlade
- description: SaaS-based AI-driven fleet management, analytics, and support platform.
  name: Pure1
- description: Kubernetes data services platform offering storage, DR, security, and migration.
  name: Portworx
- description: FlashArray-as-a-service running natively on AWS and Azure.
  name: Cloud Block Store
- description: Subscription model for non-disruptive controller and capacity upgrades.
  name: Evergreen Storage
tags:
- Storage
- Data Storage
- Flash Storage
- Enterprise Storage
- Cloud Storage
- Object Storage
- File Storage
- Block Storage
- Kubernetes Storage
- Infrastructure
use_cases:
- description: High-performance storage for SQL Server, Oracle, SAP HANA, PostgreSQL, and other database workloads.
  name: Database Storage
- description: Storage backend for VMware vSphere, Hyper-V, KVM, and Nutanix virtualization platforms.
  name: VMware and Virtualization
- description: FlashBlade powers training datasets, vector search, embedding pipelines, and RAG architectures.
  name: AI and Machine Learning Pipelines
- description: Snapshot-based backup, replication, and SafeMode immutable snapshots for ransomware recovery.
  name: Backup and Disaster Recovery
- description: Cloud Block Store extends Pure Storage to AWS, Azure, and other public clouds.
  name: Cloud Block Storage
- description: Portworx provides dynamic provisioning, snapshots, and DR for Kubernetes stateful workloads.
  name: Container and Kubernetes Storage
- description: Pure1 telemetry feeds capacity forecasting, performance analysis, and lifecycle management.
  name: Fleet Capacity Planning
website: https://www.purestorage.com
---
