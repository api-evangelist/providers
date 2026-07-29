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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: API for creating and managing CloudHSM clusters and HSM instances for dedicated hardware-based cryptographic key management.
  name: Amazon CloudHSM API
  slug: amazon-cloudhsm-api
artifact_total: 21
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-cloudhsm-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-cloudhsm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-cloudhsm-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/cloudhsm/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/cloudhsm/latest/APIReference/
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
  url: https://aws.amazon.com/blogs/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/cloudhsm/
- group: start
  title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-cloudhsm
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-cloudhsm-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloudhsm-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-cloudhsm-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-cloudhsm-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-cloudhsm-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-cloudhsm-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-cloudhsm-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-cloudhsm-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amazon-cloudhsm-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-cloudhsm-lifecycle.yml
created: '2026-03-16'
description: AWS CloudHSM is a cloud-based hardware security module (HSM) that enables you to manage cryptographic keys on dedicated FIPS 140-2 Level 3 validated, single-tenant HSM instances running within your own VPC for regulatory compliance and data security.
features:
- description: Dedicated single-tenant HSM instances meeting the highest FIPS validation levels.
  name: FIPS 140-2 Level 3 Validated
- description: Complete control over cryptographic keys with no AWS access to key material.
  name: Full Key Control
- description: Add or remove HSMs from clusters as needed, paying only for active resources hourly.
  name: Elastic Capacity
- description: Multi-AZ HSM clusters provide redundancy and automatic failover.
  name: High Availability
- description: Supports PKCS#11, Java JCE, and Microsoft CNG APIs for application integration.
  name: Industry-Standard APIs
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-cloudhsm.png
integrations:
- description: Use CloudHSM keys for Oracle TDE and SQL Server TDE in RDS.
  name: Amazon RDS
- description: Use CloudHSM as a custom key store for AWS KMS operations.
  name: AWS KMS
- description: HSM instances run inside your VPC for network isolation.
  name: Amazon VPC
- description: Control access to HSM cluster management operations.
  name: AWS IAM
- description: Audit HSM management API calls via CloudTrail.
  name: AWS CloudTrail
layout: provider
mcp_servers:
- description: ''
  name: amazon-cloudhsm-mcp.yml
  slug: amazon-cloudhsm-mcpyml
modified: '2026-06-20'
name: Amazon CloudHSM
nav: Providers
network: true
overview: 'Amazon CloudHSM publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CloudHSM, Security, Cryptography, HSM, and Compliance.


  The Amazon CloudHSM catalog on APIs.io includes 1 Spectral governance ruleset.


  Amazon CloudHSM''s developer surface includes developer portal, documentation, support, engineering blog, developer console, signup flow, YouTube channel, and 21 more developer resources.'
random_paper: 14
rules:
- name: Amazon CloudHSM API Rules
  rule_count: 19
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 6
  slug: amazon-cloudhsm-spectral-rules
score:
  band: thin
  composite: 32.8
  delta: -2.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 87.0
    governance: 40.6
    operational_transparency: 21.1
  previous_composite: 35.5
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-cloudhsm/refs/heads/main/screenshots/amazon-cloudhsm-2026-07-25T195946.png
security:
- kind: domain-security
  name: Amazon Cloudhsm Domain Security
  slug: amazon-cloudhsm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Cloudhsm Vulnerability Disclosure
  slug: amazon-cloudhsm-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Cloudhsm Trust Center
  slug: amazon-cloudhsm-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-cloudhsm
tags:
- CloudHSM
- Security
- Cryptography
- HSM
- Compliance
use_cases:
- description: Protect sensitive data with hardware-backed encryption keys.
  name: Data Encryption
- description: Manage SSL/TLS certificates and private keys in dedicated HSMs.
  name: SSL/TLS Offloading
- description: Secure private CA keys for organizations issuing their own certificates.
  name: Certificate Authority
- description: Support transparent data encryption (TDE) for Oracle and SQL Server databases.
  name: Database Encryption
- description: Meet PCI DSS, HIPAA, and other regulatory requirements for key management.
  name: Regulatory Compliance
website: https://aws.amazon.com/cloudhsm/
---
