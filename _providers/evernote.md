---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.8
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The Evernote Cloud API (EDAM) is a Thrift-based service exposing UserStore and NoteStore operations to create, read, update, search, share, and synchronize notes, notebooks, tags, and resources in a u
  name: Evernote Cloud API
  slug: evernote-cloud-api
artifact_total: 7
asyncapis:
- description: ''
  name: Evernote Webhooks
  slug: evernote-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://evernote.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.evernote.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.evernote.com/doc/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.evernote.com/doc/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.evernote.com/doc/start/python.php
- group: start
  title: ''
  type: SignUp
  url: https://dev.evernote.com/get-started/
- group: operate
  title: ''
  type: Support
  url: https://help.evernote.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://evernote.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evernote
- group: commercial
  title: ''
  type: Pricing
  url: https://evernote.com/compare-plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://evernote.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://evernote.com/privacy/policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.evernote.com/
- group: operate
  title: ''
  type: RateLimits
  url: https://dev.evernote.com/doc/articles/rate_limits.php
- group: build
  title: ''
  type: Packages
  url: packages/evernote-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/evernote-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/evernote-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/evernote-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/evernote-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/evernote-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/evernote-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/evernote-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://evernote.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/evernote-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/evernote-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/evernote-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evernote-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/evernote-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evernote-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/evernote-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/evernote-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/evernote-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/evernote-data-model.yml
created: '2026-07-17'
description: Evernote is a cross-platform note-taking, organization, and task-management application operated by Bending Spoons. It lets people capture notes, web clips, images, audio, and documents, sync them across devices, and search across their knowledge base. For developers, Evernote publishes the Evernote Cloud API — a Thrift-based (EDAM) service exposing UserStore and NoteStore operations for creating, reading, searching, sharing, and synchronizing notes, notebooks, tags, and resources. Authentication is via three-legged OAuth 1.0a or long-lived developer tokens, with a sandbox environment for development. Official SDKs cover Python, Java, Ruby, JavaScript/Node, PHP, iOS, Android, and C#. The classic EDAM API and SDKs are deprecated and no longer actively developed; Evernote is now building a Model Context Protocol (MCP) server to connect AI tools to notes.
image: https://evernote.com/img/evernote-logo.png
layout: provider
mcp_servers:
- description: ''
  name: evernote-mcp.yml
  slug: evernote-mcpyml
modified: '2026-07-19'
name: evernote
nav: Providers
network: true
overview: 'evernote publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Note Taking, Productivity, Knowledge Management, and Notes.


  The evernote catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  evernote''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, pricing, and 26 more developer resources.'
random_paper: 81
score:
  band: strong
  composite: 56.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 73.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 47.4
  previous_composite: 56.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evernote/refs/heads/main/screenshots/evernote-2026-07-25T213733.png
security:
- kind: authentication
  name: Evernote Authentication
  slug: evernote-authentication
  summary_line: oauth1/developer-token · 2 schemes
- kind: domain-security
  name: Evernote Domain Security
  slug: evernote-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Evernote Vulnerability Disclosure
  slug: evernote-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Evernote Trust Center
  slug: evernote-trust-center
  summary_line: ISO 27001, Google CASA Tier 2 (OWASP ASVS)
slug: evernote
tags:
- Company
- Note Taking
- Productivity
- Knowledge Management
- Notes
- Content
- SaaS
- Sync
website: https://evernote.com
---
