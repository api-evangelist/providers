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
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 60.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Clozd Agentic Access
  operation_count: 12
  slug: clozd-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 8
apis:
- description: Hosted remote Model Context Protocol server exposing 19 documented read tools over Clozd win-loss data — programs, deals, responses, response summaries, transcripts, decision drivers and categories, d
  name: Clozd MCP Server
  slug: clozd-mcp-server
- description: The /programs API from Clozd — 1 operation(s) for /programs.
  name: Clozd /programs API
  slug: clozd-programs-api
- description: The /programs/:program_id/competitors API from Clozd — 1 operation(s) for /programs/:program_id/competitors.
  name: Clozd /programs/:program Id/competitors API
  slug: clozd-programs-program-id-competitors-api
- description: The /programs/:program_id/deals API from Clozd — 1 operation(s) for /programs/:program_id/deals.
  name: Clozd /programs/:program Id/deals API
  slug: clozd-programs-program-id-deals-api
- description: The /programs/:program_id/deals/:deal_id API from Clozd — 1 operation(s) for /programs/:program_id/deals/:deal_id.
  name: Clozd /programs/:program Id/deals/:deal ID API
  slug: clozd-programs-program-id-deals-deal-id-api
- description: The /programs/:program_id/deals/import API from Clozd — 1 operation(s) for /programs/:program_id/deals/import.
  name: Clozd /programs/:program Id/deals/import API
  slug: clozd-programs-program-id-deals-import-api
- description: The /programs/:program_id/touchpoints API from Clozd — 1 operation(s) for /programs/:program_id/touchpoints.
  name: Clozd /programs/:program Id/touchpoints API
  slug: clozd-programs-program-id-touchpoints-api
- description: The /programs/:program_id/touchpoints/:touchpoint_id API from Clozd — 1 operation(s) for /programs/:program_id/touchpoints/:touchpoint_id.
  name: Clozd /programs/:program Id/touchpoints/:touchpoint ID API
  slug: clozd-programs-program-id-touchpoints-touchpoint-id-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clozd Data /programs /programs API
  slug: open-clozd-programs-api
- collection_type: open
  name: Clozd Data /programs/:program Id/competitors /programs/:program Id/competitors API
  slug: open-clozd-programs-program-id-competitors-api
- collection_type: open
  name: Clozd /programs/:program Id/deals /programs/:program Id/deals API
  slug: open-clozd-programs-program-id-deals-api
- collection_type: open
  name: Clozd /programs/:program Id/deals/:deal ID /programs/:program Id/deals/:deal ID API
  slug: open-clozd-programs-program-id-deals-deal-id-api
- collection_type: open
  name: Clozd Data /programs/:program Id/deals/import /programs/:program Id/deals/import API
  slug: open-clozd-programs-program-id-deals-import-api
- collection_type: open
  name: Clozd Data /programs/:program Id/touchpoints /programs/:program Id/touchpoints API
  slug: open-clozd-programs-program-id-touchpoints-api
- collection_type: open
  name: Clozd Data /programs/:program Id/touchpoints/:touchpoint ID /programs/:program Id/touchpoints/:touchpoint ID API
  slug: open-clozd-programs-program-id-touchpoints-touchpoint-id-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/clozd-data-api-v1-overlay.yaml
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
- group: build
  title: ''
  type: Packages
  url: packages/clozd-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/clozd-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clozd-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/clozd-components.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/clozd-trust-center.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/clozd-data-api-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/clozd-data-api-v3-overlay.yaml
created: '2026-08-02'
description: 'Clozd is a Lehi, Utah based decision-intelligence and win-loss analysis platform that collects structured buyer feedback — through human-led live interviews, AI-assisted Flex interviews, and autonomous Flow interviews — and turns it into decision drivers, competitor sentiment, win rates, and verbatim buyer quotes for sales, marketing, product, and customer-success teams. The platform integrates with Salesforce, HubSpot, Microsoft Dynamics, Gong, Slack, Calendly, Outlook, and Gmail, and exposes two public programmatic surfaces: the versioned Clozd Data API (v1/v2/v3) documented with OpenAPI 3.0.3 and Swagger UI at app.clozd.com for importing deals and participants and exporting programs, deals, touchpoints, responses, transcripts, and competitors; and a hosted, OAuth 2.0 protected Model Context Protocol server at mcp.clozd.com that gives Claude, ChatGPT, Cursor, Copilot, Windsurf, Antigravity, and Gemini CLI direct tool access to the same win-loss data.'
image: https://cdn.prod.website-files.com/602c29edc35660e6c913f956/65a18029f28b360a5bc33674_Group%2011337.png
layout: provider
mcp_servers:
- description: ''
  name: clozd-mcp.yml
  slug: clozd-mcpyml
- description: ''
  name: mcp
  slug: mcp
modified: '2026-08-14'
name: Clozd
nav: Providers
network: true
overview: 'Clozd publishes 7 APIs on the [APIs.io](https://apis.io/) network, including /programs API, /programs/:program Id/competitors API, /programs/:program Id/deals API, and 4 more. Tagged areas include win-loss-analysis, customer-feedback, decision-intelligence, sales-intelligence, and market-research.


  Clozd''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 31 more developer resources.'
plans:
- name: Clozd Plans Pricing
  plan_count: 0
  slug: clozd-plans-pricing
random_paper: 93
rate_limits:
- limit_count: 0
  name: Clozd Rate Limits
  slug: clozd-rate-limits
scopes:
- name: Clozd Scopes
  scope_count: 5
  slug: clozd-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: developing
  composite: 50.3
  delta: -0.7
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 30.3
    contract_quality: 61.3
    developer_ergonomics: 58.9
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 2.6
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clozd/refs/heads/main/screenshots/clozd-2026-08-07T163518.png
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
