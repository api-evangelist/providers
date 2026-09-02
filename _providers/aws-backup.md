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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Aws Backup Agentic Access
  operation_count: 28
  slug: aws-backup-agentic-access
  summary_line: 28 operations · 14 acting · 1 human-in-the-loop
api_count: 1
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
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS Backup Backup Jobs API
  slug: open-aws-backup-backup-jobs-api
- collection_type: open
  name: AWS Backup Backup Jobs Backup Plans API
  slug: open-aws-backup-backup-plans-api
- collection_type: open
  name: AWS Backup Backup Jobs Backup Selections API
  slug: open-aws-backup-backup-selections-api
- collection_type: open
  name: AWS Backup Backup Jobs Backup Vaults API
  slug: open-aws-backup-backup-vaults-api
- collection_type: open
  name: AWS Backup Backup Jobs Copy Jobs API
  slug: open-aws-backup-copy-jobs-api
- collection_type: open
  name: AWS Backup Backup Jobs Frameworks API
  slug: open-aws-backup-frameworks-api
- collection_type: open
  name: AWS Backup Backup Jobs Recovery Points API
  slug: open-aws-backup-recovery-points-api
- collection_type: open
  name: AWS Backup Backup Jobs Report Plans API
  slug: open-aws-backup-report-plans-api
- collection_type: open
  name: AWS Backup Backup Jobs Restore Jobs API
  slug: open-aws-backup-restore-jobs-api
- collection_type: open
  name: AWS Backup Backup Jobs Tags API
  slug: open-aws-backup-tags-api
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
random_paper: 19
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
