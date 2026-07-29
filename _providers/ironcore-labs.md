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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Assignments between KMS configurations and tenants
  name: IronCore Labs Configuration Assignment API
  slug: ironcore-labs-configuration-assignment-api
- description: KMS configurations from different providers (AWS, Azure, GCP, Thales)
  name: IronCore Labs KMS Configuration API
  slug: ironcore-labs-kms-configuration-api
- description: Label shared between service account configs and tenants. Controls where KMS configurations can be sent.
  name: IronCore Labs Tag API
  slug: ironcore-labs-tag-api
- description: Vendor tenants managed by the Config Broker
  name: IronCore Labs Tenant API
  slug: ironcore-labs-tenant-api
- description: Tenant secrets created by the TSP and stored in the Config Broker
  name: IronCore Labs Tenant Secret API
  slug: ironcore-labs-tenant-secret-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://ironcorelabs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ironcorelabs.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://ironcorelabs.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://ironcorelabs.com/docs/saas-shield/vendor-api/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://ironcorelabs.com/docs/data-control-platform/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://ironcorelabs.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://ironcorelabs.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IronCoreLabs
- group: operate
  title: ''
  type: Support
  url: https://github.com/IronCoreLabs/community
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ironcorelabs.com/trust-center/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ironcorelabs.com/trust-center/privacy/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/ironcore-labs-vendor-bridge-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ironcore-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ironcore-labs-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ironcore-labs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ironcore-labs-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://ironcorelabs.github.io/upptime/
- group: operate
  title: ''
  type: Deprecation
  url: https://ironcorelabs.com/docs/saas-shield/vendor-api/changelog/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ironcore-labs-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ironcore-labs-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ironcore-labs-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/ironcore-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ironcore-labs-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ironcore-labs-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ironcore-labs-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ironcore-labs-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ironcore-labs-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ironcore-labs-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ironcore-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://ironcorelabs.com/trust-center/bug-bounty-program/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ironcore-labs-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://ironcorelabs.com/trust-center/
- group: auth
  title: ''
  type: Compliance
  url: https://ironcorelabs.com/trust-center/
created: '2026-07-17'
description: IronCore Labs builds application-layer encryption tools that keep sensitive data private while it stays usable. Its products include SaaS Shield (tenant-controlled envelope encryption with customer-managed keys / BYOK for multi-tenant SaaS), Cloaked Search (a transparent encrypting proxy for Elasticsearch and OpenSearch), Cloaked AI (encryption of vector embeddings for AI/RAG workloads while preserving similarity search), the Data Control Platform (end-to-end encryption SDKs where the end user holds the key), and an S3 Proxy for per-tenant object encryption. Developers integrate through the unified IronCore Alloy SDK (Rust, Python, Java, Kotlin), the legacy Tenant Security Client (Node.js, Go, PHP), and the self-hosted Vendor API Bridge REST API for programmatic tenant and KMS configuration management.
image: https://ironcorelabs.com/images/blog/generic-ironcore-graphic-hero.jpg
layout: provider
mcp_servers:
- description: ''
  name: ironcore-labs-mcp.yml
  slug: ironcore-labs-mcpyml
modified: '2026-07-19'
name: IronCore Labs
nav: Providers
network: true
overview: 'IronCore Labs publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Configuration Assignment API, KMS Configuration API, Tag API, and 2 more. Tagged areas include Company, Encryption, Data Privacy, Security, and Application-Layer Encryption.


  IronCore Labs'' developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, authentication, and 27 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 54.6
  delta: -3.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 53.8
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 57.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ironcore-labs/refs/heads/main/screenshots/ironcore-labs-2026-07-25T222920.png
security:
- kind: authentication
  name: Ironcore Labs Authentication
  slug: ironcore-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ironcore Labs Domain Security
  slug: ironcore-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ironcore Labs Vulnerability Disclosure
  slug: ironcore-labs-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ironcore Labs Trust Center
  slug: ironcore-labs-trust-center
  summary_line: SOC 2
slug: ironcore-labs
tags:
- Company
- Encryption
- Data Privacy
- Security
- Application-Layer Encryption
- Key Management
- Cryptography
- AI
- Vector Database
- SaaS
website: https://ironcorelabs.com/
---
