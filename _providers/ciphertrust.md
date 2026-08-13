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
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: REST API for the CipherTrust Manager control plane. Manages encryption keys, secrets, certificates, tokenization, users, connections, and policies. Base path /api/v1 with JWT bearer authentication obt
  name: CipherTrust Manager REST API
  slug: ciphertrust-manager-rest-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ciphertrust-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ciphertrust-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cpl.thalesgroup.com/encryption/ciphertrust-manager
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs-cybersec.thalesgroup.com/bundle/latest-cdsp-cm/page/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs-cybersec.thalesgroup.com/bundle/latest-cdsp-cm/page/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs-cybersec.thalesgroup.com/bundle/latest-cdsp-cm/page/reference/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ThalesGroup
- group: operate
  title: ''
  type: Support
  url: https://supportportal.thalesgroup.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/ciphertrust-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/ciphertrust-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ciphertrust-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ciphertrust-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ciphertrust-security.txt
- group: auth
  title: ''
  type: Security
  url: https://cpl.thalesgroup.com/technical-support/how-to-report-a-security-vulnerability
- group: design
  title: ''
  type: Conformance
  url: conformance/ciphertrust-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cpl.thalesgroup.com/encryption/ciphertrust-manager
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ciphertrust-llms.txt
created: '2026-07-17'
description: CipherTrust Manager is Thales's centralized key- and data-security management platform and the control plane of the CipherTrust Data Security Platform (CDSP). It provides a unified plane for encryption key lifecycle management, secrets management, certificates, tokenization, data discovery, and policy enforcement across on-premises, hybrid, and multi-cloud environments including AWS, Azure, and Google Cloud, with HSM/KMIP integration, Kubernetes and DevSecOps support, role-based access controls, and post-quantum cryptography readiness. Developers and platform teams automate it through a REST API (base path /api/v1, JWT bearer authentication), an official HashiCorp Terraform provider (ThalesGroup/ciphertrust), an Ansible collection, and PowerShell orchestration modules, plus Application Protection SDKs for embedding encryption, key management, and tokenization in apps.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ciphertrust.png
layout: provider
modified: '2026-07-18'
name: CipherTrust
nav: Providers
network: true
overview: 'CipherTrust publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Encryption, Key Management, and Secrets Management.


  CipherTrust''s developer surface includes documentation, API reference, support, authentication, and 13 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 20.9
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 66.7
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 20.9
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ciphertrust/refs/heads/main/screenshots/ciphertrust-2026-07-25T205401.png
security:
- kind: authentication
  name: Ciphertrust Authentication
  slug: ciphertrust-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ciphertrust Domain Security
  slug: ciphertrust-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ciphertrust Vulnerability Disclosure
  slug: ciphertrust-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ciphertrust
tags:
- Company
- Security
- Encryption
- Key Management
- Secrets Management
- Data Protection
- Cryptography
- Tokenization
- Compliance
- KMIP
website: https://cpl.thalesgroup.com/encryption/ciphertrust-manager
---
