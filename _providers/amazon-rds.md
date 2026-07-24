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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amazon Rds Agentic Access
  operation_count: 12
  slug: amazon-rds-agentic-access
  summary_line: 12 operations
api_count: 4
apis:
- description: Operations for creating and managing Aurora database clusters
  name: Amazon RDS DB Clusters API
  slug: amazon-rds-db-clusters-api
- description: Operations for describing available database engine versions
  name: Amazon RDS DB Engine Versions API
  slug: amazon-rds-db-engine-versions-api
- description: Operations for creating, managing, and deleting RDS database instances
  name: Amazon RDS DB Instances API
  slug: amazon-rds-db-instances-api
- description: Operations for creating and managing database snapshots
  name: Amazon RDS DB Snapshots API
  slug: amazon-rds-db-snapshots-api
arazzos:
- description: Confirm a cluster is available, add a reader instance, and poll until it joins.
  name: Amazon RDS Add an Aurora Replica Instance
  slug: amazon-rds-add-aurora-replica-instance-workflow
- description: Confirm a manual snapshot is available, delete it, then verify removal.
  name: Amazon RDS Clean Up a DB Snapshot
  slug: amazon-rds-clean-up-snapshot-workflow
- description: Snapshot a source instance, wait for it, then build a fresh matching instance.
  name: Amazon RDS Snapshot and Rebuild a DB Instance
  slug: amazon-rds-clone-instance-from-snapshot-restore-workflow
- description: Enable Multi-AZ on a DB instance immediately and poll until stable.
  name: Amazon RDS Convert Instance to Multi-AZ
  slug: amazon-rds-convert-to-multi-az-workflow
- description: Snapshot member instances, delete them, then delete the Aurora cluster.
  name: Amazon RDS Delete an Aurora DB Cluster
  slug: amazon-rds-delete-aurora-cluster-workflow
- description: Set an instance backup retention period immediately and poll until stable.
  name: Amazon RDS Enable Backup Retention
  slug: amazon-rds-enable-backup-retention-workflow
- description: Resize a DB instance class immediately and poll until it stabilizes.
  name: Amazon RDS Modify a DB Instance Class
  slug: amazon-rds-modify-instance-class-workflow
- description: Create an Aurora DB cluster and poll until it reports the available status.
  name: Amazon RDS Provision an Aurora DB Cluster
  slug: amazon-rds-provision-aurora-cluster-workflow
- description: Create a DB instance and poll until it reports the available status.
  name: Amazon RDS Provision a DB Instance
  slug: amazon-rds-provision-db-instance-workflow
- description: Reboot a DB instance with optional failover and poll until it recovers.
  name: Amazon RDS Reboot a DB Instance
  slug: amazon-rds-reboot-instance-workflow
- description: Reset the master user password immediately and poll until the instance stabilizes.
  name: Amazon RDS Rotate Master Password
  slug: amazon-rds-rotate-master-password-workflow
- description: Increase allocated storage immediately and poll until the instance stabilizes.
  name: Amazon RDS Scale DB Instance Storage
  slug: amazon-rds-scale-instance-storage-workflow
- description: Create a manual DB snapshot and poll until it reports the available status.
  name: Amazon RDS Snapshot a DB Instance
  slug: amazon-rds-snapshot-db-instance-workflow
- description: Take a final manual snapshot, wait for it, then safely delete the instance.
  name: Amazon RDS Snapshot Then Delete a DB Instance
  slug: amazon-rds-snapshot-then-delete-instance-workflow
- description: Resolve a target engine version, upgrade the instance, and poll until stable.
  name: Amazon RDS Upgrade DB Engine Version
  slug: amazon-rds-upgrade-engine-version-workflow
- description: Validate the engine version is offered, then provision an instance and wait.
  name: Amazon RDS Verify Engine Support Then Provision
  slug: amazon-rds-verify-engine-then-provision-workflow
artifact_total: 70
collections:
- collection_type: postman
  name: Amazon RDS API
  slug: postman-amazon-rds
