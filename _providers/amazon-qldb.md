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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Amazon Qldb Agentic Access
  operation_count: 20
  slug: amazon-qldb-agentic-access
  summary_line: 20 operations · 12 acting
api_count: 3
apis:
- description: The Journal S3 Exports API from Amazon QLDB — 1 operation(s) for journal s3 exports.
  name: Amazon QLDB Journal S3 Exports API
  slug: amazon-qldb-journal-s3-exports-api
- description: The Ledgers API from Amazon QLDB — 10 operation(s) for ledgers.
  name: Amazon QLDB Ledgers API
  slug: amazon-qldb-ledgers-api
- description: The Tags API from Amazon QLDB — 2 operation(s) for tags.
  name: Amazon QLDB Tags API
  slug: amazon-qldb-tags-api
artifact_total: 136
collections:
- collection_type: postman
  name: Amazon QLDB Journal S3 Exports API
  slug: postman-amazon-qldb-journal-s3-exports-api
- collection_type: postman
  name: Amazon QLDB Journal S3 Exports Ledgers API
  slug: postman-amazon-qldb-ledgers-api
- collection_type: postman
  name: Amazon QLDB Journal S3 Exports Tags API
  slug: postman-amazon-qldb-tags-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon QLDB Journal S3 Exports API
  slug: open-amazon-qldb-journal-s3-exports-api
- collection_type: open
  name: Amazon QLDB Journal S3 Exports Ledgers API
  slug: open-amazon-qldb-ledgers-api
- collection_type: open
  name: Amazon QLDB Journal S3 Exports Tags API
  slug: open-amazon-qldb-tags-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-qldb/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-qldb-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-qldb-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-qldb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-qldb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-qldb-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/qldb/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/qldb/
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/qldb/
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
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-qldb-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-cancel-journal-kinesis-stream-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-create-ledger-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-create-ledger-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-describe-journal-kinesis-stream-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-describe-journal-s3export-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-describe-ledger-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-encryption-status-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-error-cause-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-export-journal-to-s3request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-export-journal-to-s3response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-export-status-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-get-block-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-get-block-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-get-digest-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-get-revision-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-get-revision-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-journal-kinesis-stream-description-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-journal-s3export-description-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-kinesis-configuration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-ledger-encryption-description-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-ledger-state-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-ledger-summary-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-list-journal-kinesis-streams-for-ledger-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-list-journal-s3exports-for-ledger-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-list-journal-s3exports-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-list-ledgers-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-list-tags-for-resource-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-output-format-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-permissions-mode-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-s3encryption-configuration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-s3export-configuration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-s3object-encryption-type-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-stream-journal-to-kinesis-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-stream-journal-to-kinesis-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-stream-status-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-tag-resource-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-update-ledger-permissions-mode-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-update-ledger-permissions-mode-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-update-ledger-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-update-ledger-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-qldb-value-holder-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-cancel-journal-kinesis-stream-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-create-ledger-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-create-ledger-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-describe-journal-kinesis-stream-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-describe-journal-s3export-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-describe-ledger-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-encryption-status-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-error-cause-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-export-journal-to-s3request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-export-journal-to-s3response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-export-status-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-get-block-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-get-block-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-get-digest-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-get-revision-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-get-revision-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-journal-kinesis-stream-description-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-journal-s3export-description-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-kinesis-configuration-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-ledger-encryption-description-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-ledger-state-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-ledger-summary-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-list-journal-kinesis-streams-for-ledger-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-list-journal-s3exports-for-ledger-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-list-journal-s3exports-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-list-ledgers-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-list-tags-for-resource-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-output-format-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-permissions-mode-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-s3encryption-configuration-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-s3export-configuration-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-s3object-encryption-type-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-stream-journal-to-kinesis-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-stream-journal-to-kinesis-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-stream-status-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-tag-resource-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-update-ledger-permissions-mode-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-update-ledger-permissions-mode-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-update-ledger-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-update-ledger-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-qldb-value-holder-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-cancel-journal-kinesis-stream-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-create-ledger-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-create-ledger-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-describe-journal-kinesis-stream-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-describe-journal-s3export-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-describe-ledger-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-export-journal-to-s3request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-export-journal-to-s3response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-get-block-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-get-block-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-get-digest-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-get-revision-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-get-revision-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-journal-kinesis-stream-description-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-journal-s3export-description-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-kinesis-configuration-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-ledger-encryption-description-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-ledger-summary-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-list-journal-kinesis-streams-for-ledger-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-list-journal-s3exports-for-ledger-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-list-journal-s3exports-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-list-ledgers-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-list-tags-for-resource-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-s3encryption-configuration-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-s3export-configuration-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-stream-journal-to-kinesis-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-stream-journal-to-kinesis-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-tag-resource-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-update-ledger-permissions-mode-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-update-ledger-permissions-mode-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-update-ledger-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-update-ledger-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-qldb-value-holder-example.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-qldb-spectral-rules.yml
created: '2024-01-15'
description: Amazon Quantum Ledger Database (QLDB) is a fully managed ledger database that provides a transparent, immutable, and cryptographically verifiable transaction log. QLDB tracks each and every application data change and maintains a complete and verifiable history of changes over time, making it ideal for systems of record where data integrity and auditability are critical.
examples:
- key_count: 1
  name: Amazon Qldb Cancel Journal Kinesis Stream Response Example
  slug: amazon-qldb-cancel-journal-kinesis-stream-response-example
