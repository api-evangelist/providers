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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.5
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for Tallyfy workflow automation. Organization-scoped resources (/organizations/{org_id}/checklists, /runs, /tasks, ...) with Bearer-token auth (personal, application, or OAuth 2.0 access toke
  name: Tallyfy REST API
  slug: tallyfy-rest-api
artifact_total: 7
asyncapis:
- description: ''
  name: Tallyfy Webhooks
  slug: tallyfy-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://tallyfy.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tallyfy.com/products/pro/integrations/open-api/
- group: docs
  title: ''
  type: Documentation
  url: https://tallyfy.com/products/
- group: docs
  title: ''
  type: APIReference
  url: https://go.tallyfy.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://tallyfy.com/products/pro/integrations/open-api/how-to-integrate-with-tallyfy-using-api/
- group: auth
  title: ''
  type: Authentication
  url: authentication/tallyfy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tallyfy-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tallyfy-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tallyfy-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tallyfy-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tallyfy-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tallyfy-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tallyfy-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/tallyfy-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/tallyfy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tallyfy-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tallyfy-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tallyfy-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tallyfy-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tallyfy-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tallyfy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://tallyfy.com/.well-known/security.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tallyfy
- group: company
  title: ''
  type: Blog
  url: https://tallyfy.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://tallyfy.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://go.tallyfy.com
- group: operate
  title: ''
  type: Support
  url: https://tallyfy.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tallyfy.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tallyfy.com/legal/privacy/
created: '2026-07-17'
description: Tallyfy is workflow and business process management software that lets teams document, launch, track, and automate repeatable processes, SOPs, approvals, and forms without code. Its REST API models templates as "checklists" and processes as "runs" and exposes tasks, form fields (captures), kick-off forms, guests, members, groups, tags, and folders. Developers and AI agents can embed Tallyfy through the REST API, outbound JSON webhooks, a public hosted MCP server (mcp.tallyfy.com), an official Go CLI, and an n8n community node.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tallyfy.png
layout: provider
mcp_servers:
- description: ''
  name: tallyfy-mcp.yml
  slug: tallyfy-mcpyml
modified: '2026-07-21'
name: Tallyfy
nav: Providers
network: true
overview: 'Tallyfy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workflow Automation, Business Process Management, SOPs, and Tasks.


  The Tallyfy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tallyfy''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, engineering blog, pricing, and 22 more developer resources.'
random_paper: 44
rate_limits:
- limit_count: 1
  name: Tallyfy Rate Limits
  slug: tallyfy-rate-limits
score:
  band: developing
  composite: 51.5
  delta: 7.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 73.9
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 44.7
  previous_composite: 44.4
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Tallyfy Authentication
  slug: tallyfy-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Tallyfy Domain Security
  slug: tallyfy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tallyfy Vulnerability Disclosure
  slug: tallyfy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tallyfy
tags:
- Company
- Workflow Automation
- Business Process Management
- SOPs
- Tasks
- Approvals
- Forms
- Process Management
- No-Code
website: https://tallyfy.com
---
