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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: AccessPathController Operations able access paths
  name: XSKY access-paths API
  slug: xsky-access-paths-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: AccessTokenController Manage users
  name: XSKY access-tokens API
  slug: xsky-access-tokens-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ActionLogController Operations about ActionLog
  name: XSKY action-logs API
  slug: xsky-action-logs-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: AlertGroupController Operations about alert group
  name: XSKY alert-groups API
  slug: xsky-alert-groups-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: AlertRuleController Operations about alert rule
  name: XSKY alert-rules API
  slug: xsky-alert-rules-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: AlertController Operations about alert
  name: XSKY alerts API
  slug: xsky-alerts-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: AuthController Manage authentication and authorization
  name: XSKY auth API
  slug: xsky-auth-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: BlockSnapshotController Operations about Block Snapshot
  name: XSKY block-snapshots API
  slug: xsky-block-snapshots-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: VolumeGroupSnapshotController Operations about volume group snapshot
  name: XSKY block-volume-group-snapshots API
  slug: xsky-block-volume-group-snapshots-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: VolumeGroupController Operations about volume group
  name: XSKY block-volume-groups API
  slug: xsky-block-volume-groups-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: BlockVolumeMigrationJobController Operations about block volume migration job
  name: XSKY block-volume-migration-jobs API
  slug: xsky-block-volume-migration-jobs-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: BlockVolumeController Operations about Block
  name: XSKY block-volumes API
  slug: xsky-block-volumes-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ChunkController Chunk Management
  name: XSKY chunks API
  slug: xsky-chunks-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ClientCodeController Operations about client code
  name: XSKY client-codes API
  slug: xsky-client-codes-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ClientGroupController Operations about client group
  name: XSKY client-groups API
  slug: xsky-client-groups-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ClientLunMappingController API /client-lun-mappings
  name: XSKY client-lun-mappings API
  slug: xsky-client-lun-mappings-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ClientController API /clients
  name: XSKY clients API
  slug: xsky-clients-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: CloudInstanceController Cloud Instance Management
  name: XSKY cloud-instances API
  slug: xsky-cloud-instances-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: CloudPlatformController Cloud Platform Management
  name: XSKY cloud-platforms API
  slug: xsky-cloud-platforms-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: CloudVolumeAttachmentController Cloud Volume Attachment Management
  name: XSKY cloud-volume-attachments API
  slug: xsky-cloud-volume-attachments-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: CloudVolumeController Cloud Volume Management
  name: XSKY cloud-volumes API
  slug: xsky-cloud-volumes-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ClusterController API /cluster
  name: XSKY cluster API
  slug: xsky-cluster-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ConfController Operations about Config
  name: XSKY confs API
  slug: xsky-confs-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: CryptoKeyController API /crypto-keys/
  name: XSKY crypto-keys API
  slug: xsky-crypto-keys-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: DiskController Disk Management
  name: XSKY disks API
  slug: xsky-disks-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: DomainUserValidatorController Domain User Validator Management
  name: XSKY domain-user-validators API
  slug: xsky-domain-user-validators-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: DpBlockBackupJobController API /dp-block-backup-jobs/
  name: XSKY dp-block-backup-jobs API
  slug: xsky-dp-block-backup-jobs-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: DpBlockBackupPolicyController API /dp-block-backup-policies
  name: XSKY dp-block-backup-policies API
  slug: xsky-dp-block-backup-policies-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: DpBlockReplicationPolicyController API /dp-block-replication-policies
  name: XSKY dp-block-replication-policies API
  slug: xsky-dp-block-replication-policies-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: DpBlockSnapshotJobController API /dp-block-snapshot-jobs/
  name: XSKY dp-block-snapshot-jobs API
  slug: xsky-dp-block-snapshot-jobs-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: DpBlockSnapshotPolicyController API /dp-block-snapshot-policies
  name: XSKY dp-block-snapshot-policies API
  slug: xsky-dp-block-snapshot-policies-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: DpBlockSnapshotRecoveryJobController API /dp-block-snapshot-recovery-jobs
  name: XSKY dp-block-snapshot-recovery-jobs API
  slug: xsky-dp-block-snapshot-recovery-jobs-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: DpFSSnapshotJobController API /dp-fs-snapshot-jobs/
  name: XSKY dp-fs-snapshot-jobs API
  slug: xsky-dp-fs-snapshot-jobs-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: DpFSSnapshotPolicyController API /dp-fs-snapshot-policies
  name: XSKY dp-fs-snapshot-policies API
  slug: xsky-dp-fs-snapshot-policies-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: DpGatewayController API /dp-gateways/
  name: XSKY dp-gateways API
  slug: xsky-dp-gateways-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: DpSiteController API /dp-sites/
  name: XSKY dp-sites API
  slug: xsky-dp-sites-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: EmailGroupController Operations about Email
  name: XSKY email-groups API
  slug: xsky-email-groups-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: EmailController Operations about Email
  name: XSKY emails API
  slug: xsky-emails-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: EventLogController Operations about EventLog
  name: XSKY event-logs API
  slug: xsky-event-logs-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSActiveDirectoryController File Storage Active Directory Management
  name: XSKY fs-active-directories API
  slug: xsky-fs-active-directories-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSArbitrationPoolController File Storage Arbitration Pool Management
  name: XSKY fs-arbitration-pools API
  slug: xsky-fs-arbitration-pools-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSClientGroupController provides APIs for file storage client group
  name: XSKY fs-client-groups API
  slug: xsky-fs-client-groups-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSClientController provides APIs for file storage client
  name: XSKY fs-clients API
  slug: xsky-fs-clients-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSFolderController provides API for file storage folder
  name: XSKY fs-folders API
  slug: xsky-fs-folders-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSFTPSessionController provides API for fs FTP session
  name: XSKY fs-ftp-sessions API
  slug: xsky-fs-ftp-sessions-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSFTPShareACLController provides API for fs ftp share acl
  name: XSKY fs-ftp-share-acls API
  slug: xsky-fs-ftp-share-acls-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSFTPShareController provides API for fs ftp share
  name: XSKY fs-ftp-shares API
  slug: xsky-fs-ftp-shares-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSGatewayGroupController provides APIs for file storage gateway group
  name: XSKY fs-gateway-groups API
  slug: xsky-fs-gateway-groups-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSGatewayController provides APIs for file storage gateway
  name: XSKY fs-gateways API
  slug: xsky-fs-gateways-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSLdapController File Storage LDAP Management
  name: XSKY fs-ldaps API
  slug: xsky-fs-ldaps-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSNFSConnectionController provides API for fs NFS connection
  name: XSKY fs-nfs-connections API
  slug: xsky-fs-nfs-connections-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSNFSShareACLController provides API for fs nfs shares acl
  name: XSKY fs-nfs-share-acls API
  slug: xsky-fs-nfs-share-acls-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSNFSShareController provides API for fs nfs shares
  name: XSKY fs-nfs-shares API
  slug: xsky-fs-nfs-shares-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSQuotaTreeController provides API for file storage quota tree
  name: XSKY fs-quota-trees API
  slug: xsky-fs-quota-trees-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSSMBSessionController provides API for fs SMB session
  name: XSKY fs-smb-sessions API
  slug: xsky-fs-smb-sessions-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSSMBShareACLController provides API for fs smb share acl
  name: XSKY fs-smb-share-acls API
  slug: xsky-fs-smb-share-acls-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSSMBShareController provides API for fs smb share
  name: XSKY fs-smb-shares API
  slug: xsky-fs-smb-shares-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSSnapshotController provides APIs for file storage snapshot
  name: XSKY fs-snapshots API
  slug: xsky-fs-snapshots-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSUserGroupController provides APIs for file storage user group
  name: XSKY fs-user-groups API
  slug: xsky-fs-user-groups-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: FSUserController provides API for file storage user
  name: XSKY fs-users API
  slug: xsky-fs-users-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: HostEncSpecController API /host-enc-specs/
  name: XSKY host-enc-specs API
  slug: xsky-host-enc-specs-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: HostInfoController Host Info Management
  name: XSKY host-info API
  slug: xsky-host-info-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: HostInitializationController provides API for host initialization
  name: XSKY host-initializations API
  slug: xsky-host-initializations-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: HostValidatorController Host Validator Management
  name: XSKY host-validators API
  slug: xsky-host-validators-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: HostController Host Management
  name: XSKY hosts API
  slug: xsky-hosts-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: IdentityPlatformController Identity Platform Management
  name: XSKY identity-platforms API
  slug: xsky-identity-platforms-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: LicenseController Operations about Install
  name: XSKY licenses API
  slug: xsky-licenses-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: LunController Operations on luns
  name: XSKY luns API
  slug: xsky-luns-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: MappingGroupController Operations able mapping groups
  name: XSKY mapping-groups API
  slug: xsky-mapping-groups-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: NetworkAddressController Network Address Management
  name: XSKY network-addresses API
  slug: xsky-network-addresses-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: NetworkDiagnosisController provides API for network diagnosis
  name: XSKY network-diagnoses API
  slug: xsky-network-diagnoses-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: NetworkDiagnosisItemController provides API for network diagnosis item
  name: XSKY network-diagnosis-items API
  slug: xsky-network-diagnosis-items-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: NetworkInterfaceController Network Interface Management
  name: XSKY network-interfaces API
  slug: xsky-network-interfaces-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: NFSGatewayBucketMapController provides API for object storage nfs gateway s3 bucket map
  name: XSKY nfs-gateway-bucket-maps API
  slug: xsky-nfs-gateway-bucket-maps-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: NFSGatewayController provides API for object storage nfs gateway
  name: XSKY nfs-gateways API
  slug: xsky-nfs-gateways-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OSBucketLoggingController API /os-bucket-loggings.
  name: XSKY os-bucket-loggings API
  slug: xsky-os-bucket-loggings-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ObjectStorageBucketController provides API for object storage bucket
  name: XSKY os-buckets API
  slug: xsky-os-buckets-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OSCustomLabelController provides API for object storage custom label
  name: XSKY os-custom-labels API
  slug: xsky-os-custom-labels-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OSExternalStorageClassController API /os-extertal-storage-classes.
  name: XSKY os-external-storage-classes API
  slug: xsky-os-external-storage-classes-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ObjectStorageGatewayController provides API for s3 gateway
  name: XSKY os-gateways API
  slug: xsky-os-gateways-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ObjectStorageKeyController provides API for object storage key
  name: XSKY os-keys API
  slug: xsky-os-keys-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ObjectStorageLifecycleController provides API for object storage lifecycle
  name: XSKY os-lifecycles API
  slug: xsky-os-lifecycles-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OSObjectController Object Storage Object Management
  name: XSKY os-objects API
  slug: xsky-os-objects-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ObjectStoragePolicyController provides API for object storage policy
  name: XSKY os-policies API
  slug: xsky-os-policies-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OSRemotePolicyController API /os-remote-policies
  name: XSKY os-remote-policies API
  slug: xsky-os-remote-policies-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OSReplicationPathController API /os-replication-paths.
  name: XSKY os-replication-paths API
  slug: xsky-os-replication-paths-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OSReplicationZoneController API /os-replication-zones.
  name: XSKY os-replication-zones API
  slug: xsky-os-replication-zones-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OSSampleController API /os-samples
  name: XSKY os-samples API
  slug: xsky-os-samples-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OSSearchEngineController provides APIs for OS search engine
  name: XSKY os-search-engines API
  slug: xsky-os-search-engines-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OSSearchGatewayController provides API for os search gateways
  name: XSKY os-search-gateways API
  slug: xsky-os-search-gateways-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OSStorageClassController API /os-storage-classes.
  name: XSKY os-storage-classes API
  slug: xsky-os-storage-classes-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ObjectStorageUserController provides API for object storage user
  name: XSKY os-users API
  slug: xsky-os-users-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OSZoneLockController API /os-zone-locks
  name: XSKY os-zone-locks API
  slug: xsky-os-zone-locks-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OSZonePairsController API /os-zone-pairs
  name: XSKY os-zone-pairs API
  slug: xsky-os-zone-pairs-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OSZonePeriodController API /os-zone-periods
  name: XSKY os-zone-periods API
  slug: xsky-os-zone-periods-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OSZoneTranslogController API /os-zone-translogs
  name: XSKY os-zone-translogs API
  slug: xsky-os-zone-translogs-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ObjectStorageZoneController API /os-zones
  name: XSKY os-zones API
  slug: xsky-os-zones-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OsdGroupController API /osd-groups
  name: XSKY osd-groups API
  slug: xsky-osd-groups-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: OsdController Osd Management
  name: XSKY osds API
  slug: xsky-osds-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: PartitionController API /partitions.
  name: XSKY partitions API
  slug: xsky-partitions-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: PlacementNodeController provides API for placement node
  name: XSKY placement-nodes API
  slug: xsky-placement-nodes-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: PoolController Operations about Pools
  name: XSKY pools API
  slug: xsky-pools-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ProtectionDomainController Protection Domain Management
  name: XSKY protection-domains API
  slug: xsky-protection-domains-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: RemoteClusterController API /remote-clusters
  name: XSKY remote-clusters API
  slug: xsky-remote-clusters-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: RoleMappingController Role Mapping Management
  name: XSKY role-mappings API
  slug: xsky-role-mappings-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: S3LoadBalancerGroupController API
  name: XSKY s3-load-balancer-groups API
  slug: xsky-s3-load-balancer-groups-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: S3LoadBalancerController API
  name: XSKY s3-load-balancers API
  slug: xsky-s3-load-balancers-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: SearchController defines search apis
  name: XSKY search API
  slug: xsky-search-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: SearchCapabilityController defines search capability apis
  name: XSKY search-capabilities API
  slug: xsky-search-capabilities-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: ServiceController Disk Management
  name: XSKY services API
  slug: xsky-services-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: SnmpController Operations able snmp
  name: XSKY snmp API
  slug: xsky-snmp-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: SSLCertificateController API
  name: XSKY ssl-certificates API
  slug: xsky-ssl-certificates-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: SystemLogController provides API for system logs
  name: XSKY system-logs API
  slug: xsky-system-logs-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: TargetController Operations able targets
  name: XSKY targets API
  slug: xsky-targets-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: TaskController Task Management
  name: XSKY tasks API
  slug: xsky-tasks-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: TrashResourceController Operations about Trash
  name: XSKY trash-resources API
  slug: xsky-trash-resources-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: TrashController Operations about Trash
  name: XSKY trashes API
  slug: xsky-trashes-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: UserController Manage users
  name: XSKY users API
  slug: xsky-users-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: VersionController Operations about Version
  name: XSKY version API
  slug: xsky-version-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: VIPGroupController API /vip-groups
  name: XSKY vip-groups API
  slug: xsky-vip-groups-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: VIPInstanceController API /vip-instances
  name: XSKY vip-instances API
  slug: xsky-vip-instances-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: VIPController API /vips
  name: XSKY vips API
  slug: xsky-vips-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: VMFlavorController API /vm-flavors
  name: XSKY vm-flavors API
  slug: xsky-vm-flavors-api
