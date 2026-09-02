---
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.6
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Kleio platform API, served from api.kleio.ai behind a Google Cloud API Gateway and protected by OAuth 2.0 authorization-code + PKCE against an Auth0 tenant at auth.kleio.ai. Kleio publishes no pub
  name: Kleio Platform API
  slug: kleio-platform
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.kleio.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.kleio.ai/news
- group: operate
  title: ''
  type: Support
  url: https://www.kleio.ai/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kleio.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kleio.ai/acceptable-use-policy
- group: auth
  title: ''
  type: Security
  url: https://www.kleio.ai/security-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kleioai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kleio-ai
- group: company
  title: ''
  type: Twitter
  url: https://x.com/kleio_ai
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kleio-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kleio-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kleio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kleio-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kleio-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kleio-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kleio-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kleio-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kleio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kleio-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/kleio-packages.yml
coverage:
  checked: '2026-08-17'
  detail: Kleio runs a real OAuth-protected platform API at api.kleio.ai — its Google Cloud API Gateway serves RFC 8414 authorization-server metadata naming an Auth0 issuer and a defined dynamic client registration route — but publishes no developer portal, API reference, OpenAPI or auth guide anywhere, and kleio.ai/pricing and kleio.ai/docs both 404, so the only route to the API is the "Request a Demo" form at kleio.ai/contact.
  evidence:
  - status: 200
    url: https://api.kleio.ai/.well-known/oauth-authorization-server
  - status: 405
    url: https://api.kleio.ai/api/oauth/register
  - status: 404
    url: https://api.kleio.ai/openapi.json
  - status: 404
    url: https://www.kleio.ai/docs
  - status: 404
    url: https://www.kleio.ai/pricing
  - status: 200
    url: https://www.kleio.ai/contact
  reason: sales-gate
  state: gated
created: '2026-08-17'
description: 'Kleio is a Paris-headquartered agentic commerce platform for complex, high-value enterprise sales, founded in 2024 by Adrien Mathieu, Philippe Wellens and Louis Poirier and backed by a EUR 3M seed round. The platform pairs a domain-specific Knowledge Engine — a continuously updated representation of a company''s catalog, pricing, business rules and ontologies — with a stack of orchestrated AI agents tuned for each stage of the sales funnel: discovery agents for intent qualification, product-guidance agents that reason over the catalog, quoting agents wired to configurators and pricing, and a Live Sales Copilot that augments human advisors in real time. Kleio deploys across web widgets, advisor desktops and third-party AI surfaces such as ChatGPT and Gemini via MCP/UCP integrations, with CRM and catalog write-back to Salesforce, HubSpot and custom systems. Named customers include Selectour, Havas Voyages, Showroomprive, Altarea Cogedim, Orpi and Emil Frey, across travel, real
  estate, automotive, wholesale, insurance, manufacturing and energy. Kleio publishes no public developer portal, API reference or OpenAPI: the platform API at api.kleio.ai is an OAuth-protected Google Cloud API Gateway reachable only to customers, and access begins with a sales conversation.'
image: https://cdn.prod.website-files.com/67b32cd10cd0c67b686078c2/67c06a31d5ccb4402746c01b_logo-circle-32x32.png
layout: provider
modified: '2026-08-17'
name: Kleio
nav: Providers
network: true
overview: 'Kleio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Data, Agentic Commerce, AI Agents, and Enterprise Sales.


  Kleio''s developer surface includes engineering blog, support, authentication, and 17 more developer resources.'
plans:
- name: Kleio Plans Pricing
  plan_count: 0
  slug: kleio-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Kleio Rate Limits
  slug: kleio-rate-limits
scopes:
- name: Kleio Scopes
  scope_count: 14
  slug: kleio-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 19.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Kleio Authentication
  slug: kleio-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Kleio Domain Security
  slug: kleio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kleio
tags:
- Company
- Ai Data
- Agentic Commerce
- AI Agents
- Enterprise Sales
- Conversational AI
- Knowledge Engine
- MCP
- Agent-to-Agent
- Retail
- Travel
- Real-Estate
- Automotive
- France
website: https://www.kleio.ai/
---
