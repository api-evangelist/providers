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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Cloud Kms Agentic Access
  operation_count: 9
  slug: google-cloud-kms-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 3
apis:
- description: The Crypto Keys API from Google Cloud KMS — 2 operation(s) for crypto keys.
  name: Google Cloud KMS Crypto Keys API
  slug: google-cloud-kms-crypto-keys-api
- description: The Crypto Operations API from Google Cloud KMS — 2 operation(s) for crypto operations.
  name: Google Cloud KMS Crypto Operations API
  slug: google-cloud-kms-crypto-operations-api
- description: The Key Rings API from Google Cloud KMS — 2 operation(s) for key rings.
  name: Google Cloud KMS Key Rings API
  slug: google-cloud-kms-key-rings-api
artifact_total: 18
collections:
- collection_type: postman
  name: Google Cloud KMS Crypto Keys API
  slug: postman-google-cloud-kms-crypto-keys-api
- collection_type: postman
  name: Google Cloud KMS Crypto Keys Crypto Operations API
  slug: postman-google-cloud-kms-crypto-operations-api
- collection_type: postman
  name: Google Cloud KMS Crypto Keys Key Rings API
  slug: postman-google-cloud-kms-key-rings-api
- collection_type: open
  name: Google Cloud KMS API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-kms/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-kms-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-kms-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-kms-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-kms-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-kms-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/kms
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/kms/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/kms/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/kms/docs/iam
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/kms/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/kms/docs/support
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/context.jsonld
created: '2026-03-13'
description: Google Cloud Key Management Service (KMS) allows you to create, import, and manage cryptographic keys and perform cryptographic operations in a central cloud service. It supports encryption, decryption, signing, and verification using symmetric and asymmetric keys for securing data and workloads.
finops:
- name: Google Cloud Kms Finops
  service_category: API
  slug: google-cloud-kms-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-kms.png
json_schemas:
- name: CryptoKey
  property_count: 10
  slug: crypto-key
jsonld:
- class_count: 3
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Cloud KMS
nav: Providers
network: true
overview: 'Google Cloud KMS publishes 3 APIs on the [APIs.io](https://apis.io/) network: Crypto Keys API, Crypto Operations API, and Key Rings API. Tagged areas include Cryptography, Encryption, Google Cloud, Key Management, and KMS.


  The Google Cloud KMS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud KMS''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Kms Plans Pricing
  plan_count: 3
  slug: google-cloud-kms-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Google Cloud Kms Rate Limits
  slug: google-cloud-kms-rate-limits
rules:
- name: Google Cloud KMS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-kms-jsonschema-spectral-rules
scopes:
- name: Google Cloud Kms Scopes
  scope_count: 2
  slug: google-cloud-kms-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 61.3
  delta: -3.2
  facets:
    commercial_clarity: 71.1
    contract_quality: 65.3
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 64.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-kms/refs/heads/main/screenshots/google-cloud-kms-2026-06-20T182123.png
security:
- kind: authentication
  name: Google Cloud Kms Authentication
  slug: google-cloud-kms-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Kms Domain Security
  slug: google-cloud-kms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Kms Vulnerability Disclosure
  slug: google-cloud-kms-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-kms
tags:
- Cryptography
- Encryption
- Google Cloud
- Key Management
- KMS
- Security
website: https://cloud.google.com/kms
---
