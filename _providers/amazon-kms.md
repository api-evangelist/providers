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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Amazon Kms Agentic Access
  operation_count: 11
  slug: amazon-kms-agentic-access
  summary_line: 11 operations · 9 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://kms.amazonaws.com
  baseurl_source: declared
  description: Encryption, decryption, and signing operations
  name: Amazon KMS Cryptographic Operations API
  slug: amazon-kms-cryptographic-operations-api
- baseURL: https://kms.amazonaws.com
  baseurl_source: declared
  description: KMS cryptographic key management
  name: Amazon KMS Keys API
  slug: amazon-kms-keys-api
arazzos:
- description: Create a new customer managed KMS key and read back its full metadata.
  name: Amazon KMS Create Key and Describe
  slug: amazon-kms-create-key-and-describe-workflow
- description: Generate a data key, then decrypt its encrypted form to recover the plaintext key.
  name: Amazon KMS Generate and Recover Data Key
  slug: amazon-kms-data-key-generate-and-decrypt-workflow
- description: Disable a KMS key and then schedule it for deletion after a waiting period.
  name: Amazon KMS Disable and Schedule Key Deletion
  slug: amazon-kms-disable-and-schedule-deletion-workflow
- description: Enable a disabled KMS key and confirm it is back in the Enabled state.
  name: Amazon KMS Enable Key and Verify State
  slug: amazon-kms-enable-key-and-verify-state-workflow
- description: Generate a data key, then round-trip ciphertext through encrypt and decrypt.
  name: Amazon KMS Envelope Encrypt and Decrypt
  slug: amazon-kms-envelope-encrypt-decrypt-workflow
- description: List the KMS keys in the account and describe the first one in detail.
  name: Amazon KMS List and Describe Keys
  slug: amazon-kms-list-and-describe-keys-workflow
- description: Create a KMS key, enable it, and immediately encrypt a payload with it.
  name: Amazon KMS Provision Key and Encrypt
  slug: amazon-kms-provision-key-and-encrypt-workflow
- description: Sign a message with an asymmetric KMS key, then verify the signature.
  name: Amazon KMS Sign and Verify
  slug: amazon-kms-sign-and-verify-workflow
artifact_total: 39
collections:
- collection_type: postman
  name: Amazon KMS API
  slug: postman-amazon-kms
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon KMS Cryptographic Operations API
  slug: open-amazon-kms-cryptographic-operations-api
- collection_type: open
  name: Amazon KMS Cryptographic Operations Keys API
  slug: open-amazon-kms-keys-api
- collection_type: open
  name: Amazon KMS API
  slug: open-amazon-kms
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-kms-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-kms-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-kms-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-kms-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-kms-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-kms/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kms-create-key-and-describe-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kms-data-key-generate-and-decrypt-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kms-disable-and-schedule-deletion-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kms-enable-key-and-verify-state-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kms-envelope-encrypt-decrypt-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kms-list-and-describe-keys-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kms-provision-key-and-encrypt-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kms-sign-and-verify-workflow.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/category/security-identity-compliance/aws-key-management-service/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/kms/home
- group: build
  title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/kms/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/kms/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/kms/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/kms/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/kms/getting-started/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/kms/faqs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-kms-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-kms-vocabulary.yaml
created: '2024-01-15'
description: AWS Key Management Service (KMS) is a managed service that makes it easy to create and control the cryptographic keys used to protect your data, integrated with other AWS services to simplify encryption of data stored and managed in those services.
examples:
- key_count: 10
  name: Amazon Kms Key Example
  slug: amazon-kms-key-example
features:
- description: Create, import, rotate, disable, delete, and audit usage of cryptographic keys from a central location.
  name: Centralized Key Management
- description: Keys are protected by FIPS 140-2 validated hardware security modules (HSMs).
  name: Hardware Security Modules
- description: Enable automatic annual rotation of KMS keys without changing key ARNs.
  name: Automatic Key Rotation
- description: Create multi-Region keys that can be replicated into multiple AWS Regions.
  name: Multi-Region Keys
- description: Generate and use asymmetric RSA and ECC key pairs for encryption and signing.
  name: Asymmetric Key Support
- description: Every KMS API call is logged to AWS CloudTrail for auditing and compliance.
  name: CloudTrail Integration
finops:
- name: Amazon Kms Finops
  service_category: API
  slug: amazon-kms-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Key
  property_count: 10
  slug: amazon-kms-key
json_structures:
- name: Amazon Kms Key Structure
  property_count: 10
  slug: amazon-kms-key-structure
jsonld:
- class_count: 1
  name: Amazon Kms Context
  property_count: 7
  slug: amazon-kms-context
layout: provider
modified: '2026-05-19'
name: Amazon KMS
nav: Providers
network: true
overview: 'Amazon KMS publishes 2 APIs on the [APIs.io](https://apis.io/) network: Cryptographic Operations API and Keys API. Tagged areas include Cryptography, Data Protection, Encryption, Key Management, and Security.


  The Amazon KMS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon KMS''s developer surface includes authentication, engineering blog, support, developer console, CLI, developer portal, documentation, and 25 more developer resources.'
plans:
- name: Amazon Kms Plans Pricing
  plan_count: 3
  slug: amazon-kms-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Amazon Kms Rate Limits
  slug: amazon-kms-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon KMS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-kms-jsonschema-spectral-rules
- effective_rule_count: 65
  extends:
  - spectral:oas
  name: Amazon KMS API Rules
  rule_count: 24
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 15
  slug: amazon-kms-spectral-rules
score:
  band: strong
  composite: 62.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 28.8
    contract_quality: 64.6
    developer_ergonomics: 83.3
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 62.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-kms/refs/heads/main/screenshots/amazon-kms-2026-06-20T171719.png
security:
- kind: authentication
  name: Amazon Kms Authentication
  slug: amazon-kms-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Kms Domain Security
  slug: amazon-kms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Kms Vulnerability Disclosure
  slug: amazon-kms-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Kms Trust Center
  slug: amazon-kms-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-kms
tags:
- Cryptography
- Data Protection
- Encryption
- Key Management
- Security
use_cases:
- description: Encrypt data stored in S3, RDS, EBS, and other AWS services using KMS keys.
  name: Data at Rest Encryption
- description: Use KMS to generate data encryption keys for envelope encryption patterns.
  name: Envelope Encryption
- description: Use asymmetric KMS keys to sign and verify digital signatures.
  name: Digital Signatures
- description: Import your own cryptographic key material into AWS KMS for compliance requirements.
  name: BYOK (Bring Your Own Key)
website: https://aws.amazon.com/kms/
---
