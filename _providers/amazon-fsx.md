---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Amazon Fsx Agentic Access
  operation_count: 1
  slug: amazon-fsx-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Operations for creating and managing file systems
  name: Amazon FSx File Systems API
  slug: amazon-fsx-file-systems-api
artifact_total: 42
collections:
- collection_type: postman
  name: Amazon FSx File Systems API
  slug: postman-amazon-fsx-file-systems-api
- collection_type: open
  name: Amazon FSx API
  slug: open-amazon-fsx
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-fsx/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-fsx-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-fsx-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-fsx-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-fsx-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/fsx/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/fsx/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/fsx/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/storage/category/storage/amazon-fsx/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/fsx/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-fsx
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-fsx-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-fsx-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-fsx-context.jsonld
created: '2024-01-15'
description: Amazon FSx provides fully managed file systems with the native compatibility and feature sets for workloads that require shared file storage. FSx supports four widely-used file systems including NetApp ONTAP, OpenZFS, Windows File Server, and Lustre, delivering high performance and low latency access to data.
examples:
- key_count: 7
  name: Amazon Fsx Backup Example
  slug: amazon-fsx-backup-example
- key_count: 12
  name: Amazon Fsx File System Example
  slug: amazon-fsx-file-system-example
- key_count: 7
  name: Amazon Fsx Snapshot Example
  slug: amazon-fsx-snapshot-example
- key_count: 9
  name: Amazon Fsx Storage Virtual Machine Example
  slug: amazon-fsx-storage-virtual-machine-example
- key_count: 2
  name: Amazon Fsx Tag Example
  slug: amazon-fsx-tag-example
features:
- description: Choose from Lustre, Windows File Server, NetApp ONTAP, and OpenZFS based on workload requirements.
  name: Multiple File System Types
- description: FSx for Lustre delivers hundreds of GB/s throughput and millions of IOPS for HPC and ML workloads.
  name: High Performance
- description: Fully compatible with each file system protocol — SMB for Windows, NFS for Linux, POSIX for Lustre.
  name: Native Compatibility
- description: Daily automatic backups stored in Amazon S3 with user-initiated backup support for disaster recovery.
  name: Automatic Backups
- description: FSx for Windows File Server and ONTAP support Multi-AZ configurations for high availability.
  name: Multi-AZ Deployment
- description: FSx for Lustre integrates natively with Amazon S3 for transparent data import, export, and auto-release.
  name: Data Repository Integration
- description: All file systems are encrypted at rest using AWS KMS with customer-managed key support.
  name: Encryption at Rest
finops:
- name: Amazon Fsx Finops
  service_category: API
  slug: amazon-fsx-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Backup
  property_count: 10
  slug: amazon-fsx-backup
- name: FileSystem
  property_count: 13
  slug: amazon-fsx-file-system
- name: Amazon FSx File System
  property_count: 11
  slug: amazon-fsx
- name: Snapshot
  property_count: 8
  slug: amazon-fsx-snapshot
- name: StorageVirtualMachine
  property_count: 11
  slug: amazon-fsx-storage-virtual-machine
- name: Tag
  property_count: 2
  slug: amazon-fsx-tag
json_structures:
- name: Amazon Fsx Backup Structure
  property_count: 0
  slug: amazon-fsx-backup-structure
- name: Amazon Fsx File System Structure
  property_count: 0
  slug: amazon-fsx-file-system-structure
- name: Amazon Fsx Snapshot Structure
  property_count: 0
  slug: amazon-fsx-snapshot-structure
- name: Amazon Fsx Storage Virtual Machine Structure
  property_count: 0
  slug: amazon-fsx-storage-virtual-machine-structure
- name: Amazon Fsx Tag Structure
  property_count: 0
  slug: amazon-fsx-tag-structure
jsonld:
- class_count: 0
  name: Amazon Fsx Context
  property_count: 2
  slug: amazon-fsx-context
layout: provider
modified: '2026-05-19'
name: Amazon FSx
nav: Providers
network: true
overview: 'Amazon FSx publishes 1 API on the [APIs.io](https://apis.io/) network: File Systems API. Tagged areas include File Systems, Lustre, NetApp, OpenZFS, and Storage.


  The Amazon FSx catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon FSx''s developer surface includes developer portal, documentation, support, engineering blog, developer console, signup flow, YouTube channel, and 14 more developer resources.'
plans:
- name: Amazon Fsx Plans Pricing
  plan_count: 3
  slug: amazon-fsx-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Amazon Fsx Rate Limits
  slug: amazon-fsx-rate-limits
rules:
- name: Amazon FSx API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-fsx-jsonschema-spectral-rules
- name: Amazon FSx API Rules
  rule_count: 28
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 18
  slug: amazon-fsx-spectral-rules
score:
  band: strong
  composite: 59.6
  delta: -2.6
  facets:
    commercial_clarity: 68.4
    contract_quality: 65.3
    developer_ergonomics: 34.8
    discoverability: 75.9
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 62.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-fsx/refs/heads/main/screenshots/amazon-fsx-2026-06-20T171653.png
security:
- kind: domain-security
  name: Amazon Fsx Domain Security
  slug: amazon-fsx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Fsx Vulnerability Disclosure
  slug: amazon-fsx-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Fsx Trust Center
  slug: amazon-fsx-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-fsx
tags:
- File Systems
- Lustre
- NetApp
- OpenZFS
- Storage
- Windows
use_cases:
- description: Use FSx for Lustre for fast scratch storage in high-performance computing and distributed ML training jobs.
  name: HPC and ML Training
- description: Migrate on-premises Windows file shares to FSx for Windows File Server with Active Directory integration.
  name: Windows Workloads
- description: Use FSx for NetApp ONTAP for enterprise NAS with SnapMirror replication, FlexClone, and multi-protocol access.
  name: Enterprise NAS
- description: Use FSx for OpenZFS for fast NFS shared storage in development, testing, and containerized workflows.
  name: DevOps and CI/CD
- description: Process high-resolution video and media assets using FSx for Lustre with S3 data repository tiering.
  name: Media Processing
- description: Use FSx for Windows File Server or ONTAP as high-performance backup targets for Oracle, SQL Server, and SAP.
  name: Database Backup Storage
website: https://aws.amazon.com/fsx/
---
