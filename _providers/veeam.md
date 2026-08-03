---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 160
  human_in_the_loop: 13
  name: Veeam Agentic Access
  operation_count: 296
  slug: veeam-agentic-access
  summary_line: 296 operations · 160 acting · 13 human-in-the-loop
api_count: 55
apis:
- description: The primary REST API for Veeam Backup & Replication, enabling programmatic management of backup jobs, restore operations, protected workloads, infrastructure components, and replication policies acros
  name: Veeam Backup & Replication REST API
  slug: veeam-backup-replication-rest-api
- description: REST API for Veeam Backup Enterprise Manager, providing centralized management of Veeam Backup & Replication servers, reporting, and enterprise-level operations exposed through a RESTful framework ove
  name: Veeam Backup Enterprise Manager REST API
  slug: veeam-backup-enterprise-manager-rest-api
- description: REST API for Veeam Backup for Microsoft 365, enabling management of backup jobs and restore operations for Exchange Online, SharePoint Online, OneDrive for Business, and Microsoft Teams. Uses HAL hype
  name: Veeam Backup for Microsoft 365 REST API
  slug: veeam-backup-for-microsoft-365-rest-api
- description: REST API for Veeam ONE, enabling monitoring, reporting, capacity planning, and intelligent diagnostics for Veeam-protected environments including VMware, Hyper-V, and Veeam Backup & Replication infras
  name: Veeam ONE REST API
  slug: veeam-one-rest-api
- description: 'REST API for Veeam Backup for AWS, enabling management of backup and recovery operations for AWS EC2 instances, RDS databases, EFS, and VPC configurations. Covers backup policies, restore points, and '
  name: Veeam Backup for AWS REST API
  slug: veeam-backup-for-aws-rest-api
- description: REST API for Veeam Backup for Microsoft Azure, providing programmatic access to backup and restore operations for Azure VMs, Azure SQL databases, and Azure File Shares. Supports management of backup p
  name: Veeam Backup for Microsoft Azure REST API
  slug: veeam-backup-for-microsoft-azure-rest-api
- description: REST API for Veeam Backup for Google Cloud, enabling management of backup and restore operations for Google Compute Engine VMs and Google Cloud SQL instances. Provides access to backup policies, resto
  name: Veeam Backup for Google Cloud REST API
  slug: veeam-backup-for-google-cloud-rest-api
- description: REST API for Veeam Recovery Orchestrator, enabling automated disaster recovery planning, orchestration testing, and failover execution. Supports management of recovery plans, compliance reports, and a
  name: Veeam Recovery Orchestrator REST API
  slug: veeam-recovery-orchestrator-rest-api
- description: The Agents section defines paths and operations for managing recovery tokens used for bare metal recovery.
  name: Veeam Agents API
  slug: veeam-agents-api
- description: The AmazonConnections API from Veeam — 9 operation(s) for amazonconnections.
  name: Veeam AmazonConnections API
  slug: veeam-amazonconnections-api
- description: The Automation section defines paths and operations for granular import and export of objects available in the REST API. It can be useful, for example, if you set up the backup infrastructure using JS
  name: Veeam Automation API
  slug: veeam-automation-api
- description: The Backup Objects section defines paths and operations for managing backup objects — virtual infrastructure objects (VMs and VM containers) that are included in backups created by the backup server.
  name: Veeam Backup Objects API
  slug: veeam-backup-objects-api
- description: The Backups section defines paths and operations for managing backups that are created on or imported to the backup server.
  name: Veeam Backups API
  slug: veeam-backups-api
- description: The Buckets API from Veeam — 5 operation(s) for buckets.
  name: Veeam Buckets API
  slug: veeam-buckets-api
- description: The Certificates API from Veeam — 3 operation(s) for certificates.
  name: Veeam Certificates API
  slug: veeam-certificates-api
- description: The Cloud Browser section defines paths and operations for retrieving information about cloud resources (compute or storage). Cloud browser helps you map a cloud folder with an object storage reposito
  name: Veeam Cloud Browser API
  slug: veeam-cloud-browser-api
- description: The Configuration Backup section defines paths and operations for managing backup of the configuration database that Veeam Backup & Replication uses.
  name: Veeam Configuration Backup API
  slug: veeam-configuration-backup-api
- description: The Connection section defines a path and operation for retrieving a TLS certificate or SSH fingerprint used to establish a secure connection between the backup server and the specified server.
  name: Veeam Connection API
  slug: veeam-connection-api
- description: The CostEstimation API from Veeam — 2 operation(s) for costestimation.
  name: Veeam CostEstimation API
  slug: veeam-costestimation-api
