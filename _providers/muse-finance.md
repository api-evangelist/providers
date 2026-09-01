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
  band: agent-aware
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Embedded-finance REST API for submitting and converting leads, managing finance applications and agreements, funds requests and credit-backed offers. Authenticated with a JWT bearer token plus an x-ap
  name: Muse Finance API
  slug: muse-finance-api
artifact_total: 6
asyncapis:
- description: ''
  name: Muse Finance Webhooks
  slug: muse-finance-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://getmymuse.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://muse-portal-prod.portal.getmymuse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.getmymuse.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://cdn-live.funding-systems.com/api-documents/finance-api/swagger.html
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.getmymuse.com/docs/getting-started
- group: start
  title: ''
  type: Login
  url: https://muse-portal-prod.portal.getmymuse.com/
- group: operate
  title: ''
  type: Support
  url: mailto:technical-support@getmymuse.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/muse-finance-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/muse-finance-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/muse-finance-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/muse-finance-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/muse-finance-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/muse-finance-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/muse-finance-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/muse-finance-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/muse-finance-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/muse-finance-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/muse-finance-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/muse-finance-domain-security.yml
created: '2026-07-17'
description: Muse Finance is a UK embedded-finance platform (Muse Finance Limited, London & Hastings) providing modular working-capital infrastructure — invoice finance, trade finance and supply finance — that lenders, originators, foreign-exchange providers and payment platforms integrate as a white-label product or via a REST API. The Muse Finance API lets partners submit and convert leads, manage finance applications and agreements, raise funds requests, submit exchange rates, and handle credit-backed offers, with JWT + API-key authentication and webhook or polling event notifications. Backed by Techstars.
image: https://getmymuse.com/favicon-96x96.png
layout: provider
mcp_servers:
- description: Candidate MCP tool list for the Muse Finance embedded-finance API, one tool per documented operation. Not an official Muse server.
  name: Muse Finance MCP Server
  slug: muse-finance-mcp-server
modified: '2026-07-20'
name: Muse Finance
nav: Providers
network: true
overview: 'Muse Finance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Embedded Finance, Invoice Finance, Trade Finance, and Lending.


  The Muse Finance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Muse Finance''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, and 13 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 1
  name: Muse Finance Rate Limits
  slug: muse-finance-rate-limits
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 13
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 42.7
    developer_ergonomics: 54.8
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 37.3
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/muse-finance/refs/heads/main/screenshots/muse-finance-2026-08-07T184450.png
security:
- kind: authentication
  name: Muse Finance Authentication
  slug: muse-finance-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Muse Finance Domain Security
  slug: muse-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: muse-finance
tags:
- Company
- Embedded Finance
- Invoice Finance
- Trade Finance
- Lending
- Fintech
- Working Capital
- United Kingdom
website: https://getmymuse.com/
---
