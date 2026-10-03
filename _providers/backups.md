---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 28
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering backup, disaster recovery, and data protection APIs. Backup APIs enable applications and platforms to schedule, orchestrate, and verify the copying of data from production systems to durable storage targets, manage retention and immutability policies, and recover workloads after incidents ranging from accidental deletion to ransomware. This collection spans enterprise backup platforms like Veeam, Commvault, Rubrik, and Cohesity, SaaS data backup providers like Rewind, OwnBackup, Spanning, and Backupify, endpoint and cloud backup services like Acronis, Druva, and Carbonite, cloud-native backup services from AWS, Azure, and Google Cloud, open-source tools like Restic, BorgBackup, and Duplicati, and storage targets used as backup destinations such as Backblaze B2 and Wasabi.
examples:
- key_count: 13
  name: Backups Backup Job Example
  slug: backups-backup-job-example
- key_count: 14
  name: Backups Recovery Point Example
  slug: backups-recovery-point-example
features:
- description: Backup APIs schedule, trigger, and monitor backup jobs across servers, virtual machines, databases, SaaS tenants, and endpoints, with policy-driven recurrence and dependency management.
  name: Backup Job Orchestration
- description: APIs enumerate and inspect recovery points (snapshots, restore points, incremental chains) so that operators and automation can pick the right point in time for granular or full recovery.
  name: Recovery Point Management
- description: Backup platforms expose retention rules, GFS (grandfather-father-son) schedules, and lifecycle transitions that move data between hot, cold, and archive tiers like S3 Glacier or Azure Archive.
  name: Retention and Lifecycle Policies
- description: Modern backup APIs configure object lock, WORM storage, air-gapped copies, and anomaly detection to defend recovery data against ransomware and insider tampering.
  name: Immutability and Ransomware Protection
- description: SaaS-focused providers like Rewind, OwnBackup, Spanning, and Backupify back up Salesforce, Microsoft 365, Google Workspace, GitHub, Shopify, and other tenant data through vendor APIs.
  name: SaaS Data Backup
- description: DR APIs from AWS, Azure, VMware, and Veeam coordinate failover, failback, runbook execution, and recovery validation across primary and secondary sites or cloud regions.
  name: Disaster Recovery Orchestration
- description: Backup APIs write to a mix of on-prem appliances, object storage (Backblaze B2, Wasabi, S3, Azure Blob), and cloud-native services, enabling 3-2-1 strategies across providers.
  name: Cross-Cloud and Hybrid Targets
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Backup, replication, and disaster recovery platform for VMs, physical servers, cloud workloads, and Microsoft 365 with a comprehensive REST API.
  name: Veeam
- description: Enterprise data protection and backup platform with REST APIs for jobs, clients, storage policies, and disaster recovery orchestration.
  name: Commvault
- description: Cloud data management and backup platform with REST APIs covering SLA domains, snapshots, recovery, and ransomware investigation.
  name: Rubrik
- description: Hyperconverged data protection and backup platform with REST APIs for protection jobs, sources, views, and recovery operations.
  name: Cohesity
- description: Centralized, policy-based AWS service that automates backup of EBS, RDS, DynamoDB, EFS, S3, and other AWS resources via API and IaC.
  name: AWS Backup
- description: Azure-native backup service that protects VMs, files, SQL, and SAP HANA workloads, with REST APIs for vaults, policies, and recovery points.
  name: Microsoft Azure Backup
- description: SaaS-delivered data protection for endpoints, data centers, and cloud workloads with APIs for backups, restores, and compliance reporting.
  name: Druva
- description: Low-cost cloud object storage commonly used as a backup target via S3-compatible APIs, supporting object lock and lifecycle rules.
  name: Backblaze B2
json_schemas:
- name: BackupJob
  property_count: 13
  slug: backups-backup-job
- name: RecoveryPoint
  property_count: 14
  slug: backups-recovery-point
json_structures:
- name: Backups Backup Job Structure
  property_count: 13
  slug: backups-backup-job-structure
- name: Backups Recovery Point Structure
  property_count: 14
  slug: backups-recovery-point-structure
jsonld:
- class_count: 9
  name: Backups Context
  property_count: 28
  slug: backups-context
layout: provider
modified: '2026-05-19'
name: Backups
nav: Providers
network: true
overview: 'Backups is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Backup, Disaster Recovery, Data Protection, Snapshot, and Archives.


  The Backups catalog on APIs.io includes 1 JSON-LD context.


  Backups'' developer surface includes developer portal and 1 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: backups
tags:
- Backup
- Disaster Recovery
- Data Protection
- Snapshot
- Archives
use_cases:
- description: Organizations use backup APIs to identify the most recent clean recovery point after a ransomware event and orchestrate restore of affected VMs, files, and databases at scale.
  name: Ransomware Recovery
- description: SMBs and enterprises run SaaS backup APIs to protect Microsoft 365 mailboxes, SharePoint sites, Google Workspace drives, and Salesforce records against accidental deletion and malicious actors.
  name: SaaS Tenant Protection
- description: Operators use APIs like AWS Backup, Azure Site Recovery, and Veeam to replicate workloads across regions and execute scheduled DR drills with measurable RPO and RTO.
  name: Cross-Region Disaster Recovery
- description: Regulated industries push immutable backup copies to archive tiers (S3 Glacier, Azure Archive, B2) via backup APIs to satisfy retention mandates under HIPAA, SOX, GDPR, and FINRA.
  name: Long-Term Archival and Compliance
- description: Endpoint backup APIs from Druva, Acronis, and Carbonite protect laptops and remote devices and let IT centrally restore files after device loss or compromise.
  name: Endpoint and Remote Worker Backup
- description: Platform engineers script database, VM, and volume snapshots via cloud-native APIs (Amazon DLM, Azure Backup, NetApp) and integrate them into CI/CD and pre-change checkpoints.
  name: Database and VM Snapshot Automation
website: https://apievangelist.com
---
