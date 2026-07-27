---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
api_count: 124
apis:
- description: AccessPathController Operations able access paths
  name: XSKY access-paths API
  slug: xsky-access-paths-api
- description: AccessTokenController Manage users
  name: XSKY access-tokens API
  slug: xsky-access-tokens-api
- description: ActionLogController Operations about ActionLog
  name: XSKY action-logs API
  slug: xsky-action-logs-api
- description: AlertGroupController Operations about alert group
  name: XSKY alert-groups API
  slug: xsky-alert-groups-api
- description: AlertRuleController Operations about alert rule
  name: XSKY alert-rules API
  slug: xsky-alert-rules-api
- description: AlertController Operations about alert
  name: XSKY alerts API
  slug: xsky-alerts-api
- description: AuthController Manage authentication and authorization
  name: XSKY auth API
  slug: xsky-auth-api
- description: BlockSnapshotController Operations about Block Snapshot
  name: XSKY block-snapshots API
  slug: xsky-block-snapshots-api
- description: VolumeGroupSnapshotController Operations about volume group snapshot
  name: XSKY block-volume-group-snapshots API
  slug: xsky-block-volume-group-snapshots-api
- description: VolumeGroupController Operations about volume group
  name: XSKY block-volume-groups API
  slug: xsky-block-volume-groups-api
- description: BlockVolumeMigrationJobController Operations about block volume migration job
  name: XSKY block-volume-migration-jobs API
  slug: xsky-block-volume-migration-jobs-api
- description: BlockVolumeController Operations about Block
  name: XSKY block-volumes API
  slug: xsky-block-volumes-api
- description: ChunkController Chunk Management
  name: XSKY chunks API
  slug: xsky-chunks-api
- description: ClientCodeController Operations about client code
  name: XSKY client-codes API
  slug: xsky-client-codes-api
- description: ClientGroupController Operations about client group
  name: XSKY client-groups API
  slug: xsky-client-groups-api
- description: ClientLunMappingController API /client-lun-mappings
  name: XSKY client-lun-mappings API
  slug: xsky-client-lun-mappings-api
- description: ClientController API /clients
  name: XSKY clients API
  slug: xsky-clients-api
- description: CloudInstanceController Cloud Instance Management
  name: XSKY cloud-instances API
  slug: xsky-cloud-instances-api
- description: CloudPlatformController Cloud Platform Management
  name: XSKY cloud-platforms API
  slug: xsky-cloud-platforms-api
- description: CloudVolumeAttachmentController Cloud Volume Attachment Management
  name: XSKY cloud-volume-attachments API
  slug: xsky-cloud-volume-attachments-api
- description: CloudVolumeController Cloud Volume Management
  name: XSKY cloud-volumes API
  slug: xsky-cloud-volumes-api
- description: ClusterController API /cluster
  name: XSKY cluster API
  slug: xsky-cluster-api
- description: ConfController Operations about Config
  name: XSKY confs API
  slug: xsky-confs-api
- description: CryptoKeyController API /crypto-keys/
  name: XSKY crypto-keys API
  slug: xsky-crypto-keys-api
- description: DiskController Disk Management
  name: XSKY disks API
  slug: xsky-disks-api
- description: DomainUserValidatorController Domain User Validator Management
  name: XSKY domain-user-validators API
  slug: xsky-domain-user-validators-api
- description: DpBlockBackupJobController API /dp-block-backup-jobs/
  name: XSKY dp-block-backup-jobs API
  slug: xsky-dp-block-backup-jobs-api
- description: DpBlockBackupPolicyController API /dp-block-backup-policies
  name: XSKY dp-block-backup-policies API
  slug: xsky-dp-block-backup-policies-api
- description: DpBlockReplicationPolicyController API /dp-block-replication-policies
  name: XSKY dp-block-replication-policies API
  slug: xsky-dp-block-replication-policies-api
- description: DpBlockSnapshotJobController API /dp-block-snapshot-jobs/
  name: XSKY dp-block-snapshot-jobs API
  slug: xsky-dp-block-snapshot-jobs-api
- description: DpBlockSnapshotPolicyController API /dp-block-snapshot-policies
  name: XSKY dp-block-snapshot-policies API
  slug: xsky-dp-block-snapshot-policies-api
- description: DpBlockSnapshotRecoveryJobController API /dp-block-snapshot-recovery-jobs
  name: XSKY dp-block-snapshot-recovery-jobs API
  slug: xsky-dp-block-snapshot-recovery-jobs-api
- description: DpFSSnapshotJobController API /dp-fs-snapshot-jobs/
  name: XSKY dp-fs-snapshot-jobs API
  slug: xsky-dp-fs-snapshot-jobs-api
