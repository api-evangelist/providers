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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.1
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Craft Connect exposes a user's Craft Space, Daily Notes, tasks, and selected documents over REST as part of the Imagine platform, so tools like Apple Shortcuts, n8n, Zapier, Replit, and custom code ca
  name: Craft Connect API
  slug: craft-connect-api
- description: The Craft eXtension API is an official TypeScript/JavaScript SDK (@craftdocs/craft-extension-api) for building extensions that run inside the Craft app to read and modify document content, blocks, and
  name: Craft eXtension API
  slug: craft-extension-api
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/craftdocs/craft-extension-api/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/craftdocs/craft-extension-api/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.craft.do/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.craft.do/imagine
- group: docs
  title: ''
  type: Documentation
  url: https://support.craft.do/
- group: docs
  title: ''
  type: APIReference
  url: https://connect.craft.do/api-docs
- group: operate
  title: ''
  type: Support
  url: https://support.craft.do/
- group: company
  title: ''
  type: Blog
  url: https://www.craft.do/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/craftdocs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.craft.do/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.craft.do/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.craft.do/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.craft.do/whats-new
- group: operate
  title: ''
  type: StatusPage
  url: https://craftdocs.statuspage.io/
- group: auth
  title: ''
  type: Compliance
  url: https://www.craft.do/security
- group: auth
  title: ''
  type: Security
  url: https://www.craft.do/security/responsible-disclosure
- group: agent
  title: ''
  type: MCPServer
  url: mcp/craft-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/craft-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/craft-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/craft-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/craft-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/craft-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/craft-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/craft-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/craft-trust-center.yml
created: '2026-07-17'
description: 'Craft (Craft Docs Ltd.) is a consumer and team productivity app that combines notes, documents, tasks, and daily planning in a single cross-platform workspace for macOS, iOS, iPadOS, Windows, and web. Beyond the end-user app, Craft exposes a developer surface through its "Imagine" platform: an official eXtension API (a TypeScript/JavaScript SDK, @craftdocs/craft-extension-api, for building extensions that run inside Craft), a Craft Connect REST API that exposes a user''s Space, Daily Notes, tasks, and selected documents, and an official remote MCP server that connects Craft to Claude, ChatGPT, Cursor, and other MCP clients. Documentation is published on a Mintlify help center with a machine-readable llms.txt, and the company states SOC 2, ISO 27001, and GDPR compliance.'
image: https://github.com/craftdocs.png
layout: provider
mcp_servers:
- description: ''
  name: craft-mcp.yml
  slug: craft-mcpyml
modified: '2026-07-18'
name: craft
nav: Providers
network: true
overview: 'craft publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Productivity, Notes, and Documents.


  craft''s developer surface includes documentation, API reference, support, engineering blog, pricing, changelog, and 19 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 33.2
  delta: -0.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 33.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/craft/refs/heads/main/screenshots/craft-2026-07-25T210634.png
security:
- kind: domain-security
  name: Craft Domain Security
  slug: craft-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Craft Vulnerability Disclosure
  slug: craft-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Craft Trust Center
  slug: craft-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: craft
tags:
- Company
- Consumer
- Productivity
- Notes
- Documents
- Note Taking
- Tasks
- Collaboration
- Writing
- AI
- MCP
- Extensions
website: https://www.craft.do/
---
