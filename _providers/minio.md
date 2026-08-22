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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.6
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: S3-compatible object storage REST API implementing Amazon S3 bucket and object operations (put/get/list/delete objects, multipart uploads, versioning, object locking, lifecycle, replication), authenti
  name: MinIO S3-Compatible API
  slug: minio-s3-compatible-api
- description: 'Administrative API (madmin) for managing MinIO/AIStor clusters: users, groups, canned and IAM policies, service accounts, healing, cluster info, configuration, and service restart.'
  name: MinIO Admin API
  slug: minio-admin-api
artifact_total: 8
asyncapis:
- description: ''
  name: Minio Bucket Notifications Webhooks
  slug: minio-bucket-notifications-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/minio-trust-center.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://min.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://min.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://min.io/product/s3-compatibility
- group: start
  title: ''
  type: GettingStarted
  url: https://min.io/docs/minio/linux/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/minio
- group: company
  title: ''
  type: Blog
  url: https://blog.min.io
- group: commercial
  title: ''
  type: Pricing
  url: https://min.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://subnet.min.io
- group: start
  title: ''
  type: SignUp
  url: https://subnet.min.io/login
- group: build
  title: ''
  type: Packages
  url: packages/minio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/minio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/minio-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/minio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/minio-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/minio-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/minio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/minio-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/minio-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/minio-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/minio-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/minio-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/minio-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/minio-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/minio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/minio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/minio-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.min.io/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/minio-bucket-notifications-webhooks.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.min.io/legal/aistor-free-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.min.io/legal/privacy-policy
created: '2026-07-17'
description: MinIO is a high-performance, S3-compatible object storage system built for large-scale AI, analytics, and cloud-native data infrastructure. Its API is a drop-in implementation of the Amazon S3 REST API (bucket and object operations, multipart uploads, versioning, object locking / WORM retention, lifecycle policies, replication, and encryption), authenticated with AWS Signature Version 4 using access-key/secret-key pairs. Alongside the S3 data API, MinIO ships an Admin API (madmin) for cluster, user, policy, and service management. It is distributed as open-source software and as the commercial AIStor product, deployed on Kubernetes via an operator and Helm charts, and driven through first-party SDKs for Go, Python, Java, JavaScript, .NET, C++, and Rust plus the `mc` command-line client.
image: https://github.com/minio.png
layout: provider
mcp_servers:
- description: ''
  name: minio-mcp.yml
  slug: minio-mcpyml
modified: '2026-07-20'
name: MinIO
nav: Providers
network: true
overview: 'MinIO publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Object Storage, Storage, S3 Compatible, Cloud Native, and Kubernetes.


  The MinIO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MinIO''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, signup flow, and 24 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 49.6
  delta: -5.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 55.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/minio/refs/heads/main/screenshots/minio-2026-08-07T172955.png
security:
- kind: authentication
  name: Minio Authentication
  slug: minio-authentication
  summary_line: signature-v4/sts/ldap/oidc · 4 schemes
- kind: domain-security
  name: Minio Domain Security
  slug: minio-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Minio Vulnerability Disclosure
  slug: minio-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Minio Trust Center
  slug: minio-trust-center
  summary_line: ISO 27001
slug: minio
tags:
- Object Storage
- Storage
- S3 Compatible
- Cloud Native
- Kubernetes
- Data Infrastructure
- AI Storage
- Company
website: https://min.io/docs
---