- key_count: 5
  name: Amazon Qldb Create Ledger Request Example
  slug: amazon-qldb-create-ledger-request-example
- key_count: 7
  name: Amazon Qldb Create Ledger Response Example
  slug: amazon-qldb-create-ledger-response-example
- key_count: 1
  name: Amazon Qldb Describe Journal Kinesis Stream Response Example
  slug: amazon-qldb-describe-journal-kinesis-stream-response-example
- key_count: 1
  name: Amazon Qldb Describe Journal S3Export Response Example
  slug: amazon-qldb-describe-journal-s3export-response-example
- key_count: 7
  name: Amazon Qldb Describe Ledger Response Example
  slug: amazon-qldb-describe-ledger-response-example
- key_count: 5
  name: Amazon Qldb Export Journal To S3Request Example
  slug: amazon-qldb-export-journal-to-s3request-example
- key_count: 1
  name: Amazon Qldb Export Journal To S3Response Example
  slug: amazon-qldb-export-journal-to-s3response-example
- key_count: 2
  name: Amazon Qldb Get Block Request Example
  slug: amazon-qldb-get-block-request-example
- key_count: 2
  name: Amazon Qldb Get Block Response Example
  slug: amazon-qldb-get-block-response-example
- key_count: 2
  name: Amazon Qldb Get Digest Response Example
  slug: amazon-qldb-get-digest-response-example
- key_count: 3
  name: Amazon Qldb Get Revision Request Example
  slug: amazon-qldb-get-revision-request-example
- key_count: 2
  name: Amazon Qldb Get Revision Response Example
  slug: amazon-qldb-get-revision-response-example
- key_count: 11
  name: Amazon Qldb Journal Kinesis Stream Description Example
  slug: amazon-qldb-journal-kinesis-stream-description-example
- key_count: 9
  name: Amazon Qldb Journal S3Export Description Example
  slug: amazon-qldb-journal-s3export-description-example
- key_count: 2
  name: Amazon Qldb Kinesis Configuration Example
  slug: amazon-qldb-kinesis-configuration-example
- key_count: 3
  name: Amazon Qldb Ledger Encryption Description Example
  slug: amazon-qldb-ledger-encryption-description-example
- key_count: 3
  name: Amazon Qldb Ledger Summary Example
  slug: amazon-qldb-ledger-summary-example
- key_count: 2
  name: Amazon Qldb List Journal Kinesis Streams For Ledger Response Example
  slug: amazon-qldb-list-journal-kinesis-streams-for-ledger-response-example
- key_count: 2
  name: Amazon Qldb List Journal S3Exports For Ledger Response Example
  slug: amazon-qldb-list-journal-s3exports-for-ledger-response-example
- key_count: 2
  name: Amazon Qldb List Journal S3Exports Response Example
  slug: amazon-qldb-list-journal-s3exports-response-example
- key_count: 2
  name: Amazon Qldb List Ledgers Response Example
  slug: amazon-qldb-list-ledgers-response-example
- key_count: 1
  name: Amazon Qldb List Tags For Resource Response Example
  slug: amazon-qldb-list-tags-for-resource-response-example
- key_count: 2
  name: Amazon Qldb S3Encryption Configuration Example
  slug: amazon-qldb-s3encryption-configuration-example
- key_count: 3
  name: Amazon Qldb S3Export Configuration Example
  slug: amazon-qldb-s3export-configuration-example