- description: The Credentials section defines paths and operations for managing credentials records that are added to the backup server.
  name: Veeam Credentials API
  slug: veeam-credentials-api
- description: The EmailNotifications API from Veeam — 2 operation(s) for emailnotifications.
  name: Veeam EmailNotifications API
  slug: veeam-emailnotifications-api
- description: The Encryption section defines paths and operations for managing passwords that are used for data encryption.
  name: Veeam Encryption API
  slug: veeam-encryption-api
- description: The General Options section defines paths and operations for retrieving and editing general settings of Veeam Backup & Replication.<br> <div class="note"><strong>NOTE</strong><br>In the current versio
  name: Veeam General Options API
  slug: veeam-general-options-api
- description: The IAMRoles API from Veeam — 6 operation(s) for iamroles.
  name: Veeam IAMRoles API
  slug: veeam-iamroles-api
- description: The Instances API from Veeam — 6 operation(s) for instances.
  name: Veeam Instances API
  slug: veeam-instances-api
- description: The Inventory Browser section defines paths and operations for retrieving VMware vSphere servers and their virtual infrastructure objects (data centers, clusters, hosts, resource pools, VMs).<br> <div
  name: Veeam Inventory Browser API
  slug: veeam-inventory-browser-api
- description: 'The Jobs section defines paths and operations for managing jobs that are coordinated by the backup server.<br> <div class="note"><strong>NOTE</strong><br>In the current version, the REST API supports '
  name: Veeam Jobs API
  slug: veeam-jobs-api
- description: The LicenseAgreement API from Veeam — 4 operation(s) for licenseagreement.
  name: Veeam LicenseAgreement API
  slug: veeam-licenseagreement-api
- description: The Licensing API from Veeam — 5 operation(s) for licensing.
  name: Veeam Licensing API
  slug: veeam-licensing-api