- collection_type: open
  name: Amazon RDS API
  slug: open-amazon-rds
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-rds-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-rds-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-rds-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-rds-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-rds-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-rds/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rds-add-aurora-replica-instance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rds-clean-up-snapshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rds-clone-instance-from-snapshot-restore-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rds-convert-to-multi-az-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rds-delete-aurora-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rds-enable-backup-retention-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rds-modify-instance-class-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rds-provision-aurora-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rds-provision-db-instance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rds-reboot-instance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rds-rotate-master-password-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rds-scale-instance-storage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rds-snapshot-db-instance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rds-snapshot-then-delete-instance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rds-upgrade-engine-version-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rds-verify-engine-then-provision-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/rds/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/rds/
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
  url: https://aws.amazon.com/blogs/database/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Portal
  url: https://console.aws.amazon.com/rds/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: Knowledge Center
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-rds
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.html
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-rds-context-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rds-openapi-create-db-cluster-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rds-openapi-create-db-instance-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rds-openapi-create-db-snapshot-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rds-openapi-db-cluster-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rds-openapi-db-instance-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rds-openapi-db-snapshot-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rds-openapi-describe-db-clusters-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rds-openapi-describe-db-instances-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rds-openapi-describe-db-snapshots-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rds-openapi-modify-db-instance-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rds-openapi-tag-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rds-instance-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rds-openapi-create-db-cluster-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rds-openapi-create-db-instance-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rds-openapi-create-db-snapshot-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rds-openapi-db-cluster-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rds-openapi-db-instance-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rds-openapi-db-snapshot-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rds-openapi-describe-db-clusters-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rds-openapi-describe-db-instances-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rds-openapi-describe-db-snapshots-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rds-openapi-modify-db-instance-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rds-openapi-tag-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rds-instance-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rds-openapi-create-db-cluster-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rds-openapi-create-db-instance-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rds-openapi-create-db-snapshot-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rds-openapi-db-cluster-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rds-openapi-db-instance-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rds-openapi-db-snapshot-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rds-openapi-describe-db-clusters-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rds-openapi-describe-db-instances-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rds-openapi-describe-db-snapshots-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rds-openapi-modify-db-instance-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rds-openapi-tag-example.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-rds-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-rds-vocabulary.yaml
created: '2024-01-15'
description: Amazon Relational Database Service (RDS) makes it easy to set up, operate, and scale a relational database in the cloud, providing cost-efficient and resizable capacity while automating time-consuming administration tasks such as hardware provisioning, database setup, patching, and backups.
examples:
- key_count: 10
  name: Amazon Rds Instance Example
  slug: amazon-rds-instance-example
- key_count: 1
  name: Amazon Rds Openapi Create Db Cluster Response Example
  slug: amazon-rds-openapi-create-db-cluster-response-example
- key_count: 1
  name: Amazon Rds Openapi Create Db Instance Response Example
  slug: amazon-rds-openapi-create-db-instance-response-example
- key_count: 1
  name: Amazon Rds Openapi Create Db Snapshot Response Example
  slug: amazon-rds-openapi-create-db-snapshot-response-example
- key_count: 10
  name: Amazon Rds Openapi Db Cluster Example
  slug: amazon-rds-openapi-db-cluster-example
- key_count: 10
  name: Amazon Rds Openapi Db Instance Example
  slug: amazon-rds-openapi-db-instance-example
- key_count: 10
  name: Amazon Rds Openapi Db Snapshot Example
  slug: amazon-rds-openapi-db-snapshot-example
- key_count: 2
  name: Amazon Rds Openapi Describe Db Clusters Response Example
  slug: amazon-rds-openapi-describe-db-clusters-response-example
- key_count: 2
  name: Amazon Rds Openapi Describe Db Instances Response Example
  slug: amazon-rds-openapi-describe-db-instances-response-example
- key_count: 2
  name: Amazon Rds Openapi Describe Db Snapshots Response Example
  slug: amazon-rds-openapi-describe-db-snapshots-response-example
- key_count: 1
  name: Amazon Rds Openapi Modify Db Instance Response Example
  slug: amazon-rds-openapi-modify-db-instance-response-example
- key_count: 2
  name: Amazon Rds Openapi Tag Example
  slug: amazon-rds-openapi-tag-example
finops:
- name: Amazon Rds Finops
  service_category: API
  slug: amazon-rds-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon RDS DB Instance
  property_count: 26
  slug: amazon-rds-instance
- name: CreateDBClusterResponse
  property_count: 1
  slug: amazon-rds-openapi-create-db-cluster-response
- name: CreateDBInstanceResponse
  property_count: 1
  slug: amazon-rds-openapi-create-db-instance-response
- name: CreateDBSnapshotResponse
  property_count: 1
  slug: amazon-rds-openapi-create-db-snapshot-response
- name: DBCluster
  property_count: 18
  slug: amazon-rds-openapi-db-cluster
- name: DBInstance
  property_count: 22
  slug: amazon-rds-openapi-db-instance
