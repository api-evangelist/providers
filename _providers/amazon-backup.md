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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 22.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Amazon Backup Agentic Access
  operation_count: 7
  slug: amazon-backup-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 1
apis:
- baseURL: https://backup.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for starting and monitoring backup jobs
  name: Amazon Backup Backup Jobs API
  slug: amazon-backup-backup-jobs-api
- baseURL: https://backup.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for creating and managing backup plans
  name: Amazon Backup Backup Plans API
  slug: amazon-backup-backup-plans-api
- baseURL: https://backup.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for creating and managing backup vaults
  name: Amazon Backup Backup Vaults API
  slug: amazon-backup-backup-vaults-api
- baseURL: https://backup.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for restoring backed-up resources
  name: Amazon Backup Restore Jobs API
  slug: amazon-backup-restore-jobs-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Backup Backup Jobs API
  slug: open-amazon-backup-backup-jobs-api
- collection_type: open
  name: Amazon Backup Backup Jobs Backup Plans API
  slug: open-amazon-backup-backup-plans-api
- collection_type: open
  name: Amazon Backup Backup Jobs Backup Vaults API
  slug: open-amazon-backup-backup-vaults-api
- collection_type: open
  name: Amazon Backup Backup Jobs Restore Jobs API
  slug: open-amazon-backup-restore-jobs-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/amazon-backup-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-backup-openapi-overlay.yaml
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


  Amazon Backup''s developer surface includes developer portal, documentation, support, engineering blog, developer console, signup flow, status page, and 19 more developer resources.'
random_paper: 19
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Backup API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-backup-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 56.3
    catalog_earned_first_party: 0.0
    catalog_gap: 58.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 29.5
    contract_quality: 60.4
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 29.5
    operational_transparency: 13.2
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
