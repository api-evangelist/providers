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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 42.3
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: 'Tigris exposes a globally distributed, S3-compatible object storage API. It fulfills over 90% of the AWS S3 API (61/68 operations in Tigris'' published compatibility suite) and works with standard AWS '
  name: Tigris Object Storage (S3 API)
  slug: s3-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/tigris-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.tigrisdata.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tigris-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tigrisdata.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tigrisdata.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.tigrisdata.com/docs/api/s3/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tigrisdata.com/docs/get-started/
- group: operate
  title: ''
  type: Support
  url: https://community.tigrisdata.com/
- group: company
  title: ''
  type: Blog
  url: https://www.tigrisdata.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tigrisdata
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tigrisdata.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://console.storage.dev/signup
- group: start
  title: ''
  type: Login
  url: https://console.storage.dev/signin
- group: start
  title: ''
  type: Console
  url: https://console.storage.dev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tigrisdata.com/docs/legal/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tigrisdata.com/docs/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tigrisdata.com/
- group: other
  title: ''
  type: X
  url: https://x.com/tigrisdata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tigrisdata/
- group: build
  title: ''
  type: Packages
  url: packages/tigris-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tigris-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tigris-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tigris-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tigris-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/tigris-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tigris-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/tigris-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tigris-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tigris-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tigris-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tigris-data-model.yml
created: '2026-07-17'
description: 'Tigris (Tigris Data, founded 2022) is a globally distributed, S3-compatible object storage cloud purpose-built for AI and agent workloads. It offers bottomless object storage with zero egress fees behind a single global endpoint (https://t3.storage.dev), speaking the AWS S3 API natively so existing tools like boto3, aws-cli, rclone, and PyTorch work by swapping the endpoint. Beyond core buckets and objects (up to 5 TB each), Tigris adds agent-native features: copy-on-write bucket forks, point-in-time snapshots, in-place object rename, conditional operations, shadow-bucket migration from AWS S3, IAM access control, an official CLI, first-party SDKs, an MCP server, and published agent skills. Backed by a16z and General Catalyst.'
image: https://www.tigrisdata.com/docs/logo/dark.png
layout: provider
mcp_servers:
- description: ''
  name: tigris-mcp.yml
  slug: tigris-mcpyml
modified: '2026-07-21'
name: Tigris
nav: Providers
network: true
overview: 'Tigris publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Object Storage, Cloud Storage, S3 Compatible, and Storage.


  Tigris'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
random_paper: 46
score:
  band: thin
  composite: 41.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 87.0
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 41.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Tigris Authentication
  slug: tigris-authentication
  summary_line: apiKey/awsSignatureV4 · 1 scheme
- kind: domain-security
  name: Tigris Domain Security
  slug: tigris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tigris Trust Center
  slug: tigris-trust-center
  summary_line: SOC 2
slug: tigris
tags:
- Company
- Object Storage
- Cloud Storage
- S3 Compatible
- Storage
- AI Infrastructure
- Agents
- Data Infrastructure
website: https://www.tigrisdata.com/docs/
---
