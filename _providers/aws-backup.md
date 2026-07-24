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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Aws Backup Agentic Access
  operation_count: 28
  slug: aws-backup-agentic-access
  summary_line: 28 operations · 14 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: REST API for centrally configuring and managing AWS Backup including backup plans, backup selections, backup vaults, recovery points, restore jobs, framework reports, audit reports, and the AWS Backup
  name: AWS Backup API
  slug: api
- description: The Backup Jobs API from AWS Backup — 2 operation(s) for backup jobs.
  name: AWS Backup Backup Jobs API
  slug: aws-backup-backup-jobs-api
- description: The Backup Plans API from AWS Backup — 2 operation(s) for backup plans.
  name: AWS Backup Backup Plans API
  slug: aws-backup-backup-plans-api
- description: The Backup Selections API from AWS Backup — 1 operation(s) for backup selections.
  name: AWS Backup Backup Selections API
  slug: aws-backup-backup-selections-api
- description: The Backup Vaults API from AWS Backup — 2 operation(s) for backup vaults.
  name: AWS Backup Backup Vaults API
  slug: aws-backup-backup-vaults-api
- description: The Copy Jobs API from AWS Backup — 1 operation(s) for copy jobs.
  name: AWS Backup Copy Jobs API
  slug: aws-backup-copy-jobs-api
- description: The Frameworks API from AWS Backup — 1 operation(s) for frameworks.
  name: AWS Backup Frameworks API
  slug: aws-backup-frameworks-api
- description: The Recovery Points API from AWS Backup — 2 operation(s) for recovery points.
  name: AWS Backup Recovery Points API
  slug: aws-backup-recovery-points-api
- description: The Report Plans API from AWS Backup — 1 operation(s) for report plans.
  name: AWS Backup Report Plans API
  slug: aws-backup-report-plans-api
- description: The Restore Jobs API from AWS Backup — 1 operation(s) for restore jobs.
  name: AWS Backup Restore Jobs API
  slug: aws-backup-restore-jobs-api
- description: The Tags API from AWS Backup — 1 operation(s) for tags.
  name: AWS Backup Tags API
  slug: aws-backup-tags-api
artifact_total: 17
collections:
- collection_type: open
  name: AWS Backup API
  slug: open-aws-backup
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-backup-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-backup-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-backup-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-backup-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aws-backup-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/backup/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/aws-backup/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/backup/pricing/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
created: '2026-05-11'
description: AWS Backup is a fully managed, policy-based data protection service that centralizes and automates backup of data across AWS services including EBS volumes, EC2 instances, RDS databases, DynamoDB tables, EFS file systems, FSx file systems, Storage Gateway volumes, S3, and on-premises data via the AWS Backup gateway. The AWS Backup API allows programmatic management of backup plans, vaults, recovery points, restore jobs, and cross-account, cross-Region copies, authenticated with AWS Signature Version 4 (SigV4).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-backup.png
layout: provider
modified: '2026-05-11'
name: AWS Backup
nav: Providers
network: true
overview: 'AWS Backup publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Backup Jobs API, Backup Plans API, Backup Selections API, and 7 more. Tagged areas include Backup, Data Protection, Disaster Recovery, Managed Service, and Compliance.


  AWS Backup''s developer surface includes authentication, documentation, pricing, signup flow, and 5 more developer resources.'
random_paper: 37
score:
  band: emerging
  composite: 27.2
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 51.3
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 27.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-backup/refs/heads/main/screenshots/aws-backup-2026-06-20T172742.png
security:
- kind: authentication
  name: Aws Backup Authentication
  slug: aws-backup-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aws Backup Domain Security
  slug: aws-backup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws Backup Vulnerability Disclosure
  slug: aws-backup-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws Backup Trust Center
  slug: aws-backup-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-backup
tags:
- Backup
- Data Protection
- Disaster Recovery
- Managed Service
- Compliance
website: https://aws.amazon.com/backup/
---