- baseURL: https://{xms-controller}/v1
  baseurl_source: declared
  description: VolumeDpBlockBackupPolicyMappingController API /volume-dp-block-backup-policy-mappings
  name: XSKY volume-dp-block-backup-policy-mappings API
  slug: xsky-volume-dp-block-backup-policy-mappings-api
artifact_total: 252
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: XMS access-paths API
  slug: open-xsky-access-paths-api
- collection_type: open
  name: XMS access-paths access-tokens API
  slug: open-xsky-access-tokens-api
- collection_type: open
  name: XMS access-paths action-logs API
  slug: open-xsky-action-logs-api
- collection_type: open
  name: XMS access-paths alert-groups API
  slug: open-xsky-alert-groups-api
- collection_type: open
  name: XMS access-paths alert-rules API
  slug: open-xsky-alert-rules-api
- collection_type: open
  name: XMS access-paths alerts API
  slug: open-xsky-alerts-api
- collection_type: open
  name: XMS access-paths auth API
  slug: open-xsky-auth-api
- collection_type: open
  name: XMS access-paths block-snapshots API
  slug: open-xsky-block-snapshots-api
- collection_type: open
  name: XMS access-paths block-volume-group-snapshots API
  slug: open-xsky-block-volume-group-snapshots-api
- collection_type: open
  name: XMS access-paths block-volume-groups API
  slug: open-xsky-block-volume-groups-api
