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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Amazon Ebs Agentic Access
  operation_count: 7
  slug: amazon-ebs-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 1
apis:
- description: The Amazon EBS Amazon Elastic Block Store (EBS) API API from Amazon EBS — 1 operation(s) for amazon ebs amazon elastic block store (ebs) api.
  name: Amazon EBS Amazon EBS Amazon Elastic Block Store (EBS) API API
  slug: amazon-ebs-amazon-ebs-amazon-elastic-block-store-ebs-api-api
- description: 'The #AttachVolume API from Amazon EBS — 1 operation(s) for #attachvolume.'
  name: 'Amazon EBS #AttachVolume API'
  slug: amazon-ebs-attachvolume-api
- description: 'The #CreateSnapshot API from Amazon EBS — 1 operation(s) for #createsnapshot.'
  name: 'Amazon EBS #CreateSnapshot API'
  slug: amazon-ebs-createsnapshot-api
- description: 'The #DeleteVolume API from Amazon EBS — 1 operation(s) for #deletevolume.'
  name: 'Amazon EBS #DeleteVolume API'
  slug: amazon-ebs-deletevolume-api
- description: 'The #DescribeSnapshots API from Amazon EBS — 1 operation(s) for #describesnapshots.'
  name: 'Amazon EBS #DescribeSnapshots API'
  slug: amazon-ebs-describesnapshots-api
- description: 'The #DetachVolume API from Amazon EBS — 1 operation(s) for #detachvolume.'
  name: 'Amazon EBS #DetachVolume API'
  slug: amazon-ebs-detachvolume-api
arazzos:
- description: Snapshot a source volume, confirm it, then create a clone volume from it.
  name: Amazon EBS Clone Volume via Snapshot
  slug: amazon-ebs-clone-volume-via-snapshot-workflow
- description: Detach an EBS volume from its instance, confirm it, then delete it.
  name: Amazon EBS Detach and Delete Volume
  slug: amazon-ebs-detach-and-delete-volume-workflow
- description: Page through EBS volumes and snapshots to build a storage inventory.
  name: Amazon EBS Inventory Volumes and Snapshots
  slug: amazon-ebs-inventory-volumes-and-snapshots-workflow
- description: Create an EBS volume, confirm it is available, then attach it to an instance.
  name: Amazon EBS Provision and Attach Volume
  slug: amazon-ebs-provision-and-attach-volume-workflow
- description: Locate a snapshot, create a volume from it, and attach the volume.
  name: Amazon EBS Restore Volume from Snapshot
  slug: amazon-ebs-restore-volume-from-snapshot-workflow
- description: Take a snapshot of an EBS volume and confirm the snapshot is visible.
  name: Amazon EBS Snapshot and Verify Volume
  slug: amazon-ebs-snapshot-and-verify-volume-workflow
artifact_total: 52
collections:
- collection_type: postman
  name: Amazon EBS Amazon Elastic Block Store (EBS) API
  slug: postman-amazon-ebs
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon EBS Amazon Elastic Block Store (EBS) Amazon EBS Amazon Elastic Block Store (EBS) API API
  slug: open-amazon-ebs-amazon-ebs-amazon-elastic-block-store-ebs-api-api
- collection_type: open
  name: 'Amazon EBS Amazon Elastic Block Store (EBS) Amazon EBS Amazon Elastic Block Store (EBS) API #AttachVolume API'
  slug: open-amazon-ebs-attachvolume-api
- collection_type: open
  name: 'Amazon EBS Amazon Elastic Block Store (EBS) Amazon EBS Amazon Elastic Block Store (EBS) API #CreateSnapshot API'
  slug: open-amazon-ebs-createsnapshot-api
- collection_type: open
  name: 'Amazon EBS Amazon Elastic Block Store (EBS) Amazon EBS Amazon Elastic Block Store (EBS) API #DeleteVolume API'
  slug: open-amazon-ebs-deletevolume-api
- collection_type: open
  name: 'Amazon EBS Amazon Elastic Block Store (EBS) Amazon EBS Amazon Elastic Block Store (EBS) API #DescribeSnapshots API'
  slug: open-amazon-ebs-describesnapshots-api
- collection_type: open
  name: 'Amazon EBS Amazon Elastic Block Store (EBS) Amazon EBS Amazon Elastic Block Store (EBS) API #DetachVolume API'
  slug: open-amazon-ebs-detachvolume-api