- description: The authorization process involves obtaining an access token and a refresh token.<br>For details on the authorization process and security settings, see [Authorization and Security](https://helpcenter
  name: Veeam Login API
  slug: veeam-login-api
- description: The Managed Servers section defines paths and operations for managing servers.<br> <div class="note"><strong>NOTE</strong><br>In the current version, the REST API supports the following server types&#
  name: Veeam Managed Servers API
  slug: veeam-managed-servers-api
- description: The Object Restore Points section defines paths and operations for retrieving restore points created on the backup server and backed up disks from the restore points.
  name: Veeam Object Restore Points API
  slug: veeam-object-restore-points-api
- description: The Overview API from Veeam — 1 operation(s) for overview.
  name: Veeam Overview API
  slug: veeam-overview-api
- description: The Policies API from Veeam — 15 operation(s) for policies.
  name: Veeam Policies API
  slug: veeam-policies-api
- description: The Problems API from Veeam — 17 operation(s) for problems.
  name: Veeam Problems API
  slug: veeam-problems-api
- description: The Proxies section defines paths and operations for managing backup proxies.<br><div class="note"><strong>NOTE</strong><br>In the current version, the REST API supports VMware backup proxies only.</d
  name: Veeam Proxies API
  slug: veeam-proxies-api
- description: The Regions API from Veeam — 4 operation(s) for regions.
  name: Veeam Regions API
  slug: veeam-regions-api
- description: The Repositories API from Veeam — 18 operation(s) for repositories.
  name: Veeam Repositories API
  slug: veeam-repositories-api
- description: 'The Restore section defines paths and operations for performing restore.<br> <div class="note"><strong>NOTE</strong><br>In the current version, the REST API supports the following recovery operations:'
  name: Veeam Restore API
  slug: veeam-restore-api
- description: The RetentionSettings API from Veeam — 2 operation(s) for retentionsettings.
  name: Veeam RetentionSettings API
  slug: veeam-retentionsettings-api
- description: The Service section defines paths and operations for retrieving information about the backup server where the REST API service is running.
  name: Veeam Service API
  slug: veeam-service-api
- description: The Services section defines a path and operation for retrieving information about associated backend services. You may need to connect to these services for integration with Veeam Backup & Replicatio
  name: Veeam Services API
  slug: veeam-services-api
- description: The Sessions API from Veeam — 11 operation(s) for sessions.
  name: Veeam Sessions API
  slug: veeam-sessions-api
- description: The SMTPServerCredentialsRecords API from Veeam — 4 operation(s) for smtpservercredentialsrecords.
  name: Veeam SMTPServerCredentialsRecords API
  slug: veeam-smtpservercredentialsrecords-api
- description: The Statistics API from Veeam — 1 operation(s) for statistics.
  name: Veeam Statistics API
  slug: veeam-statistics-api
- description: The System API from Veeam — 2 operation(s) for system.
  name: Veeam System API
  slug: veeam-system-api
- description: The Tags API from Veeam — 2 operation(s) for tags.
  name: Veeam Tags API
  slug: veeam-tags-api
- description: The Test API from Veeam — 1 operation(s) for test.
  name: Veeam Test API
  slug: veeam-test-api
- description: The Timezone API from Veeam — 4 operation(s) for timezone.
  name: Veeam Timezone API
  slug: veeam-timezone-api
- description: The Token API from Veeam — 2 operation(s) for token.
  name: Veeam Token API
  slug: veeam-token-api
- description: The Traffic Rules section defines paths and operations for retrieving and editing information about network traffic rules that are configured on the backup server.
  name: Veeam Traffic Rules API
  slug: veeam-traffic-rules-api
- description: The Users API from Veeam — 12 operation(s) for users.
  name: Veeam Users API
  slug: veeam-users-api
- description: The Version API from Veeam — 2 operation(s) for version.
  name: Veeam Version API
  slug: veeam-version-api
- description: The VmRestorePoints API from Veeam — 8 operation(s) for vmrestorepoints.
  name: Veeam VmRestorePoints API
  slug: veeam-vmrestorepoints-api
- description: The Workers API from Veeam — 3 operation(s) for workers.
  name: Veeam Workers API
  slug: veeam-workers-api
artifact_total: 73
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/veeam-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/veeam-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veeam-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/veeam-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.veeam.com/
- group: docs
  title: ''
  type: Documentation
  url: https://helpcenter.veeam.com/category/development.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/VeeamHub
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/veeam-software
- group: company
  title: ''
  type: Blog
  url: https://www.veeam.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.veeam.com/store/
- group: operate
  title: ''
  type: StatusPage
  url: https://vdcstatus.veeam.com/
- group: other
  title: ''
  type: X
  url: https://x.com/veeam
- group: commercial
  title: ''
  type: Plans
  url: plans/veeam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/veeam-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/veeam-finops.yml
created: '2026-06-13'
description: Veeam is a backup and data management platform providing REST APIs for managing backup jobs, restore operations, protected workloads, and cloud backup policies across on-premises, virtual, and cloud environments. The Veeam platform covers Backup & Replication, Backup for Microsoft 365, Backup for AWS, Azure, and Google Cloud, Veeam ONE monitoring, Recovery Orchestrator, and Service Provider Console.
examples:
- key_count: 1
  name: Veeam Backup Replication Examples
  slug: veeam-backup-replication-examples
finops:
- name: Veeam Finops
  service_category: ''
  slug: veeam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/veeam.png
json_schemas:
- name: BackupJobModel
  property_count: 0
  slug: backup-job-model
- name: BackupJobSpec
  property_count: 0
  slug: backup-job-spec
- name: BackupJobStorageModel
  property_count: 5
  slug: backup-job-storage-model
- name: CredentialsModel
  property_count: 0
  slug: credentials-model
- name: JobModel
  property_count: 0
  slug: job-model
- name: ProxyModel
  property_count: 0
  slug: proxy-model
- name: RepositoryModel
  property_count: 0
  slug: repository-model
- name: SessionModel
  property_count: 13
  slug: session-model
jsonld:
- class_count: 16
  name: Veeam Context
  property_count: 42
  slug: veeam-context
layout: provider
modified: '2026-06-13'
name: Veeam
nav: Providers
network: true
overview: 'Veeam publishes 47 APIs on the [APIs.io](https://apis.io/) network, including Agents API, AmazonConnections API, Automation API, and 44 more. Tagged areas include Backup, Data Management, Disaster Recovery, Cloud Backup, and Restore.


  The Veeam catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Veeam''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Veeam Plans Pricing
  plan_count: 5
  slug: veeam-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 0
  name: Veeam Rate Limits
  slug: veeam-rate-limits
rules:
- name: Veeam API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: veeam-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.2
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 47
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/veeam/refs/heads/main/screenshots/veeam-2026-06-20T200904.png
security:
- kind: authentication
  name: Veeam Authentication
  slug: veeam-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Veeam Domain Security
  slug: veeam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Veeam Vulnerability Disclosure
  slug: veeam-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: veeam
tags:
- Backup
- Data Management
- Disaster Recovery
- Cloud Backup
- Restore
- Replication
- Data Protection
- Microsoft 365
- Azure
- Google Cloud
- Ransomware Recovery
website: https://www.veeam.com/
---
