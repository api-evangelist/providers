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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.keepersecurity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.keeper.io/home/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.keeper.io/home/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Keeper-Security
- group: company
  title: ''
  type: Blog
  url: https://www.keepersecurity.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.keepersecurity.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.keepersecurity.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://keepersecurity.com/vault/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.keepersecurity.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.keepersecurity.com/privacypolicy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://statuspage.keeper.io/
- group: auth
  title: ''
  type: Security
  url: https://keepersecurity.com/security.html
- group: auth
  title: ''
  type: Compliance
  url: https://trust.keeper.io/
- group: build
  title: ''
  type: Packages
  url: packages/keeper-security-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/keeper-security-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/keeper-security-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/keeper-security-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/keeper-security-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keeper-security-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/keeper-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/keeper-security-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/keeper-security-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/keeper-security-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/keeper-security-llms.txt
created: '2026-07-17'
description: Keeper Security is a zero-knowledge cybersecurity company providing an enterprise password manager, privileged access management (KeeperPAM), secrets management, and dark-web monitoring. For developers, Keeper exposes Keeper Secrets Manager (KSM) — a cloud-based, zero-knowledge platform for securing infrastructure secrets such as API keys, database passwords, and certificates — through a multi-language SDK family (Python, JavaScript/Node, Java/Kotlin, .NET, Go) and the Keeper Commander and KSM command-line interfaces. Keeper does not publish a public REST OpenAPI; integration happens via these SDKs/CLIs, a Commander Service Mode REST API, Terraform providers, and CI/CD plugins. Keeper is FedRAMP High and SOC 2 Type 2 certified with ISO 27001/27017/27018, FIPS 140-3, PCI DSS Level 1, HIPAA, and GDPR compliance.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keeper-security.png
layout: provider
modified: '2026-07-19'
name: Keeper Security
nav: Providers
network: true
overview: 'Keeper Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Secrets Management, Password Manager, and Privileged Access Management.


  Keeper Security''s developer surface includes documentation, engineering blog, support, pricing, CLI, and 19 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 25.4
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keeper-security/refs/heads/main/screenshots/keeper-security-2026-07-25T223552.png
security:
- kind: domain-security
  name: Keeper Security Domain Security
  slug: keeper-security-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Keeper Security Vulnerability Disclosure
  slug: keeper-security-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Keeper Security Trust Center
  slug: keeper-security-trust-center
  summary_line: SOC 2 Type 2, SOC 3, ISO 27001, ISO 27017, ISO 27018, FedRAMP High, GovRAMP High, TX-RAMP, FIPS 140-3, PCI DSS Level 1, HIPAA, GDPR, CCPA, CMMC Level 1, 21 CFR Part 11, ITAR, TrustArc, FSQS-NL
slug: keeper-security
tags:
- Company
- Cybersecurity
- Secrets Management
- Password Manager
- Privileged Access Management
- Zero Knowledge
- Security
- SDK
website: https://www.keepersecurity.com/
---
