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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Amazon Efs Agentic Access
  operation_count: 5
  slug: amazon-efs-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: The 2015 02 01 API from Amazon EFS — 3 operation(s) for 2015 02 01.
  name: Amazon EFS 2015 02 01 API
  slug: amazon-efs-2015-02-01-api
arazzos:
- description: Confirm a file system has no mount targets, then delete the file system.
  name: Amazon EFS Decommission File System
  slug: amazon-efs-decommission-file-system-workflow
- description: Look up a file system by creation token and create it only if it does not already exist.
  name: Amazon EFS Find or Create File System
  slug: amazon-efs-find-or-create-file-system-workflow
- description: Describe a file system and enumerate its mount targets to audit its network topology.
  name: Amazon EFS Inspect File System Topology
  slug: amazon-efs-inspect-file-system-topology-workflow
- description: Create a file system, wait until available, then attach mount targets in two Availability Zones.
  name: Amazon EFS Multi-AZ Mount Targets
  slug: amazon-efs-multi-az-mount-targets-workflow
- description: Create an EFS file system, wait for it to become available, then attach a mount target.
  name: Amazon EFS Provision File System
  slug: amazon-efs-provision-file-system-workflow
- description: Verify a file system is available, create a mount target, then poll until the mount target is available.
  name: Amazon EFS Provision Mount Target
  slug: amazon-efs-provision-mount-target-workflow
artifact_total: 45
collections:
- collection_type: postman
  name: Amazon EFS Amazon Elastic File System (EFS) API
  slug: postman-amazon-efs
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon EFS Amazon Elastic File System (EFS) 2015 02 01 API
  slug: open-amazon-efs-2015-02-01-api
- collection_type: open
  name: Amazon EFS Amazon Elastic File System (EFS) API
  slug: open-amazon-efs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-efs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-efs-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-efs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-efs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-efs-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-efs/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-efs-decommission-file-system-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-efs-find-or-create-file-system-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-efs-inspect-file-system-topology-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-efs-multi-az-mount-targets-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-efs-provision-file-system-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-efs-provision-mount-target-workflow.yml
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
  url: rules/amazon-efs-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-efs-vocabulary.yaml
created: '2024-01-15'
description: Amazon Elastic File System (EFS) provides a simple, serverless, set-and-forget elastic file system for use with AWS cloud services and on-premises resources. EFS is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files.
examples:
- key_count: 3
  name: Amazon Efs Filesystem Example
  slug: amazon-efs-filesystem-example
- key_count: 3
  name: Efs Openapi Describe File Systems Response Example
  slug: efs-openapi-describe-file-systems-response-example
- key_count: 3
  name: Efs Openapi File System Example
  slug: efs-openapi-file-system-example
- key_count: 3
  name: Efs Openapi Mount Target Example
  slug: efs-openapi-mount-target-example
features:
- description: Automatically grows and shrinks as you add and remove files with no provisioning required.
  name: Elastic Scalability
- description: Standard, Infrequent Access, and Archive storage classes with automatic lifecycle management.
  name: Multiple Storage Classes
- description: Data automatically replicated across multiple Availability Zones for 99.999999999% durability.
  name: Multi-AZ Replication
- description: Thousands of EC2 instances and Lambda functions can access the same file system simultaneously.
  name: Concurrent Access
- description: Application-specific entry points with customized directory access and POSIX permissions.
  name: EFS Access Points
- description: Centralized backup management for EFS file systems with policy-based retention.
  name: AWS Backup Integration
finops:
- name: Amazon Efs Finops
  service_category: API
  slug: amazon-efs-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon EFS FileSystem
  property_count: 17
  slug: amazon-efs-filesystem
- name: DescribeFileSystemsResponse
  property_count: 3
  slug: efs-openapi-describe-file-systems-response
- name: FileSystem
  property_count: 15
  slug: efs-openapi-file-system
- name: MountTarget
  property_count: 9
  slug: efs-openapi-mount-target
json_structures:
- name: Amazon Efs Filesystem Structure
  property_count: 17
  slug: amazon-efs-filesystem-structure
- name: Efs Openapi Describe File Systems Response Structure
  property_count: 3
  slug: efs-openapi-describe-file-systems-response-structure
- name: Efs Openapi File System Structure
  property_count: 15
  slug: efs-openapi-file-system-structure
- name: Efs Openapi Mount Target Structure
  property_count: 9
  slug: efs-openapi-mount-target-structure
jsonld:
- class_count: 4
  name: Amazon Efs Context
  property_count: 30
  slug: amazon-efs-context
layout: provider
modified: '2026-05-19'
name: Amazon EFS
nav: Providers
network: true
overview: 'Amazon EFS publishes 1 API on the [APIs.io](https://apis.io/) network: 2015 02 01 API. Tagged areas include Amazon Web Services, EFS, Elastic File System, File Storage, and NFS.


  The Amazon EFS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon EFS''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 25 more developer resources.'
plans:
- name: Amazon Efs Plans Pricing
  plan_count: 3
  slug: amazon-efs-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Amazon Efs Rate Limits
  slug: amazon-efs-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon EFS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-efs-jsonschema-spectral-rules
- effective_rule_count: 75
  extends:
  - spectral:oas
  name: Amazon EFS API Rules
  rule_count: 34
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 19
  slug: amazon-efs-spectral-rules
score:
  band: strong
  composite: 58.8
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
    contract_quality: 66.7
    developer_ergonomics: 69.0
    discoverability: 61.1
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 58.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-efs/refs/heads/main/screenshots/amazon-efs-2026-06-20T171636.png
security:
- kind: authentication
  name: Amazon Efs Authentication
  slug: amazon-efs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Efs Domain Security
  slug: amazon-efs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Efs Vulnerability Disclosure
  slug: amazon-efs-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Efs Trust Center
  slug: amazon-efs-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-efs
tags:
- Amazon Web Services
- EFS
- Elastic File System
- File Storage
- NFS
- Serverless
- Storage
use_cases:
- description: Persistent shared storage for containerized applications running on ECS or EKS.
  name: Containerized Application Storage
- description: Shared training data storage accessible simultaneously by multiple compute instances.
  name: Machine Learning
- description: Shared file storage for web servers and CMS platforms requiring concurrent file access.
  name: Content Management
- description: Centralized code and configuration storage accessible by development teams and CI/CD pipelines.
  name: DevOps and Code Sharing
- description: High-throughput shared storage for analytics workloads requiring parallel data access.
  name: Big Data Analytics
website: https://aws.amazon.com/
---