- key_count: 6
  name: Amazon Qldb Stream Journal To Kinesis Request Example
  slug: amazon-qldb-stream-journal-to-kinesis-request-example
- key_count: 1
  name: Amazon Qldb Stream Journal To Kinesis Response Example
  slug: amazon-qldb-stream-journal-to-kinesis-response-example
- key_count: 1
  name: Amazon Qldb Tag Resource Request Example
  slug: amazon-qldb-tag-resource-request-example
- key_count: 1
  name: Amazon Qldb Update Ledger Permissions Mode Request Example
  slug: amazon-qldb-update-ledger-permissions-mode-request-example
- key_count: 3
  name: Amazon Qldb Update Ledger Permissions Mode Response Example
  slug: amazon-qldb-update-ledger-permissions-mode-response-example
- key_count: 2
  name: Amazon Qldb Update Ledger Request Example
  slug: amazon-qldb-update-ledger-request-example
- key_count: 6
  name: Amazon Qldb Update Ledger Response Example
  slug: amazon-qldb-update-ledger-response-example
- key_count: 1
  name: Amazon Qldb Value Holder Example
  slug: amazon-qldb-value-holder-example
finops:
- name: Amazon Qldb Finops
  service_category: API
  slug: amazon-qldb-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: CancelJournalKinesisStreamResponse
  property_count: 1
  slug: amazon-qldb-cancel-journal-kinesis-stream-response
- name: CreateLedgerRequest
  property_count: 5
  slug: amazon-qldb-create-ledger-request
- name: CreateLedgerResponse
  property_count: 7
  slug: amazon-qldb-create-ledger-response
- name: DescribeJournalKinesisStreamResponse
  property_count: 1
  slug: amazon-qldb-describe-journal-kinesis-stream-response
- name: DescribeJournalS3ExportResponse
  property_count: 1
  slug: amazon-qldb-describe-journal-s3export-response
- name: DescribeLedgerResponse
  property_count: 7
  slug: amazon-qldb-describe-ledger-response
- name: EncryptionStatus
  property_count: 0
  slug: amazon-qldb-encryption-status
- name: ErrorCause
  property_count: 0
  slug: amazon-qldb-error-cause
- name: ExportJournalToS3Request
  property_count: 5
  slug: amazon-qldb-export-journal-to-s3request
- name: ExportJournalToS3Response
  property_count: 1
  slug: amazon-qldb-export-journal-to-s3response
- name: ExportStatus
  property_count: 0
  slug: amazon-qldb-export-status
- name: GetBlockRequest
  property_count: 2
  slug: amazon-qldb-get-block-request
- name: GetBlockResponse
  property_count: 2
  slug: amazon-qldb-get-block-response
- name: GetDigestResponse
  property_count: 2
  slug: amazon-qldb-get-digest-response
- name: GetRevisionRequest
  property_count: 3
  slug: amazon-qldb-get-revision-request
- name: GetRevisionResponse
  property_count: 2
  slug: amazon-qldb-get-revision-response
- name: JournalKinesisStreamDescription
  property_count: 11
  slug: amazon-qldb-journal-kinesis-stream-description
- name: JournalS3ExportDescription
  property_count: 9
  slug: amazon-qldb-journal-s3export-description
- name: KinesisConfiguration
  property_count: 2
  slug: amazon-qldb-kinesis-configuration
- name: LedgerEncryptionDescription
  property_count: 3
  slug: amazon-qldb-ledger-encryption-description
- name: LedgerState
  property_count: 0
  slug: amazon-qldb-ledger-state
- name: LedgerSummary
  property_count: 3
  slug: amazon-qldb-ledger-summary
- name: ListJournalKinesisStreamsForLedgerResponse
  property_count: 2
  slug: amazon-qldb-list-journal-kinesis-streams-for-ledger-response
- name: ListJournalS3ExportsForLedgerResponse
  property_count: 2
  slug: amazon-qldb-list-journal-s3exports-for-ledger-response
- name: ListJournalS3ExportsResponse
  property_count: 2
  slug: amazon-qldb-list-journal-s3exports-response
- name: ListLedgersResponse
  property_count: 2
  slug: amazon-qldb-list-ledgers-response
- name: ListTagsForResourceResponse
  property_count: 1
  slug: amazon-qldb-list-tags-for-resource-response
- name: OutputFormat
  property_count: 0
  slug: amazon-qldb-output-format
- name: PermissionsMode
  property_count: 0
  slug: amazon-qldb-permissions-mode
