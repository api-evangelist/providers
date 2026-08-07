---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 68.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Altoira Agentic Access
  operation_count: 17
  slug: altoira-agentic-access
  summary_line: 17 operations · 11 acting
api_count: 1
apis:
- description: Alto's partner REST API for investment platforms and issuers. Covers the OAuth handoff that connects an investor's Alto IRA to a partner platform, offering creation and updates, offering document uplo
  name: AltoIRA.com API
  slug: altoiracom-api
artifact_total: 9
asyncapis:
- description: Alto pushes investment-lifecycle events to a Platform Partner's registered webhook endpoint so the partner can track an investor's progress through the Direction of Investment (DOI), funding and any p
  name: Alto Investment Status Webhooks
  slug: altoira-investments-asyncapi
- description: ''
  name: Altoira Investments Webhooks
  slug: altoira-investments-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.altoira.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://readme.altoira.com/
- group: docs
  title: ''
  type: Documentation
  url: https://readme.altoira.com/docs/understand-the-oauth-process-to-alto
- group: docs
  title: ''
  type: APIReference
  url: https://readme.altoira.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://readme.altoira.com/docs/understand-the-oauth-process-to-alto
- group: operate
  title: ''
  type: Support
  url: https://www.altoira.com/help-center
- group: company
  title: ''
  type: Blog
  url: https://www.altoira.com/insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AltoIRA
- group: commercial
  title: ''
  type: Pricing
  url: https://www.altoira.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.altoira.com/register
- group: start
  title: ''
  type: Login
  url: https://app.altoira.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.altoira.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.altoira.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.altoira.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.altoira.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/altoira-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/altoira-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/altoira-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/altoira-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/altoira-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/altoira-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/altoira-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/altoira-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/altoira-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/altoira-sandbox.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/altoira-agentic-access.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/altoira-partner-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/altoira-partner-api-overlay.yaml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/altoira-investments-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/altoira-investments-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/altoira-problem-types.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/altoira-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/altoira-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-06'
description: Alto (AltoIRA) is a Nashville-based self-directed IRA platform that lets everyday investors hold alternative assets — private equity, venture funds, startups, real estate, farmland, private credit and cryptocurrency — inside tax-advantaged Traditional, Roth and SEP retirement accounts. Alto Trust Company acts as the IRA custodian and Alto Securities, LLC (FINRA/SIPC) operates the Alto Marketplace of curated private-market offerings. Alto reports custody of roughly $2B in assets for about 30,000 self-directed IRA investors and support for more than 2,500 issuers who have raised capital on the platform. For issuers and investment platforms, Alto publishes a partner REST API (the "AltoIRA.com API") on a ReadMe developer hub that covers OAuth investor handoff, offering creation, document upload, investor invitation, investment retrieval, refunds, cancellations, distributions and capital calls, plus an investment-status webhook feed.
image: https://cdn.prod.website-files.com/662048df2bce7baa72aab3f3/662ae161e60cc17317200006_Altologo.svg
layout: provider
mcp_servers:
- description: ''
  name: altoira-mcp.yml
  slug: altoira-mcpyml
modified: '2026-08-06'
name: AltoIRA
nav: Providers
network: true
overview: 'AltoIRA publishes 1 API on the [APIs.io](https://apis.io/) network: AltoIRA.com API. Tagged areas include Company, Financial Services, Retirement, Self-Directed IRA, and Alternative Investments.


  The AltoIRA catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  AltoIRA''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
random_paper: 70
scopes:
- name: Altoira Scopes
  scope_count: 0
  slug: altoira-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 55.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 58.8
    developer_ergonomics: 73.9
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 28.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Altoira Authentication
  slug: altoira-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Altoira Domain Security
  slug: altoira-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Altoira Trust Center
  slug: altoira-trust-center
  summary_line: trust center published
slug: altoira
tags:
- Company
- Financial Services
- Retirement
- Self-Directed IRA
- Alternative Investments
- Private Markets
- Fintech
- Custody
- Cryptocurrency
- Wealth Management
- Investing
- Capital Raising
website: https://www.altoira.com/
---
