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
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: Manage API keys (also called API tokens) used to authenticate Control Plane API requests. Distinct from disk tokens.
  name: Archil API Tokens API
  slug: archil-api-tokens-api
- description: Manage authorized users on disks
  name: Archil Disk Users API
  slug: archil-disk-users-api
- description: Create, read, update, and delete disks
  name: Archil Disks API
  slug: archil-disks-api
- description: Run commands on a disk without provisioning compute
  name: Archil Serverless Execution API
  slug: archil-serverless-execution-api
artifact_total: 13
collections:
- collection_type: postman
  name: Archil Control Plane API Tokens API
  slug: postman-archil-api-tokens-api
- collection_type: postman
  name: Archil Control Plane API Tokens Disk Users API
  slug: postman-archil-disk-users-api
- collection_type: postman
  name: Archil Control Plane API Tokens Disks API
  slug: postman-archil-disks-api
- collection_type: postman
  name: Archil Control Plane API Tokens Serverless Execution API
  slug: postman-archil-serverless-execution-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/archil/overview
- group: auth
  title: ''
  type: TrustCenter
  url: security/archil-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://archil.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.archil.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.archil.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.archil.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.archil.com/getting-started/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://console.archil.com
- group: operate
  title: ''
  type: Support
  url: mailto:support@archil.com
- group: company
  title: ''
  type: Blog
  url: https://archil.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://archil.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://archil.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://archil.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/archil-data
- group: operate
  title: ''
  type: StatusPage
  url: https://status.archil.com
- group: auth
  title: ''
  type: Compliance
  url: https://docs.archil.com/details/security
- group: auth
  title: ''
  type: Security
  url: https://docs.archil.com/details/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/archil-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/archil-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/archil-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/archil-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/archil-mcp.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/archil-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/archil-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/archil-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/archil-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/archil-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/archil-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Archil is the cloud filesystem for AI. It turns an existing object-storage bucket (Amazon S3, Google Cloud Storage, Cloudflare R2, Azure Blob, MinIO, Wasabi, Backblaze B2, DigitalOcean Spaces) into an unlimited, POSIX-compatible local disk that thousands of machines can mount at once — live, in place, and faster than local disk. A single multi-tenant "disk" caches active data in a high-speed layer, supports copy-on-write branches and checkpoints for isolated agent and CI fan-out, and can run serverless bash and parallel grep directly against the data with no separate sandbox. Archil exposes a REST Control Plane API for managing disks, disk users, API tokens, and serverless execution, plus first-party TypeScript and Python SDKs, a `disk` CLI, a Linux `archil` mount CLI, a Kubernetes CSI driver, a Terraform provider, and an S3-compatible HTTP API. Founded 2024, backed by Felicis, Y Combinator, General Catalyst, Peak XV, and Standard Capital. Added to the API Evangelist network
  from the Felicis portfolio and enriched by the pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/archil.png
layout: provider
mcp_servers:
- description: ''
  name: archil-mcp.yml
  slug: archil-mcpyml
modified: '2026-07-18'
name: Archil
nav: Providers
network: true
overview: 'Archil publishes 4 APIs on the [APIs.io](https://apis.io/) network, including API Tokens API, Disk Users API, Disks API, and 1 more. Tagged areas include Company, Cloud Storage, Filesystem, Object Storage, and Artificial Intelligence.


  Archil''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, pricing, and 22 more developer resources.'
random_paper: 74
score:
  band: strong
  composite: 59.1
  delta: -1.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.9
    developer_ergonomics: 73.4
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 47.4
  previous_composite: 60.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/archil/refs/heads/main/screenshots/archil-2026-07-25T201028.png
security:
- kind: authentication
  name: Archil Authentication
  slug: archil-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Archil Domain Security
  slug: archil-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Archil Vulnerability Disclosure
  slug: archil-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Archil Trust Center
  slug: archil-trust-center
  summary_line: SOC 2 Type II
slug: archil
tags:
- Company
- Cloud Storage
- Filesystem
- Object Storage
- Artificial Intelligence
- Infrastructure
- Developer Tools
- Serverless
- Data
- S3
website: https://archil.com
---
