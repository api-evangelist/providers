---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
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
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 33.1
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Matchory Discovery API exposes the resolved-and-enriched supplier data layer — verified supplier profiles, MatchoryID identity resolution, portfolio consolidation, risk signals, and market intelli
  name: Matchory Discovery API
  slug: matchory-discovery-api
artifact_total: 9
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
- group: build
  title: ''
  type: Packages
  url: packages/matchory-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/matchory-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/matchory-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/matchory-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/matchory-conventions.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/matchory-robots.txt
- group: company
  title: ''
  type: Blog
  url: https://matchory.com/en/newsroom
- group: operate
  title: ''
  type: Support
  url: https://matchory.com/en/contact-us
coverage:
  checked: '2026-08-14'
  detail: Matchory markets a REST API, a GraphQL endpoint, webhooks and a first-party MCP server on matchory.com/en/technology, but the developer reference and every machine-readable contract live inside the authenticated discovery.matchory.com tenant — MCP tools/list returns HTTP 401 invalid_token, no OpenAPI exists on any host, and the advertised GraphQL endpoint has no publicly reachable location (POST /graphql answers 405 from the SPA catch-all).
  evidence:
  - status: 401
    url: https://discovery.matchory.com/mcp
  - status: 404
    url: https://api.matchory.com/openapi.json
  - status: 404
    url: https://matchory.com/openapi.json
  - status: 405
    url: https://discovery.matchory.com/graphql
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Matchory (Matchory GmbH) is a Munich-based supplier data platform for enterprise procurement. It resolves fragmented, duplicated supplier records from spreadsheets and ERP systems into a single stable identity — the MatchoryID — with 90%+ accuracy, then continuously enriches each supplier with verified profiles, market intelligence, and five-dimension risk signals (financial, country, supply-chain, compliance, ESG) drawn from a database of 15M+ verified global suppliers. Procurement teams and AI agents reach the data through a web UI, a REST/GraphQL API, webhooks, and a first-party OAuth-protected Model Context Protocol (MCP) server, letting assistants such as Claude and Microsoft Copilot ground answers in source-traceable, confidence-scored supplier data. The platform is EU-sovereign — hosted in Germany, GDPR-compliant, and ISO 27001 certified — and is used by enterprise procurement organizations including Bosch, Kärcher, Deutsche Bahn, E.ON, DMG Mori, and Trumpf.
image: https://cdn.prod.website-files.com/6784f7971856e0304b40e3de/679028bece9dccdfc4e67c4e_favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: Matchory MCP Server
  slug: matchory-mcp-server
- description: First-party, remote Model Context Protocol server exposing Matchory's resolved-and-enriched supplier intelligence layer (verified supplier profiles, MatchoryID identity resolution, risk signals, portf
  name: Matchory MCP Server
  slug: matchory-mcp-server-2
modified: '2026-08-14'
name: Matchory
nav: Providers
network: true
overview: 'Matchory publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Procurement, Supplier Discovery, Sourcing, and Supply Chain.


  The Matchory catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Matchory''s developer surface includes documentation, signup flow, pricing, authentication, engineering blog, support, and 21 more developer resources.'
plans:
- name: Matchory Plans Pricing
  plan_count: 3
  slug: matchory-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Matchory Rate Limits
  slug: matchory-rate-limits
scopes:
- name: Matchory Scopes
  scope_count: 4
  slug: matchory-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 14
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 46.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
