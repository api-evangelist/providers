---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 28.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The 1up MCP Server is a cloud-hosted Model Context Protocol server that lets an AI assistant work directly against a 1up workspace — query the knowledge base, search and edit the Q&A library, upload a
  name: 1up MCP Server
  slug: 1up-mcp-server
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://1up.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://help.1up.ai/en/
- group: docs
  title: ''
  type: APIReference
  url: https://help.1up.ai/en/articles/14304740-mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://help.1up.ai/en/articles/13002972-quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://1up.ai/support
- group: company
  title: ''
  type: Blog
  url: https://1up.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://1up.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.1up.ai/signup
- group: start
  title: ''
  type: Login
  url: https://app.1up.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://1up.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://1up.ai/legal/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/1up-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/1up-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/1up-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/1up-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/1up-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/1up-cli.yml
- group: design
  title: ''
  type: Components
  url: components/1up-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/1up-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/1up-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/1up-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/1up-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/1up-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/1up-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/1up-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1up-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/1up-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/1up-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/1up-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://1up.ai/security
- group: company
  title: ''
  type: Newsroom
  url: https://1up.ai/news
created: '2026-09-05'
description: '1up (1up Corp, 1up.ai) is a New York City based AI knowledge-automation company whose "Answer Engine" generates source-grounded answers for go-to-market teams. The platform connects approved knowledge sources — Confluence, Notion, Google Drive, OneDrive, SharePoint, Box, Dropbox, Egnyte, Salesforce, Highspot, Seismic, Zendesk, Gong, GitBook, GitHub and public websites — into a workspace-isolated knowledge base, then uses it to auto-complete RFPs, DDQs, security questionnaires and vendor assessments in Excel, Word, PDF, CSV and web portals such as OneTrust, Panorays and Whistic. 1up''s public machine surface is an MCP server rather than a REST developer program: a cloud-hosted, OAuth 2.1 protected Model Context Protocol endpoint at https://mcp.1up.ai/mcp exposing 31 documented tools across the Q&A library, questionnaires, knowledge base, knowledge groups and workspace, sold as its own $50/month pricing tier billed at $0.05 per answered question. Founded in 2021 by the founding
  team behind identity-security vendor HYPR, 1up has raised $8.5M from Upfront Ventures and Lightbank.'
image: https://cdn.prod.website-files.com/69c22ac6beee399088a918e7/69e1a4a063f3ef04164ea555_4bdbffc375cfff493276c814781ae9b9_OG.jpg
layout: provider
mcp_servers:
- description: Model Context Protocol server for the 1up knowledge-management platform. Lets an MCP client manage questionnaires, the Q&A library, knowledge-base documents and knowledge groups inside a 1up workspace
  name: 1up MCP Server
  slug: 1up-mcp-server
modified: '2026-09-05'
name: 1up
nav: Providers
network: true
overview: '1up publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Sales Enablement, Knowledge Management, and RFP Automation.


  1up''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: 1Up Plans Pricing
  plan_count: 6
  slug: 1up-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: 1Up Rate Limits
  slug: 1up-rate-limits
scopes:
- name: 1Up Scopes
  scope_count: 4
  slug: 1up-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 1Up Authentication
  slug: 1up-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: 1Up Domain Security
  slug: 1up-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: 1Up Trust Center
  slug: 1up-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, GDPR
slug: 1up
tags:
- Company
- Artificial Intelligence
- Sales Enablement
- Knowledge Management
- RFP Automation
- Security Questionnaires
- Model Context Protocol
- Agents
- SaaS
- Revenue Operations
website: https://1up.ai/
---
