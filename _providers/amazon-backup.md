---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Amazon Backup Agentic Access
  operation_count: 7
  slug: amazon-backup-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 4
apis:
- description: Operations for starting and monitoring backup jobs
  name: Amazon Backup Backup Jobs API
  slug: amazon-backup-backup-jobs-api
- description: Operations for creating and managing backup plans
  name: Amazon Backup Backup Plans API
  slug: amazon-backup-backup-plans-api
- description: Operations for creating and managing backup vaults
  name: Amazon Backup Backup Vaults API
  slug: amazon-backup-backup-vaults-api
- description: Operations for restoring backed-up resources
  name: Amazon Backup Restore Jobs API
  slug: amazon-backup-restore-jobs-api
artifact_total: 14
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-backup-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-backup-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-backup-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-backup-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
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
  url: https://aws.amazon.com/blogs/storage/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/backup/
- group: start
  title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: Status
  url: https://health.aws.amazon.com/health/status
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
  url: https://stackoverflow.com/questions/tagged/aws-backup
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://docs.aws.amazon.com/aws-backup/latest/devguide/security.html
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-backup-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-backup-security.txt
created: '2024-01-15'
description: AWS Backup is a fully managed backup service that centralizes and automates the backup of data across AWS services, enabling you to configure backup policies, monitor backup activity, and restore resources with a single, unified console and API. It supports automated backup schedules, lifecycle management, cross-region copy, Vault Lock for WORM compliance, legal holds, compliance frameworks, and automated restore testing.
examples:
- key_count: 2
  name: Create Backup Plan Example
  slug: create-backup-plan-example
- key_count: 2
  name: Start Backup Job Example
  slug: start-backup-job-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-backup.png
json_schemas:
- name: Amazon Backup Plan
  property_count: 7
  slug: amazon-backup-plan
json_structures:
- name: Backup Resource Structure
  property_count: 0
  slug: backup-resource-structure
jsonld:
- class_count: 0
  name: Amazon Backup Context
  property_count: 4
  slug: amazon-backup-context
layout: provider
modified: '2026-06-20'
name: Amazon Backup
nav: Providers
network: true
overview: 'Amazon Backup publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Backup Jobs API, Backup Plans API, Backup Vaults API, and 1 more. Tagged areas include Backup, Data Protection, Disaster Recovery, Storage, and Compliance.


  The Amazon Backup catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Amazon Backup''s developer surface includes developer portal, documentation, support, engineering blog, developer console, signup flow, status page, and 17 more developer resources.'
random_paper: 9
rules:
- name: Amazon Backup API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-backup-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.1
  delta: -0.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 65.3
    developer_ergonomics: 30.4
    discoverability: 92.6
    governance: 69.8
    operational_transparency: 15.8
  previous_composite: 52.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-backup/refs/heads/main/screenshots/amazon-backup-2026-07-25T195935.png
security:
- kind: domain-security
  name: Amazon Backup Domain Security
  slug: amazon-backup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Backup Vulnerability Disclosure
  slug: amazon-backup-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Backup Trust Center
  slug: amazon-backup-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-backup
tags:
- Backup
- Data Protection
- Disaster Recovery
- Storage
- Compliance
- Governance
- Business Continuity
website: https://aws.amazon.com/backup/
---