- name: S3EncryptionConfiguration
  property_count: 2
  slug: amazon-qldb-s3encryption-configuration
- name: S3ExportConfiguration
  property_count: 3
  slug: amazon-qldb-s3export-configuration
- name: S3ObjectEncryptionType
  property_count: 0
  slug: amazon-qldb-s3object-encryption-type
- name: StreamJournalToKinesisRequest
  property_count: 6
  slug: amazon-qldb-stream-journal-to-kinesis-request
- name: StreamJournalToKinesisResponse
  property_count: 1
  slug: amazon-qldb-stream-journal-to-kinesis-response
- name: StreamStatus
  property_count: 0
  slug: amazon-qldb-stream-status
- name: TagResourceRequest
  property_count: 1
  slug: amazon-qldb-tag-resource-request
- name: UpdateLedgerPermissionsModeRequest
  property_count: 1
  slug: amazon-qldb-update-ledger-permissions-mode-request
- name: UpdateLedgerPermissionsModeResponse
  property_count: 3
  slug: amazon-qldb-update-ledger-permissions-mode-response
- name: UpdateLedgerRequest
  property_count: 2
  slug: amazon-qldb-update-ledger-request
- name: UpdateLedgerResponse
  property_count: 6
  slug: amazon-qldb-update-ledger-response
- name: ValueHolder
  property_count: 1
  slug: amazon-qldb-value-holder
json_structures:
- name: Amazon Qldb Cancel Journal Kinesis Stream Response Structure
  property_count: 1
  slug: amazon-qldb-cancel-journal-kinesis-stream-response-structure
- name: Amazon Qldb Create Ledger Request Structure
  property_count: 5
  slug: amazon-qldb-create-ledger-request-structure
- name: Amazon Qldb Create Ledger Response Structure
  property_count: 7
  slug: amazon-qldb-create-ledger-response-structure
- name: Amazon Qldb Describe Journal Kinesis Stream Response Structure
  property_count: 1
  slug: amazon-qldb-describe-journal-kinesis-stream-response-structure
- name: Amazon Qldb Describe Journal S3Export Response Structure
  property_count: 1
  slug: amazon-qldb-describe-journal-s3export-response-structure
- name: Amazon Qldb Describe Ledger Response Structure
  property_count: 7
  slug: amazon-qldb-describe-ledger-response-structure
- name: Amazon Qldb Encryption Status Structure
  property_count: 0
  slug: amazon-qldb-encryption-status-structure
- name: Amazon Qldb Error Cause Structure
  property_count: 0
  slug: amazon-qldb-error-cause-structure
- name: Amazon Qldb Export Journal To S3Request Structure
  property_count: 5
  slug: amazon-qldb-export-journal-to-s3request-structure
- name: Amazon Qldb Export Journal To S3Response Structure
  property_count: 1
  slug: amazon-qldb-export-journal-to-s3response-structure
- name: Amazon Qldb Export Status Structure
  property_count: 0
  slug: amazon-qldb-export-status-structure
- name: Amazon Qldb Get Block Request Structure
  property_count: 2
  slug: amazon-qldb-get-block-request-structure
- name: Amazon Qldb Get Block Response Structure
  property_count: 2
  slug: amazon-qldb-get-block-response-structure
- name: Amazon Qldb Get Digest Response Structure
  property_count: 2
  slug: amazon-qldb-get-digest-response-structure
- name: Amazon Qldb Get Revision Request Structure
  property_count: 3
  slug: amazon-qldb-get-revision-request-structure
- name: Amazon Qldb Get Revision Response Structure
  property_count: 2
  slug: amazon-qldb-get-revision-response-structure
- name: Amazon Qldb Journal Kinesis Stream Description Structure
  property_count: 11
  slug: amazon-qldb-journal-kinesis-stream-description-structure
- name: Amazon Qldb Journal S3Export Description Structure
  property_count: 9
  slug: amazon-qldb-journal-s3export-description-structure
- name: Amazon Qldb Kinesis Configuration Structure
  property_count: 2
  slug: amazon-qldb-kinesis-configuration-structure
- name: Amazon Qldb Ledger Encryption Description Structure
  property_count: 3
  slug: amazon-qldb-ledger-encryption-description-structure
- name: Amazon Qldb Ledger State Structure
  property_count: 0
  slug: amazon-qldb-ledger-state-structure
- name: Amazon Qldb Ledger Summary Structure
  property_count: 3
  slug: amazon-qldb-ledger-summary-structure
