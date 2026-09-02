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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-09-01'
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
  name: Zocks
  slug: zocks
modified: '2026-07-21'
name: Zocks
nav: Providers
network: true
overview: 'Zocks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, WealthTech, Financial Advisors, and Artificial Intelligence.


  Zocks'' developer surface includes documentation, support, getting-started guide, engineering blog, pricing, signup flow, and 10 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 22.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- WealthTech
- Financial Advisors
- Artificial Intelligence
- MCP
- Meeting Intelligence
- CRM
website: https://www.zocks.io
---