- collection_type: open
  name: XMS access-paths block-volume-migration-jobs API
  slug: open-xsky-block-volume-migration-jobs-api
- collection_type: open
  name: XMS access-paths block-volumes API
  slug: open-xsky-block-volumes-api
- collection_type: open
  name: XMS access-paths chunks API
  slug: open-xsky-chunks-api
- collection_type: open
  name: XMS access-paths client-codes API
  slug: open-xsky-client-codes-api
- collection_type: open
  name: XMS access-paths client-groups API
  slug: open-xsky-client-groups-api
- collection_type: open
  name: XMS access-paths client-lun-mappings API
  slug: open-xsky-client-lun-mappings-api
- collection_type: open
  name: XMS access-paths clients API
  slug: open-xsky-clients-api
- collection_type: open
  name: XMS access-paths cloud-instances API
  slug: open-xsky-cloud-instances-api
- collection_type: open
  name: XMS access-paths cloud-platforms API
  slug: open-xsky-cloud-platforms-api
- collection_type: open
  name: XMS access-paths cloud-volume-attachments API
  slug: open-xsky-cloud-volume-attachments-api
- collection_type: open
  name: XMS access-paths cloud-volumes API
  slug: open-xsky-cloud-volumes-api
- collection_type: open
  name: XMS access-paths cluster API
  slug: open-xsky-cluster-api