- collection_type: open
  name: Amazon EBS Amazon Elastic Block Store (EBS) API
  slug: open-amazon-ebs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-ebs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-ebs-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-ebs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-ebs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-ebs-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-ebs/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ebs-clone-volume-via-snapshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ebs-detach-and-delete-volume-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ebs-inventory-volumes-and-snapshots-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ebs-provision-and-attach-volume-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ebs-restore-volume-from-snapshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ebs-snapshot-and-verify-volume-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/
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
  url: https://aws.amazon.com/support/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-web-services
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-ebs-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-ebs-vocabulary.yaml
created: '2024-01-15'
description: Amazon Elastic Block Store (EBS) provides persistent block storage volumes for use with Amazon EC2 instances. EBS volumes are highly available and reliable storage volumes that can be attached to any running instance in the same Availability Zone, offering consistent and low-latency performance for workloads that require persistent storage.
examples:
- key_count: 3
  name: Amazon Ebs Volume Example
  slug: amazon-ebs-volume-example
- key_count: 2
  name: Ebs Openapi Describe Volumes Result Example
  slug: ebs-openapi-describe-volumes-result-example
- key_count: 3
  name: Ebs Openapi Volume Example
  slug: ebs-openapi-volume-example
features:
- description: Choose from gp3, gp2, io2, io1, st1, sc1, and io2 Block Express volumes optimized for different workloads.
  name: Multiple Volume Types
- description: Point-in-time backups stored in Amazon S3 for disaster recovery, migration, and data sharing.
  name: EBS Snapshots
- description: AES-256 encryption at rest and in transit using AWS KMS customer-managed or AWS-managed keys.
  name: Encryption
- description: Dynamically modify volume size, performance, and type without detaching from instances.
  name: Elastic Volumes
- description: Automate snapshot creation, retention, deletion, and cross-account sharing with policy-based management.
  name: Data Lifecycle Manager
- description: Attach a single io2 volume to up to 16 EC2 instances simultaneously for high availability.
  name: Multi-Attach
finops:
- name: Amazon Ebs Finops
  service_category: API
  slug: amazon-ebs-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon EBS Volume
  property_count: 14
  slug: amazon-ebs-volume
- name: DescribeVolumesResult
  property_count: 2
  slug: ebs-openapi-describe-volumes-result
- name: Volume
  property_count: 13
  slug: ebs-openapi-volume
json_structures:
- name: Amazon Ebs Volume Structure
  property_count: 14
  slug: amazon-ebs-volume-structure
- name: Ebs Openapi Describe Volumes Result Structure
  property_count: 2
  slug: ebs-openapi-describe-volumes-result-structure
- name: Ebs Openapi Volume Structure
  property_count: 13
  slug: ebs-openapi-volume-structure
jsonld:
- class_count: 3
  name: Amazon Ebs Context
  property_count: 24
  slug: amazon-ebs-context
layout: provider
modified: '2026-05-19'
name: Amazon EBS
nav: Providers
network: true
overview: 'Amazon EBS publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Amazon EBS Amazon Elastic Block Store (EBS) API API, #AttachVolume API, #CreateSnapshot API, and 3 more. Tagged areas include Amazon Web Services, Block Storage, EBS, EC2, and Snapshots.


  The Amazon EBS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon EBS''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 25 more developer resources.'
plans:
- name: Amazon Ebs Plans Pricing
  plan_count: 3
  slug: amazon-ebs-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Amazon Ebs Rate Limits
  slug: amazon-ebs-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon EBS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-ebs-jsonschema-spectral-rules
- effective_rule_count: 74
  extends:
  - spectral:oas
  name: Amazon EBS API Rules
  rule_count: 33
  severity_counts:
    error: 11
    hint: 0
    info: 5
    warn: 17
  slug: amazon-ebs-spectral-rules
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 28.8
    contract_quality: 70.1
    developer_ergonomics: 69.0
    discoverability: 61.1
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-ebs/refs/heads/main/screenshots/amazon-ebs-2026-06-20T171636.png
security:
- kind: authentication
  name: Amazon Ebs Authentication
  slug: amazon-ebs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Ebs Domain Security
  slug: amazon-ebs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Ebs Vulnerability Disclosure
  slug: amazon-ebs-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Ebs Trust Center
  slug: amazon-ebs-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-ebs
tags:
- Amazon Web Services
- Block Storage
- EBS
- EC2
- Snapshots
- Storage
- Volumes
use_cases:
- description: High-performance persistent storage for MySQL, PostgreSQL, Oracle, and SQL Server databases.
  name: Relational Databases
- description: Low-latency block storage for MongoDB, Cassandra, and other NoSQL workloads.
  name: NoSQL Databases
- description: SAN workload migration for I/O-intensive SAP, Oracle, and other enterprise applications.
  name: Enterprise Applications
- description: Resizable storage for Hadoop, Spark, and other big data cluster deployments.
  name: Big Data Analytics
- description: OS and application boot volumes for all EC2 instance types.
  name: Boot Volumes
website: https://aws.amazon.com/
---
