---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 60.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Clozd Agentic Access
  operation_count: 12
  slug: clozd-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 4
apis:
- description: Current version of the Clozd public Data API. Read programs, competitors, deals (with participants, products, published feedback responses and full transcripts), and touchpoints; import deals and touc
  name: Clozd Data API v3.0
  slug: clozd-data-api-v30
- description: Prior version of the Clozd public Data API. Get a paged list of deals for a program, get a single deal with details, and import deals with participants. Superseded by v3.0, which adds programs, compet
  name: Clozd Data API v2.0
  slug: clozd-data-api-v20
- description: Original version of the Clozd public Data API, limited to a single deal-and-participant import operation for pushing CRM opportunity data into a Clozd program. Superseded by v2.0 and v3.0. Authenticat
  name: Clozd Data API v1.0
  slug: clozd-data-api-v10
- description: Hosted remote Model Context Protocol server exposing 19 documented read tools over Clozd win-loss data — programs, deals, responses, response summaries, transcripts, decision drivers and categories, d
  name: Clozd MCP Server
  slug: clozd-mcp-server
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clozd-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.clozd.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.clozd.com/public-api/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://help.clozd.com/hc/en-us/articles/9948957669659-API-Imports-Exports
- group: docs
  title: ''
  type: APIReference
  url: https://app.clozd.com/public-api/docs/?urls.primaryName=v3.0
- group: start
  title: ''
  type: GettingStarted
  url: https://help.clozd.com/hc/en-us/articles/9948957669659-API-Imports-Exports
- group: operate
  title: ''
  type: Support
  url: https://help.clozd.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.clozd.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.clozd.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Clozd
- group: start
  title: ''
  type: SignUp
  url: https://www.clozd.com/talk-with-us
- group: start
  title: ''
  type: Login
  url: https://app.clozd.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clozd.com/privacy/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clozd.com/privacy/policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.clozd.com/privacy/gdpr
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.clozd.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clozd-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clozd-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clozd-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clozd-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/clozd-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clozd-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clozd-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clozd-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clozd-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clozd-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clozd-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clozd-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/clozd-conventions.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: 'Clozd is a Lehi, Utah based decision-intelligence and win-loss analysis platform that collects structured buyer feedback — through human-led live interviews, AI-assisted Flex interviews, and autonomous Flow interviews — and turns it into decision drivers, competitor sentiment, win rates, and verbatim buyer quotes for sales, marketing, product, and customer-success teams. The platform integrates with Salesforce, HubSpot, Microsoft Dynamics, Gong, Slack, Calendly, Outlook, and Gmail, and exposes two public programmatic surfaces: the versioned Clozd Data API (v1/v2/v3) documented with OpenAPI 3.0.3 and Swagger UI at app.clozd.com for importing deals and participants and exporting programs, deals, touchpoints, responses, transcripts, and competitors; and a hosted, OAuth 2.0 protected Model Context Protocol server at mcp.clozd.com that gives Claude, ChatGPT, Cursor, Copilot, Windsurf, Antigravity, and Gemini CLI direct tool access to the same win-loss data.'
image: https://cdn.prod.website-files.com/602c29edc35660e6c913f956/65a18029f28b360a5bc33674_Group%2011337.png
layout: provider
mcp_servers:
- description: ''
  name: clozd-mcp.yml
  slug: clozd-mcpyml
modified: '2026-08-04'
name: Clozd
nav: Providers
network: true
overview: 'Clozd publishes 3 APIs on the [APIs.io](https://apis.io/) network: Data API v3.0, Data API v2.0, and Data API v1.0. Tagged areas include win-loss-analysis, customer-feedback, decision-intelligence, sales-intelligence, and market-research.


  Clozd''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 23 more developer resources.'
random_paper: 88
scopes:
- name: Clozd Scopes
  scope_count: 5
  slug: clozd-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: developing
  composite: 51.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.1
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 5.3
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 33.3
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Clozd Authentication
  slug: clozd-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Clozd Domain Security
  slug: clozd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clozd Vulnerability Disclosure
  slug: clozd-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Clozd Trust Center
  slug: clozd-trust-center
  summary_line: ISO 27001, ISO 27701, SOC 2 Type II
slug: clozd
tags:
- win-loss-analysis
- customer-feedback
- decision-intelligence
- sales-intelligence
- market-research
- competitive-intelligence
- voice-of-customer
- revenue-intelligence
- saas
- mcp
- agent-native
website: https://www.clozd.com/
---