- collection_type: open
  name: XMS access-paths confs API
  slug: open-xsky-confs-api
- collection_type: open
  name: XMS access-paths crypto-keys API
  slug: open-xsky-crypto-keys-api
- collection_type: open
  name: XMS access-paths disks API
  slug: open-xsky-disks-api
- collection_type: open
  name: XMS access-paths domain-user-validators API
  slug: open-xsky-domain-user-validators-api
- collection_type: open
  name: XMS access-paths dp-block-backup-jobs API
  slug: open-xsky-dp-block-backup-jobs-api
- collection_type: open
  name: XMS access-paths dp-block-backup-policies API
  slug: open-xsky-dp-block-backup-policies-api
- collection_type: open
  name: XMS access-paths dp-block-replication-policies API
  slug: open-xsky-dp-block-replication-policies-api
- collection_type: open
  name: XMS access-paths dp-block-snapshot-jobs API
  slug: open-xsky-dp-block-snapshot-jobs-api
- collection_type: open
  name: XMS access-paths dp-block-snapshot-policies API
  slug: open-xsky-dp-block-snapshot-policies-api
- collection_type: open
  name: XMS access-paths dp-block-snapshot-recovery-jobs API
  slug: open-xsky-dp-block-snapshot-recovery-jobs-api
- collection_type: open
  name: XMS access-paths dp-fs-snapshot-jobs API
  slug: open-xsky-dp-fs-snapshot-jobs-api
