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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Auth API API from Serval — 1 operation(s) for auth api.
  name: Serval Auth API API
  slug: serval-auth-api-api
artifact_total: 9
asyncapis:
- description: ''
  name: Serval Webhooks
  slug: serval-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Spec Auth API API
  slug: open-serval-auth-api-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/serval-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.serval.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.serval.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.serval.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.serval.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.serval.com/sections/documentation/overview/welcome
- group: operate
  title: ''
  type: Support
  url: https://docs.serval.com/sections/documentation/platform/support
- group: company
  title: ''
  type: Blog
  url: https://www.serval.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.serval.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.serval.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.serval.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.serval.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ServalHQ
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/serval-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.serval.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.serval.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/serval-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/serval-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/serval-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/serval-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/serval-lifecycle.yml
created: '2026-07-17'
description: Serval is an AI-native IT service management (ITSM) platform for modern teams. It pairs an AI help-desk agent that resolves employee requests in Slack, Microsoft Teams, email, and a web portal with a separate admin-facing automation agent (Catalyst) that turns intent into deterministic, version-controlled TypeScript workflows. Serval covers ticketing, knowledge base, journeys (onboarding/offboarding), just-in-time access management with approval flows, campaigns, SLAs, and 130+ integrations. Its public REST API (v2), hosted MCP server, CLI, and webhooks let teams manage tickets, workflows, access, users, and audit logs programmatically, with US and EU data-residency regions.
image: https://framerusercontent.com/images/V6k6fFCAJ2d3ZHM9P4chDQnDbY.png
layout: provider
mcp_servers:
- description: ''
  name: Serval MCP Server
  slug: serval-mcp-server
modified: '2026-07-21'
name: Serval
nav: Providers
network: true
overview: 'Serval publishes 1 API on the [APIs.io](https://apis.io/) network: Auth API API. Tagged areas include Company, IT Service Management, ITSM, Help Desk, and Workflow-Automation.


  The Serval catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Serval''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 14 more developer resources.'
random_paper: 2
scopes:
- name: Serval Scopes
  scope_count: 1
  slug: serval-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 4.5
    contract_quality: 59.9
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 47.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/serval/refs/heads/main/screenshots/serval-2026-08-17T081819.png
security:
- kind: authentication
  name: Serval Authentication
  slug: serval-authentication
  summary_line: http-basic/http-bearer/oauth2 · 0 schemes
- kind: domain-security
  name: Serval Domain Security
  slug: serval-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Serval Trust Center
  slug: serval-trust-center
  summary_line: trust center published
slug: serval
tags:
- Company
- IT Service Management
- ITSM
- Help Desk
- Workflow-Automation
- AI Agents
- Access Management
- Employee Support
- Ticketing
website: https://www.serval.com/
---
