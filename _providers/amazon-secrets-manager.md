---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Amazon Secrets Manager Agentic Access
  operation_count: 12
  slug: amazon-secrets-manager-agentic-access
  summary_line: 12 operations · 12 acting
api_count: 5
apis:
- description: Operations for generating passwords.
  name: Amazon Secrets Manager Passwords API
  slug: amazon-secrets-manager-passwords-api
- description: Operations for rotating secrets.
  name: Amazon Secrets Manager Rotation API
  slug: amazon-secrets-manager-rotation-api
- description: Operations for managing secrets.
  name: Amazon Secrets Manager Secrets API
  slug: amazon-secrets-manager-secrets-api
- description: 'The #TagResource API from Amazon Secrets Manager — 1 operation(s) for #tagresource.'
  name: 'Amazon Secrets Manager #TagResource API'
  slug: amazon-secrets-manager-tagresource-api
- description: 'The #UntagResource API from Amazon Secrets Manager — 1 operation(s) for #untagresource.'
  name: 'Amazon Secrets Manager #UntagResource API'
  slug: amazon-secrets-manager-untagresource-api
arazzos:
- description: Create a new secret, then immediately retrieve its decrypted value to confirm it was stored.
  name: Amazon Secrets Manager Create and Read Secret
  slug: amazon-secrets-manager-create-and-read-secret-workflow
- description: List secrets filtered by name, branch on whether a match exists, then describe and schedule deletion of the matched secret.
  name: Amazon Secrets Manager Find and Delete Secret
  slug: amazon-secrets-manager-find-and-delete-secret-workflow
- description: Generate a random password, store it as a new secret, then read the secret value back to confirm it was saved.
  name: Amazon Secrets Manager Generate Password and Store Secret
  slug: amazon-secrets-manager-generate-password-and-store-secret-workflow
- description: Cancel the scheduled deletion of a secret with RestoreSecret, then describe it to confirm the DeletedDate was cleared.
  name: Amazon Secrets Manager Restore Deleted Secret
  slug: amazon-secrets-manager-restore-deleted-secret-workflow
- description: Start rotation on a secret with a Lambda rotation function, then describe it to confirm rotation is configured.
  name: Amazon Secrets Manager Rotate and Describe
  slug: amazon-secrets-manager-rotate-and-describe-workflow
- description: Store a new encrypted version of a secret with PutSecretValue, then read the current value to confirm the update.
  name: Amazon Secrets Manager Put New Version and Verify
  slug: amazon-secrets-manager-rotate-version-and-verify-workflow
- description: Attach tags to a secret with TagResource, then describe the secret to confirm the tags are present in its metadata.
  name: Amazon Secrets Manager Tag Secret and Verify
  slug: amazon-secrets-manager-tag-secret-and-verify-workflow
- description: Update a secret's description and KMS key with UpdateSecret, then describe it to confirm the new metadata was applied.
  name: Amazon Secrets Manager Update Metadata and Verify
  slug: amazon-secrets-manager-update-metadata-and-verify-workflow
artifact_total: 65
collections:
- collection_type: postman
  name: Amazon Secrets Manager API
  slug: postman-amazon-secrets-manager
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Secrets Manager Passwords API
  slug: open-amazon-secrets-manager-passwords-api
- collection_type: open
  name: Amazon Secrets Manager Passwords Rotation API
  slug: open-amazon-secrets-manager-rotation-api
- collection_type: open
  name: Amazon Manager Passwords Secrets API
  slug: open-amazon-secrets-manager-secrets-api
- collection_type: open
  name: 'Amazon Secrets Manager Passwords #TagResource API'
  slug: open-amazon-secrets-manager-tagresource-api
- collection_type: open
  name: 'Amazon Secrets Manager Passwords #UntagResource API'
  slug: open-amazon-secrets-manager-untagresource-api
