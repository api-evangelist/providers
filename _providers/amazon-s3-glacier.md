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
- acting_count: 4
  human_in_the_loop: 0
  name: Amazon S3 Glacier Agentic Access
  operation_count: 7
  slug: amazon-s3-glacier-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- baseURL: https://glacier.amazonaws.com
  baseurl_source: declared
  description: The Vaults API from Amazon S3 Glacier — 4 operation(s) for vaults.
  name: Amazon S3 Glacier Vaults API
  slug: amazon-s3-glacier-vaults-api
- baseURL: https://glacier.amazonaws.com
  baseurl_source: declared
  description: The S3 Glacier Access Policy API from Amazon S3 Glacier — 1 operation(s) for s3 glacier access policy.
  name: Amazon S3 Glacier S3 Glacier Access Policy API
  slug: amazon-s3-glacier-access-policy-api
- baseURL: https://glacier.amazonaws.com
  baseurl_source: declared
  description: The S3 Glacier Lock Policy API from Amazon S3 Glacier — 2 operation(s) for s3 glacier lock policy.
  name: Amazon S3 Glacier S3 Glacier Lock Policy API
  slug: amazon-s3-glacier-lock-policy-api
- baseURL: https://glacier.amazonaws.com
  baseurl_source: declared
  description: The S3 Glacier Multipart Uploads API from Amazon S3 Glacier — 2 operation(s) for s3 glacier multipart uploads.
  name: Amazon S3 Glacier S3 Glacier Multipart Uploads API
  slug: amazon-s3-glacier-multipart-uploads-api
- baseURL: https://glacier.amazonaws.com
  baseurl_source: declared
  description: The S3 Glacier Notification Configuration API from Amazon S3 Glacier — 1 operation(s) for s3 glacier notification configuration.
  name: Amazon S3 Glacier S3 Glacier Notification Configuration API
  slug: amazon-s3-glacier-notification-configuration-api
- baseURL: https://glacier.amazonaws.com
  baseurl_source: declared
  description: The S3 Glacier Operations API from Amazon S3 Glacier — 5 operation(s) for s3 glacier operations.
  name: Amazon S3 Glacier S3 Glacier Operations API
  slug: amazon-s3-glacier-operations-api
- baseURL: https://glacier.amazonaws.com
  baseurl_source: declared
  description: The S3 Glacier Tags API from Amazon S3 Glacier — 3 operation(s) for s3 glacier tags.
  name: Amazon S3 Glacier S3 Glacier Tags API
  slug: amazon-s3-glacier-tags-api
artifact_total: 37
collections:
- collection_type: postman
  name: Amazon S3 Glacier REST Vaults API
  slug: postman-amazon-s3-glacier-vaults-api
- collection_type: open
  name: Amazon S3 Glacier REST API
  slug: open-amazon-s3-glacier-api
- collection_type: open
  name: Amazon S3 Glacier REST Vaults API
  slug: open-amazon-s3-glacier-vaults-api
common:
- group: commercial
  href: https://artifacts.apis.io/amazon-s3-glacier/plans/amazon-s3-glacier-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-s3-glacier-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/amazon-s3-glacier/rate-limits/amazon-s3-glacier-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-s3-glacier-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-s3-glacier/finops/amazon-s3-glacier-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-s3-glacier-finops.yml
- group: other
  href: https://artifacts.apis.io/amazon-s3-glacier/capabilities/amazon-s3-glacier-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-s3-glacier-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/s3/storage-classes/glacier/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-s3-glacier/overview
- group: agent
  href: https://artifacts.apis.io/amazon-s3-glacier/agentic-access/amazon-s3-glacier-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-s3-glacier-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-s3-glacier/security/amazon-s3-glacier-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-s3-glacier-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-s3-glacier/security/amazon-s3-glacier-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-s3-glacier-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-s3-glacier/security/amazon-s3-glacier-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-s3-glacier-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/amazon-s3-glacier/authentication/amazon-s3-glacier-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-s3-glacier-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/s3/storage-classes/glacier/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/amazonglacier/
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
  type: Portal
  url: https://console.aws.amazon.com/glacier/
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
  href: https://artifacts.apis.io/amazon-s3-glacier/json-ld/amazon-s3-glacier-api-describe-vault-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-s3-glacier-api-describe-vault-context.jsonld
