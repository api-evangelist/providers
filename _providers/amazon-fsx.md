---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Amazon Fsx Agentic Access
  operation_count: 1
  slug: amazon-fsx-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://fsx.amazonaws.com
  baseurl_source: declared
  description: Operations for creating and managing file systems
  name: Amazon FSx Filesystems API
  slug: amazon-fsx-filesystems-api
- baseURL: https://fsx.amazonaws.com
  baseurl_source: declared
  description: The Fsx Backup API from Amazon FSx — 3 operation(s) for fsx backup.
  name: Amazon FSx Fsx Backup API
  slug: amazon-fsx-backup-api
- baseURL: https://fsx.amazonaws.com
  baseurl_source: declared
  description: The Fsx Data Repository Association API from Amazon FSx — 4 operation(s) for fsx data repository association.
  name: Amazon FSx Fsx Data Repository Association API
  slug: amazon-fsx-data-repository-association-api
- baseURL: https://fsx.amazonaws.com
  baseurl_source: declared
  description: The Fsx Data Repository Task API from Amazon FSx — 3 operation(s) for fsx data repository task.
  name: Amazon FSx Fsx Data Repository Task API
  slug: amazon-fsx-data-repository-task-api
- baseURL: https://fsx.amazonaws.com
  baseurl_source: declared
  description: The Fsx File Cache API from Amazon FSx — 4 operation(s) for fsx file cache.
  name: Amazon FSx Fsx File Cache API
  slug: amazon-fsx-file-cache-api
- baseURL: https://fsx.amazonaws.com
  baseurl_source: declared
  description: The Fsx File System Aliase API from Amazon FSx — 3 operation(s) for fsx file system aliase.
  name: Amazon FSx Fsx File System Aliase API
  slug: amazon-fsx-file-system-aliase-api
- baseURL: https://fsx.amazonaws.com
  baseurl_source: declared
  description: The Fsx Operations API from Amazon FSx — 12 operation(s) for fsx operations.
  name: Amazon FSx Fsx Operations API
  slug: amazon-fsx-operations-api
- baseURL: https://fsx.amazonaws.com
  baseurl_source: declared
  description: The Fsx Snapshot API from Amazon FSx — 4 operation(s) for fsx snapshot.
  name: Amazon FSx Fsx Snapshot API
  slug: amazon-fsx-snapshot-api
- baseURL: https://fsx.amazonaws.com
  baseurl_source: declared
  description: The Fsx Storage Virtual Machine API from Amazon FSx — 4 operation(s) for fsx storage virtual machine.
  name: Amazon FSx Fsx Storage Virtual Machine API
  slug: amazon-fsx-storage-virtual-machine-api
- baseURL: https://fsx.amazonaws.com
  baseurl_source: declared
  description: The Fsx Volume API from Amazon FSx — 6 operation(s) for fsx volume.
  name: Amazon FSx Fsx Volume API
  slug: amazon-fsx-volume-api
artifact_total: 52
collections:
- collection_type: postman
  name: Amazon FSx File Systems API
  slug: postman-amazon-fsx-file-systems-api
- collection_type: open
  name: Amazon FSx File Systems API
  slug: open-amazon-fsx-file-systems-api
- collection_type: open
  name: Amazon FSx API
  slug: open-amazon-fsx
common:
- group: commercial
  href: https://artifacts.apis.io/amazon-fsx/plans/amazon-fsx-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-fsx-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/amazon-fsx/rate-limits/amazon-fsx-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-fsx-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-fsx/finops/amazon-fsx-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-fsx-finops.yml
- group: other
  href: https://artifacts.apis.io/amazon-fsx/capabilities/amazon-fsx-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-fsx-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-fsx/overview
- group: agent
  href: https://artifacts.apis.io/amazon-fsx/agentic-access/amazon-fsx-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-fsx-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-fsx/security/amazon-fsx-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-fsx-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-fsx/security/amazon-fsx-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-fsx-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-fsx/security/amazon-fsx-domain-security.yml
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
  href: https://artifacts.apis.io/amazon-fsx/rules/amazon-fsx-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-fsx-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/amazon-fsx/vocabulary/amazon-fsx-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-fsx-vocabulary.yaml
- group: design
  href: https://artifacts.apis.io/amazon-fsx/json-ld/amazon-fsx-context.jsonld
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
- has_sources: true
  method: derived
  name: Amazon Fsx Finops
  primary_unit: ''
  service_category: ''
  slug: amazon-fsx-finops
  template: true
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
overview: 'Amazon FSx publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Filesystems API, Fsx Backup API, Fsx Data Repository Association API, and 7 more. Tagged areas include Amazon Web Services, Filesystem, Lustre, NetApp, and OpenZFS.


  The Amazon FSx catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon FSx''s developer surface includes developer portal, documentation, support, engineering blog, developer console, signup flow, YouTube channel, and 18 more developer resources.'
plans:
- name: Amazon Fsx Plans Pricing
  plan_count: 0
  slug: amazon-fsx-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Amazon Fsx Rate Limits
  slug: amazon-fsx-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Amazon FSx — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-fsx-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 69
  extends:
  - spectral:oas
  name: Amazon FSx API Rules
  rule_count: 28
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 18
  slug: amazon-fsx-spectral-rules
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 63.0
    catalog_earned_first_party: 0.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 52.6
    contract_governance: 27.3
    contract_quality: 71.0
    developer_ergonomics: 41.7
    discoverability: 73.2
    operational_transparency: 36.8
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 90.0
      total: 10
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
    score: 0.0
screenshot: https://apis.io/screenshots/amazon-fsx/amazon-fsx-2026-06-20T171653.png
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
- Amazon Web Services
- Filesystem
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