- collection_type: open
  name: Amazon Secrets Manager API
  slug: open-amazon-secrets-manager
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-secrets-manager-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-secrets-manager-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-secrets-manager-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-secrets-manager-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-secrets-manager-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-secrets-manager-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-secrets-manager-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-secrets-manager-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-secrets-manager-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-secrets-manager-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-secrets-manager-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-secrets-manager-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amazon-secrets-manager-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-secrets-manager-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amazon-secrets-manager-conventions.yml
- group: build
  title: ''
  type: CLI
  url: cli/amazon-secrets-manager-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amazon-secrets-manager-data-model.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-secrets-manager/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-secrets-manager-create-and-read-secret-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-secrets-manager-find-and-delete-secret-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-secrets-manager-generate-password-and-store-secret-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-secrets-manager-restore-deleted-secret-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-secrets-manager-rotate-and-describe-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-secrets-manager-rotate-version-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-secrets-manager-tag-secret-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-secrets-manager-update-metadata-and-verify-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/secrets-manager/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/secretsmanager/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/secrets-manager/pricing/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/secrets-manager/faqs/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: auth
  title: ''
  type: Security
  url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/security.html
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-secrets-manager
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: build
  title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-secrets-manager-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-secrets-manager-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-secrets-manager-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-secrets-manager-get-random-password-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-secrets-manager-list-secrets-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-secrets-manager-tag-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-secrets-manager-get-random-password-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-secrets-manager-list-secrets-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-secrets-manager-rotation-rules-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-secrets-manager-secret-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-secrets-manager-secret-value-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-secrets-manager-tag-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-secrets-manager-get-random-password-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-secrets-manager-list-secrets-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-secrets-manager-rotation-rules-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-secrets-manager-secret-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-secrets-manager-secret-value-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-secrets-manager-tag-example.json
created: '2024-01-01'
description: Amazon Secrets Manager helps you manage, retrieve, and rotate database credentials, API keys, and other secrets throughout their lifecycle. It provides centralized secrets management with built-in integration for Amazon RDS, Amazon Redshift, and Amazon DocumentDB, enabling automatic rotation of secrets without requiring application changes.
examples:
- key_count: 1
  name: Amazon Secrets Manager Get Random Password Response Example
  slug: amazon-secrets-manager-get-random-password-response-example
- key_count: 2
  name: Amazon Secrets Manager List Secrets Response Example
  slug: amazon-secrets-manager-list-secrets-response-example
- key_count: 3
  name: Amazon Secrets Manager Rotation Rules Example
  slug: amazon-secrets-manager-rotation-rules-example
- key_count: 16
  name: Amazon Secrets Manager Secret Example
  slug: amazon-secrets-manager-secret-example
- key_count: 7
  name: Amazon Secrets Manager Secret Value Example
  slug: amazon-secrets-manager-secret-value-example
- key_count: 2
  name: Amazon Secrets Manager Tag Example
  slug: amazon-secrets-manager-tag-example
features:
- description: Automatically rotate secrets on a schedule using AWS Lambda rotation functions without changing application code.
  name: Automatic Secret Rotation
- description: Store and manage all secrets in a single, centralized location with fine-grained access controls.
  name: Centralized Secret Storage
- description: Built-in integration with Amazon RDS, Aurora, Redshift, and DocumentDB for automatic credential rotation.
  name: Native Database Integration
- description: Maintain multiple versions of a secret simultaneously to support zero-downtime rotation.
  name: Secret Versioning
- description: Log all secret access and management actions via AWS CloudTrail for compliance and audit purposes.
  name: Audit and Compliance
- description: Share secrets across AWS accounts using resource-based policies.
  name: Cross-Account Access
- description: All secrets are encrypted at rest using AWS KMS keys you control.
  name: Encryption at Rest
- description: Generate cryptographically secure random passwords with configurable complexity requirements.
  name: Random Password Generation
finops:
- name: Amazon Secrets Manager Finops
  service_category: API
  slug: amazon-secrets-manager-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-secrets-manager.png
json_schemas:
- name: GetRandomPasswordResponse
  property_count: 1
  slug: amazon-secrets-manager-get-random-password-response
- name: ListSecretsResponse
  property_count: 2
  slug: amazon-secrets-manager-list-secrets-response