- group: design
  href: https://artifacts.apis.io/amazon-s3-glacier/json-ld/amazon-s3-glacier-api-job-parameters-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-s3-glacier-api-job-parameters-context.jsonld
- group: design
  href: https://artifacts.apis.io/amazon-s3-glacier/json-ld/amazon-s3-glacier-api-list-vaults-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-s3-glacier-api-list-vaults-context.jsonld
- group: design
  href: https://artifacts.apis.io/amazon-s3-glacier/json-ld/amazon-s3-glacier-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-s3-glacier-context.jsonld
- group: design
  href: https://artifacts.apis.io/amazon-s3-glacier/json-ld/amazon-s3-glacier-vault-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-s3-glacier-vault-context.jsonld
- group: docs
  href: https://artifacts.apis.io/amazon-s3-glacier/json-schema/amazon-s3-glacier-api-describe-vault-output-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-s3-glacier-api-describe-vault-output-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-s3-glacier/json-schema/amazon-s3-glacier-api-job-parameters-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-s3-glacier-api-job-parameters-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-s3-glacier/json-schema/amazon-s3-glacier-api-list-vaults-output-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-s3-glacier-api-list-vaults-output-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-s3-glacier/json-schema/amazon-s3-glacier-vault-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-s3-glacier-vault-schema.json
- group: design
  href: https://artifacts.apis.io/amazon-s3-glacier/json-structure/amazon-s3-glacier-api-describe-vault-output-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-s3-glacier-api-describe-vault-output-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-s3-glacier/json-structure/amazon-s3-glacier-api-job-parameters-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-s3-glacier-api-job-parameters-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-s3-glacier/json-structure/amazon-s3-glacier-api-list-vaults-output-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-s3-glacier-api-list-vaults-output-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-s3-glacier/json-structure/amazon-s3-glacier-vault-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-s3-glacier-vault-structure.json
- group: build
  href: https://artifacts.apis.io/amazon-s3-glacier/examples/amazon-s3-glacier-api-describe-vault-output-example.json
  title: ''
  type: Examples
  url: examples/amazon-s3-glacier-api-describe-vault-output-example.json
- group: build
  href: https://artifacts.apis.io/amazon-s3-glacier/examples/amazon-s3-glacier-api-job-parameters-example.json
  title: ''
  type: Examples
  url: examples/amazon-s3-glacier-api-job-parameters-example.json
- group: build
  href: https://artifacts.apis.io/amazon-s3-glacier/examples/amazon-s3-glacier-api-list-vaults-output-example.json
  title: ''
  type: Examples
  url: examples/amazon-s3-glacier-api-list-vaults-output-example.json
- group: build
  href: https://artifacts.apis.io/amazon-s3-glacier/examples/amazon-s3-glacier-vault-example.json
  title: ''
  type: Examples
  url: examples/amazon-s3-glacier-vault-example.json
- group: design
  href: https://artifacts.apis.io/amazon-s3-glacier/rules/amazon-s3-glacier-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-s3-glacier-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/amazon-s3-glacier/vocabulary/amazon-s3-glacier-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-s3-glacier-vocabulary.yaml
- group: docs
  href: https://artifacts.apis.io/amazon-s3-glacier/openapi/_original/amazon-s3-glacier-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/amazon-s3-glacier-api-openapi.yml
created: '2024-01-15'
description: Amazon S3 Glacier is a secure, durable, and extremely low-cost Amazon S3 storage class purpose-built for long-term data archiving and digital preservation. It provides comprehensive security and compliance capabilities that can help meet even the most stringent regulatory requirements, with retrieval options ranging from minutes to hours depending on your access needs.
examples:
- key_count: 6
  name: Amazon S3 Glacier Api Describe Vault Output Example
  slug: amazon-s3-glacier-api-describe-vault-output-example
- key_count: 6
  name: Amazon S3 Glacier Api Job Parameters Example
  slug: amazon-s3-glacier-api-job-parameters-example
