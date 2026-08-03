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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: REST API for Qiniu Kodo object storage — bucket administration, object upload/download, stat/copy/move/delete, lifecycle and CORS rules, async fetch, and CDN prefetch/refresh. S3-compatible surface av
  name: Object Storage (Kodo)
  slug: object-storage-kodo
- description: Identity and access management API — IAM sub-users, AK/SK keypairs, groups, and permission policies scoping services/actions/resources.
  name: IAM
  slug: iam
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://qiniu.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.qiniu.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.qiniu.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.qiniu.com/kodo/1731/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.qiniu.com/kodo/1231/upload-process
- group: operate
  title: ''
  type: Support
  url: https://developer.qiniu.com/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qiniu
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qiniu.com/prices
- group: start
  title: ''
  type: Login
  url: https://sso.qiniu.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qiniu.com/user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qiniu.com/privacy-right
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qiniu-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/qiniu-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/qiniu-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/qiniu-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qiniu-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qiniu-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qiniu-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qiniu-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qiniu-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qiniu-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qiniu-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/qiniu-upload-and-manage-object.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/qiniu-provision-iam-user.md
created: '2026-07-17'
description: Qiniu Cloud (七牛云) is a data-centric cloud infrastructure platform for storing, delivering, processing, and computing over large-scale unstructured data. Its core products are Object Storage (Kodo), CDN and full-site acceleration (DCDN), live and on-demand audio/video PaaS, intelligent media processing (Dora), and AI large-model inference and agent workflows. Developers integrate over REST APIs authenticated with AccessKey/SecretKey HMAC signatures, first-party SDKs in a dozen languages, the qshell CLI, and an official MCP server. This profile was seeded as a portfolio company of Qiming Venture Partners and enriched from Qiniu's public developer surface (developer.qiniu.com, github.com/qiniu).
image: https://www.qiniu.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: qiniu-mcp.yml
  slug: qiniu-mcpyml
modified: '2026-07-20'
name: Qiniu Cloud
nav: Providers
network: true
overview: 'Qiniu Cloud publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Object Storage, CDN, and Media Processing.


  Qiniu Cloud''s developer surface includes documentation, API reference, getting-started guide, support, pricing, CLI, authentication, and 17 more developer resources.'
random_paper: 75
score:
  band: thin
  composite: 33.4
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 73.4
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 33.4
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Qiniu Authentication
  slug: qiniu-authentication
  summary_line: apiKey/hmac-signature · 3 schemes
- kind: domain-security
  name: Qiniu Domain Security
  slug: qiniu-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: qiniu
tags:
- Company
- Cloud
- Object Storage
- CDN
- Media Processing
- Live Streaming
- IAM
- SDK
- AI
- China
website: https://qiniu.com
---