- collection_type: open
  name: XMS access-paths dp-fs-snapshot-policies API
  slug: open-xsky-dp-fs-snapshot-policies-api
- collection_type: open
  name: XMS access-paths dp-gateways API
  slug: open-xsky-dp-gateways-api
- collection_type: open
  name: XMS access-paths dp-sites API
  slug: open-xsky-dp-sites-api
- collection_type: open
  name: XMS access-paths email-groups API
  slug: open-xsky-email-groups-api
- collection_type: open
  name: XMS access-paths emails API
  slug: open-xsky-emails-api
- collection_type: open
  name: XMS access-paths event-logs API
  slug: open-xsky-event-logs-api
- collection_type: open
  name: XMS access-paths fs-active-directories API
  slug: open-xsky-fs-active-directories-api
- collection_type: open
  name: XMS access-paths fs-arbitration-pools API
  slug: open-xsky-fs-arbitration-pools-api
- collection_type: open
  name: XMS access-paths fs-client-groups API
  slug: open-xsky-fs-client-groups-api
- collection_type: open
  name: XMS access-paths fs-clients API
  slug: open-xsky-fs-clients-api
- collection_type: open
  name: XMS access-paths fs-folders API
  slug: open-xsky-fs-folders-api
- collection_type: open
  name: XMS access-paths fs-ftp-sessions API
  slug: open-xsky-fs-ftp-sessions-api
- collection_type: open
  name: XMS access-paths fs-ftp-share-acls API
  slug: open-xsky-fs-ftp-share-acls-api
- collection_type: open
  name: XMS access-paths fs-ftp-shares API
  slug: open-xsky-fs-ftp-shares-api
- collection_type: open
  name: XMS access-paths fs-gateway-groups API
  slug: open-xsky-fs-gateway-groups-api
- collection_type: open
  name: XMS access-paths fs-gateways API
  slug: open-xsky-fs-gateways-api
- collection_type: open
  name: XMS access-paths fs-ldaps API
  slug: open-xsky-fs-ldaps-api
- collection_type: open
  name: XMS access-paths fs-nfs-connections API
  slug: open-xsky-fs-nfs-connections-api
- collection_type: open
  name: XMS access-paths fs-nfs-share-acls API
  slug: open-xsky-fs-nfs-share-acls-api
- collection_type: open
  name: XMS access-paths fs-nfs-shares API
  slug: open-xsky-fs-nfs-shares-api
- collection_type: open
  name: XMS access-paths fs-quota-trees API
  slug: open-xsky-fs-quota-trees-api