- description: DpFSSnapshotPolicyController API /dp-fs-snapshot-policies
  name: XSKY dp-fs-snapshot-policies API
  slug: xsky-dp-fs-snapshot-policies-api
- description: DpGatewayController API /dp-gateways/
  name: XSKY dp-gateways API
  slug: xsky-dp-gateways-api
- description: DpSiteController API /dp-sites/
  name: XSKY dp-sites API
  slug: xsky-dp-sites-api
- description: EmailGroupController Operations about Email
  name: XSKY email-groups API
  slug: xsky-email-groups-api
- description: EmailController Operations about Email
  name: XSKY emails API
  slug: xsky-emails-api
- description: EventLogController Operations about EventLog
  name: XSKY event-logs API
  slug: xsky-event-logs-api
- description: FSActiveDirectoryController File Storage Active Directory Management
  name: XSKY fs-active-directories API
  slug: xsky-fs-active-directories-api
- description: FSArbitrationPoolController File Storage Arbitration Pool Management
  name: XSKY fs-arbitration-pools API
  slug: xsky-fs-arbitration-pools-api
- description: FSClientGroupController provides APIs for file storage client group
  name: XSKY fs-client-groups API
  slug: xsky-fs-client-groups-api
- description: FSClientController provides APIs for file storage client
  name: XSKY fs-clients API
  slug: xsky-fs-clients-api
- description: FSFolderController provides API for file storage folder
  name: XSKY fs-folders API
  slug: xsky-fs-folders-api
- description: FSFTPSessionController provides API for fs FTP session
  name: XSKY fs-ftp-sessions API
  slug: xsky-fs-ftp-sessions-api
- description: FSFTPShareACLController provides API for fs ftp share acl
  name: XSKY fs-ftp-share-acls API
  slug: xsky-fs-ftp-share-acls-api
- description: FSFTPShareController provides API for fs ftp share
  name: XSKY fs-ftp-shares API
  slug: xsky-fs-ftp-shares-api
- description: FSGatewayGroupController provides APIs for file storage gateway group
  name: XSKY fs-gateway-groups API
  slug: xsky-fs-gateway-groups-api
- description: FSGatewayController provides APIs for file storage gateway
  name: XSKY fs-gateways API
  slug: xsky-fs-gateways-api
- description: FSLdapController File Storage LDAP Management
  name: XSKY fs-ldaps API
  slug: xsky-fs-ldaps-api
- description: FSNFSConnectionController provides API for fs NFS connection
  name: XSKY fs-nfs-connections API
  slug: xsky-fs-nfs-connections-api
- description: FSNFSShareACLController provides API for fs nfs shares acl
  name: XSKY fs-nfs-share-acls API
  slug: xsky-fs-nfs-share-acls-api
- description: FSNFSShareController provides API for fs nfs shares
  name: XSKY fs-nfs-shares API
  slug: xsky-fs-nfs-shares-api
- description: FSQuotaTreeController provides API for file storage quota tree
  name: XSKY fs-quota-trees API
  slug: xsky-fs-quota-trees-api
- description: FSSMBSessionController provides API for fs SMB session
  name: XSKY fs-smb-sessions API
  slug: xsky-fs-smb-sessions-api
- description: FSSMBShareACLController provides API for fs smb share acl
  name: XSKY fs-smb-share-acls API
  slug: xsky-fs-smb-share-acls-api
- description: FSSMBShareController provides API for fs smb share
  name: XSKY fs-smb-shares API
  slug: xsky-fs-smb-shares-api
- description: FSSnapshotController provides APIs for file storage snapshot
  name: XSKY fs-snapshots API
  slug: xsky-fs-snapshots-api
- description: FSUserGroupController provides APIs for file storage user group
  name: XSKY fs-user-groups API
  slug: xsky-fs-user-groups-api
- description: FSUserController provides API for file storage user
  name: XSKY fs-users API
  slug: xsky-fs-users-api
- description: HostEncSpecController API /host-enc-specs/
  name: XSKY host-enc-specs API
  slug: xsky-host-enc-specs-api
- description: HostInfoController Host Info Management
  name: XSKY host-info API
  slug: xsky-host-info-api
- description: HostInitializationController provides API for host initialization
  name: XSKY host-initializations API
  slug: xsky-host-initializations-api
- description: HostValidatorController Host Validator Management
  name: XSKY host-validators API
  slug: xsky-host-validators-api
- description: HostController Host Management
  name: XSKY hosts API
  slug: xsky-hosts-api
- description: IdentityPlatformController Identity Platform Management
  name: XSKY identity-platforms API
  slug: xsky-identity-platforms-api
- description: LicenseController Operations about Install
  name: XSKY licenses API
  slug: xsky-licenses-api
- description: LunController Operations on luns
  name: XSKY luns API
  slug: xsky-luns-api
