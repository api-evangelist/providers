---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.2
  scored_at: '2026-10-31'
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
- baseURL: https://kms.amazonaws.com
  baseurl_source: declared
  description: The Kms Alias API from Amazon KMS — 3 operation(s) for kms alias.
  name: Amazon KMS Kms Alias API
  slug: amazon-kms-alias-api
- baseURL: https://kms.amazonaws.com
  baseurl_source: declared
  description: The Kms Custom Key Store API from Amazon KMS — 6 operation(s) for kms custom key store.
  name: Amazon KMS Kms Custom Key Store API
  slug: amazon-kms-custom-key-store-api
- baseURL: https://kms.amazonaws.com
  baseurl_source: declared
  description: The Kms Grant API from Amazon KMS — 4 operation(s) for kms grant.
  name: Amazon KMS Kms Grant API
  slug: amazon-kms-grant-api
- baseURL: https://kms.amazonaws.com
  baseurl_source: declared
  description: The Kms Key Policy API from Amazon KMS — 3 operation(s) for kms key policy.
  name: Amazon KMS Kms Key Policy API
  slug: amazon-kms-key-policy-api
- baseURL: https://kms.amazonaws.com
  baseurl_source: declared
  description: The Kms Key Rotation API from Amazon KMS — 3 operation(s) for kms key rotation.
  name: Amazon KMS Kms Key Rotation API
  slug: amazon-kms-key-rotation-api
- baseURL: https://kms.amazonaws.com
  baseurl_source: declared
  description: The Kms Operations API from Amazon KMS — 21 operation(s) for kms operations.
  name: Amazon KMS Kms Operations API
  slug: amazon-kms-operations-api
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
artifact_total: 45
collections:
- collection_type: postman
  name: Amazon KMS API
  slug: postman-amazon-kms
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
- group: commercial
  href: https://artifacts.apis.io/amazon-kms/plans/amazon-kms-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-kms-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/amazon-kms/rate-limits/amazon-kms-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-kms-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-kms/finops/amazon-kms-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-kms-finops.yml
- group: other
  href: https://artifacts.apis.io/amazon-kms/capabilities/amazon-kms-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-kms-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/kms/
- group: agent
  href: https://artifacts.apis.io/amazon-kms/agentic-access/amazon-kms-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-kms-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-kms/security/amazon-kms-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-kms-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-kms/security/amazon-kms-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-kms-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-kms/security/amazon-kms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-kms-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/amazon-kms/authentication/amazon-kms-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-kms-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-kms/overview
- group: design
  href: https://artifacts.apis.io/amazon-kms/arazzo/amazon-kms-create-key-and-describe-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-kms-create-key-and-describe-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-kms/arazzo/amazon-kms-data-key-generate-and-decrypt-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-kms-data-key-generate-and-decrypt-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-kms/arazzo/amazon-kms-disable-and-schedule-deletion-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-kms-disable-and-schedule-deletion-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-kms/arazzo/amazon-kms-enable-key-and-verify-state-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-kms-enable-key-and-verify-state-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-kms/arazzo/amazon-kms-envelope-encrypt-decrypt-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-kms-envelope-encrypt-decrypt-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-kms/arazzo/amazon-kms-list-and-describe-keys-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-kms-list-and-describe-keys-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-kms/arazzo/amazon-kms-provision-key-and-encrypt-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-kms-provision-key-and-encrypt-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-kms/arazzo/amazon-kms-sign-and-verify-workflow.yml
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
  href: https://artifacts.apis.io/amazon-kms/rules/amazon-kms-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-kms-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/amazon-kms/vocabulary/amazon-kms-vocabulary.yaml
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
- has_sources: true
  method: derived
  name: Amazon Kms Finops
  primary_unit: 10,000 requests
  service_category: ''
  slug: amazon-kms-finops
  template: false
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
modified: '2026-09-16'
name: Amazon KMS
nav: Providers
network: true
overview: 'Amazon KMS publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cryptographic Operations API, Keys API, Kms Alias API, and 5 more. Tagged areas include Cryptography, Data Protection, Encryption, Key Management, and Security.


  The Amazon KMS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon KMS''s developer surface includes authentication, engineering blog, support, developer console, CLI, developer portal, documentation, and 30 more developer resources.'
plans:
- name: Amazon Kms Plans Pricing
  plan_count: 4
  slug: amazon-kms-plans-pricing
- name: Amazon Kms Price Estimates
  plan_count: 0
  slug: amazon-kms-price-estimates
random_paper: 14
rate_limits:
- limit_count: 5
  name: Amazon Kms Rate Limits
  slug: amazon-kms-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Amazon KMS — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-kms-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 65
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
  band: exemplar
  composite: 70.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.4
    catalog_earned_first_party: 12.0
    catalog_gap: 40.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.4
  facets:
    access_clarity: 100.0
    contract_governance: 27.3
    contract_quality: 62.5
    developer_ergonomics: 79.8
    discoverability: 73.2
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 67.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 75.0
      total: 8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/amazon-kms/amazon-kms-2026-06-20T171719.png
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