- collection_type: open
  name: XMS access-paths fs-smb-sessions API
  slug: open-xsky-fs-smb-sessions-api
- collection_type: open
  name: XMS access-paths fs-smb-share-acls API
  slug: open-xsky-fs-smb-share-acls-api
- collection_type: open
  name: XMS access-paths fs-smb-shares API
  slug: open-xsky-fs-smb-shares-api
- collection_type: open
  name: XMS access-paths fs-snapshots API
  slug: open-xsky-fs-snapshots-api
- collection_type: open
  name: XMS access-paths fs-user-groups API
  slug: open-xsky-fs-user-groups-api
- collection_type: open
  name: XMS access-paths fs-users API
  slug: open-xsky-fs-users-api
- collection_type: open
  name: XMS access-paths host-enc-specs API
  slug: open-xsky-host-enc-specs-api
- collection_type: open
  name: XMS access-paths host-info API
  slug: open-xsky-host-info-api
- collection_type: open
  name: XMS access-paths host-initializations API
  slug: open-xsky-host-initializations-api
- collection_type: open
  name: XMS access-paths host-validators API
  slug: open-xsky-host-validators-api
- collection_type: open
  name: XMS access-paths hosts API
  slug: open-xsky-hosts-api
- collection_type: open
  name: XMS access-paths identity-platforms API
  slug: open-xsky-identity-platforms-api
- collection_type: open
  name: XMS access-paths licenses API
  slug: open-xsky-licenses-api
- collection_type: open
  name: XMS access-paths luns API
  slug: open-xsky-luns-api
- collection_type: open
  name: XMS access-paths mapping-groups API
  slug: open-xsky-mapping-groups-api
- collection_type: open
  name: XMS access-paths network-addresses API
  slug: open-xsky-network-addresses-api
- collection_type: open
  name: XMS access-paths network-diagnoses API
  slug: open-xsky-network-diagnoses-api
- collection_type: open
  name: XMS access-paths network-diagnosis-items API
  slug: open-xsky-network-diagnosis-items-api
- collection_type: open
  name: XMS access-paths network-interfaces API
  slug: open-xsky-network-interfaces-api
- collection_type: open
  name: XMS access-paths nfs-gateway-bucket-maps API
  slug: open-xsky-nfs-gateway-bucket-maps-api
- collection_type: open
  name: XMS access-paths nfs-gateways API
  slug: open-xsky-nfs-gateways-api
- collection_type: open
  name: XMS access-paths os-bucket-loggings API
  slug: open-xsky-os-bucket-loggings-api
- collection_type: open
  name: XMS access-paths os-buckets API
  slug: open-xsky-os-buckets-api
- collection_type: open
  name: XMS access-paths os-custom-labels API
  slug: open-xsky-os-custom-labels-api
- collection_type: open
  name: XMS access-paths os-external-storage-classes API
  slug: open-xsky-os-external-storage-classes-api
- collection_type: open
  name: XMS access-paths os-gateways API
  slug: open-xsky-os-gateways-api
- collection_type: open
  name: XMS access-paths os-keys API
  slug: open-xsky-os-keys-api
- collection_type: open
  name: XMS access-paths os-lifecycles API
  slug: open-xsky-os-lifecycles-api
- collection_type: open
  name: XMS access-paths os-objects API
  slug: open-xsky-os-objects-api
- collection_type: open
  name: XMS access-paths os-policies API
  slug: open-xsky-os-policies-api
- collection_type: open
  name: XMS access-paths os-remote-policies API
  slug: open-xsky-os-remote-policies-api
- collection_type: open
  name: XMS access-paths os-replication-paths API
  slug: open-xsky-os-replication-paths-api
- collection_type: open
  name: XMS access-paths os-replication-zones API
  slug: open-xsky-os-replication-zones-api
- collection_type: open
  name: XMS access-paths os-samples API
  slug: open-xsky-os-samples-api
- collection_type: open
  name: XMS access-paths os-search-engines API
  slug: open-xsky-os-search-engines-api
- collection_type: open
  name: XMS access-paths os-search-gateways API
  slug: open-xsky-os-search-gateways-api
- collection_type: open
  name: XMS access-paths os-storage-classes API
  slug: open-xsky-os-storage-classes-api
- collection_type: open
  name: XMS access-paths os-users API
  slug: open-xsky-os-users-api
