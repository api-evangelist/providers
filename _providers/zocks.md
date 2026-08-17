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
  band: agent-aware
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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.zocks.io
- group: docs
  title: ''
  type: Documentation
  url: https://help.zocks.io/en/
- group: operate
  title: ''
  type: Support
  url: https://help.zocks.io/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://academy.zocks.io/
- group: company
  title: ''
  type: Blog
  url: https://www.zocks.io/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zocks.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.zocks.io/signup
- group: start
  title: ''
  type: Login
  url: https://console.zocks.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zocks.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zocks.io/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zocks-mcp.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.zocks.io/security
- group: design
  title: ''
  type: Conformance
  url: conformance/zocks-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zocks-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zocks-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zocks-llms.txt
created: '2026-07-17'
description: 'Zocks is an AI assistant for financial advisors that captures client conversations and automates the administrative side of advice — meeting note-taking with speaker attribution, meeting preparation, intake and account form filling, client email drafting, document intelligence, and centralized client/household profiles. Captured client intelligence syncs across CRM and wealth-management systems including Wealthbox, HubSpot, Salesforce, Redtail, Practifi, eMoney, and Orion, with Zoom and Google Meet as meeting sources. Rather than a public REST API, Zocks exposes this intelligence to AI tools through an official hosted MCP server secured with OAuth 2.0 over Streamable HTTP, installable as a connector in Claude, ChatGPT, and Microsoft Copilot with tool-call-level audit logging. The company is SOC 2 Type 2 certified and was surfaced as a portfolio company of QED Investors. Sector: fintech / wealthtech.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zocks.png
layout: provider
mcp_servers:
- description: ''
  name: zocks-mcp.yml
  slug: zocks-mcpyml
modified: '2026-07-21'
name: Zocks
nav: Providers
network: true
overview: 'Zocks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Wealthtech, Financial Advisors, and Artificial Intelligence.


  Zocks'' developer surface includes documentation, support, getting-started guide, engineering blog, pricing, signup flow, and 10 more developer resources.'
random_paper: 107
score:
  band: emerging
  composite: 24.7
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 24.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Zocks Domain Security
  slug: zocks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zocks
tags:
- Company
- Fintech
- Wealthtech
- Financial Advisors
- Artificial Intelligence
- MCP
- Meeting Intelligence
- CRM
website: https://www.zocks.io
---
