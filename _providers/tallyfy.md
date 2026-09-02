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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-09-01'
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
- description: 'Official public, hosted Tallyfy MCP server. Every tool calls the public Tallyfy REST API on behalf of the authenticated user, so an assistant only ever sees data the signed-in user is allowed to see. '
  name: Tallyfy MCP Server
  slug: tallyfy-mcp-server
modified: '2026-07-21'
name: Tallyfy
nav: Providers
network: true
overview: 'Tallyfy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workflow-Automation, Business Process Management, SOPs, and Task.


  The Tallyfy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tallyfy''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, engineering blog, pricing, and 22 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 1
  name: Tallyfy Rate Limits
  slug: tallyfy-rate-limits
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 45.5
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tallyfy/refs/heads/main/screenshots/tallyfy-2026-08-17T082246.png
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
- Workflow-Automation
- Business Process Management
- SOPs
- Task
- Approvals
- Forms
- Process Management
- No-Code
website: https://tallyfy.com
---