- collection_type: open
  name: XMS access-paths os-zone-locks API
  slug: open-xsky-os-zone-locks-api
- collection_type: open
  name: XMS access-paths os-zone-pairs API
  slug: open-xsky-os-zone-pairs-api
- collection_type: open
  name: XMS access-paths os-zone-periods API
  slug: open-xsky-os-zone-periods-api
- collection_type: open
  name: XMS access-paths os-zone-translogs API
  slug: open-xsky-os-zone-translogs-api
- collection_type: open
  name: XMS access-paths os-zones API
  slug: open-xsky-os-zones-api
- collection_type: open
  name: XMS access-paths osd-groups API
  slug: open-xsky-osd-groups-api
- collection_type: open
  name: XMS access-paths osds API
  slug: open-xsky-osds-api
- collection_type: open
  name: XMS access-paths partitions API
  slug: open-xsky-partitions-api
- collection_type: open
  name: XMS access-paths placement-nodes API
  slug: open-xsky-placement-nodes-api
- collection_type: open
  name: XMS access-paths pools API
  slug: open-xsky-pools-api
- collection_type: open
  name: XMS access-paths protection-domains API
  slug: open-xsky-protection-domains-api
- collection_type: open
  name: XMS access-paths remote-clusters API
  slug: open-xsky-remote-clusters-api
- collection_type: open
  name: XMS access-paths role-mappings API
  slug: open-xsky-role-mappings-api
- collection_type: open
  name: XMS access-paths s3-load-balancer-groups API
  slug: open-xsky-s3-load-balancer-groups-api
- collection_type: open
  name: XMS access-paths s3-load-balancers API
  slug: open-xsky-s3-load-balancers-api
- collection_type: open
  name: XMS access-paths search API
  slug: open-xsky-search-api
- collection_type: open
  name: XMS access-paths search-capabilities API
  slug: open-xsky-search-capabilities-api
- collection_type: open
  name: XMS access-paths services API
  slug: open-xsky-services-api
- collection_type: open
  name: XMS access-paths snmp API
  slug: open-xsky-snmp-api
- collection_type: open
  name: XMS access-paths ssl-certificates API
  slug: open-xsky-ssl-certificates-api
- collection_type: open
  name: XMS access-paths system-logs API
  slug: open-xsky-system-logs-api
- collection_type: open
  name: XMS access-paths targets API
  slug: open-xsky-targets-api
- collection_type: open
  name: XMS access-paths tasks API
  slug: open-xsky-tasks-api
- collection_type: open
  name: XMS access-paths trash-resources API
  slug: open-xsky-trash-resources-api
- collection_type: open
  name: XMS access-paths trashes API
  slug: open-xsky-trashes-api
- collection_type: open
  name: XMS access-paths users API
  slug: open-xsky-users-api
- collection_type: open
  name: XMS access-paths version API
  slug: open-xsky-version-api
- collection_type: open
  name: XMS access-paths vip-groups API
  slug: open-xsky-vip-groups-api
- collection_type: open
  name: XMS access-paths vip-instances API
  slug: open-xsky-vip-instances-api
- collection_type: open
  name: XMS access-paths vips API
  slug: open-xsky-vips-api
- collection_type: open
  name: XMS access-paths vm-flavors API
  slug: open-xsky-vm-flavors-api
- collection_type: open
  name: XMS access-paths volume-dp-block-backup-policy-mappings API
  slug: open-xsky-volume-dp-block-backup-policy-mappings-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/xsky-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/xsky-xms-overlay.yaml
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
- description: No official XSKY-hosted MCP server was found (searched xsky.com, the xsky-storage GitHub org, and npm). This is a candidate tool surface derived one-tool-per-operation from the XMS Swagger 2.0 contrac
  name: XSKY MCP Server
  slug: xsky-mcp-server
modified: '2026-07-21'
name: XSKY
nav: Providers
network: true
overview: 'XSKY publishes 124 APIs on the [APIs.io](https://apis.io/) network, including access-paths API, access-tokens API, action-logs API, and 121 more. Tagged areas include Storage, Software-Defined Storage, Object Storage, Block Storage, and File Storage.


  XSKY''s developer surface includes engineering blog, support, signup flow, authentication, CLI, and 18 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 86.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 46.2
    developer_ergonomics: 39.9
    discoverability: 61.1
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 31.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 124
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xsky/refs/heads/main/screenshots/xsky-2026-09-02T171207.png
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