- name: Amazon Qldb List Journal Kinesis Streams For Ledger Response Structure
  property_count: 2
  slug: amazon-qldb-list-journal-kinesis-streams-for-ledger-response-structure
- name: Amazon Qldb List Journal S3Exports For Ledger Response Structure
  property_count: 2
  slug: amazon-qldb-list-journal-s3exports-for-ledger-response-structure
- name: Amazon Qldb List Journal S3Exports Response Structure
  property_count: 2
  slug: amazon-qldb-list-journal-s3exports-response-structure
- name: Amazon Qldb List Ledgers Response Structure
  property_count: 2
  slug: amazon-qldb-list-ledgers-response-structure
- name: Amazon Qldb List Tags For Resource Response Structure
  property_count: 1
  slug: amazon-qldb-list-tags-for-resource-response-structure
- name: Amazon Qldb Output Format Structure
  property_count: 0
  slug: amazon-qldb-output-format-structure
- name: Amazon Qldb Permissions Mode Structure
  property_count: 0
  slug: amazon-qldb-permissions-mode-structure
- name: Amazon Qldb S3Encryption Configuration Structure
  property_count: 2
  slug: amazon-qldb-s3encryption-configuration-structure
- name: Amazon Qldb S3Export Configuration Structure
  property_count: 3
  slug: amazon-qldb-s3export-configuration-structure
- name: Amazon Qldb S3Object Encryption Type Structure
  property_count: 0
  slug: amazon-qldb-s3object-encryption-type-structure
- name: Amazon Qldb Stream Journal To Kinesis Request Structure
  property_count: 6
  slug: amazon-qldb-stream-journal-to-kinesis-request-structure
- name: Amazon Qldb Stream Journal To Kinesis Response Structure
  property_count: 1
  slug: amazon-qldb-stream-journal-to-kinesis-response-structure
- name: Amazon Qldb Stream Status Structure
  property_count: 0
  slug: amazon-qldb-stream-status-structure
- name: Amazon Qldb Tag Resource Request Structure
  property_count: 1
  slug: amazon-qldb-tag-resource-request-structure
- name: Amazon Qldb Update Ledger Permissions Mode Request Structure
  property_count: 1
  slug: amazon-qldb-update-ledger-permissions-mode-request-structure
- name: Amazon Qldb Update Ledger Permissions Mode Response Structure
  property_count: 3
  slug: amazon-qldb-update-ledger-permissions-mode-response-structure
- name: Amazon Qldb Update Ledger Request Structure
  property_count: 2
  slug: amazon-qldb-update-ledger-request-structure
- name: Amazon Qldb Update Ledger Response Structure
  property_count: 6
  slug: amazon-qldb-update-ledger-response-structure
- name: Amazon Qldb Value Holder Structure
  property_count: 1
  slug: amazon-qldb-value-holder-structure
jsonld:
- class_count: 33
  name: Amazon Qldb Context
  property_count: 44
  slug: amazon-qldb-context
layout: provider
modified: '2026-05-19'
name: Amazon QLDB
nav: Providers
network: true
overview: 'Amazon QLDB publishes 3 APIs on the [APIs.io](https://apis.io/) network: Journal S3 Exports API, Ledgers API, and Tags API. Tagged areas include Blockchain, Database, and Ledger.


  The Amazon QLDB catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon QLDB''s developer surface includes authentication, developer portal, documentation, support, developer console, signup flow, code examples, and 128 more developer resources.'
plans:
- name: Amazon Qldb Plans Pricing
  plan_count: 3
  slug: amazon-qldb-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 5
  name: Amazon Qldb Rate Limits
  slug: amazon-qldb-rate-limits
rules:
- name: Amazon QLDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-qldb-jsonschema-spectral-rules
- name: Amazon QLDB API Rules
  rule_count: 24
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 10
  slug: amazon-qldb-spectral-rules
score:
  band: developing
  composite: 54.7
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 65.7
    developer_ergonomics: 43.5
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-qldb/refs/heads/main/screenshots/amazon-qldb-2026-06-20T171803.png
security:
- kind: authentication
  name: Amazon Qldb Authentication
  slug: amazon-qldb-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Qldb Domain Security
  slug: amazon-qldb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Qldb Vulnerability Disclosure
  slug: amazon-qldb-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Qldb Trust Center
  slug: amazon-qldb-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-qldb
tags:
- Blockchain
- Database
- Ledger
website: https://aws.amazon.com/qldb/
---
