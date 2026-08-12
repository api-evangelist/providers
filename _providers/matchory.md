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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: The Matchory Discovery API exposes the resolved-and-enriched supplier data layer — verified supplier profiles, MatchoryID identity resolution, portfolio consolidation, risk signals, and market intelli
  name: Matchory Discovery API
  slug: matchory-discovery-api
artifact_total: 7
asyncapis:
- description: ''
  name: Matchory Webhooks
  slug: matchory-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matchory-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://matchory.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://matchory.com/en/technology
- group: docs
  title: ''
  type: Documentation
  url: https://matchory.com/en/mcp
- group: start
  title: ''
  type: Login
  url: https://discovery.matchory.com/auth/signin
- group: start
  title: ''
  type: SignUp
  url: https://matchory.com/en/book-a-demo
- group: commercial
  title: ''
  type: Pricing
  url: https://matchory.com/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://matchory.com/en/gtc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://matchory.com/en/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/matchory
- group: agent
  title: ''
  type: MCPServer
  url: mcp/matchory-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/matchory-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/matchory-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/matchory-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/matchory-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/matchory-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/matchory-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://matchory.com/en/technology
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/matchory-llms.txt
created: '2026-07-17'
description: Matchory (Matchory GmbH) is a Munich-based supplier data platform for enterprise procurement. It resolves fragmented, duplicated supplier records from spreadsheets and ERP systems into a single stable identity — the MatchoryID — with 90%+ accuracy, then continuously enriches each supplier with verified profiles, market intelligence, and five-dimension risk signals (financial, country, supply-chain, compliance, ESG) drawn from a database of 15M+ verified global suppliers. Procurement teams and AI agents reach the data through a web UI, a REST/GraphQL API, webhooks, and a first-party OAuth-protected Model Context Protocol (MCP) server, letting assistants such as Claude and Microsoft Copilot ground answers in source-traceable, confidence-scored supplier data. The platform is EU-sovereign — hosted in Germany, GDPR-compliant, and ISO 27001 certified — and is used by enterprise procurement organizations including Bosch, Kärcher, Deutsche Bahn, E.ON, DMG Mori, and Trumpf.
image: https://cdn.prod.website-files.com/6784f7971856e0304b40e3de/679028bece9dccdfc4e67c4e_favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: mcp
  slug: mcp
- description: ''
  name: matchory-mcp.yml
  slug: matchory-mcpyml
modified: '2026-07-20'
name: Matchory
nav: Providers
network: true
overview: 'Matchory publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Procurement, Supplier Discovery, Sourcing, and Supply Chain.


  The Matchory catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Matchory''s developer surface includes documentation, signup flow, pricing, authentication, and 15 more developer resources.'
random_paper: 59
scopes:
- name: Matchory Scopes
  scope_count: 4
  slug: matchory-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 41.6
  delta: -1.1
  facets:
    commercial_clarity: 52.6
    contract_quality: 51.6
    developer_ergonomics: 37.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 13.2
  previous_composite: 42.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matchory/refs/heads/main/screenshots/matchory-2026-07-25T230348.png
security:
- kind: authentication
  name: Matchory Authentication
  slug: matchory-authentication
  summary_line: oauth2/openIdConnect/apiKey/saml · 4 schemes
- kind: domain-security
  name: Matchory Domain Security
  slug: matchory-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: matchory
tags:
- Company
- Procurement
- Supplier Discovery
- Sourcing
- Supply Chain
- Data Enrichment
- Entity Resolution
- Market Intelligence
- Risk Management
- MCP
website: https://matchory.com
---