- name: RotationRules
  property_count: 3
  slug: amazon-secrets-manager-rotation-rules
- name: Secret
  property_count: 16
  slug: amazon-secrets-manager-secret
- name: SecretValue
  property_count: 7
  slug: amazon-secrets-manager-secret-value
- name: Tag
  property_count: 2
  slug: amazon-secrets-manager-tag
json_structures:
- name: Amazon Secrets Manager Get Random Password Response Structure
  property_count: 1
  slug: amazon-secrets-manager-get-random-password-response-structure
- name: Amazon Secrets Manager List Secrets Response Structure
  property_count: 2
  slug: amazon-secrets-manager-list-secrets-response-structure
- name: Amazon Secrets Manager Rotation Rules Structure
  property_count: 3
  slug: amazon-secrets-manager-rotation-rules-structure
- name: Amazon Secrets Manager Secret Structure
  property_count: 16
  slug: amazon-secrets-manager-secret-structure
- name: Amazon Secrets Manager Secret Value Structure
  property_count: 7
  slug: amazon-secrets-manager-secret-value-structure
- name: Amazon Secrets Manager Tag Structure
  property_count: 2
  slug: amazon-secrets-manager-tag-structure
jsonld:
- class_count: 6
  name: Amazon Secrets Manager Context
  property_count: 27
  slug: amazon-secrets-manager-context
layout: provider
mcp_servers:
- description: ''
  name: amazon-secrets-manager-mcp.yml
  slug: amazon-secrets-manager-mcpyml
modified: '2026-06-20'
name: Amazon Secrets Manager
nav: Providers
network: true
overview: 'Amazon Secrets Manager publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Passwords API, Rotation API, Secrets API, and 2 more. Tagged areas include Configuration, Credentials, Rotation, Secrets, and Security.


  The Amazon Secrets Manager catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Secrets Manager''s developer surface includes authentication, CLI, developer portal, getting-started guide, documentation, API reference, developer console, and 57 more developer resources.'
plans:
- name: Amazon Secrets Manager Plans Pricing
  plan_count: 3
  slug: amazon-secrets-manager-plans-pricing
random_paper: 142
rate_limits:
- limit_count: 5
  name: Amazon Secrets Manager Rate Limits
  slug: amazon-secrets-manager-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Secrets Manager API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-secrets-manager-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Amazon Secrets Manager API Rules
  rule_count: 23
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 13
  slug: amazon-secrets-manager-spectral-rules
score:
  band: exemplar
  composite: 66.7
  delta: -5.1
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 41.7
    contract_quality: 67.8
    developer_ergonomics: 76.2
    discoverability: 94.4
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 71.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-secrets-manager/refs/heads/main/screenshots/amazon-secrets-manager-2026-06-20T171815.png
security:
- kind: authentication
  name: Amazon Secrets Manager Authentication
  slug: amazon-secrets-manager-authentication
  summary_line: aws-sigv4 · 1 scheme
- kind: domain-security
  name: Amazon Secrets Manager Domain Security
  slug: amazon-secrets-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Secrets Manager Vulnerability Disclosure
  slug: amazon-secrets-manager-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Secrets Manager Trust Center
  slug: amazon-secrets-manager-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-secrets-manager
tags:
- Configuration
- Credentials
- Rotation
- Secrets
- Security
use_cases:
- description: Automatically rotate and manage database credentials for RDS, Aurora, and other databases.
  name: Database Credential Management
- description: Securely store and retrieve API keys, OAuth tokens, and other third-party service credentials.
  name: API Key Storage
- description: Centralize sensitive application configuration such as connection strings and encryption keys.
  name: Application Configuration
- description: Share service-to-service credentials securely across microservices without embedding in code.
  name: Cross-Service Credentials
- description: Meet compliance requirements like PCI DSS and SOC 2 by enforcing regular credential rotation.
  name: Compliance Secret Rotation
- description: Enforce organizational policies on secret creation, rotation schedules, and access patterns.
  name: Secrets Lifecycle Governance
website: https://aws.amazon.com/
---