- name: DBSnapshot
  property_count: 17
  slug: amazon-rds-openapi-db-snapshot
- name: DescribeDBClustersResponse
  property_count: 2
  slug: amazon-rds-openapi-describe-db-clusters-response
- name: DescribeDBInstancesResponse
  property_count: 2
  slug: amazon-rds-openapi-describe-db-instances-response
- name: DescribeDBSnapshotsResponse
  property_count: 2
  slug: amazon-rds-openapi-describe-db-snapshots-response
- name: ModifyDBInstanceResponse
  property_count: 1
  slug: amazon-rds-openapi-modify-db-instance-response
- name: Tag
  property_count: 2
  slug: amazon-rds-openapi-tag
json_structures:
- name: Amazon Rds Instance Structure
  property_count: 26
  slug: amazon-rds-instance-structure
- name: Amazon Rds Openapi Create Db Cluster Response Structure
  property_count: 1
  slug: amazon-rds-openapi-create-db-cluster-response-structure
- name: Amazon Rds Openapi Create Db Instance Response Structure
  property_count: 1
  slug: amazon-rds-openapi-create-db-instance-response-structure
- name: Amazon Rds Openapi Create Db Snapshot Response Structure
  property_count: 1
  slug: amazon-rds-openapi-create-db-snapshot-response-structure
- name: Amazon Rds Openapi Db Cluster Structure
  property_count: 18
  slug: amazon-rds-openapi-db-cluster-structure
- name: Amazon Rds Openapi Db Instance Structure
  property_count: 22
  slug: amazon-rds-openapi-db-instance-structure
- name: Amazon Rds Openapi Db Snapshot Structure
  property_count: 17
  slug: amazon-rds-openapi-db-snapshot-structure
- name: Amazon Rds Openapi Describe Db Clusters Response Structure
  property_count: 2
  slug: amazon-rds-openapi-describe-db-clusters-response-structure
- name: Amazon Rds Openapi Describe Db Instances Response Structure
  property_count: 2
  slug: amazon-rds-openapi-describe-db-instances-response-structure
- name: Amazon Rds Openapi Describe Db Snapshots Response Structure
  property_count: 2
  slug: amazon-rds-openapi-describe-db-snapshots-response-structure
- name: Amazon Rds Openapi Modify Db Instance Response Structure
  property_count: 1
  slug: amazon-rds-openapi-modify-db-instance-response-structure
- name: Amazon Rds Openapi Tag Structure
  property_count: 2
  slug: amazon-rds-openapi-tag-structure
jsonld:
- class_count: 12
  name: Amazon Rds Context
  property_count: 48
  slug: amazon-rds-context-context
- class_count: 0
  name: Amazon Rds Context
  property_count: 3
  slug: amazon-rds-context
layout: provider
modified: '2026-05-19'
name: Amazon RDS
nav: Providers
network: true
overview: 'Amazon RDS publishes 4 APIs on the [APIs.io](https://apis.io/) network, including DB Clusters API, DB Engine Versions API, DB Instances API, and 1 more. Tagged areas include Cloud Databases, Database Service, DBaaS, Managed Databases, and Relational Databases.


  The Amazon RDS catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon RDS''s developer surface includes authentication, developer portal, documentation, support, engineering blog, signup flow, YouTube channel, and 71 more developer resources.'
plans:
- name: Amazon Rds Plans Pricing
  plan_count: 3
  slug: amazon-rds-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Amazon Rds Rate Limits
  slug: amazon-rds-rate-limits
rules:
- name: Amazon RDS API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: amazon-rds-jsonschema-spectral-rules
- name: Amazon RDS API Rules
  rule_count: 27
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 17
  slug: amazon-rds-spectral-rules
score:
  band: strong
  composite: 68.6
  delta: 0.0
  facets:
    commercial_clarity: 89.5
    contract_quality: 69.9
    developer_ergonomics: 39.1
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 63.2
  previous_composite: 68.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-rds/refs/heads/main/screenshots/amazon-rds-2026-06-20T171805.png
security:
- kind: authentication
  name: Amazon Rds Authentication
  slug: amazon-rds-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Rds Domain Security
  slug: amazon-rds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Rds Vulnerability Disclosure
  slug: amazon-rds-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Rds Trust Center
  slug: amazon-rds-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-rds
tags:
- Cloud Databases
- Database Service
- DBaaS
- Managed Databases
- Relational Databases
website: https://aws.amazon.com/
---