- description: MappingGroupController Operations able mapping groups
  name: XSKY mapping-groups API
  slug: xsky-mapping-groups-api
- description: NetworkAddressController Network Address Management
  name: XSKY network-addresses API
  slug: xsky-network-addresses-api
- description: NetworkDiagnosisController provides API for network diagnosis
  name: XSKY network-diagnoses API
  slug: xsky-network-diagnoses-api
- description: NetworkDiagnosisItemController provides API for network diagnosis item
  name: XSKY network-diagnosis-items API
  slug: xsky-network-diagnosis-items-api
- description: NetworkInterfaceController Network Interface Management
  name: XSKY network-interfaces API
  slug: xsky-network-interfaces-api
- description: NFSGatewayBucketMapController provides API for object storage nfs gateway s3 bucket map
  name: XSKY nfs-gateway-bucket-maps API
  slug: xsky-nfs-gateway-bucket-maps-api
- description: NFSGatewayController provides API for object storage nfs gateway
  name: XSKY nfs-gateways API
  slug: xsky-nfs-gateways-api
- description: OSBucketLoggingController API /os-bucket-loggings.
  name: XSKY os-bucket-loggings API
  slug: xsky-os-bucket-loggings-api
- description: ObjectStorageBucketController provides API for object storage bucket
  name: XSKY os-buckets API
  slug: xsky-os-buckets-api
- description: OSCustomLabelController provides API for object storage custom label
  name: XSKY os-custom-labels API
  slug: xsky-os-custom-labels-api
- description: OSExternalStorageClassController API /os-extertal-storage-classes.
  name: XSKY os-external-storage-classes API
  slug: xsky-os-external-storage-classes-api
- description: ObjectStorageGatewayController provides API for s3 gateway
  name: XSKY os-gateways API
  slug: xsky-os-gateways-api
- description: ObjectStorageKeyController provides API for object storage key
  name: XSKY os-keys API
  slug: xsky-os-keys-api
- description: ObjectStorageLifecycleController provides API for object storage lifecycle
  name: XSKY os-lifecycles API
  slug: xsky-os-lifecycles-api
- description: OSObjectController Object Storage Object Management
  name: XSKY os-objects API
  slug: xsky-os-objects-api
- description: ObjectStoragePolicyController provides API for object storage policy
  name: XSKY os-policies API
  slug: xsky-os-policies-api
- description: OSRemotePolicyController API /os-remote-policies
  name: XSKY os-remote-policies API
  slug: xsky-os-remote-policies-api
- description: OSReplicationPathController API /os-replication-paths.
  name: XSKY os-replication-paths API
  slug: xsky-os-replication-paths-api
- description: OSReplicationZoneController API /os-replication-zones.
  name: XSKY os-replication-zones API
  slug: xsky-os-replication-zones-api
- description: OSSampleController API /os-samples
  name: XSKY os-samples API
  slug: xsky-os-samples-api
- description: OSSearchEngineController provides APIs for OS search engine
  name: XSKY os-search-engines API
  slug: xsky-os-search-engines-api
- description: OSSearchGatewayController provides API for os search gateways
  name: XSKY os-search-gateways API
  slug: xsky-os-search-gateways-api
- description: OSStorageClassController API /os-storage-classes.
  name: XSKY os-storage-classes API
  slug: xsky-os-storage-classes-api
- description: ObjectStorageUserController provides API for object storage user
  name: XSKY os-users API
  slug: xsky-os-users-api
- description: OSZoneLockController API /os-zone-locks
  name: XSKY os-zone-locks API
  slug: xsky-os-zone-locks-api
- description: OSZonePairsController API /os-zone-pairs
  name: XSKY os-zone-pairs API
  slug: xsky-os-zone-pairs-api
- description: OSZonePeriodController API /os-zone-periods
  name: XSKY os-zone-periods API
  slug: xsky-os-zone-periods-api
- description: OSZoneTranslogController API /os-zone-translogs
  name: XSKY os-zone-translogs API
  slug: xsky-os-zone-translogs-api
- description: ObjectStorageZoneController API /os-zones
  name: XSKY os-zones API
  slug: xsky-os-zones-api
- description: OsdGroupController API /osd-groups
  name: XSKY osd-groups API
  slug: xsky-osd-groups-api
- description: OsdController Osd Management
  name: XSKY osds API
  slug: xsky-osds-api
- description: PartitionController API /partitions.
  name: XSKY partitions API
  slug: xsky-partitions-api
- description: PlacementNodeController provides API for placement node
  name: XSKY placement-nodes API
  slug: xsky-placement-nodes-api
- description: PoolController Operations about Pools
  name: XSKY pools API
  slug: xsky-pools-api
- description: ProtectionDomainController Protection Domain Management
  name: XSKY protection-domains API
  slug: xsky-protection-domains-api
