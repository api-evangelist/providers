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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 67.3
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Instabase Agentic Access
  operation_count: 27
  slug: instabase-agentic-access
  summary_line: 27 operations · 16 acting
api_count: 6
apis:
- description: The Audit API from Instabase — 1 operation(s) for audit.
  name: Instabase Audit API
  slug: instabase-audit-api
- description: The Batches API from Instabase — 8 operation(s) for batches.
  name: Instabase Batches API
  slug: instabase-batches-api
- description: The Files API from Instabase — 1 operation(s) for files.
  name: Instabase Files API
  slug: instabase-files-api
- description: The Jobs API from Instabase — 1 operation(s) for jobs.
  name: Instabase Jobs API
  slug: instabase-jobs-api
- description: The Runs API from Instabase — 4 operation(s) for runs.
  name: Instabase Runs API
  slug: instabase-runs-api
- description: The Secrets API from Instabase — 1 operation(s) for secrets.
  name: Instabase Secrets API
  slug: instabase-secrets-api
artifact_total: 13
asyncapis:
- description: ''
  name: Instabase Webhooks
  slug: instabase-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.instabase.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.instabase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.instabase.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.instabase.com/api-sdk/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.instabase.com/overview/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.instabase.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.instabase.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instabase
- group: start
  title: ''
  type: SignUp
  url: https://aihub.instabase.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.instabase.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.instabase.com/
- group: build
  title: ''
  type: SDKs
  url: packages/instabase-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/instabase-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/instabase-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/instabase-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/instabase-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/instabase-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/instabase-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.instabase.com/policies/upgrades.md
- group: design
  title: ''
  type: Conformance
  url: conformance/instabase-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.instabase.com/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/instabase-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/instabase-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/instabase-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/instabase-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instabase-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/instabase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.instabase.com/
created: '2026-07-17'
description: Instabase is an agentic automation platform that transforms complex, document-heavy workflows using AI. Its AI Hub product uses large language models and packet-aware AI agents to extract, classify, validate, and reason over unstructured document packets (PDFs, images, spreadsheets, emails, scans, and more), turning them into structured, verifiable intelligence. AI Hub exposes a REST API and Python SDK for creating file batches, running automation apps and production deployments, reading and writing workspace files, and managing secrets, with industry solutions for financial services, insurance, healthcare, and the public sector. Instabase is venture-backed (a16z, Greylock, Index Ventures).
image: https://cdn.prod.website-files.com/6883b569dca0edf626a1fce5/68cdbf2b866f068b4585e5ea_Open%20graph.png
layout: provider
mcp_servers:
- description: ''
  name: instabase-mcp.yml
  slug: instabase-mcpyml
modified: '2026-07-19'
name: Instabase
nav: Providers
network: true
overview: 'Instabase publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audit API, Batches API, Files API, and 3 more. Tagged areas include Company, Intelligent Document Processing, Document AI, Artificial Intelligence, and Machine Learning.


  The Instabase catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Instabase''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 22 more developer resources.'
random_paper: 36
score:
  band: developing
  composite: 58.3
  delta: 2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.9
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 56.3
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 69.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Instabase Authentication
  slug: instabase-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Instabase Domain Security
  slug: instabase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Instabase Vulnerability Disclosure
  slug: instabase-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Instabase Trust Center
  slug: instabase-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: instabase
tags:
- Company
- Intelligent Document Processing
- Document AI
- Artificial Intelligence
- Machine Learning
- Automation
- Data Extraction
- LLM
- Financial Services
- Insurance
website: https://www.instabase.com/
---