- key_count: 2
  name: Amazon S3 Glacier Api List Vaults Output Example
  slug: amazon-s3-glacier-api-list-vaults-output-example
- key_count: 9
  name: Amazon S3 Glacier Vault Example
  slug: amazon-s3-glacier-vault-example
finops:
- has_sources: true
  method: derived
  name: Amazon S3 Glacier Finops
  primary_unit: gb
  service_category: ''
  slug: amazon-s3-glacier-finops
  template: false
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: DescribeVaultOutput
  property_count: 6
  slug: amazon-s3-glacier-api-describe-vault-output
- name: JobParameters
  property_count: 6
  slug: amazon-s3-glacier-api-job-parameters
- name: ListVaultsOutput
  property_count: 2
  slug: amazon-s3-glacier-api-list-vaults-output
- name: Amazon S3 Glacier Vault
  property_count: 9
  slug: amazon-s3-glacier-vault
json_structures:
- name: Amazon S3 Glacier Api Describe Vault Output Structure
  property_count: 6
  slug: amazon-s3-glacier-api-describe-vault-output-structure
- name: Amazon S3 Glacier Api Job Parameters Structure
  property_count: 6
  slug: amazon-s3-glacier-api-job-parameters-structure
- name: Amazon S3 Glacier Api List Vaults Output Structure
  property_count: 2
  slug: amazon-s3-glacier-api-list-vaults-output-structure
- name: Amazon S3 Glacier Vault Structure
  property_count: 9
  slug: amazon-s3-glacier-vault-structure
jsonld:
- class_count: 1
  name: Amazon S3 Glacier Api Describe Vault Context
  property_count: 6
  slug: amazon-s3-glacier-api-describe-vault-context
- class_count: 1
  name: Amazon S3 Glacier Api Job Parameters Context
  property_count: 6
  slug: amazon-s3-glacier-api-job-parameters-context
- class_count: 1
  name: Amazon S3 Glacier Api List Vaults Context
  property_count: 2
  slug: amazon-s3-glacier-api-list-vaults-context
- class_count: 0
  name: Amazon S3 Glacier Context
  property_count: 3
  slug: amazon-s3-glacier-context
- class_count: 1
  name: Amazon S3 Glacier Vault Context
  property_count: 9
  slug: amazon-s3-glacier-vault-context
layout: provider
modified: '2026-09-16'
name: Amazon S3 Glacier
nav: Providers
network: true
overview: 'Amazon S3 Glacier publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Vaults API, S3 Glacier Access Policy API, S3 Glacier Lock Policy API, and 4 more. Tagged areas include Archives, Backup, and Storage.


  The Amazon S3 Glacier catalog on APIs.io includes 5 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon S3 Glacier''s developer surface includes authentication, developer portal, documentation, support, signup flow, code examples, and 37 more developer resources.'
plans:
- name: Amazon S3 Glacier Plans Pricing
  plan_count: 9
  slug: amazon-s3-glacier-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Amazon S3 Glacier Rate Limits
  slug: amazon-s3-glacier-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Amazon S3 Glacier — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-s3-glacier-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: Amazon S3 Glacier API Rules
  rule_count: 25
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 16
  slug: amazon-s3-glacier-spectral-rules
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 64.0
    catalog_earned_first_party: 12.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.1
  facets:
    access_clarity: 92.1
    contract_governance: 27.3
    contract_quality: 61.8
    developer_ergonomics: 48.8
    discoverability: 57.1
    operational_transparency: 39.5
  previous_composite: 57.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 85.7
      total: 7
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
screenshot: https://apis.io/screenshots/amazon-s3-glacier/amazon-s3-glacier-2026-06-20T171814.png
security:
- kind: authentication
  name: Amazon S3 Glacier Authentication
  slug: amazon-s3-glacier-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon S3 Glacier Domain Security
  slug: amazon-s3-glacier-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon S3 Glacier Vulnerability Disclosure
  slug: amazon-s3-glacier-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon S3 Glacier Trust Center
  slug: amazon-s3-glacier-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-s3-glacier
tags:
- Archives
- Backup
- Storage
website: https://aws.amazon.com/s3/storage-classes/glacier/
---