- description: RemoteClusterController API /remote-clusters
  name: XSKY remote-clusters API
  slug: xsky-remote-clusters-api
- description: RoleMappingController Role Mapping Management
  name: XSKY role-mappings API
  slug: xsky-role-mappings-api
- description: S3LoadBalancerGroupController API
  name: XSKY s3-load-balancer-groups API
  slug: xsky-s3-load-balancer-groups-api
- description: S3LoadBalancerController API
  name: XSKY s3-load-balancers API
  slug: xsky-s3-load-balancers-api
- description: SearchController defines search apis
  name: XSKY search API
  slug: xsky-search-api
- description: SearchCapabilityController defines search capability apis
  name: XSKY search-capabilities API
  slug: xsky-search-capabilities-api
- description: ServiceController Disk Management
  name: XSKY services API
  slug: xsky-services-api
- description: SnmpController Operations able snmp
  name: XSKY snmp API
  slug: xsky-snmp-api
- description: SSLCertificateController API
  name: XSKY ssl-certificates API
  slug: xsky-ssl-certificates-api
- description: SystemLogController provides API for system logs
  name: XSKY system-logs API
  slug: xsky-system-logs-api
- description: TargetController Operations able targets
  name: XSKY targets API
  slug: xsky-targets-api
- description: TaskController Task Management
  name: XSKY tasks API
  slug: xsky-tasks-api
- description: TrashResourceController Operations about Trash
  name: XSKY trash-resources API
  slug: xsky-trash-resources-api
- description: TrashController Operations about Trash
  name: XSKY trashes API
  slug: xsky-trashes-api
- description: UserController Manage users
  name: XSKY users API
  slug: xsky-users-api
- description: VersionController Operations about Version
  name: XSKY version API
  slug: xsky-version-api
- description: VIPGroupController API /vip-groups
  name: XSKY vip-groups API
  slug: xsky-vip-groups-api
- description: VIPInstanceController API /vip-instances
  name: XSKY vip-instances API
  slug: xsky-vip-instances-api
- description: VIPController API /vips
  name: XSKY vips API
  slug: xsky-vips-api
- description: VMFlavorController API /vm-flavors
  name: XSKY vm-flavors API
  slug: xsky-vm-flavors-api
- description: VolumeDpBlockBackupPolicyMappingController API /volume-dp-block-backup-policy-mappings
  name: XSKY volume-dp-block-backup-policy-mappings API
  slug: xsky-volume-dp-block-backup-policy-mappings-api
artifact_total: 127
common:
- group: company
  title: ''
  type: Website
  url: https://xsky.com
- group: company
  title: ''
  type: Blog
  url: https://www.xsky.com/en/about/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xsky.com/en/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.xsky.com/supports/
- group: start
  title: ''
  type: SignUp
  url: https://www.xsky.com/en/evaluate/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xsky-storage
- group: build
  title: ''
  type: Packages
  url: packages/xsky-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/xsky-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/xsky-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/xsky-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xsky-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/xsky-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/xsky-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/xsky-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.xsky.com/supports/product-lifecycle
- group: auth
  title: ''
  type: Authentication
  url: authentication/xsky-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xsky-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/xsky-conventions.yml
- group: build
  title: ''
  type: CLI
  url: cli/xsky-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/xsky-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: XSKY (XSKY Data Technology, 星辰天合) is a Beijing-based software-defined storage vendor serving nearly 2,000 large government and enterprise institutions, ranked first in China's object-storage software market. Its distributed storage products — XEUS unified storage, XEBS block storage, XEOS object storage, XGFS file storage, and the XEDP unified data platform — are all managed through XMS, the platform's REST controller API, which XSKY publishes as a Swagger 2.0 contract with official Go and Python clients plus a CloudFormation-style provisioning tool (sds-formation) and a Kubernetes CSI driver.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xsky.png
layout: provider
mcp_servers:
- description: ''
  name: xsky-mcp.yml
  slug: xsky-mcpyml
modified: '2026-07-21'
name: XSKY
nav: Providers
network: true
overview: 'XSKY publishes 124 APIs on the [APIs.io](https://apis.io/) network, including access-paths API, access-tokens API, action-logs API, and 121 more. Tagged areas include Storage, Software-Defined Storage, Object Storage, Block Storage, and File Storage.


  XSKY''s developer surface includes engineering blog, support, signup flow, authentication, CLI, and 16 more developer resources.'
random_paper: 55
score:
  band: thin
  composite: 34.3
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 37.7
    developer_ergonomics: 45.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 34.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Xsky Authentication
  slug: xsky-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Xsky Domain Security
  slug: xsky-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: xsky
tags:
- Storage
- Software-Defined Storage
- Object Storage
- Block Storage
- File Storage
- Data Infrastructure
- Enterprise
- China
website: https://xsky.com
---
